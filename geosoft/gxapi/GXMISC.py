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
class GXMISC:
    """
    GXMISC class.

    Not a class. A catch-all for miscellaneous geophysical
    methods, primarily file conversions.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMISC(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMISC`
        
        :returns: A null `GXMISC`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXMISC` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXMISC`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def convert_cg3to_raw(cls, cg3, raw, tide_corr_opt):
        """
        Convert a CG3 dump to RAW format.
        """
        gxapi_cy.WrapMISC.convert_cg3to_raw(GXContext._get_tls_geo(), cg3.encode(), raw.encode(), tide_corr_opt)
        



    @classmethod
    def convert_cg5to_raw(cls, cg5, raw, tide_corr_opt):
        """
        Convert a CG5 dump to RAW format.
        """
        gxapi_cy.WrapMISC.convert_cg5to_raw(GXContext._get_tls_geo(), cg5.encode(), raw.encode(), tide_corr_opt)
        



    @classmethod
    def ukoa2_tbl(cls, ukoa, alias, tbl):
        """
        Convert a UKOA file to a location TBL file.

        **Note:**

        The TBL file will contain the following fields:
        
        = Line:string16
        = Station:long
        = Latitude:double
        = Longitude:double
        = X:double
        = Y:double
        = Elevation:double
        """
        gxapi_cy.WrapMISC.ukoa2_tbl(GXContext._get_tls_geo(), ukoa.encode(), alias.encode(), tbl.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer