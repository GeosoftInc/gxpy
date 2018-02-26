"""
Geosoft grid and image utilities.

.. seealso:: `geosoft.gxpy.grid`, `geosoft.gxapi.GXIMG`, `geosoft.gxapi.GXIMU`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_grid_utility.py>`_
    
"""
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import vv as gxvv
from . import grid as gxgrd
from . import map as gxmap
from . import view as gxv
from . import group as gxgrp
from . import gdb as gxgdb
from . import geometry as gxgeo
from . import utility as gxu
from . import geometry_utility as gxgeou

__version__ = geosoft.__version__

BOOL_AND = gxapi.IMU_BOOL_OPT_AND  #:
BOOL_OR = gxapi.IMU_BOOL_OPT_OR  #:
BOOL_XOR = gxapi.IMU_BOOL_OPT_XOR  #:
BOOL_SIZE_GRID1 = gxapi.IMU_BOOL_SIZING_0  #:
BOOL_SIZE_GRID2 = gxapi.IMU_BOOL_SIZING_1  #:
BOOL_SIZE_MIN = gxapi.IMU_BOOL_SIZING_MIN  #:
BOOL_SIZE_MAX = gxapi.IMU_BOOL_SIZING_MAX  #:
BOOL_OVERLAP_AVERAGE = gxapi.IMU_BOOL_OLAP_AVE  #:
BOOL_OVERLAP_GRID1 = gxapi.IMU_BOOL_OLAP_1  #:
BOOL_OVERLAP_GRID2 = gxapi.IMU_BOOL_OLAP_2  #:

TREND_EDGE = gxapi.IMU_TREND_EDGE  #:
TREND_ALL = gxapi.IMU_TREND_ALL  #:
DERIVATIVE_X = 0  #:
DERIVATIVE_Y = 1  #:
DERIVATIVE_Z = 2  #:
DERIVATIVE_ANALYTIC_SIGNAL = 3  #:
DERIVATIVE_TILT = 4  #:


def _t(s):
    return geosoft.gxpy.system.translate(s)


class GridUtilityException(Exception):
    """
    Exceptions from `geosoft.gxpy.grid_utility`.

    .. versionadded:: 9.4
    """
    pass


def remove_trend(grid, file_name=None, method=TREND_EDGE, overwrite=False):
    """
    Calculate a polynomial trend surface and return trend-removed grid.

    :param grid:        `geosoft.gxpy.grid.Grid` instance, or a file name
    :param file_name:   trend-removed grid file name, if None a temporary grid is created.
    :param method:      base trend on TREND_EDGE for edge data or TREND_ALL for all data
    :param overwrite:   True to overwrite existing file_name
    :return:            `Grid` instance
    
    .. versionadded 9.4
    """

    if not isinstance(grid, gxgrd.Grid):
        grid = gxgrd.Grid.open(grid, dtype=np.float64, mode=gxgrd.FILE_READ)

    # need GS_DOUBLE grids
    if grid.gxtype != gxapi.GS_DOUBLE:
        ing = grid.copy(grid, gx.gx().temp_file('.grd(GRD)'), dtype=np.float64)
        ing.delete_files()
    else:
        ing = grid

    if file_name is None:
        file_name = gx.gx().temp_file('.grd(GRD)')
    dtg = grid.new(file_name=file_name, properties=ing.properties(), overwrite=overwrite)
    gxapi.GXIMU.grid_trnd(ing.gximg, dtg.gximg, 0, method, 1,
                          gxapi.GXVM.create(gxapi.GS_REAL, 10), 3)
    return dtg


def derivative(grid, derivative_type, file_name=None, overwrite=False):
    """
    Return a derivative of a grid.  Derivatives are calculated by space-domain convolution.

    :param grid:            `geosoft.gxpy.grid.Grid` instance, or a file name
    :param derivative_type:  Which derivative to calculate:
    
        ========================== ====================================================================
        DERIVATIVE_X               in the grid X direction
        DERIVATIVE_Y               in the grid Y direction
        DERIVATIVE_Z               in the grid Z direction
        DERIVATIVE_ANALYTIC_SIGNAL analytic signal, or the total derivative sqrt(dx**2 + dy**2 + dz**2)
        DERIVATIVE_TILT            tilt derivative, atan2(dz, sqrt(dx**2, dy**2))
        ========================== ====================================================================
    
    :param file_name:   returned derivative file name, None for a temporary file
    :param overwrite:   True to overwrite existing file
    :return:            `Grid` instance that contains the derivative result

    .. versionadded 9.4
    """

    def vertical_derivative(g):

        # float64 grids for grid_vd
        if not isinstance(g, gxgrd.Grid):
            g = gxgrd.Grid.open(g, dtype=np.float64, mode=gxgrd.FILE_READ)
        _dtype = g.dtype
        if g.dtype != np.float64:
            g = g.copy(g, gx.gx().temp_file('.grd(GRD)'), dtype=np.float32, overwrite=True)
            g.delete_files()

        dzg = gxgrd.Grid.new(file_name=file_name, properties=g.properties(), overwrite=overwrite)
        gxapi.GXIMU.grid_vd(g.gximg, dzg.gximg)
        return gxgrd.reopen(dzg, dtype=_dtype)

    def tilt_derivative(g):
        dx = derivative(g, DERIVATIVE_X)
        dy = derivative(g, DERIVATIVE_Y)
        dz = derivative(g, DERIVATIVE_Z)
        return gxgrd.expression((dx, dy, dz), 'atan2(g3,sqrt(g1**2+g2**2))', 
                                result_file_name=file_name,
                                overwrite=overwrite)

    def analytic_signal(g):
        dx = derivative(g, DERIVATIVE_X)
        dy = derivative(g, DERIVATIVE_Y)
        dz = derivative(g, DERIVATIVE_Z)
        return gxgrd.expression((dx, dy, dz), 'sqrt(g1**2+g2**2)', 
                                result_file_name=file_name,
                                overwrite=overwrite)

    # temp file_name
    if file_name is None:
        file_name = gx.gx().temp_file('.grd(GRD)')

    if derivative_type == DERIVATIVE_Z:
        return vertical_derivative(grid)

    # need float32 grids for grid_filt
    if not isinstance(grid, gxgrd.Grid):
        grid = gxgrd.Grid.open(grid, dtype=np.float32, mode=gxgrd.FILE_READ)
    return_dtype = grid.dtype
    if grid.dtype != np.float32:
        grid = grid.copy(grid, gx.gx().temp_file('.grd(GRD)'), dtype=np.float32, overwrite=True)
        grid.delete_files()

    if derivative_type == DERIVATIVE_ANALYTIC_SIGNAL:
        rgrd = analytic_signal(grid)
        if rgrd.dtype != return_dtype:
            return gxgrd.reopen(rgrd, dtype=return_dtype)

    if derivative_type == DERIVATIVE_TILT:
        rgrd = tilt_derivative(grid)
        if rgrd.dtype != return_dtype:
            return gxgrd.reopen(rgrd, dtype=return_dtype)

    # dxy grid
    if file_name is None:
        file_name = gx.gx().temp_file('.grd(GRD)')
    dxy = gxgrd.Grid.new(file_name=file_name, properties=grid.properties(), overwrite=overwrite)

    # filter
    if derivative_type == DERIVATIVE_X:
        filter_vv = gxvv.GXvv([0., 0., 0., -0.5, 0., +0.5, 0., 0., 0.], dtype=np.float64)
    else:
        filter_vv = gxvv.GXvv([0., 0.5, 0., 0., 0., 0., 0., -0.5, 0.], dtype=np.float64)
    gxapi.GXIMU.grid_filt(grid.gximg, dxy.gximg,
                          1, 1.0,
                          gxapi.IMU_FILT_DUMMY_NO,
                          gxapi.IMU_FILT_HZDRV_NO,
                          gxapi.IMU_FILT_FILE_NO,
                          "",
                          filter_vv.gxvv)

    return gxgrd.reopen(dxy, dtype=return_dtype)


def grid_mosaic(mosaic, grid_list, type_decorate='', report=None):
    """
    Combine a set of grids into a single grid.  Raises an error if the resulting grid is too large.

    :param mosaic:          name of the output grid, returned.  Decorate with '(HGD)' to get an HGD
    :param grid_list:       list of input grid names
    :param type_decorate:   decoration for input grids if not default
    :param report:          string reporting function, report=print to print progress
    :returns:               'geosoft.gxpy.grid.Grid` instance

    .. versionadded:: 9.4
    """

    def props(gn, repro=None):
        with gxgrd.Grid.open(gn) as gg:
            if repro:
                gg.gximg.create_projected2(repro[0], repro[1])
            return gg.properties()

    def dimension(glist):

        def dimg(_gd, _rep=None):
            prp = props(_gd, _rep)
            _x0 = prp.get('x0')
            _y0 = prp.get('y0')
            _xm = _x0 + (prp.get('nx') - 1) * prp.get('dx')
            _ym = _y0 + (prp.get('ny') - 1) * prp.get('dy')
            _ipj = prp.get('coordinate_system').gxipj
            cell = prp.get('dx')
            return _x0, _y0, _xm, _ym, (_ipj, cell)

        def ndim(_x0, _xm, _dx):
            return int((_xm - _x0 + _dx / 2.0) / _dx) + 1

        dx0, dy0, dxm, dym, drepro = dimg(glist[0])
        for gd in glist[1:]:
            xx0, yy0, xxm, yym, r = dimg(gd, drepro)
            if xx0 < dx0:
                dx0 = xx0
            if yy0 < dy0:
                dy0 = yy0
            if xxm > dxm:
                dxm = xxm
            if yym > dym:
                dym = yym

        # calculate new grid dimension
        _p = props(glist[0])
        nnx = ndim(dx0, dxm, _p.get('dx'))
        nny = ndim(dy0, dym, _p.get('dy'))

        return dx0, dy0, nnx, nny, dxm, dym

    def locate(_x0, _y0, _p):

        _dx = _p.get('dx')
        _dy = _p.get('dy')
        dsx = round((p.get('x0') - _x0) / _dx)
        dsy = round((p.get('y0') - _y0) / _dy)

        return dsx, dsy

    def paste(gn, _mpg):
        with gxgrd.Grid.open(gn) as _g:
            _p = _g.properties()
            _nx = _p.get('nx')
            _ny = _p.get('ny')
            gpg = _g.gxpg()
            destx, desty = locate(x0, y0, _p)
            if report:
                report('    +{} nx,ny({},{})'.format(_g, _nx, _ny))
                report('     Copy ({},{}) -> ({},{}) of ({},{})'.format(_nx, _ny, destx, desty, mnx, mny))
            _mpg.copy_subset(gpg, desty, destx, 0, 0, _ny, _nx)
            return

    if len(grid_list) == 0:
        raise GridUtilityException(_t('At least one grid is required'))

    # create list of grids, all matching on coordinate system of first grid
    grids = []
    for i in range(len(grid_list)):
        grids.append(gxgrd.decorate_name(grid_list[i], type_decorate))

    # output grid
    x0, y0, nx, ny, xm, ym = dimension(grids)
    p = props(grids[0])
    p['x0'] = x0
    p['y0'] = y0
    p['nx'] = nx
    p['ny'] = ny
    if report is not None:
        report('')
        report('Mosaic: dim({},{}) x({},{}) y({},{}), cell({})...'.format(nx, ny, x0, xm, y0, ym, p.get('dx')))
    master = gxgrd.Grid.new(mosaic, p)
    if report:
        report('Memory image ready ({}) dim({},{}) x0,y0({},{})'.format(master, master.nx, master.ny,
                                                                        master.x0, master.y0))

    # paste grids onto master
    mnx = master.nx
    mny = master.ny
    mpg = master.gxpg()
    for g in grids:
        paste(g, mpg)

    if report:
        report('Mosaic completed: {}'.format(mosaic))

    return master


def grid_bool(g1, g2, joined_grid, opt=1, size=3, olap=1):
    """

    :param g1:          Grids to merge
    :param g2:
    :param joined_grid: joined output grid name, overwritten if it exists
    :param opt:         option logic to determine output grid points:

        =============== =========================
        BOOL_AND        dummy unless g1 and g2
        BOOL_OR         dummy unless g1 or g2
        BOOL_XOR        dummy where g1 and g2
        =============== =========================

    :param size:    size of the output grid, default is minimum size

        =============== =======================================
        BOOL_SIZE_GRID1 output size matches g1
        BOOL_SIZE_GRID2 output size matches g2
        BOOL_SIZE_MIN   output size minimised to non-dummy area
        BOOL_SIZE_MAX   output size g1 + g2:
        =============== =======================================

    :param olap:    what to do with overlapping valid points, default uses grid 1

        ==================== ==================================
        BOOL_OVERLAP_AVERAGE averave values where grid overlap
        BOOL_OVERLAP_GRID1   use g1 where grids overlap
        BOOL_OVERLAP_GRID2   use g2 where grids overlap
        ==================== ==================================

    :returns:       `Grid` instance of the merged output grid, must be closed with a call to close().

    .. versionadded:: 9.4
    """

    close_g1 = close_g2 = False
    if isinstance(g1, str):
        g1 = gxgrd.Grid.open(g1)
        close_g1 = True
    if isinstance(g2, str):
        g2 = gxgrd.Grid.open(g2)
        close_g2 = True

    gxapi.GXIMU.grid_bool(g1.gximg, g2.gximg, joined_grid, opt, size, olap)

    if close_g1:
        g1.close()
    if close_g2:
        g2.close()

    return gxgrd.Grid.open(joined_grid)

def contour_points(grid, value, max_segments=1000, interval=None):
    """
    Return a set of point segments that represent the spatial locations of contours threaded through the grid.

    Contours through oriented grids will be oriented in 3D. Grids that are not oriented will have a z value
    0.0.

    :param grid:            grid file of `geosoft.gxpy.grid.Grid` instance
    :param value:           contour value
    :param max_segments:    maximum expected number of segments, raises error if there are more actual segments.
    :param interval:        the separation between points along the contours. If not specified the minimum grid
                            cell size is used.  For `interval=0`, the points are as returned by the contouring
                            algorithm.
    :return:                list of `geosoft.gxpy.geometry.PPoint`, where each item in the list represents
                            one continuous contour from the grid.

    .. versionadded:: 9.4
    """

    if isinstance(grid, gxgrd.Grid):
        extent = grid.extent
        with grid.copy(grid) as g:
            temp_grid = g.file_name
            grid = g.file_name_decorated
            if interval is None:
                interval = min(g.dx, g.dy)

    else:
        with gxgrd.Grid.open(grid) as g:
            extent = g.extent
            if interval is None:
                interval = min(g.dx, g.dy)
        temp_grid = None

    # create a contour group for this value, export to a shape file
    with gxmap.Map.new(data_area=extent.extent_xy) as gmap:
        map_file = gmap.file_name
        with gxv.View.open(gmap, "data") as v:
            gxgrp.contour(v, '_', grid, parameters=(',0,0', '', '', '', '', '1',
                                                    str(value) + ',,,0'))
        shp_file = gx.gx().temp_file('shp')
        gmap.gxmap.export_all_in_view(shp_file, 'data', 1.0, 1.0,
                                      gxapi.MAP_EXPORT_BITS_24,
                                      gxapi.MAP_EXPORT_METHOD_STANDARD,
                                      gxapi.MAP_EXPORT_FORMAT_SHP, '')
        shp_file = shp_file[:-4] + '_lnz.shp'

    # import shape into a temporary database
    gis = gxapi.GXGIS.create(shp_file, '', gxapi.GIS_TYPE_ARCVIEW)
    with gxgdb.Geosoft_gdb.new(max_lines=max_segments, max_channels=10) as gdb:
        gdb_file = gdb.file_name
        gis.load_shapes_gdb(gdb.gxdb)

        # make points from segments
        pplist = []
        for l in gdb.lines():
            xyz = gdb.read_line(l, channels=('X', 'Y', 'Z'))[0]
            xyz[:, 2] = 0.
            if interval > 0.:
                xyz = gxgeou.resample(xyz, interval)
            if extent.coordinate_system.is_oriented:
                xyz = extent.coordinate_system.xyz_from_oriented(xyz)
            pplist.append(gxgeo.PPoint(xyz, coordinate_system=extent.coordinate_system))

    # discard the temp files
    gxu.delete_files_by_root(temp_grid)
    gxu.delete_files_by_root(map_file)
    gxu.delete_files_by_root(gdb_file)
    gxu.delete_files_by_root(shp_file[:-4])

    return pplist
