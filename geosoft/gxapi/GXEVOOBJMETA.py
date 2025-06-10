#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.

### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
import warnings
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEVOOBJMETA(gxapi_cy.WrapEVOOBJMETA):
    """
    GXEVOOBJMETA class.

    The `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` class is used to create Evo object metadata including object uuid, object path,
    version id, created at, created by, etag, workspace id, modified at, modified by and bounding box properties.

    **Note:**

    
    """

    def __init__(self, handle=0):
        super(GXEVOOBJMETA, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>`
        
        :returns: A null `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>`
        :rtype:   GXEVOOBJMETA
        """
        return GXEVOOBJMETA()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create_default(cls):
        """
        
        Create an empty `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object.
        

        :returns:    `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object
        :rtype:      GXEVOOBJMETA

        .. versionadded:: 2025.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = gxapi_cy.WrapEVOOBJMETA._create_default(GXContext._get_tls_geo())
        return GXEVOOBJMETA(ret_val)



    @classmethod
    def create(cls, metadata):
        """
        
        Create an `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object.
        
        :param metadata:  Evo object metadata in JSON string, refer to H_EVOOBJMETA or annotations for Seequent.Evo.Client.Api.Core.GeoscienceObjectMetadata
        :type  metadata:  str

        :returns:         `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object
        :rtype:           GXEVOOBJMETA

        .. versionadded:: 2025.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = gxapi_cy.WrapEVOOBJMETA._create(GXContext._get_tls_geo(), metadata.encode())
        return GXEVOOBJMETA(ret_val)






    def get_workspace_id(self, workspace_id):
        """
        
        Return the Evo workspace Id.
        
        :param workspace_id:  workspace id
        :type  workspace_id:  str_ref

        .. versionadded:: 2025.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        workspace_id.value = self._get_workspace_id(workspace_id.value.encode())
        




    def get_object_id(self, object_id):
        """
        
        Return the Evo object Id.
        
        :param object_id:  object id
        :type  object_id:  str_ref

        .. versionadded:: 2025.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        object_id.value = self._get_object_id(object_id.value.encode())
        




    def get_modified_at(self, modified_at):
        """
        
        Return the Evo object modified at.
        
        :param modified_at:  modified at
        :type  modified_at:  str_ref

        .. versionadded:: 2025.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        modified_at.value = self._get_modified_at(modified_at.value.encode())
        




    def get_bounding_box(self, bounding_box):
        """
        
        Get Evo object bounding box in JSON string.
        
        :param bounding_box:  JSON string for bounding box, refer to H_EVOBOUNDINGBOX or annotations for Seequent.Evo.Client.Api.Core.Goose.Model.BoundingBox
        :type  bounding_box:  str_ref

        .. versionadded:: 2025.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        bounding_box.value = self._get_bounding_box(bounding_box.value.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer