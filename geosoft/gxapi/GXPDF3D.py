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
class GXPDF3D(gxapi_cy.WrapPDF3D):
    """
    GXPDF3D class.

    The `GXPDF3D <geosoft.gxapi.GXPDF3D>` class provides the ability to create 3D PDFs.
    """

    def __init__(self, handle=0):
        super(GXPDF3D, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPDF3D <geosoft.gxapi.GXPDF3D>`
        
        :returns: A null `GXPDF3D <geosoft.gxapi.GXPDF3D>`
        :rtype:   GXPDF3D
        """
        return GXPDF3D()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def render(cls, mview, file_name, resolution, no_clipping):
        """
        Render a voxel, voxsurf and/or gensurf to pdf
        
        :param mview:        `GXMVIEW <geosoft.gxapi.GXMVIEW>` handle
        :param file_name:    Filename
        :param resolution:   Resolution
        :param no_clipping:  Noclipping
        :type  mview:        GXMVIEW
        :type  file_name:    str
        :type  resolution:   int
        :type  no_clipping:  int

        .. versionadded:: 6.4.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapPDF3D._render(GXContext._get_tls_geo(), mview, file_name.encode(), resolution, no_clipping)
        



    @classmethod
    def render_to_page(cls, mview, file_name, page_number, resolution, no_clip):
        """
        Render a voxel, voxsurf and/or gensurf to a specified page on a pdf
        
        :param mview:        `GXMVIEW <geosoft.gxapi.GXMVIEW>` handle
        :param file_name:    Filename
        :param page_number:  Page number
        :param resolution:   Resolution
        :param no_clip:      Noclipping
        :type  mview:        GXMVIEW
        :type  file_name:    str
        :type  page_number:  int
        :type  resolution:   int
        :type  no_clip:      int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapPDF3D._render_to_page(GXContext._get_tls_geo(), mview, file_name.encode(), page_number, resolution, no_clip)
        



    @classmethod
    def export_2d(cls, input_map, output_file, create_layersin_pdf, geospatial_pdf, open_pdf):
        """
        Export a 2D map to a PDF file.
        
        :param input_map:            Input map file
        :param output_file:          Output PDF file
        :param create_layersin_pdf:  Create layers in PDF
        :param geospatial_pdf:       Geospatial PDF
        :param open_pdf:             Open PDF after export
        :type  input_map:            str
        :type  output_file:          str
        :type  create_layersin_pdf:  int
        :type  geospatial_pdf:       int
        :type  open_pdf:             int

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapPDF3D._export_2d(GXContext._get_tls_geo(), input_map.encode(), output_file.encode(), create_layersin_pdf, geospatial_pdf, open_pdf)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer