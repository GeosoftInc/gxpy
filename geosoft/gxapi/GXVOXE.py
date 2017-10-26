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
class GXVOXE:
    """
    GXVOXE class.

    `GXVOX` evaluator class. Used to sample values from
    the voxel.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVOXE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVOXE`
        
        :returns: A null `GXVOXE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVOXE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVOXE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, vox):
        """
        Create a handle to an `GXVOXE` object
        """
        ret_val = gxapi_cy.WrapVOXE.create(GXContext._get_tls_geo(), vox._wrapper)
        return GXVOXE(ret_val)






    def profile(self, v_vx, v_vy, v_vz, v_vd, interp):
        """
        Extract a profile of data along points provided.
        """
        self._wrapper.profile(v_vx._wrapper, v_vy._wrapper, v_vz._wrapper, v_vd._wrapper, interp)
        




    def value(self, x, y, z, interp):
        """
        Get a value at a specific point
        """
        ret_val = self._wrapper.value(x, y, z, interp)
        return ret_val




    def vector(self, ox, oy, oz, vx, vy, vz, vv, interp):
        """
        Extract a profile of data along a vector
        """
        self._wrapper.vector(ox, oy, oz, vx, vy, vz, vv._wrapper, interp)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer