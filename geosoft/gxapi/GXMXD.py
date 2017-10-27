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
class GXMXD:
    """
    GXMXD class.

    A `GXMXD <geosoft.gxapi.GXMXD>` wraps and provides manipulation and usage for
    the content of an ArcGIS `GXMXD <geosoft.gxapi.GXMXD>` file.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMXD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMXD`
        
        :returns: A null `GXMXD`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXMXD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXMXD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_metadata(cls, mxd):
        """
        Create metadata for this brand new `GXMXD <geosoft.gxapi.GXMXD>` (we are the creator)
        """
        gxapi_cy.WrapMXD.create_metadata(GXContext._get_tls_geo(), mxd.encode())
        



    @classmethod
    def convert_to_map(cls, mxd, map):
        """
        Create Geosoft map from ArcGIS `GXMXD <geosoft.gxapi.GXMXD>`
        """
        gxapi_cy.WrapMXD.convert_to_map(GXContext._get_tls_geo(), mxd.encode(), map.encode())
        



    @classmethod
    def sync(cls, mxd):
        """
        Syncronize any Metadata for this `GXMXD <geosoft.gxapi.GXMXD>`
        """
        gxapi_cy.WrapMXD.sync(GXContext._get_tls_geo(), mxd.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer