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
class GXSURFACEITEM(gxapi_cy.WrapSURFACEITEM):
    """
    GXSURFACEITEM class.

    The `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>` allows you to create, read and alter Geosurface files (``*.geosoft_surface``).
    A Geosurface file can contain one or more surface items (see `GXSURFACE <geosoft.gxapi.GXSURFACE>` class). A surface item can
    contains one or more triangular polyhedral meshes.
    """

    def __init__(self, handle=0):
        super(GXSURFACEITEM, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>`
        
        :returns: A null `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>`
        :rtype:   GXSURFACEITEM
        """
        return GXSURFACEITEM()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, type, name):
        """
        Create a `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>`
        
        :param type:  Type
        :param name:  Name
        :type  type:  str
        :type  name:  str

        :returns:     `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>` Object
        :rtype:       GXSURFACEITEM

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `set_properties <geosoft.gxapi.GXSURFACEITEM.set_properties>` and `set_default_render_properties <geosoft.gxapi.GXSURFACEITEM.set_default_render_properties>`
        """
        ret_val = gxapi_cy.WrapSURFACEITEM._create(GXContext._get_tls_geo(), type.encode(), name.encode())
        return GXSURFACEITEM(ret_val)






    def get_guid(self, guid):
        """
        Gets the GUID of the surface item.
        
        :param guid:         GUID
        :type  guid:         str_ref

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The value returned by this call will not be valid for newly created items until after a call to `GXSURFACE.add_surface_item <geosoft.gxapi.GXSURFACE.add_surface_item>`.
        """
        guid.value = self._get_guid(guid.value.encode())
        




    def set_properties(self, type, name, source_guid, source_name, source_measure, secondary_source_guid, secondary_source_name, secondary_source_measure):
        """
        Sets the properties of the surface item.
        
        :param type:                      Type
        :param name:                      Name
        :param source_guid:               SourceGuid
        :param source_name:               SourceName
        :param source_measure:            SourceMeasure
        :param secondary_source_guid:     SecondarySourceGuid
        :param secondary_source_name:     SecondarySourceName
        :param secondary_source_measure:  SecondarySourceMeasure
        :type  type:                      str
        :type  name:                      str
        :type  source_guid:               str
        :type  source_name:               str
        :type  source_measure:            float
        :type  secondary_source_guid:     str
        :type  secondary_source_name:     str
        :type  secondary_source_measure:  float

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `GXSYS.generate_guid <geosoft.gxapi.GXSYS.generate_guid>`
        """
        self._set_properties(type.encode(), name.encode(), source_guid.encode(), source_name.encode(), source_measure, secondary_source_guid.encode(), secondary_source_name.encode(), secondary_source_measure)
        




    def set_properties_ex(self, type, name, source_guid, source_name, source_measure, secondary_source_guid, secondary_source_name, secondary_source_option, secondary_source_measure, secondary_source_measure2):
        """
        Sets the properties of the surface item (includes new properties introduced in 8.5).
        
        :param type:                       Type
        :param name:                       Name
        :param source_guid:                SourceGuid
        :param source_name:                SourceName
        :param source_measure:             SourceMeasure
        :param secondary_source_guid:      SecondarySourceGuid
        :param secondary_source_name:      SecondarySourceName
        :param secondary_source_option:    SecondarySourceOption
        :param secondary_source_measure:   SecondarySourceMeasure
        :param secondary_source_measure2:  SecondarySourceMeasure2
        :type  type:                       str
        :type  name:                       str
        :type  source_guid:                str
        :type  source_name:                str
        :type  source_measure:             float
        :type  secondary_source_guid:      str
        :type  secondary_source_name:      str
        :type  secondary_source_option:    int
        :type  secondary_source_measure:   float
        :type  secondary_source_measure2:  float

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `GXSYS.generate_guid <geosoft.gxapi.GXSYS.generate_guid>`
        """
        self._set_properties_ex(type.encode(), name.encode(), source_guid.encode(), source_name.encode(), source_measure, secondary_source_guid.encode(), secondary_source_name.encode(), secondary_source_option, secondary_source_measure, secondary_source_measure2)
        




    def get_properties(self, type, name, source_guid, source_name, source_measure, secondary_source_guid, secondary_source_name, secondary_source_measure):
        """
        Gets the properties of the surface item.
        
        :param type:                      Type
        :param name:                      Name
        :param source_guid:               SourceGuid
        :param source_name:               SourceName
        :param source_measure:            SourceMeasure
        :param secondary_source_guid:     SecondarySourceGuid
        :param secondary_source_name:     SecondarySourceName
        :param secondary_source_measure:  SecondarySourceMeasure
        :type  type:                      str_ref
        :type  name:                      str_ref
        :type  source_guid:               str_ref
        :type  source_name:               str_ref
        :type  source_measure:            float_ref
        :type  secondary_source_guid:     str_ref
        :type  secondary_source_name:     str_ref
        :type  secondary_source_measure:  float_ref

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        type.value, name.value, source_guid.value, source_name.value, source_measure.value, secondary_source_guid.value, secondary_source_name.value, secondary_source_measure.value = self._get_properties(type.value.encode(), name.value.encode(), source_guid.value.encode(), source_name.value.encode(), source_measure.value, secondary_source_guid.value.encode(), secondary_source_name.value.encode(), secondary_source_measure.value)
        




    def get_properties_ex(self, type, name, source_guid, source_name, source_measure, secondary_source_guid, secondary_source_name, secondary_source_option, secondary_source_measure, secondary_source_measure2):
        """
        Gets the properties of the surface item  (includes new properties introduced in 8.5).
        
        :param type:                       Type
        :param name:                       Name
        :param source_guid:                SourceGuid
        :param source_name:                SourceName
        :param source_measure:             SourceMeasure
        :param secondary_source_guid:      SecondarySourceGuid
        :param secondary_source_name:      SecondarySourceName
        :param secondary_source_option:    SecondarySourceOption
        :param secondary_source_measure:   SecondarySourceMeasure
        :param secondary_source_measure2:  SecondarySourceMeasure2
        :type  type:                       str_ref
        :type  name:                       str_ref
        :type  source_guid:                str_ref
        :type  source_name:                str_ref
        :type  source_measure:             float_ref
        :type  secondary_source_guid:      str_ref
        :type  secondary_source_name:      str_ref
        :type  secondary_source_option:    int_ref
        :type  secondary_source_measure:   float_ref
        :type  secondary_source_measure2:  float_ref

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        type.value, name.value, source_guid.value, source_name.value, source_measure.value, secondary_source_guid.value, secondary_source_name.value, secondary_source_option.value, secondary_source_measure.value, secondary_source_measure2.value = self._get_properties_ex(type.value.encode(), name.value.encode(), source_guid.value.encode(), source_name.value.encode(), source_measure.value, secondary_source_guid.value.encode(), secondary_source_name.value.encode(), secondary_source_option.value, secondary_source_measure.value, secondary_source_measure2.value)
        




    def set_default_render_properties(self, color, transparency, render_mode):
        """
        Sets default render properties of the surface item.
        
        :param color:         Color
        :param transparency:  Transparency
        :param render_mode:   :ref:`SURFACERENDER_MODE`
        :type  color:         int
        :type  transparency:  float
        :type  render_mode:   int

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `GXMVIEW.color <geosoft.gxapi.GXMVIEW.color>`
        """
        self._set_default_render_properties(color, transparency, render_mode)
        




    def get_default_render_properties(self, color, transparency, render_mode):
        """
        Gets default render properties of the surface item.
        
        :param color:         Color
        :param transparency:  Transparency
        :param render_mode:   :ref:`SURFACERENDER_MODE`
        :type  color:         int_ref
        :type  transparency:  float_ref
        :type  render_mode:   int_ref

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `GXMVIEW.color <geosoft.gxapi.GXMVIEW.color>`
        """
        color.value, transparency.value, render_mode.value = self._get_default_render_properties(color.value, transparency.value, render_mode.value)
        




    def num_components(self):
        """
        Get the number of components in the surface item.
        

        :returns:            Number of components in the surface item.
        :rtype:              int

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_components()
        return ret_val




    def add_mesh(self, vert_v_vx, vert_v_vy, vert_v_vz, tri_vv_pt1, tri_vv_pt2, tri_vv_pt3):
        """
        Adds a triangular polyhedral mesh component to the surface item.
        
        :param vert_v_vx:    Vertices X location
        :param vert_v_vy:    Vertices Y location
        :param vert_v_vz:    Vertices Z location
        :param tri_vv_pt1:   Triangles 1st Vertex
        :param tri_vv_pt2:   Triangles 2nd Vertex
        :param tri_vv_pt3:   Triangles 3rd Vertex
        :type  vert_v_vx:    GXVV
        :type  vert_v_vy:    GXVV
        :type  vert_v_vz:    GXVV
        :type  tri_vv_pt1:   GXVV
        :type  tri_vv_pt2:   GXVV
        :type  tri_vv_pt3:   GXVV

        :returns:            The index of the component added.
        :rtype:              int

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._add_mesh(vert_v_vx, vert_v_vy, vert_v_vz, tri_vv_pt1, tri_vv_pt2, tri_vv_pt3)
        return ret_val




    def get_mesh(self, index, vert_v_vx, vert_v_vy, vert_v_vz, tri_vv_pt1, tri_vv_pt2, tri_vv_pt3):
        """
        Gets a triangular polyhedral mesh of a component in the surface item.
        
        :param index:        Index of the component
        :param vert_v_vx:    Vertices X
        :param vert_v_vy:    Vertices Y
        :param vert_v_vz:    Vertices Z
        :param tri_vv_pt1:   Triangles 1st Vertex
        :param tri_vv_pt2:   Triangles 2nd Vertex
        :param tri_vv_pt3:   Triangles 3rd Vertex
        :type  index:        int
        :type  vert_v_vx:    GXVV
        :type  vert_v_vy:    GXVV
        :type  vert_v_vz:    GXVV
        :type  tri_vv_pt1:   GXVV
        :type  tri_vv_pt2:   GXVV
        :type  tri_vv_pt3:   GXVV

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_mesh(index, vert_v_vx, vert_v_vy, vert_v_vz, tri_vv_pt1, tri_vv_pt2, tri_vv_pt3)
        




    def get_extents(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the spatial range of the the surface item.
        
        :param min_x:        Minimum valid data in X.
        :param min_y:        Minimum valid data in Y.
        :param min_z:        Minimum valid data in Z.
        :param max_x:        Maximum valid data in X.
        :param max_y:        Maximum valid data in Y.
        :param max_z:        Maximum valid data in Z.
        :type  min_x:        float_ref
        :type  min_y:        float_ref
        :type  min_z:        float_ref
        :type  max_x:        float_ref
        :type  max_y:        float_ref
        :type  max_z:        float_ref

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._get_extents(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_mesh_info(self, index, closed, n_inner_comps, area, volume, volume_confidence_interval):
        """
        Gets information about a triangular polyhedral mesh component in the surface item.
        
        :param index:                       Index of the component
        :param closed:                      indicating if mesh is closed
        :param n_inner_comps:               Number of inner components
        :param area:                        Area
        :param volume:                      Volume
        :param volume_confidence_interval:  Volume confidence interval
        :type  index:                       int
        :type  closed:                      bool_ref
        :type  n_inner_comps:               int_ref
        :type  area:                        float_ref
        :type  volume:                      float_ref
        :type  volume_confidence_interval:  float_ref

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        closed.value, n_inner_comps.value, area.value, volume.value, volume_confidence_interval.value = self._get_mesh_info(index, closed.value, n_inner_comps.value, area.value, volume.value, volume_confidence_interval.value)
        




    def get_info(self, closed, area, volume, volume_confidence_interval):
        """
        Gets information about the surface item.
        
        :param closed:                      indicating if all meshes in item is closed
        :param area:                        Area
        :param volume:                      Volume
        :param volume_confidence_interval:  Volume confidence interval
        :type  closed:                      bool_ref
        :type  area:                        float_ref
        :type  volume:                      float_ref
        :type  volume_confidence_interval:  float_ref

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        closed.value, area.value, volume.value, volume_confidence_interval.value = self._get_info(closed.value, area.value, volume.value, volume_confidence_interval.value)
        




    def get_geometry_info(self, vertices, triangles):
        """
        Get the total number of vertices and triangles of all mesh components in item.
        
        :param vertices:     Total number of vertices
        :param triangles:    Total number of triangles
        :type  vertices:     int_ref
        :type  triangles:    int_ref

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        vertices.value, triangles.value = self._get_geometry_info(vertices.value, triangles.value)
        




    def compute_extended_info(self, components, vertices, edges, triangles, inconsistent, invalid, intersectiona):
        """
        Compute more information (including validation) about of all mesh components in the surface item.
        
        :param components:     Number of inner components (recomputed)
        :param vertices:       Total number of valid vertices
        :param edges:          Total number of valid edges
        :param triangles:      Total number of valid triangles
        :param inconsistent:   Number of inconsistent triangles
        :param invalid:        Number of invalid triangles
        :param intersectiona:  Number of self intersections
        :type  components:     int_ref
        :type  vertices:       int_ref
        :type  edges:          int_ref
        :type  triangles:      int_ref
        :type  inconsistent:   int_ref
        :type  invalid:        int_ref
        :type  intersectiona:  int_ref

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        components.value, vertices.value, edges.value, triangles.value, inconsistent.value, invalid.value, intersectiona.value = self._compute_extended_info(components.value, vertices.value, edges.value, triangles.value, inconsistent.value, invalid.value, intersectiona.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer