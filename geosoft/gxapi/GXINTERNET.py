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
class GXINTERNET:
    """
    GXINTERNET class.

    This library provides functions for accessing the internet
    and MAPI-compliant e-mail services.
    Supported by Oasis montaj ONLY.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapINTERNET(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXINTERNET`
        
        :returns: A null `GXINTERNET`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXINTERNET` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXINTERNET`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def download_http(cls, url, file, size):
        """
        Download `GXHTTP <geosoft.gxapi.GXHTTP>` file from the internet to file.

        **Note:**

        The file must be stored on a server that supports
        the `GXHTTP <geosoft.gxapi.GXHTTP>` protocol and not require a password.

        .. seealso::

            iserver.gxh internet class.
        """
        ret_val = gxapi_cy.WrapINTERNET.download_http(GXContext._get_tls_geo(), url.encode(), file.encode(), size)
        return ret_val



    @classmethod
    def send_mail(cls, recipient, p2, p3, p4, p5, p6, p7, p8):
        """
        Prepaire an email for the user.

        **Note:**

        Requires a MAPI complient mail system to be installed
        on the client machine.
        """
        gxapi_cy.WrapINTERNET.send_mail(GXContext._get_tls_geo(), recipient.encode(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer