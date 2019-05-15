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
class GXREG(gxapi_cy.WrapREG):
    """
    GXREG class.

    The `GXREG <geosoft.gxapi.GXREG>` class is used for storing and retrieving named
    variables. Many classes contain `GXREG <geosoft.gxapi.GXREG>` objects for storing
    information particular to the class.  The `GXMETA <geosoft.gxapi.GXMETA>` class supersedes
    the `GXREG <geosoft.gxapi.GXREG>` class and is gradually replacing the use of the
    `GXREG <geosoft.gxapi.GXREG>` class in newer applications.
    """

    def __init__(self, handle=0):
        super(GXREG, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXREG <geosoft.gxapi.GXREG>`
        
        :returns: A null `GXREG <geosoft.gxapi.GXREG>`
        :rtype:   GXREG
        """
        return GXREG()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def clear(self):
        """
        Clears all the parameters in a `GXREG <geosoft.gxapi.GXREG>` object
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._clear()
        




    def copy(self, srce):
        """
        Copy
        
        :param srce:  Source
        :type  srce:  GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(srce)
        



    @classmethod
    def create(cls, l_parm_length):
        """
        Create a handle to a `GXREG <geosoft.gxapi.GXREG>` object
        
        :param l_parm_length:  Maximum size of "parameter=setting" string.
        :type  l_parm_length:  int

        :returns:              `GXREG <geosoft.gxapi.GXREG>` Object
        :rtype:                GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapREG._create(GXContext._get_tls_geo(), l_parm_length)
        return GXREG(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create a handle to a `GXREG <geosoft.gxapi.GXREG>` object from a `GXBF <geosoft.gxapi.GXBF>`
        
        :param bf:  `GXBF <geosoft.gxapi.GXBF>` handle for file containing serialized `GXREG <geosoft.gxapi.GXREG>`
        :type  bf:  GXBF

        :returns:    `GXREG <geosoft.gxapi.GXREG>` Object
        :rtype:      GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapREG._create_s(GXContext._get_tls_geo(), bf)
        return GXREG(ret_val)






    def get(self, parm, data):
        """
        Gets a string for a specified parameter in the `GXREG <geosoft.gxapi.GXREG>` object
        
        :param parm:  Name of the parameter
        :param data:  String to get
        :type  parm:  str
        :type  data:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        data.value = self._get(parm.encode(), data.value.encode())
        




    def get_int(self, parm, data):
        """
        Gets an int for a specified parameter in the `GXREG <geosoft.gxapi.GXREG>` object
        
        :param parm:  Name of the parameter
        :param data:  Int to get
        :type  parm:  str
        :type  data:  int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If parameter is not present in `GXREG <geosoft.gxapi.GXREG>`, `iDUMMY <geosoft.gxapi.iDUMMY>` is returned.
        """
        data.value = self._get_int(parm.encode(), data.value)
        




    def get_one(self, loc, parm, data):
        """
        Gets n-th entry of the `GXREG <geosoft.gxapi.GXREG>` object
        
        :param loc:   Sequential number of `GXREG <geosoft.gxapi.GXREG>` entry
        :param parm:  String to put parameter name
        :param data:  String to put data into.
        :type  loc:   int
        :type  parm:  str_ref
        :type  data:  str_ref

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        parm.value, data.value = self._get_one(loc, parm.value.encode(), data.value.encode())
        




    def get_double(self, parm, data):
        """
        Gets an real for a specified parameter in the `GXREG <geosoft.gxapi.GXREG>` object
        
        :param parm:  Name of the parameter
        :param data:  Real to get
        :type  parm:  str
        :type  data:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If parameter is not present in `GXREG <geosoft.gxapi.GXREG>`, `rDUMMY <geosoft.gxapi.rDUMMY>` is returned.
        """
        data.value = self._get_double(parm.encode(), data.value)
        




    def entries(self):
        """
        Get the number of parms in a `GXREG <geosoft.gxapi.GXREG>` object
        

        :returns:    Number of parms in a `GXREG <geosoft.gxapi.GXREG>` object.
        :rtype:      int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._entries()
        return ret_val




    def load_ini(self, ini):
        """
        Load a registry from an INI file.
        
        :param ini:  INI file name
        :type  ini:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Items are loaded into the `GXREG <geosoft.gxapi.GXREG>` in the format "GROUP.ITEM".
        """
        self._load_ini(ini.encode())
        




    def match_string(self, parm, data):
        """
        Replace a string with reg settings.
        
        :param parm:  String to Replace
        :param data:  Output Buffer
        :type  parm:  str
        :type  data:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        data.value = self._match_string(parm.encode(), data.value.encode())
        




    def merge(self, srce, type):
        """
        Merge
        
        :param srce:  Source
        :param type:  :ref:`REG_MERGE`
        :type  srce:  GXREG
        :type  type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._merge(srce, type)
        




    def save_ini(self, ini):
        """
        Save a `GXREG <geosoft.gxapi.GXREG>` to an INI file.
        
        :param ini:  INI file name
        :type  ini:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Only `GXREG <geosoft.gxapi.GXREG>` parameters in the form "GROUP.ITEM" are
        dumped to the INI file, because they match the INI format
        which groups items under [GROUP] headings.
        Single-word items (without a separating period) are skipped.
        """
        self._save_ini(ini.encode())
        




    def serial(self, bf):
        """
        Serialize a `GXREG <geosoft.gxapi.GXREG>` object into a file.
        
        :param bf:   `GXBF <geosoft.gxapi.GXBF>` to serialize `GXREG <geosoft.gxapi.GXREG>` into
        :type  bf:   GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial(bf)
        




    def set(self, parm, data):
        """
        Sets a string parameter in the `GXREG <geosoft.gxapi.GXREG>` object
        
        :param parm:  Name of the parameter
        :param data:  String to set it to An empty string sets the setting to an empty string, but does NOT remove the parameter from the `GXREG <geosoft.gxapi.GXREG>`.
        :type  parm:  str
        :type  data:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To remove a parameter completely, use one of the
        following:

        `set_int <geosoft.gxapi.GXREG.set_int>`(Reg, sParam, `iDUMMY <geosoft.gxapi.iDUMMY>`);
        or
        `set_double <geosoft.gxapi.GXREG.set_double>`(Reg, sParam, `rDUMMY <geosoft.gxapi.rDUMMY>`);
        """
        self._set(parm.encode(), data.encode())
        




    def set_int(self, parm, data):
        """
        Sets an int for a specified parameter in the `GXREG <geosoft.gxapi.GXREG>` object
        
        :param parm:  Name of the parameter
        :param data:  Int to set, `iDUMMY <geosoft.gxapi.iDUMMY>` to remove the parameter
        :type  parm:  str
        :type  data:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_int(parm.encode(), data)
        




    def set_double(self, parm, p3):
        """
        Sets an real for a specified parameter in the `GXREG <geosoft.gxapi.GXREG>` object
        
        :param parm:  Name of the parameter
        :param p3:    Real to set, `rDUMMY <geosoft.gxapi.rDUMMY>` to remove the parameter
        :type  parm:  str
        :type  p3:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_double(parm.encode(), p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer