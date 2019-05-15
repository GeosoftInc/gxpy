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
class GXFLT(gxapi_cy.WrapFLT):
    """
    GXFLT class.

    The `GXFLT <geosoft.gxapi.GXFLT>` class allows the application of user-defined convolution filters to data in an OASIS database
    """

    def __init__(self, handle=0):
        super(GXFLT, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXFLT <geosoft.gxapi.GXFLT>`
        
        :returns: A null `GXFLT <geosoft.gxapi.GXFLT>`
        :rtype:   GXFLT
        """
        return GXFLT()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, input):
        """
        Create a filter from a comma/space delimited string.
        
        :param input:  Filter string
        :type  input:  str

        :returns:      `GXFLT <geosoft.gxapi.GXFLT>` Object
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Terminates process if filter not found.
        Sample Fraser Filter string:

              "-1,-1,1,1"
        """
        ret_val = gxapi_cy.WrapFLT._create(GXContext._get_tls_geo(), input.encode())
        return ret_val





    @classmethod
    def load(cls, file):
        """
        Load and return handle to a convolution filter.
        
        :param file:  Name of the filter File
        :type  file:  str

        :returns:     `GXFLT <geosoft.gxapi.GXFLT>` Object
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Terminates process if filter not found.
        A filter file is an ASCII file that contains filter
        coefficients, which are simply mumbers.  There can be
        one coefficient to a line.  Blank lines and comment lines
        are skipped.  Comment lines beginn with a forward slash
        character in column 1.  Following is an example Fraser
        Filter file:

           /----------------------
           / Fraser Filter
           /----------------------
           -1
           -1
           1
           1
        """
        ret_val = gxapi_cy.WrapFLT._load(GXContext._get_tls_geo(), file.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer