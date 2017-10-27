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
class GXDATALINKD:
    """
    GXDATALINKD class.

    DATALINK Display object.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDATALINKD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDATALINKD`
        
        :returns: A null `GXDATALINKD`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDATALINKD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDATALINKD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_arc_lyr(cls, arc_lyr_file):
        """
        Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object from a ArcGIS LYR file

        **Note:**

        Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr(GXContext._get_tls_geo(), arc_lyr_file.encode())
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_ex(cls, arc_lyr_file, o3d_group):
        """
        Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object from a ArcGIS LYR file

        **Note:**

        Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr_ex(GXContext._get_tls_geo(), arc_lyr_file.encode(), o3d_group)
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_from_tmp(cls, arc_lyr_file):
        """
        Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object from a temporary ArcGIS LYR file

        **Note:**

        Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr_from_tmp(GXContext._get_tls_geo(), arc_lyr_file.encode())
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_from_tmp_ex(cls, arc_lyr_file, o3d_group):
        """
        Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object from a temporary ArcGIS LYR file

        **Note:**

        Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr_from_tmp_ex(GXContext._get_tls_geo(), arc_lyr_file.encode(), o3d_group)
        return GXDATALINKD(ret_val)



    @classmethod
    def create_bing(cls, layer):
        """
        Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object for a BING dataset
        """
        ret_val = gxapi_cy.WrapDATALINKD.create_bing(GXContext._get_tls_geo(), layer)
        return GXDATALINKD(ret_val)






    def get_extents(self, min_x, max_x, min_y, max_y):
        """
        Get the data extents of the DATALINK Display object.
        """
        min_x.value, max_x.value, min_y.value, max_y.value = self._wrapper.get_extents(min_x.value, max_x.value, min_y.value, max_y.value)
        




    def get_ipj(self, ipj):
        """
        Get the projection of the DATALINK Display object.
        """
        self._wrapper.get_ipj(ipj._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer