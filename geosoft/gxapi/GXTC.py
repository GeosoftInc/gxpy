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
class GXTC:
    """
    GXTC class.

    The `GXTC <geosoft.gxapi.GXTC>` object is used in gravitational modelling to create
    a terrain correction grid from a topography grid. This is
    accomplished with a call first to `grregter <geosoft.gxapi.GXTC.grregter>`, which determines
    the terrain correction from an input topography grid, then
    to `grterain <geosoft.gxapi.GXTC.grterain>`, which calculates the actual corrections at
    the input positions.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTC(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTC`
        
        :returns: A null `GXTC`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXTC` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXTC`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, img, elev_unit, dinner, douter, dens_t, dens_w, elev_w, edge, edge_elev, opt):
        """
        Creates a Terrain Correction object
        """
        ret_val = gxapi_cy.WrapTC.create(GXContext._get_tls_geo(), img._wrapper, elev_unit, dinner, douter, dens_t, dens_w, elev_w, edge, edge_elev, opt)
        return GXTC(ret_val)



    @classmethod
    def create_ex(cls, img, elev_unit, dinner, douter, dens_t, dens_w, elev_w, edge, edge_elev, opt, survey_type):
        """
        Creates a Terrain Correction object	with surveytype
        """
        ret_val = gxapi_cy.WrapTC.create_ex(GXContext._get_tls_geo(), img._wrapper, elev_unit, dinner, douter, dens_t, dens_w, elev_w, edge, edge_elev, opt, survey_type)
        return GXTC(ret_val)






    def grregter(self, im_gi, im_go):
        """
        Create a terrain correction grid for a topo grid.
        """
        self._wrapper.grregter(im_gi._wrapper, im_go._wrapper)
        




    def grterain(self, gv_vx, gv_vy, gv_velev, gv_vslop, gv_vtcor, im_gcor, dens_t):
        """
        Calculate terrain corrections.
        """
        self._wrapper.grterain(gv_vx._wrapper, gv_vy._wrapper, gv_velev._wrapper, gv_vslop._wrapper, gv_vtcor._wrapper, im_gcor._wrapper, dens_t)
        




    def grterain2(self, gv_vx, gv_vy, gv_velev, gv_vslop, gv_vwater, gv_vtcor, im_gcor, dens_t):
        """
        Calculate terrain corrections (work for marine gravity too).
        """
        self._wrapper.grterain2(gv_vx._wrapper, gv_vy._wrapper, gv_velev._wrapper, gv_vslop._wrapper, gv_vwater._wrapper, gv_vtcor._wrapper, im_gcor._wrapper, dens_t)
        




    def g_gterain(self, gv_vx, p3, p4, p5, p6, p7, p8):
        """
        Calculate GG terrain corrections
        """
        self._wrapper.g_gterain(gv_vx._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer