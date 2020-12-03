### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXAGG import GXAGG
from .GXBF import GXBF
from .GXCSYMB import GXCSYMB
from .GXDATALINKD import GXDATALINKD
from .GXITR import GXITR
from .GXLST import GXLST
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
class GXMVIEW(gxapi_cy.WrapMVIEW):
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

    def __init__(self, handle=0):
        super(GXMVIEW, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMVIEW <geosoft.gxapi.GXMVIEW>`
        
        :returns: A null `GXMVIEW <geosoft.gxapi.GXMVIEW>`
        :rtype:   GXMVIEW
        """
        return GXMVIEW()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# 3D Entity



    def box_3d(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Draw a 3D box
        
        :param min_x:  Min X
        :param min_y:  Min Y
        :param min_z:  Min Z
        :param max_x:  Max X
        :param max_y:  Max Y
        :param max_z:  Max Z
        :type  min_x:  float
        :type  min_y:  float
        :type  min_z:  float
        :type  max_x:  float
        :type  max_y:  float
        :type  max_z:  float

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Fill color is used to color the box.
        """
        self._box_3d(min_x, min_y, min_z, max_x, max_y, max_z)
        




    def crc_view(self, crc, file):
        """
        Generate an XML CRC of a View
        
        :param crc:    CRC returned
        :param file:   Name of xml to generate (.zip added)
        :type  crc:    int_ref
        :type  file:   str

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        crc.value = self._crc_view(crc.value, file.encode())
        




    def crc_view_group(self, group, crc, file):
        """
        Generate an XML CRC of a Group
        
        :param group:  Name of Group
        :param crc:    CRC returned
        :param file:   Name of xml to generate (.zip added)
        :type  group:  str
        :type  crc:    int_ref
        :type  file:   str

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        crc.value = self._crc_view_group(group.encode(), crc.value, file.encode())
        




    def view_group_json(self, group, file):
        """
        Generate a JSON representation of a Group.
        
        :param group:  Name of Group
        :param file:   Name of JSON file to generate.
        :type  group:  str
        :type  file:   str

        .. versionadded:: 9.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._view_group_json(group.encode(), file.encode())
        




    def cylinder_3d(self, start_x, start_y, start_z, end_x, end_y, end_z, start_radius, end_radius, flags):
        """
        Draw a 3D cylinder
        
        :param start_x:       Start X
        :param start_y:       Start Y
        :param start_z:       Start Z
        :param end_x:         End X
        :param end_y:         End Y
        :param end_z:         End Z
        :param start_radius:  Start Radius (can be zero)
        :param end_radius:    End Radius (can be zero)
        :param flags:         :ref:`MVIEW_CYLINDER3D`
        :type  start_x:       float
        :type  start_y:       float
        :type  start_z:       float
        :type  end_x:         float
        :type  end_y:         float
        :type  end_z:         float
        :type  start_radius:  float
        :type  end_radius:    float
        :type  flags:         int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Fill color is used to color the cylinder.
        The flags determine if the cylinder is open and what
        end are closed. Note that you can create cones by
        specifying a 0 radius for one of the ends.
        """
        self._cylinder_3d(start_x, start_y, start_z, end_x, end_y, end_z, start_radius, end_radius, flags)
        




    def draw_object_3d(self, type, mode, objects, default_count, vert_v_vx, vert_v_vy, vert_v_vz, norm_v_vx, norm_v_vy, norm_v_vz, color_vv, index_vv, count_vv):
        """
        Draw a 3D object optimized for rendering
        
        :param type:           :ref:`MVIEW_DRAWOBJ3D_ENTITY`
        :param mode:           :ref:`MVIEW_DRAWOBJ3D_MODE`
        :param objects:        Number of Objects
        :param default_count:  Default Count (if variable and not specified)
        :param vert_v_vx:      Verticies X
        :param vert_v_vy:      Verticies Y
        :param vert_v_vz:      Verticies Z
        :param norm_v_vx:      Normals X (can be NULL)
        :param norm_v_vy:      Normals Y (can be NULL)
        :param norm_v_vz:      Normals Z (can be NULL)
        :param color_vv:       Colors `GXVV <geosoft.gxapi.GXVV>` (can be NULL)
        :param index_vv:       Index  `GXVV <geosoft.gxapi.GXVV>` (can be NULL)
        :param count_vv:       Count  `GXVV <geosoft.gxapi.GXVV>` (can be NULL)
        :type  type:           int
        :type  mode:           int
        :type  objects:        int
        :type  default_count:  int
        :type  vert_v_vx:      GXVV
        :type  vert_v_vy:      GXVV
        :type  vert_v_vz:      GXVV
        :type  norm_v_vx:      GXVV
        :type  norm_v_vy:      GXVV
        :type  norm_v_vz:      GXVV
        :type  color_vv:       GXVV
        :type  index_vv:       GXVV
        :type  count_vv:       GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._draw_object_3d(type, mode, objects, default_count, vert_v_vx, vert_v_vy, vert_v_vz, norm_v_vx, norm_v_vy, norm_v_vz, color_vv, index_vv, count_vv)
        




    def draw_surface_3d_ex(self, group_name, vert_v_vx, vert_v_vy, vert_v_vz, norm_v_vx, norm_v_vy, norm_v_vz, color_vv, color, tri_vv_pt1, tri_vv_pt2, tri_vv_pt3, ipj):
        """
        Draw a 3D object built from triangles
        
        :param group_name:  Group name
        :param vert_v_vx:   Vertices X (`GS_REAL <geosoft.gxapi.GS_REAL>`)
        :param vert_v_vy:   Vertices Y (`GS_REAL <geosoft.gxapi.GS_REAL>`)
        :param vert_v_vz:   Vertices Z (`GS_REAL <geosoft.gxapi.GS_REAL>`)
        :param norm_v_vx:   Normals X (`GS_REAL <geosoft.gxapi.GS_REAL>`)
        :param norm_v_vy:   Normals Y (`GS_REAL <geosoft.gxapi.GS_REAL>`)
        :param norm_v_vz:   Normals Z (`GS_REAL <geosoft.gxapi.GS_REAL>`)
        :param color_vv:    Colors `GXVV <geosoft.gxapi.GXVV>` (`GS_INT <geosoft.gxapi.GS_INT>`) [can be NULL]
        :param color:       Color used if above `GXVV <geosoft.gxapi.GXVV>` is NULL [0 for `GXMVIEW <geosoft.gxapi.GXMVIEW>`'s fill color]
        :param tri_vv_pt1:  Triangles Point 1 (`GS_INT <geosoft.gxapi.GS_INT>`)
        :param tri_vv_pt2:  Triangles Point 2 (`GS_INT <geosoft.gxapi.GS_INT>`)
        :param tri_vv_pt3:  Triangles Point 3 (`GS_INT <geosoft.gxapi.GS_INT>`)
        :param ipj:         Native `GXIPJ <geosoft.gxapi.GXIPJ>` of 3D object
        :type  group_name:  str
        :type  vert_v_vx:   GXVV
        :type  vert_v_vy:   GXVV
        :type  vert_v_vz:   GXVV
        :type  norm_v_vx:   GXVV
        :type  norm_v_vy:   GXVV
        :type  norm_v_vz:   GXVV
        :type  color_vv:    GXVV
        :type  color:       int
        :type  tri_vv_pt1:  GXVV
        :type  tri_vv_pt2:  GXVV
        :type  tri_vv_pt3:  GXVV
        :type  ipj:         GXIPJ

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Provide one normal per vertex.
        Triangles are defined by indices into the set of vertices.
        """
        self._draw_surface_3d_ex(group_name.encode(), vert_v_vx, vert_v_vy, vert_v_vz, norm_v_vx, norm_v_vy, norm_v_vz, color_vv, color, tri_vv_pt1, tri_vv_pt2, tri_vv_pt3, ipj)
        




    def draw_surface_3d_from_file(self, group_name, surface_file):
        """
        Draw a 3D object from a surface file
        
        :param group_name:    Group name
        :param surface_file:  Surface file
        :type  group_name:    str
        :type  surface_file:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._draw_surface_3d_from_file(group_name.encode(), surface_file.encode())
        



    @classmethod
    def font_weight_lst(cls, lst):
        """
        Fill a `GXLST <geosoft.gxapi.GXLST>` with the different font weights.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object
        :type  lst:  GXLST

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMVIEW._font_weight_lst(GXContext._get_tls_geo(), lst)
        




    def get_agg_file_names(self, group, vv):
        """
        Get the names of grid files stored in an `GXAGG <geosoft.gxapi.GXAGG>`.
        
        :param group:  Group name
        :param vv:     Returned string `GXVV <geosoft.gxapi.GXVV>` of type -`STR_FILE <geosoft.gxapi.STR_FILE>`
        :type  group:  str
        :type  vv:     GXVV

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The group must be an `GXAGG <geosoft.gxapi.GXAGG>` group. Check this using
        `is_group <geosoft.gxapi.GXMVIEW.is_group>` and `MVIEW_IS_AGG <geosoft.gxapi.MVIEW_IS_AGG>`.
        """
        self._get_agg_file_names(group.encode(), vv)
        




    def get_meta(self, group, meta):
        """
        Retrieves Metadata from a group
        
        :param group:  Group Name
        :param meta:   Meta name
        :type  group:  str
        :type  meta:   str_ref

        :returns:      `GXMETA <geosoft.gxapi.GXMETA>` Object
        :rtype:        GXMETA

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, meta.value = self._get_meta(group.encode(), meta.value.encode())
        return GXMETA(ret_val)




    def measure_text(self, text, x_min, y_min, x_max, y_max):
        """
        Compute the bounding rectangle in view units of the text using the current attributes.
        
        :param text:   Text string
        :param x_min:  X minimum
        :param y_min:  Y minimum
        :param x_max:  X maximum
        :param y_max:  Y maximum
        :type  text:   str
        :type  x_min:  float_ref
        :type  y_min:  float_ref
        :type  x_max:  float_ref
        :type  y_max:  float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Area will be 0 if error occurred (does not fail).
        This will return the bounding rectangle as if the text was placed at 0,0 and adjusted according to
        the current text alignment and angle set for the view. Also see notes for `text_size <geosoft.gxapi.GXMVIEW.text_size>`.
        """
        x_min.value, y_min.value, x_max.value, y_max.value = self._measure_text(text.encode(), x_min.value, y_min.value, x_max.value, y_max.value)
        




    def point_3d(self, x, y, z):
        """
        Draw a 3D point.
        
        :param x:      X
        :param y:      Y
        :param z:      Z
        :type  x:      float
        :type  y:      float
        :type  z:      float

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Line color and line thickness will affect rendering.
        """
        self._point_3d(x, y, z)
        




    def poly_line_3d(self, vv_x, vv_y, vv_z):
        """
        Draw a 3D polyline.
        
        :param vv_x:   X coordinates.
        :param vv_y:   Y coordinates.
        :param vv_z:   Z coordinates.
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV
        :type  vv_z:   GXVV

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummies are not allowed in the line.
        Line Color, Thickness is supported on rendering
        """
        self._poly_line_3d(vv_x, vv_y, vv_z)
        




    def relocate_group(self, group, min_x, min_y, max_x, max_y, asp):
        """
        Re-locate a group in a view.
        
        :param group:  Group name
        :param min_x:  Area X minimum
        :param min_y:  Area Y minimum
        :param max_x:  Area X maximum
        :param max_y:  Area Y maximum
        :param asp:    :ref:`MVIEW_RELOCATE`
        :type  group:  str
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float
        :type  asp:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._relocate_group(group.encode(), min_x, min_y, max_x, max_y, asp)
        




    def set_meta(self, group, meta, name):
        """
        Update the `GXMETA <geosoft.gxapi.GXMETA>` in this group with the new meta object.
        
        :param group:  Group Name
        :param meta:   `GXMETA <geosoft.gxapi.GXMETA>` object
        :param name:   Meta name of Object
        :type  group:  str
        :type  meta:   GXMETA
        :type  name:   str

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_meta(group.encode(), meta, name.encode())
        




    def sphere_3d(self, x, y, z, radius):
        """
        Draw a 3D sphere
        
        :param x:       Center X
        :param y:       Center Y
        :param z:       Center Z
        :param radius:  Radius
        :type  x:       float
        :type  y:       float
        :type  z:       float
        :type  radius:  float

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Fill color is used to color the sphere.
        """
        self._sphere_3d(x, y, z, radius)
        




    def update_met_afrom_group(self, group, meta):
        """
        Fill the `GXMETA <geosoft.gxapi.GXMETA>` with group dataset information
        
        :param group:  Group Name
        :param meta:   `GXMETA <geosoft.gxapi.GXMETA>` object to fill
        :type  group:  str
        :type  meta:   GXMETA

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._update_met_afrom_group(group.encode(), meta)
        




# 3D Plane



    def delete_plane(self, plane, del_grp):
        """
        Delete a plane in a view
        
        :param plane:    Plane number to delete
        :param del_grp:  TRUE to delete all groups on the plane
        :type  plane:    int
        :type  del_grp:  int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the groups on the plane are not deleted, they will remain in the
        3D view as "New" groups but will be unassigned to a plane.  The
        SetAllNewGroupsToPlane  function can be used to assign these groups
        to a different plane.
        """
        self._delete_plane(plane, del_grp)
        




    def get_plane_clip_ply(self, plane, pply):
        """
        Get the Plane Clip Region
        
        :param plane:  Plane index
        :param pply:   Clip Region
        :type  plane:  int
        :type  pply:   GXPLY

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** By default it is the View's Clip Region
        """
        self._get_plane_clip_ply(plane, pply)
        




    def get_plane_equation(self, plane, pitch, yaw, roll, x, y, z, sx, sy, sz):
        """
        Get the equation of a plane
        
        :param plane:  Plane index
        :param pitch:  Rotation about X (Y toward Z +ve, between -360 and 360)
        :param yaw:    Rotation about Y (Z toward X +ve, between -360 and 360)
        :param roll:   Rotation about Z (Y toward X +ve, between -360 and 360)
        :param x:      X offset of plane
        :param y:      Y offset of plane
        :param z:      Z offset of plane
        :param sx:     X scale
        :param sy:     Y scale
        :param sz:     Z scale
        :type  plane:  int
        :type  pitch:  float_ref
        :type  yaw:    float_ref
        :type  roll:   float_ref
        :type  x:      float_ref
        :type  y:      float_ref
        :type  z:      float_ref
        :type  sx:     float_ref
        :type  sy:     float_ref
        :type  sz:     float_ref

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, sz.value = self._get_plane_equation(plane, pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, sz.value)
        




    def get_view_plane_equation(self, pitch, yaw, roll, x, y, z, sx, sy, sz):
        """
        Get the View's Plane Equation
        
        :param pitch:  Angle in X
        :param yaw:    Angle in Y
        :param roll:   Angle in Z
        :param x:      Offset in X
        :param y:      Offset in Y
        :param z:      Offset in Z
        :param sx:     Scale in X
        :param sy:     Scale in Y
        :param sz:     Scale in Z
        :type  pitch:  float_ref
        :type  yaw:    float_ref
        :type  roll:   float_ref
        :type  x:      float_ref
        :type  y:      float_ref
        :type  z:      float_ref
        :type  sx:     float_ref
        :type  sy:     float_ref
        :type  sz:     float_ref

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, sz.value = self._get_view_plane_equation(pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, sz.value)
        




    def create_plane(self, plane):
        """
        Create a 3D Plane for 2D Groups
        
        :param plane:  Name of Plane
        :type  plane:  str

        :returns:      x - Index of plane
        :rtype:        int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._create_plane(plane.encode())
        return ret_val




    def find_plane(self, plane):
        """
        Find a plane in a view
        
        :param plane:  Name of the plane
        :type  plane:  str

        :returns:      Plane number, -1 if not found
        :rtype:        int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._find_plane(plane.encode())
        return ret_val




    def is_surface_plane(self, plane):
        """
        Is a surface plane?
        
        :param plane:  Name of the plane
        :type  plane:  str
        :rtype:        bool

        .. versionadded:: 9.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_surface_plane(plane.encode())
        return ret_val




    def is_plane_visible(self, plane):
        """
        Is the plane visible?
        
        :param plane:  Name of the plane
        :type  plane:  str
        :rtype:        bool

        .. versionadded:: 9.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_plane_visible(plane.encode())
        return ret_val




    def get_def_plane(self, name):
        """
        Get the default drawing plane.
        
        :param name:   Name
        :type  name:   str_ref

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 2D drawing to a 3D View will always be placed on the
        default drawing plane.  If no default drawing plane
        has been set, the first valid plane in the view is
        used as the default drawing plane.
        """
        name.value = self._get_def_plane(name.value.encode())
        




    def is_view_3d(self):
        """
        Is the view 3D?
        

        :returns:      TRUE if view is 3D
        :rtype:        int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_view_3d()
        return ret_val




    def is_section(self):
        """
        Is the view a section view?
        

        :returns:      TRUE if view is a section view.
        :rtype:        int

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Section views are recognized because their projection contains one of the following orientations:

        `IPJ_ORIENT_SECTION <geosoft.gxapi.IPJ_ORIENT_SECTION>` - Target-type sections with Z projection horizontally
        `IPJ_ORIENT_SECTION_NORMAL <geosoft.gxapi.IPJ_ORIENT_SECTION_NORMAL>` - Like `IPJ_ORIENT_SECTION <geosoft.gxapi.IPJ_ORIENT_SECTION>`, but Z projects
        perpendicular to the secton plane.
        `IPJ_ORIENT_SECTION_CROOKED <geosoft.gxapi.IPJ_ORIENT_SECTION_CROOKED>` - Crooked sections
        `IPJ_ORIENT_3D <geosoft.gxapi.IPJ_ORIENT_3D>` - Some Sections extracted from a voxel - e.g. VoxelToGrids,
        as the voxel can have any orientation in 3D.
        """
        ret_val = self._is_section()
        return ret_val




    def list_plane_groups(self, plane, lst):
        """
        List all groups in a specific plane of a 3D view
        
        :param plane:  Plane number
        :param lst:    List of plane names and numbers
        :type  plane:  int
        :type  lst:    GXLST

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The group names are placed in the list names, group
        numbers are placed in the list values.

        Groups are added to the end of the `GXLST <geosoft.gxapi.GXLST>`.
        """
        self._list_plane_groups(plane, lst)
        




    def list_planes(self, lst):
        """
        List all planes in a 3D view
        
        :param lst:    List of plane names and numbers
        :type  lst:    GXLST

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The plane names are placed in the list names, plane
        numbers are placed in the list values.

        Planes are added to the end of the `GXLST <geosoft.gxapi.GXLST>`.
        """
        self._list_planes(lst)
        




    def set_all_groups_to_plane(self, plane):
        """
        Set all groups to be within one plane
        
        :param plane:  Plane Index to set all groups to
        :type  plane:  int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_all_groups_to_plane(plane)
        




    def set_all_new_groups_to_plane(self, plane):
        """
        Set all groups that are not in any plane to this plane
        
        :param plane:  Plane Index to set all groups to
        :type  plane:  int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_all_new_groups_to_plane(plane)
        




    def set_def_plane(self, name):
        """
        Set the default drawing plane.
        
        :param name:   Name
        :type  name:   str

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 2D drawing to a 3D View will always be placed on the
        default drawing plane.  If no default drawing plane
        has been set, the first valid plane in the view is
        used as the default drawing plane.
        """
        self._set_def_plane(name.encode())
        




    def set_group_to_plane(self, plane, group):
        """
        Set a group to a plane
        
        :param plane:  Plane Index to set all groups to
        :param group:  Name of group to set
        :type  plane:  int
        :type  group:  str

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_group_to_plane(plane, group.encode())
        




    def set_3dn(self, o3dn):
        """
        Set the `GX3DN <geosoft.gxapi.GX3DN>` object for this view
        
        :param o3dn:   `GX3DN <geosoft.gxapi.GX3DN>` to set (NULL for 2D view)
        :type  o3dn:   GX3DN

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To make the view a 2D view, set a `GX3DN <geosoft.gxapi.GX3DN>` of NULL.
        """
        self._set_3dn(o3dn)
        




    def get_3d_point_of_view(self, x, y, z, distance, declination, inclination):
        """
        Get 3D point of view (values are will be `rDUMMY <geosoft.gxapi.rDUMMY>` if view for 2D views)
        
        :param x:            X center
        :param y:            Y center
        :param z:            Z center
        :param distance:     Distance from center
        :param declination:  Declination, 0 to 360 CW from Y
        :param inclination:  Inclination, -90 to +90
        :type  x:            float_ref
        :type  y:            float_ref
        :type  z:            float_ref
        :type  distance:     float_ref
        :type  declination:  float_ref
        :type  inclination:  float_ref

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        x.value, y.value, z.value, distance.value, declination.value, inclination.value = self._get_3d_point_of_view(x.value, y.value, z.value, distance.value, declination.value, inclination.value)
        




    def set_3d_point_of_view(self, x, y, z, distance, declination, inclination):
        """
        Set 3D point of view (no effect on 2D views)
        
        :param x:            X center
        :param y:            Y center
        :param z:            Z center
        :param distance:     Distance from center
        :param declination:  Declination, 0 to 360 CW from Y
        :param inclination:  Inclination, -90 to +90
        :type  x:            float
        :type  y:            float
        :type  z:            float
        :type  distance:     float
        :type  declination:  float
        :type  inclination:  float

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_3d_point_of_view(x, y, z, distance, declination, inclination)
        




    def set_plane_clip_ply(self, plane, pply):
        """
        Set the Plane Clip Region
        
        :param plane:  Plane index
        :param pply:   Clip Region
        :type  plane:  int
        :type  pply:   GXPLY

        .. versionadded:: 5.1.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** By default it is the View's Clip Region
        """
        self._set_plane_clip_ply(plane, pply)
        




    def set_plane_equation(self, plane, pitch, yaw, roll, x, y, z, sx, sy, sz):
        """
        Set the equation of a plane
        
        :param plane:  Plane index
        :param pitch:  Rotation about X (Z toward Y +ve, between -360 and 360)
        :param yaw:    Rotation about Y (Z toward X +ve, between -360 and 360)
        :param roll:   Rotation about Z (Y toward X +ve, between -360 and 360)
        :param x:      X offset of plane
        :param y:      Y offset of plane
        :param z:      Z offset of plane
        :param sx:     X scale
        :param sy:     Y scale
        :param sz:     Z scale
        :type  plane:  int
        :type  pitch:  float
        :type  yaw:    float
        :type  roll:   float
        :type  x:      float
        :type  y:      float
        :type  z:      float
        :type  sx:     float
        :type  sy:     float
        :type  sz:     float

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** For a grid with the "Y" axis giving elevation:
        use rotations = (-90, 0, 0) for a section with azimuth 90 (E-W)
        use rotations = (-90, 0, -90) for a section with azimuth 0 (N-S)
        """
        self._set_plane_equation(plane, pitch, yaw, roll, x, y, z, sx, sy, sz)
        




    def set_plane_surface(self, plane, surface):
        """
        Set the surface image of a plane
        
        :param plane:    Plane index
        :param surface:  Optional surface image/grid name, can be empty
        :type  plane:    int
        :type  surface:  str

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_plane_surface(plane, surface.encode())
        




    def get_plane_surface(self, plane, surface):
        """
        Get the surface image of a plane
        
        :param plane:    Plane index
        :param surface:  Optional surface image/grid name, can be empty
        :type  plane:    int
        :type  surface:  str_ref

        .. versionadded:: 9.9

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        surface.value = self._get_plane_surface(plane, surface.value.encode())
        




    def set_plane_surf_info(self, plane, sample, base, scale, min, max):
        """
        Set the surface information
        
        :param plane:   Plane index
        :param sample:  Sample rate (>=1)
        :param base:    Base
        :param scale:   Scale
        :param min:     Min
        :param max:     Max
        :type  plane:   int
        :type  sample:  int
        :type  base:    float
        :type  scale:   float
        :type  min:     float
        :type  max:     float

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_plane_surf_info(plane, sample, base, scale, min, max)
        




    def get_plane_surf_info(self, plane, sample, base, scale, min, max):
        """
        Get the surface information
        
        :param plane:   Plane index
        :param sample:  Sample rate (>=1)
        :param base:    Base
        :param scale:   Scale
        :param min:     Min
        :param max:     Max
        :type  plane:   int
        :type  sample:  int_ref
        :type  base:    float_ref
        :type  scale:   float_ref
        :type  min:     float_ref
        :type  max:     float_ref

        .. versionadded:: 9.9

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        sample.value, base.value, scale.value, min.value, max.value = self._get_plane_surf_info(plane, sample.value, base.value, scale.value, min.value, max.value)
        




# 3D Rendering 2D



    def define_plane_3d(self, center_x, center_y, center_z, x_vector_x, x_vector_y, x_vector_z, y_vector_x, y_vector_y, y_vector_z):
        """
        Define a 2D drawing plane based on point and normal
        
        :param center_x:    Center point X
        :param center_y:    Center point Y
        :param center_z:    Center point Z
        :param x_vector_x:  X Vector X
        :param x_vector_y:  X Vector Y
        :param x_vector_z:  X Vector Z
        :param y_vector_x:  Y Vector X
        :param y_vector_y:  Y Vector Y
        :param y_vector_z:  Y Vector Z
        :type  center_x:    float
        :type  center_y:    float
        :type  center_z:    float
        :type  x_vector_x:  float
        :type  x_vector_y:  float
        :type  x_vector_z:  float
        :type  y_vector_x:  float
        :type  y_vector_y:  float
        :type  y_vector_z:  float

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 2D rendering commands are translated to 3D commands
        based on the plane.
        """
        self._define_plane_3d(center_x, center_y, center_z, x_vector_x, x_vector_y, x_vector_z, y_vector_x, y_vector_y, y_vector_z)
        




    def define_viewer_axis_3d(self, center_x, center_y, center_z, dir_point_x, dir_point_y, dir_point_z):
        """
        Define a 2D drawing plane based on the user's view that
        oriented around the vector.
        
        :param center_x:     Center point X
        :param center_y:     Center point Y
        :param center_z:     Center point Z
        :param dir_point_x:  Directional Point X
        :param dir_point_y:  Directional Point Y
        :param dir_point_z:  Directional Point Z
        :type  center_x:     float
        :type  center_y:     float
        :type  center_z:     float
        :type  dir_point_x:  float
        :type  dir_point_y:  float
        :type  dir_point_z:  float

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._define_viewer_axis_3d(center_x, center_y, center_z, dir_point_x, dir_point_y, dir_point_z)
        




    def define_viewer_plane_3d(self, center_x, center_y, center_z):
        """
        Define a 2D drawing plane based on the user's view.
        
        :param center_x:  Center point X
        :param center_y:  Center point Y
        :param center_z:  Center point Z
        :type  center_x:  float
        :type  center_y:  float
        :type  center_z:  float

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The plane is always facing the viewer. Otherwise the
        this is identical to the previous
        """
        self._define_viewer_plane_3d(center_x, center_y, center_z)
        




# 3D Snapshots



    def get_3d_snapshots(self):
        """
        Get the list of 3D snapshots in a 3D view.
        

        :returns:      `GXLST <geosoft.gxapi.GXLST>` object
        :rtype:        GXLST

        .. versionadded:: 9.9

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns name/guid pairs.
        """
        ret_val = self._get_3d_snapshots()
        return GXLST(ret_val)




    def restore_3d_snapshot(self, guid):
        """
        Restore 3D view to specific snapshot state.
        
        :param guid:   Snapshot GUID
        :type  guid:   str

        .. versionadded:: 9.9

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._restore_3d_snapshot(guid.encode())
        




    def capture_3d_snapshot(self, name, description, light_weight, guid):
        """
        Capture current 3D view state to a snapshot.
        
        :param name:          Snapshot name
        :param description:   Snapshot description
        :param light_weight:  Is this a light weight snapshot, i.e. just captures view orientation and type and not group visibility/clipping etc.
        :param guid:          Snapshot GUID
        :type  name:          str
        :type  description:   str
        :type  light_weight:  bool
        :type  guid:          str_ref

        .. versionadded:: 9.9

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        guid.value = self._capture_3d_snapshot(name.encode(), description.encode(), light_weight, guid.value.encode())
        




# Clipping



    def clip_poly_ex(self, vv_x, vv_y, unit, exclude):
        """
        Add a polygon to the clip region.
        
        :param vv_x:     X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:     Y `GXVV <geosoft.gxapi.GXVV>`
        :param unit:     :ref:`MVIEW_UNIT`
        :param exclude:  Exclude
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  unit:     int
        :type  exclude:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The polygon will be added to the current clip region.
        The `GXVV <geosoft.gxapi.GXVV>`'s cannot have any dummy elements.
        """
        self._clip_poly_ex(vv_x, vv_y, unit, exclude)
        




    def clip_rect_ex(self, min_x, min_y, max_x, max_y, unit, exclude):
        """
        Add a rectangle to the clip region.
        
        :param min_x:    X minimum
        :param min_y:    Y minimum
        :param max_x:    X maximum
        :param max_y:    Y maximum
        :param unit:     :ref:`MVIEW_UNIT`
        :param exclude:  Exclude
        :type  min_x:    float
        :type  min_y:    float
        :type  max_x:    float
        :type  max_y:    float
        :type  unit:     int
        :type  exclude:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The rectangle will be added to the current clip region.
        """
        self._clip_rect_ex(min_x, min_y, max_x, max_y, unit, exclude)
        




    def clip_clear(self):
        """
        Remove/clear the view clip region.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._clip_clear()
        




    def clip_groups(self, mode):
        """
        Set the Clipping mode on/off for all groups.
        
        :param mode:   :ref:`MVIEW_CLIP`
        :type  mode:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._clip_groups(mode)
        




    def clip_marked_groups(self, mode):
        """
        Set the Clipping mode on/off for marked groups.
        
        :param mode:   :ref:`MVIEW_CLIP`
        :type  mode:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._clip_marked_groups(mode)
        




    def clip_poly(self, vv_x, vv_y, unit):
        """
        Add a polygon to the clip region.
        
        :param vv_x:   X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:   Y `GXVV <geosoft.gxapi.GXVV>`
        :param unit:   :ref:`MVIEW_UNIT`
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV
        :type  unit:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The polygon will be added to the current clip region.
        The `GXVV <geosoft.gxapi.GXVV>`'s cannot have any dummy elements.
        """
        self._clip_poly(vv_x, vv_y, unit)
        




    def clip_rect(self, min_x, min_y, max_x, max_y, unit):
        """
        Add a rectangle to the clip region.
        
        :param min_x:  X minimum
        :param min_y:  Y minimum
        :param max_x:  X maximum
        :param max_y:  Y maximum
        :param unit:   :ref:`MVIEW_UNIT`
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float
        :type  unit:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The rectangle will be added to the current clip region.
        """
        self._clip_rect(min_x, min_y, max_x, max_y, unit)
        




    def delete_ext_clip_ply(self, ext_ply):
        """
        Deletes an extended clip `GXPLY <geosoft.gxapi.GXPLY>` object used by this view.
        
        :param ext_ply:  Extended ClipPLY number
        :type  ext_ply:  int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._delete_ext_clip_ply(ext_ply)
        




    def ext_clip_ply_list(self, lst):
        """
        Get the names of existing extended clip `GXPLY <geosoft.gxapi.GXPLY>` objects in this view as list.
        
        :type  lst:    GXLST

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._ext_clip_ply_list(lst)
        




    def get_clip_ply(self, poly):
        """
        Get clipping polygons, in the user projection
        
        :param poly:   Poly
        :type  poly:   GXPLY

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The returned `GXPLY <geosoft.gxapi.GXPLY>` is recast into the User projection.
        For oriented views (especially sections), use
        `get_ply <geosoft.gxapi.GXMVIEW.get_ply>`, which returns the Clip `GXPLY <geosoft.gxapi.GXPLY>` in the view's native
        projection (e.g. the one set using `set_ipj <geosoft.gxapi.GXMVIEW.set_ipj>`).
        """
        self._get_clip_ply(poly)
        




    def get_ext_clip_ply(self, ext_ply, ply):
        """
        Get an extended clip `GXPLY <geosoft.gxapi.GXPLY>` object used by this view.
        
        :param ext_ply:  Extended ClipPLY number
        :param ply:      `GXPLY <geosoft.gxapi.GXPLY>` object to get
        :type  ext_ply:  int
        :type  ply:      GXPLY

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_ext_clip_ply(ext_ply, ply)
        




    def get_group_ext_clip_ply(self, group, ext_ply):
        """
        Gets extended clip information for group in view.
        
        :param group:    Group Name
        :param ext_ply:  Extended `GXPLY <geosoft.gxapi.GXPLY>` number (returned, -1 if not set)
        :type  group:    str
        :type  ext_ply:  int_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ext_ply.value = self._get_group_ext_clip_ply(group.encode(), ext_ply.value)
        




    def get_ply(self, poly):
        """
        Get clipping polygons, in the base projection
        
        :param poly:   Poly
        :type  poly:   GXPLY

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This should be used to get the clipping polygon for
        oriented views (especially sections).
        """
        self._get_ply(poly)
        




    def group_clip_mode(self, mode):
        """
        Set the Clipping mode on or off for new groups.
        
        :param mode:   :ref:`MVIEW_CLIP`
        :type  mode:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All new groups will be clipped.
        """
        self._group_clip_mode(mode)
        




    def get_name_ext_clip_ply(self, ext_ply, name):
        """
        Get the name of the extended clip `GXPLY <geosoft.gxapi.GXPLY>` object in this view.
        
        :param ext_ply:  Extended ClipPLY number
        :param name:     Name
        :type  ext_ply:  int
        :type  name:     str_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value = self._get_name_ext_clip_ply(ext_ply, name.value.encode())
        




    def num_ext_clip_ply(self):
        """
        Get the number of extended clip `GXPLY <geosoft.gxapi.GXPLY>` objects in this view.
        

        :returns:      Number of PLYs
        :rtype:        int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_ext_clip_ply()
        return ret_val




    def set_ext_clip_ply(self, ext_ply, name, ply):
        """
        Set an extended clip `GXPLY <geosoft.gxapi.GXPLY>` object used by this view.
        
        :param ext_ply:  Extended ClipPLY number, If greater or equal to the return value of `num_ext_clip_ply <geosoft.gxapi.GXMVIEW.num_ext_clip_ply>` it will be added to the end of the current list
        :param name:     Name (Has to be unique, otherwise error will be returned)
        :param ply:      `GXPLY <geosoft.gxapi.GXPLY>` object to set, use a null `GXPLY <geosoft.gxapi.GXPLY>` to rename an existing object
        :type  ext_ply:  int
        :type  name:     str
        :type  ply:      GXPLY

        :returns:        Index of new or changed `GXPLY <geosoft.gxapi.GXPLY>`, -1 on error
        :rtype:          int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._set_ext_clip_ply(ext_ply, name.encode(), ply)
        return ret_val




    def set_clip_ply(self, poly):
        """
        Set clipping region to a `GXPLY <geosoft.gxapi.GXPLY>`
        
        :param poly:   Poly
        :type  poly:   GXPLY

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_clip_ply(poly)
        




    def set_group_ext_clip_ply(self, group, ext_ply):
        """
        Sets extended clip information for group in view.
        
        :param group:    Group Name
        :param ext_ply:  Extended `GXPLY <geosoft.gxapi.GXPLY>` number (-1 to clear)
        :type  group:    str
        :type  ext_ply:  int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_group_ext_clip_ply(group.encode(), ext_ply)
        




# Color


    @classmethod
    def color2_rgb(cls, color, r, g, b):
        """
        Convert to RGB values.
        
        :param color:  Color value
        :param r:      Red
        :param g:      Green
        :param b:      Blue
        :type  color:  int
        :type  r:      int_ref
        :type  g:      int_ref
        :type  b:      int_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Color component intensities will be in the range 0-255.

        .. seealso::

            `color <geosoft.gxapi.GXMVIEW.color>`
        """
        r.value, g.value, b.value = gxapi_cy.WrapMVIEW._color2_rgb(GXContext._get_tls_geo(), color, r.value, g.value, b.value)
        



    @classmethod
    def color_descr(cls, color, color_descr):
        """
        Convert a color to a color string label
        
        :param color:        COL_ANY variable
        :param color_descr:  Color descriptor returned
        :type  color:        int
        :type  color_descr:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `color <geosoft.gxapi.GXMVIEW.color>`.
        """
        color_descr.value = gxapi_cy.WrapMVIEW._color_descr(GXContext._get_tls_geo(), color, color_descr.value.encode())
        



    @classmethod
    def color(cls, color):
        """
        Get a color from a color string label
        
        :param color:  Color name string
        :type  color:  str

        :returns:      Color int
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Color strings may be "R","G","B","C","M","Y",
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
        ret_val = gxapi_cy.WrapMVIEW._color(GXContext._get_tls_geo(), color.encode())
        return ret_val



    @classmethod
    def color_cmy(cls, c, m, y):
        """
        Return CMY color.
        
        :param c:  Cyan
        :param m:  Magenta
        :param y:  Yellow
        :type  c:  int
        :type  m:  int
        :type  y:  int

        :returns:    Color int based on color model.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Color component intensities must be in the range 0-255.

        .. seealso::

            `color <geosoft.gxapi.GXMVIEW.color>`
        """
        ret_val = gxapi_cy.WrapMVIEW._color_cmy(GXContext._get_tls_geo(), c, m, y)
        return ret_val



    @classmethod
    def color_hsv(cls, h, s, v):
        """
        Return HSV color.
        
        :param h:  Hue
        :param s:  Saturation
        :param v:  Color
        :type  h:  int
        :type  s:  int
        :type  v:  int

        :returns:    Color int based on color model.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Color component intensities must be in the range 0-255.

        .. seealso::

            `color <geosoft.gxapi.GXMVIEW.color>`
        """
        ret_val = gxapi_cy.WrapMVIEW._color_hsv(GXContext._get_tls_geo(), h, s, v)
        return ret_val



    @classmethod
    def color_rgb(cls, r, g, b):
        """
        Return RGB color.
        
        :param r:  Red
        :param g:  Green
        :param b:  Blue
        :type  r:  int
        :type  g:  int
        :type  b:  int

        :returns:    Color int based on color model.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Color component intensities must be in the range 0-255.

        .. seealso::

            `color <geosoft.gxapi.GXMVIEW.color>`
        """
        ret_val = gxapi_cy.WrapMVIEW._color_rgb(GXContext._get_tls_geo(), r, g, b)
        return ret_val




# Drawing Attribute



    def clip_mode(self, mode):
        """
        Set the view clipping mode on or off.
        
        :param mode:   :ref:`MVIEW_CLIP`
        :type  mode:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Entitles that follow in this group will be clipped
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
        self._clip_mode(mode)
        




    def fill_color(self, color):
        """
        Set the fill color.
        
        :param color:  Color
        :type  color:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._fill_color(color)
        




    def line_color(self, color):
        """
        Set the line color.
        
        :param color:  Color
        :type  color:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._line_color(color)
        




    def line_smooth(self, smooth):
        """
        Set the line edge smoothing.
        
        :param smooth:  :ref:`MVIEW_SMOOTH`
        :type  smooth:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._line_smooth(smooth)
        




    def line_style(self, style, pitch):
        """
        Set the style of a line.
        
        :param style:  Line Style #, see default.lpt
        :param pitch:  Pitch in view units
        :type  style:  int
        :type  pitch:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Line styles are selected by ordinal value (line style #)
        from those defined in default.lpt.  If default.lpt does
        not have a the style specified, the file user.lpt is
        searched.  If this file does not contain the line style
        solid is assumed.

        Note that line styles from default.lpt and user.lpt are
        read into the map at the time the map is created, not
        at display time.
        """
        self._line_style(style, pitch)
        




    def line_thick(self, thick):
        """
        Set the line thickness.
        
        :param thick:  Line thickness in view space units
        :type  thick:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._line_thick(thick)
        




    def pat_angle(self, angle):
        """
        Sets the pattern angle
        
        :param angle:  Angle
        :type  angle:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Allows the user to apply a rotation to the basic
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
        self._pat_angle(angle)
        




    def pat_density(self, density):
        """
        Sets the tiling density.
        
        :param density:  Relative density (default = 1).
        :type  density:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This number is the ratio between the plotted unit cell size and the
        distance between the plotted tile centers. The default value is 1.
        A value larger than 1 increases the density of the pattern, while
        values less than 1 make the pattern more "spread out".
        This can be used along with sPatStyleMethod to create more complicated
        fills from simple patterns.

        See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._pat_density(density)
        




    def pat_number(self, number):
        """
        Sets the pattern number
        
        :param number:  Pattern number
        :type  number:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Pattern 0 is solid fill.(default)
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
        self._pat_number(number)
        




    def pat_size(self, size):
        """
        Sets the pattern unit cell size (X)
        
        :param size:   Pattern size in view units
        :type  size:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._pat_size(size)
        




    def pat_style(self, style):
        """
        Sets the tiling method (i.e. rectangle, triangle)
        
        :param style:  :ref:`MVIEW_TILE`
        :type  style:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Normally, the unit cell is duplicated across the fill area
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
        self._pat_style(style)
        




    def pat_thick(self, thick):
        """
        Sets the pattern line thickness
        
        :param thick:  Line thickness as fraction of pattern size (ie. 0.05)
        :type  thick:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See the IMPORTANT note for sPatNumber_MVIEW().
        """
        self._pat_thick(thick)
        




    def symb_angle(self, angle):
        """
        Set the Symb angle.
        
        :param angle:  Angle in degrees CCW from +X
        :type  angle:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._symb_angle(angle)
        




    def symb_color(self, color):
        """
        Set the Symbol color.
        
        :param color:  Color
        :type  color:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._symb_color(color)
        




    def symb_fill_color(self, color):
        """
        Set the Symbol color fill.
        
        :param color:  Color
        :type  color:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._symb_fill_color(color)
        




    def symb_font(self, face, geofont, weight, italic):
        """
        Set the symbol font and style.
        
        :param face:     Face name
        :param geofont:  Geosoft font?
        :param weight:   :ref:`MVIEW_FONT_WEIGHT`
        :param italic:   Italic font?
        :type  face:     str
        :type  geofont:  bool
        :type  weight:   int
        :type  italic:   bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the font cannot be found, the DEFAULT_SYMBOL_FONT
        specified in the [MONTAJ] section of GEOSOFT.INI
        will be used.

        See `text_font <geosoft.gxapi.GXMVIEW.text_font>` for the font name syntax.
        """
        self._symb_font(face.encode(), geofont, weight, italic)
        




    def symb_number(self, number):
        """
        Set the Symbol number.
        
        :param number:  Symbol number
        :type  number:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The lower 16 bits of the number is interpreted as UTF-16 with a valid Unicode character
        code point. GFN fonts wil produce valid symbols depending on the font for 0x01-0x7f and the degree,
        plus-minus and diameter symbol(latin small letter o with stroke) for 0xB0, 0xB1 and 0xF8 respectively.

        It is possible to check if a character is valid using `GXUNC.is_valid_utf16_char <geosoft.gxapi.GXUNC.is_valid_utf16_char>`. The high 16-bits are reserved
        for future use. Also see: `GXUNC.valid_symbol <geosoft.gxapi.GXUNC.valid_symbol>` and `GXUNC.validate_symbols <geosoft.gxapi.GXUNC.validate_symbols>`.
        """
        self._symb_number(number)
        




    def symb_size(self, size):
        """
        Set the Symb size.
        
        :param size:   Size in view units
        :type  size:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._symb_size(size)
        




    def text_angle(self, angle):
        """
        Set the text angle.
        
        :param angle:  Angle in degrees CCW from +X
        :type  angle:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._text_angle(angle)
        




    def text_color(self, color):
        """
        Set the Text color.
        
        :param color:  Color
        :type  color:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._text_color(color)
        




    def text_font(self, face, geo_font, weight, italic):
        """
        Set the text font.
        
        :param face:      Font face name
        :param geo_font:  Geosoft font? (TRUE or FALSE)
        :param weight:    :ref:`MVIEW_FONT_WEIGHT`
        :param italic:    Italic font? (TRUE or FALSE)
        :type  face:      str
        :type  geo_font:  int
        :type  weight:    int
        :type  italic:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Font characteristics can be defined using the function parameters,
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
        on the GX API level are encoded in :ref:`UTF8` during runtime which makes it possible
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
        self._text_font(face.encode(), geo_font, weight, italic)
        




    def text_ref(self, ref):
        """
        Set the text plot reference point.
        
        :param ref:    :ref:`TEXT_REF`
        :type  ref:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._text_ref(ref)
        




    def text_size(self, size):
        """
        Set the text size.
        
        :param size:   Size in view units
        :type  size:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Because views may have differing X and Y scales this size can only make sense in one of these directions
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
        self._text_size(size)
        




    def transparency(self, trans):
        """
        Sets the transparency for new objects.
        
        :param trans:  Transparency (1.0 - Opaque, 0.0 - Transparent)
        :type  trans:  float

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1.0 Renders completely opaque objects while 0.0 will be transparent.
        Objects written after this will have a combined transparency value with the
        group transparency if it is set (e.g. 0.5 for group and 0.8 stream will result in 0.4).
        """
        self._transparency(trans)
        




    def z_value(self, val):
        """
        Sets Z-value info.
        
        :param val:    Z-Value
        :type  val:    float

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This number is stored in map mainly for exports to other vector formats (e.g ShapeFiles)
        A contour map that's exported to a shape file will use this value as a Z-value attributes for its shapes.
        """
        self._z_value(val)
        




# Drawing Entity



    def arc(self, x, y, radius, ratio, angle, start, end):
        """
        Draw an arc.
        
        :param x:       Center x
        :param y:       Center y
        :param radius:  Radius
        :param ratio:   Ratio x/y
        :param angle:   Angle
        :param start:   Start angle
        :param end:     End angle
        :type  x:       float
        :type  y:       float
        :type  radius:  float
        :type  ratio:   float
        :type  angle:   float
        :type  start:   float
        :type  end:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._arc(x, y, radius, ratio, angle, start, end)
        




    def chord(self, x, y, radius, ratio, angle, start, end):
        """
        Draw a filled arc.
        
        :param x:       Center x
        :param y:       Center y
        :param radius:  Radius
        :param ratio:   Ratio x/y
        :param angle:   Angle
        :param start:   Start angle
        :param end:     End angle
        :type  x:       float
        :type  y:       float
        :type  radius:  float
        :type  ratio:   float
        :type  angle:   float
        :type  start:   float
        :type  end:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._chord(x, y, radius, ratio, angle, start, end)
        




    def classified_symbols(self, vv_x, vv_y, vv_z, scal_mm, zmin, zval, size, fcol):
        """
        Plot classified symbols
        
        :param vv_x:     X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:     Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:     Data `GXVV <geosoft.gxapi.GXVV>`
        :param scal_mm:  Scale factor to convert mm to view units
        :param zmin:     Classified minimum Z to plot
        :param zval:     Comma delimited list of Z maximums
        :param size:     Comma delimited list of sizes in mm
        :param fcol:     Comma delimited list of color strings
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  vv_z:     GXVV
        :type  scal_mm:  float
        :type  zmin:     float
        :type  zval:     str
        :type  size:     str
        :type  fcol:     str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** For example, to plot three levels <95, 95-100 and
        100-120, three string arguments would be:

        "95,100,120"      maximums of each class
        "2.0,2.5,3.0"     sizes in mm
        "y,g,r"           fill colors
        """
        self._classified_symbols(vv_x, vv_y, vv_z, scal_mm, zmin, zval.encode(), size.encode(), fcol.encode())
        




    def complex_polygon(self, vv_i, vv_x, vv_y):
        """
        Draw a polygon with holes in it.
        
        :param vv_i:   `GXVV <geosoft.gxapi.GXVV>` of type int holding the number of points for each polygon
        :param vv_x:   X coordinates.
        :param vv_y:   Y coordinates.
        :type  vv_i:   GXVV
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** You pass a `GXVV <geosoft.gxapi.GXVV>` with polygon sizes and 2 point vvs.
        """
        self._complex_polygon(vv_i, vv_x, vv_y)
        




    def ellipse(self, x, y, radius, ratio, angle):
        """
        Draw an ellipse
        
        :param x:       Center x
        :param y:       Center y
        :param radius:  Radius
        :param ratio:   Ratio x/y
        :param angle:   Angle
        :type  x:       float
        :type  y:       float
        :type  radius:  float
        :type  ratio:   float
        :type  angle:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._ellipse(x, y, radius, ratio, angle)
        




    def line(self, x0, y0, x1, y1):
        """
        Draw a line.
        
        :param x0:     X0
        :param y0:     Y0
        :param x1:     X1
        :param y1:     Y1
        :type  x0:     float
        :type  y0:     float
        :type  x1:     float
        :type  y1:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._line(x0, y0, x1, y1)
        




    def line_vv(self, gvv):
        """
        Draw line segments stored in a GS_D2LINE `GXVV <geosoft.gxapi.GXVV>`.
        
        :param gvv:    `GXVV <geosoft.gxapi.GXVV>` for GS_D2LINE
        :type  gvv:    GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._line_vv(gvv)
        




    def polygon_dm(self, vv_x, vv_y):
        """
        Like PolyLineDm, but draw polygons.
        
        :param vv_x:   X coordinates.
        :param vv_y:   Y coordinates.
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV

        .. versionadded:: 5.0.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._polygon_dm(vv_x, vv_y)
        




    def polygon_ply(self, ply):
        """
        Draw a complex polygon from `GXPLY <geosoft.gxapi.GXPLY>`.
        
        :type  ply:    GXPLY

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._polygon_ply(ply)
        




    def polygon_mply(self, mply):
        """
        Draw multiple complex polygons from `GXMPLY <geosoft.gxapi.GXMPLY>`.
        
        :type  mply:   GXMPLY

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._polygon_mply(mply)
        




    def poly_line(self, type, vv_x, vv_y):
        """
        Draw a polyline or polygon (dummies deleted).
        
        :param type:   :ref:`MVIEW_DRAW`
        :param vv_x:   X coordinates.
        :param vv_y:   Y coordinates.
        :type  type:   int
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Dummies in X and/or Y `GXVV <geosoft.gxapi.GXVV>` are deleted and it results
        in 'solid' line. Using `poly_line_dm <geosoft.gxapi.GXMVIEW.poly_line_dm>` (below) function
        if gaps from dummies are to be kept.
        """
        self._poly_line(type, vv_x, vv_y)
        




    def poly_line_dm(self, vv_x, vv_y):
        """
        Draw a polyline with gaps defined by dummies in X/Y VVs
        
        :param vv_x:   X coordinates.
        :param vv_y:   Y coordinates.
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._poly_line_dm(vv_x, vv_y)
        




    def poly_wrap(self, vv_x, vv_y):
        """
        Draw wrapped polylines from X and Y `GXVV <geosoft.gxapi.GXVV>`'s.
        
        :param vv_x:   X coordinates.
        :param vv_y:   Y coordinates.
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Convert a given VVy into a wrapped VVy using
        the current view window as the wrap region.
        Then draw polylines from it.

        .. seealso::

            `poly_line <geosoft.gxapi.GXMVIEW.poly_line>`
        """
        self._poly_wrap(vv_x, vv_y)
        




    def rectangle(self, x0, y0, x1, y1):
        """
        Draw a rectangle.
        
        :param x0:     X0
        :param y0:     Y0
        :param x1:     X1
        :param y1:     Y1
        :type  x0:     float
        :type  y0:     float
        :type  x1:     float
        :type  y1:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._rectangle(x0, y0, x1, y1)
        




    def segment(self, x, y, radius, ratio, angle, start, end):
        """
        Draw a filled segment of an ellipse.
        
        :param x:       Center x
        :param y:       Center y
        :param radius:  Radius
        :param ratio:   Ratio x/y
        :param angle:   Angle
        :param start:   Start angle
        :param end:     End angle
        :type  x:       float
        :type  y:       float
        :type  radius:  float
        :type  ratio:   float
        :type  angle:   float
        :type  start:   float
        :type  end:     float

        .. versionadded:: 5.0.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._segment(x, y, radius, ratio, angle, start, end)
        




    def size_symbols(self, vv_x, vv_y, vv_z):
        """
        Plot sized symbols
        
        :param vv_x:   X
        :param vv_y:   Y
        :param vv_z:   Symbol sizes (in view units)
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV
        :type  vv_z:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._size_symbols(vv_x, vv_y, vv_z)
        




    def symbol(self, x, y):
        """
        Plot a symbol
        
        :param x:      X
        :param y:      Y
        :type  x:      float
        :type  y:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._symbol(x, y)
        




    def symbols(self, vv_x, vv_y):
        """
        Plot symbols
        
        :param vv_x:   X
        :param vv_y:   Y
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._symbols(vv_x, vv_y)
        




    def symbols_itr(self, itr, vv_x, vv_y, vv_z):
        """
        Plot symbols using an `GXITR <geosoft.gxapi.GXITR>`
        
        :param itr:    `GXITR <geosoft.gxapi.GXITR>` file name (ZON or `GXITR <geosoft.gxapi.GXITR>`)
        :param vv_x:   X
        :param vv_y:   Y
        :param vv_z:   Z
        :type  itr:    str
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV
        :type  vv_z:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._symbols_itr(itr.encode(), vv_x, vv_y, vv_z)
        




    def text(self, text, x, y):
        """
        Draw text.
        
        :param text:   Text to plot
        :param x:      X location of text
        :param y:      Y location of text
        :type  text:   str
        :type  x:      float
        :type  y:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._text(text.encode(), x, y)
        




# Drawing Object



    def aggregate(self, agg, name):
        """
        Add an aggregate to a view.
        
        :param agg:    Aggregate
        :param name:   Aggregate name Maximum length is `MVIEW_NAME_LENGTH <geosoft.gxapi.MVIEW_NAME_LENGTH>`
        :type  agg:    GXAGG
        :type  name:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._aggregate(agg, name.encode())
        




    def get_aggregate(self, group):
        """
        Get an existing Aggregate object from the view.
        
        :param group:  Group number
        :type  group:  int

        :returns:      `GXAGG <geosoft.gxapi.GXAGG>` object
        :rtype:        GXAGG

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method returns a cached object owned by the `GXMVIEW <geosoft.gxapi.GXMVIEW>` and will be destroyed automatically when the `GXMVIEW <geosoft.gxapi.GXMVIEW>` is disposed
        """
        ret_val = self._get_aggregate(group)
        return GXAGG(ret_val)




    def change_line_message(self, line):
        """
        Change the specified line in a view.
        
        :param line:   Change to this line
        :type  line:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The line name can be created by calling LineLabel_DB using
        `DB_LINE_LABEL_FORMAT_LINK <geosoft.gxapi.DB_LINE_LABEL_FORMAT_LINK>`. This insures that the label is
        created is the same way as used in the database.
        """
        self._change_line_message(line.encode())
        




    def col_symbol(self, name, csymb):
        """
        Add a colored symbol object to a view.
        
        :param name:   Name of the color symbol group
        :param csymb:  `GXCSYMB <geosoft.gxapi.GXCSYMB>` object
        :type  name:   str
        :type  csymb:  GXCSYMB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._col_symbol(name.encode(), csymb)
        




    def get_col_symbol(self, group):
        """
        Get an existing colored symbol object from the view.
        
        :param group:  Group number
        :type  group:  int

        :returns:      `GXCSYMB <geosoft.gxapi.GXCSYMB>` object
        :rtype:        GXCSYMB

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method returns a cached object owned by the `GXMVIEW <geosoft.gxapi.GXMVIEW>` and will be destroyed automatically when the `GXMVIEW <geosoft.gxapi.GXMVIEW>` is disposed
        """
        ret_val = self._get_col_symbol(group)
        return GXCSYMB(ret_val)




    def datalinkd(self, datalinkd, name):
        """
        Add a Data Link Display (`GXDATALINKD <geosoft.gxapi.GXDATALINKD>`) object to the view.
        
        :param name:       Name Maximum length is `MVIEW_NAME_LENGTH <geosoft.gxapi.MVIEW_NAME_LENGTH>`
        :type  datalinkd:  GXDATALINKD
        :type  name:       str

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._datalinkd(datalinkd, name.encode())
        




    def get_datalinkd(self, group):
        """
        Get an existing Data Link Display (`GXDATALINKD <geosoft.gxapi.GXDATALINKD>`) object from the view.
        
        :param group:  Group number
        :type  group:  int

        :returns:      `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object
        :rtype:        GXDATALINKD

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method returns a cached object owned by the `GXMVIEW <geosoft.gxapi.GXMVIEW>` and will be destroyed automatically when the `GXMVIEW <geosoft.gxapi.GXMVIEW>` is disposed
        """
        ret_val = self._get_datalinkd(group)
        return GXDATALINKD(ret_val)




    def easy_maker(self, name, groups):
        """
        Used for GX makers which use both maps and databases.
        
        :param name:    Maker name, used in menu prompt
        :param groups:  INI groups (terminate each with a ";")
        :type  name:    str
        :type  groups:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._easy_maker(name.encode(), groups.encode())
        




    def get_maker_name(self, group, str_val):
        """
        Used to retrieve the maker for a particular view group.
        
        :param group:    Group number
        :param str_val:  String in which to place the maker name
        :type  group:    int
        :type  str_val:  str_ref

        .. versionadded:: 9.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        str_val.value = self._get_maker_name(group, str_val.value.encode())
        




    def emf_object(self, min_x, min_y, max_x, max_y, file):
        """
        Add an EMF file data object to the view.
        
        :param min_x:  Min X
        :param min_y:  Min Y
        :param max_x:  Max X
        :param max_y:  Max Y
        :param file:   EMF File holding data
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float
        :type  file:   str

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._emf_object(min_x, min_y, max_x, max_y, file.encode())
        




    def external_string_object(self, min_x, min_y, max_x, max_y, name, cl, data):
        """
        Add an external string data object to the view.
        
        :param min_x:  Min X
        :param min_y:  Min Y
        :param max_x:  Max X
        :param max_y:  Max Y
        :param name:   Name of external object
        :param cl:     Class of external object
        :param data:   String data of external object
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float
        :type  name:   str
        :type  cl:     str
        :type  data:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._external_string_object(min_x, min_y, max_x, max_y, name.encode(), cl.encode(), data.encode())
        




    def link(self, db, name):
        """
        Make a link to a database.
        
        :param db:     Database handle
        :param name:   Link name
        :type  db:     GXDB
        :type  name:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._link(db, name.encode())
        




    def maker(self, db, map, prog, type, name, groups):
        """
        Generates a Maker for the database and/or map.
        
        :param db:      Database required? (0 = No, 1 = Yes)
        :param map:     Map required?      (0 = No, 1 = Yes)
        :param prog:    Program name
        :param type:    :ref:`MAKER`
        :param name:    Maker name, used in menu prompt
        :param groups:  INI groups (terminate each with a ";")
        :type  db:      int
        :type  map:     int
        :type  prog:    str
        :type  type:    int
        :type  name:    str
        :type  groups:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._maker(db, map, prog.encode(), type, name.encode(), groups.encode())
        




    def meta(self, meta, name):
        """
        Store Metadata in a group
        
        :param meta:   `GXMETA <geosoft.gxapi.GXMETA>` object
        :param name:   Menu name of Object
        :type  meta:   GXMETA
        :type  name:   str

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._meta(meta, name.encode())
        




    def voxd(self, voxd, name):
        """
        Add a Voxel Display (`GXVOXD <geosoft.gxapi.GXVOXD>`) object to the view.
        
        :param name:   Name Maximum length is `MVIEW_NAME_LENGTH <geosoft.gxapi.MVIEW_NAME_LENGTH>`
        :type  voxd:   GXVOXD
        :type  name:   str

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._voxd(voxd, name.encode())
        




    def get_voxd(self, group):
        """
        Get an existing `GXVOXD <geosoft.gxapi.GXVOXD>` object from the view.
        
        :param group:  Group number
        :type  group:  int

        :returns:      `GXVOXD <geosoft.gxapi.GXVOXD>` object
        :rtype:        GXVOXD

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method returns a cached object owned by the `GXMVIEW <geosoft.gxapi.GXMVIEW>` and will be destroyed automatically when the `GXMVIEW <geosoft.gxapi.GXMVIEW>` is disposed
        """
        ret_val = self._get_voxd(group)
        return GXVOXD(ret_val)




    def draw_vector_voxel_vectors(self, vox, group, itr, scale_factor, height_base_ratio, max_base_size_ratio, cutoff_value, max_vectors):
        """
        Display vectors from a vector voxel in the view.
        
        :param group:                View group name Maximum length is `MVIEW_NAME_LENGTH <geosoft.gxapi.MVIEW_NAME_LENGTH>`
        :param itr:                  Image transform - must contain zones
        :param scale_factor:         Vector length scale factor - w.r.t. the voxel minimum horizontal cell size (default 1)
        :param height_base_ratio:    Ratio of the vector cone height to its base (default 4)
        :param max_base_size_ratio:  Ratio of maximum base size to minimum horizontal cell size (default 0.25)
        :param cutoff_value:         Cutoff value - do not plot vectors with amplitudes less than this value (`rDUMMY <geosoft.gxapi.rDUMMY>` or 0 to plot all)
        :param max_vectors:          Maximum number of vectors - decimate as required to reduce (`iDUMMY <geosoft.gxapi.iDUMMY>` to plot all)
        :type  vox:                  GXVOX
        :type  group:                str
        :type  itr:                  GXITR
        :type  scale_factor:         float
        :type  height_base_ratio:    float
        :type  max_base_size_ratio:  float
        :type  cutoff_value:         float
        :type  max_vectors:          int

        .. versionadded:: 7.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This will result in a `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>` group object within the view
        """
        self._draw_vector_voxel_vectors(vox, group.encode(), itr, scale_factor, height_base_ratio, max_base_size_ratio, cutoff_value, max_vectors)
        




    def get_vector_3d(self, group):
        """
        Get an existing `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>` object from the view.
        
        :param group:  Group number
        :type  group:  int

        :returns:      `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>` object
        :rtype:        GXVECTOR3D

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method returns a cached object owned by the `GXMVIEW <geosoft.gxapi.GXMVIEW>` and will be destroyed automatically when the `GXMVIEW <geosoft.gxapi.GXMVIEW>` is disposed
        """
        ret_val = self._get_vector_3d(group)
        return GXVECTOR3D(ret_val)




    def draw_vectors_3d(self, group, vv_x, vv_y, vv_z, vv_vx, vv_vy, vv_vz, itr, scale_for_max_vector, height_base_ratio, max_base_size_ratio):
        """
        Display vectors in the view.
        
        :param group:                 View group name Maximum length is `MVIEW_NAME_LENGTH <geosoft.gxapi.MVIEW_NAME_LENGTH>`
        :param vv_x:                  X locations
        :param vv_y:                  Y locations
        :param vv_z:                  Z locations
        :param vv_vx:                 Vector X component
        :param vv_vy:                 Vector Y component
        :param vv_vz:                 Vector Z component
        :param itr:                   Image transform - must contain zones
        :param scale_for_max_vector:  Scale factor for the longest vector in map units / vector units. Vector lengths for the rest of the vectors scale by the square root of the vector amplitudes.
                                      This results in the apparent (viewed) area of the vector being proportional to the amplitude.
        :param height_base_ratio:     Ratio of the vector cone height to its base (default 4)
        :param max_base_size_ratio:   Maximum base size in view units. Leave blank (dummy) for no limit. If applied this can make larger vectors skinnier, but does not reduce the length, so they don't obscure other vectors as much.
        :type  group:                 str
        :type  vv_x:                  GXVV
        :type  vv_y:                  GXVV
        :type  vv_z:                  GXVV
        :type  vv_vx:                 GXVV
        :type  vv_vy:                 GXVV
        :type  vv_vz:                 GXVV
        :type  itr:                   GXITR
        :type  scale_for_max_vector:  float
        :type  height_base_ratio:     float
        :type  max_base_size_ratio:   float

        .. versionadded:: 8.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._draw_vectors_3d(group.encode(), vv_x, vv_y, vv_z, vv_vx, vv_vy, vv_vz, itr, scale_for_max_vector, height_base_ratio, max_base_size_ratio)
        




# Group Methods



    def set_group_itr(self, group, itr):
        """
        Set group `GXITR <geosoft.gxapi.GXITR>`
        
        :param group:  Group number
        :type  group:  int
        :type  itr:    GXITR

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A group `GXITR <geosoft.gxapi.GXITR>` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._set_group_itr(group, itr)
        




    def get_group_itr(self, group):
        """
        Get group `GXITR <geosoft.gxapi.GXITR>`
        
        :param group:  Group number
        :type  group:  int
        :rtype:        GXITR

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A group `GXITR <geosoft.gxapi.GXITR>` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._get_group_itr(group)
        return GXITR(ret_val)




    def group_itr_exists(self, group):
        """
        Determine if group `GXITR <geosoft.gxapi.GXITR>` exists.
        
        :param group:  Group number
        :type  group:  int

        :returns:      1 - `GXITR <geosoft.gxapi.GXITR>` exists, 0 - `GXITR <geosoft.gxapi.GXITR>` does not exist
        :rtype:        int

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A group `GXITR <geosoft.gxapi.GXITR>` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._group_itr_exists(group)
        return ret_val




    def delete_group_itr(self, group):
        """
        Deletes existing `GXITR <geosoft.gxapi.GXITR>` associated with a group.
        
        :param group:  Group number
        :type  group:  int

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A group `GXITR <geosoft.gxapi.GXITR>` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._delete_group_itr(group)
        




    def set_group_tpat(self, group, tpat):
        """
        Set group `GXTPAT <geosoft.gxapi.GXTPAT>`
        
        :param group:  Group number
        :type  group:  int
        :type  tpat:   GXTPAT

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A group `GXTPAT <geosoft.gxapi.GXTPAT>` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._set_group_tpat(group, tpat)
        




    def get_group_tpat(self, group):
        """
        Get group `GXTPAT <geosoft.gxapi.GXTPAT>`
        
        :param group:  Group number
        :type  group:  int
        :rtype:        GXTPAT

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A group `GXTPAT <geosoft.gxapi.GXTPAT>` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._get_group_tpat(group)
        return GXTPAT(ret_val)




    def group_tpat_exists(self, group):
        """
        Determine if group `GXTPAT <geosoft.gxapi.GXTPAT>` exists.
        
        :param group:  Group number
        :type  group:  int

        :returns:      1 - `GXTPAT <geosoft.gxapi.GXTPAT>` exists, 0 - `GXTPAT <geosoft.gxapi.GXTPAT>` does not exist
        :rtype:        int

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A group `GXTPAT <geosoft.gxapi.GXTPAT>` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        ret_val = self._group_tpat_exists(group)
        return ret_val




    def delete_group_tpat(self, group):
        """
        Deletes existing `GXTPAT <geosoft.gxapi.GXTPAT>` associated with a group.
        
        :param group:  Group number
        :type  group:  int

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A group `GXTPAT <geosoft.gxapi.GXTPAT>` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
        Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
        to refresh the objects.
        """
        self._delete_group_tpat(group)
        




    def group_storage_exists(self, group, storage_name):
        """
        Determine if generic storage associated with a group exists.
        
        :param group:         Group number
        :param storage_name:  Storage name
        :type  group:         int
        :type  storage_name:  str

        :returns:             1 - storage exists, 0 - storage does not exist
        :rtype:               int

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** External API users should not use storage names starting with "Geosoft"
        """
        ret_val = self._group_storage_exists(group, storage_name.encode())
        return ret_val




    def read_group_storage(self, group, storage_name):
        """
        Reads existing generic storage associated with a group into an in-memory `GXBF <geosoft.gxapi.GXBF>`.
        
        :param group:         Group number
        :param storage_name:  Storage name
        :type  group:         int
        :type  storage_name:  str

        :returns:             `GXBF <geosoft.gxapi.GXBF>` Object
        :rtype:               GXBF

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** External API users should not use storage names starting with "Geosoft"
        """
        ret_val = self._read_group_storage(group, storage_name.encode())
        return GXBF(ret_val)




    def delete_group_storage(self, group, storage_name):
        """
        Deletes existing generic storage associated with a group.
        
        :param group:         Group number
        :param storage_name:  Storage name
        :type  group:         int
        :type  storage_name:  str

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** External API users should not use storage names starting with "Geosoft"
        """
        self._delete_group_storage(group, storage_name.encode())
        




    def write_group_storage(self, group, storage_name, bf):
        """
        Open generic existing storage associated with a group for reading.
        
        :param group:         Group number
        :param storage_name:  Storage name
        :param bf:            `GXBF <geosoft.gxapi.GXBF>` to read from
        :type  group:         int
        :type  storage_name:  str
        :type  bf:            GXBF

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** External API users should not use storage names starting with "Geosoft"
        """
        self._write_group_storage(group, storage_name.encode(), bf)
        




    def copy_marked_groups(self, mvie_wd):
        """
        Copies all marked groups from one view into another view
        
        :param mvie_wd:  Destination `GXMVIEW <geosoft.gxapi.GXMVIEW>`
        :type  mvie_wd:  GXMVIEW

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Projections in source and destination views are used to copy the
        entities. Entities are clipped by the destination view's clipping
        region.
        """
        self._copy_marked_groups(mvie_wd)
        




    def copy_raw_marked_groups(self, mvie_wd):
        """
        Copies all marked groups raw from one view into another
        
        :param mvie_wd:  Destination `GXMVIEW <geosoft.gxapi.GXMVIEW>`
        :type  mvie_wd:  GXMVIEW

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The projections, and clipping is completly ignored.
        """
        self._copy_raw_marked_groups(mvie_wd)
        




    def crc_group(self, name, crc):
        """
        Compute CRC for a group.
        
        :param name:   Group name
        :param crc:    CRC to start (use `CRC_INIT_VALUE <geosoft.gxapi.CRC_INIT_VALUE>`)
        :type  name:   str
        :type  crc:    int
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._crc_group(name.encode(), crc)
        return ret_val




    def delete_group(self, group):
        """
        Delete a group.
        
        :param group:  Group name
        :type  group:  str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Does nothing if the group does not already exist.
        """
        self._delete_group(group.encode())
        




    def del_marked_groups(self):
        """
        Delete marked groups.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._del_marked_groups()
        




    def get_group_extent(self, group_name, xmin, ymin, xmax, ymax, unit):
        """
        Get extent of a group in a view
        
        :param group_name:  Group name
        :param xmin:        Minimum X, returned
        :param ymin:        Minimum Y, returned
        :param xmax:        Maximum X, returned
        :param ymax:        Maximum Y, returned
        :param unit:        :ref:`MVIEW_UNIT`
        :type  group_name:  str
        :type  xmin:        float_ref
        :type  ymin:        float_ref
        :type  xmax:        float_ref
        :type  ymax:        float_ref
        :type  unit:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        xmin.value, ymin.value, xmax.value, ymax.value = self._get_group_extent(group_name.encode(), xmin.value, ymin.value, xmax.value, ymax.value, unit)
        




    def get_group_transparency(self, group_name, trans):
        """
        Gets the transparency value of group
        
        :param group_name:  Group name
        :param trans:       Transparency (1.0 - Opaque, 0.0 - Transparent)
        :type  group_name:  str
        :type  trans:       float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        trans.value = self._get_group_transparency(group_name.encode(), trans.value)
        




    def group_to_ply(self, name, pply):
        """
        Save all polygons in group into `GXPLY <geosoft.gxapi.GXPLY>` obj.
        
        :param name:   Group name
        :param pply:   `GXPLY <geosoft.gxapi.GXPLY>` to add to
        :type  name:   str
        :type  pply:   GXPLY

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The coordinates will be in the working coordinate system
        of the view.  The SetWorkingIPJ_MVIEW method can be used
        to change the working coordinate system. This function will
        return an empty `GXPLY <geosoft.gxapi.GXPLY>` if the group is hidden.
        """
        self._group_to_ply(name.encode(), pply)
        




    def hide_marked_groups(self, mode):
        """
        Hide/Show marked groups.
        
        :param mode:   :ref:`MVIEW_HIDE`
        :type  mode:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._hide_marked_groups(mode)
        




    def hide_shadow_2d_interpretations(self, mode):
        """
        Hide/Show 2d shadow interpretations.
        
        :param mode:   :ref:`MVIEW_HIDE`
        :type  mode:   int

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._hide_shadow_2d_interpretations(mode)
        




    def exist_group(self, name):
        """
        Checks to see if a group exists.
        
        :param name:   Group name
        :type  name:   str

        :returns:      0  - group does not exist.
                       1  - group exists.
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._exist_group(name.encode())
        return ret_val




    def gen_new_group_name(self, group, new_name):
        """
        Generate the name of a group from a base name that
        is new. (always unique and won't overwrite existing
        objects).
        
        :param group:     Base Name of group
        :param new_name:  New Name of group
        :type  group:     str
        :type  new_name:  str_ref

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        new_name.value = self._gen_new_group_name(group.encode(), new_name.value.encode())
        




    def is_group(self, group, what):
        """
        Query a status or characteristic of a group
        
        :param group:  Group name
        :param what:   :ref:`MVIEW_IS`
        :type  group:  str
        :type  what:   int

        :returns:      TRUE or FALSE (1 or 0)
        :rtype:        int

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_group(group.encode(), what)
        return ret_val




    def is_group_empty(self, group):
        """
        Is the group empty?
        
        :param group:  Group name
        :type  group:  str

        :returns:      TRUE or FALSE (1 or 0)
        :rtype:        int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_group_empty(group.encode())
        return ret_val




    def is_movable(self):
        """
        Is this view movable?
        
        :rtype:        bool

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Views are always physically movable in the API, this
        flag is for preventing accidental moving in the `GXGUI <geosoft.gxapi.GXGUI>`.
        By default views are not movable.
        """
        ret_val = self._is_movable()
        return ret_val




    def is_visible(self):
        """
        Is this view visible?
        
        :rtype:        bool

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_visible()
        return ret_val




    def list_groups(self, lst, flag):
        """
        Get a list of the groups in a view.
        
        :param lst:    List
        :param flag:   :ref:`MVIEW_GROUP_LIST`
        :type  lst:    GXLST
        :type  flag:   int

        :returns:      Number of groups in the list
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._list_groups(lst, flag)
        return ret_val




    def render_order(self):
        """
        Query the view render order
        

        :returns:      Render order
        :rtype:        int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Views with lower numbers should render first, `iDUMMY <geosoft.gxapi.iDUMMY>` is undefined
        """
        ret_val = self._render_order()
        return ret_val




    def is_group_exportable(self, group):
        """
        Query whether the group is an exportable type.
        
        :param group:  Group name
        :type  group:  str

        :returns:      TRUE or FALSE (1 or 0)
        :rtype:        int

        .. versionadded:: 9.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_group_exportable(group.encode())
        return ret_val




    def mark_all_groups(self, mark):
        """
        Mark or unmark all groups.
        
        :param mark:   0 - unmark, 1 - mark
        :type  mark:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._mark_all_groups(mark)
        




    def mark_empty_groups(self, mark):
        """
        Mark/unmark all empty groups.
        
        :param mark:   0 - unmark, 1 - mark
        :type  mark:   int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._mark_empty_groups(mark)
        




    def mark_group(self, name, mark):
        """
        Mark or unmark a specific group
        
        :param name:   Group name
        :param mark:   0 - unmark, 1 - mark
        :type  name:   str
        :type  mark:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._mark_group(name.encode(), mark)
        




    def move_group_backward(self, group):
        """
        Move the group backward one position (render sooner).
        
        :param group:  Group name
        :type  group:  str

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._move_group_backward(group.encode())
        




    def move_group_forward(self, group):
        """
        Move the group forward one position (render later).
        
        :param group:  Group name
        :type  group:  str

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._move_group_forward(group.encode())
        




    def move_group_to_back(self, group):
        """
        Move the group to the back (render first).
        
        :param group:  Group name
        :type  group:  str

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._move_group_to_back(group.encode())
        




    def move_group_to_front(self, group):
        """
        Move the group to the front (render last).
        
        :param group:  Group name
        :type  group:  str

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._move_group_to_front(group.encode())
        




    def rename_group(self, old, new_group_name):
        """
        Rename a group.
        
        :param old:             Old group name
        :param new_group_name:  New group name
        :type  old:             str
        :type  new_group_name:  str

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Does nothing if the group does not already exist.
        """
        self._rename_group(old.encode(), new_group_name.encode())
        




    def set_group_moveable(self, group, move):
        """
        Set the movable attribute of a group.
        
        :param group:  Group name
        :param move:   0 - not movable, 1 - movable
        :type  group:  str
        :type  move:   int

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_group_moveable(group.encode(), move)
        




    def set_group_transparency(self, group_name, trans):
        """
        Sets the transparency value of group
        
        :param group_name:  Group name
        :param trans:       Transparency  (1.0 - Opaque, 0.0 - Transparent)
        :type  group_name:  str
        :type  trans:       float

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_group_transparency(group_name.encode(), trans)
        




    def set_mark_moveable(self, move):
        """
        Set the movable attribute of marked groups.
        
        :param move:   0 - not movable, 1 - movable
        :type  move:   int

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_mark_moveable(move)
        




    def set_movability(self, movable):
        """
        Set the view movability
        
        :type  movable:  bool

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Views are always physically movable in the API, this
        flag is for preventing accidental moving in the `GXGUI <geosoft.gxapi.GXGUI>`.
        By default views are not movable.
        """
        self._set_movability(movable)
        




    def set_render_order(self, order):
        """
        Set the view render order
        
        :param order:  Render order
        :type  order:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Views with lower numbers should render first, `iDUMMY <geosoft.gxapi.iDUMMY>` is undefined
        """
        self._set_render_order(order)
        




    def set_visibility(self, visible):
        """
        Set the view visibility
        
        :type  visible:  bool

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_visibility(visible)
        




    def start_group(self, name, mode):
        """
        Start a group.
        
        :param name:   Group name, can be NULL, Maximum length is `MVIEW_NAME_LENGTH <geosoft.gxapi.MVIEW_NAME_LENGTH>`
        :param mode:   :ref:`MVIEW_GROUP`
        :type  name:   str
        :type  mode:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Line and fill colors and thickness must be set
        before drawing to a group.

        If the group name is NULL, output will be sent to
        the primary group stream and the :ref:`MVIEW_GROUP` is
        ignored.

        Group names must be different from view names.
        """
        self._start_group(name.encode(), mode)
        




    def get_group_guid(self, group, guid):
        """
        Gets a GUID of a group in the `GXMVIEW <geosoft.gxapi.GXMVIEW>`.
        
        :param group:  Group number
        :param guid:   GUID
        :type  group:  int
        :type  guid:   str_ref

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If a GUID was never queried a new one will be assigned and the map will be modified. Only if the map is saved will this value then persist.
        """
        guid.value = self._get_group_guid(group, guid.value.encode())
        




    def find_group_by_guid(self, guid):
        """
        Find a Group by name.
        
        :param guid:   GUID
        :type  guid:   str

        :returns:      Group Number.
        :rtype:        int

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._find_group_by_guid(guid.encode())
        return ret_val




# Projection



    def set_working_ipj(self, ipj):
        """
        Set the working projection of the view.
        
        :param ipj:    The input projection
        :type  ipj:    GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The working projection is the coordinate system of coordinates drawn to
        the view.  The working coordinate system can be different than the view
        coordinate system, in which case the coordinates are re-projected to the
        view coordinate system before they are placed in the view.

        .. seealso::

            `mode_pj <geosoft.gxapi.GXMVIEW.mode_pj>` to control use of the working projection.
        """
        self._set_working_ipj(ipj)
        




    def clear_esrild_ts(self):
        """
        Clear ESRI local datum transformations currently in use.
        

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._clear_esrild_ts()
        




    def is_projection_empty(self):
        """
        Returns 1 if the view projection and view user projection are both empty (undefined).
        

        :returns:      1 if the view projection and view user projection are both empty.
        :rtype:        int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use, for instance, to see if the map view contains projection information. The first time you add data that
        has projection information you should set up an empty view projection so that subsequent data added with a different
        projection is properly displayed in relation to the initial data.
        """
        ret_val = self._is_projection_empty()
        return ret_val




    def get_ipj(self, ipj):
        """
        Get the projection of the view.
        
        :param ipj:    `GXIPJ <geosoft.gxapi.GXIPJ>` in which to place the view `GXIPJ <geosoft.gxapi.GXIPJ>`
        :type  ipj:    GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_ipj(ipj)
        




    def get_user_ipj(self, ipj):
        """
        Get the user projection of the view.
        
        :param ipj:    `GXIPJ <geosoft.gxapi.GXIPJ>` in which to place the view `GXIPJ <geosoft.gxapi.GXIPJ>`
        :type  ipj:    GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_user_ipj(ipj)
        




    def mode_pj(self, mode):
        """
        Set the working projection mode
        
        :param mode:   :ref:`MVIEW_PJ`
        :type  mode:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This controls how your coordinates and attributes will be interpreted.
        A working projection must be set useing SetWorkingIPJ_MVIEW for this
        method to have any effect.

        .. seealso::

            SetWorkingIPJ
        """
        self._mode_pj(mode)
        




    def north(self):
        """
        Returns North direction at center of view.
        

        :returns:      North direction id deg. azimuth relative to view Y.
        :rtype:        float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** North is calculated from the `GXIPJ <geosoft.gxapi.GXIPJ>` North direction.
        It will be `rDUMMY <geosoft.gxapi.rDUMMY>` if `GXIPJ <geosoft.gxapi.GXIPJ>` is unknown.
        """
        ret_val = self._north()
        return ret_val




    def set_ipj(self, ipj):
        """
        Set the projection of the view.
        
        :param ipj:    `GXIPJ <geosoft.gxapi.GXIPJ>` to place in the view
        :type  ipj:    GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function also sets the User `GXIPJ <geosoft.gxapi.GXIPJ>`,
        and automatically clears the WARP before doing so.
        This would be equivalent to calling :func:`_ClearWarp_IPJ'
        followed by `set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>` on the view.
        """
        self._set_ipj(ipj)
        




    def set_user_ipj(self, ipj):
        """
        Set the user projection of the view.
        
        :param ipj:    `GXIPJ <geosoft.gxapi.GXIPJ>` to place in the view
        :type  ipj:    GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_user_ipj(ipj)
        




# Render



    def get_3d_group_flags(self, group_num):
        """
        Get a 3D geometry group's 3D rendering flags.
        
        :param group_num:  Group number
        :type  group_num:  int

        :returns:          Combination of :ref:`MVIEW_3D_RENDER` flags or 0
        :rtype:            int

        .. versionadded:: 9.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_3d_group_flags(group_num)
        return ret_val




    def set_3d_group_flags(self, group_num, flags):
        """
        Set a 3D geometry group's 3D rendering flags.
        
        :param group_num:  Group number
        :param flags:      Combination of :ref:`MVIEW_3D_RENDER` flags or 0
        :type  group_num:  int
        :type  flags:      int

        .. versionadded:: 9.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_3d_group_flags(group_num, flags)
        




    def get_group_freeze_scale(self, group_num, scale):
        """
        Get a scale freezing value for the group (`rDUMMY <geosoft.gxapi.rDUMMY>` for disabled).
        
        :param group_num:  Group number
        :param scale:      Variable to fill with freeze scale
        :type  group_num:  int
        :type  scale:      float_ref

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        scale.value = self._get_group_freeze_scale(group_num, scale.value)
        




    def set_freeze_scale(self, scale):
        """
        Set a scale freezing value into stream (`rDUMMY <geosoft.gxapi.rDUMMY>` for disabled).
        
        :param scale:  Freeze Scale value
        :type  scale:  float

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Objects written after this will override any scale freezing set for the group
        """
        self._set_freeze_scale(scale)
        




    def set_group_freeze_scale(self, group_num, scale):
        """
        Set a scale freezing value for the group (`rDUMMY <geosoft.gxapi.rDUMMY>` for disabled).
        
        :param group_num:  Group number
        :param scale:      Variable to fill with freeze scale
        :type  group_num:  int
        :type  scale:      float

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_group_freeze_scale(group_num, scale)
        




    def find_group(self, group_name):
        """
        Find a Group by name.
        
        :param group_name:  Group name
        :type  group_name:  str

        :returns:           Group Number.
        :rtype:             int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._find_group(group_name.encode())
        return ret_val




    def group_name(self, group_num, group_name):
        """
        Get a group name
        
        :param group_num:   Group number, error if not valid
        :param group_name:  Group Name
        :type  group_num:   int
        :type  group_name:  str_ref

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        group_name.value = self._group_name(group_num, group_name.value.encode())
        




    def render(self, hdc, left, bottom, right, top, min_x, min_y, max_x, max_y):
        """
        Render a specified area of view onto a Windows DC handle
        
        :param hdc:     DC Handle
        :param left:    Left value of the render rect in Windows coordinates (bottom>top)
        :param bottom:  Bottom value
        :param right:   Right value
        :param top:     Top value
        :param min_x:   Area X minimum
        :param min_y:   Area Y minimum
        :param max_x:   Area X maximum
        :param max_y:   Area Y maximum
        :type  hdc:     int
        :type  left:    int
        :type  bottom:  int
        :type  right:   int
        :type  top:     int
        :type  min_x:   float
        :type  min_y:   float
        :type  max_x:   float
        :type  max_y:   float

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._render(hdc, left, bottom, right, top, min_x, min_y, max_x, max_y)
        




# Utility Drawing



    def set_u_fac(self, hdc):
        """
        Set the unit conversion of a view.
        
        :param hdc:    New UFac value
        :type  hdc:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_u_fac(hdc)
        




    def axis_x(self, y_loc, left, right, major_tick, minor_tick, tick_size):
        """
        Draw an X axis
        
        :param y_loc:       Y location in view units
        :param left:        Left  X
        :param right:       Right X
        :param major_tick:  Major tick interval
        :param minor_tick:  Minor tick interval (half size of major)
        :param tick_size:   Tick size in view units (negative for down ticks)
        :type  y_loc:       float
        :type  left:        float
        :type  right:       float
        :type  major_tick:  float
        :type  minor_tick:  float
        :type  tick_size:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All coordinates are in view units.

        .. seealso::

            rOptimumTick_MVIEW
        """
        self._axis_x(y_loc, left, right, major_tick, minor_tick, tick_size)
        




    def axis_y(self, x_loc, bottom, top, major_tick, minor_tick, tick_size):
        """
        Draw a  Y axis
        
        :param x_loc:       X location in view units
        :param bottom:      Bottom Y
        :param top:         Top    Y
        :param major_tick:  Major tick interval
        :param minor_tick:  Minor tick interval (half size of major)
        :param tick_size:   Tick size in view units (negative for left ticks)
        :type  x_loc:       float
        :type  bottom:      float
        :type  top:         float
        :type  major_tick:  float
        :type  minor_tick:  float
        :type  tick_size:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All coordinates are in view units.

        .. seealso::

            rOptimumTick_MVIEW
        """
        self._axis_y(x_loc, bottom, top, major_tick, minor_tick, tick_size)
        




    def grid(self, x_inc, y_inc, dx, dy, grid_type):
        """
        Draw a grid in the current window
        
        :param x_inc:      X grid increment
        :param y_inc:      Y grid increment
        :param dx:         dX dot increment/cross X size
        :param dy:         dY dot increment/cross Y size
        :param grid_type:  :ref:`MVIEW_GRID`
        :type  x_inc:      float
        :type  y_inc:      float
        :type  dx:         float
        :type  dy:         float
        :type  grid_type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The grid will be drawn in the current window specified
        by the last SetWindow call.

        .. seealso::

            `axis_x <geosoft.gxapi.GXMVIEW.axis_x>`, `axis_y <geosoft.gxapi.GXMVIEW.axis_y>`, `optimum_tick <geosoft.gxapi.GXMVIEW.optimum_tick>`
        """
        self._grid(x_inc, y_inc, dx, dy, grid_type)
        




    def label_fid(self, vv_x, fid_start, fid_incr, interval, y_loc, y_scale):
        """
        Label fiducials on a profile
        
        :param vv_x:       X `GXVV <geosoft.gxapi.GXVV>`
        :param fid_start:  Fiducial start
        :param fid_incr:   Fiducial increment
        :param interval:   Fiducial label interval, default 100.0
        :param y_loc:      Y location in view unit
        :param y_scale:    Y scale
        :type  vv_x:       GXVV
        :type  fid_start:  float
        :type  fid_incr:   float
        :type  interval:   float
        :type  y_loc:      float
        :type  y_scale:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A 1mm long vertical tick is drawn at the place
        where a label is present. The label is drawn
        below the tick.

        The incoming X `GXVV <geosoft.gxapi.GXVV>` is used to define the place for
        label.
        """
        self._label_fid(vv_x, fid_start, fid_incr, interval, y_loc, y_scale)
        




    def label_x(self, l_loc, left, right, lable_int, just, bound, orient):
        """
        Label annotations on the X axis
        
        :param l_loc:      Y location in view units
        :param left:       Left  X
        :param right:      Right X
        :param lable_int:  Label interval
        :param just:       :ref:`MVIEW_LABEL_JUST`
        :param bound:      :ref:`MVIEW_LABEL_BOUND`
        :param orient:     :ref:`MVIEW_LABEL_ORIENT`
        :type  l_loc:      float
        :type  left:       float
        :type  right:      float
        :type  lable_int:  float
        :type  just:       int
        :type  bound:      int
        :type  orient:     int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Label bounding will justify edge labels to be inside
        the bar limits. But bounding does not apply if
        labels are drawn vertically (top right or top left)

        .. seealso::

            `axis_x <geosoft.gxapi.GXMVIEW.axis_x>`, `axis_y <geosoft.gxapi.GXMVIEW.axis_y>`, `optimum_tick <geosoft.gxapi.GXMVIEW.optimum_tick>`
        """
        self._label_x(l_loc, left, right, lable_int, just, bound, orient)
        




    def label_y(self, x, bottom, top, lable_int, just, bound, orient):
        """
        Label annotations on the Y axis
        
        :param x:          X location in view units
        :param bottom:     Bottom Y
        :param top:        Top    Y
        :param lable_int:  Label interval
        :param just:       :ref:`MVIEW_LABEL_JUST`
        :param bound:      :ref:`MVIEW_LABEL_BOUND`
        :param orient:     :ref:`MVIEW_LABEL_ORIENT`
        :type  x:          float
        :type  bottom:     float
        :type  top:        float
        :type  lable_int:  float
        :type  just:       int
        :type  bound:      int
        :type  orient:     int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Label bounding will justify edge labels to be inside
        the bar limits. But bounding does not apply if
        labels are drawn vertically (top right or top left)

        .. seealso::

            `axis_x <geosoft.gxapi.GXMVIEW.axis_x>`, `axis_y <geosoft.gxapi.GXMVIEW.axis_y>`, `optimum_tick <geosoft.gxapi.GXMVIEW.optimum_tick>`
        """
        self._label_y(x, bottom, top, lable_int, just, bound, orient)
        



    @classmethod
    def optimum_tick(cls, min, max, sep):
        """
        Return a default optimum tick interval
        
        :param min:  Minimum of range
        :param max:  Maximum
        :param sep:  Optimum interval
        :type  min:  float
        :type  max:  float
        :type  sep:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        sep.value = gxapi_cy.WrapMVIEW._optimum_tick(GXContext._get_tls_geo(), min, max, sep.value)
        




# View


    @classmethod
    def create(cls, map, name, mode):
        """
        Create `GXMVIEW <geosoft.gxapi.GXMVIEW>`.
        
        :param map:   `GXMAP <geosoft.gxapi.GXMAP>` on which to place the view
        :param name:  View name (maximum `MVIEW_NAME_LENGTH <geosoft.gxapi.MVIEW_NAME_LENGTH>`)
        :param mode:  :ref:`MVIEW_OPEN`
        :type  map:   GXMAP
        :type  name:  str
        :type  mode:  int

        :returns:     `GXMVIEW <geosoft.gxapi.GXMVIEW>`, aborts if creation fails
        :rtype:       GXMVIEW

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** View scaling is set to mm on the map and the view
        origin is set to the map origin.
        """
        ret_val = gxapi_cy.WrapMVIEW._create(GXContext._get_tls_geo(), map, name.encode(), mode)
        return GXMVIEW(ret_val)



    @classmethod
    def create_crooked_section(cls, map, ipj, name, x0, y0, xs, ys, scale, v_ex, dist0, elev, v_vxs, v_vx, v_vy):
        """
        Creates a new crooked section view.
        
        :param map:    `GXMAP <geosoft.gxapi.GXMAP>` Object
        :param ipj:    Geographic projection of input X, Y locations below (without orientation)
        :param name:   View Name
        :param x0:     Base view bottom left corner X (mm)
        :param y0:     Base view bottom left corner Y (mm)
        :param xs:     Base view size in X (mm)
        :param ys:     Base view size in Y (mm)
        :param scale:  Map horizontal scale (X-axis)
        :param v_ex:   Vertical exaggeration (1.0 is normal, must be >0.0)
        :param dist0:  Starting distance at the left side of the view.
        :param elev:   Elevation at TOP of the view
        :param v_vxs:  Cumulative distances along the secton
        :param v_vx:   True X locations along the section
        :param v_vy:   True Y locations along the section
        :type  map:    GXMAP
        :type  ipj:    GXIPJ
        :type  name:   str
        :type  x0:     float
        :type  y0:     float
        :type  xs:     float
        :type  ys:     float
        :type  scale:  float
        :type  v_ex:   float
        :type  dist0:  float
        :type  elev:   float
        :type  v_vxs:  GXVV
        :type  v_vx:   GXVV
        :type  v_vy:   GXVV

        :returns:      `GXMVIEW <geosoft.gxapi.GXMVIEW>`, aborts if creation fails
        :rtype:        GXMVIEW

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A crooked section is a section running vertically beneath
        a path of (X, Y) locations, like a river. This view supports
        linking to other plan, section, or 3D views.
        The data view coordinates are set up so that vertical coordinate
        corresponds to elevation, and the X coordinate is the distance along
        the crooked feature, beginning at zero on the left, but the
        status bar will show the true (X, Y, Z) location.

        If the scale is set to `rDUMMY <geosoft.gxapi.rDUMMY>`, then it will be calculated so that
        the points will all fit horizontally.
        """
        ret_val = gxapi_cy.WrapMVIEW._create_crooked_section(GXContext._get_tls_geo(), map, ipj, name.encode(), x0, y0, xs, ys, scale, v_ex, dist0, elev, v_vxs, v_vx, v_vy)
        return GXMVIEW(ret_val)



    @classmethod
    def create_crooked_section_data_profile(cls, map, ipj, name, x0, y0, xs, ys, scale, dist0, min_z, max_z, log_z, v_vxs, v_vx, v_vy):
        """
        Creates a new crooked section data profile view.
        
        :param map:    `GXMAP <geosoft.gxapi.GXMAP>` Object
        :param ipj:    Geographic projection of input X, Y locations below (without orientation)
        :param name:   View Name
        :param x0:     Base view bottom left corner X (mm)
        :param y0:     Base view bottom left corner Y (mm)
        :param xs:     Base view size in X (mm)
        :param ys:     Base view size in Y (mm)
        :param scale:  Map horizontal scale (X-axis)
        :param dist0:  Starting distance at the left side of the view.
        :param min_z:  Data value at bottom of the view
        :param max_z:  Data value at top of the view
        :param log_z:  Make logarithmic Y-axis (0:No, 1:Yes)?
        :param v_vxs:  Cumulative distances along the secton
        :param v_vx:   True X locations along the section
        :param v_vy:   True Y locations along the section
        :type  map:    GXMAP
        :type  ipj:    GXIPJ
        :type  name:   str
        :type  x0:     float
        :type  y0:     float
        :type  xs:     float
        :type  ys:     float
        :type  scale:  float
        :type  dist0:  float
        :type  min_z:  float
        :type  max_z:  float
        :type  log_z:  int
        :type  v_vxs:  GXVV
        :type  v_vx:   GXVV
        :type  v_vy:   GXVV

        :returns:      `GXMVIEW <geosoft.gxapi.GXMVIEW>`, aborts if creation fails
        :rtype:        GXMVIEW

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is the same as `create_crooked_section <geosoft.gxapi.GXMVIEW.create_crooked_section>`, except that the
        vertical axis plots a data value, not elevation, and allows for
        logarithmic scaling.

        See Also: `create_crooked_section <geosoft.gxapi.GXMVIEW.create_crooked_section>`.
        """
        ret_val = gxapi_cy.WrapMVIEW._create_crooked_section_data_profile(GXContext._get_tls_geo(), map, ipj, name.encode(), x0, y0, xs, ys, scale, dist0, min_z, max_z, log_z, v_vxs, v_vx, v_vy)
        return GXMVIEW(ret_val)






    def extent(self, what, unit, min_x, min_y, max_x, max_y):
        """
        Get the view extents
        
        :param what:   :ref:`MVIEW_EXTENT`
        :param unit:   :ref:`MVIEW_EXTENT_UNIT`
        :param min_x:  X minimum
        :param min_y:  Y minimum
        :param max_x:  X maximum
        :param max_y:  Y maximum
        :type  what:   int
        :type  unit:   int
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The CLIP region is the current view window or the limits
        of the current clip polygon.

        If `MVIEW_EXTENT_ALL <geosoft.gxapi.MVIEW_EXTENT_ALL>` is requested and the view has no groups, the
        clip extents are returned.

        If clip extents are requested and there are no clip extents, an
        area 0.0,0.0 1.0,1.0 is returned.

        The `MVIEW_EXTENT_VISIBLE <geosoft.gxapi.MVIEW_EXTENT_VISIBLE>` flag will return the union of the `MVIEW_EXTENT_CLIP <geosoft.gxapi.MVIEW_EXTENT_CLIP>` area and the
        extents of all non-masked visible groups in the view.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._extent(what, unit, min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_map(self):
        """
        Get the `GXMAP <geosoft.gxapi.GXMAP>` of the view.
        

        :returns:      The `GXMAP <geosoft.gxapi.GXMAP>` of the View.
        :rtype:        GXMAP

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_map()
        return GXMAP(ret_val)




    def get_reg(self):
        """
        Get the `GXREG <geosoft.gxapi.GXREG>` of the view.
        

        :returns:      The `GXREG <geosoft.gxapi.GXREG>` of the View.
        :rtype:        GXREG

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_reg()
        return GXREG(ret_val)




    def get_name(self, name):
        """
        Gets the name of a view.
        
        :param name:   View name returned
        :type  name:   str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value = self._get_name(name.value.encode())
        




    def get_guid(self, guid):
        """
        Gets the GUID of the `GXMVIEW <geosoft.gxapi.GXMVIEW>`.
        
        :param guid:   GUID
        :type  guid:   str_ref

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If a GUID was never queried a new one will be assigned and the map will be modified. Only if the map is saved will this value then persist.
        """
        guid.value = self._get_guid(guid.value.encode())
        




# View Control



    def plot_to_view(self, x, y):
        """
        Convert a plot coordinate in mm to a VIEW coordinate.
        
        :param x:      X in plot mm, returned in View coordinates
        :param y:      Y in plot mm, returned in View coordinates
        :type  x:      float_ref
        :type  y:      float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        x.value, y.value = self._plot_to_view(x.value, y.value)
        




    def set_thin_res(self, thin):
        """
        Set polyline/polygon thinning resolution
        
        :param thin:   Thinning resolution in mm, -1.0 to turn off.
        :type  thin:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The thinning resolution controls the removal of
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
        self._set_thin_res(thin)
        




    def view_to_plot(self, x, y):
        """
        Convert a VIEW coordinate to a plot coordinate in mm.
        
        :param x:      X in View, returned in mm from plot origin
        :param y:      Y in View, returned in mm from plot origin
        :type  x:      float_ref
        :type  y:      float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        x.value, y.value = self._view_to_plot(x.value, y.value)
        




    def best_fit_window(self, m_min_x, m_min_y, m_max_x, m_max_y, v_min_x, v_min_y, v_max_x, v_max_y, fit_view):
        """
        Fit an area in ground coordinates centered to an area in mm on map or vise versa
        keeping X and Y scales the same.
        
        :param m_min_x:   X minimum (mm) of the area in map relative to map origin
        :param m_min_y:   Y minimum  ..
        :param m_max_x:   X maximum  ..
        :param m_max_y:   Y maximum  ..
        :param v_min_x:   Min X in ground coordinate to fit to the area defined above
        :param v_min_y:   Min Y in ground coordinate ..
        :param v_max_x:   Max X in ground coordinate ..
        :param v_max_y:   Max Y in ground coordinate ..
        :param fit_view:  :ref:`MVIEW_FIT`
        :type  m_min_x:   float_ref
        :type  m_min_y:   float_ref
        :type  m_max_x:   float_ref
        :type  m_max_y:   float_ref
        :type  v_min_x:   float_ref
        :type  v_min_y:   float_ref
        :type  v_max_x:   float_ref
        :type  v_max_y:   float_ref
        :type  fit_view:  int

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** X and Y scales will be redefined and units will remain unchanged.
        The final X and Y ranges (if changed) are returned.

        .. seealso::

            `fit_window <geosoft.gxapi.GXMVIEW.fit_window>`
        """
        m_min_x.value, m_min_y.value, m_max_x.value, m_max_y.value, v_min_x.value, v_min_y.value, v_max_x.value, v_max_y.value = self._best_fit_window(m_min_x.value, m_min_y.value, m_max_x.value, m_max_y.value, v_min_x.value, v_min_y.value, v_max_x.value, v_max_y.value, fit_view)
        




    def fit_map_window_3d(self, m_min_x, m_min_y, m_max_x, m_max_y, v_min_x, v_min_y, v_max_x, v_max_y):
        """
        Set the 2D view window for a 3D view.
        
        :param m_min_x:  X minimum (mm) of the area in map relative to map origin
        :param m_min_y:  Y minimum  ..
        :param m_max_x:  X maximum  ..
        :param m_max_y:  Y maximum  ..
        :param v_min_x:  Min X in ground coordinate to fit to the area defined above
        :param v_min_y:  Min Y in ground coordinate ..
        :param v_max_x:  Max X in ground coordinate ..
        :param v_max_y:  Max Y in ground coordinate ..
        :type  m_min_x:  float
        :type  m_min_y:  float
        :type  m_max_x:  float
        :type  m_max_y:  float
        :type  v_min_x:  float
        :type  v_min_y:  float
        :type  v_max_x:  float
        :type  v_max_y:  float

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 3D views are placed in 2D maps within a 2D mapping window
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
        self._fit_map_window_3d(m_min_x, m_min_y, m_max_x, m_max_y, v_min_x, v_min_y, v_max_x, v_max_y)
        




    def fit_window(self, m_min_x, m_min_y, m_max_x, m_max_y, v_min_x, v_min_y, v_max_x, v_max_y):
        """
        Fit an area in ground coordinates to an area in mm on map.
        
        :param m_min_x:  X minimum (mm) of the area in map relative to map origin
        :param m_min_y:  Y minimum  ..
        :param m_max_x:  X maximum  ..
        :param m_max_y:  Y maximum  ..
        :param v_min_x:  Min X in ground coordinate to fit to the area defined above
        :param v_min_y:  Min Y in ground coordinate ..
        :param v_max_x:  Max X in ground coordinate ..
        :param v_max_y:  Max Y in ground coordinate ..
        :type  m_min_x:  float
        :type  m_min_y:  float
        :type  m_max_x:  float
        :type  m_max_y:  float
        :type  v_min_x:  float
        :type  v_min_y:  float
        :type  v_max_x:  float
        :type  v_max_y:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** X and Y scales will be redefined and the units will be set to <unknown>.
        Coordinate ranges must be greater than 0.0.

        .. seealso::

            `set_window <geosoft.gxapi.GXMVIEW.set_window>`
        """
        self._fit_window(m_min_x, m_min_y, m_max_x, m_max_y, v_min_x, v_min_y, v_max_x, v_max_y)
        




    def get_class_name(self, cl, name):
        """
        Get a class name.
        
        :param cl:     Class
        :param name:   Name
        :type  cl:     str
        :type  name:   str_ref

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** `GXMVIEW <geosoft.gxapi.GXMVIEW>` class names are intended to be used to record the
        names of certain classes in the view, such as "Plane"
        for the default drawing plane.
        """
        name.value = self._get_class_name(cl.encode(), name.value.encode())
        




    def map_origin(self, x_origin, y_origin):
        """
        Get the map origin from a view
        
        :param x_origin:  Returned map origin - X
        :param y_origin:  Returned map origin - Y
        :type  x_origin:  float_ref
        :type  y_origin:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        x_origin.value, y_origin.value = self._map_origin(x_origin.value, y_origin.value)
        




    def re_scale(self, scale):
        """
        Change the scale of a view.
        
        :param scale:  Scale factor (> 0.0)
        :type  scale:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The view size is multiplied by the scale factor.
        The view location will move relative to the map origin
        by the scale factor.
        """
        self._re_scale(scale)
        




    def get_map_scale(self):
        """
        Get the current map scale of the view
        

        :returns:      The current map scale to 6 significant digits
        :rtype:        float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_map_scale()
        return ret_val




    def scale_mm(self):
        """
        Get the horizontal scale in view X units/mm
        

        :returns:      Returns horizontal scale in view X units/mm
        :rtype:        float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The scale factor is intended to be used by methods
        that would like to specify sizes in mm.  Examples
        would be text sizes, line thicknesses and line
        pitch.
        """
        ret_val = self._scale_mm()
        return ret_val




    def scale_pj_mm(self):
        """
        Get horizontal scale in projected user units/mm
        

        :returns:      Returns horizontal scale in projected user units/mm
        :rtype:        float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The scale factor is intended to be used by methods
        that would like to specify sizes in mm.  Examples
        would be text sizes, line thicknesses and line
        pitch.
        Same as rScaleMM if working projection not defined
        """
        ret_val = self._scale_pj_mm()
        return ret_val




    def scale_ymm(self):
        """
        Get the vertical scale in Y units/mm
        

        :returns:      Returns vertical scale in view Y units/mm
        :rtype:        float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The scale factor is intended to be used by methods
        that would like to specify sizes in mm.  Examples
        would be text sizes, line thicknesses and line
        pitch.
        """
        ret_val = self._scale_ymm()
        return ret_val




    def scale_all_group(self, xs, ys):
        """
        Scale all groups (except for GRID) in a view
        
        :param xs:     X scale
        :param ys:     Y scale
        :type  xs:     float
        :type  ys:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** X (and Y) scale is the ratio of the new dimension over
        the old dimension of a reference object. For example, if a horizontal
        straight line of 10m long becomes 20m, X scale should be 2.

        The view is then scaled back so that the view occupies the same
        area size as before.  The view's clip area is updated as well.
        """
        self._scale_all_group(xs, ys)
        




    def scale_window(self, min_x, min_y, max_x, max_y, bot_x, bot_y, x_scal, y_scal):
        """
        Assign view coordinates to define a window.
        
        :param min_x:   X minimum in view coordinates
        :param min_y:   Y minimum
        :param max_x:   X maximum
        :param max_y:   Y maximum
        :param bot_x:   X minimum in plot coordinates
        :param bot_y:   Y minimum
        :param x_scal:  Horizontal scale (view unit/plot unit in mm)
        :param y_scal:  Vertical scale
        :type  min_x:   float
        :type  min_y:   float
        :type  max_x:   float
        :type  max_y:   float
        :type  bot_x:   float
        :type  bot_y:   float
        :type  x_scal:  float
        :type  y_scal:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The provided coordinates are converted to map mm
        using the current view translation and scaling.
        SetWindow is effectively called.

        .. seealso::

            `set_window <geosoft.gxapi.GXMVIEW.set_window>`, `scale_window <geosoft.gxapi.GXMVIEW.scale_window>`, `tran_scale <geosoft.gxapi.GXMVIEW.tran_scale>`
        """
        self._scale_window(min_x, min_y, max_x, max_y, bot_x, bot_y, x_scal, y_scal)
        




    def set_class_name(self, cl, name):
        """
        Set a class name.
        
        :param cl:     Class
        :param name:   Name
        :type  cl:     str
        :type  name:   str

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** `GXMVIEW <geosoft.gxapi.GXMVIEW>` class names are intended to be used to record the
        names of certain classes in the view, such as "Plane"
        for the default drawing plane.
        """
        self._set_class_name(cl.encode(), name.encode())
        




    def set_window(self, min_x, min_y, max_x, max_y, unit):
        """
        Set the view window
        
        :param min_x:  X minimum
        :param min_y:  Y minimum
        :param max_x:  X maximum
        :param max_y:  Y maximum
        :param unit:   :ref:`MVIEW_UNIT`
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float
        :type  unit:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The current clip region will be set to the clip
        window.

        .. seealso::

            `fit_window <geosoft.gxapi.GXMVIEW.fit_window>`, `scale_window <geosoft.gxapi.GXMVIEW.scale_window>`, `extent <geosoft.gxapi.GXMVIEW.extent>`.
        """
        self._set_window(min_x, min_y, max_x, max_y, unit)
        




    def tran_scale(self, x, y, xs, ys):
        """
        Set the view translation and scaling
        
        :param x:      X origin (user X to be placed at map 0)
        :param y:      Y origin (user Y to be placed at map 0)
        :param xs:     X mm/user unit
        :param ys:     Y mm/user unit
        :type  x:      float
        :type  y:      float
        :type  xs:     float
        :type  ys:     float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Warning. For reasons unknown (and maybe a bug), this
        function resets the view `GXIPJ <geosoft.gxapi.GXIPJ>` units. It is a good idea
        to call the SetUnits_IPJ function after calling this
        function in order to restore them. This will be addressed
        in v6.4.
        """
        self._tran_scale(x, y, xs, ys)
        




    def user_to_view(self, x, y):
        """
        Convert a USERplot in mm to a VIEW coordinate
        
        :param x:      X in USER, returned in View coordinates
        :param y:      Y in USER, returned in View coordinates
        :type  x:      float_ref
        :type  y:      float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`
            `get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>`
        """
        x.value, y.value = self._user_to_view(x.value, y.value)
        




    def view_to_user(self, x, y):
        """
        Convert a VIEW coordinate to a USER coordinate.
        
        :param x:      X in View, returned in user coordinates
        :param y:      Y in View, returned in user coordinates
        :type  x:      float_ref
        :type  y:      float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `set_user_ipj <geosoft.gxapi.GXMVIEW.set_user_ipj>`
            `get_user_ipj <geosoft.gxapi.GXMVIEW.get_user_ipj>`
        """
        x.value, y.value = self._view_to_user(x.value, y.value)
        




# Obsolete



    def get_surface_filename(self, group, filename):
        """
        Get the surface filename.
        
        :param group:     Group name
        :param filename:  filename returned
        :type  group:     str
        :type  filename:  str_ref

        .. versionadded:: 9.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The group must be a `GXSURFACE <geosoft.gxapi.GXSURFACE>` group. Check this using
        `is_group <geosoft.gxapi.GXMVIEW.is_group>` and `MVIEW_IS_GENSURF <geosoft.gxapi.MVIEW_IS_GENSURF>` or `MVIEW_IS_VOXSURF <geosoft.gxapi.MVIEW_IS_VOXSURF>` .
        """
        filename.value = self._get_surface_filename(group.encode(), filename.value.encode())
        




    def is_surface_item_visible(self, group, guid):
        """
        Is the surface item visible?
        
        :param group:  Group name
        :param guid:   Item GUID
        :type  group:  str
        :type  guid:   str
        :rtype:        bool

        .. versionadded:: 9.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_surface_item_visible(group.encode(), guid.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer