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
class GXINTERNET(gxapi_cy.WrapINTERNET):
    """
    GXINTERNET class.

    This library provides functions for accessing the internet
    and MAPI-compliant e-mail services.
    Supported by Oasis montaj ONLY.
    """

    def __init__(self, handle=0):
        super(GXINTERNET, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXINTERNET <geosoft.gxapi.GXINTERNET>`
        
        :returns: A null `GXINTERNET <geosoft.gxapi.GXINTERNET>`
        :rtype:   GXINTERNET
        """
        return GXINTERNET()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def download_http(cls, url, file, size):
        """
        Download `GXHTTP <geosoft.gxapi.GXHTTP>` file from the internet to file.
        
        :param url:   `GXHTTP <geosoft.gxapi.GXHTTP>` URL
        :param file:  File Name to save to
        :param size:  No longer used, just pass 0
        :type  url:   str
        :type  file:  str
        :type  size:  int

        :returns:     0 - Ok
                      1 - Error
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The file must be stored on a server that supports
        the `GXHTTP <geosoft.gxapi.GXHTTP>` protocol and not require a password.

        .. seealso::

            iserver.gxh internet class.
        """
        ret_val = gxapi_cy.WrapINTERNET._download_http(GXContext._get_tls_geo(), url.encode(), file.encode(), size)
        return ret_val



    @classmethod
    def send_mail(cls, recipient, p2, p3, p4, p5, p6, p7, p8):
        """
        Prepaire an email for the user.
        
        :param recipient:  Recipient Name        ("" for none)
        :param p2:         Recipient Address     ("" for none)
        :param p3:         szSubject             ("" for none)
        :param p4:         Message Text          ("" for none)
        :param p5:         Attachment1 File Name ("" for none)
        :param p6:         Attachment1 User Name ("" for none)
        :param p7:         Attachment2 File Name ("" for none)
        :param p8:         Attachment2 User Name ("" for none)
        :type  recipient:  str
        :type  p2:         str
        :type  p3:         str
        :type  p4:         str
        :type  p5:         str
        :type  p6:         str
        :type  p7:         str
        :type  p8:         str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Requires a MAPI complient mail system to be installed
        on the client machine.
        """
        gxapi_cy.WrapINTERNET._send_mail(GXContext._get_tls_geo(), recipient.encode(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer