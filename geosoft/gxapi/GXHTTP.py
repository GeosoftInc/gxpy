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
class GXHTTP(gxapi_cy.WrapHTTP):
    """
    GXHTTP class.

    Connect to an Internet Server using `GXHTTP <geosoft.gxapi.GXHTTP>`.

    **Note:**

    References:

    1. http://www.w3.org/Protocols/`GXHTTP <geosoft.gxapi.GXHTTP>`/HTTP2.html

    2. http://www.w3.org/Addressing/URL/5_BNF.html

    Note that path and search must conform be xalpha string (ref 2.).
    Special characters can be specified with a %xx, where xx is the
    hex ASCII number.  For example, a search string "This one" should
    be  specified as "This%20one"
    """

    def __init__(self, handle=0):
        super(GXHTTP, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXHTTP <geosoft.gxapi.GXHTTP>`
        
        :returns: A null `GXHTTP <geosoft.gxapi.GXHTTP>`
        :rtype:   GXHTTP
        """
        return GXHTTP()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, url, user_name, password, purpose):
        """
        This method creates a connection to an `GXHTTP <geosoft.gxapi.GXHTTP>` server
        
        :param url:        URL of the server
        :param user_name:  User name, "" for none
        :param password:   Password,  "" for none
        :param purpose:    Purpose of communication (for user verification)
        :type  url:        str
        :type  user_name:  str
        :type  password:   str
        :type  purpose:    str

        :returns:          `GXHTTP <geosoft.gxapi.GXHTTP>` Object
        :rtype:            GXHTTP

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** An OM user has the ability to control access and verification of access
        to servers over the Internet.  A GX Developer has no way to change the
        users choice of access.  This is to prevent the creation of GX's that
        may be dangerous or may be used to collect information without the
        knowledgede of the user.

        If the specified URL is restricted from access by the user, the create
        function will fail.

        If the specified URL has not been accessed by this user before, or if
        the user has this site on "Verify", the user will be presented with a
        dialog requiring verification before communication can begin.  The user
        may choose to change the server site to a full "Trust" relationship, in
        which case the verification message will not reappear unless the site
        is explicitly changed back to verify or is restricted.

        If you intend your GX to communicate with a server without
        verification, you must instruct your user to change their trust
        relationship with your server to "Trusted".  Your user will have the
        opportunity to do so the first time a script is run.
        """
        ret_val = gxapi_cy.WrapHTTP._create(GXContext._get_tls_geo(), url.encode(), user_name.encode(), password.encode(), purpose.encode())
        return GXHTTP(ret_val)






    def download(self, file, bf, dynamic):
        """
        Download file from the internet to a `GXBF <geosoft.gxapi.GXBF>`.
        
        :param file:     File Name on the `GXHTTP <geosoft.gxapi.GXHTTP>` site
        :param bf:       `GXBF <geosoft.gxapi.GXBF>` in which to place the file
        :param dynamic:  Dynamic content (0 - no, 1 - yes)
        :type  file:     str
        :type  bf:       GXBF
        :type  dynamic:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The file will be written starting at the current location
        in the `GXBF <geosoft.gxapi.GXBF>`
        """
        self._download(file.encode(), bf, dynamic)
        




    def silent_download(self, file, bf, dynamic):
        """
        Download file from the internet to a `GXBF <geosoft.gxapi.GXBF>` with no prompt for proxy authentication.
        
        :param file:     File Name on the `GXHTTP <geosoft.gxapi.GXHTTP>` site
        :param bf:       `GXBF <geosoft.gxapi.GXBF>` in which to place the file
        :param dynamic:  Dynamic content (0 - no, 1 - yes)
        :type  file:     str
        :type  bf:       GXBF
        :type  dynamic:  int

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The file will be written starting at the current location
        in the `GXBF <geosoft.gxapi.GXBF>`. No prompt for proxy authentication
        """
        self._silent_download(file.encode(), bf, dynamic)
        




    def get(self, cl, method, bf, ret_bf):
        """
        Get data from a server.
        
        :param cl:      Http path (file or an ISAPI DLL), no spaces
        :param method:  Http search string, no spaces
        :param bf:      Data to send
        :param ret_bf:  Data returned
        :type  cl:      str
        :type  method:  str
        :type  bf:      GXBF
        :type  ret_bf:  GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Full contents of the `GXBF <geosoft.gxapi.GXBF>` are sent in an `GXHTTP <geosoft.gxapi.GXHTTP>` GET message.
        `GXBF <geosoft.gxapi.GXBF>` pointer is returned to location before the call.

        request URL will be:
        http://server/path?search
        """
        self._get(cl.encode(), method.encode(), bf, ret_bf)
        




    def post(self, cl, method, bf):
        """
        Post data to the server.
        
        :param cl:      Http path (file or an ISAPI DLL)
        :param method:  Http search string, no spaces
        :param bf:      Data to post
        :type  cl:      str
        :type  method:  str
        :type  bf:      GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Full contents of the `GXBF <geosoft.gxapi.GXBF>` are sent as an `GXHTTP <geosoft.gxapi.GXHTTP>` POST message.

        request URL will be:
        http://server/path?search
        """
        self._post(cl.encode(), method.encode(), bf)
        




    def set_proxy_credentials(self, username, password):
        """
        Assigns the proxy username and password so that
        user is not prompted when the first download fails
        
        :param username:  Username
        :param password:  Password
        :type  username:  str
        :type  password:  str

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_proxy_credentials(username.encode(), password.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer