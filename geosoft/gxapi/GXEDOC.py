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
class GXEDOC:
    """
    GXEDOC class.

    The :class:`GXEDOC` class provides access to a generic documents views as loaded within
    Oasis montaj.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEDOC(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXEDOC':
        """
        A null (undefined) instance of :class:`GXEDOC`
        
        :returns: A null :class:`GXEDOC`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXEDOC` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXEDOC`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# GMSYS 3D Models


    @classmethod
    def create_new_gms_3d(cls, p1: str, p2: int, p3: int, p4: int) -> 'GXEDOC':
        ret_val = gxapi_cy.WrapEDOC.create_new_gms_3d(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4)
        return GXEDOC(ret_val)




# Miscellaneous


    @classmethod
    def current(cls, p1: int) -> 'GXEDOC':
        ret_val = gxapi_cy.WrapEDOC.current(GXContext._get_tls_geo(), p1)
        return GXEDOC(ret_val)



    @classmethod
    def current_no_activate(cls, p1: int) -> 'GXEDOC':
        ret_val = gxapi_cy.WrapEDOC.current_no_activate(GXContext._get_tls_geo(), p1)
        return GXEDOC(ret_val)



    @classmethod
    def current_if_exists(cls, p1: int) -> 'GXEDOC':
        ret_val = gxapi_cy.WrapEDOC.current_if_exists(GXContext._get_tls_geo(), p1)
        return GXEDOC(ret_val)





    @classmethod
    def get_documents_lst(cls, p1: 'GXLST', p2: int, p3: int) -> int:
        ret_val = gxapi_cy.WrapEDOC.get_documents_lst(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        return ret_val




    def get_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_name(p2.value.encode())
        




    def get_window_state(self) -> int:
        ret_val = self._wrapper.get_window_state()
        return ret_val



    @classmethod
    def have_current(cls, p1: int) -> int:
        ret_val = gxapi_cy.WrapEDOC.have_current(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def loaded(cls, p1: str, p2: int) -> int:
        ret_val = gxapi_cy.WrapEDOC.loaded(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val




    def get_window_position(self, p2: int_ref, p3: int_ref, p4: int_ref, p5: int_ref, p6: int_ref, p7: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_window_position(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def set_window_position(self, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        self._wrapper.set_window_position(p2, p3, p4, p5, p6, p7)
        




    def read_only(self) -> int:
        ret_val = self._wrapper.read_only()
        return ret_val



    @classmethod
    def load(cls, p1: str, p2: int) -> 'GXEDOC':
        ret_val = gxapi_cy.WrapEDOC.load(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXEDOC(ret_val)



    @classmethod
    def load_no_activate(cls, p1: str, p2: int) -> 'GXEDOC':
        ret_val = gxapi_cy.WrapEDOC.load_no_activate(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXEDOC(ret_val)




    def make_current(self) -> None:
        self._wrapper.make_current()
        




    def set_window_state(self, p2: int) -> None:
        self._wrapper.set_window_state(p2)
        



    @classmethod
    def sync(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapEDOC.sync(GXContext._get_tls_geo(), p1.encode(), p2)
        




    def sync_open(self) -> None:
        self._wrapper.sync_open()
        



    @classmethod
    def un_load(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapEDOC.un_load(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def un_load_all(cls, p1: int) -> None:
        gxapi_cy.WrapEDOC.un_load_all(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def un_load_discard(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapEDOC.un_load_discard(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def un_load_verify(cls, p1: str, p2: int, p3: int) -> None:
        gxapi_cy.WrapEDOC.un_load_verify(GXContext._get_tls_geo(), p1.encode(), p2, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer