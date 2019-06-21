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
class GXMISC(gxapi_cy.WrapMISC):
    """
    GXMISC class.

    Not a class. A catch-all for miscellaneous geophysical
    methods, primarily file conversions.
    """

    def __init__(self, handle=0):
        super(GXMISC, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMISC <geosoft.gxapi.GXMISC>`
        
        :returns: A null `GXMISC <geosoft.gxapi.GXMISC>`
        :rtype:   GXMISC
        """
        return GXMISC()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def convert_cg3to_raw(cls, cg3, raw, tide_corr_opt):
        """
        Convert a CG3 dump to RAW format.
        
        :param cg3:            Name of the CG3 file
        :param raw:            Name of the RAW file
        :param tide_corr_opt:  TideCorr Option: 1 - use geosoft, 0 - use CG3/CG5
        :type  cg3:            str
        :type  raw:            str
        :type  tide_corr_opt:  int

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMISC._convert_cg3to_raw(GXContext._get_tls_geo(), cg3.encode(), raw.encode(), tide_corr_opt)
        



    @classmethod
    def convert_cg5to_raw(cls, cg5, raw, tide_corr_opt):
        """
        Convert a CG5 dump to RAW format.
        
        :param cg5:            Name of the CG5 file
        :param raw:            Name of the RAW file
        :param tide_corr_opt:  TideCorr Option: 1 - use geosoft, 0 - use CG3/CG5
        :type  cg5:            str
        :type  raw:            str
        :type  tide_corr_opt:  int

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMISC._convert_cg5to_raw(GXContext._get_tls_geo(), cg5.encode(), raw.encode(), tide_corr_opt)
        



    @classmethod
    def ukoa2_tbl(cls, ukoa, alias, tbl):
        """
        Convert a UKOA file to a location TBL file.
        
        :param ukoa:   Name of the UKOA file
        :param alias:  Line name alias table
        :param tbl:    Name of the output table
        :type  ukoa:   str
        :type  alias:  str
        :type  tbl:    str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The TBL file will contain the following fields:

        = Line:string16
        = Station:long
        = Latitude:double
        = Longitude:double
        = X:double
        = Y:double
        = Elevation:double
        """
        gxapi_cy.WrapMISC._ukoa2_tbl(GXContext._get_tls_geo(), ukoa.encode(), alias.encode(), tbl.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer