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
class GXVOXE:
    """
    GXVOXE class.

    `GXVOX <geosoft.gxapi.GXVOX>` evaluator class. Used to sample values from
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
        Create a handle to an `GXVOXE <geosoft.gxapi.GXVOXE>` object
        
        :param vox:  `GXVOX <geosoft.gxapi.GXVOX>` Object
        :type  vox:  GXVOX

        :returns:    `GXVOXE <geosoft.gxapi.GXVOXE>` handle, terminates if creation fails
        :rtype:      GXVOXE

        .. versionadded:: 6.3
        """
        ret_val = gxapi_cy.WrapVOXE.create(GXContext._get_tls_geo(), vox._wrapper)
        return GXVOXE(ret_val)






    def profile(self, vv_x, vv_y, vv_z, vv_d, interp):
        """
        Extract a profile of data along points provided.
        
        :param vv_x:    X `GXVV <geosoft.gxapi.GXVV>` (must be double)
        :param vv_y:    Y `GXVV <geosoft.gxapi.GXVV>` (must be double)
        :param vv_z:    Z `GXVV <geosoft.gxapi.GXVV>` (must be double)
        :param vv_d:    D `GXVV <geosoft.gxapi.GXVV>` (must be double)
        :param interp:  `VOXE_EVAL`
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_z:    GXVV
        :type  vv_d:    GXVV
        :type  interp:  int

        .. versionadded:: 6.3
        """
        self._wrapper.profile(vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_d._wrapper, interp)
        




    def value(self, x, y, z, interp):
        """
        Get a value at a specific point
        
        :param x:       X Location
        :param y:       Y Location
        :param z:       Z Location
        :param interp:  `VOXE_EVAL`
        :type  x:       float
        :type  y:       float
        :type  z:       float
        :type  interp:  int

        :returns:       Value at the point or DUMMY if not valid
        :rtype:         float

        .. versionadded:: 6.3
        """
        ret_val = self._wrapper.value(x, y, z, interp)
        return ret_val




    def vector(self, ox, oy, oz, vx, vy, vz, vv, interp):
        """
        Extract a profile of data along a vector
        
        :param ox:      X Origin
        :param oy:      Y Origin
        :param oz:      Z Origin
        :param vx:      X Delta
        :param vy:      Y Delta
        :param vz:      Z Delta
        :param vv:      Data `GXVV <geosoft.gxapi.GXVV>` (must be double)
        :param interp:  `VOXE_EVAL`
        :type  ox:      float
        :type  oy:      float
        :type  oz:      float
        :type  vx:      float
        :type  vy:      float
        :type  vz:      float
        :type  vv:      GXVV
        :type  interp:  int

        .. versionadded:: 6.3
        """
        self._wrapper.vector(ox, oy, oz, vx, vy, vz, vv._wrapper, interp)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer