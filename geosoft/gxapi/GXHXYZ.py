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
class GXHXYZ(gxapi_cy.WrapHXYZ):
    """
    GXHXYZ class.

    High Performance Data Point Storage. This is used
    to put Point data on a DAP server. It is compressed
    and uses a Quad-Tree design to allow very high speed
    data extraction. It is also multi-threaded.
    """

    def __init__(self, handle=0):
        super(GXHXYZ, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXHXYZ <geosoft.gxapi.GXHXYZ>`
        
        :returns: A null `GXHXYZ <geosoft.gxapi.GXHXYZ>`
        :rtype:   GXHXYZ
        """
        return GXHXYZ()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, name):
        """
        
        Create a handle to an `GXHXYZ <geosoft.gxapi.GXHXYZ>` object
        
        :param name:  File Name
        :type  name:  str

        :returns:     `GXHXYZ <geosoft.gxapi.GXHXYZ>` Object
        :rtype:       GXHXYZ

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = gxapi_cy.WrapHXYZ._create(GXContext._get_tls_geo(), name.encode())
        return GXHXYZ(ret_val)






    def get_meta(self, meta):
        """
        
        Get the metadata of a grid.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to save `GXHXYZ <geosoft.gxapi.GXHXYZ>`'s meta to
        :type  meta:  GXMETA

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        self._get_meta(meta)
        



    @classmethod
    def h_create_db(cls, db, gvv, name):
        """
        
        Make an `GXHXYZ <geosoft.gxapi.GXHXYZ>` from GDB
        
        :param db:    `GXDB <geosoft.gxapi.GXDB>` handle
        :param gvv:   `GXVV <geosoft.gxapi.GXVV>` of channels to export
        :param name:  Name of `GXHXYZ <geosoft.gxapi.GXHXYZ>` object
        :type  db:    GXDB
        :type  gvv:   GXVV
        :type  name:  str

        :returns:     `GXHXYZ <geosoft.gxapi.GXHXYZ>` object
        :rtype:       GXHXYZ

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = gxapi_cy.WrapHXYZ._h_create_db(GXContext._get_tls_geo(), db, gvv, name.encode())
        return GXHXYZ(ret_val)



    @classmethod
    def h_create_sql(cls, templ, x, y, z, ipj, name):
        """
        
        Make an `GXHXYZ <geosoft.gxapi.GXHXYZ>` from SQL Query
        
        :param templ:  Template File Name
        :param x:      X field name
        :param y:      Y field name
        :param z:      Z field name
        :param ipj:    Projection of data values
        :param name:   Name of `GXHXYZ <geosoft.gxapi.GXHXYZ>` object
        :type  templ:  str
        :type  x:      str
        :type  y:      str
        :type  z:      str
        :type  ipj:    GXIPJ
        :type  name:   str

        :returns:      `GXHXYZ <geosoft.gxapi.GXHXYZ>` object
        :rtype:        GXHXYZ

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = gxapi_cy.WrapHXYZ._h_create_sql(GXContext._get_tls_geo(), templ.encode(), x.encode(), y.encode(), z.encode(), ipj, name.encode())
        return GXHXYZ(ret_val)




    def set_meta(self, meta):
        """
        
        Set the metadata of a grid.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to add to `GXHXYZ <geosoft.gxapi.GXHXYZ>`'s meta
        :type  meta:  GXMETA

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        self._set_meta(meta)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer