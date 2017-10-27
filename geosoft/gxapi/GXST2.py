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
class GXST2:
    """
    GXST2 class.

    Bi-variate statistics. The `GXST2 <geosoft.gxapi.GXST2>` class accumulates statistics
    on two data vectors simultaneously in order to compute correlation
    information. Statistics are accumulated using the `data_vv <geosoft.gxapi.GXST2.data_vv>` function.
    See also `GXST <geosoft.gxapi.GXST>` (mono-variate statistics).
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapST2(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXST2`
        
        :returns: A null `GXST2`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXST2` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXST2`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls):
        """
        Creates a statistics object which is used to accumulate statistics.
        

        :returns:    `GXST2 <geosoft.gxapi.GXST2>` Object
        :rtype:      GXST2

        .. versionadded:: 5.0
        """
        ret_val = gxapi_cy.WrapST2.create(GXContext._get_tls_geo())
        return GXST2(ret_val)




    def data_vv(self, vv_x, vv_y):
        """
        Add all the values in VVx and VVy to `GXST2 <geosoft.gxapi.GXST2>` object.
        
        :param vv_x:  VVx handle
        :param vv_y:  VVy handle
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV

        .. versionadded:: 5.0
        """
        self._wrapper.data_vv(vv_x._wrapper, vv_y._wrapper)
        






    def items(self):
        """
        Gets Number of items
        

        :returns:    Number of items in `GXST2 <geosoft.gxapi.GXST2>`
        :rtype:      int

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.items()
        return ret_val




    def reset(self):
        """
        Resets the Statistics.
        

        .. versionadded:: 5.0
        """
        self._wrapper.reset()
        




    def get(self, id):
        """
        Gets correlation coeff. from the `GXST2 <geosoft.gxapi.GXST2>` object.
        
        :param id:   `ST2_CORRELATION`
        :type  id:   int

        :returns:    Data you asked for
                     `GS_R8DM <geosoft.gxapi.GS_R8DM>` for none
        :rtype:      float

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.get(id)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer