"""
Geosoft grid and image utilities.

.. seealso:: `geosoft.gxpy.grid`, `geosoft.gxapi.GXIMG`, `geosoft.gxapi.GXIMU`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_grid_utility.py>`_
    
"""
import os
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
from . import coordinate_system as gxcs

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
DERIVATIVE_XY = 3  #: horizontal gradient sqrt(dx**2 + dy**2)
DERIVATIVE_XYZ = 4  #: total gradient (analytic signal) sqrt(dx**2 _ dy**2 + dz**2)
TILT_ANGLE = 5  #: radians, atan(d_z/d_xy), Miller and Singh, 1994
RETURN_PPOINT = 0  #:
RETURN_LIST_OF_PPOINT = 1  #:
RETURN_GDB = 2  #:


def _t(s):
    return geosoft.gxpy.system.translate(s)


class GridUtilityException(geosoft.GXRuntimeError):
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


def derivative(grid, derivative_type, file_name=None, overwrite=False, dtype=None):
    """
    Return a derivative of a grid.  Derivatives are calculated by space-domain convolution.

    :param grid:            `geosoft.gxpy.grid.Grid` instance, or a file name
    :param derivative_type:  Which derivative to calculate:
    
        ========================== ====================================================================
        DERIVATIVE_X               in the grid X direction
        DERIVATIVE_Y               in the grid Y direction
        DERIVATIVE_Z               in the grid Z direction
        DERIVATIVE_XYZ             the total derivative sqrt(dx**2 + dy**2 + dz**2) (analytic signal)
        TILT_ANGLE                 tilt angle, atan2(dz, sqrt(dx**2, dy**2))
        ========================== ====================================================================
    
    :param file_name:   returned derivative file name, None for a temporary file
    :param overwrite:   True to overwrite existing file
    :param dtype:       dtype for the return grid, default is the same as the passed grid.
    :return:            `geosoft.gxpy.grid.Grid` instance that contains the derivative result

    .. versionadded 9.4
    """

    def vertical_derivative(g, dt):

        # float64 grids for grid_vd
        if not isinstance(g, gxgrd.Grid):
            g = gxgrd.Grid.open(g, dtype=np.float64, mode=gxgrd.FILE_READ)

        if g.dtype != np.float64:
            g = g.copy(g, gx.gx().temp_file('.grd(GRD)'), dtype=np.float32, overwrite=True)
            g.delete_files()

        dzg = gxgrd.Grid.new(file_name=file_name, properties=g.properties(), overwrite=overwrite)
        gxapi.GXIMU.grid_vd(g.gximg, dzg.gximg)
        dzg.unit_of_measure = g.unit_of_measure + '/' + g.coordinate_system.unit_of_measure
        return gxgrd.reopen(dzg, dtype=dt)

    def tilt_angle(g, fn=None):
        dx = derivative(g, DERIVATIVE_X)
        dy = derivative(g, DERIVATIVE_Y)
        dz = derivative(g, DERIVATIVE_Z)

        result = gxgrd.expression((dx, dy, dz), 'atan2(g3,sqrt(g1**2+g2**2))',
                                  result_file_name=fn,
                                  overwrite=overwrite)
        result.unit_of_measure = 'radians'
        return gxgrd.reopen(result)

    def horizontal_gradient(g):
        dx = derivative(g, DERIVATIVE_X)
        dy = derivative(g, DERIVATIVE_Y)
        result = gxgrd.expression((dx, dy), 'sqrt(g1**2+g2**2)',
                                  result_file_name=file_name,
                                  overwrite=overwrite)
        result.unit_of_measure = g.unit_of_measure + '/' + g.coordinate_system.unit_of_measure
        return result

    def total_gradient(g):
        dx = derivative(g, DERIVATIVE_X)
        dy = derivative(g, DERIVATIVE_Y)
        dz = derivative(g, DERIVATIVE_Z)
        result = gxgrd.expression((dx, dy, dz), 'sqrt(g1**2+g2**2+g3**2)',
                                  result_file_name=file_name,
                                  overwrite=overwrite)
        result.unit_of_measure = g.unit_of_measure + '/' + g.coordinate_system.unit_of_measure
        return result

    if derivative_type == DERIVATIVE_Z:
        return vertical_derivative(grid, dt=dtype)

    # need float32 grids for grid_filt
    if not isinstance(grid, gxgrd.Grid):
        grid = gxgrd.Grid.open(grid, dtype=np.float32, mode=gxgrd.FILE_READ)

    if dtype is None:
        return_dtype = grid.dtype
    else:
        return_dtype = dtype

    if grid.dtype != np.float32:
        grid = grid.copy(grid, gx.gx().temp_file('.grd(GRD)'), dtype=np.float32, overwrite=True)
        grid.delete_files()

    if derivative_type == DERIVATIVE_XY:
        rgrd = horizontal_gradient(grid)
        if rgrd.dtype != return_dtype:
            return gxgrd.reopen(rgrd, dtype=return_dtype)

    if derivative_type == DERIVATIVE_XYZ:
        rgrd = total_gradient(grid)
        if rgrd.dtype != return_dtype:
            return gxgrd.reopen(rgrd, dtype=return_dtype)

    if derivative_type == TILT_ANGLE:
        if file_name is None:
            file_name = gx.gx().temp_file('.grd(GRD)')
        rgrd = tilt_angle(grid, fn=file_name)
        if rgrd.dtype != return_dtype:
            return gxgrd.reopen(rgrd, dtype=return_dtype)

    # dxy grid
    if file_name is None:
        file_name = gx.gx().temp_file('.grd(GRD)')
    dxy = gxgrd.Grid.new(file_name=file_name, properties=grid.properties(), overwrite=overwrite)

    # filter
    if derivative_type == DERIVATIVE_X:
        filter_vv = gxvv.GXvv([0., 0., 0., -0.5, 0., +0.5, 0., 0., 0.], dtype=np.float64)
        mult = 1.0 / grid.dx
    else:
        filter_vv = gxvv.GXvv([0., 0.5, 0., 0., 0., 0., 0., -0.5, 0.], dtype=np.float64)
        mult = 1.0 / grid.dy
    gxapi.GXIMU.grid_filt(grid.gximg, dxy.gximg,
                          1, mult,
                          gxapi.IMU_FILT_DUMMY_NO,
                          gxapi.IMU_FILT_HZDRV_NO,
                          gxapi.IMU_FILT_FILE_NO,
                          "",
                          filter_vv.gxvv)
    dxy.unit_of_measure = grid.unit_of_measure + '/' + grid.coordinate_system.unit_of_measure
    return gxgrd.reopen(dxy, dtype=return_dtype)


def tilt_depth(grid, resolution=None, return_as=RETURN_PPOINT, gdb=None, overwrite=False, report=None):
    """
    Given an RTP TMI grid, or the vertical derivative of the gravity anomaly, calculate
    contact source depths using the tilt-depth method as suggested by Rick Blakely.
    The contact source depth is the reciprocol of the horizontal gradient of the
    tilt-derivative at the zero-contour of the tilt derivative.

    :param grid:        `geosoft.gxpy.grid.Grid` instance or a grid file name. Ideally the grid should be RTP.
    :param resolution:  zero-contour sampling resolution, defaults to 4 times the grid cell size.
    :param return_as:   return results as:

        ===================== ====================================================================
        RETURN_PPOINT         return results as a single `geosoft.gxpy.geometry.PPoint` instance
        RETURN_LIST_OF_PPOINT return results as a list of `geosoft.gxpy.geometry.PPoint` instances
        RETURN_GDB            return result as a `geosoft.gxpy.gdb.Geosoft_gdb` instance
        ===================== ====================================================================

    :param gdb:         return database name, or a `geosoft.gxpy.gdv.Geosoft_database` instance. If not
                        specified and `return_as=RETURN_GDB`, a temporary database is created.
    :param overwrite:   True to overwrite existing gdb.
    :param report:      reporting function called to report progress. `report=print` to print to console.
    :return:            depends on `return_as` setting

    .. versionadded:: 9.4
    """

    if gdb is not None:
        return_as = RETURN_GDB

    if report:
        report('Calculate tilt-angle...')

    ta = derivative(grid, TILT_ANGLE)
    if report:
        report('Find zero contour of the tilt-angle...')

    if resolution is None:
        resolution = min(ta.dx, ta.dy) * 4.
    gdb = contour_points(ta, 0., resolution=resolution, return_as=RETURN_GDB, gdb=gdb, overwrite=overwrite)
    if report:
        report('Calculate tilt-derivative...')
    tad = derivative(ta, DERIVATIVE_XY)

    # get gradient of the TD at the zero locations
    if report:
        report('Calculate depth = recirocal(tilt-derivative) at zero contour of the tilt-angle...')

    for ln in gdb.list_lines():
        xyz, chlist, fid = gdb.read_line(ln, channels=('X', 'Y', 'Z'))
        zero_tad = sample(tad, xyz)
        zero_tad[zero_tad == 0.] = np.nan
        np.reciprocal(zero_tad, out=zero_tad)
        xyz[:, 2] = zero_tad
        gdb.write_line(ln, xyz, chlist, fid)

    if return_as == RETURN_GDB:
        return gdb

    pplist = []
    for ln in gdb.list_lines():
        xyz = gdb.read_line(ln, channels=('X', 'Y', 'Z'))[0]
        pplist.append(gxgeo.PPoint(xyz, coordinate_system=gdb.coordinate_system))

    gdb.close(discard=True)

    if return_as == RETURN_LIST_OF_PPOINT:
        return pplist

    return gxgeo.PPoint.merge(pplist)


def sample(grid, xyz):
    """
    Return grid values sampled at the point locations.

    :param grid:    `geosoft.gxpy.grid.Grid` instance or a grid file name.
    :param xyz:     `geosoft.gxpy.geometry.PPoint` instance, or a numpy array shapped (-1, 3) that holds
                    the desired (x, y, z) locations. If a PPoint instance is passed it will be reporjected to the
                    grid coordinate system if necessary.
    :return:        1-dimensional numpy array of grid data values that match the passes PPoint or XYZ.
    """

    if not isinstance(grid, gxgrd.Grid):
        grid = gxgrd.Grid(grid, dtype=np.float64)

    if isinstance(xyz, gxgeo.Geometry):
        if xyz.coordinate_system != grid.coordinate_system:
            xyz = gxgeo.PPoint(xyz, coordinate_system=grid.coordinate_system)
        if xyz.coordinate_system.is_oriented:
            xyz = xyz.coordinate_system.oriented_from_xyz(xyz)
        xyz = xyz.pp

    vvx, vvy, vvz = gxvv.vvset_from_np(xyz)
    gxapi.GXIMU.get_zvv(grid.gximg, vvx.gxvv, vvy.gxvv, vvz.gxvv)
    return vvz.np


def grid_mosaic(mosaic, grid_list, type_decorate='', report=None):
    """
    Combine a set of grids into a single grid.  Raises an error if the resulting grid is too large.

    :param mosaic:          name of the output grid, returned.  Decorate with '(HGD)' to get an HGD
    :param grid_list:       list of input grid names
    :param type_decorate:   decoration for input grids if not default
    :param report:          string reporting function, report=print to print progress
    :returns:               `geosoft.gxpy.grid.Grid` instance

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


def contour_points(grid, value, max_segments=1000, resolution=None,
                   return_as=RETURN_LIST_OF_PPOINT, gdb=None, overwrite=False):
    """
    Return a set of point segments that represent the spatial locations of contours threaded through the grid.

    Contours through 3D oriented grids will be oriented in 3D. Grids that are not 3D oriented will have a z value
    0.0.

    :param grid:            grid file of `geosoft.gxpy.grid.Grid` instance
    :param value:           contour value
    :param max_segments:    maximum expected number of segments, raises error if there are more actual segments.
    :param resolution:      the separation between points along the contours. If not specified the minimum
                            grid cell size is used.  Set `resolution=0`, for use the locations as returned by the
                            contouring algorithm.
    :param return_as:       return results as:

        ===================== ====================================================================
        RETURN_PPOINT         return results as a single `geosoft.gxpy.geometry.PPoint` instance
        RETURN_LIST_OF_PPOINT return results as a list of `geosoft.gxpy.geometry.PPoint` instances
        RETURN_GDB            return result as a `geosoft.gxpy.gdb.Geosoft_gdb` instance
        ===================== ====================================================================

    :param gdb:         return database name, or a `geosoft.gxpy.gdv.Geosoft_database` instance. If not
                        specified and `return_as=RETURN_GDB`, a temporary database is created.
    :return:            depends on `return_as` setting

    .. versionadded:: 9.4
    """

    if isinstance(grid, gxgrd.Grid):
        extent = grid.extent
        with grid.copy(grid) as g:
            temp_grid = g.file_name
            grid = g.file_name_decorated
            if resolution is None:
                resolution = min(g.dx, g.dy)

    else:
        with gxgrd.Grid.open(grid) as g:
            extent = g.extent
            if resolution is None:
                resolution = min(g.dx, g.dy)
        temp_grid = None

    # create a contour group for this value, export to a shape file
    with gxmap.Map.new(data_area=extent.extent_xy, overwrite=True) as gmap:
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

    if not os.path.exists(shp_file):
        raise GridUtilityException(_t('The grid data does not intersect value {}').format(value))

    if gdb is not None:
        return_as = RETURN_GDB

    # import shape to database
    if not isinstance(gdb, gxgdb.Geosoft_gdb):
        gdb = gxgdb.Geosoft_gdb.new(name=gdb, max_lines=max_segments, max_channels=10, overwrite=overwrite)

    gis = gxapi.GXGIS.create(shp_file, '', gxapi.GIS_TYPE_ARCVIEW)
    gis.load_shapes_gdb(gdb.gxdb)
    gdb.coordinate_system = extent.coordinate_system

    # discard the temp files
    gxu.delete_files_by_root(temp_grid)
    gxu.delete_files_by_root(map_file)
    gxu.delete_files_by_root(shp_file[:-4])

    # resample to resolution
    if resolution > 0.:
        for ln in gdb.list_lines():
            xyz, chlist, _ = gdb.read_line(ln, channels=('X', 'Y', 'Z'))
            xyz = gxgeou.resample(xyz, resolution)
            gdb.write_line(ln, xyz, chlist)

    if return_as == RETURN_GDB:
        return gdb

    # make points from segments
    pplist = []
    for ln in gdb.list_lines():
        xyz = gdb.read_line(ln, channels=('X', 'Y', 'Z'))[0]
        xyz[:, 2] = 0.
        if resolution > 0.:
            xyz = gxgeou.resample(xyz, resolution)
        if extent.coordinate_system.is_oriented:
            xyz = extent.coordinate_system.xyz_from_oriented(xyz)
        pplist.append(gxgeo.PPoint(xyz, coordinate_system=extent.coordinate_system))

    # discard the database
    gdb.close(discard=True)

    if return_as == RETURN_PPOINT:
        return gxgeo.PPoint.merge(pplist)

    return pplist


def calculate_slope_standard_deviation(grid):
    """

    Return the standard deviation of the slopes.

    :param grid: Grid
    :returns:    Standard deviation of grid slopes

    .. Note:: This method calculates the standard deviation of the horizontal
        differences in the X and Y directions for the supplied
        image.  This is useful for shading routines.  A good
        default scaling factor is 2.5 / standard deviation.

        The image will be sub-sampled to a statistically meaningful number.

        The cell sizes are used to determine the slopes.

    .. versionadded:: 9.4
    """

    close_g = False
    if isinstance(grid, str):
        grid = gxgrd.Grid.open(grid)
        close_g = True

    try:
        return gxapi.GXIMU.slope_standard_deviation(grid.gximg)
    finally:
        if close_g:
            grid.close()
