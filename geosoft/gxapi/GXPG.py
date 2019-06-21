### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXPG(gxapi_cy.WrapPG):
    """
    GXPG class.

    Pager methods for large 2-D arrays
    This class handles very-large 2-D arrays in which efficient
    access is required along both rows and columns.

    **Note:**

    Typically a grid is accessed using the `GXIMG <geosoft.gxapi.GXIMG>` class, and a `GXPG <geosoft.gxapi.GXPG>`
    is obtained from the `GXIMG <geosoft.gxapi.GXIMG>` using the `GXIMG.get_pg <geosoft.gxapi.GXIMG.get_pg>` function.
    Following operations on the `GXPG <geosoft.gxapi.GXPG>`, it can be written back to
    the `GXIMG <geosoft.gxapi.GXIMG>` using `GXIMG.set_pg <geosoft.gxapi.GXIMG.set_pg>`.
    """

    def __init__(self, handle=0):
        super(GXPG, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPG <geosoft.gxapi.GXPG>`
        
        :returns: A null `GXPG <geosoft.gxapi.GXPG>`
        :rtype:   GXPG
        """
        return GXPG()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



# 2D Methods



    def copy(self, pgs):
        """
        Copy the data from one pager to another.
        
        :param pgs:  Source `GXPG <geosoft.gxapi.GXPG>` object
        :type  pgs:  GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(pgs)
        




    def copy_subset(self, pgs, y_row_d, x_col_d, y_row_s, x_col_s, ny, nx):
        """
        Copy a subset of data from one pager to another.
        
        :param pgs:      Source `GXPG <geosoft.gxapi.GXPG>` object
        :param y_row_d:  Y (row) Origin on destination
        :param x_col_d:  X (col) Origin on destination
        :param y_row_s:  Y (row) Origin on source
        :param x_col_s:  X (col) Origin on source
        :param ny:       Number of Y (rows) to copy
        :param nx:       Number of X (columns) to copy
        :type  pgs:      GXPG
        :type  y_row_d:  int
        :type  x_col_d:  int
        :type  y_row_s:  int
        :type  x_col_s:  int
        :type  ny:       int
        :type  nx:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 2D Only
        """
        self._copy_subset(pgs, y_row_d, x_col_d, y_row_s, x_col_s, ny, nx)
        



    @classmethod
    def create(cls, row, col, type):
        """
        Creates a Pager object
        
        :param row:   # elements in y (# of row)
        :param col:   # elements in x (# of column)
        :param type:  :ref:`GS_TYPES`
        :type  row:   int
        :type  col:   int
        :type  type:  int

        :returns:     `GXPG <geosoft.gxapi.GXPG>` Object
        :rtype:       GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapPG._create(GXContext._get_tls_geo(), row, col, type)
        return GXPG(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create a 2D `GXPG <geosoft.gxapi.GXPG>` from serialized source.
        
        :type  bf:  GXBF

        :returns:    `GXPG <geosoft.gxapi.GXPG>` Object
        :rtype:      GXPG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** For 3D pagers, use CreateBF_PG.
        """
        ret_val = gxapi_cy.WrapPG._create_s(GXContext._get_tls_geo(), bf)
        return GXPG(ret_val)






    def dummy(self):
        """
        Sets the Entire pager to dummy.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._dummy()
        




    def e_type(self):
        """
        Gets the type of pager.
        

        :returns:    :ref:`GS_TYPES`
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._e_type()
        return ret_val




    def n_cols(self):
        """
        Gets the # of columns in pager.
        

        :returns:    # of columns.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._n_cols()
        return ret_val




    def n_rows(self):
        """
        Gets the # of rows in pager.
        

        :returns:    # of rows.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._n_rows()
        return ret_val




    def n_slices(self):
        """
        Gets the # of slices (z) in pager.
        

        :returns:    # of rows.
        :rtype:      int

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._n_slices()
        return ret_val




    def range(self, min, max):
        """
        Computes the range of the entire pager.
        
        :param min:  Minimum Data (Dummy if no range)
        :param max:  Maximum Data (Dummy if no range)
        :type  min:  float_ref
        :type  max:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        min.value, max.value = self._range(min.value, max.value)
        




    def get(self, col, row):
        """
        Read a single value from a 2D `GXPG <geosoft.gxapi.GXPG>`
        
        :param col:  iBx - element # in x (column #)
        :param row:  iBy - element # in y (row #)
        :type  col:  int
        :type  row:  int
        :rtype:      float

        .. versionadded:: 8.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is a low-performance method.
        """
        ret_val = self._get(col, row)
        return ret_val




    def read_col(self, col, o, n, vv):
        """
        Read a set of elements in X (column) from pager into vv
        
        :param col:  iBx - element # in x (column #)
        :param o:    iBy - begining element # in y to read (0 is the first)
        :param n:    iNy - # elements to read (0 for whole vector)
        :param vv:   hVV - `GXVV <geosoft.gxapi.GXVV>` handle
        :type  col:  int
        :type  o:    int
        :type  n:    int
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read_col(col, o, n, vv)
        




    def read_row(self, row, o, n, vv):
        """
        Read a set of elements in Y (row) from pager into vv
        
        :param row:  iBy - element # in y (row #)
        :param o:    iBx - begining element # in x to read (0 is the first)
        :param n:    iNx - # elements to read (0 for whole vector)
        :param vv:   hVV - `GXVV <geosoft.gxapi.GXVV>` handle
        :type  row:  int
        :type  o:    int
        :type  n:    int
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read_row(row, o, n, vv)
        




    def re_allocate(self, n_row, n_col):
        """
        Changes the size of Pager
        
        :param n_row:  Number of Y (rows) to reallocate
        :param n_col:  Number of X (columns) to reallocate
        :type  n_row:  int
        :type  n_col:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._re_allocate(n_row, n_col)
        




    def serial(self, bf):
        """
        Serialize a 2D `GXPG <geosoft.gxapi.GXPG>` to a `GXBF <geosoft.gxapi.GXBF>`.
        
        :type  bf:  GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** For 3D pagers, use `write_bf <geosoft.gxapi.GXPG.write_bf>`.
        """
        self._serial(bf)
        




    def statistics(self, st):
        """
        Compute the statistics of a pager object.
        
        :param st:  hST - statistics object
        :type  st:  GXST

        .. versionadded:: 6.3.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._statistics(st)
        




    def write_col(self, col, o, n, vv):
        """
        Write a set of elements in X (column) from vv into pager
        
        :param col:  iBx - element # in x (column #)
        :param o:    iBy - begining element # in y to write (0 is the first)
        :param n:    iNy - # elements to write (0 for whole vector)
        :param vv:   hVV - `GXVV <geosoft.gxapi.GXVV>` handle
        :type  col:  int
        :type  o:    int
        :type  n:    int
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_col(col, o, n, vv)
        




    def write_row(self, row, o, n, vv):
        """
        Write a set of elements in Y (row) from vv into pager
        
        :param row:  iBy - element # in y (row #)
        :param o:    iBx - begining element # in x to write (0 is the first)
        :param n:    iNx - # elements to write (0 for whole vector)
        :param vv:   hVV - `GXVV <geosoft.gxapi.GXVV>` handle
        :type  row:  int
        :type  o:    int
        :type  n:    int
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_row(row, o, n, vv)
        




# 3D Methods



    def copy_subset_3d(self, pgs, sliced, n, vv, slices, rows, cols, n_slice, n_row, n_col):
        """
        Copy a subset of data from one pager to another.
        
        :param pgs:      Source `GXPG <geosoft.gxapi.GXPG>` object
        :param sliced:   Z (slice) Origin on destination
        :param n:        Y (row) Origin on destination
        :param vv:       X (col) Origin on destination
        :param slices:   Z (slice) Origin on source
        :param rows:     Y (row) Origin on source
        :param cols:     X (col) Origin on source
        :param n_slice:  Number of Z (slice) to copy
        :param n_row:    Number of Y (rows) to copy
        :param n_col:    Number of X (columns) to copy
        :type  pgs:      GXPG
        :type  sliced:   int
        :type  n:        int
        :type  vv:       int
        :type  slices:   int
        :type  rows:     int
        :type  cols:     int
        :type  n_slice:  int
        :type  n_row:    int
        :type  n_col:    int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 2D Only
        """
        self._copy_subset_3d(pgs, sliced, n, vv, slices, rows, cols, n_slice, n_row, n_col)
        



    @classmethod
    def create_3d(cls, slice, row, col, type):
        """
        Creates a Pager object
        
        :param slice:  # elements in z (# of slices)
        :param row:    # elements in y (# of row)
        :param col:    # elements in x (# of column)
        :param type:   :ref:`GS_TYPES`
        :type  slice:  int
        :type  row:    int
        :type  col:    int
        :type  type:   int

        :returns:      `GXPG <geosoft.gxapi.GXPG>` Object
        :rtype:        GXPG

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapPG._create_3d(GXContext._get_tls_geo(), slice, row, col, type)
        return GXPG(ret_val)




    def read_col_3d(self, slice, col, o, n, vv):
        """
        Read a set of elements in X (column) from pager into vv
        
        :param slice:  iBz - element # in z (slice #)
        :param col:    iBx - element # in x (column #)
        :param o:      iBy - begining element # in y to read (0 is the first)
        :param n:      iNy - # elements to read (0 for whole vector)
        :param vv:     hVV - `GXVV <geosoft.gxapi.GXVV>` handle
        :type  slice:  int
        :type  col:    int
        :type  o:      int
        :type  n:      int
        :type  vv:     GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read_col_3d(slice, col, o, n, vv)
        




    def read_row_3d(self, slice, row, o, n, vv):
        """
        Read a set of elements in Y (row) from pager into vv
        
        :param slice:  iBz - element # in z (slice #)
        :param row:    iBy - element # in y (row #)
        :param o:      iBx - begining element # in x to read (0 is the first)
        :param n:      iNx - # elements to read (0 for whole vector)
        :param vv:     hVV - `GXVV <geosoft.gxapi.GXVV>` handle
        :type  slice:  int
        :type  row:    int
        :type  o:      int
        :type  n:      int
        :type  vv:     GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read_row_3d(slice, row, o, n, vv)
        




    def read_trace_3d(self, col, row, o, n, vv):
        """
        Read a set of elements in Z (trace) from pager into vv
        
        :param col:  iBx - element # in x (column #)
        :param row:  iBy - element # in y (row #)
        :param o:    iBy - begining element # in z to read (0 is the first)
        :param n:    iNy - # elements to read (0 for whole vector)
        :param vv:   hVV - `GXVV <geosoft.gxapi.GXVV>` handle
        :type  col:  int
        :type  row:  int
        :type  o:    int
        :type  n:    int
        :type  vv:   GXVV

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read_trace_3d(col, row, o, n, vv)
        




    def re_allocate_3d(self, n_slice, n_row, n_col):
        """
        Changes the size of 3D Pager
        
        :param n_slice:  Number of Z (slices) to reallocate
        :param n_row:    Number of Y (rows) to reallocate
        :param n_col:    Number of X (columns) to reallocate
        :type  n_slice:  int
        :type  n_row:    int
        :type  n_col:    int

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._re_allocate_3d(n_slice, n_row, n_col)
        




    def write_col_3d(self, slice, col, o, n, vv):
        """
        Write a set of elements in X (column) from vv into pager
        
        :param slice:  iBz - element # in z (slice #)
        :param col:    iBx - element # in x (column #)
        :param o:      iBy - begining element # in y to write (0 is the first)
        :param n:      iNy - # elements to write (0 for whole vector)
        :param vv:     hVV - `GXVV <geosoft.gxapi.GXVV>` handle
        :type  slice:  int
        :type  col:    int
        :type  o:      int
        :type  n:      int
        :type  vv:     GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_col_3d(slice, col, o, n, vv)
        




    def write_row_3d(self, slice, row, o, n, vv):
        """
        Write a set of elements in Y (row) from vv into pager
        
        :param slice:  iBz - element # in z (slice #)
        :param row:    iBy - element # in y (row #)
        :param o:      iBx - begining element # in x to write (0 is the first)
        :param n:      iNx - # elements to write (0 for whole vector)
        :param vv:     hVV - `GXVV <geosoft.gxapi.GXVV>` handle
        :type  slice:  int
        :type  row:    int
        :type  o:      int
        :type  n:      int
        :type  vv:     GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_row_3d(slice, row, o, n, vv)
        




    def write_trace_3d(self, col, row, o, n, vv):
        """
        Write a set of elements in Z (trace) from pager into vv
        
        :param col:  iBx - element # in x (column #)
        :param row:  iBy - element # in y (row #)
        :param o:    iBy - begining element # in z to read (0 is the first)
        :param n:    iNy - # elements to read (0 for whole vector)
        :param vv:   hVV - `GXVV <geosoft.gxapi.GXVV>` handle
        :type  col:  int
        :type  row:  int
        :type  o:    int
        :type  n:    int
        :type  vv:   GXVV

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_trace_3d(col, row, o, n, vv)
        




# Utility Methods



    def read_bf(self, bf, dir, conv, rev_x, rev_y, rev_z):
        """
        Read the contents of a 2D or 3D pager to from a `GXBF <geosoft.gxapi.GXBF>`.
        
        :param bf:     `GXBF <geosoft.gxapi.GXBF>` to read from
        :param dir:    :ref:`PG_3D_DIR`
        :param conv:   :ref:`PG_BF_CONV`
        :param rev_x:  Reverse X
        :param rev_y:  Reverse Y
        :param rev_z:  Reverse Z
        :type  bf:     GXBF
        :type  dir:    int
        :type  conv:   int
        :type  rev_x:  int
        :type  rev_y:  int
        :type  rev_z:  int

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read_bf(bf, dir, conv, rev_x, rev_y, rev_z)
        




    def read_ra(self, ra, dir, rev_x, rev_y, rev_z, dummy):
        """
        Read the contents of a 2D or 3D pager to from an `GXRA <geosoft.gxapi.GXRA>`.
        
        :param ra:     `GXRA <geosoft.gxapi.GXRA>` to read from
        :param dir:    :ref:`PG_3D_DIR`
        :param rev_x:  Reverse X
        :param rev_y:  Reverse Y
        :param rev_z:  Reverse Z
        :param dummy:  Dummy
        :type  ra:     GXRA
        :type  dir:    int
        :type  rev_x:  int
        :type  rev_y:  int
        :type  rev_z:  int
        :type  dummy:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Each line must hold only 1 value
        """
        self._read_ra(ra, dir, rev_x, rev_y, rev_z, dummy.encode())
        




    def write_bf(self, bf, dir, conv, rev_x, rev_y, rev_z):
        """
        Write the contents of a 2D or 3D pager to a `GXBF <geosoft.gxapi.GXBF>`.
        
        :param bf:     `GXBF <geosoft.gxapi.GXBF>` to write to
        :param dir:    :ref:`PG_3D_DIR`
        :param conv:   :ref:`PG_BF_CONV`
        :param rev_x:  Reverse X
        :param rev_y:  Reverse Y
        :param rev_z:  Reverse Z
        :type  bf:     GXBF
        :type  dir:    int
        :type  conv:   int
        :type  rev_x:  int
        :type  rev_y:  int
        :type  rev_z:  int

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_bf(bf, dir, conv, rev_x, rev_y, rev_z)
        




    def write_bf_ex(self, bf, dir, conv, rev_x, rev_y, rev_z, p_dummy):
        """
        Write the contents of a 2D or 3D pager to a `GXBF <geosoft.gxapi.GXBF>`.
        
        :param bf:       `GXBF <geosoft.gxapi.GXBF>` to write to
        :param dir:      :ref:`PG_3D_DIR`
        :param conv:     :ref:`PG_BF_CONV`
        :param rev_x:    Reverse X
        :param rev_y:    Reverse Y
        :param rev_z:    Reverse Z
        :param p_dummy:  Dummy value
        :type  bf:       GXBF
        :type  dir:      int
        :type  conv:     int
        :type  rev_x:    int
        :type  rev_y:    int
        :type  rev_z:    int
        :type  p_dummy:  float

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_bf_ex(bf, dir, conv, rev_x, rev_y, rev_z, p_dummy)
        




    def write_wa(self, wa, dir, rev_x, rev_y, rev_z, dummy):
        """
        Write the contents of a 2D or 3D pager to a `GXWA <geosoft.gxapi.GXWA>`
        
        :param wa:     `GXWA <geosoft.gxapi.GXWA>` to write to
        :param dir:    :ref:`PG_3D_DIR`
        :param rev_x:  Reverse X
        :param rev_y:  Reverse Y
        :param rev_z:  Reverse Z
        :param dummy:  Dummy
        :type  wa:     GXWA
        :type  dir:    int
        :type  rev_x:  int
        :type  rev_y:  int
        :type  rev_z:  int
        :type  dummy:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Each line will hold only 1 value
        """
        self._write_wa(wa, dir, rev_x, rev_y, rev_z, dummy.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer