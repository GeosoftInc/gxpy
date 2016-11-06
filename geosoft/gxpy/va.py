
import geosoft
import numpy as np
import geosoft.gxapi as gxapi
from . import utility as gxu

__version__ = geosoft.__version__


class VAException(Exception):
    '''
    Exceptions from this module.

    .. versionadded:: 9.1
    '''
    pass


def _(s):
    return s


class GXva():
    '''
    VA class wrapper.

    :param dtype:   numpy data type, or 'str#', where # is a string length, default np.float
    :param width:   array width
    :param fid:     fid tuple (start,increment), default (0.0,1.0)
    :constructor vaNP:  create from a numpy array

    .. versionadded:: 9.1
    '''

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __init__(self, width, dtype=np.float, fid=(0.0, 1.0)):
        self._gxtype = gxu.gx_dtype(dtype)
        self._dtype = gxu.dtype_gx(self._gxtype)
        self._width = width
        self._va = gxapi.GXVA.create_ext(self._gxtype, 0, width)
        self._va.set_fid_start(fid[0])
        self._va.set_fid_incr(fid[1])
        self._sr = None

    @classmethod
    def vaNp(cls, npdata, fid=(0.0, 1.0)):
        """
        Create a VA from numpy data.

        :param npdata:  numpy data array
        :param fid:     fid tuple (start,increment), default (0.0,1.0)
        :return:        GXva

        .. versionadded:: 9.1
        """

        va = cls(npdata.shape[1], dtype=npdata.dtype, fid=fid)

        # numerical data
        if va._gxtype >= 0:
            va._va.set_ln(npdata.shape[0])
            va._va.set_array_np(0, 0, npdata)

        # strings
        else:
            raise VAException(_("VA of strings is not supported."))

        return va

    def fid(self):
        '''
        :return:    fid tuple (start,increment)

        .. versionadded:: 9.1
        '''
        start = self._va.get_fid_start()
        incr = self._va.get_fid_incr()
        return (start, incr)

    def setFid(self, fid):
        '''
        Set the fiducial of the va.

        :param fid: (fidStart,fidIncrement)

        .. versionadded:: 9.1
        '''
        self._va.set_fid_start(fid[0])
        self._va.set_fid_incr(fid[1])

    def reFid(self, fid, length):
        '''
        Resample VA to a new fiducial and length

        :param fid: (start,incr)
        :param length: length

        .. versionadded:: 9.1
        '''
        self._va.re_fid(fid[0], fid[1], length)

    def length(self):
        '''
        :return:    number of elements in the VA

        .. versionadded:: 9.1
        '''
        return self._va.len()

    def width(self):
        '''
        :return:    width of each row(element) in the VA

        .. versionadded:: 9.1
        '''
        return self._width

    def size(self):
        '''
        :return:    VA size (length, width)

        .. versionadded:: 9.1
        '''
        return (self.length(), self._width)

    def gxtype(self):
        '''
        :return: GX data type

        .. versionadded:: 9.1
        '''
        return self._gxtype

    def dtype(self):
        '''
        :return: numpy data type

        .. versionadded:: 9.1
        '''
        return self._dtype

    def np(self, dtype=None, start=0, n=None, start_col=0, n_col=None):
        '''
        Return a numpy array of data from a va.

        :param start:       index of first value, must be >=0
        :param n:           number of values wanted
        :param start_col:   index of the first column wanted
        :param n_col:       number of columns
        :param dtype:       numpy data type wanted

        .. versionadded:: 9.1
        '''

        if dtype is None:
            dtype = self._dtype
        else:
            dtype = np.dtype(dtype)

        # strings not supported
        if gxu.gx_dtype(dtype) < 0:
            raise VAException(_('VA string elements are not supported.'))

        if n is None:
            n = self.length() - start
        else:
            n = min((self.length() - start), n)
        if (n <= 0) or (start < 0):
            raise VAException(_('Cannot get (start,n) ({},{}) from va of length {}').format(start, n, self.length()))

        if n_col is None:
            n_col = self._width - start_col
        else:
            n_col = min((self._width - start_col), n_col)
        if (n_col <= 0) or (start_col < 0):
            raise VAException(_('Cannot get columns (start,n) ({},{}) from VA of width {}').
                              format(start_col, n_col, self._width))

        npd = self._va.get_array_np(start, start_col, n, n_col, dtype).reshape(-1, self._width)

        fid = self.fid()
        start = fid[0] + start * fid[1]
        return npd, (start, fid[1])

    def va(self, npdata, fid=(0.0, 1.0)):
        """
        Copy numpy data into a VA.

        :param npdata:  numpy data array (must be 2D)
        :param fid:     fid tuple (start,increment), default (0.0,1.0)

        .. versionadded:: 9.1
        """

        try:
            npd = npdata.reshape((-1, self._width))
        except ValueError:
            raise VAException(_('Numpy data does not match VA data width ({}).'
                                .format(self._width)))

        self._va.set_array_np(0, 0, npd)
        self._va.set_ln(npd.shape[0])
        self.setFid(fid)
