"""
Geosoft vector.

.. note::

    Regression tests provide usage examples: `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_vv.py>`_

"""

import geosoft
import numpy as np
import geosoft.gxapi as gxapi
from . import utility as gxu

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class VVException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.1
    """
    pass


class GXvv():
    """
    VV class wrapper.

    :param array:       array-like, None to create an empty VV
    :param dtype:       numpy data type.  For unicode strings 'U#', where # is a string length. If not specified
                        the type is taken from first element in array, of if no array the default is 'float'.
    :param fid:         (start, increment) fiducial
    
    :constructors:
     
        ``GXvv.vv_np`` create from a numpy array
        
    :properties:
    
        ``vv``          gxapi.GXvv instance
        ``fid``         (start, increment) fiducial
        ``length``      number of elements in the VV
        ``gxtype``      GX data type
        ``dtype``       numpy data type

    .. versionchanged:: 9.2
        allow construction directly from arrays

    .. versionadded:: 9.1
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._np = None
        self._vv = None

    def __init__(self, array=None, dtype=None, fid=(0.0, 1.0)):

        if (array is not None) and (type(array) is not np.ndarray):
            if dtype is None:
                dtype = np.dtype(type(array[0]))
            array = np.array(array, dtype=dtype)
            dtype = array.dtype # if strings, type will change to the longest string

        if dtype is None:
            try:
                dtype = array.dtype
            except AttributeError:
                dtype = np.float

        self._gxtype = gxu.gx_dtype(dtype)
        self._dtype = gxu.dtype_gx(self._gxtype)
        self._is_int = gxu.is_int(self._gxtype)
        self._vv = gxapi.GXVV.create_ext(self._gxtype, 0)
        self.fid = fid
        self._start, self._incr = self.fid
        self._sr = None
        self._np = None
        self._next = 0

        if array is not None:
            if self._gxtype >= 0:
                self._vv.set_data_np(0, array.flatten())
            else:
                # strings
                array = array.flatten()
                ne = array.shape[0]
                for i in range(ne):
                    self._vv.set_string(i, str(array[i]))

    def __len__(self):
        return self._vv.length()

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self.length:
            self._next = 0
            self._start, self._incr = self.fid
            raise StopIteration
        else:
            i = self._next
            self._next += 1
            return self.np[i], self._start + self._incr * i

    def __getitem__(self, item):
        start, incr = self.fid
        if self._is_int:
            v = int(self.np[item])
        else:
            v = float(self.np[item])
        return v, start + incr * item

    @property
    def gxvv(self):
        return self._vv

    @property
    def fid(self):
        """
        :return:    fid tuple (start,increment)

        .. versionadded:: 9.1
        """
        return (self._vv.get_fid_start(), self._vv.get_fid_incr())

    @fid.setter
    def fid(self, fid):
        """
        Set the fiducial of the vv.

        :param fid: (fidStart,fidIncrement)

        .. versionadded:: 9.2
        """
        self._vv.set_fid_start(fid[0])
        self._vv.set_fid_incr(fid[1])

    @property
    def length(self):
        """
        :return:    number of elements in the VV

        .. versionadded:: 9.1
        """
        return self.__len__()

    @property
    def gxtype(self):
        """
        :return: GX data type

        .. versionadded:: 9.1
        """
        return self._gxtype

    @property
    def dtype(self):
        """
        :return: numpy data type

        .. versionadded:: 9.1
        """
        return self._dtype

    @property
    def is_int(self):
        """ True if a base integer type"""
        return self._is_int

    @property
    def np(self):
        """
        Numpy array of VV data, in the data type of the VV.  Use :meth:`get_np` to get a numpy array
        in another dtype.
        
        .. versionadded:: 9.2 
        """
        if self.length == 0:
            return np.array([], dtype=self._dtype)

        self._np, *_ = self.get_data()
        return self._np

    def get_data(self, dtype=None, start=0, n=None):
        """
        Return vv data in a numpy array

        :param start:   index of first value, must be >=0
        :param n:       number of values wanted
        :param dtype:   numpy data type wanted
        :returns:       (data, (fid_start, fid_incr))

        .. versionadded:: 9.1
        """

        if dtype is None:
            dtype = self._dtype
        else:
            dtype = np.dtype(dtype)

        if (self._np is not None) and (dtype == self.dtype) and (start == 0) and (n is None):
            return self._np

        if n is None:
            n = self.length - start
        else:
            n = min((self.length - start), n)

        if (n < 0) or (start < 0) or (start >= self.length):
            raise VVException(_t('Cannot get (start,n) ({},{}) from vv of length {}').format(start, n, self.length))

        if n == 0:
            npd = np.array([], dtype=dtype)

        else:

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

        fid = self.fid
        start = fid[0] + start * fid[1]
        return npd, (start, fid[1])

    def set_data(self, data, fid=(0.0, 1.0)):
        """
        Set vv data from an array

        :param data:    data array
        :param fid:     fid tuple (start,increment), default (0.0,1.0)

        .. versionadded:: 9.1
        """

        if not isinstance(data, np.ndarray):
            data = np.array(data)
        npdata = data.flatten()

        # numerical data
        if self._gxtype >= 0:
            self._vv.set_data_np(0, npdata)

        # strings
        else:
            ne = npdata.shape[0]
            for i in range(ne):
                self._vv.set_string(i, str(npdata[i]))

        self._vv.set_len(npdata.shape[0])
        self.fid = fid

    def refid(self, fid, length):
        """
        Resample VV to a new fiducial and length

        :param fid: (start,incr)
        :param length: length

        .. versionadded:: 9.1
        """
        self._vv.re_fid(fid[0], fid[1], length)
        self.fid = fid
