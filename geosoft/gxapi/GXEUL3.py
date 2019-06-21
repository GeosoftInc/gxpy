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
class GXEUL3(gxapi_cy.WrapEUL3):
    """
    GXEUL3 class.

    This is a specialized class which performs 3D Euler deconvolution
    for potential field interpretation.
    """

    def __init__(self, handle=0):
        super(GXEUL3, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEUL3 <geosoft.gxapi.GXEUL3>`
        
        :returns: A null `GXEUL3 <geosoft.gxapi.GXEUL3>`
        :rtype:   GXEUL3
        """
        return GXEUL3()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def destr(self):
        """
        Destroys a `GXEUL3 <geosoft.gxapi.GXEUL3>` object.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._destr()
        



    @classmethod
    def creat(cls, imgt, imgtx, imgty, imgtz, wnd_siz, gi, tolrnc, max_dis, obs_flg, obs_hght, obs_elev):
        """
        Creates an `GXEUL3 <geosoft.gxapi.GXEUL3>` object.
        
        :param imgt:      Image of grid T
        :param imgtx:     Image of grid Tx
        :param imgty:     Image of grid Ty
        :param imgtz:     Image of grid Tz
        :param wnd_siz:   Window size (maximum 20)
        :param gi:        Geometric index, from 0.0 to 3.0
        :param tolrnc:    Max tolerance to allow (percentage)
        :param max_dis:   Max dist. acceptable (0 for infinite)
        :param obs_flg:   ObsFlg  Height (0) or Elevation (1)
        :param obs_hght:  Height of observation plane
        :param obs_elev:  Elevation of observation plane
        :type  imgt:      GXIMG
        :type  imgtx:     GXIMG
        :type  imgty:     GXIMG
        :type  imgtz:     GXIMG
        :type  wnd_siz:   int
        :type  gi:        float
        :type  tolrnc:    float
        :type  max_dis:   float
        :type  obs_flg:   int
        :type  obs_hght:  float
        :type  obs_elev:  float

        :returns:         `GXEUL3 <geosoft.gxapi.GXEUL3>` Object
        :rtype:           GXEUL3

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapEUL3._creat(GXContext._get_tls_geo(), imgt, imgtx, imgty, imgtz, wnd_siz, gi, tolrnc, max_dis, obs_flg, obs_hght, obs_elev)
        return GXEUL3(ret_val)




    def get_result(self, vv_r, pi_res_field):
        """
        Get a result field `GXVV <geosoft.gxapi.GXVV>` from `GXEUL3 <geosoft.gxapi.GXEUL3>` object
        
        :param vv_r:          `GXVV <geosoft.gxapi.GXVV>` to store the result
        :param pi_res_field:  :ref:`EUL3_RESULT`
        :type  vv_r:          GXVV
        :type  pi_res_field:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._get_result(vv_r, pi_res_field)
        




    def write(self, out_fil):
        """
        Write the results of `GXEUL3 <geosoft.gxapi.GXEUL3>` object to output file.
        
        :param out_fil:  Output File Name
        :type  out_fil:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._write(out_fil.encode())
        



    @classmethod
    def ex_euler_derive(cls, vv_dist, pr_dx, vv_mag, length, vv_gx, vv_gz, max_sol):
        """
        Calculates gradients
        
        :param vv_dist:  Input distance
        :param pr_dx:    Sample Interval
        :param vv_mag:   Input mag
        :param length:   SampleCount
        :param vv_gx:    Horizontal Gradient out
        :param vv_gz:    Vertical Gradient out
        :param max_sol:  Output array size limit
        :type  vv_dist:  GXVV
        :type  pr_dx:    float
        :type  vv_mag:   GXVV
        :type  length:   int
        :type  vv_gx:    GXVV
        :type  vv_gz:    GXVV
        :type  max_sol:  int

        :returns:        0 for OK, -1 for Error
        :rtype:          int

        .. versionadded:: 9.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapEUL3._ex_euler_derive(GXContext._get_tls_geo(), vv_dist, pr_dx, vv_mag, length, vv_gx, vv_gz, max_sol)
        return ret_val



    @classmethod
    def ex_euler_calc(cls, typ, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20):
        """
        Does the exeuler depth calculations
        
        :param typ:  Solution type flag (0 for contacts, 1 for dykes)
        :param p2:   Structural index value (used only when generating dykes)
        :param p3:   Window length
        :param p4:   Field strength in nT
        :param p5:   Inclination
        :param p6:   Declination
        :param p7:   Profile azimuth wrt north
        :param p8:   Minimum depth for returned solutions
        :param p9:   Maximum depth for returned solutions
        :param p10:  Percentage error allowed before rejection
        :param p11:  Number of points in profile
        :param p12:  Array of point distances along profile
        :param p13:  Array of observed values
        :param p14:  Array of horizontal derivative values. Can be NULL for calculated
        :param p15:  Array of vertical derivative values. Can be NULL for calculated
        :param p16:  Length of solutions arrays passed in
        :param p17:  The profile distance for each solution
        :param p18:  The depth for each solution
        :param p19:  The dip for each solution
        :param p20:  The susceptibility for each solution
        :type  typ:  int
        :type  p2:   float
        :type  p3:   int
        :type  p4:   float
        :type  p5:   float
        :type  p6:   float
        :type  p7:   float
        :type  p8:   float
        :type  p9:   float
        :type  p10:  float
        :type  p11:  int
        :type  p12:  GXVV
        :type  p13:  GXVV
        :type  p14:  GXVV
        :type  p15:  GXVV
        :type  p16:  int
        :type  p17:  GXVV
        :type  p18:  GXVV
        :type  p19:  GXVV
        :type  p20:  GXVV

        :returns:    >0 for OK, -1 for Error
        :rtype:      int

        .. versionadded:: 9.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapEUL3._ex_euler_calc(GXContext._get_tls_geo(), typ, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer