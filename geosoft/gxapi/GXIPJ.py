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
class GXIPJ:
    """
    GXIPJ class.

    The `GXIPJ` class describes a single spatial reference in the world,
    defined under a coordinate system, an orientation,
    and a warp (which can be used to distort the projected object
    to a particular shape or boundary).

    **Note:**

    `GXIPJ` objects may be attached to channels or views. Two IPJs taken
    together are used to create a `GXPJ` object, which allows for the
    conversion of positions from one projection to the other.
    See also the `GXLL2` class, which creates Datum correction lookups.
    
    See also          `GXPJ`    Converts coordinates between projections
    `GXLL2`   Creates Datum correction lookups.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIPJ(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIPJ`
        
        :returns: A null `GXIPJ`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXIPJ` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXIPJ`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear_warp(self):
        """
        Clear warp parameters (if any) from an `GXIPJ`.
        """
        self._wrapper.clear_warp()
        




    def make_geographic(self):
        """
        Remove a projected coordinate system from an `GXIPJ`

        **Note:**

        This function does nothing if the `GXIPJ` is not a projected coordinate system.
        """
        self._wrapper.make_geographic()
        




    def make_wgs84(self):
        """
        Make a WGS 84 geographic projection
        """
        self._wrapper.make_wgs84()
        




    def set_units(self, scale, str_val):
        """
        Set unit parameters
        """
        self._wrapper.set_units(scale, str_val.encode())
        




    def add_exagg_warp(self, x_exag, y_exag, z_exag, x_orig, y_orig, z_orig):
        """
        Add a warp to `GXIPJ` to exaggerate X, Y and Z.
        """
        self._wrapper.add_exagg_warp(x_exag, y_exag, z_exag, x_orig, y_orig, z_orig)
        




    def add_log_warp(self, x, y):
        """
        Add a warp to `GXIPJ` to log one or both coordinantes
        """
        self._wrapper.add_log_warp(x, y)
        




    def add_matrix_warp(self, v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33):
        """
        Add a warp to `GXIPJ` using a matrix
        """
        self._wrapper.add_matrix_warp(v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33)
        




    def add_warp(self, type, vv_x_old, vv_y_old, vv_x_new, vv_y_new):
        """
        Add a warp to `GXIPJ`.

        **Note:**

        There must be at least "warp type" points in the
        warp point `GXVV`'s.
        All point `GXVV`'s must have the same number of points.
        If there are more points than required by the warp,
        the warp will be determined by least-square fitting
        to the warp surface for all but the 4-point warp.
        The 4-point ward requires exactly 4 points.
        
        Cannot be used with WARP_MATRIX or WARP_LOG
        """
        self._wrapper.add_warp(type, vv_x_old._wrapper, vv_y_old._wrapper, vv_x_new._wrapper, vv_y_new._wrapper)
        




    def clear_coordinate_system(self):
        """
        Clear coordinate sytsem, except for units

        **Note:**

        Clears the Datum, Local Datum and Projection info.
        Leaves units, any warp or orientation warp unchanged.
        """
        self._wrapper.clear_coordinate_system()
        




    def clear_orientation(self):
        """
        Clear an orientation warp from an `GXIPJ`.
        """
        self._wrapper.clear_orientation()
        




    def convert_orientation_warp_vv(self, vv_x, vv_y, vv_z, f_forward):
        """
        Convert X,Y and Z VVs using the orientation warp from an `GXIPJ`.
        """
        self._wrapper.convert_orientation_warp_vv(vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, f_forward)
        




    def copy(self, ip_jd):
        """
        Copy IPJs
        """
        self._wrapper.copy(ip_jd._wrapper)
        




    def copy_projection(self, ip_jd):
        """
        Copy the projection from one `GXIPJ` to another

        **Note:**

        Copies the projection parameters, while leaving the rest
        (e.g. Datum, Local Datum Transform) unchanged.
        """
        self._wrapper.copy_projection(ip_jd._wrapper)
        



    @classmethod
    def create(cls):
        """
        This method creates a projection object.
        """
        ret_val = gxapi_cy.WrapIPJ.create(GXContext._get_tls_geo())
        return GXIPJ(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create `GXIPJ` from serialized source.
        """
        ret_val = gxapi_cy.WrapIPJ.create_s(GXContext._get_tls_geo(), bf._wrapper)
        return GXIPJ(ret_val)



    @classmethod
    def create_xml(cls, file):
        """
        Create an `GXIPJ` from serialized Geosoft MetaData XML file
        """
        ret_val = gxapi_cy.WrapIPJ.create_xml(GXContext._get_tls_geo(), file.encode())
        return GXIPJ(ret_val)






    def get_3d_view(self, x, y, z, rx, ry, rz, sx, sy, str_val):
        """
        Get 3D orientation parameters

        **Note:**

        The view must have a 3D orientation
        """
        x.value, y.value, z.value, rx.value, ry.value, rz.value, sx.value, sy.value, str_val.value = self._wrapper.get_3d_view(x.value, y.value, z.value, rx.value, ry.value, rz.value, sx.value, sy.value, str_val.value)
        




    def get_3d_view_ex(self, x, y, z, rx, ry, rz, sx, sy, str_val, rotate, flags):
        """
        Get 3D orientation parameters with new flags

        **Note:**

        The view must have a 3D orientation
        """
        x.value, y.value, z.value, rx.value, ry.value, rz.value, sx.value, sy.value, str_val.value, rotate.value, flags.value = self._wrapper.get_3d_view_ex(x.value, y.value, z.value, rx.value, ry.value, rz.value, sx.value, sy.value, str_val.value, rotate.value, flags.value)
        




    def get_crooked_section_view_v_vs(self, dist_vv, xvv, yvv, log_z):
        """
        Get the crooked section path.

        **Note:**

        Returns the orignal VVs used to set up the crooked section path.
        """
        log_z.value = self._wrapper.get_crooked_section_view_v_vs(dist_vv._wrapper, xvv._wrapper, yvv._wrapper, log_z.value)
        



    @classmethod
    def get_list(cls, parm, datum, lst):
        """
        Get a list of parameters.

        **Note:**

        The datum filter string, if specified, will limit the requested
        list to those valid for the spacified datum.
        """
        gxapi_cy.WrapIPJ.get_list(GXContext._get_tls_geo(), parm, datum.encode(), lst._wrapper)
        




    def get_orientation_info(self, x, y, z, az, swing):
        """
        Get `GXIPJ` orientation parameters.

        **Note:**

        IPJ_ORIENT_TYPE:
        `IPJ_ORIENT_DEFAULT` - no special orientation - plan view.
        This is equivalent to `IPJ_ORIENT_PLAN` with
        dXo = dYo = dZo = dRotation = 0.0.
        
        `IPJ_ORIENT_PLAN`      Azimuth = Rotation CCW degrees
        The plan differs from the default view in that
        a reference level is set, and the axes can be
        rotated and offset from the local X,Y.
        
        `IPJ_ORIENT_SECTION`   Azimuth - CW degrees from North
        -360 <= azimuth <= 360
        Swing - degrees bottom towards viewer
        -90 < swing < 90
        The section view projects all plotted objects
        HORIZONTALLY onto the viewing plan in order to
        preserve elevations, even if the section has a swing.
        """
        x.value, y.value, z.value, az.value, swing.value = self._wrapper.get_orientation_info(x.value, y.value, z.value, az.value, swing.value)
        




    def get_plane_equation(self, min_x, min_y, max_x, max_y, pitch, yaw, roll, x, y, z, sx, sy, str_val):
        """
        Get the equation of a plane

        **Note:**

        Two opposite corners of the plane are required.
        Because the origin of the plane does not necessarily
        have a stable back-projection into true 3d coordinates.
        In practice, use the current view extents, or the corners
        of a grid.
        """
        pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value = self._wrapper.get_plane_equation(min_x, min_y, max_x, max_y, pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value)
        




    def get_plane_equation2(self, ip_jo, min_x, min_y, max_x, max_y, pitch, yaw, roll, x, y, z, sx, sy, str_val):
        """
        Get the equation of a plane with reprojection.

        **Note:**

        This is the same as `get_plane_equation`, but the
        input projected coordinate system (PCS) may
        be different from that of the `GXIPJ` you want the
        plane equation values described in. This may be
        required, for instance, when a 3D view has been created
        in one PCS, and an oriented grid from a different PCS is
        to be displayed in that view.
        
        If the two input IPJs share the same PCS then the `get_plane_equation`
        function is called directly, using the input `GXIPJ`.
        """
        pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value = self._wrapper.get_plane_equation2(ip_jo._wrapper, min_x, min_y, max_x, max_y, pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value)
        




    def compare_datums(self, ipj2):
        """
        Compare the datums of two coordinate systems?

        **Note:**

        To transform between different datums requires the use of a local
        datum transform.  The local datum transform can be defined when
        a coordinate system is created, but the definition is optional.
        This function will test that the local datum transforms are defined.
        Note that a coordinate transformation between datums without a
        local datum transform is still possible, but only the effect of
        ellipsoid shape will be modelled in the transform.
        """
        ret_val = self._wrapper.compare_datums(ipj2._wrapper)
        return ret_val




    def convert_warp(self, x, y, z, f_forward):
        """
        Converts a point X, Y, Z to the new `GXIPJ` plane.
        """
        ret_val, x.value, y.value, z.value = self._wrapper.convert_warp(x.value, y.value, z.value, f_forward)
        return ret_val




    def convert_warp_vv(self, vv_x, vv_y, f_forward):
        """
        Converts a set of X & Y VVs to the new `GXIPJ` plane. The Z is assumed to be 0
        """
        ret_val = self._wrapper.convert_warp_vv(vv_x._wrapper, vv_y._wrapper, f_forward)
        return ret_val




    def coordinate_systems_are_the_same(self, ipj2):
        """
        Are these two coordinate systems the same?

        **Note:**

        This does not compare LDT information (use `compare_datums` for that).
        """
        ret_val = self._wrapper.coordinate_systems_are_the_same(ipj2._wrapper)
        return ret_val




    def coordinate_systems_are_the_same_within_a_small_tolerance(self, ipj2):
        """
        Same as `coordinate_systems_are_the_same`, but allows for small numerical differences
        """
        ret_val = self._wrapper.coordinate_systems_are_the_same_within_a_small_tolerance(ipj2._wrapper)
        return ret_val




    def get_display_name(self, str_val):
        """
        Get a name for display purposes from `GXIPJ`
        """
        str_val.value = self._wrapper.get_display_name(str_val.value.encode())
        




    def get_esri(self, esri):
        """
        Store coordinate system in an ESRI prj coordinate string

        **Note:**

        If the projection is not supported in ESRI, the projection
        string will be empty.
        """
        esri.value = self._wrapper.get_esri(esri.value.encode())
        




    def get_gxf(self, str1, str2, str3, str4, str5):
        """
        Store coordinate system in GXF style strings.

        **Note:**

        See GXF revision 3 for string descriptions
        All strings must be the same length, 160 (`STR_GXF`) recommended.
        Strings too short will be truncated.
        """
        str1.value, str2.value, str3.value, str4.value, str5.value = self._wrapper.get_gxf(str1.value.encode(), str2.value.encode(), str3.value.encode(), str4.value.encode(), str5.value.encode())
        




    def get_mi_coord_sys(self, coord, units):
        """
        Store coordinate system in MapInfo coordsys pair
        """
        coord.value, units.value = self._wrapper.get_mi_coord_sys(coord.value.encode(), units.value.encode())
        




    def get_name(self, type, str_val):
        """
        Get an `GXIPJ` name
        """
        str_val.value = self._wrapper.get_name(type, str_val.value.encode())
        




    def set_vcs(self, str_val):
        """
        Set the Vertical Coordinate System in the `GXIPJ` name string

        **Note:**

        The vertical coordinate system (vcs) describes the datum used for vertical coordinates. The vcs name, if
        known, will appear in square brackets as part of the coordinate system name.
        
        Examples:
        
        ::
        
            "WGS 84 [geoid]"
            "WGS 84 / UTM zone 12S" - the vcs is not known.
            "WGS 84 / UTM zone 12S [NAVD88]"
        
        Valid inputs:
        
             "NAVD88"          - Clears existing vcs, if any, and sets the VCS name to "NAVD88".
             ""                - Clears the vcs
        """
        self._wrapper.set_vcs(str_val.encode())
        




    def get_orientation(self):
        """
        Get `GXIPJ` orientation in space.

        **Note:**

        Projections can be created oriented horizontally (e.g. in plan maps)
        or vertically (in section maps - Wholeplot and `GXIP`).
        """
        ret_val = self._wrapper.get_orientation()
        return ret_val




    def get_orientation_name(self, str_val):
        """
        Get a name for display purposes from `GXIPJ`
        """
        str_val.value = self._wrapper.get_orientation_name(str_val.value.encode())
        




    def get_units(self, scale, str_val):
        """
        Get unit parameters
        """
        scale.value, str_val.value = self._wrapper.get_units(scale.value, str_val.value.encode())
        




    def get_xml(self, str_val):
        """
        Get an Geosoft Metadata XML string from an `GXIPJ`
        """
        str_val.value = self._wrapper.get_xml(str_val.value.encode())
        




    def has_projection(self):
        """
        Does the `GXIPJ` object contain a projection?
        """
        ret_val = self._wrapper.has_projection()
        return ret_val




    def is_3d_inverted(self):
        """
        Is this 3D View inverted ?
        """
        ret_val = self._wrapper.is_3d_inverted()
        return ret_val




    def is_3d_inverted_angles(self):
        """
        Are the angles in this 3D View inverted ?
        """
        ret_val = self._wrapper.is_3d_inverted_angles()
        return ret_val




    def is_geographic(self):
        """
        See if this projection is geographic
        """
        ret_val = self._wrapper.is_geographic()
        return ret_val




    def orientations_are_the_same(self, ipj2):
        """
        Are these two orientations the same?
        """
        ret_val = self._wrapper.orientations_are_the_same(ipj2._wrapper)
        return ret_val




    def orientations_are_the_same_within_a_small_tolerance(self, ipj2):
        """
        Same as `orientations_are_the_same`, but allows for small numerical differences
        """
        ret_val = self._wrapper.orientations_are_the_same_within_a_small_tolerance(ipj2._wrapper)
        return ret_val




    def has_section_orientation(self):
        """
        Does this projection contain an orientation used by section plots?

        **Note:**

        Returns     1 if there is a section orientation
        
        The following orientations can be used to orient sections or section views:
        
        `IPJ_ORIENT_SECTION` - Target-type sections with Z projection horizontally
        `IPJ_ORIENT_SECTION_NORMAL` - Like `IPJ_ORIENT_SECTION`, but Z projects
        perpendicular to the secton plane.
        `IPJ_ORIENT_SECTION_CROOKED` - Crooked sections
        `IPJ_ORIENT_3D` - Some Sections extracted from a voxel - e.g. VoxelToGrids,
        as the voxel can have any orientation in 3D.
        
        It is sometimes important to ignore the section orientation, for instance
        when rendering a grid in 3D where it has been located on a plane.
        """
        ret_val = self._wrapper.has_section_orientation()
        return ret_val




    def projection_type_is_fully_supported(self):
        """
        Is the projection type fully supported?

        **Note:**

        This function checks only the projected coordinated system
        in the `GXIPJ` object, so should only be used with projections
        of type `IPJ_TYPE_PCS`.
        This function does not test the validity of datums or local
        datum transforms.
        """
        ret_val = self._wrapper.projection_type_is_fully_supported()
        return ret_val




    def set_gxf_safe(self, str1, str2, str3, str4, str5):
        """
        Same as `set_gxf`, but fails gracefully.

        **Note:**

        `set_gxf` will fail and terminate the GX if anything goes wrong (e.g. having a wrong
        parameter). If this function fails, it simply returns 0 and leaves the
        `GXIPJ` unchanged.
        """
        ret_val = self._wrapper.set_gxf_safe(str1.encode(), str2.encode(), str3.encode(), str4.encode(), str5.encode())
        return ret_val




    def source_type(self):
        """
        Get `GXIPJ` source type
        """
        ret_val = self._wrapper.source_type()
        return ret_val




    def support_datum_transform(self, ipj2):
        """
        Can we transform between these two datums?

        **Note:**

        To transform between different datums requires the use of a local
        datum transform.  The local datum transform can be defined when
        a coordinate system is created, but the definition is optional.
        This function will test that the local datum transforms are defined.
        Note that a coordinate transformation between datums without a
        local datum transform is still possible, but only the effect of
        ellipsoid shape will be modelled in the transform.
        """
        ret_val = self._wrapper.support_datum_transform(ipj2._wrapper)
        return ret_val



    @classmethod
    def unit_name(cls, val, type, name):
        """
        Get a unit name given a scale factor
        """
        name.value = gxapi_cy.WrapIPJ.unit_name(GXContext._get_tls_geo(), val, type, name.value.encode())
        




    def warped(self):
        """
        Does `GXIPJ` contain a warp?
        """
        ret_val = self._wrapper.warped()
        return ret_val




    def warps_are_the_same(self, ipj2):
        """
        Are these two warps the same?
        """
        ret_val = self._wrapper.warps_are_the_same(ipj2._wrapper)
        return ret_val




    def warps_are_the_same_within_a_small_tolerance(self, ipj2):
        """
        Same as `warps_are_the_same`, but allows for small numerical differences
        """
        ret_val = self._wrapper.warps_are_the_same_within_a_small_tolerance(ipj2._wrapper)
        return ret_val




    def warp_type(self):
        """
        Obtain the warp type of an `GXIPJ`.
        """
        ret_val = self._wrapper.warp_type()
        return ret_val




    def make_projected(self, min_lon, min_lat, max_lon, max_lat):
        """
        Create a default projected coordinate system from lat-long ranges.

        **Note:**

        Terminates with invalid or unsupported ranges.
        If the map crosses the equator, or if map is within 20 degrees of the
        equator, uses an equatorial mercator projection centered at the central
        longitude. Otherwise, uses a Lambert Conic Conformal (1SP) projection
        for the map. Global maps outside of +/- 70 degrees latitude are not
        supported.
        """
        self._wrapper.make_projected(min_lon, min_lat, max_lon, max_lat)
        




    def new_box_resolution(self, ip_jo, res, min_x, min_y, max_x, max_y, min_res, max_res, diag_res):
        """
        Determine a data resolution in a new coordinate system

        **Note:**

        if there are any problems reprojecting, new resolutions will
        dummy.  The conversion to new resolution is based on measurements
        along the four edges and two diagonals.
        """
        min_res.value, max_res.value, diag_res.value = self._wrapper.new_box_resolution(ip_jo._wrapper, res, min_x, min_y, max_x, max_y, min_res.value, max_res.value, diag_res.value)
        




    def read(self, type, str1, str2, str3):
        """
        Read and define an `GXIPJ` from a standard file.
        """
        self._wrapper.read(type, str1.encode(), str2.encode(), str3.encode())
        




    def get_method_parm(self, parm):
        """
        Get projection method parameter
        """
        ret_val = self._wrapper.get_method_parm(parm)
        return ret_val




    def get_north_azimuth(self, x, y):
        """
        Return the azimuth of geographic North at a point.

        **Note:**

        If the `GXIPJ` is not a projected coordinate system
        then the returned azimuth is `GS_R8DM`;
        """
        ret_val = self._wrapper.get_north_azimuth(x, y)
        return ret_val



    @classmethod
    def unit_scale(cls, name, default):
        """
        Get a unit scale (m/unit) given a name

        **Note:**

        If name cannot be found, returns default.
        """
        ret_val = gxapi_cy.WrapIPJ.unit_scale(GXContext._get_tls_geo(), name.encode(), default)
        return ret_val




    def serial(self, bf):
        """
        Serialize `GXIPJ` to a `GXBF`.
        """
        self._wrapper.serial(bf._wrapper)
        




    def serial_fgdcxml(self, file):
        """
        Write the `GXIPJ` as a FDGC MetaData XML object
        """
        self._wrapper.serial_fgdcxml(file.encode())
        




    def serial_isoxml(self, file):
        """
        Write the `GXIPJ` as a ISO MetaData XML object
        """
        self._wrapper.serial_isoxml(file.encode())
        




    def serial_xml(self, file):
        """
        Write the `GXIPJ` as a Geosoft MetaData XML object
        """
        self._wrapper.serial_xml(file.encode())
        




    def set_3d_inverted(self, inverted):
        """
        Set whether a view is inverted (must be 3D already)
        """
        self._wrapper.set_3d_inverted(inverted)
        




    def set_3d_inverted_angles(self, inverted):
        """
        Set whether the angles in this view are inverted (must be 3D already)
        """
        self._wrapper.set_3d_inverted_angles(inverted)
        




    def set_3d_view(self, x, y, z, rx, ry, rz, sx, sy, str_val):
        """
        Set 3D orientation parameters

        **Note:**

        Sets up translation, scaling and rotation in all three directions
        for 3D objects.
        """
        self._wrapper.set_3d_view(x, y, z, rx, ry, rz, sx, sy, str_val)
        




    def set_3d_view_ex(self, x, y, z, rx, ry, rz, sx, sy, str_val, rotate, flags):
        """
        Set 3D orientation parameters with new flags

        **Note:**

        Sets up translation, scaling and rotation in all three directions
        for 3D objects.
        """
        self._wrapper.set_3d_view_ex(x, y, z, rx, ry, rz, sx, sy, str_val, rotate, flags)
        




    def set_3d_view_from_axes(self, x, y, z, x1, x2, x3, y1, y2, y3, sx, sy, str_val):
        """
        Set 3D orientation parameters

        **Note:**

        Sets up translation, scaling and rotation in all three directions
        for 3D objects, based on input origin and X and Y axis vectors.
        """
        self._wrapper.set_3d_view_from_axes(x, y, z, x1, x2, x3, y1, y2, y3, sx, sy, str_val)
        




    def set_crooked_section_view(self, dist_vv, xvv, yvv, log_z):
        """
        Set up the crooked section view.

        **Note:**

        A non-plane section. It is a vertical section which curves along a path in
        (X, Y).
        """
        self._wrapper.set_crooked_section_view(dist_vv._wrapper, xvv._wrapper, yvv._wrapper, log_z)
        




    def set_depth_section_view(self, depth):
        """
        Set depth section orientation parameters
        """
        self._wrapper.set_depth_section_view(depth)
        




    def set_esri(self, esri):
        """
        Set coordinate system from an ESRI prj coordinate string

        **Note:**

        If the projection is not supported in Geosoft, the
        `GXIPJ` will be unknown.
        """
        self._wrapper.set_esri(esri.encode())
        




    def set_gxf(self, str1, str2, str3, str4, str5):
        """
        Set coordinate system from GXF style strings.

        **Note:**

        Simplest Usage:
        
        The coordinate system can be resolved from the "coordinate system name"
        if the name is specified using an EPSG number or naming convention such as:
        
        "datum / projection"  (example: "Arc 1960 / UTM zone 37S")
        
        Where:
        "datum" is the EPSG datum name (eg. NAD83).  All supported datums are
        listed in ...usercsvdatum.csv.
        "projection" is the EPSG coordinate system map projection.
        datum name (eg. "UTM zone 10N").  All supported coordinate
        system projections are listed in ...user/csv/transform.csv.
        All EPSG known combined coordinate systems of the earth are
        listed in ...user/csv/ipj_pcs.csv.
        
        To define a geographic (longitude, latitude) oordinate system, specify
        the datum name alone (ie "Arc 1960").  EPSG numbers can also be used, so in
        the example above the name can be "21037".
        
        The coordinate system may also be oriented arbitrarily in 3D relative to
        the base coordinate system by specifying the orientation as a set of
        6 comma-separated values between angled brackets after the coordinate 
        system name, e.g:
        
        ::
        
             "datum / projection"<oX,oY,oZ,rX,rY,rZ>
             21037<oX,oY,oZ,rX,rY,rZ>
        
        where:
        
        oX,oY,oZ    is the location of the local origin on the CS
        
        rX,rY,rZ    are rotations in degrees azimuth (clockwise) of
                    the local axis frame around the X, Y and Z axis
                    respectively.  A simple plane rotation will only have
                    a rotation around Z.  
        
        For example:
        
        ::
        
             "Arc 1960 / UTM zone 37S"<525000,2500000,0,0,0,15>
        
        defines a local system with origin at (525000,2500000)
        with a rotation of 15 degrees azimuth.
        
        Orientation parameters not defined will default to align with the
        base CS,  Note that although allowed, it does not make sense to have
        an orientation on a geographic coordinate system (long,lat).
        
        Complete usage:
        
        A coordinate system can also be fully described by providing an additional
        four strings that define the datum, map projection, length units and
        prefered local datum transform.  Refer to GXF revision 3 for further detail:
        http://www.geosoft.com/resources/goto/GXF-Grid-eXchange-File
        
        Note that coordinate system reference tables sre maintained in csv files
        located in the .../user/csv folder found with the Geosoft installation files,
        which will usually be located here:
        C:\\Program Files (x86)\\Geosoft\\Oasis montaj\\user\\csv
        
        The "datum" string can use a datum name defined in the "datum.csv" file,
        or the local datum name from datumtrf.csv, or the local datum description
        from ldatum.csv.
        For a non-EPSG datum, you can define your own datum parameters in the
        Datum stringfield as follows:
        
        ::
        
             "*YourDatumName",major_axis,flattening(or eccentricity)[,prime_meridian]
        
        where
        The * before "YourDatumName" indicates this is a non-EPSG name.
        major_axis is in metres.
        flattening less than 0 is interpreted as eccentricity (0 indicates a sphere).
        prime_meridian is optional, specified in degrees of longitude relative to
        Greenwich.
        
        The "Projection" can contain a projection system defined in the
        "transform.csv" file, or the name of a projection type followed by projection
        parameters.  Geographic coordinates systems (long/lat only) must leave
        "projection" blank.
        
        Projection names not defined in "transform.csv" can be defined in the
        "projection" string as follows:
        
        ::
        
             method,length_units,P1,P2,...
        
        where:
        
            method
                 is a method from the table "transform_parameters.csv".
        
            length_units
                 is a "Unit_length" from units.csv.
                 P1 through P8 (or fewer) are the projection parameters for the method
                 as defined in "transform_parameters.csv", and in the order defined.
                 Parameters that are blank in "transform_parameters.csv" are omitted
                 from the list so that each method will have a minimum list of
                 parameters.
        
        Angular parameters must always be degrees, and may be defined a
        decimal degree fromat, or "DEG.MM.SS.ssss".
        Distance parameters (False Northing and False Easting) must be
        defined in the "length_units" (string 4).
        
        Examples:
        
        ::
        
            Geographic long,lat on datum "Arc 1960":
            "4210","","","",""
            "Arc 1960","","","",""
            "","Arc 1960","","",""
        
            Projected Coordinate System, UTM zone 37S
            "21037","","","",""
            "","4210","16137","",""
            ""Arc 1960 / UTM zone 37S"","","","",""
            "",""Arc 1960"","UTM zone 37S","",""
            "",""Arc 1960"","UTM zone 37S","m",""
            "",""Arc 1960"","UTM zone 37S","m,1.0",""
            "",""Arc 1960"","UTM zone 37S","m,1.0","");
            "",""Arc 1960"","UTM zone 37S","m","Arc 1960 to WGS 84 (1)"
        
            Locally oriented coordinate system (origin at 525000,2500000, rotated 15 deg):
            "21037<525000,2500000,0,0,0,15>","","","",""
            "<525000,2500000,0,0,0,15>","4210","16137","",""
            ""Arc 1960 / UTM zone 37S"<525000,2500000,0,0,0,15>","","","",""
        """
        self._wrapper.set_gxf(str1.encode(), str2.encode(), str3.encode(), str4.encode(), str5.encode())
        




    def set_method_parm(self, parm, parm_value):
        """
        Set projection method parameter

        **Note:**

        If parameter is not valid, nothing happens.
        """
        self._wrapper.set_method_parm(parm, parm_value)
        




    def set_mi_coord_sys(self, coord, units):
        """
        Set coordinate system from a MapInfo coordsys command
        """
        self._wrapper.set_mi_coord_sys(coord.encode(), units.encode())
        




    def set_normal_section_view(self, x, y, z, azimuth, swing):
        """
        Set normal section orientation parameters

        **Note:**

        This section is the type where values are projected
        normal to the section, and the "Y" values in a grid
        do not necessarily correspond to the elvations for a swung section.
        """
        self._wrapper.set_normal_section_view(x, y, z, azimuth, swing)
        




    def set_plan_view(self, x, y, z, rot):
        """
        Set plan orientation parameters.

        **Note:**

        This sets up the orientation of an `GXIPJ` for plan view plots,
        for instance in Wholeplot. These differ from regular plan
        map views in that the elevation of the view plane is set, and
        the view may be rotated. In addition, when viewed in a map,
        a view with this `GXIPJ` will give a status bar location (X, Y, Z)
        of the actual location in space, as opposed to just the X, Y of
        the view plane itself.
        """
        self._wrapper.set_plan_view(x, y, z, rot)
        




    def set_section_view(self, x, y, z, azimuth, swing):
        """
        Set section orientation parameters

        **Note:**

        This sets up the orientation of an `GXIPJ` for section view plots,
        for instance in Wholeplot. In addition, when viewed in a map,
        a view with this `GXIPJ` will give a status bar location (X, Y, Z)
        of the actual location in space, as opposed to just the X, Y of
        the view plane itself.
        Swung sections are tricky because they are set up for section
        plots in such a way that the vertical axis remains "true"; points
        are projected horizontally to the viewing plane, independent of the
        swing angle. In other words, all locations in 3D space viewed using this
        projection will plot on the same horizontal line in the map view.
        This function is NOT suitable for simply creating
        an orientation for a dipping grid or view.
        """
        self._wrapper.set_section_view(x, y, z, azimuth, swing)
        




    def set_wms_coord_sys(self, coord, min_x, min_y, max_x, max_y):
        """
        Set coordinate system from a WMS coordsys string.

        **Note:**

        WMS coordinate strings supported:
        
        
        EPSG:code
        
        where "code" is the EPSG code number
        "EPSG:4326"  is geographic "WGS 84" (see datum.csv)
        "EPSG:25834" is projected "ETRS89 / UTM zone 34N"
        (see ipj_pcs.csv)
        
        The bounding box for EPSG systems must be defined in the
        EPSG coordinate system.  If a bounding box is provided,
        it will not be changed.
        
        
        AUTO:wm_id,epsg_units,lon,lat (see OGC documentation)
        
        for "AUTO" coordinates, the "epsg_units" is the units
        of the bounding box.  This procedure will transform
        the supplied bounding box from these units to the
        units of the projection.  Normally, this is from
        long/lat (9102) to metres (9001).
        """
        self._wrapper.set_wms_coord_sys(coord.encode(), min_x, min_y, max_x, max_y)
        




    def set_xml(self, str_val):
        """
        Set an `GXIPJ` from a Geosoft Metadata XML string
        """
        self._wrapper.set_xml(str_val.encode())
        




    def get_3d_matrix_orientation(self, v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33):
        """
        Gets the coefficients of a 3D matrix orientation.
        """
        v00.value, v01.value, v02.value, v03.value, v10.value, v11.value, v12.value, v13.value, v20.value, v21.value, v22.value, v23.value, v30.value, v31.value, v32.value, v33.value = self._wrapper.get_3d_matrix_orientation(v00.value, v01.value, v02.value, v03.value, v10.value, v11.value, v12.value, v13.value, v20.value, v21.value, v22.value, v23.value, v30.value, v31.value, v32.value, v33.value)
        




    def set_3d_matrix_orientation(self, v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33):
        """
        Apply a 3D orientation directly using matrix coefficients.
        """
        self._wrapper.set_3d_matrix_orientation(v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33)
        




    def reproject_section_grid(self, output_ipj, x0, y0, dx, dy, rot):
        """
        Reproject a section grid

        **Note:**

        Reproject a section grid to a new `GXIPJ`, adjusting its orientation and registration so that
        it remains in the same location.
        """
        x0.value, y0.value, dx.value, dy.value, rot.value = self._wrapper.reproject_section_grid(output_ipj._wrapper, x0.value, y0.value, dx.value, dy.value, rot.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer