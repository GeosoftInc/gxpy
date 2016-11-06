import os
import gc
import time
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
from . import ipj as gxipj
from . import vv as gxvv
from . import utility as gxu

__version__ = geosoft.__version__


class GRDException(Exception):
    '''
    Exceptions from this module.

    .. versionadded:: 9.1
    '''
    pass

# constants
FILE_READ = 0
FILE_READWRITE = 1     # file exists, but can change properties
FILE_NEW = 2


class GXgrd():
    """
    Grid and image class.

    Creation options:

        ====== =============================
        open() open an existing grid/image
        new()  create a new grid/image
        ====== =============================

    .. versionadded:: 9.1
    """

    gc = None
    _delete_files = False
    _filename = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.__del__()

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        if self._filename is None:
            return '__memory__'
        else:
            return self._filename

    def __init__(self, fileName=None, dtype=None, mode=None, kx=1, dim=None):

        self._delete_files = False
        self._readonly = False
        self._np = None
        self._hpg = None

        # When working with very large grids (gigabyte+), the
        # file system cannot always keep up with closing/caching and re-opening the
        # grid. Though this is actually a system problem, we deal with this problem by attempting
        # to open a grid three times before raising an error.

        # rebuild a clean file name
        self._hgd = False
        if (fileName is None) or (len(fileName.strip()) == 0):
            self._filename = None
        else:
            self._np = GXgrd.name_parts(fileName)
            self._filename = GXgrd.decorate_name(os.path.join(self._np[0], self._np[1]), self._np[4])

            if mode == FILE_NEW:
                # special case - HGD file, must work with a memory grid, save to HGD at end
                if self._np[4].lower() == 'hgd':
                    self._hgd = True

        # When working with very large grids (gigabyte+), the
        # file system cannot always keep up with closing/caching and re-opening the
        # grid. Though this is actually a system problem, we deal with this problem by attempting
        # to open a grid three times before raising an error.

        self._img = None
        attempt = 0
        while self._img is None:

            try:
                if (self._filename is None):
                    self._img = gxapi.GXIMG.create(gxu.gx_dtype(dtype), kx, dim[0], dim[1])

                elif mode == FILE_NEW:
                    if self._hgd:
                        # for HGD grids, make a memory grid, which will be saved to an HGD on closing
                        self._img = gxapi.GXIMG.create(gxu.gx_dtype(dtype), kx, dim[0], dim[1])
                    else:
                        self._img = gxapi.GXIMG.create_new_file(gxu.gx_dtype(dtype), kx, dim[0], dim[1], self._filename)

                elif mode == FILE_READ:
                    self._img = gxapi.GXIMG.create_file(gxu.gx_dtype(dtype), self._filename, gxapi.IMG_FILE_READONLY)
                    self._readonly = True

                else:
                    self._img = gxapi.GXIMG.create_file(gxu.gx_dtype(dtype), self._filename, gxapi.IMG_FILE_READORWRITE)

            except geosoft.gxapi.GXError as e:
                time.sleep(0.1)
                gc.collect()
                attempt += 1
                if attempt > 10:
                    raise GRDException('Cannot open: {}\nBecause: {}'.format(self._filename, str(e)))

    def __del__(self):

        def df(fn):
            try:
                os.remove(fn)
            except OSError as e:
                pass

        if self._delete_files:

            img = self._img
            self._img = None
            del img

            # delete files
            if self._filename is not None:

                fn = GXgrd.name_parts(self._filename)
                filename = os.path.join(fn[0], fn[1])
                ext = fn[3]
                df(filename)
                df(filename + '.gi')
                df(filename + '.xml')

                # hgd files
                if ext == '.hgd':
                    for i in range(16):
                        df(filename + str(i))

        elif self._hgd:
            # an HGD memory grid was made, save it to an HGD file
            gxapi.GXHGD.h_create_img(self._img, GXgrd.decorate_name(self._filename, 'HGD'))
            gc.collect()

    @classmethod
    def open(cls, fileName, dtype=None, mode=None):
        """
        Open an existing grid file.

        :param gxPy:        GX context
        :param fileName:    name of the grid file
        :param dtype:       numpy data type
        :param mode:        open mode:

            =================  ================================================
            FILE_READ          only read the file, properties cannot be changed
            FILE_READWRITE     grid stays the same, but properties may change
            =================  ================================================

        .. versionadded:: 9.1
        """

        if mode is None:
            mode = FILE_READ
        grd = cls(fileName, dtype=dtype, mode=mode)

        return grd

    @classmethod
    def new(cls, fileName=None, properties={}):
        """
        Create a new grid file.

        :param gxPy:        GX context
        :param fileName:    name of the grid file, None or '' for a memory grid
        :param properties:  dictionary of grid properties

        .. versionadded:: 9.1
        """

        # set basic grid properties
        dtype = properties.get('dtype', None)
        nx = properties.get('nx', 0)
        ny = properties.get('ny', 0)
        if (nx <= 0) or (ny <= 0):
            raise ValueError('Grid dimension ({},{}) must be > 0'.format(nx, ny))

        grd = cls(fileName, dtype=dtype, mode=FILE_NEW, dim=(nx, ny))
        grd.set_properties(properties)

        return grd

    @classmethod
    def from_data_array(cls, data, filename, properties={}):
        """
        Create grid from a 2D numpy array.

        :param gxPy:        GXpy
        :param data:        2D numpy data array, must be 2D
        :param filename:    name of the file
        :return:            GXgrd instance

        .. versionadded:: 9.1
        """

        ny, nx = data.shape
        properties['nx'] = nx
        properties['ny'] = ny
        properties['dtype'] = data.dtype
        grd = cls.new(filename, properties=properties)
        grd.write_rows(data)
        return grd

    def delete_files(self, delete=True):
        """
        Delete the files associated with this grid when deleting the grid object.
        Note that files are not deleted until all references to this object are
        deleted and garbage collection is performed.

        :param delete: set to False to reverse a previous delete request

        .. versionadded:: 9.1
        """
        self._delete_files = delete

    @staticmethod
    def name_parts(name):
        """
        Return folder, undecorated file name + ext, file root, ext, decorations.

        If extension is not specified, ".grd" assumed

        For example:

        .. code::

            >>> import geosoftpy.grd as grd
            >>> namep = grd.GXgrd.name_parts("f:/someFolder/name.grd(GRD;TYPE=SHORT)")
            >>> print(namep)
            ('f:/someFolder/','name.grd','name','.grd','(GRD;TYPE=SHORT)')

        .. versionadded:: 9.1
        """

        path = os.path.abspath(name)
        fn = os.path.dirname(path)
        bn = os.path.basename(path).split('(')
        name = bn[0]
        root, ext = os.path.splitext(bn[0])
        if len(bn) > 1:
            dec = bn[1].split(')')[0]
        else:
            dec = ''

        if ext == '':
            if (dec == '') or (dec[:3].upper() == 'GRD'):
                # add Geosoft grd extension
                ext = '.grd'
                name = name + ext

        return fn, name, root, ext, dec

    @staticmethod
    def decorate_name(name, decorations=''):
        """
        Properly decorate a grid name.

        :param name:        file name
        :param decorations: file decorations, semicolon delimited
        :returns:           decorated file name

        .. versionadded:: 9.1
        """

        if len(decorations.strip()) > 0:
            d = decorations.lstrip('(')
            end = d.find(')')
            if end != -1:
                d = d[:end]
            name = name.split('(')[0]
        else:
            name = name.strip()
            n = name.split('(')
            if len(name) > len(n[0]):
                d = n[1].split(')')[0]
                name = n[0]
            else:
                return n[0]
        return name + '(' + d + ')'

    def dtype(self):
        """
        :return: numpy data type for the grid

        .. versionadded:: 9.1
        """
        return gxu.dtype_gx(self._img.e_type())

    def properties(self):
        """
        Get the grid properties dictionary
        :return: properties dictionary

        .. versionadded:: 9.1
        """

        properties = {}
        properties['nx'] = self._img.nx()
        properties['ny'] = self._img.ny()
        properties['x0'] = self._img.query_double(gxapi.IMG_QUERY_rXO)
        properties['y0'] = self._img.query_double(gxapi.IMG_QUERY_rYO)
        properties['dx'] = self._img.query_double(gxapi.IMG_QUERY_rDX)
        properties['dy'] = self._img.query_double(gxapi.IMG_QUERY_rDY)
        properties['rot'] = self._img.query_double(gxapi.IMG_QUERY_rROT)
        properties['dtype'] = self.dtype()
        np = GXgrd.name_parts(self._filename)
        properties['filename'] = os.path.join(np[0], np[1])
        if len(np[4]) > 0:
            properties['gridtype'] = np[4].split(';')[0]
        else:
            properties['gridtype'] = np[3][1:]
        properties['decoration'] = np[4]

        # get coordinate system
        ipj = gxipj.GXipj()
        self._img.get_ipj(ipj._ipj)
        properties['ipj'] = ipj

        return properties

    def set_properties(self, properties):
        """
        Set grid properties from a properties dict.  Settable property keys are:

            ===== ============================================
            'x0'  grid X origin location (default 0.0)
            'y0'  grid Y origin location (0.0)
            'dx'  grid X point separation (1.0)
            'dy'  grid Y point separation (1.0)
            'rot' grid counter-clockwise rotation angle (0.0)
            'ipj' coordinate system object (unchanged)
            ===== ============================================

        Not all keys need be passed, though best practice it to get the properties from
        the grid and modify those that need to change and pass the properties back.

        :param properties: properties dictionary

        .. versionadded:: 9.1
        """

        if self._readonly:
            raise ValueError('{} opened as read-only, cannot set properties.'.format(self._filename))

        dx = properties.get('dx', 1.0)
        dy = properties.get('dy', dx)
        self._img.set_info(dx, dy,
                           properties.get('x0', 0.0),
                           properties.get('y0', 0.0),
                           properties.get('rot', 0.0))
        ipj = properties.get('ipj', None)
        if ipj is not None:
            if isinstance(ipj, str):
                ipj = gxipj.GXipj.from_name(ipj)
            self._img.set_ipj(ipj._ipj)

    def save_as(self, fileName, dtype=None):
        """
        Save a grid to a new file.  File is overwritten if it exists.

        :param fileName:    name of the file to save
        :param dtype:       numpy data type, None to use type of the parent grid
        :return:            GXgrd of saved file

        .. versionadded:: 9.1
        """

        p = self.properties()
        if not (dtype is None):
            p['dtype'] = dtype

        savegrid = GXgrd.new(fileName, p)
        self._img.copy(savegrid._img)
        del savegrid
        gc.collect()

        return GXgrd.open(fileName, mode=FILE_READWRITE)

    def _geth_pg(self):
        '''Get an hpg for the grid, adding the handle to the class so it does not get destroyed.'''
        if self._hpg is None:
            self._hpg = self._img.geth_pg()
        return self._hpg

    def indexWindow(self, name, x0=0, y0=0, nx=None, ny=None):
        """
        Window a grid based on index.
        :param x0:  integer index of the first X point
        :param y0:  integer index of the first Y point
        :param nx:  number of points in x
        :param ny:  number of points in y

        .. versionadded:: 9.1
        """

        p = self.properties()
        gnx = p.get('nx')
        gny = p.get('ny')
        if nx is None:
            nx = gnx - x0
        if ny is None:
            ny = gny - y0
        mx = x0 + nx
        my = y0 + ny
        if ((x0 >= gnx) or (y0 >= gny) or
                (x0 < 0) or (y0 < 0) or
                (nx <= 0) or (ny <= 0) or
                (mx > gnx) or (my > gny)):
            raise GRDException('Window x0,y0,mx,my({},{},{},{}) out of bounds ({},{})'.format(x0, y0, mx, my, gnx, gny))

        if p.get('rot') != 0.0:
            raise ('Cannot window a rotated grid.')

        # create new grid
        p['nx'] = nx
        p['ny'] = ny
        p['x0'] = p.get('x0') + p.get('dx') * x0
        p['y0'] = p.get('y0') + p.get('dy') * y0
        wgd = self.new(name, p)
        wpg = wgd._geth_pg()
        gpg = self._geth_pg()
        wpg.copy_subset(gpg, 0, 0, y0, x0, ny, nx)

        return wgd

    def write_rows(self, data, ix0=0, iy0=0, order=1):
        """
        Write data to a grid by rows.

        :param data:    array of data to write
        :param ix0:     grid X index of first point
        :param iy0:     grid Y index of first point, top index if writing rows top to bottom
        :param order:   1: bottom to top; -1: top to bottom

        .. versionadded:: 9.1
        """

        ny, nx = data.shape
        vv = gxvv.GXvv(self.dtype())
        iy = iy0
        for i in range(ny):
            self._img.write_y(iy, ix0, 0, vv.vv_np(data[i, :])._vv)
            iy += order

    def read_rows(self, ix0=0, iy0=0):
        '''

        :param ix0:
        :param iy0:
        :return:

        .. versionadded:: 9.1
        '''


# grid utilities
def array_locations(properties, z=0.):
    '''
    Create an array of (x,y,z) points for a grid defined by properties
    :param properties:  grid properties
    :return:            array of points, shaped (ny, nx, 3)

    .. versionadded:: 9.1
    '''

    nx = properties.get('nx')
    ny = properties.get('ny')
    dx = properties.get('dx')
    dy = properties.get('dy', dx)
    offset = np.array([properties.get('x0', 0.), properties.get('y0', 0.), z])
    loc = np.zeros((ny, nx, 3))
    loc[:, :, 0:2] = np.mgrid[0: (nx - 0.5) * dx: dx, 0: (ny - 0.5) * dy: dy].swapaxes(0, 2)

    return loc + offset


def gridMosaic(mosaic, gridList, typeDecoration='', report=None):
    """
    Combine a set of grids into a single grid.  Raises an error if the resulting grid is too large.

    :param mosaic:          name of the output grid, returned.  Decorate with '(HGD)' to get an HGD
    :param gridList:        list of input grid names
    :param typeDecoration:  decoration for input grids if not default
    :param report:          string reporting function, report=print to print progress
    :return:                GXgrd

    .. versionadded:: 9.1
    """

    def props(gn, repro=None):
        g = GXgrd.open(gn)
        if repro:
            g._img.create_projected2(repro[0], repro[1])
        p = g.properties()
        return p

    def dimension(glist):

        def dimg(g, repro=None):
            p = props(g, repro)
            x0 = p.get('x0')
            y0 = p.get('y0')
            xM = x0 + (p.get('nx') - 1) * p.get('dx')
            yM = y0 + (p.get('ny') - 1) * p.get('dy')
            ipj = p.get('ipj')._ipj
            cell = p.get('dx')
            return x0, y0, xM, yM, (ipj, cell)

        def ndim(x0, xM, dX):
            return int((xM - x0 + dX / 2.0) / dX) + 1

        x0, y0, xM, yM, repro = dimg(glist[0])
        for g in glist[1:]:
            xx0, yy0, xxM, yyM, r = dimg(g, repro)
            if xx0 < x0:
                x0 = xx0
            if yy0 < y0:
                y0 = yy0
            if xxM > xM:
                xM = xxM
            if yyM > yM:
                yM = yyM

        # calculate new grid dimension
        p = props(glist[0])
        nX = ndim(x0, xM, p.get('dx'))
        nY = ndim(y0, yM, p.get('dy'))

        return x0, y0, nX, nY, xM, yM

    def locate(x0, y0, p):

        dx = p.get('dx')
        dy = p.get('dy')
        dsx = round((p.get('x0') - x0) / dx)
        dsy = round((p.get('y0') - y0) / dy)

        return dsx, dsy

    def paste(gn, mpg):
        g = GXgrd.open(gn)
        p = g.properties()
        nX = p.get('nx')
        nY = p.get('ny')
        gpg = g._geth_pg()
        destx, desty = locate(x0, y0, p)
        if report:
            report('    +{} nx,ny({},{})'.format(g, nX, nY))
            report('     Copy ({},{}) -> ({},{}) of ({},{})'.format(nX, nY, destx, desty, mnx, mny))
        mpg.copy_subset(gpg, desty, destx, 0, 0, nY, nX)
        return

    if len(gridList) == 0:
        raise ValueError('At least one grid is required')

    # create list of grids, all matching on coordinate system of first grid
    grids = []
    for i in range(len(gridList)):
        grids.append(GXgrd.decorate_name(gridList[i], typeDecoration))

    # output grid
    x0, y0, nX, nY, xm, ym = dimension(grids)
    p = props(grids[0])
    p['x0'] = x0
    p['y0'] = y0
    p['nx'] = nX
    p['ny'] = nY
    if report is not None:
        report('')
        report('Mosaic: dim({},{}) x({},{}) y({},{}), cell({})...'.format(nX, nY, x0, xm, y0, ym, p.get('dx')))
    master = GXgrd.new(mosaic, p)
    if report:
        p = master.properties()
        x0 = p.get('x0')
        y0 = p.get('y0')
        nx = p.get('nx')
        ny = p.get('ny')
        report('Memory image ready ({}) dim({},{}) x0,y0({},{})'.format(master, nx, ny, x0, y0))

    # paste grids onto master
    pm = master.properties()
    mnx = pm.get('nx')
    mny = pm.get('ny')
    mpg = master._geth_pg()
    for g in grids:
        paste(g, mpg)

    if report:
        report('Mosaic completed: {}'.format(mosaic))

    return master


def gridBool(g1, g2, joinedGrid, opt=1, size=3, olap=1):
    """

    :param g1,g2:   GXgrd of grids to merge
    :param new:     new output grid, overwritten if it exists
    :param opt:     logic to use on overlap points, default 1 (OR):

        === ============================================
        0   AND, both grids must have valid value
        1   OR, either grid has a valid value
        2   XOR, same as OR, except overlap is dummied
        === ============================================

    :param size:    size of the output grid, default is minimum size

        === ==========================================
        0   minimum size - dummy regions clipped
        1   size to grid 1
        2   size to grid 2
        3   size to maximum including both grids
        === ==========================================

    :param olap:    what to do with overlapping valid points, default uses grid 1

        === ==========================================
        0   average points
        1   use grid 1
        2   use grid 2
        === ==========================================

    :returns:       GXgrd of the merged output grid

    .. versionadded:: 9.1
    """

    if isinstance(g1, str):
        g1 = GXgrd.open(g1)
    if isinstance(g2, str):
        g2 = GXgrd.open(g2)

    gxapi.GXIMU.grid_bool(g1._img, g2._img, joinedGrid, opt, size, olap)
    return GXgrd.open(joinedGrid)
