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
    The :class:`geosoft.gxapi.GXVM` class will store vector (array) data in a memory buffer which
    can be accessed using the :class:`geosoft.gxapi.GXVM` methods.
    The main use for the :class:`geosoft.gxapi.GXVM` class is to store data in a single physical
    memory location.  This memory can then be accessed by a user DLL using
    the GetPtrVM_GEO function defined in gx_extern.h.
    :class:`geosoft.gxapi.GXVM` memory can be any size, but a :class:`geosoft.gxapi.GXVM` is intended for handling relatively
    small sets of data compared to a :class:`geosoft.gxapi.GXVV`, which can work efficiently with
    very large volumes of data.  The acceptable maximum :class:`geosoft.gxapi.GXVM` size depends on
    the operating system and the performance requirements of an application.
    The best performance is achieved when all :class:`geosoft.gxapi.GXVM` memory can be stored
    comfortably within the the available system RAM.  If all :class:`geosoft.gxapi.GXVM` memory
    will not fit in the system RAM, the operating system virtual memory
    manager will be used to swap memory to the operations systems virtual
    memory paging file.  Note that the operating system virtual memory
    manager is much slower than the manager used by Geosoft when working with
    very large arrays in a :class:`geosoft.gxapi.GXVV`.
    
    See :class:`geosoft.gxapi.GXVV` for methods to move data between a :class:`geosoft.gxapi.GXVM` and a :class:`geosoft.gxapi.GXVV`.
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXVM`
        
        :returns: A null :class:`geosoft.gxapi.GXVM`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXVM` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXVM`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1, p2):
        """
        Create a :class:`geosoft.gxapi.GXVM`.

        **Note:**

        The :class:`geosoft.gxapi.GXVM` elements are initialized to dummies.
        """
        ret_val = gxapi_cy.WrapVM.create(GXContext._get_tls_geo(), p1, p2)
        return GXVM(ret_val)



    @classmethod
    def create_ext(cls, p1, p2):
        """
        Create a :class:`geosoft.gxapi.GXVM`, using one of the `GS_TYPES` special data types.

        **Note:**

        The :class:`geosoft.gxapi.GXVM` elements are initialized to dummies.
        """
        ret_val = gxapi_cy.WrapVM.create_ext(GXContext._get_tls_geo(), p1, p2)
        return GXVM(ret_val)






    def get_int(self, p2):
        """
        Get an integer element from a :class:`geosoft.gxapi.GXVM`.
        """
        ret_val = self._wrapper.get_int(p2)
        return ret_val




    def get_string(self, p2, p3):
        """
        Get a string element from a :class:`geosoft.gxapi.GXVM`.

        **Note:**

        Returns element wanted, or blank string
        if the value is dummy or outside of the range of data.
        
        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        p3.value = self._wrapper.get_string(p2, p3.value.encode())
        




    def length(self):
        """
        Returns current :class:`geosoft.gxapi.GXVM` length.
        """
        ret_val = self._wrapper.length()
        return ret_val




    def re_size(self, p2):
        """
        Re-set the size of a :class:`geosoft.gxapi.GXVM`.

        **Note:**

        If increasing the :class:`geosoft.gxapi.GXVM` size, new elements are set to dummies.
        """
        self._wrapper.re_size(p2)
        




    def get_double(self, p2):
        """
        Get a real element from a :class:`geosoft.gxapi.GXVM`.
        """
        ret_val = self._wrapper.get_double(p2)
        return ret_val




    def set_int(self, p2, p3):
        """
        Set an integer element in a :class:`geosoft.gxapi.GXVM`.

        **Note:**

        Element being set cannot be < 0.
        
        If the element is > current :class:`geosoft.gxapi.GXVM` length, the :class:`geosoft.gxapi.GXVM` length is
        increased.  Reallocating :class:`geosoft.gxapi.GXVM` lengths can lead to fragmented
        memory and should be avoided if possible.
        """
        self._wrapper.set_int(p2, p3)
        




    def set_double(self, p2, p3):
        """
        Set a real element in a :class:`geosoft.gxapi.GXVM`.

        **Note:**

        Element being set cannot be < 0.
        
        If the element is > current :class:`geosoft.gxapi.GXVM` length, the :class:`geosoft.gxapi.GXVM` length is
        increased.  Reallocating :class:`geosoft.gxapi.GXVM` lengths can lead to fragmented
        memory and should be avoided if possible.
        """
        self._wrapper.set_double(p2, p3)
        




    def set_string(self, p2, p3):
        """
        Set a string element in a :class:`geosoft.gxapi.GXVM`.

        **Note:**

        Element being set cannot be < 0.
        
        If the element is > current :class:`geosoft.gxapi.GXVM` length, the :class:`geosoft.gxapi.GXVM` length is
        increased.  Reallocating :class:`geosoft.gxapi.GXVM` lengths can lead to fragmented
        memory and should be avoided if possible.
        """
        self._wrapper.set_string(p2, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer