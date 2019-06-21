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
class GXIPGUI(gxapi_cy.WrapIPGUI):
    """
    GXIPGUI class.

    This class is used in the `GXIP <geosoft.gxapi.GXIP>` System for `GXGUI <geosoft.gxapi.GXGUI>` functions
    such as defining parameters for pseudo-section plots.
    """

    def __init__(self, handle=0):
        super(GXIPGUI, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIPGUI <geosoft.gxapi.GXIPGUI>`
        
        :returns: A null `GXIPGUI <geosoft.gxapi.GXIPGUI>`
        :rtype:   GXIPGUI
        """
        return GXIPGUI()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def modify_job(cls, ip, db, ini, plot_type, page):
        """
        Modify parameters for an `GXIP <geosoft.gxapi.GXIP>` plot.
        
        :param ip:         `GXDH <geosoft.gxapi.GXDH>` Handle
        :param db:         `GXDB <geosoft.gxapi.GXDB>` Handle
        :param ini:        Job Name (``*.inp``)
        :param plot_type:  Job type :ref:`IP_PLOT`
        :param page:       Page to open `GXGUI <geosoft.gxapi.GXGUI>` on
        :type  ip:         GXIP
        :type  db:         GXDB
        :type  ini:        str
        :type  plot_type:  int
        :type  page:       int_ref

        :returns:          0 - Ok
                           -1 - User Cancelled
        :rtype:            int

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val, page.value = gxapi_cy.WrapIPGUI._modify_job(GXContext._get_tls_geo(), ip, db, ini.encode(), plot_type, page.value)
        return ret_val



    @classmethod
    def launch_ipqc_tool(cls, db, line, chan):
        """
        Launch the In-Line `GXIP <geosoft.gxapi.GXIP>` QC tool on a database.
        
        :param db:    Database name
        :param line:  Current Line (can be blank)
        :param chan:  Channel to open with (can be blank)
        :type  db:    str
        :type  line:  str
        :type  chan:  str

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The database should be a currently open database.
        """
        gxapi_cy.WrapIPGUI._launch_ipqc_tool(GXContext._get_tls_geo(), db.encode(), line.encode(), chan.encode())
        



    @classmethod
    def launch_offset_ipqc_tool(cls, db, line, chan):
        """
        Launch the Offset `GXIP <geosoft.gxapi.GXIP>` QC tool on a database.
        
        :param db:    Database name
        :param line:  Current Line (can be blank)
        :param chan:  Channel to open with (can be blank)
        :type  db:    str
        :type  line:  str
        :type  chan:  str

        .. versionadded:: 9.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The database should be a currently open database.
        """
        gxapi_cy.WrapIPGUI._launch_offset_ipqc_tool(GXContext._get_tls_geo(), db.encode(), line.encode(), chan.encode())
        



    @classmethod
    def ipqc_tool_exists(cls):
        """
        See if there is an IPQC Tool (Offset or Inline) already open.
        

        :returns:    0 if not open, 1 if open
        :rtype:      int

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** See if there is an IPQC Tool already open.
        """
        ret_val = gxapi_cy.WrapIPGUI._ipqc_tool_exists(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def launch_remove_contributing_electrodes_ext_tool(cls, db, map):
        """
        Launch the Remove Contributing Electrodes dialog.
        
        :param db:   Database name
        :param map:  Current Map
        :type  db:   str
        :type  map:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** This tool removes the `GXEXT <geosoft.gxapi.GXEXT>` object that allows the database-map linking between an IP data base 
        and IP plan map for plotting contributing electrodes for a given database row of data.
        """
        gxapi_cy.WrapIPGUI._launch_remove_contributing_electrodes_ext_tool(GXContext._get_tls_geo(), db.encode(), map.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer