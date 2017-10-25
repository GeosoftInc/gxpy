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

    A view (:class:`geosoft.gxapi.GXMVIEW` class) has a 2-D/3-D translation matrix, a map
    projection and a clip region.  A view contains any number of
    "groups", and each "group" contains one or more graphics
    elements (entities).  Different types of groups will contain
    different types of entities:

    **Note:**

    :class:`geosoft.gxapi.GXCSYMB` groups (color symbols) contain data and rules for
    presenting the data as color symbols.  See ColSymbol_MVIEW
    and the :class:`geosoft.gxapi.GXCSYMB` class.
    
    :class:`geosoft.gxapi.GXAGG` groups (aggregates) contain images.  See Aggregate_MVIEW
    and the :class:`geosoft.gxapi.GXAGG` class.
    
    PAGG groups (poly-aggregates) contain images with multiple
    frames that make up an animation.  See PolyAggregate_MVIEW
    and the PAGG class.
    
    Standard groups contain symbols, lines, polylines, and polygons.
    See StartGroup_MVIEW.
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXMVIEW`
        
        :returns: A null :class:`geosoft.gxapi.GXMVIEW`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXMVIEW` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXMVIEW`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# 3D Entity



    def box_3d(self, p2, p3, p4, p5, p6, p7):
        """
        Draw a 3D box

        **Note:**

        The Fill color is used to color the box.
        """
        self._wrapper.box_3d(p2, p3, p4, p5, p6, p7)
        




    def crc_view(self, p2, p3):
        """
        Generate an XML CRC of a View
        """
        p2.value = self._wrapper.crc_view(p2.value, p3.encode())
        




    def crc_view_group(self, p2, p3, p4):
        """
        Generate an XML CRC of a Group
        """
        p3.value = self._wrapper.crc_view_group(p2.encode(), p3.value, p4.encode())
        




    def cylinder_3d(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Draw a 3D cylinder

        **Note:**

        The Fill color is used to color the cylinder.
        The flags determine if the cylinder is open and what
        end are closed. Note that you can create cones by
        specifying a 0 radius for one of the ends.
        """
        self._wrapper.cylinder_3d(p2, p3, p4, p5, p6, p7, p8, p9, p10)
        




    def draw_object_3d(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Draw a 3D object optimized for rendering
        """
        self._wrapper.draw_object_3d(p2, p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper, p12._wrapper, p13._wrapper, p14._wrapper)
        




    def draw_surface_3d_ex(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Draw a 3D object built from triangles

        **Note:**

        Provide one normal per vertex.
        Triangles are defined by indices into the set of vertices.
        """
        self._wrapper.draw_surface_3d_ex(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11._wrapper, p12._wrapper, p13._wrapper, p14._wrapper)
        




    def draw_surface_3d_from_file(self, p2, p3):
        """
        Draw a 3D object from a surface file
        """
        self._wrapper.draw_surface_3d_from_file(p2.encode(), p3.encode())
        



    @classmethod
    def font_weight_lst(cls, p1):
        """
        Fill a :class:`geosoft.gxapi.GXLST` with the different font weights.
        """
        gxapi_cy.WrapMVIEW.font_weight_lst(GXContext._get_tls_geo(), p1._wrapper)
        




    def get_agg_file_names(self, p2, p3):
        """
        Get the names of grid files stored in an :class:`geosoft.gxapi.GXAGG`.

        **Note:**

        The group must be an :class:`geosoft.gxapi.GXAGG` group. Check this using
        iIsGroup_MVIEW(View, sGroup, :attr:`geosoft.gxapi.MVIEW_IS_AGG`).
        """
        self._wrapper.get_agg_file_names(p2.encode(), p3._wrapper)
        




    def get_meta(self, p2, p3):
        """
        Retrieves Metadata from a group
        """
        ret_val, p3.value = self._wrapper.get_meta(p2.encode(), p3.value.encode())
        return GXMETA(ret_val)




    def measure_text(self, p2, p3, p4, p5, p6):
        """
        Compute the bounding rectangle in view units of the text using the current attributes.

        **Note:**

        Area will be 0 if error occured (does not fail).
        This will return the bounding rectangle as if the text was placed at 0,0 and adjusted according to
        the current text alignment and angle set for the view. Also see notes for TextSize_MVIEW.
        """
        p3.value, p4.value, p5.value, p6.value = self._wrapper.measure_text(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        




    def point_3d(self, p2, p3, p4):
        """
        Draw a 3D point.

        **Note:**

        The Line color and line thickness will affect rendering.
        """
        self._wrapper.point_3d(p2, p3, p4)
        




    def poly_line_3d(self, p2, p3, p4):
        """
        Draw a 3D polyline.

        **Note:**

        Dummies are not allowed in the line.
        Line Color, Thickness is supported on rendering
        """
        self._wrapper.poly_line_3d(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def relocate_group(self, p2, p3, p4, p5, p6, p7):
        """
        Re-locate a group in a view.
        """
        self._wrapper.relocate_group(p2.encode(), p3, p4, p5, p6, p7)
        




    def set_meta(self, p2, p3, p4):
        """
        Update the :class:`geosoft.gxapi.GXMETA` in this group with the new meta object.
        """
        self._wrapper.set_meta(p2.encode(), p3._wrapper, p4.encode())
        




    def sphere_3d(self, p2, p3, p4, p5):
        """
        Draw a 3D sphere

        **Note:**

        The Fill color is used to color the sphere.
        """
        self._wrapper.sphere_3d(p2, p3, p4, p5)
        




    def update_met_afrom_group(self, p2, p3):
        """
        Fill the :class:`geosoft.gxapi.GXMETA` with group dataset information
        """
        self._wrapper.update_met_afrom_group(p2.encode(), p3._wrapper)
        




# 3D Plane



    def delete_plane(self, p2, p3):
        """
        Delete a plane in a view

        **Note:**

        If the groups on the plane are not deleted, they will remain in the
        3D view as "New" groups but will be unassigned to a plane.  The
        SetAllNewGroupsToPlane  function can be used to assign these groups
        to a different plane.
        """
        self._wrapper.delete_plane(p2, p3)
        




    def get_plane_clip_ply(self, p2, p3):
        """
        Get the Plane Clip Region

        **Note:**

        By default it is the View's Clip Region
        """
        self._wrapper.get_plane_clip_ply(p2, p3._wrapper)
        




    def get_plane_equation(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Get the equation of a plane
        """
        p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value = self._wrapper.get_plane_equation(p2, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value)
        




    def get_view_plane_equation(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Get the View's Plane Equation
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value = self._wrapper.get_view_plane_equation(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value)
        




    def create_plane(self, p2):
        """
        Create a 3D Plane for 2D Groups
        """
        ret_val = self._wrapper.create_plane(p2.encode())
        return ret_val




    def find_plane(self, p2):
        """
        Find a plane in a view
        """
        ret_val = self._wrapper.find_plane(p2.encode())
        return ret_val




    def get_def_plane(self, p2):
        """
        Get the default drawing plane.

        **Note:**

        2D drawing to a 3D View will always be placed on the
        default drawing plane.  If no default drawing plane
        has been set, the first valid plane in the view is
        used as the default drawing plane.
        """
        p2.value = self._wrapper.get_def_plane(p2.value.encode())
        




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
        
        :attr:`geosoft.gxapi.IPJ_ORIENT_SECTION` - Target-type sections with Z projection horizontally
        :attr:`geosoft.gxapi.IPJ_ORIENT_SECTION_NORMAL` - Like :attr:`geosoft.gxapi.IPJ_ORIENT_SECTION`, but Z projects
        perpendicular to the secton plane.
        :attr:`geosoft.gxapi.IPJ_ORIENT_SECTION_CROOKED` - Crooked sections
        :attr:`geosoft.gxapi.IPJ_ORIENT_3D` - Some Sections extracted from a voxel - e.g. VoxelToGrids,
        as the voxel can have any orientation in 3D.
        """
        ret_val = self._wrapper.is_section()
        return ret_val




    def list_plane_groups(self, p2, p3):
        """
        List all groups in a specific plane of a 3D view

        **Note:**

        The group names are placed in the list names, group
        numbers are placed in the list values.
        
        Groups are added to the end of the :class:`geosoft.gxapi.GXLST`.
        """
        self._wrapper.list_plane_groups(p2, p3._wrapper)
        




    def list_planes(self, p2):
        """
        List all planes in a 3D view

        **Note:**

        The plane names are placed in the list names, plane
        numbers are placed in the list values.
        
        Planes are added to the end of the :class:`geosoft.gxapi.GXLST`.
        """
        self._wrapper.list_planes(p2._wrapper)
        




    def set_all_groups_to_plane(self, p2):
        """
        Set all groups to be within one plane
        """
        self._wrapper.set_all_groups_to_plane(p2)
        




    def set_all_new_groups_to_plane(self, p2):
        """
        Set all groups that are not in any plane to this plane
        """
        self._wrapper.set_all_new_groups_to_plane(p2)
        




    def set_def_plane(self, p2):
        """
        Set the default drawing plane.

        **Note:**

        2D drawing to a 3D View will always be placed on the
        default drawing plane.  If no default drawing plane
        has been set, the first valid plane in the view is
        used as the default drawing plane.
        """
        self._wrapper.set_def_plane(p2.encode())
        




    def set_group_to_plane(self, p2, p3):
        """
        Set a group to a plane
        """
        self._wrapper.set_group_to_plane(p2, p3.encode())
        




    def set_h_3dn(self, p2):
        """
        Set the :class:`geosoft.gxapi.GX3DN` object for this view

        **Note:**

        To make the view a 2D view, set a :class:`geosoft.gxapi.GX3DN` of NULL.
        """
        self._wrapper.set_h_3dn(p2._wrapper)
        




    def get_3d_point_of_view(self, p2, p3, p4, p5, p6, p7):
        """
        Get 3D point of view (values are will be :attr:`geosoft.gxapi.rDUMMY` if view for 2D views)
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_3d_point_of_view(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def set_3d_point_of_view(self, p2, p3, p4, p5, p6, p7):
        """
        Set 3D point of view (no effect on 2D views)
        """
        self._wrapper.set_3d_point_of_view(p2, p3, p4, p5, p6, p7)
        




    def set_plane_clip_ply(self, p2, p3):
        """
        Set the Plane Clip Region

        **Note:**

        By default it is the View's Clip Region
        """
        self._wrapper.set_plane_clip_ply(p2, p3._wrapper)
        




    def set_plane_equation(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Set the equation of a plane

        **Note:**

        For a grid with the "Y" axis giving elevation:
        use rotations = (-90, 0, 0) for a section with azimuth 90 (E-W)
        use rotations = (-90, 0, -90) for a section with azimuth 0 (N-S)
        """
        self._wrapper.set_plane_equation(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)
        




    def set_plane_surface(self, p2, p3):
        """
        Set the surface image of a plane
        """
        self._wrapper.set_plane_surface(p2, p3.encode())
        




    def set_plane_surf_info(self, p2, p3, p4, p5, p6, p7):
        """
        Set the surface information
        """
        self._wrapper.set_plane_surf_info(p2, p3, p4, p5, p6, p7)
        




# 3D Rendering 2D



    def define_plane_3d(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Define a 2D drawing plane based on point and normal

        **Note:**

        2D rendering commands are translated to 3D commands
        based on the plane.
        """
        self._wrapper.define_plane_3d(p2, p3, p4, p5, p6, p7, p8, p9, p10)
        




    def define_viewer_axis_3d(self, p2, p3, p4, p5, p6, p7):
        """
        Define a 2D drawing plane based on the user's view that
        oriented around the vector.
        """
        self._wrapper.define_viewer_axis_3d(p2, p3, p4, p5, p6, p7)
        




    def define_viewer_plane_3d(self, p2, p3, p4):
        """
        Define a 2D drawing plane based on the user's view.

        **Note:**

        The plane is always facing the viewer. Otherwise the
        this is identical to the previous
        """
        self._wrapper.define_viewer_plane_3d(p2, p3, p4)
        




# Clipping



    def clip_poly_ex(self, p2, p3, p4, p5):
        """
        Add a polygon to the clip region.

        **Note:**

        The polygon will be added to the current clip region.
        The :class:`geosoft.gxapi.GXVV`'s cannot have any dummy elements.
        """
        self._wrapper.clip_poly_ex(p2._wrapper, p3._wrapper, p4, p5)
        




    def clip_rect_ex(self, p2, p3, p4, p5, p6, p7):
        """
        Add a rectangle to the clip region.

        **Note:**

        The rectangle will be added to the current clip region.
        """
        self._wrapper.clip_rect_ex(p2, p3, p4, p5, p6, p7)
        




    def clip_clear(self):
        """
        Remove/clear the view clip region.
        """
        self._wrapper.clip_clear()
        




    def clip_groups(self, p2):
        """
        Set the Clipping mode on/off for all groups.
        """
        self._wrapper.clip_groups(p2)
        




    def clip_marked_groups(self, p2):
        """
        Set the Clipping mode on/off for marked groups.
        """
        self._wrapper.clip_marked_groups(p2)
        




    def clip_poly(self, p2, p3, p4):
        """
        Add a polygon to the clip region.

        **Note:**

        The polygon will be added to the current clip region.
        The :class:`geosoft.gxapi.GXVV`'s cannot have any dummy elements.
        """
        self._wrapper.clip_poly(p2._wrapper, p3._wrapper, p4)
        




    def clip_rect(self, p2, p3, p4, p5, p6):
        """
        Add a rectangle to the clip region.

        **Note:**

        The rectangle will be added to the current clip region.
        """
        self._wrapper.clip_rect(p2, p3, p4, p5, p6)
        




    def delete_ext_clip_ply(self, p2):
        """
        Deletes an extended clip :class:`geosoft.gxapi.GXPLY` object used by this view.
        """
        self._wrapper.delete_ext_clip_ply(p2)
        




    def ext_clip_ply_list(self, p2):
        """
        Get the names of existing extended clip :class:`geosoft.gxapi.GXPLY` objects in this view as list.
        """
        self._wrapper.ext_clip_ply_list(p2._wrapper)
        




    def get_clip_ply(self, p2):
        """
        Get clipping polygons, in the user projection

        **Note:**

        The returned :class:`geosoft.gxapi.GXPLY` is recast into the User projection.
        For oriented views (especially sections), use
        GetPLY_MVIEW, which returns the Clip :class:`geosoft.gxapi.GXPLY` in the view's native
        projection (e.g. the one set using SetIPJ_MVIEW).
        """
        self._wrapper.get_clip_ply(p2._wrapper)
        




    def get_ext_clip_ply(self, p2, p3):
        """
        Get an extended clip :class:`geosoft.gxapi.GXPLY` object used by this view.
        """
        self._wrapper.get_ext_clip_ply(p2, p3._wrapper)
        




    def get_group_ext_clip_ply(self, p2, p3):
        """
        Gets extended clip information for group in view.
        """
        p3.value = self._wrapper.get_group_ext_clip_ply(p2.encode(), p3.value)
        




    def get_ply(self, p2):
        """
        Get clipping polygons, in the base projection

        **Note:**

        This should be used to get the clipping polygon for
        oriented views (especially sections).
        """
        self._wrapper.get_ply(p2._wrapper)
        




    def group_clip_mode(self, p2):
        """
        Set the Clipping mode on or off for new groups.

        **Note:**

        All new groups will be clipped.
        """
        self._wrapper.group_clip_mode(p2)
        




    def get_name_ext_clip_ply(self, p2, p3):
        """
        Get the name of the extended clip :class:`geosoft.gxapi.GXPLY` object in this view.
        """
        p3.value = self._wrapper.get_name_ext_clip_ply(p2, p3.value.encode())
        




    def num_ext_clip_ply(self):
        """
        Get the number of extended clip :class:`geosoft.gxapi.GXPLY` objects in this view.
        """
        ret_val = self._wrapper.num_ext_clip_ply()
        return ret_val




    def set_ext_clip_ply(self, p2, p3, p4):
        """
        Set an extended clip :class:`geosoft.gxapi.GXPLY` object used by this view.
        """
        ret_val = self._wrapper.set_ext_clip_ply(p2, p3.encode(), p4._wrapper)
        return ret_val




    def set_clip_ply(self, p2):
        """
        Set clipping region to a :class:`geosoft.gxapi.GXPLY`
        """
        self._wrapper.set_clip_ply(p2._wrapper)
        




    def set_group_ext_clip_ply(self, p2, p3):
        """
        Sets extended clip information for group in view.
        """
        self._wrapper.set_group_ext_clip_ply(p2.encode(), p3)
        




# Color


    @classmethod
    def color2_rgb(cls, p1, p2, p3, p4):
        """
        Convert to RGB values.

        **Note:**

        Color component intensities will be in the range 0-255.
        """
        p2.value, p3.value, p4.value = gxapi_cy.WrapMVIEW.color2_rgb(GXContext._get_tls_geo(), p1, p2.value, p3.value, p4.value)
        



    @classmethod
    def color_descr(cls, p1, p2):
        """
        Convert a color to a color string label

        **Note:**

        See iColor_MVIEW.
        """
        p2.value = gxapi_cy.WrapMVIEW.color_descr(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def color(cls, p1):
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
        """
        ret_val = gxapi_cy.WrapMVIEW.color(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def color_cmy(cls, p1, p2, p3):
        """
        Return CMY color.

        **Note:**

        Color component intensities must be in the range 0-255.
        """
        ret_val = gxapi_cy.WrapMVIEW.color_cmy(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val



    @classmethod
    def color_hsv(cls, p1, p2, p3):
        """
        Return HSV color.

        **Note:**

        Color component intensities must be in the range 0-255.
        """
        ret_val = gxapi_cy.WrapMVIEW.color_hsv(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val



    @classmethod
    def color_rgb(cls, p1, p2, p3):
        """
        Return RGB color.

        **Note:**

        Color component intensities must be in the range 0-255.
        """
        ret_val = gxapi_cy.WrapMVIEW.color_rgb(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val




# Drawing Attribute



    def clip_mode(self, p2):
        """
        Set the view clipping mode on or off.

        **Note:**

        Entitles that follow in this group will be clipped
        or not clipped depending on this mode.
        
        The montaj editor cannot change the clip mode of
        embedded clipped/unclipped enties that are controlled
        by this call.  Use the Group clipping functions
        instead.
        
        It is highly recommended that you use the GroupClipMode_MVIEW
        function to control clipping on a group-by-group basis, instead
        of using ClipMode_MVIEW when inside a group, as it is impossible
        to determine the  true visible extents of a group. In such cases, the
        "zoom to full map extents" command may give incorrect results.
        """
        self._wrapper.clip_mode(p2)
        




    def fill_color(self, p2):
        """
        Set the fill color.
        """
        self._wrapper.fill_color(p2)
        




    def line_color(self, p2):
        """
        Set the line color.
        """
        self._wrapper.line_color(p2)
        




    def line_smooth(self, p2):
        """
        Set the line edge smoothing.
        """
        self._wrapper.line_smooth(p2)
        




    def line_style(self, p2, p3):
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
        self._wrapper.line_style(p2, p3)
        




    def line_thick(self, p2):
        """
        Set the line thickness.
        """
        self._wrapper.line_thick(p2)
        




    def pat_angle(self, p2):
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
        angle. Using this along with PatStyle(View, :attr:`geosoft.gxapi.MVIEW_TILE_RANDOM`)
        can give a "hand-drawn" effect to geological fills.
        
        See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._wrapper.pat_angle(p2)
        




    def pat_density(self, p2):
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
        self._wrapper.pat_density(p2)
        




    def pat_number(self, p2):
        """
        Sets the pattern number

        **Note:**

        Pattern 0 is solid fill.(default)
        Set the pattern color using FillColor_MVIEW.
        
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
        self._wrapper.pat_number(p2)
        




    def pat_size(self, p2):
        """
        Sets the pattern unit cell size (X)

        **Note:**

        See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._wrapper.pat_size(p2)
        




    def pat_style(self, p2):
        """
        Sets the tiling method (i.e. rectangle, triangle)

        **Note:**

        Normally, the unit cell is duplicated across the fill area
        like floor tiles (:attr:`geosoft.gxapi.MVIEW_TILE_RECTANGULAR`).
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
        self._wrapper.pat_style(p2)
        




    def pat_thick(self, p2):
        """
        Sets the pattern line thickness

        **Note:**

        See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._wrapper.pat_thick(p2)
        




    def symb_angle(self, p2):
        """
        Set the Symb angle.
        """
        self._wrapper.symb_angle(p2)
        




    def symb_color(self, p2):
        """
        Set the Symbol color.
        """
        self._wrapper.symb_color(p2)
        




    def symb_fill_color(self, p2):
        """
        Set the Symbol color fill.
        """
        self._wrapper.symb_fill_color(p2)
        




    def symb_font(self, p2, p3, p4, p5):
        """
        Set the symbol font and style.

        **Note:**

        If the font cannot be found, the DEFAULT_SYMBOL_FONT
        specified in the [MONTAJ] section of GEOSOFT.INI
        will be used.
        
        See TextFont_MVIEW for the font name syntax.
        """
        self._wrapper.symb_font(p2.encode(), p3, p4, p5)
        




    def symb_number(self, p2):
        """
        Set the Symbol number.

        **Note:**

        The lower 16 bits of the number is interpreted as UTF-16 with a valid Unicode character
        code point. GFN fonts wil produce valid symbols depending on the font for 0x01-0x7f and the degree,
        plus-minus and diameter symbol(latin small letter o with stroke) for 0xB0, 0xB1 and 0xF8 respectively.
        
        It is possible to check if a character is valid using iIsValidUTF16Char_UNC. The high 16-bits are reserved
        for future use. Also see: iValidSymbol_UNC and ValidateSymbols_UNC.
        """
        self._wrapper.symb_number(p2)
        




    def symb_size(self, p2):
        """
        Set the Symb size.
        """
        self._wrapper.symb_size(p2)
        




    def text_angle(self, p2):
        """
        Set the text angle.
        """
        self._wrapper.text_angle(p2)
        




    def text_color(self, p2):
        """
        Set the Text color.
        """
        self._wrapper.text_color(p2)
        




    def text_font(self, p2, p3, p4, p5):
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
        on the GX API level are encoded in `UTF8` during runtime which makes it possible
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
        self._wrapper.text_font(p2.encode(), p3, p4, p5)
        




    def text_ref(self, p2):
        """
        Set the text plot reference point.
        """
        self._wrapper.text_ref(p2)
        




    def text_size(self, p2):
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
        self._wrapper.text_size(p2)
        




    def transparency(self, p2):
        """
        Sets the transparency for new objects.

        **Note:**

        1.0 Renders completely opaque objects while 0.0 will be transparent.
        Objects written after this will have a combined transparency value with the
        group transparency if it is set (e.g. 0.5 for group and 0.8 stream will result in 0.4).
        """
        self._wrapper.transparency(p2)
        




    def z_value(self, p2):
        """
        Sets Z-value info.

        **Note:**

        This number is stored in map mainly for exports to other vector formats (e.g ShapeFiles)
        A contour map that's exported to a shape file will use this value as a Z-value attributes for its shapes.
        """
        self._wrapper.z_value(p2)
        




# Drawing Entity



    def arc(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Draw an arc.
        """
        self._wrapper.arc(p2, p3, p4, p5, p6, p7, p8)
        




    def chord(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Draw a filled arc.
        """
        self._wrapper.chord(p2, p3, p4, p5, p6, p7, p8)
        




    def classified_symbols(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Plot classified symbols

        **Note:**

        For example, to plot three levels <95, 95-100 and
        100-120, three string arguments would be:
        
        "95,100,120"      maximums of each class
        "2.0,2.5,3.0"     sizes in mm
        "y,g,r"           fill colors
        """
        self._wrapper.classified_symbols(p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7.encode(), p8.encode(), p9.encode())
        




    def complex_polygon(self, p2, p3, p4):
        """
        Draw a polygon with holes in it.

        **Note:**

        You pass a :class:`geosoft.gxapi.GXVV` with polygon sizes and 2 point vvs.
        """
        self._wrapper.complex_polygon(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def ellipse(self, p2, p3, p4, p5, p6):
        """
        Draw an ellipse
        """
        self._wrapper.ellipse(p2, p3, p4, p5, p6)
        




    def line(self, p2, p3, p4, p5):
        """
        Draw a line.
        """
        self._wrapper.line(p2, p3, p4, p5)
        




    def line_vv(self, p2):
        """
        Draw line segments stored in a GS_D2LINE :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.line_vv(p2._wrapper)
        




    def polygon_dm(self, p2, p3):
        """
        Like PolyLineDm, but draw polygons.
        """
        self._wrapper.polygon_dm(p2._wrapper, p3._wrapper)
        




    def polygon_ply(self, p2):
        """
        Draw a complex polygon from :class:`geosoft.gxapi.GXPLY`.
        """
        self._wrapper.polygon_ply(p2._wrapper)
        




    def poly_line(self, p2, p3, p4):
        """
        Draw a polyline or polygon (dummies deleted).

        **Note:**

        Dummies in X and/or Y :class:`geosoft.gxapi.GXVV` are deleted and it results
        in 'solid' line. Using PolyLineDm_MVIEW (below) function
        if gaps from dummies are to be kept.
        """
        self._wrapper.poly_line(p2, p3._wrapper, p4._wrapper)
        




    def poly_line_dm(self, p2, p3):
        """
        Draw a polyline with gaps defined by dummies in X/Y VVs
        """
        self._wrapper.poly_line_dm(p2._wrapper, p3._wrapper)
        




    def poly_wrap(self, p2, p3):
        """
        Draw wrapped polylines from X and Y :class:`geosoft.gxapi.GXVV`'s.

        **Note:**

        Convert a given VVy into a wrapped VVy using
        the current view window as the wrap region.
        Then draw polylines from it.
        """
        self._wrapper.poly_wrap(p2._wrapper, p3._wrapper)
        




    def rectangle(self, p2, p3, p4, p5):
        """
        Draw a rectangle.
        """
        self._wrapper.rectangle(p2, p3, p4, p5)
        




    def segment(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Draw a filled segment of an ellipse.
        """
        self._wrapper.segment(p2, p3, p4, p5, p6, p7, p8)
        




    def size_symbols(self, p2, p3, p4):
        """
        Plot sized symbols
        """
        self._wrapper.size_symbols(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def symbol(self, p2, p3):
        """
        Plot a symbol
        """
        self._wrapper.symbol(p2, p3)
        




    def symbols(self, p2, p3):
        """
        Plot symbols
        """
        self._wrapper.symbols(p2._wrapper, p3._wrapper)
        




    def symbols_itr(self, p2, p3, p4, p5):
        """
        Plot symbols using an :class:`geosoft.gxapi.GXITR`
        """
        self._wrapper.symbols_itr(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper)
        




    def text(self, p2, p3, p4):
        """
        Draw text.
        """
        self._wrapper.text(p2.encode(), p3, p4)
        




# Drawing Object



    def aggregate(self, p2, p3):
        """
        Add an aggregate to a view.
        """
        self._wrapper.aggregate(p2._wrapper, p3.encode())
        




    def get_aggregate(self, p2):
        """
        Get an existing Aggregate object from the view.

        **Note:**

        This method returns a cached object owned by the :class:`geosoft.gxapi.GXMVIEW` and will be destroyed automatically when the :class:`geosoft.gxapi.GXMVIEW` is disposed
        """
        ret_val = self._wrapper.get_aggregate(p2)
        return GXAGG(ret_val)




    def change_line_message(self, p2):
        """
        Change the specified line in a view.

        **Note:**

        The line name can be created by calling LineLabel_DB using
        :attr:`geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINK`. This insures that the label is
        created is the same way as used in the database.
        """
        self._wrapper.change_line_message(p2.encode())
        




    def col_symbol(self, p2, p3):
        """
        Add a colored symbol object to a view.
        """
        self._wrapper.col_symbol(p2.encode(), p3._wrapper)
        




    def get_col_symbol(self, p2):
        """
        Get an existing colored symbol object from the view.

        **Note:**

        This method returns a cached object owned by the :class:`geosoft.gxapi.GXMVIEW` and will be destroyed automatically when the :class:`geosoft.gxapi.GXMVIEW` is disposed
        """
        ret_val = self._wrapper.get_col_symbol(p2)
        return GXCSYMB(ret_val)




    def datalinkd(self, p2, p3):
        """
        Add a Data Link Display (:class:`geosoft.gxapi.GXDATALINKD`) object to the view.
        """
        self._wrapper.datalinkd(p2._wrapper, p3.encode())
        




    def get_datalinkd(self, p2):
        """
        Get an existing Data Link Display (:class:`geosoft.gxapi.GXDATALINKD`) object from the view.

        **Note:**

        This method returns a cached object owned by the :class:`geosoft.gxapi.GXMVIEW` and will be destroyed automatically when the :class:`geosoft.gxapi.GXMVIEW` is disposed
        """
        ret_val = self._wrapper.get_datalinkd(p2)
        return GXDATALINKD(ret_val)




    def easy_maker(self, p2, p3):
        """
        Used for GX makers which use both maps and databases.
        """
        self._wrapper.easy_maker(p2.encode(), p3.encode())
        




    def emf_object(self, p2, p3, p4, p5, p6):
        """
        Add an EMF file data object to the view.
        """
        self._wrapper.emf_object(p2, p3, p4, p5, p6.encode())
        




    def external_string_object(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Add an external string data object to the view.
        """
        self._wrapper.external_string_object(p2, p3, p4, p5, p6.encode(), p7.encode(), p8.encode())
        




    def link(self, p2, p3):
        """
        Make a link to a database.
        """
        self._wrapper.link(p2._wrapper, p3.encode())
        




    def maker(self, p2, p3, p4, p5, p6, p7):
        """
        Generates a Maker for the database and/or map.
        """
        self._wrapper.maker(p2, p3, p4.encode(), p5, p6.encode(), p7.encode())
        




    def meta(self, p2, p3):
        """
        Store Metadata in a group
        """
        self._wrapper.meta(p2._wrapper, p3.encode())
        




    def voxd(self, p2, p3):
        """
        Add a Voxel Display (:class:`geosoft.gxapi.GXVOXD`) object to the view.
        """
        self._wrapper.voxd(p2._wrapper, p3.encode())
        




    def get_voxd(self, p2):
        """
        Get an existing :class:`geosoft.gxapi.GXVOXD` object from the view.

        **Note:**

        This method returns a cached object owned by the :class:`geosoft.gxapi.GXMVIEW` and will be destroyed automatically when the :class:`geosoft.gxapi.GXMVIEW` is disposed
        """
        ret_val = self._wrapper.get_voxd(p2)
        return GXVOXD(ret_val)




    def draw_vector_voxel_vectors(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Display vectors from a vector voxel in the view.

        **Note:**

        This will result in a :class:`geosoft.gxapi.GXVECTOR3D` group object within the view
        """
        self._wrapper.draw_vector_voxel_vectors(p2._wrapper, p3.encode(), p4._wrapper, p5, p6, p7, p8, p9)
        




    def get_vector_3d(self, p2):
        """
        Get an existing :class:`geosoft.gxapi.GXVECTOR3D` object from the view.

        **Note:**

        This method returns a cached object owned by the :class:`geosoft.gxapi.GXMVIEW` and will be destroyed automatically when the :class:`geosoft.gxapi.GXMVIEW` is disposed
        """
        ret_val = self._wrapper.get_vector_3d(p2)
        return GXVECTOR3D(ret_val)




    def draw_vectors_3d(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Display vectors in the view.
        """
        self._wrapper.draw_vectors_3d(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11, p12)
        




# Group Methods



    def set_group_itr(self, p2, p3):
        """
        Set group :class:`geosoft.gxapi.GXITR`

        **Note:**

        A group :class:`geosoft.gxapi.GXITR` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._wrapper.set_group_itr(p2, p3._wrapper)
        




    def get_group_itr(self, p2):
        """
        Get group :class:`geosoft.gxapi.GXITR`

        **Note:**

        A group :class:`geosoft.gxapi.GXITR` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._wrapper.get_group_itr(p2)
        return GXITR(ret_val)




    def group_itr_exists(self, p2):
        """
        Determine if group :class:`geosoft.gxapi.GXITR` exists.

        **Note:**

        A group :class:`geosoft.gxapi.GXITR` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._wrapper.group_itr_exists(p2)
        return ret_val




    def delete_group_itr(self, p2):
        """
        Deletes existing :class:`geosoft.gxapi.GXITR` associated with a group.

        **Note:**

        A group :class:`geosoft.gxapi.GXITR` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._wrapper.delete_group_itr(p2)
        




    def set_group_tpat(self, p2, p3):
        """
        Set group :class:`geosoft.gxapi.GXTPAT`

        **Note:**

        A group :class:`geosoft.gxapi.GXTPAT` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._wrapper.set_group_tpat(p2, p3._wrapper)
        




    def get_group_tpat(self, p2):
        """
        Get group :class:`geosoft.gxapi.GXTPAT`

        **Note:**

        A group :class:`geosoft.gxapi.GXTPAT` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._wrapper.get_group_tpat(p2)
        return GXTPAT(ret_val)




    def group_tpat_exists(self, p2):
        """
        Determine if group :class:`geosoft.gxapi.GXTPAT` exists.

        **Note:**

        A group :class:`geosoft.gxapi.GXTPAT` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._wrapper.group_tpat_exists(p2)
        return ret_val




    def delete_group_tpat(self, p2):
        """
        Deletes existing :class:`geosoft.gxapi.GXTPAT` associated with a group.

        **Note:**

        A group :class:`geosoft.gxapi.GXTPAT` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._wrapper.delete_group_tpat(p2)
        




    def group_storage_exists(self, p2, p3):
        """
        Determine if generic storage associated with a group exists.

        **Note:**

        External API users should not use storage names starting with "Geosoft"
        """
        ret_val = self._wrapper.group_storage_exists(p2, p3.encode())
        return ret_val




    def read_group_storage(self, p2, p3):
        """
        Reads existing generic storage associated with a group into an in-memory :class:`geosoft.gxapi.GXBF`.

        **Note:**

        External API users should not use storage names starting with "Geosoft"
        """
        ret_val = self._wrapper.read_group_storage(p2, p3.encode())
        return GXBF(ret_val)




    def delete_group_storage(self, p2, p3):
        """
        Deletes existing generic storage associated with a group.

        **Note:**

        External API users should not use storage names starting with "Geosoft"
        """
        self._wrapper.delete_group_storage(p2, p3.encode())
        




    def write_group_storage(self, p2, p3, p4):
        """
        Open generic existing storage associated with a group for reading.

        **Note:**

        External API users should not use storage names starting with "Geosoft"
        """
        self._wrapper.write_group_storage(p2, p3.encode(), p4._wrapper)
        




    def copy_marked_groups(self, p2):
        """
        Copies all marked groups from one view into another view

        **Note:**

        Projections in source and destination views are used to copy the
        entities. Entities are clipped by the destination view's clipping
        region.
        """
        self._wrapper.copy_marked_groups(p2._wrapper)
        




    def copy_raw_marked_groups(self, p2):
        """
        Copies all marked groups raw from one view into another

        **Note:**

        The projections, and clipping is completly ignored.
        """
        self._wrapper.copy_raw_marked_groups(p2._wrapper)
        




    def crc_group(self, p2, p3):
        """
        Compute CRC for a group.
        """
        ret_val = self._wrapper.crc_group(p2.encode(), p3)
        return ret_val




    def delete_group(self, p2):
        """
        Delete a group.

        **Note:**

        Does nothing if the group does not already exist.
        """
        self._wrapper.delete_group(p2.encode())
        




    def del_marked_groups(self):
        """
        Delete marked groups.
        """
        self._wrapper.del_marked_groups()
        




    def get_group_extent(self, p2, p3, p4, p5, p6, p7):
        """
        Get extent of a group in a view
        """
        p3.value, p4.value, p5.value, p6.value = self._wrapper.get_group_extent(p2.encode(), p3.value, p4.value, p5.value, p6.value, p7)
        




    def get_group_transparency(self, p2, p3):
        """
        Gets the transparency value of group
        """
        p3.value = self._wrapper.get_group_transparency(p2.encode(), p3.value)
        




    def group_to_ply(self, p2, p3):
        """
        Save all polygons in group into :class:`geosoft.gxapi.GXPLY` obj.

        **Note:**

        The coordinates will be in the working coordinate system
        of the view.  The SetWorkingIPJ_MVIEW method can be used
        to change the working coordinate system. This function will
        return an empty :class:`geosoft.gxapi.GXPLY` if the group is hidden.
        """
        self._wrapper.group_to_ply(p2.encode(), p3._wrapper)
        




    def hide_marked_groups(self, p2):
        """
        Hide/Show marked groups.
        """
        self._wrapper.hide_marked_groups(p2)
        




    def hide_shadow2_d_interpretations(self, p2):
        """
        Hide/Show 2d shadow interpretations.
        """
        self._wrapper.hide_shadow2_d_interpretations(p2)
        




    def exist_group(self, p2):
        """
        Checks to see if a group exists.
        """
        ret_val = self._wrapper.exist_group(p2.encode())
        return ret_val




    def gen_new_group_name(self, p2, p3):
        """
        Generate the name of a group from a base name that
        is new. (always unique and won't overwrite existing
        objects).
        """
        p3.value = self._wrapper.gen_new_group_name(p2.encode(), p3.value.encode())
        




    def is_group(self, p2, p3):
        """
        Query a status or characteristic of a group
        """
        ret_val = self._wrapper.is_group(p2.encode(), p3)
        return ret_val




    def is_group_empty(self, p2):
        """
        Is the group empty?
        """
        ret_val = self._wrapper.is_group_empty(p2.encode())
        return ret_val




    def is_movable(self):
        """
        Is this view movable?

        **Note:**

        Views are always physically movable in the API, this
        flag is for preventing accidental moving in the :class:`geosoft.gxapi.GXGUI`.
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




    def list_groups(self, p2, p3):
        """
        Get a list of the groups in a view.
        """
        ret_val = self._wrapper.list_groups(p2._wrapper, p3)
        return ret_val




    def render_order(self):
        """
        Query the view render order

        **Note:**

        Views with lower numbers should render first, :attr:`geosoft.gxapi.iDUMMY` is undefined
        """
        ret_val = self._wrapper.render_order()
        return ret_val




    def mark_all_groups(self, p2):
        """
        Mark or unmark all groups.
        """
        self._wrapper.mark_all_groups(p2)
        




    def mark_empty_groups(self, p2):
        """
        Mark/unmark all empty groups.
        """
        self._wrapper.mark_empty_groups(p2)
        




    def mark_group(self, p2, p3):
        """
        Mark or unmark a specific group
        """
        self._wrapper.mark_group(p2.encode(), p3)
        




    def move_group_backward(self, p2):
        """
        Move the group backward one position (render sooner).
        """
        self._wrapper.move_group_backward(p2.encode())
        




    def move_group_forward(self, p2):
        """
        Move the group forward one position (render later).
        """
        self._wrapper.move_group_forward(p2.encode())
        




    def move_group_to_back(self, p2):
        """
        Move the group to the back (render first).
        """
        self._wrapper.move_group_to_back(p2.encode())
        




    def move_group_to_front(self, p2):
        """
        Move the group to the front (render last).
        """
        self._wrapper.move_group_to_front(p2.encode())
        




    def rename_group(self, p2, p3):
        """
        Rename a group.

        **Note:**

        Does nothing if the group does not already exist.
        """
        self._wrapper.rename_group(p2.encode(), p3.encode())
        




    def set_group_moveable(self, p2, p3):
        """
        Set the movable attribute of a group.
        """
        self._wrapper.set_group_moveable(p2.encode(), p3)
        




    def set_group_transparency(self, p2, p3):
        """
        Sets the transparency value of group
        """
        self._wrapper.set_group_transparency(p2.encode(), p3)
        




    def set_mark_moveable(self, p2):
        """
        Set the movable attribute of marked groups.
        """
        self._wrapper.set_mark_moveable(p2)
        




    def set_movability(self, p2):
        """
        Set the view movability

        **Note:**

        Views are always physically movable in the API, this
        flag is for preventing accidental moving in the :class:`geosoft.gxapi.GXGUI`.
        By default views are not movable.
        """
        self._wrapper.set_movability(p2)
        




    def set_render_order(self, p2):
        """
        Set the view render order

        **Note:**

        Views with lower numbers should render first, :attr:`geosoft.gxapi.iDUMMY` is undefined
        """
        self._wrapper.set_render_order(p2)
        




    def set_visibility(self, p2):
        """
        Set the view visibility
        """
        self._wrapper.set_visibility(p2)
        




    def start_group(self, p2, p3):
        """
        Start a group.

        **Note:**

        Line and fill colors and thickness must be set
        before drawing to a group.
        
        If the group name is NULL, output will be sent to
        the primary group stream and the `MVIEW_GROUP` is
        ignored.
        
        Group names must be different from view names.
        """
        self._wrapper.start_group(p2.encode(), p3)
        




    def get_group_guid(self, p2, p3):
        """
        Gets a GUID of a group in the :class:`geosoft.gxapi.GXMVIEW`.

        **Note:**

        If a GUID was never queried a new one will be assigned and the map will be modified. Only if the map is saved will this value then persist.
        """
        p3.value = self._wrapper.get_group_guid(p2, p3.value.encode())
        




    def find_group_by_guid(self, p2):
        """
        Find a Group by name.
        """
        ret_val = self._wrapper.find_group_by_guid(p2.encode())
        return ret_val




# Projection



    def set_working_ipj(self, p2):
        """
        Set the working projection of the view.

        **Note:**

        The working projection is the coordinate system of coordinates drawn to
        the view.  The working coordinate system can be different than the view
        coordinate system, in which case the coordinates are re-projected to the
        view coordinate system before they are placed in the view.
        """
        self._wrapper.set_working_ipj(p2._wrapper)
        




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




    def get_ipj(self, p2):
        """
        Get the projection of the view.
        """
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_user_ipj(self, p2):
        """
        Get the user projection of the view.
        """
        self._wrapper.get_user_ipj(p2._wrapper)
        




    def mode_pj(self, p2):
        """
        Set the working projection mode

        **Note:**

        This controls how your coordinates and attributes will be interpreted.
        A working projection must be set useing SetWorkingIPJ_MVIEW for this
        method to have any effect.
        """
        self._wrapper.mode_pj(p2)
        




    def north(self):
        """
        Returns North direction at center of view.

        **Note:**

        North is calculated from the :class:`geosoft.gxapi.GXIPJ` North direction.
        It will be :attr:`geosoft.gxapi.rDUMMY` if :class:`geosoft.gxapi.GXIPJ` is unknown.
        """
        ret_val = self._wrapper.north()
        return ret_val




    def set_ipj(self, p2):
        """
        Set the projection of the view.

        **Note:**

        As of v5.1.8, this function also sets the User :class:`geosoft.gxapi.GXIPJ`,
        and automatically clears the WARP before doing so, so
        that instead of the following construction:
        
        SetIPJ_MVIEW(View,hIPJ);
        ClearWarp_IPJ(hIPJ);
        SetUserIPJ_MVIEW(View,hIPJ);
        
        you can simply use:
        
        SetIPJ_MVIEW(View,hIPJ);
        """
        self._wrapper.set_ipj(p2._wrapper)
        




    def set_user_ipj(self, p2):
        """
        Set the user projection of the view.
        """
        self._wrapper.set_user_ipj(p2._wrapper)
        




# Render



    def get_3d_group_flags(self, p2):
        """
        Get a 3D geometry group's 3D rendering flags.
        """
        ret_val = self._wrapper.get_3d_group_flags(p2)
        return ret_val




    def set_3d_group_flags(self, p2, p3):
        """
        Set a 3D geometry group's 3D rendering flags.
        """
        self._wrapper.set_3d_group_flags(p2, p3)
        




    def get_group_freeze_scale(self, p2, p3):
        """
        Get a scale freezing value for the group (:attr:`geosoft.gxapi.rDUMMY` for disabled).
        """
        p3.value = self._wrapper.get_group_freeze_scale(p2, p3.value)
        




    def set_freeze_scale(self, p2):
        """
        Set a scale freezing value into stream (:attr:`geosoft.gxapi.rDUMMY` for disabled).

        **Note:**

        Objects written after this will override any scale freezing set for the group
        """
        self._wrapper.set_freeze_scale(p2)
        




    def set_group_freeze_scale(self, p2, p3):
        """
        Set a scale freezing value for the group (:attr:`geosoft.gxapi.rDUMMY` for disabled).
        """
        self._wrapper.set_group_freeze_scale(p2, p3)
        




    def find_group(self, p2):
        """
        Find a Group by name.
        """
        ret_val = self._wrapper.find_group(p2.encode())
        return ret_val




    def group_name(self, p2, p3):
        """
        Get a group name
        """
        p3.value = self._wrapper.group_name(p2, p3.value.encode())
        




    def render(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Render a specified area of view onto a Windows DC handle
        """
        self._wrapper.render(p2, p3, p4, p5, p6, p7, p8, p9, p10)
        




# Utility Drawing



    def set_u_fac(self, p2):
        """
        Set the unit conversion of a view.
        """
        self._wrapper.set_u_fac(p2)
        




    def axis_x(self, p2, p3, p4, p5, p6, p7):
        """
        Draw an X axis

        **Note:**

        All coordinates are in view units.
        """
        self._wrapper.axis_x(p2, p3, p4, p5, p6, p7)
        




    def axis_y(self, p2, p3, p4, p5, p6, p7):
        """
        Draw a  Y axis

        **Note:**

        All coordinates are in view units.
        """
        self._wrapper.axis_y(p2, p3, p4, p5, p6, p7)
        




    def grid(self, p2, p3, p4, p5, p6):
        """
        Draw a grid in the current window

        **Note:**

        The grid will be drawn in the current window specified
        by the last SetWindow call.
        """
        self._wrapper.grid(p2, p3, p4, p5, p6)
        




    def label_fid(self, p2, p3, p4, p5, p6, p7):
        """
        Label fiducials on a profile

        **Note:**

        A 1mm long vertical tick is drawn at the place
        where a label is present. The label is drawn
        below the tick.
        
        The incoming X :class:`geosoft.gxapi.GXVV` is used to define the place for
        label.
        """
        self._wrapper.label_fid(p2._wrapper, p3, p4, p5, p6, p7)
        




    def label_x(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Label annotations on the X axis

        **Note:**

        Label bounding will justify edge labels to be inside
        the bar limits. But bounding does not apply if
        labels are drawn vertically (top right or top left)
        """
        self._wrapper.label_x(p2, p3, p4, p5, p6, p7, p8)
        




    def label_y(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Label annotations on the Y axis

        **Note:**

        Label bounding will justify edge labels to be inside
        the bar limits. But bounding does not apply if
        labels are drawn vertically (top right or top left)
        """
        self._wrapper.label_y(p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def optimum_tick(cls, p1, p2, p3):
        """
        Return a default optimum tick interval
        """
        p3.value = gxapi_cy.WrapMVIEW.optimum_tick(GXContext._get_tls_geo(), p1, p2, p3.value)
        




# View


    @classmethod
    def create(cls, p1, p2, p3):
        """
        Create :class:`geosoft.gxapi.GXMVIEW`.

        **Note:**

        View scaling is set to mm on the map and the view
        origin is set to the map origin.
        """
        ret_val = gxapi_cy.WrapMVIEW.create(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        return GXMVIEW(ret_val)



    @classmethod
    def create_crooked_section(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
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
        
        If the scale is set to :attr:`geosoft.gxapi.rDUMMY`, then it will be calculated so that
        the points will all fit horizontally.
        """
        ret_val = gxapi_cy.WrapMVIEW.create_crooked_section(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper, p13._wrapper, p14._wrapper)
        return GXMVIEW(ret_val)



    @classmethod
    def create_crooked_section_data_profile(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15):
        """
        Creates a new crooked section data profile view.

        **Note:**

        This is the same as CreateCrookedSection_MVIEW, except that the
        vertical axis plots a data value, not elevation, and allows for
        logarithmic scaling.
        
        See Also: CreateCrookedSection_MVIEW.
        """
        ret_val = gxapi_cy.WrapMVIEW.create_crooked_section_data_profile(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4, p5, p6, p7, p8, p9, p10, p11, p12, p13._wrapper, p14._wrapper, p15._wrapper)
        return GXMVIEW(ret_val)






    def extent(self, p2, p3, p4, p5, p6, p7):
        """
        Get the view extents

        **Note:**

        The CLIP region is the current view window or the limits
        of the current clip polygon.
        
        If :attr:`geosoft.gxapi.MVIEW_EXTENT_ALL` is requested and the view has no groups, the
        clip extents are returned.
        
        If clip extents are requested and there are no clip extents, an
        area 0.0,0.0 1.0,1.0 is returned.
        
        The :attr:`geosoft.gxapi.MVIEW_EXTENT_VISIBLE` flag will return the union of the :attr:`geosoft.gxapi.MVIEW_EXTENT_CLIP` area and the
        extents of all non-masked visible groups in the view.
        """
        p4.value, p5.value, p6.value, p7.value = self._wrapper.extent(p2, p3, p4.value, p5.value, p6.value, p7.value)
        




    def get_map(self):
        """
        Get the :class:`geosoft.gxapi.GXMAP` of the view.
        """
        ret_val = self._wrapper.get_map()
        return GXMAP(ret_val)




    def get_reg(self):
        """
        Get the :class:`geosoft.gxapi.GXREG` of the view.
        """
        ret_val = self._wrapper.get_reg()
        return GXREG(ret_val)




    def get_name(self, p2):
        """
        Gets the name of a view.
        """
        p2.value = self._wrapper.get_name(p2.value.encode())
        




    def get_guid(self, p2):
        """
        Gets the GUID of the :class:`geosoft.gxapi.GXMVIEW`.

        **Note:**

        If a GUID was never queried a new one will be assigned and the map will be modified. Only if the map is saved will this value then persist.
        """
        p2.value = self._wrapper.get_guid(p2.value.encode())
        




# View Control



    def plot_to_view(self, p2, p3):
        """
        Convert a plot coordinate in mm to a VIEW coordinate.
        """
        p2.value, p3.value = self._wrapper.plot_to_view(p2.value, p3.value)
        




    def set_thin_res(self, p2):
        """
        Set polyline/polygon thinning resolution

        **Note:**

        The thinning resolution controls the removal of
        redundant points from polylines and polygons.  Points
        that deviate from a straight line by less than the
        thinning resolution are removed.  This can significantly
        reduce the size of a :class:`geosoft.gxapi.GXMAP` file.
        We recommend that you set the thinning resolution to
        0.02 mm.
        
        By default, the thinning resolution is set to 0.05mm.
        
        Set resolution to 0.0 to remove colinear points only.
        
        To turn off thinning after turning it on, call
        SetThinRes_MVIEW with a resolution of -1.
        """
        self._wrapper.set_thin_res(p2)
        




    def view_to_plot(self, p2, p3):
        """
        Convert a VIEW coordinate to a plot coordinate in mm.
        """
        p2.value, p3.value = self._wrapper.view_to_plot(p2.value, p3.value)
        




    def best_fit_window(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Fit an area in ground coordinates centered to an area in mm on map or vise versa
        keeping X and Y scales the same.

        **Note:**

        X and Y scales will be redefined and units will remain unchanged.
        The final X and Y ranges (if changed) are returned.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value = self._wrapper.best_fit_window(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10)
        




    def fit_map_window_3d(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Set the 2D view window for a 3D view.

        **Note:**

        3D views are placed in 2D maps within a 2D mapping window
        that is analgous to a 2D View.  This allows all 2D functions
        (such as changing a view location and size) to treat a 3D
        view just like a 2D view.
        
        The FitMapWindow3D_MVIEW function allows you to
        locate and set the "apparent" 2D mapping of a 3D view on
        the map. An intial map window is established
        as specified on the map, and the view scaling is
        established to fit the specified area within that
        map area.
        """
        self._wrapper.fit_map_window_3d(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def fit_window(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Fit an area in ground coordinates to an area in mm on map.

        **Note:**

        X and Y scales will be redefined and the units will be set to <unknown>.
        Coordinate ranges must be greater than 0.0.
        """
        self._wrapper.fit_window(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def get_class_name(self, p2, p3):
        """
        Get a class name.

        **Note:**

        :class:`geosoft.gxapi.GXMVIEW` class names are intended to be used to record the
        names of certain classes in the view, such as "Plane"
        for the default drawing plane.
        """
        p3.value = self._wrapper.get_class_name(p2.encode(), p3.value.encode())
        




    def map_origin(self, p2, p3):
        """
        Get the map origin from a view
        """
        p2.value, p3.value = self._wrapper.map_origin(p2.value, p3.value)
        




    def re_scale(self, p2):
        """
        Change the scale of a view.

        **Note:**

        The view size is multiplied by the scale factor.
        The view location will move relative to the map origin
        by the scale factor.
        """
        self._wrapper.re_scale(p2)
        




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




    def scale_all_group(self, p2, p3):
        """
        Scale all groups (except for GRID) in a view

        **Note:**

        X (and Y) scale is the ratio of the new dimension over
        the old dimension of a reference object. For example, if a horizontal
        straight line of 10m long becomes 20m, X scale should be 2.
        
        The view is then scaled back so that the view occupies the same
        area size as before.  The view's clip area is updated as well.
        """
        self._wrapper.scale_all_group(p2, p3)
        




    def scale_window(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Assign view coordinates to define a window.

        **Note:**

        The provided coordinates are converted to map mm
        using the current view translation and scaling.
        SetWindow is effectively called.
        """
        self._wrapper.scale_window(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def set_class_name(self, p2, p3):
        """
        Set a class name.

        **Note:**

        :class:`geosoft.gxapi.GXMVIEW` class names are intended to be used to record the
        names of certain classes in the view, such as "Plane"
        for the default drawing plane.
        """
        self._wrapper.set_class_name(p2.encode(), p3.encode())
        




    def set_window(self, p2, p3, p4, p5, p6):
        """
        Set the view window

        **Note:**

        The current clip region will be set to the clip
        window.
        """
        self._wrapper.set_window(p2, p3, p4, p5, p6)
        




    def tran_scale(self, p2, p3, p4, p5):
        """
        Set the view translation and scaling

        **Note:**

        Warning. For reasons unknown (and maybe a bug), this
        function resets the view :class:`geosoft.gxapi.GXIPJ` units. It is a good idea
        to call the SetUnits_IPJ function after calling this
        function in order to restore them. This will be addressed
        in v6.4.
        """
        self._wrapper.tran_scale(p2, p3, p4, p5)
        




    def user_to_view(self, p2, p3):
        """
        Convert a USERplot in mm to a VIEW coordinate
        """
        p2.value, p3.value = self._wrapper.user_to_view(p2.value, p3.value)
        




    def view_to_user(self, p2, p3):
        """
        Convert a VIEW coordinate to a USER coordinate.
        """
        p2.value, p3.value = self._wrapper.view_to_user(p2.value, p3.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer