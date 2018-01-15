"""
Geosoft vector arrays (vector of array elements)

:Classes:

    =============== =========================
    :class:`GXva`   vector of array elements
    =============== =========================

VA and VV classes are related based on a key called a *fiducial*, 
which has a start value and increment between values.  The :meth:`refid` method can be used to resample vector
data to the same fiducial so that vector-to-vector operations can be performed.

.. seealso:: :mod:`geosoft.gxpy.vv`, :mod:`geosoft.gxapi.GXVA`, :mod:`geosoft.gxapi.GXVV`

.. note::

    Regression tests provide usage examples:    
    `va tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_gxva.py>`_

"""
from collections.abc import Sequence
import numpy as np
import geosoft
import geosoft.gxapi as gxapi
from . import utility as gxu

__version__ = geosoft.__version__

def _t(s):
    return geosoft.gxpy.system.translate(s)


class VAException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.va`.

    .. versionadded:: 9.1
    """
    pass


class GXva(Sequence):
    """
    VA class wrapper.

    :param array:           2D numpy array, None for an empty VA
    :param dtype:           numpy data type, default np.float
    :param width:           array width, default is determined from array.
    :param fid:             fid tuple (start,increment), default (0.0, 1.0)
    :param unit_of_measure: the unit of measurement for the data

    Maximum number of elements must be less that 2^31 - 1

    .. versionchanged:: 9.3 added unit_of_measure

    .. versionchanged:: 9.2 allow construction directly from numpy array

    .. versionadded:: 9.1
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_gxva'):
            self._gxva = None

    def __len__(self):
        return self._gxva.len()

    def __init__(self, array=None, width=None, dtype=None, fid=(0.0, 1.0), unit_of_measure=''):

        if array is not None:
            if not isinstance(array, np.ndarray):
                array = np.array(array)

            if array.ndim != 2:
                raise VAException(_t('array must have 2 dimensions'))

            if width is None:
                width = array.shape[1]

            if dtype is None:
                dtype = array.dtype

        if width is None or (width < 2):
            raise VAException('width must be >= 2')

        self._gxtype = gxu.gx_dtype(dtype)
        if self._gxtype < 0:
            raise VAException(_t("VA of strings is not supported."))

        self._dtype = gxu.dtype_gx(self._gxtype)
        self._width = width
        self._gxva = gxapi.GXVA.create_ext(self._gxtype, 0, self._width)
        self.fid = fid
        self._start, self._incr = self.fid
        self._sr = None
        self._next = 0
        self._unit_of_measure = unit_of_measure

        if array is not None:
            self.set_data(array, fid)

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
        self._start, self._incr = self.fid
        return self.np[item], self._start + self._incr * item

    @property
    def unit_of_measure(self):
        """ data unit of measurement"""
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, uom):
        self._unit_of_measure = str(uom)

    @property
    def fid(self):
        """
        fid tuple (start,increment), can be set

        .. versionadded:: 9.1
        """
        return self._gxva.get_fid_start(), self._gxva.get_fid_incr()

    @fid.setter
    def fid(self, fid):
        self._gxva.set_fid_start(fid[0])
        self._gxva.set_fid_incr(fid[1])


    def refid(self, fid, length):
        """
        Resample VA to a new fiducial and length

        :param fid: (start,incr)
        :param length: length

        .. versionadded:: 9.1
        """
        self._gxva.re_fid(fid[0], fid[1], length)
        self.fid = fid

    @property
    def length(self):
        """
        number of elements in the VA, can be set.

        .. versionadded:: 9.1

        .. versionchanged:: 9.3 can be set
        """
        return self.__len__()

    @length.setter
    def length(self, length):
        self.refid(self.fid, length)

    @property
    def width(self):
        """
        width of each row(element) in the VA

        .. versionadded:: 9.1
        """
        return self._width

    @property
    def dimensions(self):
        """
        VA dimensions (length, width)

        .. versionadded:: 9.2
        """
        return (self.length, self._width)

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
    def np(self):
        """
        Numpy array of VA data, in the data type of the VA.  Use :meth:`get_data` to get a numpy array
        in another `dtype`.  Array will be 2-dimensional.

        .. versionadded:: 9.2 
        """
        return self.get_data()[0]

    @property
    def gxva(self):
        """
        The :class:`geosoft.gxapi.GXVA` instance handle.

        ..versionadded:: 9.3
        """
        return self._gxva

    def get_data(self, dtype=None, start=0, n=None, start_col=0, n_col=None):
        """
        Return a numpy array of data from a va.

        :param start:       index of first value, must be >=0
        :param n:           number of values wanted
        :param start_col:   index of the first column wanted
        :param n_col:       number of columns
        :param dtype:       numpy data type wanted

        .. versionadded:: 9.1
        """

        if dtype is None:
            dtype = self._dtype
        else:
            dtype = np.dtype(dtype)

        # strings not supported
        if gxu.gx_dtype(dtype) < 0:
            raise VAException(_t('VA string elements are not supported.'))

        if n is None:
            n = self.length - start
        else:
            n = min((self.length - start), n)
        if (n <= 0) or (start < 0):
            raise VAException(_t('Cannot get (start,n) ({},{}) from va of length {}').format(start, n, self.length))

        if n_col is None:
            n_col = self._width - start_col
        else:
            n_col = min((self._width - start_col), n_col)
        if (n_col <= 0) or (start_col < 0):
            raise VAException(_t('Cannot get columns (start,n) ({},{}) from VA of width {}').
                              format(start_col, n_col, self._width))

        npd = self._gxva.get_array_np(start, start_col, n, n_col, dtype).reshape(-1, n_col)

        # float dummies to nan
        if npd.dtype == np.float32 or npd.dtype == np.float64:
            npd[npd == gxu.gx_dummy(npd.dtype)] = np.nan

        fid = self.fid
        start = fid[0] + start * fid[1]
        return npd, (start, fid[1])

    def set_data(self, npdata, fid=(0.0, 1.0)):
        """
        Copy numpy data into a VA.

        :param npdata:  numpy data array (must be 2D)
        :param fid:     fid tuple (start,increment), default (0.0,1.0)

        Maximum number of elements must be less that 2^31 - 1

        .. versionadded:: 9.1
        """

        try:
            npd = npdata.reshape((-1, self._width))
        except ValueError:
            raise VAException(_t('Numpy data does not align with VA data width ({}).').format(self._width))

        max_length = gxapi.iMAX // self._width
        if npdata.shape[0] > max_length:
            raise VAException(_t('Array length {} too long. Maximum is {} for width {}').format(npdata.shape[0], max_length, self._width))

        if npdata.dtype == np.float32 or npdata.dtype == np.float64:
            if np.isnan(np.min(npdata)):
                npdata = npdata.copy()
                npdata[np.isnan(npdata)] = gxu.gx_dummy(npdata.dtype)

        self._gxva.set_ln(npd.shape[0])
        self._gxva.set_array_np(0, 0, npd)
        self.fid = fid
