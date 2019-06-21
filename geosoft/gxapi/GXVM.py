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
class GXVM(gxapi_cy.WrapVM):
    """
    GXVM class.

    In-memory vector data methods
    The `GXVM <geosoft.gxapi.GXVM>` class will store vector (array) data in a memory buffer which
    can be accessed using the `GXVM <geosoft.gxapi.GXVM>` methods.
    The main use for the `GXVM <geosoft.gxapi.GXVM>` class is to store data in a single physical
    memory location.  This memory can then be accessed by a user DLL using
    the `GXGEO.get_ptr_vm <geosoft.gxapi.GXGEO.get_ptr_vm>` function defined in gx_extern.h.
    `GXVM <geosoft.gxapi.GXVM>` memory can be any size, but a `GXVM <geosoft.gxapi.GXVM>` is intended for handling relatively
    small sets of data compared to a `GXVV <geosoft.gxapi.GXVV>`, which can work efficiently with
    very large volumes of data.  The acceptable maximum `GXVM <geosoft.gxapi.GXVM>` size depends on
    the operating system and the performance requirements of an application.
    The best performance is achieved when all `GXVM <geosoft.gxapi.GXVM>` memory can be stored
    comfortably within the the available system RAM.  If all `GXVM <geosoft.gxapi.GXVM>` memory
    will not fit in the system RAM, the operating system virtual memory
    manager will be used to swap memory to the operations systems virtual
    memory paging file.  Note that the operating system virtual memory
    manager is much slower than the manager used by Geosoft when working with
    very large arrays in a `GXVV <geosoft.gxapi.GXVV>`.

    See `GXVV <geosoft.gxapi.GXVV>` for methods to move data between a `GXVM <geosoft.gxapi.GXVM>` and a `GXVV <geosoft.gxapi.GXVV>`.
    """

    def __init__(self, handle=0):
        super(GXVM, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVM <geosoft.gxapi.GXVM>`
        
        :returns: A null `GXVM <geosoft.gxapi.GXVM>`
        :rtype:   GXVM
        """
        return GXVM()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, type, elements):
        """
        Create a `GXVM <geosoft.gxapi.GXVM>`.
        
        :param type:      :ref:`GEO_VAR`
        :param elements:  `GXVM <geosoft.gxapi.GXVM>` length (less than 16777215)
        :type  type:      int
        :type  elements:  int

        :returns:         `GXVM <geosoft.gxapi.GXVM>` Object
        :rtype:           GXVM

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXVM <geosoft.gxapi.GXVM>` elements are initialized to dummies.
        """
        ret_val = gxapi_cy.WrapVM._create(GXContext._get_tls_geo(), type, elements)
        return GXVM(ret_val)



    @classmethod
    def create_ext(cls, type, elements):
        """
        Create a `GXVM <geosoft.gxapi.GXVM>`, using one of the :ref:`GS_TYPES` special data types.
        
        :param type:      :ref:`GS_TYPES`
        :param elements:  `GXVM <geosoft.gxapi.GXVM>` length (less than 16777215)
        :type  type:      int
        :type  elements:  int

        :returns:         `GXVM <geosoft.gxapi.GXVM>` Object
        :rtype:           GXVM

        .. versionadded:: 6.4.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXVM <geosoft.gxapi.GXVM>` elements are initialized to dummies.
        """
        ret_val = gxapi_cy.WrapVM._create_ext(GXContext._get_tls_geo(), type, elements)
        return GXVM(ret_val)






    def get_int(self, element):
        """
        Get an integer element from a `GXVM <geosoft.gxapi.GXVM>`.
        
        :param element:  Element wanted
        :type  element:  int

        :returns:        Element wanted, or `iDUMMY <geosoft.gxapi.iDUMMY>`
                         if the value is dummy or outside of the range of data.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_int(element)
        return ret_val




    def get_string(self, element, str_val):
        """
        Get a string element from a `GXVM <geosoft.gxapi.GXVM>`.
        
        :param element:  Element wanted
        :param str_val:  String in which to place element
        :type  element:  int
        :type  str_val:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns element wanted, or blank string
        if the value is dummy or outside of the range of data.

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        str_val.value = self._get_string(element, str_val.value.encode())
        




    def length(self):
        """
        Returns current `GXVM <geosoft.gxapi.GXVM>` length.
        

        :returns:    # of elements in the `GXVM <geosoft.gxapi.GXVM>`.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._length()
        return ret_val




    def re_size(self, newsize):
        """
        Re-set the size of a `GXVM <geosoft.gxapi.GXVM>`.
        
        :param newsize:  New size (number of elements)
        :type  newsize:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If increasing the `GXVM <geosoft.gxapi.GXVM>` size, new elements are set to dummies.
        """
        self._re_size(newsize)
        




    def get_double(self, element):
        """
        Get a real element from a `GXVM <geosoft.gxapi.GXVM>`.
        
        :param element:  Element wanted
        :type  element:  int

        :returns:        Element wanted, or `rDUMMY <geosoft.gxapi.rDUMMY>`
                         if the value is dummy or outside of the range of data.
        :rtype:          float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_double(element)
        return ret_val




    def set_int(self, element, value):
        """
        Set an integer element in a `GXVM <geosoft.gxapi.GXVM>`.
        
        :param element:  Element to set
        :param value:    Value to set
        :type  element:  int
        :type  value:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Element being set cannot be < 0.

        If the element is > current `GXVM <geosoft.gxapi.GXVM>` length, the `GXVM <geosoft.gxapi.GXVM>` length is
        increased.  Reallocating `GXVM <geosoft.gxapi.GXVM>` lengths can lead to fragmented
        memory and should be avoided if possible.
        """
        self._set_int(element, value)
        




    def set_double(self, element, value):
        """
        Set a real element in a `GXVM <geosoft.gxapi.GXVM>`.
        
        :param element:  Element to set
        :param value:    Value to set
        :type  element:  int
        :type  value:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Element being set cannot be < 0.

        If the element is > current `GXVM <geosoft.gxapi.GXVM>` length, the `GXVM <geosoft.gxapi.GXVM>` length is
        increased.  Reallocating `GXVM <geosoft.gxapi.GXVM>` lengths can lead to fragmented
        memory and should be avoided if possible.
        """
        self._set_double(element, value)
        




    def set_string(self, element, value):
        """
        Set a string element in a `GXVM <geosoft.gxapi.GXVM>`.
        
        :param element:  Element to set
        :param value:    String to set
        :type  element:  int
        :type  value:    str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Element being set cannot be < 0.

        If the element is > current `GXVM <geosoft.gxapi.GXVM>` length, the `GXVM <geosoft.gxapi.GXVM>` length is
        increased.  Reallocating `GXVM <geosoft.gxapi.GXVM>` lengths can lead to fragmented
        memory and should be avoided if possible.
        """
        self._set_string(element, value.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer