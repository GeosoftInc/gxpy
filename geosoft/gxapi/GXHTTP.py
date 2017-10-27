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
class GXHTTP:
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

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapHTTP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXHTTP`
        
        :returns: A null `GXHTTP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXHTTP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXHTTP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, url, user_name, password, purpose):
        """
        This method creates a connection to an `GXHTTP <geosoft.gxapi.GXHTTP>` server

        **Note:**

        An OM user has the ability to control access and verification of access
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
        ret_val = gxapi_cy.WrapHTTP.create(GXContext._get_tls_geo(), url.encode(), user_name.encode(), password.encode(), purpose.encode())
        return GXHTTP(ret_val)






    def download(self, file, bf, dynamic):
        """
        Download file from the internet to a `GXBF <geosoft.gxapi.GXBF>`.

        **Note:**

        The file will be written starting at the current location
        in the `GXBF <geosoft.gxapi.GXBF>`
        """
        self._wrapper.download(file.encode(), bf._wrapper, dynamic)
        




    def silent_download(self, file, bf, dynamic):
        """
        Download file from the internet to a `GXBF <geosoft.gxapi.GXBF>` with no prompt for proxy authentication.

        **Note:**

        The file will be written starting at the current location
        in the `GXBF <geosoft.gxapi.GXBF>`. No prompt for proxy authentication
        """
        self._wrapper.silent_download(file.encode(), bf._wrapper, dynamic)
        




    def get(self, cl, method, bf, ret_bf):
        """
        Get data from a server.

        **Note:**

        Full contents of the `GXBF <geosoft.gxapi.GXBF>` are sent in an `GXHTTP <geosoft.gxapi.GXHTTP>` GET message.
        `GXBF <geosoft.gxapi.GXBF>` pointer is returned to location before the call.
        
        request URL will be:
        http://server/path?search
        """
        self._wrapper.get(cl.encode(), method.encode(), bf._wrapper, ret_bf._wrapper)
        




    def post(self, cl, method, bf):
        """
        Post data to the server.

        **Note:**

        Full contents of the `GXBF <geosoft.gxapi.GXBF>` are sent as an `GXHTTP <geosoft.gxapi.GXHTTP>` POST message.
        
        request URL will be:
        http://server/path?search
        """
        self._wrapper.post(cl.encode(), method.encode(), bf._wrapper)
        




    def set_proxy_credentials(self, username, password):
        """
        Assigns the proxy username and password so that
        user is not prompted when the first download fails
        """
        self._wrapper.set_proxy_credentials(username.encode(), password.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer