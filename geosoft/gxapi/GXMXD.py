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
class GXMXD(gxapi_cy.WrapMXD):
    """
    GXMXD class.

    A `GXMXD <geosoft.gxapi.GXMXD>` wraps and provides manipulation and usage for
    the content of an ArcGIS `GXMXD <geosoft.gxapi.GXMXD>` file.
    """

    def __init__(self, handle=0):
        super(GXMXD, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMXD <geosoft.gxapi.GXMXD>`
        
        :returns: A null `GXMXD <geosoft.gxapi.GXMXD>`
        :rtype:   GXMXD
        """
        return GXMXD()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def commit(self):
        """
        
        .. deprecated:: None None 
        Commit any changes to a `GXMXD <geosoft.gxapi.GXMXD>`.
        

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        warnings.warn("""Deprecated since unknown, """, )
        self._commit()
        



    @classmethod
    def create(cls, name):
        """
        
        .. deprecated:: None None 
        Create a `GXMXD <geosoft.gxapi.GXMXD>`.
        
        :param name:  `GXMXD <geosoft.gxapi.GXMXD>` file name
        :type  name:  str

        :returns:     `GXMXD <geosoft.gxapi.GXMXD>` Object
        :rtype:       GXMXD

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        warnings.warn("""Deprecated since unknown, """, )
        ret_val = gxapi_cy.WrapMXD._create(GXContext._get_tls_geo(), name.encode())
        return GXMXD(ret_val)



    @classmethod
    def create_metadata(cls, mxd):
        """
        
        Create metadata for this brand new `GXMXD <geosoft.gxapi.GXMXD>` (we are the creator)
        
        :param mxd:  `GXMXD <geosoft.gxapi.GXMXD>` file name
        :type  mxd:  str

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapMXD._create_metadata(GXContext._get_tls_geo(), mxd.encode())
        






    def discard(self):
        """
        
        .. deprecated:: None None 
        Discard all changes made to the `GXMXD <geosoft.gxapi.GXMXD>`.
        

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        warnings.warn("""Deprecated since unknown, """, )
        self._discard()
        




    def save_as_map(self, map, focus_map_only):
        """
        
        .. deprecated:: None None 
        Save `GXMXD <geosoft.gxapi.GXMXD>` as Geosoft map
        
        :param map:             Geosoft map file name
        :param focus_map_only:  Export focus map only?
        :type  map:             str
        :type  focus_map_only:  bool

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        warnings.warn("""Deprecated since unknown, """, )
        self._save_as_map(map.encode(), focus_map_only)
        



    @classmethod
    def convert_to_map(cls, mxd, map):
        """
        
        Create Geosoft map from ArcGIS `GXMXD <geosoft.gxapi.GXMXD>`
        
        :param mxd:  ArcGIS `GXMXD <geosoft.gxapi.GXMXD>` file name
        :param map:  Geosoft map file name
        :type  mxd:  str
        :type  map:  str

        .. versionadded:: 9.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapMXD._convert_to_map(GXContext._get_tls_geo(), mxd.encode(), map.encode())
        




    def save_as_mxd(self, mxdHandle):
        """
        
        .. deprecated:: None None 
        Save `GXMXD <geosoft.gxapi.GXMXD>` as a `GXMXD <geosoft.gxapi.GXMXD>` in different location
        
        :param mxdHandle:  `GXMXD <geosoft.gxapi.GXMXD>` file name
        :type  mxdHandle:  str

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        warnings.warn("""Deprecated since unknown, """, )
        self._save_as_mxd(mxdHandle.encode())
        



    @classmethod
    def sync(cls, mxd):
        """
        
        Syncronize any Metadata for this `GXMXD <geosoft.gxapi.GXMXD>`
        
        :param mxd:  `GXMXD <geosoft.gxapi.GXMXD>` file name
        :type  mxd:  str

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapMXD._sync(GXContext._get_tls_geo(), mxd.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer