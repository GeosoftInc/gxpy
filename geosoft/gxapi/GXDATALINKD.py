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
    def create_arc_lyr(cls, p1):
        """
        Create an `GXDATALINKD` object from a ArcGIS LYR file

        **Note:**

        Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr(GXContext._get_tls_geo(), p1.encode())
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_ex(cls, p1, p2):
        """
        Create an `GXDATALINKD` object from a ArcGIS LYR file

        **Note:**

        Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr_ex(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_from_tmp(cls, p1):
        """
        Create an `GXDATALINKD` object from a temporary ArcGIS LYR file

        **Note:**

        Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr_from_tmp(GXContext._get_tls_geo(), p1.encode())
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_from_tmp_ex(cls, p1, p2):
        """
        Create an `GXDATALINKD` object from a temporary ArcGIS LYR file

        **Note:**

        Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr_from_tmp_ex(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXDATALINKD(ret_val)



    @classmethod
    def create_bing(cls, p1):
        """
        Create an `GXDATALINKD` object for a BING dataset
        """
        ret_val = gxapi_cy.WrapDATALINKD.create_bing(GXContext._get_tls_geo(), p1)
        return GXDATALINKD(ret_val)






    def get_extents(self, p2, p3, p4, p5):
        """
        Get the data extents of the DATALINK Display object.
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_extents(p2.value, p3.value, p4.value, p5.value)
        




    def get_ipj(self, p2):
        """
        Get the projection of the DATALINK Display object.
        """
        self._wrapper.get_ipj(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer