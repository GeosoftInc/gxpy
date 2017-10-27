### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXAGG import GXAGG
from .GXBF import GXBF
from .GXCSYMB import GXCSYMB
from .GXDATALINKD import GXDATALINKD
from .GXITR import GXITR
from .GXMAP import GXMAP
from .GXMETA import GXMETA
from .GXREG import GXREG
from .GXTPAT import GXTPAT
from .GXVECTOR3D import GXVECTOR3D
from .GXVOXD import GXVOXD


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMVIEW:
    """
    GXMVIEW class.

    A view (`GXMVIEW <geosoft.gxapi.GXMVIEW>` class) has a 2-D/3-D translation matrix, a map
    projection and a clip region.  A view contains any number of
    "groups", and each "group" contains one or more graphics
    elements (entities).  Different types of groups will contain
    different types of entities:

    **Note:**

    `GXCSYMB <geosoft.gxapi.GXCSYMB>` groups (color symbols) contain data and rules for
    presenting the data as color symbols.  See `col_symbol <geosoft.gxapi.GXMVIEW.col_symbol>`
    and the `GXCSYMB <geosoft.gxapi.GXCSYMB>` class.
    
    `GXAGG <geosoft.gxapi.GXAGG>` groups (aggregates) contain images.  See `aggregate <geosoft.gxapi.GXMVIEW.aggregate>`
    and the `GXAGG <geosoft.gxapi.GXAGG>` class.
    
    Standard groups contain symbols, lines, polylines, and polygons.
    See `start_group <geosoft.gxapi.GXMVIEW.start_group>`.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMVIEW(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMVIEW`
        
        :returns: A null `GXMVIEW`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXMVIEW` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXMVIEW`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# 3D Entity



    def box_3d(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Draw a 3D box

        **Note:**

        The Fill color is used to color the box.
        """
        self._wrapper.box_3d(min_x, min_y, min_z, max_x, max_y, max_z)
        




    def crc_view(self, crc, file):
        """
        Generate an XML CRC of a View
        """
        crc.value = self._wrapper.crc_view(crc.value, file.encode())
        




    def crc_view_group(self, group, crc, file):
        """
        Generate an XML CRC of a Group
        """
        crc.value = self._wrapper.crc_view_group(group.encode(), crc.value, file.encode())
        




    def cylinder_3d(self, start_x, start_y, start_z, end_x, end_y, end_z, start_radius, end_radius, flags):
        """
        Draw a 3D cylinder

        **Note:**

        The Fill color is used to color the cylinder.
        The flags determine if the cylinder is open and what
        end are closed. Note that you can create cones by
        specifying a 0 radius for one of the ends.
        """
        self._wrapper.cylinder_3d(start_x, start_y, start_z, end_x, end_y, end_z, start_radius, end_radius, flags)
        




    def draw_object_3d(self, type, mode, objects, default_count, vert_v_vx, vert_v_vy, vert_v_vz, norm_v_vx, norm_v_vy, norm_v_vz, color_vv, index_vv, count_vv):
        """
        Draw a 3D object optimized for rendering
        """
        self._wrapper.draw_object_3d(type, mode, objects, default_count, vert_v_vx._wrapper, vert_v_vy._wrapper, vert_v_vz._wrapper, norm_v_vx._wrapper, norm_v_vy._wrapper, norm_v_vz._wrapper, color_vv._wrapper, index_vv._wrapper, count_vv._wrapper)
        




    def draw_surface_3d_ex(self, group_name, vert_v_vx, vert_v_vy, vert_v_vz, norm_v_vx, norm_v_vy, norm_v_vz, color_vv, color, tri_vv_pt1, tri_vv_pt2, tri_vv_pt3, ipj):
        """
        Draw a 3D object built from triangles

        **Note:**

        Provide one normal per vertex.
        Triangles are defined by indices into the set of vertices.
        """
        self._wrapper.draw_surface_3d_ex(group_name.encode(), vert_v_vx._wrapper, vert_v_vy._wrapper, vert_v_vz._wrapper, norm_v_vx._wrapper, norm_v_vy._wrapper, norm_v_vz._wrapper, color_vv._wrapper, color, tri_vv_pt1._wrapper, tri_vv_pt2._wrapper, tri_vv_pt3._wrapper, ipj._wrapper)
        




    def draw_surface_3d_from_file(self, group_name, surface_file):
        """
        Draw a 3D object from a surface file
        """
        self._wrapper.draw_surface_3d_from_file(group_name.encode(), surface_file.encode())
        



    @classmethod
    def font_weight_lst(cls, lst):
        """
        Fill a `GXLST <geosoft.gxapi.GXLST>` with the different font weights.
        """
        gxapi_cy.WrapMVIEW.font_weight_lst(GXContext._get_tls_geo(), lst._wrapper)
        




    def get_agg_file_names(self, group, vv):
        """
        Get the names of grid files stored in an `GXAGG <geosoft.gxapi.GXAGG>`.

        **Note:**

        The group must be an `GXAGG <geosoft.gxapi.GXAGG>` group. Check this using
        `is_group <geosoft.gxapi.GXMVIEW.is_group>` and `MVIEW_IS_AGG <geosoft.gxapi.MVIEW_IS_AGG>`.
        """
        self._wrapper.get_agg_file_names(group.encode(), vv._wrapper)
        




    def get_meta(self, group, meta):
        """
        Retrieves Metadata from a group
        """
        ret_val, meta.value = self._wrapper.get_meta(group.encode(), meta.value.encode())
        return GXMETA(ret_val)




    def measure_text(self, text, x_min, y_min, x_max, y_max):
        """
        Compute the bounding rectangle in view units of the text using the current attributes.

        **Note:**

        Area will be 0 if error occurred (does not fail).
        This will return the bounding rectangle as if the text was placed at 0,0 and adjusted according to
        the current text alignment and angle set for the view. Also see notes for `text_size <geosoft.gxapi.GXMVIEW.text_size>`.
        """
        x_min.value, y_min.value, x_max.value, y_max.value = self._wrapper.measure_text(text.encode(), x_min.value, y_min.value, x_max.value, y_max.value)
        




    def point_3d(self, x, y, z):
        """
        Draw a 3D point.

        **Note:**

        The Line color and line thickness will affect rendering.
        """
        self._wrapper.point_3d(x, y, z)
        




    def poly_line_3d(self, vv_x, vv_y, vv_z):
        """
        Draw a 3D polyline.

        **Note:**

        Dummies are not allowed in the line.
        Line Color, Thickness is supported on rendering
        """
        self._wrapper.poly_line_3d(vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        




    def relocate_group(self, group, min_x, min_y, max_x, max_y, asp):
        """
        Re-locate a group in a view.
        """
        self._wrapper.relocate_group(group.encode(), min_x, min_y, max_x, max_y, asp)
        




    def set_meta(self, group, meta, name):
        """
        Update the `GXMETA <geosoft.gxapi.GXMETA>` in this group with the new meta object.
        """
        self._wrapper.set_meta(group.encode(), meta._wrapper, name.encode())
        




    def sphere_3d(self, x, y, z, radius):
        """
        Draw a 3D sphere

        **Note:**

        The Fill color is used to color the sphere.
        """
        self._wrapper.sphere_3d(x, y, z, radius)
        




    def update_met_afrom_group(self, group, meta):
        """
        Fill the `GXMETA <geosoft.gxapi.GXMETA>` with group dataset information
        """
        self._wrapper.update_met_afrom_group(group.encode(), meta._wrapper)
        




# 3D Plane



    def delete_plane(self, plane, del_grp):
        """
        Delete a plane in a view

        **Note:**

        If the groups on the plane are not deleted, they will remain in the
        3D view as "New" groups but will be unassigned to a plane.  The
        SetAllNewGroupsToPlane  function can be used to assign these groups
        to a different plane.
        """
        self._wrapper.delete_plane(plane, del_grp)
        




    def get_plane_clip_ply(self, plane, pply):
        """
        Get the Plane Clip Region

        **Note:**

        By default it is the View's Clip Region
        """
        self._wrapper.get_plane_clip_ply(plane, pply._wrapper)
        




    def get_plane_equation(self, plane, pitch, yaw, roll, x, y, z, sx, sy, str_val):
        """
        Get the equation of a plane
        """
        pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value = self._wrapper.get_plane_equation(plane, pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value)
        




    def get_view_plane_equation(self, pitch, yaw, roll, x, y, z, sx, sy, str_val):
        """
        Get the View's Plane Equation
        """
        pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value = self._wrapper.get_view_plane_equation(pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value)
        




    def create_plane(self, plane):
        """
        Create a 3D Plane for 2D Groups
        """
        ret_val = self._wrapper.create_plane(plane.encode())
        return ret_val




    def find_plane(self, plane):
        """
        Find a plane in a view
        """
        ret_val = self._wrapper.find_plane(plane.encode())
        return ret_val




    def get_def_plane(self, name):
        """
        Get the default drawing plane.

        **Note:**

        2D drawing to a 3D View will always be placed on the
        default drawing plane.  If no default drawing plane
        has been set, the first valid plane in the view is
        used as the default drawing plane.
        """
        name.value = self._wrapper.get_def_plane(name.value.encode())
        




    def is_view_3d(self):
        """
        Is the view 3D?
        """
        ret_val = self._wrapper.is_view_3d()
        return ret_val




    def is_section(self):
        """
        Is the view a section view?

        **Note:**

        Section views are recognized because their projection contains one of the following orientations:
        
        `IPJ_ORIENT_SECTION <geosoft.gxapi.IPJ_ORIENT_SECTION>` - Target-type sections with Z projection horizontally
        `IPJ_ORIENT_SECTION_NORMAL <geosoft.gxapi.IPJ_ORIENT_SECTION_NORMAL>` - Like `IPJ_ORIENT_SECTION <geosoft.gxapi.IPJ_ORIENT_SECTION>`, but Z projects
        perpendicular to the secton plane.
        `IPJ_ORIENT_SECTION_CROOKED <geosoft.gxapi.IPJ_ORIENT_SECTION_CROOKED>` - Crooked sections
        `IPJ_ORIENT_3D <geosoft.gxapi.IPJ_ORIENT_3D>` - Some Sections extracted from a voxel - e.g. VoxelToGrids,
        as the voxel can have any orientation in 3D.
        """
        ret_val = self._wrapper.is_section()
        return ret_val




    def list_plane_groups(self, plane, lst):
        """
        List all groups in a specific plane of a 3D view

        **Note:**

        The group names are placed in the list names, group
        numbers are placed in the list values.
        
        Groups are added to the end of the `GXLST <geosoft.gxapi.GXLST>`.
        """
        self._wrapper.list_plane_groups(plane, lst._wrapper)
        




    def list_planes(self, lst):
        """
        List all planes in a 3D view

        **Note:**

        The plane names are placed in the list names, plane
        numbers are placed in the list values.
        
        Planes are added to the end of the `GXLST <geosoft.gxapi.GXLST>`.
        """
        self._wrapper.list_planes(lst._wrapper)
        




    def set_all_groups_to_plane(self, plane):
        """
        Set all groups to be within one plane
        """
        self._wrapper.set_all_groups_to_plane(plane)
        




    def set_all_new_groups_to_plane(self, plane):
        """
        Set all groups that are not in any plane to this plane
        """
        self._wrapper.set_all_new_groups_to_plane(plane)
        




    def set_def_plane(self, name):
        """
        Set the default drawing plane.

        **Note:**

        2D drawing to a 3D View will always be placed on the
        default drawing plane.  If no default drawing plane
        has been set, the first valid plane in the view is
        used as the default drawing plane.
        """
        self._wrapper.set_def_plane(name.encode())
        




    def set_group_to_plane(self, plane, group):
        """
        Set a group to a plane
        """
        self._wrapper.set_group_to_plane(plane, group.encode())
        




    def set_h_3dn(self, o3dn):
        """
        Set the `GX3DN <geosoft.gxapi.GX3DN>` object for this view

        **Note:**

        To make the view a 2D view, set a `GX3DN <geosoft.gxapi.GX3DN>` of NULL.
        """
        self._wrapper.set_h_3dn(o3dn._wrapper)
        




    def get_3d_point_of_view(self, x, y, z, distance, declination, inclination):
        """
        Get 3D point of view (values are will be `rDUMMY <geosoft.gxapi.rDUMMY>` if view for 2D views)
        """
        x.value, y.value, z.value, distance.value, declination.value, inclination.value = self._wrapper.get_3d_point_of_view(x.value, y.value, z.value, distance.value, declination.value, inclination.value)
        




    def set_3d_point_of_view(self, x, y, z, distance, declination, inclination):
        """
        Set 3D point of view (no effect on 2D views)
        """
        self._wrapper.set_3d_point_of_view(x, y, z, distance, declination, inclination)
        




    def set_plane_clip_ply(self, plane, pply):
        """
        Set the Plane Clip Region

        **Note:**

        By default it is the View's Clip Region
        """
        self._wrapper.set_plane_clip_ply(plane, pply._wrapper)
        




    def set_plane_equation(self, plane, pitch, yaw, roll, x, y, z, sx, sy, str_val):
        """
        Set the equation of a plane

        **Note:**

        For a grid with the "Y" axis giving elevation:
        use rotations = (-90, 0, 0) for a section with azimuth 90 (E-W)
        use rotations = (-90, 0, -90) for a section with azimuth 0 (N-S)
        """
        self._wrapper.set_plane_equation(plane, pitch, yaw, roll, x, y, z, sx, sy, str_val)
        




    def set_plane_surface(self, plane, surface):
        """
        Set the surface image of a plane
        """
        self._wrapper.set_plane_surface(plane, surface.encode())
        




    def set_plane_surf_info(self, plane, sample, base, scale, min, max):
        """
        Set the surface information
        """
        self._wrapper.set_plane_surf_info(plane, sample, base, scale, min, max)
        




# 3D Rendering 2D



    def define_plane_3d(self, center_x, center_y, center_z, x_vector_x, x_vector_y, x_vector_z, y_vector_x, y_vector_y, y_vector_z):
        """
        Define a 2D drawing plane based on point and normal

        **Note:**

        2D rendering commands are translated to 3D commands
        based on the plane.
        """
        self._wrapper.define_plane_3d(center_x, center_y, center_z, x_vector_x, x_vector_y, x_vector_z, y_vector_x, y_vector_y, y_vector_z)
        




    def define_viewer_axis_3d(self, center_x, center_y, center_z, dir_point_x, dir_point_y, dir_point_z):
        """
        Define a 2D drawing plane based on the user's view that
        oriented around the vector.
        """
        self._wrapper.define_viewer_axis_3d(center_x, center_y, center_z, dir_point_x, dir_point_y, dir_point_z)
        




    def define_viewer_plane_3d(self, center_x, center_y, center_z):
        """
        Define a 2D drawing plane based on the user's view.

        **Note:**

        The plane is always facing the viewer. Otherwise the
        this is identical to the previous
        """
        self._wrapper.define_viewer_plane_3d(center_x, center_y, center_z)
        




# Clipping



    def clip_poly_ex(self, vv_x, vv_y, unit, exclude):
        """
        Add a polygon to the clip region.

        **Note:**

        The polygon will be added to the current clip region.
        The `GXVV <geosoft.gxapi.GXVV>`'s cannot have any dummy elements.
        """
        self._wrapper.clip_poly_ex(vv_x._wrapper, vv_y._wrapper, unit, exclude)
        




    def clip_rect_ex(self, min_x, min_y, max_x, max_y, unit, exclude):
        """
        Add a rectangle to the clip region.

        **Note:**

        The rectangle will be added to the current clip region.
        """
        self._wrapper.clip_rect_ex(min_x, min_y, max_x, max_y, unit, exclude)
        




    def clip_clear(self):
        """
        Remove/clear the view clip region.
        """
        self._wrapper.clip_clear()
        




    def clip_groups(self, mode):
        """
        Set the Clipping mode on/off for all groups.
        """
        self._wrapper.clip_groups(mode)
        




    def clip_marked_groups(self, mode):
        """
        Set the Clipping mode on/off for marked groups.
        """
        self._wrapper.clip_marked_groups(mode)
        




    def clip_poly(self, vv_x, vv_y, unit):
        """
        Add a polygon to the clip region.

        **Note:**

        The polygon will be added to the current clip region.
        The `GXVV <geosoft.gxapi.GXVV>`'s cannot have any dummy elements.
        """
        self._wrapper.clip_poly(vv_x._wrapper, vv_y._wrapper, unit)
        




    def clip_rect(self, min_x, min_y, max_x, max_y, unit):
        """
        Add a rectangle to the clip region.

        **Note:**

        The rectangle will be added to the current clip region.
        """
        self._wrapper.clip_rect(min_x, min_y, max_x, max_y, unit)
        




    def delete_ext_clip_ply(self, ext_ply):
        """
        Deletes an extended clip `GXPLY <geosoft.gxapi.GXPLY>` object used by this view.
        """
        self._wrapper.delete_ext_clip_ply(ext_ply)
        




    def ext_clip_ply_list(self, lst):
        """
        Get the names of existing extended clip `GXPLY <geosoft.gxapi.GXPLY>` objects in this view as list.
        """
        self._wrapper.ext_clip_ply_list(lst._wrapper)
        




    def get_clip_ply(self, poly):
        """
        Get clipping polygons, in the user projection

        **Note:**

        The returned `GXPLY <geosoft.gxapi.GXPLY>` is recast into the User projection.
        For oriented views (especially sections), use
        `get_ply <geosoft.gxapi.GXMVIEW.get_ply>`, which returns the Clip `GXPLY <geosoft.gxapi.GXPLY>` in the view's native
        projection (e.g. the one set using `set_ipj <geosoft.gxapi.GXMVIEW.set_ipj>`).
        """
        self._wrapper.get_clip_ply(poly._wrapper)
        




    def get_ext_clip_ply(self, ext_ply, ply):
        """
        Get an extended clip `GXPLY <geosoft.gxapi.GXPLY>` object used by this view.
        """
        self._wrapper.get_ext_clip_ply(ext_ply, ply._wrapper)
        




    def get_group_ext_clip_ply(self, group, ext_ply):
        """
        Gets extended clip information for group in view.
        """
        ext_ply.value = self._wrapper.get_group_ext_clip_ply(group.encode(), ext_ply.value)
        




    def get_ply(self, poly):
        """
        Get clipping polygons, in the base projection

        **Note:**

        This should be used to get the clipping polygon for
        oriented views (especially sections).
        """
        self._wrapper.get_ply(poly._wrapper)
        




    def group_clip_mode(self, mode):
        """
        Set the Clipping mode on or off for new groups.

        **Note:**

        All new groups will be clipped.
        """
        self._wrapper.group_clip_mode(mode)
        




    def get_name_ext_clip_ply(self, ext_ply, name):
        """
        Get the name of the extended clip `GXPLY <geosoft.gxapi.GXPLY>` object in this view.
        """
        name.value = self._wrapper.get_name_ext_clip_ply(ext_ply, name.value.encode())
        




    def num_ext_clip_ply(self):
        """
        Get the number of extended clip `GXPLY <geosoft.gxapi.GXPLY>` objects in this view.
        """
        ret_val = self._wrapper.num_ext_clip_ply()
        return ret_val




    def set_ext_clip_ply(self, ext_ply, name, ply):
        """
        Set an extended clip `GXPLY <geosoft.gxapi.GXPLY>` object used by this view.
        """
        ret_val = self._wrapper.set_ext_clip_ply(ext_ply, name.encode(), ply._wrapper)
        return ret_val




    def set_clip_ply(self, poly):
        """
        Set clipping region to a `GXPLY <geosoft.gxapi.GXPLY>`
        """
        self._wrapper.set_clip_ply(poly._wrapper)
        




    def set_group_ext_clip_ply(self, group, ext_ply):
        """
        Sets extended clip information for group in view.
        """
        self._wrapper.set_group_ext_clip_ply(group.encode(), ext_ply)
        




# Color


    @classmethod
    def color2_rgb(cls, color, r, g, b):
        """
        Convert to RGB values.

        **Note:**

        Color component intensities will be in the range 0-255.

        .. seealso::

            `color <geosoft.gxapi.GXMVIEW.color>`
        """
        r.value, g.value, b.value = gxapi_cy.WrapMVIEW.color2_rgb(GXContext._get_tls_geo(), color, r.value, g.value, b.value)
        



    @classmethod
    def color_descr(cls, color, color_descr):
        """
        Convert a color to a color string label

        **Note:**

        See `color <geosoft.gxapi.GXMVIEW.color>`.
        """
        color_descr.value = gxapi_cy.WrapMVIEW.color_descr(GXContext._get_tls_geo(), color, color_descr.value.encode())
        



    @classmethod
    def color(cls, color):
        """
        Get a color from a color string label

        **Note:**

        Color strings may be "R","G","B","C","M","Y",
        "H","S","V", or "K" or a combination of these
        characters, each followed by up to three digits
        specifying a number between 0 and 255.
        An empty string produce C_ANY_NONE.
        
        You must stay in the same color model, RGB, CMY,
        HSV or K.
        
        For example "R", "R127G22", "H255S127V32"
        
        Characters are not case sensitive.

        .. seealso::

            iColorXXX_MVIEW macros
        """
        ret_val = gxapi_cy.WrapMVIEW.color(GXContext._get_tls_geo(), color.encode())
        return ret_val



    @classmethod
    def color_cmy(cls, c, m, y):
        """
        Return CMY color.

        **Note:**

        Color component intensities must be in the range 0-255.

        .. seealso::

            `color <geosoft.gxapi.GXMVIEW.color>`
        """
        ret_val = gxapi_cy.WrapMVIEW.color_cmy(GXContext._get_tls_geo(), c, m, y)
        return ret_val



    @classmethod
    def color_hsv(cls, h, s, v):
        """
        Return HSV color.

        **Note:**

        Color component intensities must be in the range 0-255.

        .. seealso::

            `color <geosoft.gxapi.GXMVIEW.color>`
        """
        ret_val = gxapi_cy.WrapMVIEW.color_hsv(GXContext._get_tls_geo(), h, s, v)
        return ret_val



    @classmethod
    def color_rgb(cls, r, g, b):
        """
        Return RGB color.

        **Note:**

        Color component intensities must be in the range 0-255.

        .. seealso::

            `color <geosoft.gxapi.GXMVIEW.color>`
        """
        ret_val = gxapi_cy.WrapMVIEW.color_rgb(GXContext._get_tls_geo(), r, g, b)
        return ret_val




# Drawing Attribute



    def clip_mode(self, mode):
        """
        Set the view clipping mode on or off.

        **Note:**

        Entitles that follow in this group will be clipped
        or not clipped depending on this mode.
        
        The montaj editor cannot change the clip mode of
        embedded clipped/unclipped enties that are controlled
        by this call.  Use the Group clipping functions
        instead.
        
        It is highly recommended that you use the `group_clip_mode <geosoft.gxapi.GXMVIEW.group_clip_mode>`
        function to control clipping on a group-by-group basis, instead
        of using `clip_mode <geosoft.gxapi.GXMVIEW.clip_mode>` when inside a group, as it is impossible
        to determine the  true visible extents of a group. In such cases, the
        "zoom to full map extents" command may give incorrect results.
        """
        self._wrapper.clip_mode(mode)
        




    def fill_color(self, color):
        """
        Set the fill color.
        """
        self._wrapper.fill_color(color)
        




    def line_color(self, color):
        """
        Set the line color.
        """
        self._wrapper.line_color(color)
        




    def line_smooth(self, smooth):
        """
        Set the line edge smoothing.
        """
        self._wrapper.line_smooth(smooth)
        




    def line_style(self, style, pitch):
        """
        Set the style of a line.

        **Note:**

        Line styles are selected by ordinal value (line style #)
        from those defined in default.lpt.  If default.lpt does
        not have a the style specified, the file user.lpt is
        searched.  If this file does not contain the line style
        solid is assumed.
        
        Note that line styles from default.lpt and user.lpt are
        read into the map at the time the map is created, not
        at display time.
        """
        self._wrapper.line_style(style, pitch)
        




    def line_thick(self, thick):
        """
        Set the line thickness.
        """
        self._wrapper.line_thick(thick)
        




    def pat_angle(self, angle):
        """
        Sets the pattern angle

        **Note:**

        Allows the user to apply a rotation to the basic
        pattern. Care should be taken to ensure that the
        tiling remains continuous; i.e. if the pattern
        consists of horizontal lines, only angles of
        -90, 0, 90, 180 (etc.) would give seamless tiling.
        However, simple, closed figure, such as a star,
        could be given any angle.
        Rotations about the center point (0.5, 0.5) of the
        unit cell are performed prior to applying PatSize.
        The default value is 0.0.
        Setting an angle of -999 inititates the random angle
        feature, and each pattern tile is rotated to a different
        angle. Using this along with PatStyle(View, `MVIEW_TILE_RANDOM <geosoft.gxapi.MVIEW_TILE_RANDOM>`)
        can give a "hand-drawn" effect to geological fills.
        
        See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._wrapper.pat_angle(angle)
        




    def pat_density(self, density):
        """
        Sets the tiling density.

        **Note:**

        This number is the ratio between the plotted unit cell size and the
        distance between the plotted tile centers. The default value is 1.
        A value larger than 1 increases the density of the pattern, while
        values less than 1 make the pattern more "spread out".
        This can be used along with sPatStyleMethod to create more complicated
        fills from simple patterns.
        
        See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._wrapper.pat_density(density)
        




    def pat_number(self, number):
        """
        Sets the pattern number

        **Note:**

        Pattern 0 is solid fill.(default)
        Set the pattern color using `fill_color <geosoft.gxapi.GXMVIEW.fill_color>`.
        
        Patterns are selected by ordinal value (pattern number)
        from those defined in default.pat.  If default.pat does
        not have a the pattern specified, the file user.pat is
        searched.  If this file does not contain the pattern
        solid is assumed.
        
        Note that patterns from default.pat and user.pat are
        read into the map at the time the map is created, not
        at display time.
        
        IMPORTANT: A call to this function resets all the various
        pattern attributes to those defined for the selected pattern.
        If you want to modify any attributes, call that function (e.g.
        sPatSize_MVIEW(), AFTER you call sPatNumber_MVIEW().
        """
        self._wrapper.pat_number(number)
        




    def pat_size(self, size):
        """
        Sets the pattern unit cell size (X)

        **Note:**

        See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._wrapper.pat_size(size)
        




    def pat_style(self, style):
        """
        Sets the tiling method (i.e. rectangle, triangle)

        **Note:**

        Normally, the unit cell is duplicated across the fill area
        like floor tiles (`MVIEW_TILE_RECTANGULAR <geosoft.gxapi.MVIEW_TILE_RECTANGULAR>`).
        DIAGONAL tiling rotates the tiling positions (but not the tiles)
        by 45 degrees.
        TRIANGULAR tiling
        Offsets each succeeding row by half the unit cell size, and
        lessens the vertical offset, so that the unit cell centers
        form a triangular grid pattern.
        RANDOM tiling adds small random offsets in both directions to give
        the diffuse effect seen on many geological maps.
        
        NOTE: Some patterns are designed to be interlocking and may only
        work "correctly" with one tiling method.
        
        See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._wrapper.pat_style(style)
        




    def pat_thick(self, thick):
        """
        Sets the pattern line thickness

        **Note:**

        See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._wrapper.pat_thick(thick)
        




    def symb_angle(self, angle):
        """
        Set the Symb angle.
        """
        self._wrapper.symb_angle(angle)
        




    def symb_color(self, color):
        """
        Set the Symbol color.
        """
        self._wrapper.symb_color(color)
        




    def symb_fill_color(self, color):
        """
        Set the Symbol color fill.
        """
        self._wrapper.symb_fill_color(color)
        




    def symb_font(self, face, geofont, weight, italic):
        """
        Set the symbol font and style.

        **Note:**

        If the font cannot be found, the DEFAULT_SYMBOL_FONT
        specified in the [MONTAJ] section of GEOSOFT.INI
        will be used.
        
        See `text_font <geosoft.gxapi.GXMVIEW.text_font>` for the font name syntax.
        """
        self._wrapper.symb_font(face.encode(), geofont, weight, italic)
        




    def symb_number(self, number):
        """
        Set the Symbol number.

        **Note:**

        The lower 16 bits of the number is interpreted as UTF-16 with a valid Unicode character
        code point. GFN fonts wil produce valid symbols depending on the font for 0x01-0x7f and the degree,
        plus-minus and diameter symbol(latin small letter o with stroke) for 0xB0, 0xB1 and 0xF8 respectively.
        
        It is possible to check if a character is valid using `GXUNC.is_valid_utf16_char <geosoft.gxapi.GXUNC.is_valid_utf16_char>`. The high 16-bits are reserved
        for future use. Also see: `GXUNC.valid_symbol <geosoft.gxapi.GXUNC.valid_symbol>` and `GXUNC.validate_symbols <geosoft.gxapi.GXUNC.validate_symbols>`.
        """
        self._wrapper.symb_number(number)
        




    def symb_size(self, size):
        """
        Set the Symb size.
        """
        self._wrapper.symb_size(size)
        




    def text_angle(self, angle):
        """
        Set the text angle.
        """
        self._wrapper.text_angle(angle)
        




    def text_color(self, color):
        """
        Set the Text color.
        """
        self._wrapper.text_color(color)
        




    def text_font(self, face, geo_font, weight, italic):
        """
        Set the text font.

        **Note:**

        Font characteristics can be defined using the function parameters,
        or may be defined as decorations in the font name.  A decorated font
        name has the following format:
        
        font_name(type,weight,italics,charset)
        
        where
        type     - "TT" or "GFN"
        weight   - last word from MVIEW_FONT_WEIGHT_ (ie. "LIGHT")
        italics  - "ITALICS" for for italics
        charset  - Before version 6.2. this decoration was honoured and it affected the display
        of characters above ASCII 127. 6.2. introduced Unicode in the core
        montaj engine that eliminated the need for such a setting. All strings
        on the GX API level are encoded in `UTF8_` during runtime which makes it possible
        to represent all possible characters without using character sets. This decoration
        will now be ignored.
        
        Qualifiers take precidence over passed parameters.
        The order of qualifiers is not relevant.
        
        examples:
        
        "sr(GFN,ITALICS)"  - geosoft GFN font, normal weight, italics
        "Arial(TT,XBOLD)"  - TrueType font, bold
        "Times(TT,ITALICS,_EastEurope)"
        - TrueType font, italics, Eastern Europe charcters
        
        Decorated name qualifiers take precedence over passed parameters.
        
        If the font cannot be found, or if "Default" is used, the DEFAULT_MAP_FONT
        specified in the [MONTAJ] section of GEOSOFT.INI
        will be used.
        """
        self._wrapper.text_font(face.encode(), geo_font, weight, italic)
        




    def text_ref(self, ref):
        """
        Set the text plot reference point.
        """
        self._wrapper.text_ref(ref)
        




    def text_size(self, size):
        """
        Set the text size.

        **Note:**

        Because views may have differing X and Y scales this size can only make sense in one of these directions
        otherwise text would appear warped on these kinds of views. The X direction was chosen to represent the
        font size. For instance if the X scale is 1 unit/mm and my Y scale is 2 units/mm a font size of 3.0 view
        units will result in un-rotated text that appears 6 view units or 3mm high in the Y direction.
        
        Another important thing to keep in mind that this size represents what is known as the "ascent" height
        of the font. The full height of the text may be higher if characters with accents or lower extension
        (e.g. the lowercase y) appear in the text. For TrueType fonts the mapping system will do a best effort
        positioning and sizing of the text using the alignment set and information about the font that it queries
        from the operating system. For instance; if Arial text "Blog" is placed at (0,0) and the alignment
        setting is Left-Bottom the left side of the B should be aligned at 0 in the X direction and the
        bottom of all the letters except y will be at 0 in the Y direction. The lower part of the y will extend
        below 0 in the Y (this is known as the "descent" height of the font at this size). The letters B and l
        should be very close to the size set here (this may differ slightly for different fonts).
        """
        self._wrapper.text_size(size)
        




    def transparency(self, trans):
        """
        Sets the transparency for new objects.

        **Note:**

        1.0 Renders completely opaque objects while 0.0 will be transparent.
        Objects written after this will have a combined transparency value with the
        group transparency if it is set (e.g. 0.5 for group and 0.8 stream will result in 0.4).
        """
        self._wrapper.transparency(trans)
        




    def z_value(self, val):
        """
        Sets Z-value info.

        **Note:**

        This number is stored in map mainly for exports to other vector formats (e.g ShapeFiles)
        A contour map that's exported to a shape file will use this value as a Z-value attributes for its shapes.
        """
        self._wrapper.z_value(val)
        




# Drawing Entity



    def arc(self, x, y, radius, ratio, angle, start, end):
        """
        Draw an arc.
        """
        self._wrapper.arc(x, y, radius, ratio, angle, start, end)
        




    def chord(self, x, y, radius, ratio, angle, start, end):
        """
        Draw a filled arc.
        """
        self._wrapper.chord(x, y, radius, ratio, angle, start, end)
        




    def classified_symbols(self, vv_x, vv_y, vv_z, scal_mm, zmin, zval, size, fcol):
        """
        Plot classified symbols

        **Note:**

        For example, to plot three levels <95, 95-100 and
        100-120, three string arguments would be:
        
        "95,100,120"      maximums of each class
        "2.0,2.5,3.0"     sizes in mm
        "y,g,r"           fill colors
        """
        self._wrapper.classified_symbols(vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, scal_mm, zmin, zval.encode(), size.encode(), fcol.encode())
        




    def complex_polygon(self, vv_i, vv_x, vv_y):
        """
        Draw a polygon with holes in it.

        **Note:**

        You pass a `GXVV <geosoft.gxapi.GXVV>` with polygon sizes and 2 point vvs.
        """
        self._wrapper.complex_polygon(vv_i._wrapper, vv_x._wrapper, vv_y._wrapper)
        




    def ellipse(self, x, y, radius, ratio, angle):
        """
        Draw an ellipse
        """
        self._wrapper.ellipse(x, y, radius, ratio, angle)
        




    def line(self, x0, y0, x1, y1):
        """
        Draw a line.
        """
        self._wrapper.line(x0, y0, x1, y1)
        




    def line_vv(self, gvv):
        """
        Draw line segments stored in a GS_D2LINE `GXVV <geosoft.gxapi.GXVV>`.
        """
        self._wrapper.line_vv(gvv._wrapper)
        




    def polygon_dm(self, vv_x, vv_y):
        """
        Like PolyLineDm, but draw polygons.
        """
        self._wrapper.polygon_dm(vv_x._wrapper, vv_y._wrapper)
        




    def polygon_ply(self, ply):
        """
        Draw a complex polygon from `GXPLY <geosoft.gxapi.GXPLY>`.
        """
        self._wrapper.polygon_ply(ply._wrapper)
        




    def poly_line(self, type, vv_x, vv_y):
        """
        Draw a polyline or polygon (dummies deleted).

        **Note:**

        Dummies in X and/or Y `GXVV <geosoft.gxapi.GXVV>` are deleted and it results
        in 'solid' line. Using `poly_line_dm <geosoft.gxapi.GXMVIEW.poly_line_dm>` (below) function
        if gaps from dummies are to be kept.
        """
        self._wrapper.poly_line(type, vv_x._wrapper, vv_y._wrapper)
        




    def poly_line_dm(self, vv_x, vv_y):
        """
        Draw a polyline with gaps defined by dummies in X/Y VVs
        """
        self._wrapper.poly_line_dm(vv_x._wrapper, vv_y._wrapper)
        




    def poly_wrap(self, vv_x, vv_y):
        """
        Draw wrapped polylines from X and Y `GXVV <geosoft.gxapi.GXVV>`'s.

        **Note:**

        Convert a given VVy into a wrapped VVy using
        the current view window as the wrap region.
        Then draw polylines from it.

        .. seealso::

            `poly_line <geosoft.gxapi.GXMVIEW.poly_line>`
        """
        self._wrapper.poly_wrap(vv_x._wrapper, vv_y._wrapper)
        




    def rectangle(self, x0, y0, x1, y1):
        """
        Draw a rectangle.
        """
        self._wrapper.rectangle(x0, y0, x1, y1)
        




    def segment(self, x, y, radius, ratio, angle, start, end):
        """
        Draw a filled segment of an ellipse.
        """
        self._wrapper.segment(x, y, radius, ratio, angle, start, end)
        




    def size_symbols(self, vv_x, vv_y, vv_z):
        """
        Plot sized symbols
        """
        self._wrapper.size_symbols(vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        




    def symbol(self, x, y):
        """
        Plot a symbol
        """
        self._wrapper.symbol(x, y)
        




    def symbols(self, vv_x, vv_y):
        """
        Plot symbols
        """
        self._wrapper.symbols(vv_x._wrapper, vv_y._wrapper)
        




    def symbols_itr(self, itr, vv_x, vv_y, vv_z):
        """
        Plot symbols using an `GXITR <geosoft.gxapi.GXITR>`
        """
        self._wrapper.symbols_itr(itr.encode(), vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        




    def text(self, text, x, y):
        """
        Draw text.
        """
        self._wrapper.text(text.encode(), x, y)
        




# Drawing Object



    def aggregate(self, agg, name):
        """
        Add an aggregate to a view.
        """
        self._wrapper.aggregate(agg._wrapper, name.encode())
        




    def get_aggregate(self, group):
        """
        Get an existing Aggregate object from the view.

        **Note:**

        This method returns a cached object owned by the `GXMVIEW <geosoft.gxapi.GXMVIEW>` and will be destroyed automatically when the `GXMVIEW <geosoft.gxapi.GXMVIEW>` is disposed
        """
        ret_val = self._wrapper.get_aggregate(group)
        return GXAGG(ret_val)




    def change_line_message(self, line):
        """
        Change the specified line in a view.

        **Note:**

        The line name can be created by calling LineLabel_DB using
        `DB_LINE_LABEL_FORMAT_LINK <geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINK>`. This insures that the label is
        created is the same way as used in the database.
        """
        self._wrapper.change_line_message(line.encode())
        




    def col_symbol(self, name, csymb):
        """
        Add a colored symbol object to a view.
        """
        self._wrapper.col_symbol(name.encode(), csymb._wrapper)
        




    def get_col_symbol(self, group):
        """
        Get an existing colored symbol object from the view.

        **Note:**

        This method returns a cached object owned by the `GXMVIEW <geosoft.gxapi.GXMVIEW>` and will be destroyed automatically when the `GXMVIEW <geosoft.gxapi.GXMVIEW>` is disposed
        """
        ret_val = self._wrapper.get_col_symbol(group)
        return GXCSYMB(ret_val)




    def datalinkd(self, datalinkd, name):
        """
        Add a Data Link Display (`GXDATALINKD <geosoft.gxapi.GXDATALINKD>`) object to the view.
        """
        self._wrapper.datalinkd(datalinkd._wrapper, name.encode())
        




    def get_datalinkd(self, group):
        """
        Get an existing Data Link Display (`GXDATALINKD <geosoft.gxapi.GXDATALINKD>`) object from the view.

        **Note:**

        This method returns a cached object owned by the `GXMVIEW <geosoft.gxapi.GXMVIEW>` and will be destroyed automatically when the `GXMVIEW <geosoft.gxapi.GXMVIEW>` is disposed
        """
        ret_val = self._wrapper.get_datalinkd(group)
        return GXDATALINKD(ret_val)




    def easy_maker(self, name, groups):
        """
        Used for GX makers which use both maps and databases.
        """
        self._wrapper.easy_maker(name.encode(), groups.encode())
        




    def emf_object(self, min_x, min_y, max_x, max_y, file):
        """
        Add an EMF file data object to the view.
        """
        self._wrapper.emf_object(min_x, min_y, max_x, max_y, file.encode())
        




    def external_string_object(self, min_x, min_y, max_x, max_y, name, cl, data):
        """
        Add an external string data object to the view.
        """
        self._wrapper.external_string_object(min_x, min_y, max_x, max_y, name.encode(), cl.encode(), data.encode())
        




    def link(self, db, name):
        """
        Make a link to a database.
        """
        self._wrapper.link(db._wrapper, name.encode())
        




    def maker(self, db, map, prog, type, name, groups):
        """
        Generates a Maker for the database and/or map.
        """
        self._wrapper.maker(db, map, prog.encode(), type, name.encode(), groups.encode())
        




    def meta(self, meta, name):
        """
        Store Metadata in a group
        """
        self._wrapper.meta(meta._wrapper, name.encode())
        




    def voxd(self, voxd, name):
        """
        Add a Voxel Display (`GXVOXD <geosoft.gxapi.GXVOXD>`) object to the view.
        """
        self._wrapper.voxd(voxd._wrapper, name.encode())
        




    def get_voxd(self, group):
        """
        Get an existing `GXVOXD <geosoft.gxapi.GXVOXD>` object from the view.

        **Note:**

        This method returns a cached object owned by the `GXMVIEW <geosoft.gxapi.GXMVIEW>` and will be destroyed automatically when the `GXMVIEW <geosoft.gxapi.GXMVIEW>` is disposed
        """
        ret_val = self._wrapper.get_voxd(group)
        return GXVOXD(ret_val)




    def draw_vector_voxel_vectors(self, vox, group, itr, scale_factor, height_base_ratio, max_base_size_ratio, cutoff_value, max_vectors):
        """
        Display vectors from a vector voxel in the view.

        **Note:**

        This will result in a `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>` group object within the view
        """
        self._wrapper.draw_vector_voxel_vectors(vox._wrapper, group.encode(), itr._wrapper, scale_factor, height_base_ratio, max_base_size_ratio, cutoff_value, max_vectors)
        




    def get_vector_3d(self, group):
        """
        Get an existing `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>` object from the view.

        **Note:**

        This method returns a cached object owned by the `GXMVIEW <geosoft.gxapi.GXMVIEW>` and will be destroyed automatically when the `GXMVIEW <geosoft.gxapi.GXMVIEW>` is disposed
        """
        ret_val = self._wrapper.get_vector_3d(group)
        return GXVECTOR3D(ret_val)




    def draw_vectors_3d(self, group, vv_x, vv_y, vv_z, vv_vx, vv_vy, vv_vz, itr, scale_for_max_vector, height_base_ratio, max_base_size_ratio):
        """
        Display vectors in the view.
        """
        self._wrapper.draw_vectors_3d(group.encode(), vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_vx._wrapper, vv_vy._wrapper, vv_vz._wrapper, itr._wrapper, scale_for_max_vector, height_base_ratio, max_base_size_ratio)
        




# Group Methods



    def set_group_itr(self, group, itr):
        """
        Set group `GXITR <geosoft.gxapi.GXITR>`

        **Note:**

        A group `GXITR <geosoft.gxapi.GXITR>` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._wrapper.set_group_itr(group, itr._wrapper)
        




    def get_group_itr(self, group):
        """
        Get group `GXITR <geosoft.gxapi.GXITR>`

        **Note:**

        A group `GXITR <geosoft.gxapi.GXITR>` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._wrapper.get_group_itr(group)
        return GXITR(ret_val)




    def group_itr_exists(self, group):
        """
        Determine if group `GXITR <geosoft.gxapi.GXITR>` exists.

        **Note:**

        A group `GXITR <geosoft.gxapi.GXITR>` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._wrapper.group_itr_exists(group)
        return ret_val




    def delete_group_itr(self, group):
        """
        Deletes existing `GXITR <geosoft.gxapi.GXITR>` associated with a group.

        **Note:**

        A group `GXITR <geosoft.gxapi.GXITR>` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._wrapper.delete_group_itr(group)
        




    def set_group_tpat(self, group, tpat):
        """
        Set group `GXTPAT <geosoft.gxapi.GXTPAT>`

        **Note:**

        A group `GXTPAT <geosoft.gxapi.GXTPAT>` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._wrapper.set_group_tpat(group, tpat._wrapper)
        




    def get_group_tpat(self, group):
        """
        Get group `GXTPAT <geosoft.gxapi.GXTPAT>`

        **Note:**

        A group `GXTPAT <geosoft.gxapi.GXTPAT>` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._wrapper.get_group_tpat(group)
        return GXTPAT(ret_val)




    def group_tpat_exists(self, group):
        """
        Determine if group `GXTPAT <geosoft.gxapi.GXTPAT>` exists.

        **Note:**

        A group `GXTPAT <geosoft.gxapi.GXTPAT>` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._wrapper.group_tpat_exists(group)
        return ret_val




    def delete_group_tpat(self, group):
        """
        Deletes existing `GXTPAT <geosoft.gxapi.GXTPAT>` associated with a group.

        **Note:**

        A group `GXTPAT <geosoft.gxapi.GXTPAT>` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._wrapper.delete_group_tpat(group)
        




    def group_storage_exists(self, group, storage_name):
        """
        Determine if generic storage associated with a group exists.

        **Note:**

        External API users should not use storage names starting with "Geosoft"
        """
        ret_val = self._wrapper.group_storage_exists(group, storage_name.encode())
        return ret_val




    def read_group_storage(self, group, storage_name):
        """
        Reads existing generic storage associated with a group into an in-memory `GXBF <geosoft.gxapi.GXBF>`.

        **Note:**

        External API users should not use storage names starting with "Geosoft"
        """
        ret_val = self._wrapper.read_group_storage(group, storage_name.encode())
        return GXBF(ret_val)




    def delete_group_storage(self, group, storage_name):
        """
        Deletes existing generic storage associated with a group.

        **Note:**

        External API users should not use storage names starting with "Geosoft"
        """
        self._wrapper.delete_group_storage(group, storage_name.encode())
        




    def write_group_storage(self, group, storage_name, bf):
        """
        Open generic existing storage associated with a group for reading.

        **Note:**

        External API users should not use storage names starting with "Geosoft"
        """
        self._wrapper.write_group_storage(group, storage_name.encode(), bf._wrapper)
        




    def copy_marked_groups(self, mvie_wd):
        """
        Copies all marked groups from one view into another view

        **Note:**

        Projections in source and destination views are used to copy the
        entities. Entities are clipped by the destination view's clipping
        region.
        """
        self._wrapper.copy_marked_groups(mvie_wd._wrapper)
        




    def copy_raw_marked_groups(self, mvie_wd):
        """
        Copies all marked groups raw from one view into another

        **Note:**

        The projections, and clipping is completly ignored.
        """
        self._wrapper.copy_raw_marked_groups(mvie_wd._wrapper)
        




    def crc_group(self, name, crc):
        """
        Compute CRC for a group.
        """
        ret_val = self._wrapper.crc_group(name.encode(), crc)
        return ret_val




    def delete_group(self, group):
        """
        Delete a group.

        **Note:**

        Does nothing if the group does not already exist.
        """
        self._wrapper.delete_group(group.encode())
        




    def del_marked_groups(self):
        """
        Delete marked groups.
        """
        self._wrapper.del_marked_groups()
        




    def get_group_extent(self, group_name, xmin, ymin, xmax, ymax, unit):
        """
        Get extent of a group in a view
        """
        xmin.value, ymin.value, xmax.value, ymax.value = self._wrapper.get_group_extent(group_name.encode(), xmin.value, ymin.value, xmax.value, ymax.value, unit)
        




    def get_group_transparency(self, group_name, trans):
        """
        Gets the transparency value of group
        """
        trans.value = self._wrapper.get_group_transparency(group_name.encode(), trans.value)
        




    def group_to_ply(self, name, pply):
        """
        Save all polygons in group into `GXPLY <geosoft.gxapi.GXPLY>` obj.

        **Note:**

        The coordinates will be in the working coordinate system
        of the view.  The SetWorkingIPJ_MVIEW method can be used
        to change the working coordinate system. This function will
        return an empty `GXPLY <geosoft.gxapi.GXPLY>` if the group is hidden.
        """
        self._wrapper.group_to_ply(name.encode(), pply._wrapper)
        




    def hide_marked_groups(self, mode):
        """
        Hide/Show marked groups.
        """
        self._wrapper.hide_marked_groups(mode)
        




    def hide_shadow2_d_interpretations(self, mode):
        """
        Hide/Show 2d shadow interpretations.
        """
        self._wrapper.hide_shadow2_d_interpretations(mode)
        




    def exist_group(self, name):
        """
        Checks to see if a group exists.
        """
        ret_val = self._wrapper.exist_group(name.encode())
        return ret_val




    def gen_new_group_name(self, group, new_name):
        """
        Generate the name of a group from a base name that
        is new. (always unique and won't overwrite existing
        objects).
        """
        new_name.value = self._wrapper.gen_new_group_name(group.encode(), new_name.value.encode())
        




    def is_group(self, group, what):
        """
        Query a status or characteristic of a group
        """
        ret_val = self._wrapper.is_group(group.encode(), what)
        return ret_val




    def is_group_empty(self, group):
        """
        Is the group empty?
        """
        ret_val = self._wrapper.is_group_empty(group.encode())
        return ret_val




    def is_movable(self):
        """
        Is this view movable?

        **Note:**

        Views are always physically movable in the API, this
        flag is for preventing accidental moving in the `GXGUI <geosoft.gxapi.GXGUI>`.
        By default views are not movable.
        """
        ret_val = self._wrapper.is_movable()
        return ret_val




    def is_visible(self):
        """
        Is this view visible?
        """
        ret_val = self._wrapper.is_visible()
        return ret_val




    def list_groups(self, lst, flag):
        """
        Get a list of the groups in a view.
        """
        ret_val = self._wrapper.list_groups(lst._wrapper, flag)
        return ret_val




    def render_order(self):
        """
        Query the view render order

        **Note:**

        Views with lower numbers should render first, `iDUMMY <geosoft.gxapi.iDUMMY>` is undefined
        """
        ret_val = self._wrapper.render_order()
        return ret_val




    def mark_all_groups(self, mark):
        """
        Mark or unmark all groups.
        """
        self._wrapper.mark_all_groups(mark)
        




    def mark_empty_groups(self, mark):
        """
        Mark/unmark all empty groups.
        """
        self._wrapper.mark_empty_groups(mark)
        




    def mark_group(self, name, mark):
        """
        Mark or unmark a specific group
        """
        self._wrapper.mark_group(name.encode(), mark)
        




    def move_group_backward(self, group):
        """
        Move the group backward one position (render sooner).
        """
        self._wrapper.move_group_backward(group.encode())
        




    def move_group_forward(self, group):
        """
        Move the group forward one position (render later).
        """
        self._wrapper.move_group_forward(group.encode())
        




    def move_group_to_back(self, group):
        """
        Move the group to the back (render first).
        """
        self._wrapper.move_group_to_back(group.encode())
        




    def move_group_to_front(self, group):
        """
        Move the group to the front (render last).
        """
        self._wrapper.move_group_to_front(group.encode())
        




    def rename_group(self, old, new):
        """
        Rename a group.

        **Note:**

        Does nothing if the group does not already exist.
        """
        self._wrapper.rename_group(old.encode(), new.encode())
        




    def set_group_moveable(self, group, move):
        """
        Set the movable attribute of a group.
        """
        self._wrapper.set_group_moveable(group.encode(), move)
        




    def set_group_transparency(self, group_name, trans):
        """
        Sets the transparency value of group
        """
        self._wrapper.set_group_transparency(group_name.encode(), trans)
        




    def set_mark_moveable(self, move):
        """
        Set the movable attribute of marked groups.
        """
        self._wrapper.set_mark_moveable(move)
        




    def set_movability(self, flag):
        """
        Set the view movability

        **Note:**

        Views are always physically movable in the API, this
        flag is for preventing accidental moving in the `GXGUI <geosoft.gxapi.GXGUI>`.
        By default views are not movable.
        """
        self._wrapper.set_movability(flag)
        




    def set_render_order(self, order):
        """
        Set the view render order

        **Note:**

        Views with lower numbers should render first, `iDUMMY <geosoft.gxapi.iDUMMY>` is undefined
        """
        self._wrapper.set_render_order(order)
        




    def set_visibility(self, flag):
        """
        Set the view visibility
        """
        self._wrapper.set_visibility(flag)
        




    def start_group(self, name, mode):
        """
        Start a group.

        **Note:**

        Line and fill colors and thickness must be set
        before drawing to a group.
        
        If the group name is NULL, output will be sent to
        the primary group stream and the `MVIEW_GROUP_` is
        ignored.
        
        Group names must be different from view names.
        """
        self._wrapper.start_group(name.encode(), mode)
        




    def get_group_guid(self, group, guid):
        """
        Gets a GUID of a group in the `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

        **Note:**

        If a GUID was never queried a new one will be assigned and the map will be modified. Only if the map is saved will this value then persist.
        """
        guid.value = self._wrapper.get_group_guid(group, guid.value.encode())
        




    def find_group_by_guid(self, guid):
        """
        Find a Group by name.
        """
        ret_val = self._wrapper.find_group_by_guid(guid.encode())
        return ret_val




# Projection



    def set_working_ipj(self, ipj):
        """
        Set the working projection of the view.

        **Note:**

        The working projection is the coordinate system of coordinates drawn to
        the view.  The working coordinate system can be different than the view
        coordinate system, in which case the coordinates are re-projected to the
        view coordinate system before they are placed in the view.

        .. seealso::

            `mode_pj <geosoft.gxapi.GXMVIEW.mode_pj>` to control use of the working projection.
        """
        self._wrapper.set_working_ipj(ipj._wrapper)
        




    def clear_esrild_ts(self):
        """
        Clear ESRI local datum transformations currently in use.
        """
        self._wrapper.clear_esrild_ts()
        




    def is_projection_empty(self):
        """
        Returns 1 if the view projection and view user projection are both empty (undefined).

        **Note:**

        Use, for instance, to see if the map view contains projection information. The first time you add data that
        has projection information you should set up an empty view projection so that subsequent data added with a different
        projection is properly displayed in relation to the initial data.
        """
        ret_val = self._wrapper.is_projection_empty()
        return ret_val




    def get_ipj(self, ipj):
        """
        Get the projection of the view.
        """
        self._wrapper.get_ipj(ipj._wrapper)
        




    def get_user_ipj(self, ipj):
        """
        Get the user projection of the view.
        """
        self._wrapper.get_user_ipj(ipj._wrapper)
        




    def mode_pj(self, mode):
        """
        Set the working projection mode

        **Note:**

        This controls how your coordinates and attributes will be interpreted.
        A working projection must be set useing SetWorkingIPJ_MVIEW for this
        method to have any effect.

        .. seealso::

            SetWorkingIPJ
        """
        self._wrapper.mode_pj(mode)
        




    def north(self):
        """
        Returns North direction at center of view.

        **Note:**

        North is calculated from the `GXIPJ <geosoft.gxapi.GXIPJ>` North direction.
        It will be `rDUMMY <geosoft.gxapi.rDUMMY>` if `GXIPJ <geosoft.gxapi.GXIPJ>` is unknown.
        """
        ret_val = self._wrapper.north()
        return ret_val




    def set_ipj(self, ipj):
        """
        Set the projection of the view.

        **Note:**

        This function also sets the User `GXIPJ <geosoft.gxapi.GXIPJ>`,
        and automatically clears the WARP before doing so.
        This would be equivalent to calling :func:`_ClearWarp_IPJ'
        followed by `set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>` on the view.
        """
        self._wrapper.set_ipj(ipj._wrapper)
        




    def set_user_ipj(self, ipj):
        """
        Set the user projection of the view.
        """
        self._wrapper.set_user_ipj(ipj._wrapper)
        




# Render



    def get_3d_group_flags(self, group_num):
        """
        Get a 3D geometry group's 3D rendering flags.
        """
        ret_val = self._wrapper.get_3d_group_flags(group_num)
        return ret_val




    def set_3d_group_flags(self, group_num, flags):
        """
        Set a 3D geometry group's 3D rendering flags.
        """
        self._wrapper.set_3d_group_flags(group_num, flags)
        




    def get_group_freeze_scale(self, group_num, scale):
        """
        Get a scale freezing value for the group (`rDUMMY <geosoft.gxapi.rDUMMY>` for disabled).
        """
        scale.value = self._wrapper.get_group_freeze_scale(group_num, scale.value)
        




    def set_freeze_scale(self, scale):
        """
        Set a scale freezing value into stream (`rDUMMY <geosoft.gxapi.rDUMMY>` for disabled).

        **Note:**

        Objects written after this will override any scale freezing set for the group
        """
        self._wrapper.set_freeze_scale(scale)
        




    def set_group_freeze_scale(self, group_num, scale):
        """
        Set a scale freezing value for the group (`rDUMMY <geosoft.gxapi.rDUMMY>` for disabled).
        """
        self._wrapper.set_group_freeze_scale(group_num, scale)
        




    def find_group(self, group_name):
        """
        Find a Group by name.
        """
        ret_val = self._wrapper.find_group(group_name.encode())
        return ret_val




    def group_name(self, group_num, group_name):
        """
        Get a group name
        """
        group_name.value = self._wrapper.group_name(group_num, group_name.value.encode())
        




    def render(self, hdc, h_dc, left, bottom, right, top, min_x, min_y, max_x):
        """
        Render a specified area of view onto a Windows DC handle
        """
        self._wrapper.render(hdc, h_dc, left, bottom, right, top, min_x, min_y, max_x)
        




# Utility Drawing



    def set_u_fac(self, hdc):
        """
        Set the unit conversion of a view.
        """
        self._wrapper.set_u_fac(hdc)
        




    def axis_x(self, hdc, h_dc, left, bottom, right, top):
        """
        Draw an X axis

        **Note:**

        All coordinates are in view units.

        .. seealso::

            rOptimumTick_MVIEW
        """
        self._wrapper.axis_x(hdc, h_dc, left, bottom, right, top)
        




    def axis_y(self, hdc, h_dc, left, bottom, right, top):
        """
        Draw a  Y axis

        **Note:**

        All coordinates are in view units.

        .. seealso::

            rOptimumTick_MVIEW
        """
        self._wrapper.axis_y(hdc, h_dc, left, bottom, right, top)
        




    def grid(self, hdc, h_dc, left, bottom, right):
        """
        Draw a grid in the current window

        **Note:**

        The grid will be drawn in the current window specified
        by the last SetWindow call.

        .. seealso::

            `axis_x <geosoft.gxapi.GXMVIEW.axis_x>`, `axis_y <geosoft.gxapi.GXMVIEW.axis_y>`, `optimum_tick <geosoft.gxapi.GXMVIEW.optimum_tick>`
        """
        self._wrapper.grid(hdc, h_dc, left, bottom, right)
        




    def label_fid(self, hdc, h_dc, left, bottom, right, top):
        """
        Label fiducials on a profile

        **Note:**

        A 1mm long vertical tick is drawn at the place
        where a label is present. The label is drawn
        below the tick.
        
        The incoming X `GXVV <geosoft.gxapi.GXVV>` is used to define the place for
        label.
        """
        self._wrapper.label_fid(hdc._wrapper, h_dc, left, bottom, right, top)
        




    def label_x(self, hdc, h_dc, left, bottom, right, top, min_x):
        """
        Label annotations on the X axis

        **Note:**

        Label bounding will justify edge labels to be inside
        the bar limits. But bounding does not apply if
        labels are drawn vertically (top right or top left)

        .. seealso::

            `axis_x <geosoft.gxapi.GXMVIEW.axis_x>`, `axis_y <geosoft.gxapi.GXMVIEW.axis_y>`, `optimum_tick <geosoft.gxapi.GXMVIEW.optimum_tick>`
        """
        self._wrapper.label_x(hdc, h_dc, left, bottom, right, top, min_x)
        




    def label_y(self, hdc, h_dc, left, bottom, right, top, min_x):
        """
        Label annotations on the Y axis

        **Note:**

        Label bounding will justify edge labels to be inside
        the bar limits. But bounding does not apply if
        labels are drawn vertically (top right or top left)

        .. seealso::

            `axis_x <geosoft.gxapi.GXMVIEW.axis_x>`, `axis_y <geosoft.gxapi.GXMVIEW.axis_y>`, `optimum_tick <geosoft.gxapi.GXMVIEW.optimum_tick>`
        """
        self._wrapper.label_y(hdc, h_dc, left, bottom, right, top, min_x)
        



    @classmethod
    def optimum_tick(cls, mview, hdc, h_dc):
        """
        Return a default optimum tick interval
        """
        h_dc.value = gxapi_cy.WrapMVIEW.optimum_tick(GXContext._get_tls_geo(), mview, hdc, h_dc.value)
        




# View


    @classmethod
    def create(cls, map, name, mode):
        """
        Create `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

        **Note:**

        View scaling is set to mm on the map and the view
        origin is set to the map origin.
        """
        ret_val = gxapi_cy.WrapMVIEW.create(GXContext._get_tls_geo(), map._wrapper, name.encode(), mode)
        return GXMVIEW(ret_val)



    @classmethod
    def create_crooked_section(cls, map, ipj, h_dc, left, bottom, right, top, min_x, min_y, max_x, max_y, v_vxs, v_vx, v_vy):
        """
        Creates a new crooked section view.

        **Note:**

        A crooked section is a section running vertically beneath
        a path of (X, Y) locations, like a river. This view supports
        linking to other plan, section, or 3D views.
        The data view coordinates are set up so that vertical coordinate
        corresponds to elevation, and the X coordinate is the distance along
        the crooked feature, beginning at zero on the left, but the
        status bar will show the true (X, Y, Z) location.
        
        If the scale is set to `rDUMMY <geosoft.gxapi.rDUMMY>`, then it will be calculated so that
        the points will all fit horizontally.
        """
        ret_val = gxapi_cy.WrapMVIEW.create_crooked_section(GXContext._get_tls_geo(), map._wrapper, ipj._wrapper, h_dc.encode(), left, bottom, right, top, min_x, min_y, max_x, max_y, v_vxs._wrapper, v_vx._wrapper, v_vy._wrapper)
        return GXMVIEW(ret_val)



    @classmethod
    def create_crooked_section_data_profile(cls, map, ipj, name, x0, y0, xs, ys, scale, dist0, min_z, max_z, log_z, v_vxs, v_vx, v_vy):
        """
        Creates a new crooked section data profile view.

        **Note:**

        This is the same as `create_crooked_section <geosoft.gxapi.GXMVIEW.create_crooked_section>`, except that the
        vertical axis plots a data value, not elevation, and allows for
        logarithmic scaling.
        
        See Also: `create_crooked_section <geosoft.gxapi.GXMVIEW.create_crooked_section>`.
        """
        ret_val = gxapi_cy.WrapMVIEW.create_crooked_section_data_profile(GXContext._get_tls_geo(), map._wrapper, ipj._wrapper, name.encode(), x0, y0, xs, ys, scale, dist0, min_z, max_z, log_z, v_vxs._wrapper, v_vx._wrapper, v_vy._wrapper)
        return GXMVIEW(ret_val)






    def extent(self, what, unit, min_x, min_y, max_x, max_y):
        """
        Get the view extents

        **Note:**

        The CLIP region is the current view window or the limits
        of the current clip polygon.
        
        If `MVIEW_EXTENT_ALL <geosoft.gxapi.MVIEW_EXTENT_ALL>` is requested and the view has no groups, the
        clip extents are returned.
        
        If clip extents are requested and there are no clip extents, an
        area 0.0,0.0 1.0,1.0 is returned.
        
        The `MVIEW_EXTENT_VISIBLE <geosoft.gxapi.MVIEW_EXTENT_VISIBLE>` flag will return the union of the `MVIEW_EXTENT_CLIP <geosoft.gxapi.MVIEW_EXTENT_CLIP>` area and the
        extents of all non-masked visible groups in the view.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.extent(what, unit, min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_map(self):
        """
        Get the `GXMAP <geosoft.gxapi.GXMAP>` of the view.
        """
        ret_val = self._wrapper.get_map()
        return GXMAP(ret_val)




    def get_reg(self):
        """
        Get the `GXREG <geosoft.gxapi.GXREG>` of the view.
        """
        ret_val = self._wrapper.get_reg()
        return GXREG(ret_val)




    def get_name(self, name):
        """
        Gets the name of a view.
        """
        name.value = self._wrapper.get_name(name.value.encode())
        




    def get_guid(self, guid):
        """
        Gets the GUID of the `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

        **Note:**

        If a GUID was never queried a new one will be assigned and the map will be modified. Only if the map is saved will this value then persist.
        """
        guid.value = self._wrapper.get_guid(guid.value.encode())
        




# View Control



    def plot_to_view(self, x, y):
        """
        Convert a plot coordinate in mm to a VIEW coordinate.
        """
        x.value, y.value = self._wrapper.plot_to_view(x.value, y.value)
        




    def set_thin_res(self, thin):
        """
        Set polyline/polygon thinning resolution

        **Note:**

        The thinning resolution controls the removal of
        redundant points from polylines and polygons.  Points
        that deviate from a straight line by less than the
        thinning resolution are removed.  This can significantly
        reduce the size of a `GXMAP <geosoft.gxapi.GXMAP>` file.
        We recommend that you set the thinning resolution to
        0.02 mm.
        
        By default, the thinning resolution is set to 0.05mm.
        
        Set resolution to 0.0 to remove colinear points only.
        
        To turn off thinning after turning it on, call
        SetThinRes_MVIEW with a resolution of -1.
        """
        self._wrapper.set_thin_res(thin)
        




    def view_to_plot(self, x, y):
        """
        Convert a VIEW coordinate to a plot coordinate in mm.
        """
        x.value, y.value = self._wrapper.view_to_plot(x.value, y.value)
        




    def best_fit_window(self, m_min_x, m_min_y, m_max_x, m_max_y, v_min_x, v_min_y, v_max_x, v_max_y, fit_view):
        """
        Fit an area in ground coordinates centered to an area in mm on map or vise versa
        keeping X and Y scales the same.

        **Note:**

        X and Y scales will be redefined and units will remain unchanged.
        The final X and Y ranges (if changed) are returned.

        .. seealso::

            `fit_window <geosoft.gxapi.GXMVIEW.fit_window>`
        """
        m_min_x.value, m_min_y.value, m_max_x.value, m_max_y.value, v_min_x.value, v_min_y.value, v_max_x.value, v_max_y.value = self._wrapper.best_fit_window(m_min_x.value, m_min_y.value, m_max_x.value, m_max_y.value, v_min_x.value, v_min_y.value, v_max_x.value, v_max_y.value, fit_view)
        




    def fit_map_window_3d(self, m_min_x, m_min_y, m_max_x, m_max_y, v_min_x, v_min_y, v_max_x, v_max_y):
        """
        Set the 2D view window for a 3D view.

        **Note:**

        3D views are placed in 2D maps within a 2D mapping window
        that is analgous to a 2D View.  This allows all 2D functions
        (such as changing a view location and size) to treat a 3D
        view just like a 2D view.
        
        The `fit_map_window_3d <geosoft.gxapi.GXMVIEW.fit_map_window_3d>` function allows you to
        locate and set the "apparent" 2D mapping of a 3D view on
        the map. An intial map window is established
        as specified on the map, and the view scaling is
        established to fit the specified area within that
        map area.
        """
        self._wrapper.fit_map_window_3d(m_min_x, m_min_y, m_max_x, m_max_y, v_min_x, v_min_y, v_max_x, v_max_y)
        




    def fit_window(self, m_min_x, m_min_y, m_max_x, m_max_y, v_min_x, v_min_y, v_max_x, v_max_y):
        """
        Fit an area in ground coordinates to an area in mm on map.

        **Note:**

        X and Y scales will be redefined and the units will be set to <unknown>.
        Coordinate ranges must be greater than 0.0.

        .. seealso::

            `set_window <geosoft.gxapi.GXMVIEW.set_window>`
        """
        self._wrapper.fit_window(m_min_x, m_min_y, m_max_x, m_max_y, v_min_x, v_min_y, v_max_x, v_max_y)
        




    def get_class_name(self, cl, name):
        """
        Get a class name.

        **Note:**

        `GXMVIEW <geosoft.gxapi.GXMVIEW>` class names are intended to be used to record the
        names of certain classes in the view, such as "Plane"
        for the default drawing plane.
        """
        name.value = self._wrapper.get_class_name(cl.encode(), name.value.encode())
        




    def map_origin(self, x_origin, y_origin):
        """
        Get the map origin from a view
        """
        x_origin.value, y_origin.value = self._wrapper.map_origin(x_origin.value, y_origin.value)
        




    def re_scale(self, scale):
        """
        Change the scale of a view.

        **Note:**

        The view size is multiplied by the scale factor.
        The view location will move relative to the map origin
        by the scale factor.
        """
        self._wrapper.re_scale(scale)
        




    def get_map_scale(self):
        """
        Get the current map scale of the view
        """
        ret_val = self._wrapper.get_map_scale()
        return ret_val




    def scale_mm(self):
        """
        Get the horizontal scale in view X units/mm

        **Note:**

        The scale factor is intended to be used by methods
        that would like to specify sizes in mm.  Examples
        would be text sizes, line thicknesses and line
        pitch.
        """
        ret_val = self._wrapper.scale_mm()
        return ret_val




    def scale_pj_mm(self):
        """
        Get horizontal scale in projected user units/mm

        **Note:**

        The scale factor is intended to be used by methods
        that would like to specify sizes in mm.  Examples
        would be text sizes, line thicknesses and line
        pitch.
        Same as rScaleMM if working projection not defined
        """
        ret_val = self._wrapper.scale_pj_mm()
        return ret_val




    def scale_ymm(self):
        """
        Get the vertical scale in Y units/mm

        **Note:**

        The scale factor is intended to be used by methods
        that would like to specify sizes in mm.  Examples
        would be text sizes, line thicknesses and line
        pitch.
        """
        ret_val = self._wrapper.scale_ymm()
        return ret_val




    def scale_all_group(self, xs, ys):
        """
        Scale all groups (except for GRID) in a view

        **Note:**

        X (and Y) scale is the ratio of the new dimension over
        the old dimension of a reference object. For example, if a horizontal
        straight line of 10m long becomes 20m, X scale should be 2.
        
        The view is then scaled back so that the view occupies the same
        area size as before.  The view's clip area is updated as well.
        """
        self._wrapper.scale_all_group(xs, ys)
        




    def scale_window(self, min_x, min_y, max_x, max_y, bot_x, bot_y, x_scal, y_scal):
        """
        Assign view coordinates to define a window.

        **Note:**

        The provided coordinates are converted to map mm
        using the current view translation and scaling.
        SetWindow is effectively called.

        .. seealso::

            `set_window <geosoft.gxapi.GXMVIEW.set_window>`, `scale_window <geosoft.gxapi.GXMVIEW.scale_window>`, `tran_scale <geosoft.gxapi.GXMVIEW.tran_scale>`
        """
        self._wrapper.scale_window(min_x, min_y, max_x, max_y, bot_x, bot_y, x_scal, y_scal)
        




    def set_class_name(self, cl, name):
        """
        Set a class name.

        **Note:**

        `GXMVIEW <geosoft.gxapi.GXMVIEW>` class names are intended to be used to record the
        names of certain classes in the view, such as "Plane"
        for the default drawing plane.
        """
        self._wrapper.set_class_name(cl.encode(), name.encode())
        




    def set_window(self, min_x, min_y, max_x, max_y, unit):
        """
        Set the view window

        **Note:**

        The current clip region will be set to the clip
        window.

        .. seealso::

            `fit_window <geosoft.gxapi.GXMVIEW.fit_window>`, `scale_window <geosoft.gxapi.GXMVIEW.scale_window>`, `extent <geosoft.gxapi.GXMVIEW.extent>`.
        """
        self._wrapper.set_window(min_x, min_y, max_x, max_y, unit)
        




    def tran_scale(self, x, y, xs, ys):
        """
        Set the view translation and scaling

        **Note:**

        Warning. For reasons unknown (and maybe a bug), this
        function resets the view `GXIPJ <geosoft.gxapi.GXIPJ>` units. It is a good idea
        to call the SetUnits_IPJ function after calling this
        function in order to restore them. This will be addressed
        in v6.4.
        """
        self._wrapper.tran_scale(x, y, xs, ys)
        




    def user_to_view(self, x, y):
        """
        Convert a USERplot in mm to a VIEW coordinate

        .. seealso::

            `set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`
            `get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>`
        """
        x.value, y.value = self._wrapper.user_to_view(x.value, y.value)
        




    def view_to_user(self, x, y):
        """
        Convert a VIEW coordinate to a USER coordinate.

        .. seealso::

            `set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`
            `get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>`
        """
        x.value, y.value = self._wrapper.view_to_user(x.value, y.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer