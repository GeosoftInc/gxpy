"""
Geosoft vector. 

:Classes:

    =============== =========================
    :class:`GXvv`   data vector
    =============== =========================

VA and VV classes are related based on a key called a *fiducial*, 
which has a start value and increment between values.  The :meth:`refid` method can be used to resample vector
data to the same fiducial so that vector-to-vector operations can be performed.

.. seealso:: :mod:`geosoft.gxpy.va`, :mod:`geosoft.gxapi.GXVV`, :mod:`geosoft.gxapi.GXVA`

.. note::

    Regression tests provide usage examples:    
    `vv tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_vv.py>`_

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
    Exceptions from :mod:`geosoft.gxpy.vv`.

    .. versionadded:: 9.1
    """
    pass


class GXvv:
    """
    VV class wrapper.

    :param array:           array-like, None to create an empty VV
    :param dtype:           numpy data type.  For unicode strings 'U#', where # is a string length. If not specified
                            the type is taken from first element in array, of if no array the default is 'float'.
    :param fid:             (start, increment) fiducial
    :param unit_of_measure: unit of measure for the contained data.
    
    :Constructors:
     
        ``GXvv.vv_np`` create from a numpy array
        
    :Properties:
    
        ``vv``          :class:`geosoft.gxapi.GXvv` instance
        ``fid``         (start, increment) fiducial
        ``length``      number of elements in the VV
        ``gxtype``      GX data type
        ``dtype``       numpy data type

    .. versionadded:: 9.1

    .. versionchanged:: 9.2 support construction directly from arrays

    .. versionchanged:: 9.3 added unit_of_measure
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._np = None
        self._vv = None

    def __init__(self, array=None, dtype=None, fid=(0.0, 1.0), unit_of_measure=''):

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
        self._sr = None
        self._np = None
        self._next = 0
        self._unit_of_measure = unit_of_measure

        if array is not None:
            self.set_data(array.flatten(), fid)

    def __len__(self):
        return self._vv.length()

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self.length:
            self._next = 0
            raise StopIteration
        else:
            i = self._next
            self._next += 1
            return self.np[i], self.fid[0] + self.fid[1] * i

    def __getitem__(self, item):
        start, incr = self.fid
        if self._is_int:
            v = int(self.np[item])
        else:
            v = float(self.np[item])
        return v, start + incr * item

    @property
    def unit_of_measure(self):
        """ data unit of measurement"""
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, uom):
        self._unit_of_measure = str(uom)

    @property
    def gxvv(self):
        """:class:`geosoft.gxapi.GXVV` instance"""
        return self._vv

    @property
    def fid(self):
        """
        fid tuple (start,increment), can be set

        .. versionadded:: 9.1
        """
        return (self._vv.get_fid_start(), self._vv.get_fid_incr())

    @fid.setter
    def fid(self, fid):
        self._vv.set_fid_start(fid[0])
        self._vv.set_fid_incr(fid[1])

    @property
    def length(self):
        """
        number of elements in the VV

        .. versionadded:: 9.1
        """
        return self.__len__()

    @property
    def gxtype(self):
        """
        GX data type

        .. versionadded:: 9.1
        """
        return self._gxtype

    @property
    def dtype(self):
        """
        numpy data type

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
        Numpy array of VV data, in the data type of the VV.  Use :meth:`get_data` to get a numpy array
        in another dtype.
        
        .. versionadded:: 9.2 
        """
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
            return self._np, self.fid

        if n is None:
            n = self.length - start
        else:
            n = min((self.length - start), n)

        if (n < 0) or (start < 0) or ((start >= self.length) and self.length > 0):
            raise VVException(_t('Cannot get (start,n) ({},{}) from vv of length {}').format(start, n, self.length))

        if (n == 0) or (self.length == 0):
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

    def set_data(self, data, fid=None):
        """
        Set vv data from an array.  If the array is float type numpy.nan are

        :param data:    data array
        :param fid:     fid tuple (start,increment), default does not change

        .. versionadded:: 9.1

        .. versionmodified:: 9.3
            default fid leaves fid unchanged
        """

        if not isinstance(data, np.ndarray):
            data = np.array(data)
        npdata = data.flatten()

        # numerical data
        if self._gxtype >= 0:
            if npdata.dtype == np.float32 or npdata.dtype == np.float64:
                npdata[npdata == np.nan] = gxu.gx_dummy(npdata.dtype)
            self._vv.set_data_np(0, npdata)

        # strings
        else:
            ne = npdata.shape[0]
            for i in range(ne):
                self._vv.set_string(i, str(npdata[i]))

        self._np = None

        self._vv.set_len(npdata.shape[0])
        if fid:
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

    def list(self):
        """
        Return the content of the VV as a list.
        
        .. versionadded:: 9.2
        """
        return [v[0] for v in self]