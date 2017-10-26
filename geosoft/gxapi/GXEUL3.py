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
class GXEUL3:
    """
    GXEUL3 class.

    This is a specialized class which performs 3D Euler deconvolution
    for potential field interpretation.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEUL3(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEUL3`
        
        :returns: A null `GXEUL3`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXEUL3` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXEUL3`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def destr(self):
        """
        Destroys a `GXEUL3` object.
        """
        self._wrapper.destr()
        



    @classmethod
    def creat(cls, imgt, imgtx, imgty, imgtz, wnd_siz, p6, p7, p8, p9, p10, p11):
        """
        Creates an `GXEUL3` object.
        """
        ret_val = gxapi_cy.WrapEUL3.creat(GXContext._get_tls_geo(), imgt._wrapper, imgtx._wrapper, imgty._wrapper, imgtz._wrapper, wnd_siz, p6, p7, p8, p9, p10, p11)
        return GXEUL3(ret_val)




    def get_result(self, v_vr, pi_res_field):
        """
        Get a result field `GXVV` from `GXEUL3` object
        """
        self._wrapper.get_result(v_vr._wrapper, pi_res_field)
        




    def write(self, out_fil):
        """
        Write the results of `GXEUL3` object to output file.
        """
        self._wrapper.write(out_fil.encode())
        



    @classmethod
    def ex_euler_derive(cls, v_vdist, pr_dx, v_vmag, length, v_vgx, v_vgz, max_sol):
        """
        Calculates gradients
        """
        ret_val = gxapi_cy.WrapEUL3.ex_euler_derive(GXContext._get_tls_geo(), v_vdist._wrapper, pr_dx, v_vmag._wrapper, length, v_vgx._wrapper, v_vgz._wrapper, max_sol)
        return ret_val



    @classmethod
    def ex_euler_calc(cls, typ, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20):
        """
        Does the exeuler depth calculations
        """
        ret_val = gxapi_cy.WrapEUL3.ex_euler_calc(GXContext._get_tls_geo(), typ, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper, p13._wrapper, p14._wrapper, p15._wrapper, p16, p17._wrapper, p18._wrapper, p19._wrapper, p20._wrapper)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer