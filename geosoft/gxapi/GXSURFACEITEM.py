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
class GXSURFACEITEM:
    """
    GXSURFACEITEM class.

    The `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>` allows you to create, read and alter Geosurface files (``*.geosoft_surface``).
    A Geosurface file can contain one or more surface items (see `GXSURFACE <geosoft.gxapi.GXSURFACE>` class). A surface item can
    contains one or more triangular polyhedral meshes.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSURFACEITEM(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSURFACEITEM`
        
        :returns: A null `GXSURFACEITEM`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXSURFACEITEM` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXSURFACEITEM`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, type, name):
        """
        Create a `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>`

        .. seealso::

            `set_properties <geosoft.gxapi.GXSURFACEITEM.set_properties>` and `set_default_render_properties <geosoft.gxapi.GXSURFACEITEM.set_default_render_properties>`
        """
        ret_val = gxapi_cy.WrapSURFACEITEM.create(GXContext._get_tls_geo(), type.encode(), name.encode())
        return GXSURFACEITEM(ret_val)






    def get_guid(self, guid):
        """
        Gets the GUID of the surface item.

        **Note:**

        The value returned by this call will not be valid for newly created items until after a call to `GXSURFACE.add_surface_item <geosoft.gxapi.GXSURFACE.add_surface_item>`.
        """
        guid.value = self._wrapper.get_guid(guid.value.encode())
        




    def set_properties(self, type, name, source_guid, source_name, source_measure, secondary_source_guid, secondary_source_name, secondary_source_measure):
        """
        Sets the properties of the surface item.

        .. seealso::

            `GXSYS.generate_guid <geosoft.gxapi.GXSYS.generate_guid>`
        """
        self._wrapper.set_properties(type.encode(), name.encode(), source_guid.encode(), source_name.encode(), source_measure, secondary_source_guid.encode(), secondary_source_name.encode(), secondary_source_measure)
        




    def set_properties_ex(self, type, name, source_guid, source_name, source_measure, secondary_source_guid, secondary_source_name, secondary_source_option, secondary_source_measure, secondary_source_measure2):
        """
        Sets the properties of the surface item (includes new properties introduced in 8.5).

        .. seealso::

            `GXSYS.generate_guid <geosoft.gxapi.GXSYS.generate_guid>`
        """
        self._wrapper.set_properties_ex(type.encode(), name.encode(), source_guid.encode(), source_name.encode(), source_measure, secondary_source_guid.encode(), secondary_source_name.encode(), secondary_source_option, secondary_source_measure, secondary_source_measure2)
        




    def get_properties(self, type, name, source_guid, source_name, source_measure, secondary_source_guid, secondary_source_name, secondary_source_measure):
        """
        Gets the properties of the surface item.
        """
        type.value, name.value, source_guid.value, source_name.value, source_measure.value, secondary_source_guid.value, secondary_source_name.value, secondary_source_measure.value = self._wrapper.get_properties(type.value.encode(), name.value.encode(), source_guid.value.encode(), source_name.value.encode(), source_measure.value, secondary_source_guid.value.encode(), secondary_source_name.value.encode(), secondary_source_measure.value)
        




    def get_properties_ex(self, type, name, source_guid, source_name, source_measure, secondary_source_guid, secondary_source_name, secondary_source_option, secondary_source_measure, secondary_source_measure2):
        """
        Gets the properties of the surface item  (includes new properties introduced in 8.5).
        """
        type.value, name.value, source_guid.value, source_name.value, source_measure.value, secondary_source_guid.value, secondary_source_name.value, secondary_source_option.value, secondary_source_measure.value, secondary_source_measure2.value = self._wrapper.get_properties_ex(type.value.encode(), name.value.encode(), source_guid.value.encode(), source_name.value.encode(), source_measure.value, secondary_source_guid.value.encode(), secondary_source_name.value.encode(), secondary_source_option.value, secondary_source_measure.value, secondary_source_measure2.value)
        




    def set_default_render_properties(self, color, transparency, render_mode):
        """
        Sets default render properties of the surface item.

        .. seealso::

            `GXMVIEW.color <geosoft.gxapi.GXMVIEW.color>`
        """
        self._wrapper.set_default_render_properties(color, transparency, render_mode)
        




    def get_default_render_properties(self, color, transparency, render_mode):
        """
        Gets default render properties of the surface item.

        .. seealso::

            `GXMVIEW.color <geosoft.gxapi.GXMVIEW.color>`
        """
        color.value, transparency.value, render_mode.value = self._wrapper.get_default_render_properties(color.value, transparency.value, render_mode.value)
        




    def num_components(self):
        """
        Get the number of components in the surface item.
        """
        ret_val = self._wrapper.num_components()
        return ret_val




    def add_mesh(self, vert_v_vx, vert_v_vy, vert_v_vz, tri_vv_pt1, tri_vv_pt2, tri_vv_pt3):
        """
        Adds a triangular polyhedral mesh component to the surface item.
        """
        ret_val = self._wrapper.add_mesh(vert_v_vx._wrapper, vert_v_vy._wrapper, vert_v_vz._wrapper, tri_vv_pt1._wrapper, tri_vv_pt2._wrapper, tri_vv_pt3._wrapper)
        return ret_val




    def get_mesh(self, index, vert_v_vx, vert_v_vy, vert_v_vz, tri_vv_pt1, tri_vv_pt2, tri_vv_pt3):
        """
        Gets a triangular polyhedral mesh of a component in the surface item.
        """
        self._wrapper.get_mesh(index, vert_v_vx._wrapper, vert_v_vy._wrapper, vert_v_vz._wrapper, tri_vv_pt1._wrapper, tri_vv_pt2._wrapper, tri_vv_pt3._wrapper)
        




    def get_extents(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the spatial range of the the surface item.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._wrapper.get_extents(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_mesh_info(self, index, closed, n_inner_comps, area, volume, volume_confidence_interval):
        """
        Gets information about a triangular polyhedral mesh component in the surface item.
        """
        closed.value, n_inner_comps.value, area.value, volume.value, volume_confidence_interval.value = self._wrapper.get_mesh_info(index, closed.value, n_inner_comps.value, area.value, volume.value, volume_confidence_interval.value)
        




    def get_info(self, closed, area, volume, volume_confidence_interval):
        """
        Gets information about the surface item.
        """
        closed.value, area.value, volume.value, volume_confidence_interval.value = self._wrapper.get_info(closed.value, area.value, volume.value, volume_confidence_interval.value)
        




    def get_geometry_info(self, vertices, triangles):
        """
        Get the total number of vertices and triangles of all mesh components in item.
        """
        vertices.value, triangles.value = self._wrapper.get_geometry_info(vertices.value, triangles.value)
        




    def compute_extended_info(self, components, vertices, edges, triangles, inconsistent, invalid, intersectiona):
        """
        Compute more information (including validation) about of all mesh components in the surface item.
        """
        components.value, vertices.value, edges.value, triangles.value, inconsistent.value, invalid.value, intersectiona.value = self._wrapper.compute_extended_info(components.value, vertices.value, edges.value, triangles.value, inconsistent.value, invalid.value, intersectiona.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer