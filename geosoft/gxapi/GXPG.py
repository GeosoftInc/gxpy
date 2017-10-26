### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXPG:
    """
    GXPG class.

    Pager methods for large 2-D arrays
    This class handles very-large 2-D arrays in which efficient
    access is required along both rows and columns.

    **Note:**

    Typically a grid is accessed using the `GXIMG` class, and a `GXPG`
    is obtained from the `GXIMG` using the `GXIMG.get_pg` function.
    Following operations on the `GXPG`, it can be written back to
    the `GXIMG` using `GXIMG.set_pg`.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPG(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPG`
        
        :returns: A null `GXPG`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXPG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXPG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# 2D Methods



    def copy(self, pgs):
        """
        Copy the data from one pager to another.
        """
        self._wrapper.copy(pgs._wrapper)
        




    def copy_subset(self, pgs, y_row_d, x_col_d, y_row_s, x_col_s, ny, nx):
        """
        Copy a subset of data from one pager to another.

        **Note:**

        2D Only
        """
        self._wrapper.copy_subset(pgs._wrapper, y_row_d, x_col_d, y_row_s, x_col_s, ny, nx)
        



    @classmethod
    def create(cls, row, p2, p3):
        """
        Creates a Pager object
        """
        ret_val = gxapi_cy.WrapPG.create(GXContext._get_tls_geo(), row, p2, p3)
        return GXPG(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create a 2D `GXPG` from serialized source.

        **Note:**

        For 3D pagers, use CreateBF_PG.
        """
        ret_val = gxapi_cy.WrapPG.create_s(GXContext._get_tls_geo(), bf._wrapper)
        return GXPG(ret_val)






    def dummy(self):
        """
        Sets the Entire pager to dummy.
        """
        self._wrapper.dummy()
        




    def e_type(self):
        """
        Gets the type of pager.
        """
        ret_val = self._wrapper.e_type()
        return ret_val




    def n_cols(self):
        """
        Gets the # of columns in pager.
        """
        ret_val = self._wrapper.n_cols()
        return ret_val




    def n_rows(self):
        """
        Gets the # of rows in pager.
        """
        ret_val = self._wrapper.n_rows()
        return ret_val




    def n_slices(self):
        """
        Gets the # of slices (z) in pager.
        """
        ret_val = self._wrapper.n_slices()
        return ret_val




    def range(self, min, max):
        """
        Computes the range of the entire pager.
        """
        min.value, max.value = self._wrapper.range(min.value, max.value)
        




    def get(self, col, p3):
        """
        Read a single value from a 2D `GXPG`

        **Note:**

        This is a low-performance method.
        """
        ret_val = self._wrapper.get(col, p3)
        return ret_val




    def read_col(self, col, o, n, vv):
        """
        Read a set of elements in X (column) from pager into vv
        """
        self._wrapper.read_col(col, o, n, vv._wrapper)
        




    def read_row(self, row, o, n, vv):
        """
        Read a set of elements in Y (row) from pager into vv
        """
        self._wrapper.read_row(row, o, n, vv._wrapper)
        




    def re_allocate(self, n_row, p3):
        """
        Changes the size of Pager
        """
        self._wrapper.re_allocate(n_row, p3)
        




    def serial(self, bf):
        """
        Serialize a 2D `GXPG` to a `GXBF`.

        **Note:**

        For 3D pagers, use `write_bf`.
        """
        self._wrapper.serial(bf._wrapper)
        




    def statistics(self, st):
        """
        Compute the statistics of a pager object.
        """
        self._wrapper.statistics(st._wrapper)
        




    def write_col(self, col, o, n, vv):
        """
        Write a set of elements in X (column) from vv into pager
        """
        self._wrapper.write_col(col, o, n, vv._wrapper)
        




    def write_row(self, row, o, n, vv):
        """
        Write a set of elements in Y (row) from vv into pager
        """
        self._wrapper.write_row(row, o, n, vv._wrapper)
        




# 3D Methods



    def copy_subset_3d(self, pgs, sliced, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Copy a subset of data from one pager to another.

        **Note:**

        2D Only
        """
        self._wrapper.copy_subset_3d(pgs._wrapper, sliced, p4, p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def create_3d(cls, slice, p2, p3, p4):
        """
        Creates a Pager object
        """
        ret_val = gxapi_cy.WrapPG.create_3d(GXContext._get_tls_geo(), slice, p2, p3, p4)
        return GXPG(ret_val)




    def read_col_3d(self, slice, col, o, n, vv):
        """
        Read a set of elements in X (column) from pager into vv
        """
        self._wrapper.read_col_3d(slice, col, o, n, vv._wrapper)
        




    def read_row_3d(self, slice, row, o, n, vv):
        """
        Read a set of elements in Y (row) from pager into vv
        """
        self._wrapper.read_row_3d(slice, row, o, n, vv._wrapper)
        




    def read_trace_3d(self, col, row, o, n, vv):
        """
        Read a set of elements in Z (trace) from pager into vv
        """
        self._wrapper.read_trace_3d(col, row, o, n, vv._wrapper)
        




    def re_allocate_3d(self, n_slice, p3, p4):
        """
        Changes the size of 3D Pager
        """
        self._wrapper.re_allocate_3d(n_slice, p3, p4)
        




    def write_col_3d(self, slice, col, o, n, vv):
        """
        Write a set of elements in X (column) from vv into pager
        """
        self._wrapper.write_col_3d(slice, col, o, n, vv._wrapper)
        




    def write_row_3d(self, slice, row, o, n, vv):
        """
        Write a set of elements in Y (row) from vv into pager
        """
        self._wrapper.write_row_3d(slice, row, o, n, vv._wrapper)
        




    def write_trace_3d(self, col, row, o, n, vv):
        """
        Write a set of elements in Z (trace) from pager into vv
        """
        self._wrapper.write_trace_3d(col, row, o, n, vv._wrapper)
        




# Utility Methods



    def read_bf(self, bf, dir, conv, rev_x, rev_y, rev_z):
        """
        Read the contents of a 2D or 3D pager to from a `GXBF`.
        """
        self._wrapper.read_bf(bf._wrapper, dir, conv, rev_x, rev_y, rev_z)
        




    def read_ra(self, ra, dir, rev_x, rev_y, rev_z, dummy):
        """
        Read the contents of a 2D or 3D pager to from an `GXRA`.

        **Note:**

        Each line must hold only 1 value
        """
        self._wrapper.read_ra(ra._wrapper, dir, rev_x, rev_y, rev_z, dummy.encode())
        




    def write_bf(self, bf, dir, conv, rev_x, rev_y, rev_z):
        """
        Write the contents of a 2D or 3D pager to a `GXBF`.
        """
        self._wrapper.write_bf(bf._wrapper, dir, conv, rev_x, rev_y, rev_z)
        




    def write_bf_ex(self, bf, dir, conv, rev_x, rev_y, rev_z, p_dummy):
        """
        Write the contents of a 2D or 3D pager to a `GXBF`.
        """
        self._wrapper.write_bf_ex(bf._wrapper, dir, conv, rev_x, rev_y, rev_z, p_dummy)
        




    def write_wa(self, wa, dir, rev_x, rev_y, rev_z, dummy):
        """
        Write the contents of a 2D or 3D pager to a `GXWA`

        **Note:**

        Each line will hold only 1 value
        """
        self._wrapper.write_wa(wa._wrapper, dir, rev_x, rev_y, rev_z, dummy.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer