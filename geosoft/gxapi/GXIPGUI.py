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
class GXIPGUI:
    """
    GXIPGUI class.

    This class is used in the `GXIP` System for `GXGUI` functions
    such as defining parameters for pseudo-section plots.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIPGUI(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIPGUI`
        
        :returns: A null `GXIPGUI`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXIPGUI` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXIPGUI`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def modify_job(cls, ip, db, ini, plot_type, page):
        """
        Modify parameters for an `GXIP` plot.
        """
        ret_val, page.value = gxapi_cy.WrapIPGUI.modify_job(GXContext._get_tls_geo(), ip._wrapper, db._wrapper, ini.encode(), plot_type, page.value)
        return ret_val



    @classmethod
    def launch_ipqc_tool(cls, db, line, chan):
        """
        Launch the In-Line `GXIP` QC tool on a database.

        **Note:**

        The database should be a currently open database.
        """
        gxapi_cy.WrapIPGUI.launch_ipqc_tool(GXContext._get_tls_geo(), db.encode(), line.encode(), chan.encode())
        



    @classmethod
    def launch_offset_ipqc_tool(cls, db, line, chan):
        """
        Launch the Offset `GXIP` QC tool on a database.

        **Note:**

        The database should be a currently open database.
        """
        gxapi_cy.WrapIPGUI.launch_offset_ipqc_tool(GXContext._get_tls_geo(), db.encode(), line.encode(), chan.encode())
        



    @classmethod
    def ipqc_tool_exists(cls):
        """
        See if there is an IPQC Tool (Offset or Inline) already open.

        **Note:**

        See if there is an IPQC Tool already open.
        """
        ret_val = gxapi_cy.WrapIPGUI.ipqc_tool_exists(GXContext._get_tls_geo())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer