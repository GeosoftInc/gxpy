### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
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
    using the `GXSYS.global_set` function using the following parameters:
    
    MONTAJ.GX_FONT="Font_name"
    
    This sets the default font to "Font_name". It applies to text in all
    components of the dialog.
    
    Additional customization of individual components can be accomplished
    using the following parameters:
    
    MONTAJ.GX_CAPTION_FONT="Caption_Font": Font for the field captions (labels)
    MONTAJ.GX_BUTTON_FONT="Button_Font"  : Font for buttons, including the "Browse" button
    MONTAJ.GX_TITLE_FONT="Title_Font"    : Font for special titles (see `set_title`).
    
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
    def null(cls):
        """
        A null (undefined) instance of `GXDGW`
        
        :returns: A null `GXDGW`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDGW` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDGW`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, name):
        """
        This method creates a Dialog window from a specified
        resource. The Resource is loaded into memory but not displayed.
        """
        ret_val = gxapi_cy.WrapDGW.create(GXContext._get_tls_geo(), name.encode())
        return GXDGW(ret_val)






    def get_info_meta(self, p2, p3, p4, p5, p6):
        """
        Copies the Dialog information to a `GXMETA` attribute.
        """
        self._wrapper.get_info_meta(p2, p3, p4._wrapper, p5, p6)
        




    def get_info_sys(self, id, info, group, field):
        """
        This method uses the information in a Dialog box to
        set a `GXSYS` variable.
        """
        self._wrapper.get_info_sys(id, info, group.encode(), field.encode())
        




    def get_list(self, id):
        """
        This method retrieves the list (`GXLST`) object associated
        with a Dialog object.
        """
        ret_val = self._wrapper.get_list(id)
        return GXLST(ret_val)




    def gt_info(self, id, info, buff):
        """
        This method fills the specified string with the text from
        the text object specified.
        """
        buff.value = self._wrapper.gt_info(id, info, buff.value.encode())
        




    def run_dialogue(self):
        """
        This method runs the Dialog window.
        """
        ret_val = self._wrapper.run_dialogue()
        return ret_val




    def set_info(self, id, info, buff):
        """
        This method sets the string of a text object. If the string
        is too long it will be truncated.
        """
        self._wrapper.set_info(id, info, buff.encode())
        




    def set_info_meta(self, p2, p3, p4, p5, p6):
        """
        This sets a text object to the text found in a `GXMETA` attribute.
        """
        self._wrapper.set_info_meta(p2, p3, p4._wrapper, p5, p6)
        




    def set_info_sys(self, id, info, group, field):
        """
        This sets a text object to the text found in a system
        parameter variable. If the variable has not been set,
        the text is not set.
        """
        self._wrapper.set_info_sys(id, info, group.encode(), field.encode())
        




    def set_title(self, title):
        """
        Changes the title of the dialog.

        **Note:**

        A "Special", additional title can be added to a dialog by using
        the following syntax:
        
        `set_title`(Diag, "Window Title\\nAdditional Title");
        
        In the title argument, a line break character '\\n' is used to
        separate the parts.
        
        The window title free_appears as the title in the upper bar of the dialog.
        The additional title free_appears below this, in the main body of the
        dialog, and is separated from the rest of the fields by a horizontal
        line. It is printed in the bold version of the default font (or of the
        special font specified using the MONTAJ.GX_TITLE_FONT parameter noted
        above in "Setting Fonts in GX dialogs."
        """
        self._wrapper.set_title(title.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer