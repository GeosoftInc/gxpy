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
class GXWA:
    """
    GXWA class.

    The `GXWA <geosoft.gxapi.GXWA>` class enables you to access and write data to ASCII files.
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
        A null (undefined) instance of `GXWA`
        
        :returns: A null `GXWA`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXWA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXWA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def puts(self, str_val):
        """
        Writes a string to the file.
        
        :param str_val:  String to write
        :type  str_val:  str

        .. versionadded:: 5.0
        """
        self._wrapper.puts(str_val.encode())
        



    @classmethod
    def create(cls, file, append):
        """
        Creates an ASCII file to write to.
        
        :param file:    Name of the File
        :param append:  :ref:`WA_OPEN`
        :type  file:    str
        :type  append:  int

        :returns:       `GXWA <geosoft.gxapi.GXWA>` Handle
        :rtype:         GXWA

        .. versionadded:: 5.0

        **Note:**

        ANSI Encoding is assumed, See `create_ex <geosoft.gxapi.GXWA.create_ex>` to override this.
        """
        ret_val = gxapi_cy.WrapWA.create(GXContext._get_tls_geo(), file.encode(), append)
        return GXWA(ret_val)



    @classmethod
    def create_ex(cls, file, append, encode):
        """
        Creates an ASCII file to write to.
        
        :param file:    Name of the File
        :param append:  :ref:`WA_OPEN`
        :param encode:  :ref:`WA_ENCODE`
        :type  file:    str
        :type  append:  int
        :type  encode:  int

        :returns:       `GXWA <geosoft.gxapi.GXWA>` Handle
        :rtype:         GXWA

        .. versionadded:: 6.2

        **Note:**

        Before version 6.2. text in on the GX API level were handled as characters in the current ANSI code page
        defining how characters above ASCII 127 would be displayed. 6.2. introduced Unicode in the core
        montaj engine that greatly increased the number of symbols that can be used. The :ref:`WA_ENCODE` constants
        were introduce that controls how text are written to files on disk with the `GXWA <geosoft.gxapi.GXWA>` class.
        """
        ret_val = gxapi_cy.WrapWA.create_ex(GXContext._get_tls_geo(), file.encode(), append, encode)
        return GXWA(ret_val)



    @classmethod
    def create_sbf(cls, sbf, file, append):
        """
        Creates an ASCII file to write to in an `GXSBF <geosoft.gxapi.GXSBF>`.
        
        :param sbf:     Storage
        :param file:    Name of the File
        :param append:  :ref:`WA_OPEN`
        :type  sbf:     GXSBF
        :type  file:    str
        :type  append:  int

        :returns:       `GXWA <geosoft.gxapi.GXWA>` Handle
        :rtype:         GXWA

        .. versionadded:: 5.0

        **Note:**

        See sbf.gxh. ANSI Encoding is assumed, See `create_sbf_ex <geosoft.gxapi.GXWA.create_sbf_ex>` to override this.
        """
        ret_val = gxapi_cy.WrapWA.create_sbf(GXContext._get_tls_geo(), sbf._wrapper, file.encode(), append)
        return GXWA(ret_val)



    @classmethod
    def create_sbf_ex(cls, sbf, file, append, encode):
        """
        Creates an ASCII file to write to in an `GXSBF <geosoft.gxapi.GXSBF>`.
        
        :param sbf:     Storage
        :param file:    Name of the File
        :param append:  :ref:`WA_OPEN`
        :param encode:  :ref:`WA_ENCODE`
        :type  sbf:     GXSBF
        :type  file:    str
        :type  append:  int
        :type  encode:  int

        :returns:       `GXWA <geosoft.gxapi.GXWA>` Handle
        :rtype:         GXWA

        .. versionadded:: 6.2

        **Note:**

        Also see sbf.gxh
        Before version 6.2. text in on the GX API level were handled as characters in the current ANSI code page
        defining how characters above ASCII 127 would be displayed. 6.2. introduced Unicode in the core
        montaj engine that greatly increased the number of symbols that can be used. The :ref:`WA_ENCODE` constants
        were introduce that controls how text are written to files on disk with the `GXWA <geosoft.gxapi.GXWA>` class.
        """
        ret_val = gxapi_cy.WrapWA.create_sbf_ex(GXContext._get_tls_geo(), sbf._wrapper, file.encode(), append, encode)
        return GXWA(ret_val)






    def new_line(self):
        """
        Forces a new line in the `GXWA <geosoft.gxapi.GXWA>` object.
        

        .. versionadded:: 5.0
        """
        self._wrapper.new_line()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer