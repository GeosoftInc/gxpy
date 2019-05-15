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
class GXST2(gxapi_cy.WrapST2):
    """
    GXST2 class.

    Bi-variate statistics. The `GXST2 <geosoft.gxapi.GXST2>` class accumulates statistics
    on two data vectors simultaneously in order to compute correlation
    information. Statistics are accumulated using the `data_vv <geosoft.gxapi.GXST2.data_vv>` function.
    See also `GXST <geosoft.gxapi.GXST>` (mono-variate statistics).
    """

    def __init__(self, handle=0):
        super(GXST2, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXST2 <geosoft.gxapi.GXST2>`
        
        :returns: A null `GXST2 <geosoft.gxapi.GXST2>`
        :rtype:   GXST2
        """
        return GXST2()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls):
        """
        Creates a statistics object which is used to accumulate statistics.
        

        :returns:    `GXST2 <geosoft.gxapi.GXST2>` Object
        :rtype:      GXST2

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapST2._create(GXContext._get_tls_geo())
        return GXST2(ret_val)




    def data_vv(self, vv_x, vv_y):
        """
        Add all the values in VVx and VVy to `GXST2 <geosoft.gxapi.GXST2>` object.
        
        :param vv_x:  VVx handle
        :param vv_y:  VVy handle
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._data_vv(vv_x, vv_y)
        






    def items(self):
        """
        Gets Number of items
        

        :returns:    Number of items in `GXST2 <geosoft.gxapi.GXST2>`
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._items()
        return ret_val




    def reset(self):
        """
        Resets the Statistics.
        

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._reset()
        




    def get(self, id):
        """
        Gets correlation coeff. from the `GXST2 <geosoft.gxapi.GXST2>` object.
        
        :param id:   :ref:`ST2_CORRELATION`
        :type  id:   int

        :returns:    Data you asked for
                     `GS_R8DM <geosoft.gxapi.GS_R8DM>` for none
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get(id)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer