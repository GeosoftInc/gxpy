### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIPGUI:
    """
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
    def null(cls) -> 'GXIPGUI':
        """
        A null (undefined) instance of :class:`GXIPGUI`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXIPGUI` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXIPGUI`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def modify_job(cls, p1: 'GXIP', p2: 'GXDB', p3: str, p4: int, p5: int_ref) -> int:
        ret_val, p5.value = gxapi_cy.WrapIPGUI.modify_job(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4, p5.value)
        return ret_val



    @classmethod
    def launch_ipqc_tool(cls, p1: str, p2: str, p3: str) -> None:
        gxapi_cy.WrapIPGUI.launch_ipqc_tool(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def launch_offset_ipqc_tool(cls, p1: str, p2: str, p3: str) -> None:
        gxapi_cy.WrapIPGUI.launch_offset_ipqc_tool(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def ipqc_tool_exists(cls) -> int:
        ret_val = gxapi_cy.WrapIPGUI.ipqc_tool_exists(GXContext._get_tls_geo())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer