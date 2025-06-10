#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.

### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
import warnings
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVAU(gxapi_cy.WrapVAU):
    """
    GXVAU class.

    This is not a class. These are methods that work on
    data stored in `GXVA <geosoft.gxapi.GXVA>` objects
    """

    def __init__(self, handle=0):
        super(GXVAU, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVAU <geosoft.gxapi.GXVAU>`
        
        :returns: A null `GXVAU <geosoft.gxapi.GXVAU>`
        :rtype:   GXVAU
        """
        return GXVAU()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def cond_depth_tem(cls, resp_va, time_va, cond_va, depth_va, current, flag, min_xvv, min_yvv, max_xvv, max_yvv, t_moment, r_moment, array):
        """
        
        .. deprecated:: None None 
        Calculate TEM apparent conductivity and depth
        
        :param resp_va:   Response channel (microvolts)
        :param time_va:   Time channel (milliseconds)
        :param cond_va:   Conductivity channel (siemen/m)
        :param depth_va:  Depth (m)
        :param current:   Transmitter current
        :param flag:      Flag  Transmitter defined by moment (0) or by 4 VVs (1) below
        :param min_xvv:   Minimum X to define transmitter loop layout (moment)
        :param min_yvv:   Minimum Y to define transmitter loop layout (moment)
        :param max_xvv:   Maximum X to define transmitter loop layout (moment)
        :param max_yvv:   Maximum Y to define transmitter loop layout (moment)
        :param t_moment:  Transmitter moment (square meters), dummy if the above flag is 1
        :param r_moment:  Receiver moment (square meters)
        :param array:     :ref:`TEM_ARRAY`
        :type  resp_va:   GXVA
        :type  time_va:   GXVA
        :type  cond_va:   GXVA
        :type  depth_va:  GXVA
        :type  current:   float
        :type  flag:      int
        :type  min_xvv:   GXVV
        :type  min_yvv:   GXVV
        :type  max_xvv:   GXVV
        :type  max_yvv:   GXVV
        :type  t_moment:  float
        :type  r_moment:  float
        :type  array:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        warnings.warn("""Deprecated since unknown, """, )
        gxapi_cy.WrapVAU._cond_depth_tem(GXContext._get_tls_geo(), resp_va, time_va, cond_va, depth_va, current, flag, min_xvv, min_yvv, max_xvv, max_yvv, t_moment, r_moment, array)
        



    @classmethod
    def prune(cls, v_ap, vv_r, o):
        """
        
        Prune values from a `GXVA <geosoft.gxapi.GXVA>` based on reference `GXVA <geosoft.gxapi.GXVA>`
        
        :param v_ap:  `GXVA <geosoft.gxapi.GXVA>` to prune
        :param vv_r:  Reference `GXVV <geosoft.gxapi.GXVV>`
        :param o:     :ref:`VAU_PRUNE`
        :type  v_ap:  GXVA
        :type  vv_r:  GXVV
        :type  o:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Pruning will shorten the `GXVA <geosoft.gxapi.GXVA>` by removing values
        that are either dummy or non-dummy in the reference
        `GXVA <geosoft.gxapi.GXVA>`
        """
        
        gxapi_cy.WrapVAU._prune(GXContext._get_tls_geo(), v_ap, vv_r, o)
        



    @classmethod
    def section_cond_tem(cls, cond_va, depth_va, section, out_vv):
        """
        
        .. deprecated:: None None 
        Derive TEM apparent conductivity section at given depth
        
        :param cond_va:   Conductivity `GXVA <geosoft.gxapi.GXVA>`,`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`
        :param depth_va:  Depth `GXVA <geosoft.gxapi.GXVA>`,`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`
        :param section:   Depth derive TEM section (same unit as Depth `GXVA <geosoft.gxapi.GXVA>`)
        :param out_vv:    Returned conductivity at given depth,`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`
        :type  cond_va:   GXVA
        :type  depth_va:  GXVA
        :type  section:   float
        :type  out_vv:    GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        warnings.warn("""Deprecated since unknown, """, )
        gxapi_cy.WrapVAU._section_cond_tem(GXContext._get_tls_geo(), cond_va, depth_va, section, out_vv)
        



    @classmethod
    def total_vector(cls, xva, yva, zva, tva):
        """
        
        Calculate total vector for X,Y and Z components
        
        :param xva:  X Component object
        :param yva:  Y Component object
        :param zva:  Z Component object
        :param tva:  Returned total vector `GXVA <geosoft.gxapi.GXVA>` object
        :type  xva:  GXVA
        :type  yva:  GXVA
        :type  zva:  GXVA
        :type  tva:  GXVA

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVAU._total_vector(GXContext._get_tls_geo(), xva, yva, zva, tva)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer