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
class GXVOXE(gxapi_cy.WrapVOXE):
    """
    GXVOXE class.

    `GXVOX <geosoft.gxapi.GXVOX>` evaluator class. Used to sample values from
    the voxel.
    """

    def __init__(self, handle=0):
        super(GXVOXE, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVOXE <geosoft.gxapi.GXVOXE>`
        
        :returns: A null `GXVOXE <geosoft.gxapi.GXVOXE>`
        :rtype:   GXVOXE
        """
        return GXVOXE()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



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

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapVOXE._create(GXContext._get_tls_geo(), vox)
        return GXVOXE(ret_val)






    def profile(self, vv_x, vv_y, vv_z, vv_d, interp):
        """
        Extract a profile of data along points provided.
        
        :param vv_x:    X `GXVV <geosoft.gxapi.GXVV>` (must be double)
        :param vv_y:    Y `GXVV <geosoft.gxapi.GXVV>` (must be double)
        :param vv_z:    Z `GXVV <geosoft.gxapi.GXVV>` (must be double)
        :param vv_d:    D `GXVV <geosoft.gxapi.GXVV>` (must be double)
        :param interp:  :ref:`VOXE_EVAL`
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_z:    GXVV
        :type  vv_d:    GXVV
        :type  interp:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._profile(vv_x, vv_y, vv_z, vv_d, interp)
        




    def value(self, x, y, z, interp):
        """
        Get a value at a specific point
        
        :param x:       X Location
        :param y:       Y Location
        :param z:       Z Location
        :param interp:  :ref:`VOXE_EVAL`
        :type  x:       float
        :type  y:       float
        :type  z:       float
        :type  interp:  int

        :returns:       Value at the point or DUMMY if not valid
        :rtype:         float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._value(x, y, z, interp)
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
        :param interp:  :ref:`VOXE_EVAL`
        :type  ox:      float
        :type  oy:      float
        :type  oz:      float
        :type  vx:      float
        :type  vy:      float
        :type  vz:      float
        :type  vv:      GXVV
        :type  interp:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._vector(ox, oy, oz, vx, vy, vz, vv, interp)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer