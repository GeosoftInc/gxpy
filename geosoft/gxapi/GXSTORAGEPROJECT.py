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
class GXSTORAGEPROJECT(gxapi_cy.WrapSTORAGEPROJECT):
    """
    GXSTORAGEPROJECT class.

    Project Storage.
    """

    def __init__(self, handle=0):
        super(GXSTORAGEPROJECT, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSTORAGEPROJECT <geosoft.gxapi.GXSTORAGEPROJECT>`
        
        :returns: A null `GXSTORAGEPROJECT <geosoft.gxapi.GXSTORAGEPROJECT>`
        :rtype:   GXSTORAGEPROJECT
        """
        return GXSTORAGEPROJECT()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def open(cls, name):
        """
        Open a project storage.
        
        :param name:  Project File Name
        :type  name:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSTORAGEPROJECT._open(GXContext._get_tls_geo(), name.encode())
        



    @classmethod
    def close(cls):
        """
        Close the project storage.
        

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSTORAGEPROJECT._close(GXContext._get_tls_geo())
        



    @classmethod
    def remove_dataset(cls, name):
        """
        Remove this dataset from the project.
        
        :param name:  Dataset File Name
        :type  name:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSTORAGEPROJECT._remove_dataset(GXContext._get_tls_geo(), name.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer