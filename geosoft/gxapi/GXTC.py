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
class GXTC(gxapi_cy.WrapTC):
    """
    GXTC class.

    The `GXTC <geosoft.gxapi.GXTC>` object is used in gravitational modelling to create
    a terrain correction grid from a topography grid. This is
    accomplished with a call first to `grregter <geosoft.gxapi.GXTC.grregter>`, which determines
    the terrain correction from an input topography grid, then
    to `grterain <geosoft.gxapi.GXTC.grterain>`, which calculates the actual corrections at
    the input positions.
    """

    def __init__(self, handle=0):
        super(GXTC, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTC <geosoft.gxapi.GXTC>`
        
        :returns: A null `GXTC <geosoft.gxapi.GXTC>`
        :rtype:   GXTC
        """
        return GXTC()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, img, elev_unit, dinner, douter, dens_t, dens_w, elev_w, edge, edge_elev, opt):
        """
        Creates a Terrain Correction object
        
        :param img:        Topo (DEM) grid
        :param elev_unit:  Elevation unit in 1 metre (i.e. 0.3048 for feet)
        :param dinner:     Inner distance (in topo grid projection units, default in metres)
        :param douter:     Outer distance (in topo grid projection units, default in metres)
        :param dens_t:     Terrain density in g/cc
        :param dens_w:     Water density in g/cc
        :param elev_w:     Water reference elevation (in elevation unit)
        :param edge:       1 to calculate an edge correction (compensation), 0 otherwise
        :param edge_elev:  Average elevation beyond max distance (in elevation unit)
        :param opt:        :ref:`TC_OPT`
        :type  img:        GXIMG
        :type  elev_unit:  float
        :type  dinner:     float
        :type  douter:     float
        :type  dens_t:     float
        :type  dens_w:     float
        :type  elev_w:     float
        :type  edge:       int
        :type  edge_elev:  float
        :type  opt:        int

        :returns:          `GXTC <geosoft.gxapi.GXTC>` Object
        :rtype:            GXTC

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapTC._create(GXContext._get_tls_geo(), img, elev_unit, dinner, douter, dens_t, dens_w, elev_w, edge, edge_elev, opt)
        return GXTC(ret_val)



    @classmethod
    def create_ex(cls, img, elev_unit, dinner, douter, dens_t, dens_w, elev_w, edge, edge_elev, opt, survey_type):
        """
        Creates a Terrain Correction object	with surveytype
        
        :param img:          Topo (DEM) grid
        :param elev_unit:    Elevation unit in 1 metre (i.e. 0.3048 for feet)
        :param dinner:       Inner distance (in topo grid projection units, default in metres)
        :param douter:       Outer distance (in topo grid projection units, default in metres)
        :param dens_t:       Terrain density in g/cc
        :param dens_w:       Water density in g/cc
        :param elev_w:       Water reference elevation (in elevation unit)
        :param edge:         1 to calculate an edge correction (compensation), 0 otherwise
        :param edge_elev:    Average elevation beyond max distance (in elevation unit)
        :param opt:          :ref:`TC_OPT`
        :param survey_type:  :ref:`TC_SURVEYTYPE`
        :type  img:          GXIMG
        :type  elev_unit:    float
        :type  dinner:       float
        :type  douter:       float
        :type  dens_t:       float
        :type  dens_w:       float
        :type  elev_w:       float
        :type  edge:         int
        :type  edge_elev:    float
        :type  opt:          int
        :type  survey_type:  int

        :returns:            `GXTC <geosoft.gxapi.GXTC>` Object
        :rtype:              GXTC

        .. versionadded:: 6.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapTC._create_ex(GXContext._get_tls_geo(), img, elev_unit, dinner, douter, dens_t, dens_w, elev_w, edge, edge_elev, opt, survey_type)
        return GXTC(ret_val)






    def grregter(self, im_gi, im_go):
        """
        Create a terrain correction grid for a topo grid.
        
        :param im_gi:  Input `GXIMG <geosoft.gxapi.GXIMG>` (local DEM topo grid used for station elevation)
        :param im_go:  Image of output grid
        :type  im_gi:  GXIMG
        :type  im_go:  GXIMG

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._grregter(im_gi, im_go)
        




    def grterain(self, gv_vx, gv_vy, gv_velev, gv_vslop, gv_vtcor, im_gcor, dens_t):
        """
        Calculate terrain corrections.
        
        :param gv_vx:     Input X channel data (in topo grid projection units, default in metres)
        :param gv_vy:     Input Y channel data (in topo grid projection units, default in metres)
        :param gv_velev:  Input Elevation channel data (in elevation unit)
        :param gv_vslop:  Input slope channel data
        :param gv_vtcor:  Output Terrain Corrected channel data
        :param im_gcor:   Image of input correction grid
        :param dens_t:    Terrain density (default 2.67)
        :type  gv_vx:     GXVV
        :type  gv_vy:     GXVV
        :type  gv_velev:  GXVV
        :type  gv_vslop:  GXVV
        :type  gv_vtcor:  GXVV
        :type  im_gcor:   GXIMG
        :type  dens_t:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._grterain(gv_vx, gv_vy, gv_velev, gv_vslop, gv_vtcor, im_gcor, dens_t)
        




    def grterain2(self, gv_vx, gv_vy, gv_velev, gv_vslop, gv_vwater, gv_vtcor, im_gcor, dens_t):
        """
        Calculate terrain corrections (work for marine gravity too).
        
        :param gv_vx:      Input X channel data (in topo grid projection units, default in metres)
        :param gv_vy:      Input Y channel data (in topo grid projection units, default in metres)
        :param gv_velev:   Input Elevation channel data (in elevation unit)
        :param gv_vslop:   Input slope channel data
        :param gv_vwater:  Input Water depth channel data (in metres)
        :param gv_vtcor:   Output Terrain Corrected channel data
        :param im_gcor:    Image of input correction grid
        :param dens_t:     Terrain density (default 2.67)
        :type  gv_vx:      GXVV
        :type  gv_vy:      GXVV
        :type  gv_velev:   GXVV
        :type  gv_vslop:   GXVV
        :type  gv_vwater:  GXVV
        :type  gv_vtcor:   GXVV
        :type  im_gcor:    GXIMG
        :type  dens_t:     float

        .. versionadded:: 6.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._grterain2(gv_vx, gv_vy, gv_velev, gv_vslop, gv_vwater, gv_vtcor, im_gcor, dens_t)
        




    def g_gterain(self, gv_vx, p3, p4, p5, p6, p7, p8):
        """
        Calculate GG terrain corrections
        
        :param gv_vx:  Input X channel data (in topo grid projection units, default in metres)
        :param p3:     Input Y channel data (in topo grid projection units, default in metres)
        :param p4:     Input Elevation channel data (in elevation unit)
        :param p5:     Output Terrain Corrected channel data
        :param p6:     Terrain density (default 2.67)
        :param p7:     Terrain reference level (default 0.0)
        :param p8:     :ref:`GG_ELEMENT`
        :type  gv_vx:  GXVV
        :type  p3:     GXVV
        :type  p4:     GXVV
        :type  p5:     GXVV
        :type  p6:     float
        :type  p7:     float
        :type  p8:     int

        .. versionadded:: 6.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._g_gterain(gv_vx, p3, p4, p5, p6, p7, p8)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer