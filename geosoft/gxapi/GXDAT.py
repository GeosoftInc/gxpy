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

    The :class:`geosoft.gxapi.GXDAT` object is used to access data from an variety of data sources
    using the same access functions. The :class:`geosoft.gxapi.GXDAT` interface supports data access
    on a point-by-point, of line-by-line basis.  For example,
    the Run_BIGRID function uses 2 :class:`geosoft.gxapi.GXDAT` objects - one :class:`geosoft.gxapi.GXDAT` associated with the
    input data source, which is read line-by-line, and a second associated with
    the output grid file output grid file.
    
    Use a specific :class:`geosoft.gxapi.GXDAT` creation method for an associated
    information source in order to make a :class:`geosoft.gxapi.GXDAT` as required
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXDAT`
        
        :returns: A null :class:`geosoft.gxapi.GXDAT`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXDAT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXDAT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_db(cls, p1, p2, p3, p4):
        """
        Create a handle to a database :class:`geosoft.gxapi.GXDAT` object
        """
        ret_val = gxapi_cy.WrapDAT.create_db(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode())
        return GXDAT(ret_val)



    @classmethod
    def create_xgd(cls, p1, p2):
        """
        Create a handle to a grid file :class:`geosoft.gxapi.GXDAT` object
        """
        ret_val = gxapi_cy.WrapDAT.create_xgd(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXDAT(ret_val)





    @classmethod
    def get_lst(cls, p1, p2, p3, p4):
        """
        Put available :class:`geosoft.gxapi.GXDAT` filters and qualifiers in a :class:`geosoft.gxapi.GXLST`

        **Note:**

        The filters displayed in the Grid/Image file browse dialog are put
        in the "Name" of the :class:`geosoft.gxapi.GXLST`, while the file qualifiers are stored in
        the "Value".
        """
        gxapi_cy.WrapDAT.get_lst(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        




    def range_xyz(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Determine the range in X, Y and Z in the :class:`geosoft.gxapi.GXDAT` source

        **Note:**

        Terminates if unable to open an RPT :class:`geosoft.gxapi.GXDAT` interface.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value = self._wrapper.range_xyz(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer