### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXLST import GXLST
### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDGW:
    """
    GXDGW class.

    Provides access to dialog boxes for user I/O. You can
    use this class to store to, or retrieve information from
    the current workspace parameter block via dialog boxes

    **Note:**

    Setting Fonts in GX dialogs.
    
    By default, "new look" GX dialogs uses the "Tahoma" font. This font can be
    overridden by updating the application settings. This can be done programmatically
    using the GlobalSet_SYS function using the following parameters:
    
    MONTAJ.GX_FONT="Font_name"
    
    This sets the default font to "Font_name". It applies to text in all
    components of the dialog.
    
    Additional customization of individual components can be accomplished
    using the following parameters:
    
    MONTAJ.GX_CAPTION_FONT="Caption_Font": Font for the field captions (labels)
    MONTAJ.GX_BUTTON_FONT="Button_Font"  : Font for buttons, including the "Browse" button
    MONTAJ.GX_TITLE_FONT="Title_Font"    : Font for special titles (see SetTitle_DGW).
    
    The font used for the text in edit windows remains the default, or the
    value specified using MONTAJ.GX_FONT.
    
    Note that the "OK" button, and the Title, use "Bold" versions of the
    specified font. If the bolded version does not exist as a normal font,
    then the operating system may provide its own alternative which may not
    appear the same as you expect.
    
    Before version 6.2. there used to be a parameter, MONTAJ.GX_CHARSET, that
    affected characters above ASCII 127. 6.2. introduced Unicode in the core
    montaj engine that eliminated the need for such a setting. All strings
    on the GX API level are encoded in `UTF8` during runtime which makes it possible
    to represent all possible characters without using character sets.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDGW(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXDGW':
        """
        A null (undefined) instance of :class:`GXDGW`
        
        :returns: A null :class:`GXDGW`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDGW` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDGW`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str) -> 'GXDGW':
        ret_val = gxapi_cy.WrapDGW.create(GXContext._get_tls_geo(), p1.encode())
        return GXDGW(ret_val)






    def get_info_meta(self, p2: int, p3: int, p4: 'GXMETA', p5: int, p6: int) -> None:
        self._wrapper.get_info_meta(p2, p3, p4._wrapper, p5, p6)
        




    def get_info_sys(self, p2: int, p3: int, p4: str, p5: str) -> None:
        self._wrapper.get_info_sys(p2, p3, p4.encode(), p5.encode())
        




    def get_list(self, p2: int) -> 'GXLST':
        ret_val = self._wrapper.get_list(p2)
        return GXLST(ret_val)




    def gt_info(self, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = self._wrapper.gt_info(p2, p3, p4.value.encode())
        




    def run_dialogue(self) -> int:
        ret_val = self._wrapper.run_dialogue()
        return ret_val




    def set_info(self, p2: int, p3: int, p4: str) -> None:
        self._wrapper.set_info(p2, p3, p4.encode())
        




    def set_info_meta(self, p2: int, p3: int, p4: 'GXMETA', p5: int, p6: int) -> None:
        self._wrapper.set_info_meta(p2, p3, p4._wrapper, p5, p6)
        




    def set_info_sys(self, p2: int, p3: int, p4: str, p5: str) -> None:
        self._wrapper.set_info_sys(p2, p3, p4.encode(), p5.encode())
        




    def set_title(self, p2: str) -> None:
        self._wrapper.set_title(p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer