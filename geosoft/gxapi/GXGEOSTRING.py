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
class GXGEOSTRING:
    """
    GXGEOSTRING class.

    The `GXGEOSTRING` class is used to read information stored in Geostring files 
    (``*.geosoft_string``). Geosoft geostrings are 3D vector files that store digitized 
    interpretations drawn on section maps. Both polygon and polyline features can be 
    stored in the same file. This API currently only provides read access, 
    but read/write support could be added in the future.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGEOSTRING(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGEOSTRING`
        
        :returns: A null `GXGEOSTRING`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXGEOSTRING` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXGEOSTRING`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def open(cls, p1, p2):
        """
        Open a Geostring file
        """
        ret_val = gxapi_cy.WrapGEOSTRING.open(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXGEOSTRING(ret_val)






    def get_ipj(self, p2):
        """
        Get the coordinate system of the Geostring.
        """
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_features(self, p2):
        """
        Get the features

        **Note:**

        List items are returned with feature GUID in name and feature name in value.
        """
        self._wrapper.get_features(p2._wrapper)
        




    def get_sections(self, p2):
        """
        Get the sections

        **Note:**

        List items are returned with section GUID in name and section name in value.
        """
        self._wrapper.get_sections(p2._wrapper)
        




    def get_all_shapes(self, p2):
        """
        Get the all shapes
        """
        self._wrapper.get_all_shapes(p2._wrapper)
        




    def get_shapes_for_feature(self, p2, p3):
        """
        Get all shapes linked to a specific feature
        """
        self._wrapper.get_shapes_for_feature(p2.encode(), p3._wrapper)
        




    def get_shapes_for_section(self, p2, p3):
        """
        Get all shapes linked to a specific section
        """
        self._wrapper.get_shapes_for_section(p2.encode(), p3._wrapper)
        




    def get_shapes_for_feature_and_section(self, p2, p3, p4):
        """
        Get all shapes linked to a specific feature and section
        """
        self._wrapper.get_shapes_for_feature_and_section(p2.encode(), p3.encode(), p4._wrapper)
        




    def get_feature_properties(self, p2, p3, p5, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17):
        """
        Get a feature's properties
        """
        p3.value, p5.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value, p17.value = self._wrapper.get_feature_properties(p2.encode(), p3.value.encode(), p5.value.encode(), p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value, p17.value)
        




    def get_section_properties(self, p2, p3, p5, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16):
        """
        Get a section's properties
        """
        p3.value, p5.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value = self._wrapper.get_section_properties(p2.encode(), p3.value.encode(), p5.value.encode(), p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value)
        




    def get_shape_properties(self, p2, p3, p5, p7, p8, p9):
        """
        Get a shape's properties
        """
        p3.value, p5.value = self._wrapper.get_shape_properties(p2.encode(), p3.value.encode(), p5.value.encode(), p7._wrapper, p8._wrapper, p9._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer