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

    Typically a grid is accessed using the :class:`geosoft.gxapi.GXIMG` class, and a :class:`geosoft.gxapi.GXPG`
    is obtained from the :class:`geosoft.gxapi.GXIMG` using the GetPG_IMG function.
    Following operations on the :class:`geosoft.gxapi.GXPG`, it can be written back to
    the :class:`geosoft.gxapi.GXIMG` using SetPG_IMG.
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXPG`
        
        :returns: A null :class:`geosoft.gxapi.GXPG`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXPG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXPG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# 2D Methods



    def copy(self, p2):
        """
        Copy the data from one pager to another.
        """
        self._wrapper.copy(p2._wrapper)
        




    def copy_subset(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Copy a subset of data from one pager to another.

        **Note:**

        2D Only
        """
        self._wrapper.copy_subset(p2._wrapper, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def create(cls, p1, p2, p3):
        """
        Creates a Pager object
        """
        ret_val = gxapi_cy.WrapPG.create(GXContext._get_tls_geo(), p1, p2, p3)
        return GXPG(ret_val)



    @classmethod
    def create_s(cls, p1):
        """
        Create a 2D :class:`geosoft.gxapi.GXPG` from serialized source.

        **Note:**

        For 3D pagers, use CreateBF_PG.
        """
        ret_val = gxapi_cy.WrapPG.create_s(GXContext._get_tls_geo(), p1._wrapper)
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




    def range(self, p2, p3):
        """
        Computes the range of the entire pager.
        """
        p2.value, p3.value = self._wrapper.range(p2.value, p3.value)
        




    def get(self, p2, p3):
        """
        Read a single value from a 2D :class:`geosoft.gxapi.GXPG`

        **Note:**

        This is a low-performance method.
        """
        ret_val = self._wrapper.get(p2, p3)
        return ret_val




    def read_col(self, p2, p3, p4, p5):
        """
        Read a set of elements in X (column) from pager into vv
        """
        self._wrapper.read_col(p2, p3, p4, p5._wrapper)
        




    def read_row(self, p2, p3, p4, p5):
        """
        Read a set of elements in Y (row) from pager into vv
        """
        self._wrapper.read_row(p2, p3, p4, p5._wrapper)
        




    def re_allocate(self, p2, p3):
        """
        Changes the size of Pager
        """
        self._wrapper.re_allocate(p2, p3)
        




    def serial(self, p2):
        """
        Serialize a 2D :class:`geosoft.gxapi.GXPG` to a :class:`geosoft.gxapi.GXBF`.

        **Note:**

        For 3D pagers, use WriteBF_PG.
        """
        self._wrapper.serial(p2._wrapper)
        




    def statistics(self, p2):
        """
        Compute the statistics of a pager object.
        """
        self._wrapper.statistics(p2._wrapper)
        




    def write_col(self, p2, p3, p4, p5):
        """
        Write a set of elements in X (column) from vv into pager
        """
        self._wrapper.write_col(p2, p3, p4, p5._wrapper)
        




    def write_row(self, p2, p3, p4, p5):
        """
        Write a set of elements in Y (row) from vv into pager
        """
        self._wrapper.write_row(p2, p3, p4, p5._wrapper)
        




# 3D Methods



    def copy_subset_3d(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Copy a subset of data from one pager to another.

        **Note:**

        2D Only
        """
        self._wrapper.copy_subset_3d(p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def create_3d(cls, p1, p2, p3, p4):
        """
        Creates a Pager object
        """
        ret_val = gxapi_cy.WrapPG.create_3d(GXContext._get_tls_geo(), p1, p2, p3, p4)
        return GXPG(ret_val)




    def read_col_3d(self, p2, p3, p4, p5, p6):
        """
        Read a set of elements in X (column) from pager into vv
        """
        self._wrapper.read_col_3d(p2, p3, p4, p5, p6._wrapper)
        




    def read_row_3d(self, p2, p3, p4, p5, p6):
        """
        Read a set of elements in Y (row) from pager into vv
        """
        self._wrapper.read_row_3d(p2, p3, p4, p5, p6._wrapper)
        




    def read_trace_3d(self, p2, p3, p4, p5, p6):
        """
        Read a set of elements in Z (trace) from pager into vv
        """
        self._wrapper.read_trace_3d(p2, p3, p4, p5, p6._wrapper)
        




    def re_allocate_3d(self, p2, p3, p4):
        """
        Changes the size of 3D Pager
        """
        self._wrapper.re_allocate_3d(p2, p3, p4)
        




    def write_col_3d(self, p2, p3, p4, p5, p6):
        """
        Write a set of elements in X (column) from vv into pager
        """
        self._wrapper.write_col_3d(p2, p3, p4, p5, p6._wrapper)
        




    def write_row_3d(self, p2, p3, p4, p5, p6):
        """
        Write a set of elements in Y (row) from vv into pager
        """
        self._wrapper.write_row_3d(p2, p3, p4, p5, p6._wrapper)
        




    def write_trace_3d(self, p2, p3, p4, p5, p6):
        """
        Write a set of elements in Z (trace) from pager into vv
        """
        self._wrapper.write_trace_3d(p2, p3, p4, p5, p6._wrapper)
        




# Utility Methods



    def read_bf(self, p2, p3, p4, p5, p6, p7):
        """
        Read the contents of a 2D or 3D pager to from a :class:`geosoft.gxapi.GXBF`.
        """
        self._wrapper.read_bf(p2._wrapper, p3, p4, p5, p6, p7)
        




    def read_ra(self, p2, p3, p4, p5, p6, p7):
        """
        Read the contents of a 2D or 3D pager to from an :class:`geosoft.gxapi.GXRA`.

        **Note:**

        Each line must hold only 1 value
        """
        self._wrapper.read_ra(p2._wrapper, p3, p4, p5, p6, p7.encode())
        




    def write_bf(self, p2, p3, p4, p5, p6, p7):
        """
        Write the contents of a 2D or 3D pager to a :class:`geosoft.gxapi.GXBF`.
        """
        self._wrapper.write_bf(p2._wrapper, p3, p4, p5, p6, p7)
        




    def write_bf_ex(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Write the contents of a 2D or 3D pager to a :class:`geosoft.gxapi.GXBF`.
        """
        self._wrapper.write_bf_ex(p2._wrapper, p3, p4, p5, p6, p7, p8)
        




    def write_wa(self, p2, p3, p4, p5, p6, p7):
        """
        Write the contents of a 2D or 3D pager to a :class:`geosoft.gxapi.GXWA`

        **Note:**

        Each line will hold only 1 value
        """
        self._wrapper.write_wa(p2._wrapper, p3, p4, p5, p6, p7.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer