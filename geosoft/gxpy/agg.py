import os

import geosoft
import geosoft.gxapi as gxapi
from . import vv as gxvv

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class AGGException(Exception):
    '''
    Exceptions from this module.

    .. versionadded:: 9.2
    '''
    pass

ZONE_DEFAULT = 0
ZONE_LINEAR = 1
ZONE_NORMAL = 2
ZONE_EQUALAREA = 3
ZONE_SHADE = 4
ZONE_LOGLINEAR = 5
ZONE_LAST = 6

class GXagg():
    '''
    The AGG class supports the creation of images from one or more grid data sets.
    AGGs can be placed into map views.

    :param grid_file:   None, or the name of a grid file to create a default AGG with a single grid.
    :param shade:       if True, add shading effect
    :param zone:        Colour distribution method:

        ::

            ZONE_DEFAULT        as set by user global default settings
            ZONE_LINEAR         linearly distributed
            ZONE_NORMAL         normal (Gaussian) distribution
            ZONE_EQUALAREA      each colour will occupy an equal area on the image
            ZONE_LOGLINEAR      logarithmic linear distribution
            ZONE_LAST           last used colouring for this grid file
            ZONE_SHADE          Displays the shaded image version of the grid. The shaded image is
                                a grid file will with '_s' appended to the file name.  If it does not
                                exist, a shaded image with illumination inclination and declination
                                both set to 45 degrees is automatically created.

    .. versionadded:: 9.2
    '''
    #TODO add shaded image to grd

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        s = 'GXagg> '
        for fn in self.list_files():
            s = s + os.path.basename(fn).split('.')[0] + ', '
        return s[:-2]

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __init__(self, grid_file=None, shade=False, zone=None):

        self.gxagg = gxapi.GXAGG.create()
        if grid_file is not None:
            if zone is None:
                zone = ZONE_DEFAULT
            self.gxagg.layer_img(grid_file, zone, '', gxapi.rDUMMY)
            if shade and zone != ZONE_SHADE:
                self.gxagg.layer_img(grid_file, ZONE_SHADE, 'lgray.tbl', gxapi.rDUMMY)

    def list_files(self):
        '''
        Return list of files in the agg.

        .. versionadded:: 9.2
        '''

        vv = gxvv.GXvv(dtype='U1024')
        self.gxagg.list_img(vv._vv)
        return vv.list()