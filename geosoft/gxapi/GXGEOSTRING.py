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

    The `GXGEOSTRING <geosoft.gxapi.GXGEOSTRING>` class is used to read information stored in Geostring files 
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
    def open(cls, geostring_file, mode):
        """
        Open a Geostring file
        """
        ret_val = gxapi_cy.WrapGEOSTRING.open(GXContext._get_tls_geo(), geostring_file.encode(), mode)
        return GXGEOSTRING(ret_val)






    def get_ipj(self, ipj):
        """
        Get the coordinate system of the Geostring.
        """
        self._wrapper.get_ipj(ipj._wrapper)
        




    def get_features(self, lst):
        """
        Get the features

        **Note:**

        List items are returned with feature GUID in name and feature name in value.
        """
        self._wrapper.get_features(lst._wrapper)
        




    def get_sections(self, lst):
        """
        Get the sections

        **Note:**

        List items are returned with section GUID in name and section name in value.
        """
        self._wrapper.get_sections(lst._wrapper)
        




    def get_all_shapes(self, lst):
        """
        Get the all shapes
        """
        self._wrapper.get_all_shapes(lst._wrapper)
        




    def get_shapes_for_feature(self, guid, lst):
        """
        Get all shapes linked to a specific feature
        """
        self._wrapper.get_shapes_for_feature(guid.encode(), lst._wrapper)
        




    def get_shapes_for_section(self, guid, lst):
        """
        Get all shapes linked to a specific section
        """
        self._wrapper.get_shapes_for_section(guid.encode(), lst._wrapper)
        




    def get_shapes_for_feature_and_section(self, feature_guid, section_guid, lst):
        """
        Get all shapes linked to a specific feature and section
        """
        self._wrapper.get_shapes_for_feature_and_section(feature_guid.encode(), section_guid.encode(), lst._wrapper)
        




    def get_feature_properties(self, guid, name, description, polygon, pat_number, pat_size, pat_thick, pat_density, pat_color, pat_bg_color, line_style, line_thickness, line_pitch, line_color):
        """
        Get a feature's properties
        """
        name.value, description.value, polygon.value, pat_number.value, pat_size.value, pat_thick.value, pat_density.value, pat_color.value, pat_bg_color.value, line_style.value, line_thickness.value, line_pitch.value, line_color.value = self._wrapper.get_feature_properties(guid.encode(), name.value.encode(), description.value.encode(), polygon.value, pat_number.value, pat_size.value, pat_thick.value, pat_density.value, pat_color.value, pat_bg_color.value, line_style.value, line_thickness.value, line_pitch.value, line_color.value)
        




    def get_section_properties(self, guid, name, container_name, orientation, easting, northing, elevation, azimuth, swing, a, b, c, d):
        """
        Get a section's properties
        """
        name.value, container_name.value, orientation.value, easting.value, northing.value, elevation.value, azimuth.value, swing.value, a.value, b.value, c.value, d.value = self._wrapper.get_section_properties(guid.encode(), name.value.encode(), container_name.value.encode(), orientation.value, easting.value, northing.value, elevation.value, azimuth.value, swing.value, a.value, b.value, c.value, d.value)
        




    def get_shape_properties(self, guid, feature_guid, section_guid, vert_v_vx, vert_v_vy, vert_v_vz):
        """
        Get a shape's properties
        """
        feature_guid.value, section_guid.value = self._wrapper.get_shape_properties(guid.encode(), feature_guid.value.encode(), section_guid.value.encode(), vert_v_vx._wrapper, vert_v_vy._wrapper, vert_v_vz._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer