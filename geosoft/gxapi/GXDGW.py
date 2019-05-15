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
class GXDGW(gxapi_cy.WrapDGW):
    """
    GXDGW class.

    Provides access to dialog boxes for user I/O. You can
    use this class to store to, or retrieve information from
    the current workspace parameter block via dialog boxes

    **Note:**

    Setting Fonts in GX dialogs.

    By default, "new look" GX dialogs uses the "Tahoma" font. This font can be
    overridden by updating the application settings. This can be done programmatically
    using the `GXSYS.global_set <geosoft.gxapi.GXSYS.global_set>` function using the following parameters:

    MONTAJ.GX_FONT="Font_name"

    This sets the default font to "Font_name". It applies to text in all
    components of the dialog.

    Additional customization of individual components can be accomplished
    using the following parameters:

    MONTAJ.GX_CAPTION_FONT="Caption_Font": Font for the field captions (labels)
    MONTAJ.GX_BUTTON_FONT="Button_Font"  : Font for buttons, including the "Browse" button
    MONTAJ.GX_TITLE_FONT="Title_Font"    : Font for special titles (see `set_title <geosoft.gxapi.GXDGW.set_title>`).

    The font used for the text in edit windows remains the default, or the
    value specified using MONTAJ.GX_FONT.

    Note that the "OK" button, and the Title, use "Bold" versions of the
    specified font. If the bolded version does not exist as a normal font,
    then the operating system may provide its own alternative which may not
    appear the same as you expect.

    Before version 6.2. there used to be a parameter, MONTAJ.GX_CHARSET, that
    affected characters above ASCII 127. 6.2. introduced Unicode in the core
    montaj engine that eliminated the need for such a setting. All strings
    on the GX API level are encoded in :ref:`UTF8` during runtime which makes it possible
    to represent all possible characters without using character sets.
    """

    def __init__(self, handle=0):
        super(GXDGW, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDGW <geosoft.gxapi.GXDGW>`
        
        :returns: A null `GXDGW <geosoft.gxapi.GXDGW>`
        :rtype:   GXDGW
        """
        return GXDGW()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, name):
        """
        This method creates a Dialog window from a specified
        resource. The Resource is loaded into memory but not displayed.
        
        :param name:  Name of the Window Resource to use
        :type  name:  str

        :returns:     Handle to the `GXDGW <geosoft.gxapi.GXDGW>` object.
        :rtype:       GXDGW

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapDGW._create(GXContext._get_tls_geo(), name.encode())
        return GXDGW(ret_val)






    def get_info_meta(self, obj, dlg_obj_type, meta, meta_obj, meta_attrib):
        """
        Copies the Dialog information to a `GXMETA <geosoft.gxapi.GXMETA>` attribute.
        
        :param obj:           Dialog Object
        :param dlg_obj_type:  :ref:`DGW_OBJECT`
        :param meta_obj:      Object
        :param meta_attrib:   Attribute
        :type  obj:           int
        :type  dlg_obj_type:  int
        :type  meta:          GXMETA
        :type  meta_obj:      int
        :type  meta_attrib:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._get_info_meta(obj, dlg_obj_type, meta, meta_obj, meta_attrib)
        




    def get_info_sys(self, id, info, group, field):
        """
        This method uses the information in a Dialog box to
        set a `GXSYS <geosoft.gxapi.GXSYS>` variable.
        
        :param id:     Dialog Object
        :param info:   :ref:`DGW_OBJECT`
        :param group:  Group name of the Variable
        :param field:  Variable name
        :type  id:     int
        :type  info:   int
        :type  group:  str
        :type  field:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._get_info_sys(id, info, group.encode(), field.encode())
        




    def get_list(self, id):
        """
        This method retrieves the list (`GXLST <geosoft.gxapi.GXLST>`) object associated
        with a Dialog object.
        
        :param id:   Dialog Object
        :type  id:   int

        :returns:    The List Object
        :rtype:      GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_list(id)
        return GXLST(ret_val)




    def gt_info(self, id, info, buff):
        """
        This method fills the specified string with the text from
        the text object specified.
        
        :param id:    Handle to the TEXT Object
        :param info:  :ref:`DGW_OBJECT`
        :param buff:  Where to place the String
        :type  id:    int
        :type  info:  int
        :type  buff:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        buff.value = self._gt_info(id, info, buff.value.encode())
        




    def run_dialogue(self):
        """
        This method runs the Dialog window.
        

        :returns:    The Exit Code of the Dialog window.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._run_dialogue()
        return ret_val




    def set_info(self, id, info, buff):
        """
        This method sets the string of a text object. If the string
        is too long it will be truncated.
        
        :param id:    Handle to the TEXT Object
        :param info:  :ref:`DGW_OBJECT`
        :param buff:  String to set the Text To
        :type  id:    int
        :type  info:  int
        :type  buff:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_info(id, info, buff.encode())
        




    def set_info_meta(self, obj, dlg_obj_type, meta, meta_obj, meta_attrib):
        """
        This sets a text object to the text found in a `GXMETA <geosoft.gxapi.GXMETA>` attribute.
        
        :param obj:           Dialog Object
        :param dlg_obj_type:  :ref:`DGW_OBJECT`
        :param meta_obj:      Object
        :param meta_attrib:   Attribute
        :type  obj:           int
        :type  dlg_obj_type:  int
        :type  meta:          GXMETA
        :type  meta_obj:      int
        :type  meta_attrib:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_info_meta(obj, dlg_obj_type, meta, meta_obj, meta_attrib)
        




    def set_info_sys(self, id, info, group, field):
        """
        This sets a text object to the text found in a system
        parameter variable. If the variable has not been set,
        the text is not set.
        
        :param id:     Dialog Object
        :param info:   :ref:`DGW_OBJECT`
        :param group:  Group name of the Variable
        :param field:  Variable name
        :type  id:     int
        :type  info:   int
        :type  group:  str
        :type  field:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_info_sys(id, info, group.encode(), field.encode())
        




    def set_title(self, title):
        """
        Changes the title of the dialog.
        
        :param title:  Title to set
        :type  title:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** A "Special", additional title can be added to a dialog by passing a title
        to `set_title <geosoft.gxapi.GXDGW.set_title>` with the following syntax:

        ``"Window Title\\nAdditional Title"``

        In the title argument, a line break character ``'\\n'`` is used to
        separate the parts.

        The window title free_appears as the title in the upper bar of the dialog.
        The additional title free_appears below this, in the main body of the
        dialog, and is separated from the rest of the fields by a horizontal
        line. It is printed in the bold version of the default font (or of the
        special font specified using the MONTAJ.GX_TITLE_FONT parameter noted
        above in "Setting Fonts in GX dialogs."
        """
        self._set_title(title.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer