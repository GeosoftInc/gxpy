### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXSTK import GXSTK


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMSTK(gxapi_cy.WrapMSTK):
    """
    GXMSTK class.

    Multi-profile stack
    This class is used for storing data of multiple profiles and
    plotting profiles in a map. It is a container of `GXSTK <geosoft.gxapi.GXSTK>` class objects.

    See also:         `GXSTK <geosoft.gxapi.GXSTK>` class.
    """

    def __init__(self, handle=0):
        super(GXMSTK, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMSTK <geosoft.gxapi.GXMSTK>`
        
        :returns: A null `GXMSTK <geosoft.gxapi.GXMSTK>`
        :rtype:   GXMSTK
        """
        return GXMSTK()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def add_stk(self):
        """
        Create and add a `GXSTK <geosoft.gxapi.GXSTK>` object to `GXMSTK <geosoft.gxapi.GXMSTK>`
        

        :returns:     `GXSTK <geosoft.gxapi.GXSTK>`, fail if error
        :rtype:       GXSTK

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Index to the added `GXSTK <geosoft.gxapi.GXSTK>` object is the last one in `GXMSTK <geosoft.gxapi.GXMSTK>` container.
        """
        ret_val = self._add_stk()
        return GXSTK(ret_val)




    def chan_list_vv(self, db, num_ch_vv, str_ch_vv, x_ch_vv, prof_ch_vv, prof_ch__un_used_vv):
        """
        Save channel names in VVs based on channel types
        
        :param db:                   Database handle
        :param num_ch_vv:            List of names of numeric channels
        :param str_ch_vv:            List of name of string channels
        :param x_ch_vv:              List of channel names which can be used for X axis. Must be numeric channels but not `GXVA <geosoft.gxapi.GXVA>` channels
        :param prof_ch_vv:           List of profiles with channel names in both `GXMSTK <geosoft.gxapi.GXMSTK>` and `GXDB <geosoft.gxapi.GXDB>`
        :param prof_ch__un_used_vv:  List of profiles with channels in `GXMSTK <geosoft.gxapi.GXMSTK>` but not in database
        :type  db:                   GXDB
        :type  num_ch_vv:            GXVV
        :type  str_ch_vv:            GXVV
        :type  x_ch_vv:              GXVV
        :type  prof_ch_vv:           GXVV
        :type  prof_ch__un_used_vv:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Terms 'used' and 'unused' indicate that the a channel name
        in database also 'in' and 'not in' the `GXMSTK <geosoft.gxapi.GXMSTK>` object respectively
        """
        self._chan_list_vv(db, num_ch_vv, str_ch_vv, x_ch_vv, prof_ch_vv, prof_ch__un_used_vv)
        



    @classmethod
    def create(cls):
        """
        Create `GXMSTK <geosoft.gxapi.GXMSTK>`.
        

        :returns:    `GXMSTK <geosoft.gxapi.GXMSTK>`, aborts if creation fails
        :rtype:      GXMSTK

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapMSTK._create(GXContext._get_tls_geo())
        return GXMSTK(ret_val)






    def draw_profile(self, db, line, map):
        """
        Draw multiple profiles in map
        
        :param db:    Database handle
        :param line:  Database line
        :param map:   `GXMAP <geosoft.gxapi.GXMAP>` handle
        :type  db:    GXDB
        :type  line:  int
        :type  map:   GXMAP

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._draw_profile(db, line, map)
        




    def set_y_axis_direction(self, direction):
        """
        Set the Y-axis direction - normal or inverted
        
        :param direction:  Y-axis direction: 0 - normal, 1 - inverted
        :type  direction:  int

        .. versionadded:: 8.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_y_axis_direction(direction)
        




    def find_stk2(self, str_val, index, vv_rtd):
        """
        Find index of `GXSTK <geosoft.gxapi.GXSTK>` from a string of group names and X/Y channels
        
        :param str_val:  Input string (see notes above). Will be modified on return
        :param index:    Index to the `GXSTK <geosoft.gxapi.GXSTK>` found, Must be greater than 0 if found, -1 if not found
        :param vv_rtd:   Returned `GXVV <geosoft.gxapi.GXVV>` with names of Group, X channel and Y channel `GXVV <geosoft.gxapi.GXVV>` type must be of STRING
        :type  str_val:  str
        :type  index:    int_ref
        :type  vv_rtd:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Format of the input string:

        Map group name + " ( " + X channel name + " , " + Y channel name + " )"

        for example, string "DATA ( DIST , MAG )"  indicates a map group name of DATA,
        X channel name of DIST and Y channel name of MAG.
        """
        index.value = self._find_stk2(str_val.encode(), index.value, vv_rtd)
        




    def get_stk(self, num):
        """
        Get a specific `GXSTK <geosoft.gxapi.GXSTK>` object from a `GXMSTK <geosoft.gxapi.GXMSTK>` object
        (Index of 0 gets the first `GXSTK <geosoft.gxapi.GXSTK>` in the `GXMSTK <geosoft.gxapi.GXMSTK>`)
        
        :param num:   Index to `GXSTK <geosoft.gxapi.GXSTK>` to get
        :type  num:   int

        :returns:     x     - `GXSTK <geosoft.gxapi.GXSTK>` Object handle
        :rtype:       GXSTK

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_stk(num)
        return GXSTK(ret_val)




    def delete_stk(self, num):
        """
        Delete a `GXSTK <geosoft.gxapi.GXSTK>` object
        
        :param num:   Index to `GXSTK <geosoft.gxapi.GXSTK>` to delete (0 is first one)
        :type  num:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** 0 is the first one
        """
        self._delete_stk(num)
        




    def find_stk(self, str_val, index, group, x_ch, y_ch):
        """
        Find index of `GXSTK <geosoft.gxapi.GXSTK>` from a string of group names and X/Y channels
        
        :param str_val:  Input string (see notes above). Will be modified on return
        :param index:    Index to the `GXSTK <geosoft.gxapi.GXSTK>` found, Must be greater than 0 if found, -1 if not found
        :param group:    Output group name string
        :param x_ch:     Output X channel name string
        :param y_ch:     Output Y channel name string
        :type  str_val:  str
        :type  index:    int_ref
        :type  group:    str_ref
        :type  x_ch:     str_ref
        :type  y_ch:     str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Format of the input string:

        Map group name + " ( " + X channel name + " , " + Y channel name + " )"

        for example, string "DATA ( DIST , MAG )"  indicates a map group name of DATA,
        X channel name of DIST and Y channel name of MAG.
        """
        index.value, group.value, x_ch.value, y_ch.value = self._find_stk(str_val.encode(), index.value, group.value.encode(), x_ch.value.encode(), y_ch.value.encode())
        




    def get_num_stk(self):
        """
        Get the number of `GXSTK <geosoft.gxapi.GXSTK>` objects in a `GXMSTK <geosoft.gxapi.GXMSTK>` object
        

        :returns:     The number of `GXSTK <geosoft.gxapi.GXSTK>` objects in a `GXMSTK <geosoft.gxapi.GXMSTK>` object
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_num_stk()
        return ret_val




    def read_ini(self, ra):
        """
        Read multiple profiles parameters from an INI file
        
        :param ra:    `GXRA <geosoft.gxapi.GXRA>` handle to an INI file
        :type  ra:    GXRA

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._read_ini(ra)
        




    def save_profile(self, wa):
        """
        Save multiple profile INI parameters in a `GXWA <geosoft.gxapi.GXWA>` file of INI format
        
        :param wa:    `GXWA <geosoft.gxapi.GXWA>` handle to an INI file
        :type  wa:    GXWA

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._save_profile(wa)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer