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
class GXMAPTEMPLATE(gxapi_cy.WrapMAPTEMPLATE):
    """
    GXMAPTEMPLATE class.

    A `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>` wraps and provides manipulation and usage for the XML content in map template files.
    See the annotated schema file maptemplate.xsd in the <GEOSOFT>\\maptemplate folder and the accompanying
    documentation in that folder for documentation on the file format.
    """

    def __init__(self, handle=0):
        super(GXMAPTEMPLATE, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`
        
        :returns: A null `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>`
        :rtype:   GXMAPTEMPLATE
        """
        return GXMAPTEMPLATE()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Content Manipulation Methods



    def get_tmp_copy(self, tmp):
        """
        Get a temporary XML file for manipulation of the map template.
        
        :param tmp:          Returned temporary map template file name
        :type  tmp:          str_ref

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** After manipulating contents the object may be updated by a call to
        the UpdateFromTmpCopy method.
        """
        tmp.value = self._get_tmp_copy(tmp.value.encode())
        




    def update_from_tmp_copy(self, tmp):
        """
        Update the object contents from a temporary XML file that may have bee manipulated externally.
        
        :param tmp:          Temporary map template file name
        :type  tmp:          str

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This method will not modify the original contents of the file until a call to the
        the Commit method is made or the object is destroyed. A call to the Discard method
        will restore the contents to that of the original file. The temporary file is not deleted
        and should be to not leak file resources.
        """
        self._update_from_tmp_copy(tmp.encode())
        




# File Methods



    def commit(self):
        """
        Commit any changes to the map template to disk
        

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._commit()
        



    @classmethod
    def create(cls, name, base, mode):
        """
        Create a `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>` from an existing file.
        
        :param name:  Map Template file name
        :param base:  Map Template base template to create from
        :param mode:  :ref:`MAPTEMPLATE_OPEN`
        :type  name:  str
        :type  base:  str
        :type  mode:  int

        :returns:     `GXMAPTEMPLATE <geosoft.gxapi.GXMAPTEMPLATE>` Object
        :rtype:       GXMAPTEMPLATE

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The base template name should be the file name part of a geosoft_maptemplate
        file in the <geosoft>\\maptemplate or <geosoftuser>\\maptemplate folders. A base file
        in the user folder will override any in the Geosoft install dir.
        """
        ret_val = gxapi_cy.WrapMAPTEMPLATE._create(GXContext._get_tls_geo(), name.encode(), base.encode(), mode)
        return GXMAPTEMPLATE(ret_val)






    def discard(self):
        """
        Discard all changes made to the map template and reload from disk.
        

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._discard()
        




    def get_file_name(self, name):
        """
        Get the file name of the map template.
        
        :param name:         Returned map template file name
        :type  name:         str_ref

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        name.value = self._get_file_name(name.value.encode())
        




# Map Making



    def create_map(self, map, group):
        """
        Create a map from the map template
        
        :param map:          New map file name (if it exists it will be overwritten)
        :param group:        Group name to use for settings
        :type  map:          str
        :type  group:        str

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._create_map(map.encode(), group.encode())
        




# Render/Preview



    def refresh(self):
        """
        Refresh the map template with any newly saved items
        

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._refresh()
        




    def render_preview(self, hdc, left, bottom, right, top):
        """
        Create a preview of the map template onto a
        Windows DC handle
        
        :param hdc:          DC Handle
        :param left:         Left value of the render rect in Windows coordinates (bottom>top)
        :param bottom:       Bottom value
        :param right:        Right value
        :param top:          Top value
        :type  hdc:          int
        :type  left:         int
        :type  bottom:       int
        :type  right:        int
        :type  top:          int

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._render_preview(hdc, left, bottom, right, top)
        




    def render_preview_map_production(self, hdc, left, bottom, right, top):
        """
        Render a preview for map sheet production purposes
        
        :param hdc:          DC Handle (pass 0 to just query the Data view pixel location)
        :param left:         Left value of the render rect in Windows coordinates (bottom>top)
        :param bottom:       Bottom value
        :param right:        Right value
        :param top:          Top value
        :type  hdc:          int
        :type  left:         int_ref
        :type  bottom:       int_ref
        :type  right:        int_ref
        :type  top:          int_ref

        .. versionadded:: 6.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This method can also be used to get the data view pixel location
        by passing a null DC handle. This help to plot the view contents
        preview from another location.
        """
        left.value, bottom.value, right.value, top.value = self._render_preview_map_production(hdc, left.value, bottom.value, right.value, top.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer