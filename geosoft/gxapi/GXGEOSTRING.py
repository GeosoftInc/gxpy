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
class GXGEOSTRING(gxapi_cy.WrapGEOSTRING):
    """
    GXGEOSTRING class.

    The `GXGEOSTRING <geosoft.gxapi.GXGEOSTRING>` class is used to read information stored in Geostring files 
    (``*.geosoft_string``). Geosoft geostrings are 3D vector files that store digitized 
    interpretations drawn on section maps. Both polygon and polyline features can be 
    stored in the same file. This API currently only provides read access, 
    but read/write support could be added in the future.
    """

    def __init__(self, handle=0):
        super(GXGEOSTRING, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGEOSTRING <geosoft.gxapi.GXGEOSTRING>`
        
        :returns: A null `GXGEOSTRING <geosoft.gxapi.GXGEOSTRING>`
        :rtype:   GXGEOSTRING
        """
        return GXGEOSTRING()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def open(cls, geostring_file, mode):
        """
        Open a Geostring file
        
        :param geostring_file:  Geostring file name
        :param mode:            :ref:`GEOSTRING_OPEN`
        :type  geostring_file:  str
        :type  mode:            int

        :returns:               `GXGEOSTRING <geosoft.gxapi.GXGEOSTRING>` Object
        :rtype:                 GXGEOSTRING

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapGEOSTRING._open(GXContext._get_tls_geo(), geostring_file.encode(), mode)
        return GXGEOSTRING(ret_val)






    def get_ipj(self, ipj):
        """
        Get the coordinate system of the Geostring.
        
        :param ipj:        `GXIPJ <geosoft.gxapi.GXIPJ>` in which to place the Geostring coordinate system
        :type  ipj:        GXIPJ

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_ipj(ipj)
        




    def get_features(self, lst):
        """
        Get the features
        
        :param lst:        `GXLST <geosoft.gxapi.GXLST>` to fill
        :type  lst:        GXLST

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** List items are returned with feature GUID in name and feature name in value.
        """
        self._get_features(lst)
        




    def get_sections(self, lst):
        """
        Get the sections
        
        :param lst:        `GXLST <geosoft.gxapi.GXLST>` to fill
        :type  lst:        GXLST

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** List items are returned with section GUID in name and section name in value.
        """
        self._get_sections(lst)
        




    def get_all_shapes(self, lst):
        """
        Get the all shapes
        
        :param lst:        `GXLST <geosoft.gxapi.GXLST>` to fill
        :type  lst:        GXLST

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_all_shapes(lst)
        




    def get_shapes_for_feature(self, guid, lst):
        """
        Get all shapes linked to a specific feature
        
        :param guid:       Feature GUID
        :param lst:        `GXLST <geosoft.gxapi.GXLST>` to fill
        :type  guid:       str
        :type  lst:        GXLST

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_shapes_for_feature(guid.encode(), lst)
        




    def get_shapes_for_section(self, guid, lst):
        """
        Get all shapes linked to a specific section
        
        :param guid:       Section GUID
        :param lst:        `GXLST <geosoft.gxapi.GXLST>` to fill
        :type  guid:       str
        :type  lst:        GXLST

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_shapes_for_section(guid.encode(), lst)
        




    def get_shapes_for_feature_and_section(self, feature_guid, section_guid, lst):
        """
        Get all shapes linked to a specific feature and section
        
        :param feature_guid:  Feature GUID
        :param section_guid:  Section GUID
        :param lst:           `GXLST <geosoft.gxapi.GXLST>` to fill
        :type  feature_guid:  str
        :type  section_guid:  str
        :type  lst:           GXLST

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_shapes_for_feature_and_section(feature_guid.encode(), section_guid.encode(), lst)
        




    def get_feature_properties(self, guid, name, description, polygon, pat_number, pat_size, pat_thick, pat_density, pat_color, pat_bg_color, line_style, line_thickness, line_pitch, line_color):
        """
        Get a feature's properties
        
        :param guid:            Feature GUID
        :param name:            Name
        :param description:     Description
        :param polygon:         Indicates if feature is described by polygons (shapes are polylines if not set)
        :param pat_number:      The fill pattern number (see `GXMVIEW.pat_number <geosoft.gxapi.GXMVIEW.pat_number>`)
        :param pat_size:        The fill pattern size (see `GXMVIEW.pat_size <geosoft.gxapi.GXMVIEW.pat_size>`)
        :param pat_thick:       The fill pattern thickness (see `GXMVIEW.pat_thick <geosoft.gxapi.GXMVIEW.pat_thick>`)
        :param pat_density:     The fill pattern density (see `GXMVIEW.pat_density <geosoft.gxapi.GXMVIEW.pat_density>`)
        :param pat_color:       The fill color (an `GXMVIEW <geosoft.gxapi.GXMVIEW>` color)
        :param pat_bg_color:    The fill background color (an `GXMVIEW <geosoft.gxapi.GXMVIEW>` color)
        :param line_style:      The line style (see `GXMVIEW.line_style <geosoft.gxapi.GXMVIEW.line_style>`)
        :param line_thickness:  The line thickness (see `GXMVIEW.line_thick <geosoft.gxapi.GXMVIEW.line_thick>`)
        :param line_pitch:      The dash pattern pitch (see `GXMVIEW.line_style <geosoft.gxapi.GXMVIEW.line_style>`)
        :param line_color:      The line color (an `GXMVIEW <geosoft.gxapi.GXMVIEW>` color)
        :type  guid:            str
        :type  name:            str_ref
        :type  description:     str_ref
        :type  polygon:         bool_ref
        :type  pat_number:      int_ref
        :type  pat_size:        float_ref
        :type  pat_thick:       float_ref
        :type  pat_density:     float_ref
        :type  pat_color:       int_ref
        :type  pat_bg_color:    int_ref
        :type  line_style:      int_ref
        :type  line_thickness:  float_ref
        :type  line_pitch:      float_ref
        :type  line_color:      int_ref

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value, description.value, polygon.value, pat_number.value, pat_size.value, pat_thick.value, pat_density.value, pat_color.value, pat_bg_color.value, line_style.value, line_thickness.value, line_pitch.value, line_color.value = self._get_feature_properties(guid.encode(), name.value.encode(), description.value.encode(), polygon.value, pat_number.value, pat_size.value, pat_thick.value, pat_density.value, pat_color.value, pat_bg_color.value, line_style.value, line_thickness.value, line_pitch.value, line_color.value)
        




    def get_section_properties(self, guid, name, container_name, orientation, easting, northing, elevation, azimuth, swing, a, b, c, d):
        """
        Get a section's properties
        
        :param guid:            Section GUID
        :param name:            Name
        :param container_name:  ContainerName
        :param orientation:     :ref:`SECTION_ORIENTATION`
        :param easting:         Easting
        :param northing:        Northing
        :param elevation:       Elevation
        :param azimuth:         Azimuth
        :param swing:           Swing
        :param a:               A in the scalar equation of best-fit plane describing the section
        :param b:               B in the scalar equation of best-fit plane describing the section
        :param c:               C in the scalar equation of best-fit plane describing the section
        :param d:               D in the scalar equation of best-fit plane describing the section
        :type  guid:            str
        :type  name:            str_ref
        :type  container_name:  str_ref
        :type  orientation:     int_ref
        :type  easting:         float_ref
        :type  northing:        float_ref
        :type  elevation:       float_ref
        :type  azimuth:         float_ref
        :type  swing:           float_ref
        :type  a:               float_ref
        :type  b:               float_ref
        :type  c:               float_ref
        :type  d:               float_ref

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value, container_name.value, orientation.value, easting.value, northing.value, elevation.value, azimuth.value, swing.value, a.value, b.value, c.value, d.value = self._get_section_properties(guid.encode(), name.value.encode(), container_name.value.encode(), orientation.value, easting.value, northing.value, elevation.value, azimuth.value, swing.value, a.value, b.value, c.value, d.value)
        




    def get_shape_properties(self, guid, feature_guid, section_guid, vert_v_vx, vert_v_vy, vert_v_vz):
        """
        Get a shape's properties
        
        :param guid:          Shape GUID
        :param feature_guid:  Feature GUID
        :param section_guid:  Section GUID
        :param vert_v_vx:     Vertices X location
        :param vert_v_vy:     Vertices Y location
        :param vert_v_vz:     Vertices Z location
        :type  guid:          str
        :type  feature_guid:  str_ref
        :type  section_guid:  str_ref
        :type  vert_v_vx:     GXVV
        :type  vert_v_vy:     GXVV
        :type  vert_v_vz:     GXVV

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        feature_guid.value, section_guid.value = self._get_shape_properties(guid.encode(), feature_guid.value.encode(), section_guid.value.encode(), vert_v_vx, vert_v_vy, vert_v_vz)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer