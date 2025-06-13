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
class GXSHD(gxapi_cy.WrapSHD):
    """
    GXSHD class.

    This class supports fast interactive shadowing in a map or grid document.

    The SHD object is created using the
    StartShading_EMAP method.
    """

    def __init__(self, handle=0):
        super(GXSHD, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSHD <geosoft.gxapi.GXSHD>`
        
        :returns: A null `GXSHD <geosoft.gxapi.GXSHD>`
        :rtype:   GXSHD
        """
        return GXSHD()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def refresh(self, grid_path, inclination, declination, scale, contrast, brightness, wet_look):
        """
        
        Refresh the SHD with new shading parameters.
        
        :param grid_path:    Grid path returned
        :param inclination:  inclination (degrees)
        :param declination:  declination (degrees)
        :param scale:        vertical scale relative to base scale
        :param contrast:     contrast 0-1 (recommended >0.1, can change with wet_look changes)
        :param brightness:   brightness 0-1 (can change with wet_look changes)
        :param wet_look:     Apply wet-look effect (shading layer uses lighter distribution)?
        :type  grid_path:    str
        :type  inclination:  float
        :type  declination:  float
        :type  scale:        float
        :type  contrast:     float_ref
        :type  brightness:   float_ref
        :type  wet_look:     bool

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        
        contrast.value, brightness.value = self._refresh(grid_path.encode(), inclination, declination, scale, contrast.value, brightness.value, wet_look)
        




    def track_interactive(self, constraint, inclination, declination):
        """
        
        Track a line on map and get shading parameters based on its length and direction.
        
        :param constraint:   :ref:`SHD_FIX`
        :param inclination:  returned inclination
        :param declination:  returned declination
        :type  constraint:   int
        :type  inclination:  float_ref
        :type  declination:  float_ref

        :returns:            0 if tracking completed successfully.
                             1 if user cancelled or tracking failed.
        :rtype:              int

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        
        ret_val, inclination.value, declination.value = self._track_interactive(constraint, inclination.value, declination.value)
        return ret_val




    def end_shading(self, apply_changes):
        """
        
        This ends interactive shading and must be called if any interactive changes should be applied. Passing false to apply changes is equivalent to simply disposing handle.
        
        :param apply_changes:  Apply changes to map.
        :type  apply_changes:  bool

        .. versionadded:: 2021.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        .. seealso::

            StartShading_EMAP
        """
        
        self._end_shading(apply_changes)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer