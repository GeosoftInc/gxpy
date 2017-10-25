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
class GXDAT:
    """
    GXDAT class.

    The `GXDAT` object is used to access data from an variety of data sources
    using the same access functions. The `GXDAT` interface supports data access
    on a point-by-point, of line-by-line basis.  For example,
    the `GXBIGRID.run` function uses 2 `GXDAT` objects - one `GXDAT` associated with the
    input data source, which is read line-by-line, and a second associated with
    the output grid file output grid file.
    
    Use a specific `GXDAT` creation method for an associated
    information source in order to make a `GXDAT` as required
    by a specific processing function.  The gridding methods all use DATs.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDAT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDAT`
        
        :returns: A null `GXDAT`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDAT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDAT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_db(cls, p1, p2, p3, p4):
        """
        Create a handle to a database `GXDAT` object
        """
        ret_val = gxapi_cy.WrapDAT.create_db(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode())
        return GXDAT(ret_val)



    @classmethod
    def create_xgd(cls, p1, p2):
        """
        Create a handle to a grid file `GXDAT` object
        """
        ret_val = gxapi_cy.WrapDAT.create_xgd(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXDAT(ret_val)





    @classmethod
    def get_lst(cls, p1, p2, p3, p4):
        """
        Put available `GXDAT` filters and qualifiers in a `GXLST`

        **Note:**

        The filters displayed in the Grid/Image file browse dialog are put
        in the "Name" of the `GXLST`, while the file qualifiers are stored in
        the "Value".
        """
        gxapi_cy.WrapDAT.get_lst(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        




    def range_xyz(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Determine the range in X, Y and Z in the `GXDAT` source

        **Note:**

        Terminates if unable to open an RPT `GXDAT` interface.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value = self._wrapper.range_xyz(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer