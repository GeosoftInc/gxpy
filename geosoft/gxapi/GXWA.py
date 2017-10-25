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
class GXWA:
    """
    GXWA class.

    The :class:`geosoft.gxapi.GXWA` class enables you to access and write data to ASCII files.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapWA(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXWA`
        
        :returns: A null :class:`geosoft.gxapi.GXWA`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXWA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXWA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def puts(self, p2):
        """
        Writes a string to the file.
        """
        self._wrapper.puts(p2.encode())
        



    @classmethod
    def create(cls, p1, p2):
        """
        Creates an ASCII file to write to.

        **Note:**

        ANSI Encoding is assumed, See CreateEx_WA to override this.
        """
        ret_val = gxapi_cy.WrapWA.create(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXWA(ret_val)



    @classmethod
    def create_ex(cls, p1, p2, p3):
        """
        Creates an ASCII file to write to.

        **Note:**

        Before version 6.2. text in on the GX API level were handled as characters in the current ANSI code page
        defining how characters above ASCII 127 would be displayed. 6.2. introduced Unicode in the core
        montaj engine that greatly increased the number of symbols that can be used. The `WA_ENCODE` constants
        were introduce that controls how text are written to files on disk with the :class:`geosoft.gxapi.GXWA` class.
        """
        ret_val = gxapi_cy.WrapWA.create_ex(GXContext._get_tls_geo(), p1.encode(), p2, p3)
        return GXWA(ret_val)



    @classmethod
    def create_sbf(cls, p1, p2, p3):
        """
        Creates an ASCII file to write to in an :class:`geosoft.gxapi.GXSBF`.

        **Note:**

        See sbf.gxh. ANSI Encoding is assumed, See CreateSBFEx_WA to override this.
        """
        ret_val = gxapi_cy.WrapWA.create_sbf(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        return GXWA(ret_val)



    @classmethod
    def create_sbf_ex(cls, p1, p2, p3, p4):
        """
        Creates an ASCII file to write to in an :class:`geosoft.gxapi.GXSBF`.

        **Note:**

        Also see sbf.gxh
        Before version 6.2. text in on the GX API level were handled as characters in the current ANSI code page
        defining how characters above ASCII 127 would be displayed. 6.2. introduced Unicode in the core
        montaj engine that greatly increased the number of symbols that can be used. The `WA_ENCODE` constants
        were introduce that controls how text are written to files on disk with the :class:`geosoft.gxapi.GXWA` class.
        """
        ret_val = gxapi_cy.WrapWA.create_sbf_ex(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        return GXWA(ret_val)






    def new_line(self):
        """
        Forces a new line in the :class:`geosoft.gxapi.GXWA` object.
        """
        self._wrapper.new_line()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer