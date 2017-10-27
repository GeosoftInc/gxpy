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
class GXMAPTEMPLATE:
    """
    GXMAPTEMPLATE class.

    A `GXMAPTEMPLATE` wraps and provides manipulation and usage for the XML content in map template files.
    See the annotated schema file maptemplate.xsd in the <GEOSOFT>\\maptemplate folder and the accompanying
    documentation in that folder for documentation on the file format.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMAPTEMPLATE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMAPTEMPLATE`
        
        :returns: A null `GXMAPTEMPLATE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXMAPTEMPLATE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXMAPTEMPLATE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Content Manipulation Methods



    def get_tmp_copy(self, tmp):
        """
        Get a temporary XML file for manipulation of the map template.

        **Note:**

        After manipulating contents the object may be updated by a call to
        the UpdateFromTmpCopy method.
        """
        tmp.value = self._wrapper.get_tmp_copy(tmp.value.encode())
        




    def update_from_tmp_copy(self, tmp):
        """
        Update the object contents from a temporary XML file that may have bee manipulated externally.

        **Note:**

        This method will not modify the original contents of the file until a call to the
        the Commit method is made or the object is destroyed. A call to the Discard method
        will restore the contents to that of the original file. The temporary file is not deleted
        and should be to not leak file resources.
        """
        self._wrapper.update_from_tmp_copy(tmp.encode())
        




# File Methods



    def commit(self):
        """
        Commit any changes to the map template to disk
        """
        self._wrapper.commit()
        



    @classmethod
    def create(cls, name, base, mode):
        """
        Create a `GXMAPTEMPLATE` from an existing file.

        **Note:**

        The base template name should be the file name part of a geosoft_maptemplate
        file in the <geosoft>\\maptemplate or <geosoftuser>\\maptemplate folders. A base file
        in the user folder will override any in the Geosoft install dir.
        """
        ret_val = gxapi_cy.WrapMAPTEMPLATE.create(GXContext._get_tls_geo(), name.encode(), base.encode(), mode)
        return GXMAPTEMPLATE(ret_val)






    def discard(self):
        """
        Discard all changes made to the map template and reload from disk.
        """
        self._wrapper.discard()
        




    def get_file_name(self, name):
        """
        Get the file name of the map template.
        """
        name.value = self._wrapper.get_file_name(name.value.encode())
        




# Map Making



    def create_map(self, map, group):
        """
        Create a map from the map template
        """
        self._wrapper.create_map(map.encode(), group.encode())
        




# Render/Preview



    def refresh(self):
        """
        Refresh the map template with any newly saved items
        """
        self._wrapper.refresh()
        




    def render_preview(self, hdc, left, bottom, right, top):
        """
        Create a preview of the map template onto a
        Windows DC handle
        """
        self._wrapper.render_preview(hdc, left, bottom, right, top)
        




    def render_preview_map_production(self, hdc, left, bottom, right, top):
        """
        Render a preview for map sheet production purposes

        **Note:**

        This method can also be used to get the data view pixel location
        by passing a null DC handle. This help to plot the view contents
        preview from another location.
        """
        left.value, bottom.value, right.value, top.value = self._wrapper.render_preview_map_production(hdc, left.value, bottom.value, right.value, top.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer