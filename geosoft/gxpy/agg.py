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
ZONE_SHARE = 4
ZONE_LOGLINEAR = 5
ZONE_LAST = 6

class GXagg():
    '''
    The AGG class supports the creation of images from one or more grid data sets.
    AGGs can be placed into map views.

    :param grid_file:     None, or the name of a grid file to create a default AGG with a single grid.

    .. versionadded:: 9.2
    '''

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

    def __init__(self, grid_file=None):

        self.gxagg = gxapi.GXAGG.create()
        if grid_file is not None:
            self.gxagg.layer_img(grid_file, ZONE_DEFAULT, '', gxapi.rDUMMY)

    def list_files(self):
        '''
        Return list of files in the agg.

        .. versionadded:: 9.2
        '''

        vv = gxvv.GXvv(dtype='U1024')
        self.gxagg.list_img(vv._vv)
        return vv.list()