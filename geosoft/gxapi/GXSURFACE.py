### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXSURFACEITEM import GXSURFACEITEM


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSURFACE(gxapi_cy.WrapSURFACE):
    """
    GXSURFACE class.

    The `GXSURFACE <geosoft.gxapi.GXSURFACE>` class allows you to create, read and alter Geosurface files (``*.geosoft_surface``).
    A Geosurface file can contain one or more surface items (see `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>` class). In turn each item can
    contains one or more triangular polyhedral meshes.
    """

    def __init__(self, handle=0):
        super(GXSURFACE, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSURFACE <geosoft.gxapi.GXSURFACE>`
        
        :returns: A null `GXSURFACE <geosoft.gxapi.GXSURFACE>`
        :rtype:   GXSURFACE
        """
        return GXSURFACE()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, surface_file, ipj):
        """
        Create a new Geosurface file
        
        :param surface_file:  Geosurface file name
        :param ipj:           `GXIPJ <geosoft.gxapi.GXIPJ>` containing coordinate system of the Geosurface
        :type  surface_file:  str
        :type  ipj:           GXIPJ

        :returns:             `GXSURFACE <geosoft.gxapi.GXSURFACE>` Object
        :rtype:               GXSURFACE

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSURFACE._create(GXContext._get_tls_geo(), surface_file.encode(), ipj)
        return GXSURFACE(ret_val)



    @classmethod
    def open(cls, surface_file, mode):
        """
        Open a Geosurface file
        
        :param surface_file:  Geosurface file name
        :param mode:          :ref:`SURFACE_OPEN`
        :type  surface_file:  str
        :type  mode:          int

        :returns:             `GXSURFACE <geosoft.gxapi.GXSURFACE>` Object
        :rtype:               GXSURFACE

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSURFACE._open(GXContext._get_tls_geo(), surface_file.encode(), mode)
        return GXSURFACE(ret_val)






    def get_ipj(self, ipj):
        """
        Get the coordinate system of the `GXSURFACE <geosoft.gxapi.GXSURFACE>`.
        
        :param ipj:      `GXIPJ <geosoft.gxapi.GXIPJ>` in which to place the Geosurface coordinate system
        :type  ipj:      GXIPJ

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_ipj(ipj)
        




    def set_ipj(self, ipj):
        """
        Change the coordinate system of the `GXSURFACE <geosoft.gxapi.GXSURFACE>`.
        
        :param ipj:      `GXIPJ <geosoft.gxapi.GXIPJ>` containing the new coordinate system of the Geosurface
        :type  ipj:      GXIPJ

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_ipj(ipj)
        




    def get_surface_items(self, lst):
        """
        Get the surfaces items in a Geosurface file
        
        :param lst:      `GXLST <geosoft.gxapi.GXLST>` to fill
        :type  lst:      GXLST

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_surface_items(lst)
        




    def get_surface_item(self, guid):
        """
        Get the an existing surface item from the `GXSURFACE <geosoft.gxapi.GXSURFACE>`
        
        :param guid:     Item GUID
        :type  guid:     str

        :returns:        `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>` Object
        :rtype:          GXSURFACEITEM

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_surface_item(guid.encode())
        return GXSURFACEITEM(ret_val)




    def add_surface_item(self, surfaceitem):
        """
        Add a new surface item to the `GXSURFACE <geosoft.gxapi.GXSURFACE>`
        
        :param surfaceitem:  `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>` to add
        :type  surfaceitem:  GXSURFACEITEM

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._add_surface_item(surfaceitem)
        



    @classmethod
    def get_surface_names(cls, surface_file, lst):
        """
        Get the surface item names in a Geosurface file
        
        :param surface_file:  Geosurface file
        :param lst:           `GXLST <geosoft.gxapi.GXLST>` to fill
        :type  surface_file:  str
        :type  lst:           GXLST

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSURFACE._get_surface_names(GXContext._get_tls_geo(), surface_file.encode(), lst)
        



    @classmethod
    def get_closed_surface_names(cls, surface_file, lst):
        """
        Get the names of closed surface items in a Geosurface file (may return an empty list)
        
        :param surface_file:  Geosurface file
        :param lst:           `GXLST <geosoft.gxapi.GXLST>` to fill (may return an empty `GXLST <geosoft.gxapi.GXLST>` if none of the surfaces are closed)
        :type  surface_file:  str
        :type  lst:           GXLST

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSURFACE._get_closed_surface_names(GXContext._get_tls_geo(), surface_file.encode(), lst)
        




    def get_extents(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the spatial range of all surface items.
        
        :param min_x:    Minimum valid data in X.
        :param min_y:    Minimum valid data in Y.
        :param min_z:    Minimum valid data in Z.
        :param max_x:    Maximum valid data in X.
        :param max_y:    Maximum valid data in Y.
        :param max_z:    Maximum valid data in Z.
        :type  min_x:    float_ref
        :type  min_y:    float_ref
        :type  min_z:    float_ref
        :type  max_x:    float_ref
        :type  max_y:    float_ref
        :type  max_z:    float_ref

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._get_extents(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        



    @classmethod
    def crc(cls, surface_file, output, crc):
        """
        Compute an XML CRC of a Geosurface file.
        
        :param surface_file:  Geosurface file
        :param output:        Output file
        :param crc:           CRC (unused, always set to 0)
        :type  surface_file:  str
        :type  output:        str
        :type  crc:           int_ref

        :returns:             CRC Value (always 0)
        :rtype:               int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, crc.value = gxapi_cy.WrapSURFACE._crc(GXContext._get_tls_geo(), surface_file.encode(), output.encode(), crc.value)
        return ret_val



    @classmethod
    def sync(cls, name):
        """
        Syncronize the Metadata for this Geosurface
        
        :param name:  Geosurface file
        :type  name:  str

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSURFACE._sync(GXContext._get_tls_geo(), name.encode())
        



    @classmethod
    def create_from_dxf(cls, ipj, surface_file, dxf_file):
        """
        Create Geosurface file from DXF file.
        
        :param surface_file:  Geosurface file
        :param dxf_file:      DXF file
        :type  ipj:           GXIPJ
        :type  surface_file:  str
        :type  dxf_file:      str

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSURFACE._create_from_dxf(GXContext._get_tls_geo(), ipj, surface_file.encode(), dxf_file.encode())
        



    @classmethod
    def create_from_vulcan_triangulation(cls, triangulation_file, ipj, surface_file):
        """
        Create Geosurface file from a Maptek Vulcan triangulation file.
        
        :param triangulation_file:  00t file
        :param surface_file:        Geosurface file
        :type  triangulation_file:  str
        :type  ipj:                 GXIPJ
        :type  surface_file:        str

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapSURFACE._create_from_vulcan_triangulation(GXContext._get_tls_geo(), triangulation_file.encode(), ipj, surface_file.encode())
        



    @classmethod
    def append_vulcan_triangulation(cls, triangulation_file, ipj, surface_file):
        """
        Create new surface from a Maptek Vulcan triangulation file and add to an existing geosurface.
        
        :param triangulation_file:  00t file
        :param surface_file:        Geosurface file
        :type  triangulation_file:  str
        :type  ipj:                 GXIPJ
        :type  surface_file:        str

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapSURFACE._append_vulcan_triangulation(GXContext._get_tls_geo(), triangulation_file.encode(), ipj, surface_file.encode())
        



    @classmethod
    def dump_geometry_to_text_file(cls, surface_filename, text_filename):
        """
        Dump surface geometry to a text file.
        
        :param surface_filename:  Geosurface file
        :param text_filename:     Text file
        :type  surface_filename:  str
        :type  text_filename:     str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSURFACE._dump_geometry_to_text_file(GXContext._get_tls_geo(), surface_filename.encode(), text_filename.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer