
import geosoft
import numpy as np
import geosoft.gxapi as gxapi
from . import utility as gxu

__version__ = geosoft.__version__


class VVException(Exception):
    '''
    Exceptions from this module.

    .. versionadded:: 9.1
    '''
    pass


class GXvv():
    '''
    VV class wrapper.

    :param dtype:   numpy data type, or 'str#', where # is a string length, default np.float
    :param fid:     fid tuple (start,increment), default (0.0,1.0)
    :constructor vvNP:  create from a numpy array

    .. versionadded:: 9.1
    '''

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __init__(self, dtype=np.float, fid=(0.0, 1.0)):
        self._gxtype = gxu.gx_dtype(dtype)
        self._dtype = gxu.dtype_gx(self._gxtype)
        self._vv = gxapi.GXVV.create_ext(self._gxtype, 0)
        self._vv.set_fid_start(fid[0])
        self._vv.set_fid_incr(fid[1])
        self._sr = None

    @classmethod
    def vv_np(cls, npdata, fid=(0.0, 1.0)):
        """
        Create a VV from numpy data.

        :param npdata:  numpy data array
        :param fid:     fid tuple (start,increment), default (0.0,1.0)
        :return:        GXvv

        .. versionadded:: 9.1
        """

        vv = cls(dtype=npdata.dtype, fid=fid)

        # numerical data
        if vv._gxtype >= 0:
            vv._vv.set_data_np(0, npdata.flatten())

        # strings
        else:
            npdata = npdata.flatten()
            ne = npdata.shape[0]
            for i in range(ne):
                vv._vv.set_string(i, str(npdata[i]))

        return vv

    def fid(self):
        '''
        :return:    fid tuple (start,increment)

        .. versionadded:: 9.1
        '''
        start = self._vv.get_fid_start()
        incr = self._vv.get_fid_incr()
        return (start, incr)

    def setFid(self, fid):
        '''
        Set the fiducial of the vv.

        :param fid: (fidStart,fidIncrement)

        .. versionadded:: 9.1
        '''
        self._vv.set_fid_start(fid[0])
        self._vv.set_fid_incr(fid[1])

    def reFid(self, fid, length):
        '''
        Resample VV to a new fiducial and length

        :param fid: (start,incr)
        :param length: length

        .. versionadded:: 9.1
        '''
        self._vv.re_fid(fid[0], fid[1], length)

    def length(self):
        '''
        :return:    number of elements in the VV

        .. versionadded:: 9.1
        '''
        return self._vv.length()

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

    def np(self, dtype=None, start=0, n=None):
        '''
        Return a numpy array of data from a vv.

        :param start:   index of first value, must be >=0
        :param n:       number of values wanted
        :param dtype:   numpy data type wanted

        .. versionadded:: 9.1
        '''

        if dtype is None:
            dtype = self._dtype
        else:
            dtype = np.dtype(dtype)

        if n is None:
            n = self.length() - start
        else:
            n = min((self.length() - start), n)

        if (n <= 0) or (start < 0):
            raise VVException('Cannot get (start,n) ({},{}) from vv of length {}'.format(start, n, self.length()))

        # strings wanted
        if dtype.type is np.str_:
            if self._sr is None:
                self._sr = gxapi.str_ref()
            npd = np.empty((n,), dtype=dtype)
            for i in range(start, start + n):
                self._vv.get_string(i, self._sr)
                npd[i - start] = self._sr.value

        # numeric wanted
        else:

            # strings to numeric
            if self._gxtype < 0:
                if np.issubclass_(dtype.type, np.integer):
                    vvd = gxapi.GXVV.create_ext(gxapi.GS_LONG, n)
                else:
                    vvd = gxapi.GXVV.create_ext(gxapi.GS_DOUBLE, n)

                vvd.copy(self._vv)  # this will do the conversion
                npd = vvd.get_data_np(start, n, dtype)

            # numeric to numeric
            else:
                npd = self._vv.get_data_np(start, n, dtype)

        fid = self.fid()
        start = fid[0] + start * fid[1]
        return npd, (start, fid[1])

    def vv(self, npdata, fid=(0.0, 1.0)):
        """
        Copy numpy data to the vv.

        :param npdata:  numpy data array
        :param fid:     fid tuple (start,increment), default (0.0,1.0)

        .. versionadded:: 9.1
        """

        npdata = npdata.flatten()

        # numerical data
        if self._gxtype >= 0:
            self._vv.set_data_np(0, npdata)

        # strings
        else:
            ne = npdata.shape[0]
            for i in range(ne):
                self._vv.set_string(i, str(npdata[i]))

        self._vv.set_len(npdata.shape[0])
        self.setFid(fid)
