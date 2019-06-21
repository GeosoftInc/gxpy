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
class GXIPJ(gxapi_cy.WrapIPJ):
    """
    GXIPJ class.

    The `GXIPJ <geosoft.gxapi.GXIPJ>` class describes a single spatial reference in the world,
    defined under a coordinate system, an orientation,
    and a warp (which can be used to distort the projected object
    to a particular shape or boundary).

    **Note:**

    `GXIPJ <geosoft.gxapi.GXIPJ>` objects may be attached to channels or views. Two IPJs taken
    together are used to create a `GXPJ <geosoft.gxapi.GXPJ>` object, which allows for the
    conversion of positions from one projection to the other.
    See also the `GXLL2 <geosoft.gxapi.GXLL2>` class, which creates Datum correction lookups.

    See also          `GXPJ <geosoft.gxapi.GXPJ>`    Converts coordinates between projections
    `GXLL2 <geosoft.gxapi.GXLL2>`   Creates Datum correction lookups.
    """

    def __init__(self, handle=0):
        super(GXIPJ, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIPJ <geosoft.gxapi.GXIPJ>`
        
        :returns: A null `GXIPJ <geosoft.gxapi.GXIPJ>`
        :rtype:   GXIPJ
        """
        return GXIPJ()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def clear_warp(self):
        """
        Clear warp parameters (if any) from an `GXIPJ <geosoft.gxapi.GXIPJ>`.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._clear_warp()
        




    def make_geographic(self):
        """
        Remove a projected coordinate system from an `GXIPJ <geosoft.gxapi.GXIPJ>`
        

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function does nothing if the `GXIPJ <geosoft.gxapi.GXIPJ>` is not a projected coordinate system.
        """
        self._make_geographic()
        




    def make_wgs84(self):
        """
        Make a WGS 84 geographic projection
        

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._make_wgs84()
        




    def set_units(self, scale, str_val):
        """
        Set unit parameters
        
        :param scale:    Factor to meters, must be >= 0.0
        :param str_val:  Abbreviation, can be ""
        :type  scale:    float
        :type  str_val:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_units(scale, str_val.encode())
        




    def add_exagg_warp(self, x_exag, y_exag, z_exag, x_orig, y_orig, z_orig):
        """
        Add a warp to `GXIPJ <geosoft.gxapi.GXIPJ>` to exaggerate X, Y and Z.
        
        :param x_exag:  X exaggeration, must be > 0.0
        :param y_exag:  Y exaggeration, must be > 0.0
        :param z_exag:  Z exaggeration, must be > 0.0
        :param x_orig:  X reference origin
        :param y_orig:  Y reference origin
        :param z_orig:  Z reference origin
        :type  x_exag:  float
        :type  y_exag:  float
        :type  z_exag:  float
        :type  x_orig:  float
        :type  y_orig:  float
        :type  z_orig:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._add_exagg_warp(x_exag, y_exag, z_exag, x_orig, y_orig, z_orig)
        




    def add_log_warp(self, x, y):
        """
        Add a warp to `GXIPJ <geosoft.gxapi.GXIPJ>` to log one or both coordinantes
        
        :param x:    Log in X?
        :param y:    Log in Y?
        :type  x:    int
        :type  y:    int

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._add_log_warp(x, y)
        




    def add_matrix_warp(self, v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33):
        """
        Add a warp to `GXIPJ <geosoft.gxapi.GXIPJ>` using a matrix
        
        :param v00:  Row 0 Element 0
        :param v01:  Row 0 Element 1
        :param v02:  Row 0 Element 2
        :param v03:  Row 0 Element 3
        :param v10:  Row 1 Element 0
        :param v11:  Row 1 Element 1
        :param v12:  Row 1 Element 2
        :param v13:  Row 1 Element 3
        :param v20:  Row 2 Element 0
        :param v21:  Row 2 Element 1
        :param v22:  Row 2 Element 2
        :param v23:  Row 2 Element 3
        :param v30:  Row 3 Element 0
        :param v31:  Row 3 Element 1
        :param v32:  Row 3 Element 2
        :param v33:  Row 3 Element 3
        :type  v00:  float
        :type  v01:  float
        :type  v02:  float
        :type  v03:  float
        :type  v10:  float
        :type  v11:  float
        :type  v12:  float
        :type  v13:  float
        :type  v20:  float
        :type  v21:  float
        :type  v22:  float
        :type  v23:  float
        :type  v30:  float
        :type  v31:  float
        :type  v32:  float
        :type  v33:  float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._add_matrix_warp(v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33)
        




    def add_warp(self, type, vv_x_old, vv_y_old, vv_x_new, vv_y_new):
        """
        Add a warp to `GXIPJ <geosoft.gxapi.GXIPJ>`.
        
        :param type:      :ref:`IPJ_TYPE`
        :param vv_x_old:  Old X `GXVV <geosoft.gxapi.GXVV>` (real)
        :param vv_y_old:  Old Y `GXVV <geosoft.gxapi.GXVV>` (real)
        :param vv_x_new:  New X `GXVV <geosoft.gxapi.GXVV>` (real)
        :param vv_y_new:  New Y `GXVV <geosoft.gxapi.GXVV>` (real)
        :type  type:      int
        :type  vv_x_old:  GXVV
        :type  vv_y_old:  GXVV
        :type  vv_x_new:  GXVV
        :type  vv_y_new:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** There must be at least "warp type" points in the
        warp point `GXVV <geosoft.gxapi.GXVV>`'s.
        All point `GXVV <geosoft.gxapi.GXVV>`'s must have the same number of points.
        If there are more points than required by the warp,
        the warp will be determined by least-square fitting
        to the warp surface for all but the 4-point warp.
        The 4-point ward requires exactly 4 points.

        Cannot be used with WARP_MATRIX or WARP_LOG
        """
        self._add_warp(type, vv_x_old, vv_y_old, vv_x_new, vv_y_new)
        




    def clear_coordinate_system(self):
        """
        Clear coordinate sytsem, except for units
        

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Clears the Datum, Local Datum and Projection info.
        Leaves units, any warp or orientation warp unchanged.
        """
        self._clear_coordinate_system()
        




    def clear_orientation(self):
        """
        Clear an orientation warp from an `GXIPJ <geosoft.gxapi.GXIPJ>`.
        

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._clear_orientation()
        




    def convert_orientation_warp_vv(self, vv_x, vv_y, vv_z, f_forward):
        """
        Convert X,Y and Z VVs using the orientation warp from an `GXIPJ <geosoft.gxapi.GXIPJ>`.
        
        :param vv_x:       X `GXVV <geosoft.gxapi.GXVV>` coordinates converted on output
        :param vv_y:       Y `GXVV <geosoft.gxapi.GXVV>` coordinates converted on output
        :param vv_z:       Z `GXVV <geosoft.gxapi.GXVV>` coordinates converted on output
        :param f_forward:  1 -  Forward (raw -> coordinate) , 0 - (coordinate -> raw)
        :type  vv_x:       GXVV
        :type  vv_y:       GXVV
        :type  vv_z:       GXVV
        :type  f_forward:  int

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._convert_orientation_warp_vv(vv_x, vv_y, vv_z, f_forward)
        




    def copy(self, ip_jd):
        """
        Copy IPJs
        
        :param ip_jd:  Destination `GXIPJ <geosoft.gxapi.GXIPJ>`
        :type  ip_jd:  GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(ip_jd)
        




    def copy_projection(self, ip_jd):
        """
        Copy the projection from one `GXIPJ <geosoft.gxapi.GXIPJ>` to another
        
        :param ip_jd:  Source
        :type  ip_jd:  GXIPJ

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Copies the projection parameters, while leaving the rest
        (e.g. Datum, Local Datum Transform) unchanged.
        """
        self._copy_projection(ip_jd)
        



    @classmethod
    def create(cls):
        """
        This method creates a projection object.
        

        :returns:    `GXIPJ <geosoft.gxapi.GXIPJ>` Object
        :rtype:      GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapIPJ._create(GXContext._get_tls_geo())
        return GXIPJ(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create `GXIPJ <geosoft.gxapi.GXIPJ>` from serialized source.
        
        :type  bf:  GXBF

        :returns:    `GXIPJ <geosoft.gxapi.GXIPJ>` Object
        :rtype:      GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapIPJ._create_s(GXContext._get_tls_geo(), bf)
        return GXIPJ(ret_val)



    @classmethod
    def create_xml(cls, file):
        """
        Create an `GXIPJ <geosoft.gxapi.GXIPJ>` from serialized Geosoft MetaData XML file
        
        :param file:  File Name
        :type  file:  str

        :returns:     `GXIPJ <geosoft.gxapi.GXIPJ>` Object
        :rtype:       GXIPJ

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapIPJ._create_xml(GXContext._get_tls_geo(), file.encode())
        return GXIPJ(ret_val)






    def get_3d_view(self, x, y, z, rx, ry, rz, sx, sy, str_val):
        """
        Get 3D orientation parameters
        
        :param x:        X location of view origin
        :param y:        Y location of view origin
        :param z:        Z location of view origin
        :param rx:       Rotation in X
        :param ry:       Rotation in Y
        :param rz:       Rotation in Z
        :param sx:       Scaling in X
        :param sy:       Scaling in Y
        :param str_val:  Scaling in Z
        :type  x:        float_ref
        :type  y:        float_ref
        :type  z:        float_ref
        :type  rx:       float_ref
        :type  ry:       float_ref
        :type  rz:       float_ref
        :type  sx:       float_ref
        :type  sy:       float_ref
        :type  str_val:  float_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The view must have a 3D orientation
        """
        x.value, y.value, z.value, rx.value, ry.value, rz.value, sx.value, sy.value, str_val.value = self._get_3d_view(x.value, y.value, z.value, rx.value, ry.value, rz.value, sx.value, sy.value, str_val.value)
        




    def get_3d_view_ex(self, x, y, z, rx, ry, rz, sx, sy, str_val, rotate, flags):
        """
        Get 3D orientation parameters with new flags
        
        :param x:        X location of view origin
        :param y:        Y location of view origin
        :param z:        Z location of view origin
        :param rx:       Rotation in X
        :param ry:       Rotation in Y
        :param rz:       Rotation in Z
        :param sx:       Scaling in X
        :param sy:       Scaling in Y
        :param str_val:  Scaling in Z
        :param rotate:   :ref:`IPJ_3D_ROTATE`
        :param flags:    :ref:`IPJ_3D_FLAG`
        :type  x:        float_ref
        :type  y:        float_ref
        :type  z:        float_ref
        :type  rx:       float_ref
        :type  ry:       float_ref
        :type  rz:       float_ref
        :type  sx:       float_ref
        :type  sy:       float_ref
        :type  str_val:  float_ref
        :type  rotate:   int_ref
        :type  flags:    int_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The view must have a 3D orientation
        """
        x.value, y.value, z.value, rx.value, ry.value, rz.value, sx.value, sy.value, str_val.value, rotate.value, flags.value = self._get_3d_view_ex(x.value, y.value, z.value, rx.value, ry.value, rz.value, sx.value, sy.value, str_val.value, rotate.value, flags.value)
        




    def get_crooked_section_view_v_vs(self, dist_vv, xvv, yvv, log_z):
        """
        Get the crooked section path.
        
        :param dist_vv:  Section X locations (e.g. distance along the curve)
        :param xvv:      True X
        :param yvv:      True Y
        :param log_z:    Use logarithmic Y-axis (usually for data profiles) 0:No, 1:Yes
        :type  dist_vv:  GXVV
        :type  xvv:      GXVV
        :type  yvv:      GXVV
        :type  log_z:    int_ref

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns the orignal VVs used to set up the crooked section path.
        """
        log_z.value = self._get_crooked_section_view_v_vs(dist_vv, xvv, yvv, log_z.value)
        



    @classmethod
    def get_list(cls, parm, datum, lst):
        """
        Get a list of parameters.
        
        :param parm:   :ref:`IPJ_PARM_LST`
        :param datum:  Datum filter, "" for no filter
        :param lst:    List returned
        :type  parm:   int
        :type  datum:  str
        :type  lst:    GXLST

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The datum filter string, if specified, will limit the requested
        list to those valid for the spacified datum.
        """
        gxapi_cy.WrapIPJ._get_list(GXContext._get_tls_geo(), parm, datum.encode(), lst)
        




    def get_orientation_info(self, x, y, z, az, swing):
        """
        Get `GXIPJ <geosoft.gxapi.GXIPJ>` orientation parameters.
        
        :param x:      Plane Origin X
        :param y:      Plane Origin Y
        :param z:      Plane Origin Z
        :param az:     Plane Azimuth (section) or Rotation (plan)
        :param swing:  Plane Swing   (section)
        :type  x:      float_ref
        :type  y:      float_ref
        :type  z:      float_ref
        :type  az:     float_ref
        :type  swing:  float_ref

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** IPJ_ORIENT_TYPE:
        `IPJ_ORIENT_DEFAULT <geosoft.gxapi.IPJ_ORIENT_DEFAULT>` - no special orientation - plan view.
        This is equivalent to `IPJ_ORIENT_PLAN <geosoft.gxapi.IPJ_ORIENT_PLAN>` with
        dXo = dYo = dZo = dRotation = 0.0.

        `IPJ_ORIENT_PLAN <geosoft.gxapi.IPJ_ORIENT_PLAN>`      Azimuth = Rotation CCW degrees
        The plan differs from the default view in that
        a reference level is set, and the axes can be
        rotated and offset from the local X,Y.

        `IPJ_ORIENT_SECTION <geosoft.gxapi.IPJ_ORIENT_SECTION>`   Azimuth - CW degrees from North
        -360 <= azimuth <= 360
        Swing - degrees bottom towards viewer
        -90 < swing < 90
        The section view projects all plotted objects
        HORIZONTALLY onto the viewing plan in order to
        preserve elevations, even if the section has a swing.
        """
        x.value, y.value, z.value, az.value, swing.value = self._get_orientation_info(x.value, y.value, z.value, az.value, swing.value)
        




    def get_plane_equation(self, min_x, min_y, max_x, max_y, pitch, yaw, roll, x, y, z, sx, sy, str_val):
        """
        Get the equation of a plane
        
        :param min_x:    Min X of surface
        :param min_y:    Min Y of surface
        :param max_x:    Max X of surface
        :param max_y:    Max Y of surface
        :param pitch:    Pitch angle (between -360 and 360)
        :param yaw:      Yaw angle (between -360 and 360)
        :param roll:     Roll angles (between -360 and 360)
        :param x:        X offset of plane
        :param y:        Y offset of plane
        :param z:        Z offset of plane
        :param sx:       X scale
        :param sy:       Y scale
        :param str_val:  Z scale
        :type  min_x:    float
        :type  min_y:    float
        :type  max_x:    float
        :type  max_y:    float
        :type  pitch:    float_ref
        :type  yaw:      float_ref
        :type  roll:     float_ref
        :type  x:        float_ref
        :type  y:        float_ref
        :type  z:        float_ref
        :type  sx:       float_ref
        :type  sy:       float_ref
        :type  str_val:  float_ref

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Two opposite corners of the plane are required.
        Because the origin of the plane does not necessarily
        have a stable back-projection into true 3d coordinates.
        In practice, use the current view extents, or the corners
        of a grid.
        """
        pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value = self._get_plane_equation(min_x, min_y, max_x, max_y, pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value)
        




    def get_plane_equation2(self, ip_jo, min_x, min_y, max_x, max_y, pitch, yaw, roll, x, y, z, sx, sy, str_val):
        """
        Get the equation of a plane with reprojection.
        
        :param ip_jo:    `GXIPJ <geosoft.gxapi.GXIPJ>` object for the output values
        :param min_x:    Min X of surface (in grid coords)
        :param min_y:    Min Y of surface
        :param max_x:    Max X of surface
        :param max_y:    Max Y of surface
        :param pitch:    Pitch angle (between -360 and 360) (in view coords)
        :param yaw:      Yaw angle (between -360 and 360)
        :param roll:     Roll angles (between -360 and 360)
        :param x:        X offset of plane (in view coords)
        :param y:        Y offset of plane
        :param z:        Z offset of plane
        :param sx:       X scale (in view coords)
        :param sy:       Y scale
        :param str_val:  Z scale
        :type  ip_jo:    GXIPJ
        :type  min_x:    float
        :type  min_y:    float
        :type  max_x:    float
        :type  max_y:    float
        :type  pitch:    float_ref
        :type  yaw:      float_ref
        :type  roll:     float_ref
        :type  x:        float_ref
        :type  y:        float_ref
        :type  z:        float_ref
        :type  sx:       float_ref
        :type  sy:       float_ref
        :type  str_val:  float_ref

        .. versionadded:: 6.4.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is the same as `get_plane_equation <geosoft.gxapi.GXIPJ.get_plane_equation>`, but the
        input projected coordinate system (PCS) may
        be different from that of the `GXIPJ <geosoft.gxapi.GXIPJ>` you want the
        plane equation values described in. This may be
        required, for instance, when a 3D view has been created
        in one PCS, and an oriented grid from a different PCS is
        to be displayed in that view.

        If the two input IPJs share the same PCS then the `get_plane_equation <geosoft.gxapi.GXIPJ.get_plane_equation>`
        function is called directly, using the input `GXIPJ <geosoft.gxapi.GXIPJ>`.
        """
        pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value = self._get_plane_equation2(ip_jo, min_x, min_y, max_x, max_y, pitch.value, yaw.value, roll.value, x.value, y.value, z.value, sx.value, sy.value, str_val.value)
        




    def compare_datums(self, ipj2):
        """
        Compare the datums of two coordinate systems?
        
        :param ipj2:  `GXIPJ <geosoft.gxapi.GXIPJ>` 2
        :type  ipj2:  GXIPJ

        :returns:     0 - Datums are different
                      1 - Datums are the same, but different LDT
                      2 - Datums and LTD are the same
        :rtype:       int

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To transform between different datums requires the use of a local
        datum transform.  The local datum transform can be defined when
        a coordinate system is created, but the definition is optional.
        This function will test that the local datum transforms are defined.
        Note that a coordinate transformation between datums without a
        local datum transform is still possible, but only the effect of
        ellipsoid shape will be modelled in the transform.
        """
        ret_val = self._compare_datums(ipj2)
        return ret_val




    def convert_warp(self, x, y, z, f_forward):
        """
        Converts a point X, Y, Z to the new `GXIPJ <geosoft.gxapi.GXIPJ>` plane.
        
        :param x:          X coordinates converted on output
        :param y:          Y coordinates converted on output
        :param z:          Z coordinates converted on output
        :param f_forward:  1 -  Forward (raw -> coordinate) , 0 - (coordinate -> raw)
        :type  x:          float_ref
        :type  y:          float_ref
        :type  z:          float_ref
        :type  f_forward:  int

        :returns:          0 if ok - 1 otherwise
        :rtype:            int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, x.value, y.value, z.value = self._convert_warp(x.value, y.value, z.value, f_forward)
        return ret_val




    def convert_warp_vv(self, vv_x, vv_y, f_forward):
        """
        Converts a set of X & Y VVs to the new `GXIPJ <geosoft.gxapi.GXIPJ>` plane. The Z is assumed to be 0
        
        :param vv_x:       X `GXVV <geosoft.gxapi.GXVV>` coordinates converted on output
        :param vv_y:       Y `GXVV <geosoft.gxapi.GXVV>` coordinates converted on output
        :param f_forward:  1 -  Forward (raw -> coordinate) , 0 - (coordinate -> raw)
        :type  vv_x:       GXVV
        :type  vv_y:       GXVV
        :type  f_forward:  int

        :returns:          0 if ok - 1 otherwise
        :rtype:            int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._convert_warp_vv(vv_x, vv_y, f_forward)
        return ret_val




    def coordinate_systems_are_the_same(self, ipj2):
        """
        Are these two coordinate systems the same?
        
        :param ipj2:  `GXIPJ <geosoft.gxapi.GXIPJ>` 2
        :type  ipj2:  GXIPJ

        :returns:     0 - No
                      1 - Yes
        :rtype:       int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This does not compare LDT information (use `compare_datums <geosoft.gxapi.GXIPJ.compare_datums>` for that).
        """
        ret_val = self._coordinate_systems_are_the_same(ipj2)
        return ret_val




    def coordinate_systems_are_the_same_within_a_small_tolerance(self, ipj2):
        """
        Same as `coordinate_systems_are_the_same <geosoft.gxapi.GXIPJ.coordinate_systems_are_the_same>`, but allows for small numerical differences
        
        :param ipj2:  `GXIPJ <geosoft.gxapi.GXIPJ>` 2
        :type  ipj2:  GXIPJ

        :returns:     0 - No
                      1 - Yes
        :rtype:       int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._coordinate_systems_are_the_same_within_a_small_tolerance(ipj2)
        return ret_val




    def get_display_name(self, str_val):
        """
        Get a name for display purposes from `GXIPJ <geosoft.gxapi.GXIPJ>`
        
        :param str_val:  Name returned
        :type  str_val:  str_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        str_val.value = self._get_display_name(str_val.value.encode())
        




    def get_esri(self, esri):
        """
        Store coordinate system in an ESRI prj coordinate string
        
        :param esri:  ESRI projection string returned
        :type  esri:  str_ref

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the projection is not supported in ESRI, the projection
        string will be empty.
        """
        esri.value = self._get_esri(esri.value.encode())
        




    def get_gxf(self, str1, str2, str3, str4, str5):
        """
        Store coordinate system in GXF style strings.
        
        :param str1:  Projection name
        :param str2:  Datum name, major axis, elipticity
        :param str3:  Method name, parameters
        :param str4:  Unit name, factor
        :param str5:  Local transform name,dX,dY,dZ,rX,rY,rZ,Scale
        :type  str1:  str_ref
        :type  str2:  str_ref
        :type  str3:  str_ref
        :type  str4:  str_ref
        :type  str5:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See GXF revision 3 for string descriptions
        All strings must be the same length, 160 (`STR_GXF <geosoft.gxapi.STR_GXF>`) recommended.
        Strings too short will be truncated.
        """
        str1.value, str2.value, str3.value, str4.value, str5.value = self._get_gxf(str1.value.encode(), str2.value.encode(), str3.value.encode(), str4.value.encode(), str5.value.encode())
        




    def get_mi_coord_sys(self, coord, units):
        """
        Store coordinate system in MapInfo coordsys pair
        
        :param coord:  MapInfo coordsys string returned
        :param units:  MapInfo unit string returned
        :type  coord:  str_ref
        :type  units:  str_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        coord.value, units.value = self._get_mi_coord_sys(coord.value.encode(), units.value.encode())
        




    def get_name(self, type, str_val):
        """
        Get an `GXIPJ <geosoft.gxapi.GXIPJ>` name
        
        :param type:     :ref:`IPJ_NAME`
        :param str_val:  Name returned
        :type  type:     int
        :type  str_val:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        str_val.value = self._get_name(type, str_val.value.encode())
        




    def set_vcs(self, str_val):
        """
        Set the Vertical Coordinate System in the `GXIPJ <geosoft.gxapi.GXIPJ>` name string
        
        :param str_val:  New name (See Valid inputs above).
        :type  str_val:  str

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The vertical coordinate system (vcs) describes the datum used for vertical coordinates. The vcs name, if
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
        self._set_vcs(str_val.encode())
        




    def get_orientation(self):
        """
        Get `GXIPJ <geosoft.gxapi.GXIPJ>` orientation in space.
        

        :returns:    :ref:`IPJ_ORIENT`
        :rtype:      int

        .. versionadded:: 5.1.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Projections can be created oriented horizontally (e.g. in plan maps)
        or vertically (in section maps - Wholeplot and `GXIP <geosoft.gxapi.GXIP>`).
        """
        ret_val = self._get_orientation()
        return ret_val




    def get_orientation_name(self, str_val):
        """
        Get a name for display purposes from `GXIPJ <geosoft.gxapi.GXIPJ>`
        
        :param str_val:  Name returned
        :type  str_val:  str_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        str_val.value = self._get_orientation_name(str_val.value.encode())
        




    def get_units(self, scale, str_val):
        """
        Get unit parameters
        
        :param scale:    Factor to meters
        :param str_val:  Abbreviation
        :type  scale:    float_ref
        :type  str_val:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        scale.value, str_val.value = self._get_units(scale.value, str_val.value.encode())
        




    def get_xml(self, str_val):
        """
        Get an Geosoft Metadata XML string from an `GXIPJ <geosoft.gxapi.GXIPJ>`
        
        :param str_val:  XML string returned
        :type  str_val:  str_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        str_val.value = self._get_xml(str_val.value.encode())
        




    def has_projection(self):
        """
        Does the `GXIPJ <geosoft.gxapi.GXIPJ>` object contain a projection?
        

        :returns:    0 - No
                     1 - Yes
        :rtype:      int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._has_projection()
        return ret_val




    def is_3d_inverted(self):
        """
        Is this 3D View inverted ?
        

        :returns:    0 - No
                     1 - Yes (inverted)
        :rtype:      int

        .. versionadded:: 6.3.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_3d_inverted()
        return ret_val




    def is_3d_inverted_angles(self):
        """
        Are the angles in this 3D View inverted ?
        

        :returns:    0 - No
                     1 - Yes (inverted)
        :rtype:      int

        .. versionadded:: 6.3.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_3d_inverted_angles()
        return ret_val




    def is_geographic(self):
        """
        See if this projection is geographic
        

        :returns:    0 - No
                     1 - Yes
        :rtype:      int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_geographic()
        return ret_val




    def orientations_are_the_same(self, ipj2):
        """
        Are these two orientations the same?
        
        :param ipj2:  `GXIPJ <geosoft.gxapi.GXIPJ>` 2
        :type  ipj2:  GXIPJ

        :returns:     0 - No
                      1 - Yes
        :rtype:       int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._orientations_are_the_same(ipj2)
        return ret_val




    def orientations_are_the_same_within_a_small_tolerance(self, ipj2):
        """
        Same as `orientations_are_the_same <geosoft.gxapi.GXIPJ.orientations_are_the_same>`, but allows for small numerical differences
        
        :param ipj2:  `GXIPJ <geosoft.gxapi.GXIPJ>` 2
        :type  ipj2:  GXIPJ

        :returns:     0 - No
                      1 - Yes
        :rtype:       int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._orientations_are_the_same_within_a_small_tolerance(ipj2)
        return ret_val




    def has_section_orientation(self):
        """
        Does this projection contain an orientation used by section plots?
        

        :returns:    0 - No
                     1 - Yes
        :rtype:      int

        .. versionadded:: 8.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns     1 if there is a section orientation

        The following orientations can be used to orient sections or section views:

        `IPJ_ORIENT_SECTION <geosoft.gxapi.IPJ_ORIENT_SECTION>` - Target-type sections with Z projection horizontally
        `IPJ_ORIENT_SECTION_NORMAL <geosoft.gxapi.IPJ_ORIENT_SECTION_NORMAL>` - Like `IPJ_ORIENT_SECTION <geosoft.gxapi.IPJ_ORIENT_SECTION>`, but Z projects
        perpendicular to the secton plane.
        `IPJ_ORIENT_SECTION_CROOKED <geosoft.gxapi.IPJ_ORIENT_SECTION_CROOKED>` - Crooked sections
        `IPJ_ORIENT_3D <geosoft.gxapi.IPJ_ORIENT_3D>` - Some Sections extracted from a voxel - e.g. VoxelToGrids,
        as the voxel can have any orientation in 3D.

        It is sometimes important to ignore the section orientation, for instance
        when rendering a grid in 3D where it has been located on a plane.
        """
        ret_val = self._has_section_orientation()
        return ret_val




    def projection_type_is_fully_supported(self):
        """
        Is the projection type fully supported?
        

        :returns:    0 - No
                     1 - Yes
        :rtype:      int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function checks only the projected coordinated system
        in the `GXIPJ <geosoft.gxapi.GXIPJ>` object, so should only be used with projections
        of type `IPJ_TYPE_PCS <geosoft.gxapi.IPJ_TYPE_PCS>`.
        This function does not test the validity of datums or local
        datum transforms.
        """
        ret_val = self._projection_type_is_fully_supported()
        return ret_val




    def set_gxf_safe(self, str1, str2, str3, str4, str5):
        """
        Same as `set_gxf <geosoft.gxapi.GXIPJ.set_gxf>`, but fails gracefully.
        
        :param str1:  "projection name" or PCS_NAME from ipj_pcs.csv (datum / projection) or EPSG coordinate system code number or "<file.prj>" projection file name or "<file.wrp>" warp file name
        :param str2:  "datum name"[, major axis, elipticity, prime meridian] or DATUM from datum.csv or EPSG datum code number
        :param str3:  "method name", parameters (P1 through P8) or "projection name"[,"method name","Units",P1,P2...] or TRANSFORM from transform.csv or EPSG transform method code number
        :param str4:  "unit name", convertion to metres or UNIT_LENGTH from units.csv
        :param str5:  "local transform name"[,dX,dY,dZ,rX,rY,rZ,Scale] or DATUM_TRF from datumtrf.csv or AREA_OF_USE from ldatum.csv or EPSG local datum transform code number
        :type  str1:  str
        :type  str2:  str
        :type  str3:  str
        :type  str4:  str
        :type  str5:  str

        :returns:     0 - error in setting `GXIPJ <geosoft.gxapi.GXIPJ>`, input `GXIPJ <geosoft.gxapi.GXIPJ>` unchanged.
                      1 - success: `GXIPJ <geosoft.gxapi.GXIPJ>` set using input values.
        :rtype:       int

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** `set_gxf <geosoft.gxapi.GXIPJ.set_gxf>` will fail and terminate the GX if anything goes wrong (e.g. having a wrong
        parameter). If this function fails, it simply returns 0 and leaves the
        `GXIPJ <geosoft.gxapi.GXIPJ>` unchanged.
        """
        ret_val = self._set_gxf_safe(str1.encode(), str2.encode(), str3.encode(), str4.encode(), str5.encode())
        return ret_val




    def source_type(self):
        """
        Get `GXIPJ <geosoft.gxapi.GXIPJ>` source type
        

        :returns:    :ref:`IPJ_TYPE`
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._source_type()
        return ret_val




    def support_datum_transform(self, ipj2):
        """
        Can we transform between these two datums?
        
        :param ipj2:  `GXIPJ <geosoft.gxapi.GXIPJ>` 2
        :type  ipj2:  GXIPJ

        :returns:     0 - No
                      1 - Yes, either because both CS are on the same datum,
                      or because a local datum transform is defined
                      for each coordinate system.
        :rtype:       int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To transform between different datums requires the use of a local
        datum transform.  The local datum transform can be defined when
        a coordinate system is created, but the definition is optional.
        This function will test that the local datum transforms are defined.
        Note that a coordinate transformation between datums without a
        local datum transform is still possible, but only the effect of
        ellipsoid shape will be modelled in the transform.
        """
        ret_val = self._support_datum_transform(ipj2)
        return ret_val



    @classmethod
    def unit_name(cls, val, type, name):
        """
        Get a unit name given a scale factor
        
        :param val:   Factor to meters
        :param type:  :ref:`IPJ_UNIT`
        :param name:  Name returned, "" if cannot find unit
        :type  val:   float
        :type  type:  int
        :type  name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value = gxapi_cy.WrapIPJ._unit_name(GXContext._get_tls_geo(), val, type, name.value.encode())
        




    def warped(self):
        """
        Does `GXIPJ <geosoft.gxapi.GXIPJ>` contain a warp?
        
        :rtype:      bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._warped()
        return ret_val




    def warps_are_the_same(self, ipj2):
        """
        Are these two warps the same?
        
        :param ipj2:  `GXIPJ <geosoft.gxapi.GXIPJ>` 2
        :type  ipj2:  GXIPJ

        :returns:     0 - No
                      1 - Yes
        :rtype:       int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._warps_are_the_same(ipj2)
        return ret_val




    def warps_are_the_same_within_a_small_tolerance(self, ipj2):
        """
        Same as `warps_are_the_same <geosoft.gxapi.GXIPJ.warps_are_the_same>`, but allows for small numerical differences
        
        :param ipj2:  `GXIPJ <geosoft.gxapi.GXIPJ>` 2
        :type  ipj2:  GXIPJ

        :returns:     0 - No
                      1 - Yes
        :rtype:       int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._warps_are_the_same_within_a_small_tolerance(ipj2)
        return ret_val




    def warp_type(self):
        """
        Obtain the warp type of an `GXIPJ <geosoft.gxapi.GXIPJ>`.
        

        :returns:    :ref:`IPJ_WARP`
        :rtype:      int

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._warp_type()
        return ret_val




    def make_projected(self, min_lon, min_lat, max_lon, max_lat):
        """
        Create a default projected coordinate system from lat-long ranges.
        
        :param min_lon:  Minimum longitude
        :param min_lat:  Minimum latitude
        :param max_lon:  Maximum longitude
        :param max_lat:  Maximum latitude
        :type  min_lon:  float
        :type  min_lat:  float
        :type  max_lon:  float
        :type  max_lat:  float

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Terminates with invalid or unsupported ranges.
        If the map crosses the equator, or if map is within 20 degrees of the
        equator, uses an equatorial mercator projection centered at the central
        longitude. Otherwise, uses a Lambert Conic Conformal (1SP) projection
        for the map. Global maps outside of +/- 70 degrees latitude are not
        supported.
        """
        self._make_projected(min_lon, min_lat, max_lon, max_lat)
        




    def new_box_resolution(self, ip_jo, res, min_x, min_y, max_x, max_y, min_res, max_res, diag_res):
        """
        Determine a data resolution in a new coordinate system
        
        :param ip_jo:     New `GXIPJ <geosoft.gxapi.GXIPJ>`
        :param res:       Data resolution in original `GXIPJ <geosoft.gxapi.GXIPJ>`
        :param min_x:     X minimum of bounding box in new `GXIPJ <geosoft.gxapi.GXIPJ>`
        :param min_y:     Y minimum
        :param max_x:     X maximum
        :param max_y:     Y maximum
        :param min_res:   Minimum data resolution in new `GXIPJ <geosoft.gxapi.GXIPJ>`,
        :param max_res:   Maximum data resolution in new `GXIPJ <geosoft.gxapi.GXIPJ>`
        :param diag_res:  Diagonal data resolution in new `GXIPJ <geosoft.gxapi.GXIPJ>`
        :type  ip_jo:     GXIPJ
        :type  res:       float
        :type  min_x:     float
        :type  min_y:     float
        :type  max_x:     float
        :type  max_y:     float
        :type  min_res:   float_ref
        :type  max_res:   float_ref
        :type  diag_res:  float_ref

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** if there are any problems reprojecting, new resolutions will
        dummy.  The conversion to new resolution is based on measurements
        along the four edges and two diagonals.
        """
        min_res.value, max_res.value, diag_res.value = self._new_box_resolution(ip_jo, res, min_x, min_y, max_x, max_y, min_res.value, max_res.value, diag_res.value)
        




    def read(self, type, str1, str2, str3):
        """
        Read and define an `GXIPJ <geosoft.gxapi.GXIPJ>` from a standard file.
        
        :param type:  :ref:`IPJ_TYPE`
        :param str1:  String 1
        :param str2:  String 2
        :param str3:  String 3
        :type  type:  int
        :type  str1:  str
        :type  str2:  str
        :type  str3:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._read(type, str1.encode(), str2.encode(), str3.encode())
        




    def get_method_parm(self, parm):
        """
        Get projection method parameter
        
        :param parm:  :ref:`IPJ_CSP`
        :type  parm:  int

        :returns:     Parameter setting, `rDUMMY <geosoft.gxapi.rDUMMY>` if dot used
        :rtype:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_method_parm(parm)
        return ret_val




    def get_north_azimuth(self, x, y):
        """
        Return the azimuth of geographic North at a point.
        
        :param x:    Input X location
        :param y:    Input Y location
        :type  x:    float
        :type  y:    float

        :returns:    Azimuth (degrees CW) of geographic north from grid north at a location.
        :rtype:      float

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the `GXIPJ <geosoft.gxapi.GXIPJ>` is not a projected coordinate system
        then the returned azimuth is `GS_R8DM <geosoft.gxapi.GS_R8DM>`;
        """
        ret_val = self._get_north_azimuth(x, y)
        return ret_val



    @classmethod
    def unit_scale(cls, name, default):
        """
        Get a unit scale (m/unit) given a name
        
        :param name:     Unit name, abbreviation or full name
        :param default:  Default to return if name not found
        :type  name:     str
        :type  default:  float

        :returns:        Scale factor m/unit
        :rtype:          float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If name cannot be found, returns default.
        """
        ret_val = gxapi_cy.WrapIPJ._unit_scale(GXContext._get_tls_geo(), name.encode(), default)
        return ret_val




    def serial(self, bf):
        """
        Serialize `GXIPJ <geosoft.gxapi.GXIPJ>` to a `GXBF <geosoft.gxapi.GXBF>`.
        
        :type  bf:   GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial(bf)
        




    def serial_fgdcxml(self, file):
        """
        Write the `GXIPJ <geosoft.gxapi.GXIPJ>` as a FDGC MetaData XML object
        
        :param file:  Name of file to export to
        :type  file:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial_fgdcxml(file.encode())
        




    def serial_isoxml(self, file):
        """
        Write the `GXIPJ <geosoft.gxapi.GXIPJ>` as a ISO MetaData XML object
        
        :param file:  Name of file to export to
        :type  file:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial_isoxml(file.encode())
        




    def serial_xml(self, file):
        """
        Write the `GXIPJ <geosoft.gxapi.GXIPJ>` as a Geosoft MetaData XML object
        
        :param file:  Name of file to export to
        :type  file:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial_xml(file.encode())
        




    def set_3d_inverted(self, inverted):
        """
        Set whether a view is inverted (must be 3D already)
        
        :param inverted:  Inverted (0 or 1)
        :type  inverted:  int

        .. versionadded:: 6.3.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_3d_inverted(inverted)
        




    def set_3d_inverted_angles(self, inverted):
        """
        Set whether the angles in this view are inverted (must be 3D already)
        
        :param inverted:  Inverted (0 or 1)
        :type  inverted:  int

        .. versionadded:: 6.3.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_3d_inverted_angles(inverted)
        




    def set_3d_view(self, x, y, z, rx, ry, rz, sx, sy, str_val):
        """
        Set 3D orientation parameters
        
        :param x:        X location of view origin
        :param y:        Y location of view origin
        :param z:        Z location of view origin
        :param rx:       Rotation in X
        :param ry:       Rotation in Y
        :param rz:       Rotation in Z
        :param sx:       Scaling in X
        :param sy:       Scaling in Y
        :param str_val:  Scaling in Z
        :type  x:        float
        :type  y:        float
        :type  z:        float
        :type  rx:       float
        :type  ry:       float
        :type  rz:       float
        :type  sx:       float
        :type  sy:       float
        :type  str_val:  float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Sets up translation, scaling and rotation in all three directions
        for 3D objects.
        """
        self._set_3d_view(x, y, z, rx, ry, rz, sx, sy, str_val)
        




    def set_3d_view_ex(self, x, y, z, rx, ry, rz, sx, sy, str_val, rotate, flags):
        """
        Set 3D orientation parameters with new flags
        
        :param x:        X location of view origin
        :param y:        Y location of view origin
        :param z:        Z location of view origin
        :param rx:       Rotation in X
        :param ry:       Rotation in Y
        :param rz:       Rotation in Z
        :param sx:       Scaling in X
        :param sy:       Scaling in Y
        :param str_val:  Scaling in Z
        :param rotate:   :ref:`IPJ_3D_ROTATE`
        :param flags:    :ref:`IPJ_3D_FLAG`
        :type  x:        float
        :type  y:        float
        :type  z:        float
        :type  rx:       float
        :type  ry:       float
        :type  rz:       float
        :type  sx:       float
        :type  sy:       float
        :type  str_val:  float
        :type  rotate:   int
        :type  flags:    int

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Sets up translation, scaling and rotation in all three directions
        for 3D objects.
        """
        self._set_3d_view_ex(x, y, z, rx, ry, rz, sx, sy, str_val, rotate, flags)
        




    def set_3d_view_from_axes(self, x, y, z, x1, x2, x3, y1, y2, y3, sx, sy, str_val):
        """
        Set 3D orientation parameters
        
        :param x:        X location of view origin
        :param y:        Y location of view origin
        :param z:        Z location of view origin
        :param x1:       X axis X component
        :param x2:       X axis Y component
        :param x3:       X axis Z component
        :param y1:       Y axis X component
        :param y2:       Y axis Y component
        :param y3:       Y axis Z component
        :param sx:       Scaling in X
        :param sy:       Scaling in Y
        :param str_val:  Scaling in Z
        :type  x:        float
        :type  y:        float
        :type  z:        float
        :type  x1:       float
        :type  x2:       float
        :type  x3:       float
        :type  y1:       float
        :type  y2:       float
        :type  y3:       float
        :type  sx:       float
        :type  sy:       float
        :type  str_val:  float

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Sets up translation, scaling and rotation in all three directions
        for 3D objects, based on input origin and X and Y axis vectors.
        """
        self._set_3d_view_from_axes(x, y, z, x1, x2, x3, y1, y2, y3, sx, sy, str_val)
        




    def set_crooked_section_view(self, dist_vv, xvv, yvv, log_z):
        """
        Set up the crooked section view.
        
        :param dist_vv:  Section X locations (e.g. distance along the curve)
        :param xvv:      True X
        :param yvv:      True Y
        :param log_z:    Use logarithmic Y-axis (usually for data profiles) 0:No, 1:Yes
        :type  dist_vv:  GXVV
        :type  xvv:      GXVV
        :type  yvv:      GXVV
        :type  log_z:    int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A non-plane section. It is a vertical section which curves along a path in
        (X, Y).
        """
        self._set_crooked_section_view(dist_vv, xvv, yvv, log_z)
        




    def set_depth_section_view(self, depth):
        """
        Set depth section orientation parameters
        
        :param depth:  View Y value for Depth = 0.0.
        :type  depth:  float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_depth_section_view(depth)
        




    def set_esri(self, esri):
        """
        Set coordinate system from an ESRI prj coordinate string
        
        :param esri:  ESRI prj format projection string
        :type  esri:  str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the projection is not supported in Geosoft, the
        `GXIPJ <geosoft.gxapi.GXIPJ>` will be unknown.
        """
        self._set_esri(esri.encode())
        




    def set_gxf(self, str1, str2, str3, str4, str5):
        """
        Set coordinate system from GXF style strings.
        
        :param str1:  "projection name" or PCS_NAME from ipj_pcs.csv (datum / projection) or EPSG coordinate system code number or "<file.prj>" projection file name or "<file.wrp>" warp file name
        :param str2:  "datum name"[, major axis, elipticity, prime meridian] or DATUM from datum.csv or EPSG datum code number
        :param str3:  "method name", parameters (P1 through P8) or "projection name"[,"method name","Units",P1,P2...] or TRANSFORM from transform.csv or EPSG transform method code number
        :param str4:  "unit name", convertion to metres or UNIT_LENGTH from units.csv
        :param str5:  "local transform name"[,dX,dY,dZ,rX,rY,rZ,Scale] or DATUM_TRF from datumtrf.csv or AREA_OF_USE from ldatum.csv or EPSG local datum transform code number
        :type  str1:  str
        :type  str2:  str
        :type  str3:  str
        :type  str4:  str
        :type  str5:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Simplest Usage:

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
        self._set_gxf(str1.encode(), str2.encode(), str3.encode(), str4.encode(), str5.encode())
        




    def set_method_parm(self, parm, parm_value):
        """
        Set projection method parameter
        
        :param parm:        :ref:`IPJ_CSP`
        :param parm_value:  Parameter value
        :type  parm:        int
        :type  parm_value:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If parameter is not valid, nothing happens.
        """
        self._set_method_parm(parm, parm_value)
        




    def set_mi_coord_sys(self, coord, units):
        """
        Set coordinate system from a MapInfo coordsys command
        
        :param coord:  MapInfo Coordinate System
        :param units:  MapInfo Units
        :type  coord:  str
        :type  units:  str

        .. versionadded:: 5.1.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_mi_coord_sys(coord.encode(), units.encode())
        




    def set_normal_section_view(self, x, y, z, azimuth, swing):
        """
        Set normal section orientation parameters
        
        :param x:        X location of view origin
        :param y:        Y location of view origin
        :param z:        Z location of view origin
        :param azimuth:  Section azimuth - degrees CCW from north
        :param swing:    Section swing -90 < swing < 90.
        :type  x:        float
        :type  y:        float
        :type  z:        float
        :type  azimuth:  float
        :type  swing:    float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This section is the type where values are projected
        normal to the section, and the "Y" values in a grid
        do not necessarily correspond to the elvations for a swung section.
        """
        self._set_normal_section_view(x, y, z, azimuth, swing)
        




    def set_plan_view(self, x, y, z, rot):
        """
        Set plan orientation parameters.
        
        :param x:    X location of view origin
        :param y:    Y location of view origin
        :param z:    Z location of view origin
        :param rot:  Rotation CCW from normal XY coords
        :type  x:    float
        :type  y:    float
        :type  z:    float
        :type  rot:  float

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This sets up the orientation of an `GXIPJ <geosoft.gxapi.GXIPJ>` for plan view plots,
        for instance in Wholeplot. These differ from regular plan
        map views in that the elevation of the view plane is set, and
        the view may be rotated. In addition, when viewed in a map,
        a view with this `GXIPJ <geosoft.gxapi.GXIPJ>` will give a status bar location (X, Y, Z)
        of the actual location in space, as opposed to just the X, Y of
        the view plane itself.
        """
        self._set_plan_view(x, y, z, rot)
        




    def set_section_view(self, x, y, z, azimuth, swing):
        """
        Set section orientation parameters
        
        :param x:        X location of view origin
        :param y:        Y location of view origin
        :param z:        Z location of view origin
        :param azimuth:  Section azimuth - degrees CCW from north
        :param swing:    Section swing -90 < swing < 90.
        :type  x:        float
        :type  y:        float
        :type  z:        float
        :type  azimuth:  float
        :type  swing:    float

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This sets up the orientation of an `GXIPJ <geosoft.gxapi.GXIPJ>` for section view plots,
        for instance in Wholeplot. In addition, when viewed in a map,
        a view with this `GXIPJ <geosoft.gxapi.GXIPJ>` will give a status bar location (X, Y, Z)
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
        self._set_section_view(x, y, z, azimuth, swing)
        




    def set_wms_coord_sys(self, coord, min_x, min_y, max_x, max_y):
        """
        Set coordinate system from a WMS coordsys string.
        
        :param coord:  WMS style coordinate string
        :param min_x:  Minimum X bounding box
        :param min_y:  Minimum Y
        :param max_x:  Maximum X
        :param max_y:  Maximum Y
        :type  coord:  str
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** WMS coordinate strings supported:


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
        self._set_wms_coord_sys(coord.encode(), min_x, min_y, max_x, max_y)
        




    def set_xml(self, str_val):
        """
        Set an `GXIPJ <geosoft.gxapi.GXIPJ>` from a Geosoft Metadata XML string
        
        :param str_val:  XML string to set
        :type  str_val:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_xml(str_val.encode())
        




    def set_from_binary_as_string(self, str_val):
        """
        Set `GXIPJ <geosoft.gxapi.GXIPJ>` from binary-as-string
        
        :param str_val:  Binary as string
        :type  str_val:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_from_binary_as_string(str_val.encode())
        




    def get_from_binary_as_string(self, str_val):
        """
        Get `GXIPJ <geosoft.gxapi.GXIPJ>` from binary-as-string
        
        :param str_val:  Binary as string returned
        :type  str_val:  str_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        str_val.value = self._get_from_binary_as_string(str_val.value.encode())
        




    def get_3d_matrix_orientation(self, v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33):
        """
        Gets the coefficients of a 3D matrix orientation.
        
        :param v00:  Row 0 Element 0
        :param v01:  Row 0 Element 1
        :param v02:  Row 0 Element 2
        :param v03:  Row 0 Element 3
        :param v10:  Row 1 Element 0
        :param v11:  Row 1 Element 1
        :param v12:  Row 1 Element 2
        :param v13:  Row 1 Element 3
        :param v20:  Row 2 Element 0
        :param v21:  Row 2 Element 1
        :param v22:  Row 2 Element 2
        :param v23:  Row 2 Element 3
        :param v30:  Row 3 Element 0
        :param v31:  Row 3 Element 1
        :param v32:  Row 3 Element 2
        :param v33:  Row 3 Element 3
        :type  v00:  float_ref
        :type  v01:  float_ref
        :type  v02:  float_ref
        :type  v03:  float_ref
        :type  v10:  float_ref
        :type  v11:  float_ref
        :type  v12:  float_ref
        :type  v13:  float_ref
        :type  v20:  float_ref
        :type  v21:  float_ref
        :type  v22:  float_ref
        :type  v23:  float_ref
        :type  v30:  float_ref
        :type  v31:  float_ref
        :type  v32:  float_ref
        :type  v33:  float_ref

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        v00.value, v01.value, v02.value, v03.value, v10.value, v11.value, v12.value, v13.value, v20.value, v21.value, v22.value, v23.value, v30.value, v31.value, v32.value, v33.value = self._get_3d_matrix_orientation(v00.value, v01.value, v02.value, v03.value, v10.value, v11.value, v12.value, v13.value, v20.value, v21.value, v22.value, v23.value, v30.value, v31.value, v32.value, v33.value)
        




    def set_3d_matrix_orientation(self, v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33):
        """
        Apply a 3D orientation directly using matrix coefficients.
        
        :param v00:  Row 0 Element 0
        :param v01:  Row 0 Element 1
        :param v02:  Row 0 Element 2
        :param v03:  Row 0 Element 3
        :param v10:  Row 1 Element 0
        :param v11:  Row 1 Element 1
        :param v12:  Row 1 Element 2
        :param v13:  Row 1 Element 3
        :param v20:  Row 2 Element 0
        :param v21:  Row 2 Element 1
        :param v22:  Row 2 Element 2
        :param v23:  Row 2 Element 3
        :param v30:  Row 3 Element 0
        :param v31:  Row 3 Element 1
        :param v32:  Row 3 Element 2
        :param v33:  Row 3 Element 3
        :type  v00:  float
        :type  v01:  float
        :type  v02:  float
        :type  v03:  float
        :type  v10:  float
        :type  v11:  float
        :type  v12:  float
        :type  v13:  float
        :type  v20:  float
        :type  v21:  float
        :type  v22:  float
        :type  v23:  float
        :type  v30:  float
        :type  v31:  float
        :type  v32:  float
        :type  v33:  float

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_3d_matrix_orientation(v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33)
        




    def reproject_section_grid(self, output_ipj, x0, y0, dx, dy, rot):
        """
        Reproject a section grid
        
        :param output_ipj:  Reprojected `GXIPJ <geosoft.gxapi.GXIPJ>` on input (need not include an orientation). On output contains the same
                            						type of orientation as the initial `GXIPJ <geosoft.gxapi.GXIPJ>`, adjusted to be in the same location.
        :param x0:          X origin of grid (input initial value, output new value)
        :param y0:          Y origin of grid (input initial value, output new value)
        :param dx:          X cell size of grid (input initial value, output new value)
        :param dy:          Y cell size of grid (input initial value, output new value)
        :param rot:         Grid rotation (degrees CCW) (input initial value, output new value)
        :type  output_ipj:  GXIPJ
        :type  x0:          float_ref
        :type  y0:          float_ref
        :type  dx:          float_ref
        :type  dy:          float_ref
        :type  rot:         float_ref

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Reproject a section grid to a new `GXIPJ <geosoft.gxapi.GXIPJ>`, adjusting its orientation and registration so that
        it remains in the same location.
        """
        x0.value, y0.value, dx.value, dy.value, rot.value = self._reproject_section_grid(output_ipj, x0.value, y0.value, dx.value, dy.value, rot.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer