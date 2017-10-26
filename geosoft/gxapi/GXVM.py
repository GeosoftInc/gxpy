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
class GXVM:
    """
    GXVM class.

    In-memory vector data methods
    The `GXVM` class will store vector (array) data in a memory buffer which
    can be accessed using the `GXVM` methods.
    The main use for the `GXVM` class is to store data in a single physical
    memory location.  This memory can then be accessed by a user DLL using
    the `GXGEO.get_ptr_vm` function defined in gx_extern.h.
    `GXVM` memory can be any size, but a `GXVM` is intended for handling relatively
    small sets of data compared to a `GXVV`, which can work efficiently with
    very large volumes of data.  The acceptable maximum `GXVM` size depends on
    the operating system and the performance requirements of an application.
    The best performance is achieved when all `GXVM` memory can be stored
    comfortably within the the available system RAM.  If all `GXVM` memory
    will not fit in the system RAM, the operating system virtual memory
    manager will be used to swap memory to the operations systems virtual
    memory paging file.  Note that the operating system virtual memory
    manager is much slower than the manager used by Geosoft when working with
    very large arrays in a `GXVV`.
    
    See `GXVV` for methods to move data between a `GXVM` and a `GXVV`.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVM(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVM`
        
        :returns: A null `GXVM`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVM` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVM`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, type, elements):
        """
        Create a `GXVM`.

        **Note:**

        The `GXVM` elements are initialized to dummies.
        """
        ret_val = gxapi_cy.WrapVM.create(GXContext._get_tls_geo(), type, elements)
        return GXVM(ret_val)



    @classmethod
    def create_ext(cls, type, elements):
        """
        Create a `GXVM`, using one of the `GS_TYPES` special data types.

        **Note:**

        The `GXVM` elements are initialized to dummies.
        """
        ret_val = gxapi_cy.WrapVM.create_ext(GXContext._get_tls_geo(), type, elements)
        return GXVM(ret_val)






    def get_int(self, element):
        """
        Get an integer element from a `GXVM`.
        """
        ret_val = self._wrapper.get_int(element)
        return ret_val




    def get_string(self, element, str_val):
        """
        Get a string element from a `GXVM`.

        **Note:**

        Returns element wanted, or blank string
        if the value is dummy or outside of the range of data.
        
        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        str_val.value = self._wrapper.get_string(element, str_val.value.encode())
        




    def length(self):
        """
        Returns current `GXVM` length.
        """
        ret_val = self._wrapper.length()
        return ret_val




    def re_size(self, newsize):
        """
        Re-set the size of a `GXVM`.

        **Note:**

        If increasing the `GXVM` size, new elements are set to dummies.
        """
        self._wrapper.re_size(newsize)
        




    def get_double(self, element):
        """
        Get a real element from a `GXVM`.
        """
        ret_val = self._wrapper.get_double(element)
        return ret_val




    def set_int(self, element, value):
        """
        Set an integer element in a `GXVM`.

        **Note:**

        Element being set cannot be < 0.
        
        If the element is > current `GXVM` length, the `GXVM` length is
        increased.  Reallocating `GXVM` lengths can lead to fragmented
        memory and should be avoided if possible.
        """
        self._wrapper.set_int(element, value)
        




    def set_double(self, element, value):
        """
        Set a real element in a `GXVM`.

        **Note:**

        Element being set cannot be < 0.
        
        If the element is > current `GXVM` length, the `GXVM` length is
        increased.  Reallocating `GXVM` lengths can lead to fragmented
        memory and should be avoided if possible.
        """
        self._wrapper.set_double(element, value)
        




    def set_string(self, element, value):
        """
        Set a string element in a `GXVM`.

        **Note:**

        Element being set cannot be < 0.
        
        If the element is > current `GXVM` length, the `GXVM` length is
        increased.  Reallocating `GXVM` lengths can lead to fragmented
        memory and should be avoided if possible.
        """
        self._wrapper.set_string(element, value.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer