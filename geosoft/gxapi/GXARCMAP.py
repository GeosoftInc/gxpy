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
class GXARCMAP:
    """
    GXARCMAP class.

    This library is not a class. It contains various utilities
    used in maps and layers by the Geosoft extensions for ArcGIS.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapARCMAP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXARCMAP`
        
        :returns: A null :class:`geosoft.gxapi.GXARCMAP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXARCMAP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXARCMAP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def change_size(cls, p1, p2):
        """
        Changes the custom page size of the ArcGIS Map document.
        """
        gxapi_cy.WrapARCMAP.change_size(GXContext._get_tls_geo(), p1, p2)
        



    @classmethod
    def display_in_3d_view(cls, p1):
        """
        Display a file in 3D view
        """
        gxapi_cy.WrapARCMAP.display_in_3d_view(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def export_feature_layer_by_name_to_3d_file(cls, p1, p2, p3, p4):
        """
        Exports the shapes from a feature layer of the ArcMap document to a 3D File.
        """
        gxapi_cy.WrapARCMAP.export_feature_layer_by_name_to_3d_file(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def export_selected_feature_layer_to_3d_file(cls, p1):
        """
        Exports the shapes from the currently selected feature layer (if any) in ArcMap to a 3D file (only on oriented frames i.e. sections).
        """
        gxapi_cy.WrapARCMAP.export_selected_feature_layer_to_3d_file(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def get_current_document_info(cls, p1, p2, p3):
        """
        Get some info on the current :class:`geosoft.gxapi.GXMXD` in ArcMap and selected layer (if any)
        """
        p1.value, p2.value, p3.value = gxapi_cy.WrapARCMAP.get_current_document_info(GXContext._get_tls_geo(), p1.value.encode(), p2.value.encode(), p3.value.encode())
        



    @classmethod
    def get_selected_layer_info(cls, p1, p2, p3):
        """
        Get the name info on the specified selected layer
        """
        p2.value, p3.value = gxapi_cy.WrapARCMAP.get_selected_layer_info(GXContext._get_tls_geo(), p1, p2.value.encode(), p3.value.encode())
        



    @classmethod
    def get_number_of_selected_layers(cls):
        """
        Get the number of selected layers in the TOC
        
        Returns									 The number of layers selected.
        """
        ret_val = gxapi_cy.WrapARCMAP.get_number_of_selected_layers(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def load_map(cls, p1, p2, p3, p4):
        """
        Loads a Geosoft map into the ArcMap document.

        **Note:**

        The extra datasets CSV should contain the the following fields:
        
         ID          -  Unique identifier
         DATASOURCE  -  Filename
         TYPE        -  RASTER and SHAPE supported
         MAPMATCH    -  Map to associate with (used for grouping logic)
         VIEWMATCH   -  View to match with in associated map (used for grouping logic)
         ZONEFILE    -  Used for type RASTER
        """
        ret_val = gxapi_cy.WrapARCMAP.load_map(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4)
        return ret_val



    @classmethod
    def load_map_ex(cls, p1, p2, p3, p4, p5):
        """
        Loads a Geosoft map into the ArcMap document, specifying which View to use as Data view.

        **Note:**

        The extra datasets CSV should contain the the following fields:
        
         ID          -  Unique identifier
         DATASOURCE  -  Filename
         TYPE        -  RASTER and SHAPE supported
         MAPMATCH    -  Map to associate with (used for grouping logic)
         VIEWMATCH   -  View to match with in associated map (used for grouping logic)
         ZONEFILE    -  Used for type RASTER
        """
        ret_val = gxapi_cy.WrapARCMAP.load_map_ex(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5)
        return ret_val



    @classmethod
    def load_shape(cls, p1, p2):
        """
        Load a shape file into ArcMap.
        """
        ret_val = gxapi_cy.WrapARCMAP.load_shape(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val



    @classmethod
    def load_spf(cls, p1, p2):
        """
        Load all the shape files generated by importing a SPF into ArcMap.
        """
        ret_val = gxapi_cy.WrapARCMAP.load_spf(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val



    @classmethod
    def load_lyr(cls, p1):
        """
        Load a LYR file to the current data frame
        """
        gxapi_cy.WrapARCMAP.load_lyr(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def load_map(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Loads a Geosoft map into the current ArcMap document

        **Note:**

        The extra datasets CSV should contain the the following fields:
        
            ID          -  Unique identifier
            DATASOURCE  -  Filename
            TYPE        -  RASTER and SHAPE supported
            MAPMATCH    -  Map to associate with (used for grouping logic)
            VIEWMATCH   -  View to match with in associated map (used for grouping logic)
            ZONEFILE    -  Used for type RASTER
        """
        gxapi_cy.WrapARCMAP.load_map(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5, p6, p7)
        



    @classmethod
    def load_map_view(cls, p1, p2, p3, p4):
        """
        Load a Geosoft Map as a layer into the current data frame
        """
        gxapi_cy.WrapARCMAP.load_map_view(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4)
        



    @classmethod
    def load_raster(cls, p1):
        """
        Load a raster file to the current data frame

        **Note:**

        Loads any file type recognized as "raster" formats by ARC :class:`geosoft.gxapi.GXGIS`.
        This includes geosoft GRD files.
        """
        gxapi_cy.WrapARCMAP.load_raster(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def load_shape(cls, p1, p2, p3):
        """
        Load a :class:`geosoft.gxapi.GXSHP` file to the current data frame

        **Note:**

        The input layer name is created using the (optional) prefix and suffix as follows:
        
        Prefix_NAME_Suffix
        """
        gxapi_cy.WrapARCMAP.load_shape(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def map_view_to_shape(cls, p1, p2, p3, p4):
        """
        Create :class:`geosoft.gxapi.GXSHP` file(s) from a Geosoft Map view.

        **Note:**

        The output :class:`geosoft.gxapi.GXSHP` file name(s) are made up as follows
        (where NAME is the input :class:`geosoft.gxapi.GXSHP` file name):
        
              NAME_pt.shp    (point objects)
              NAME_ln.shp    (line or arc objects)
              NAME_pg.shp    (polygon objects)
        """
        gxapi_cy.WrapARCMAP.map_view_to_shape(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4._wrapper)
        



    @classmethod
    def query_size(cls, p1, p2):
        """
        Query the page size in mm of the entire map page.
        """
        p1.value, p2.value = gxapi_cy.WrapARCMAP.query_size(GXContext._get_tls_geo(), p1.value, p2.value)
        



    @classmethod
    def show_layer_by_name_in_3d(cls, p1, p2, p3):
        """
        Shows a layer in ArcMap in a 3D view in an :class:`geosoft.gxapi.GXMXD`
        """
        gxapi_cy.WrapARCMAP.show_layer_by_name_in_3d(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def show_selected_layers_in_3d(cls):
        """
        Shows the selected layers in ArcMap in a 3D view
        """
        gxapi_cy.WrapARCMAP.show_selected_layers_in_3d(GXContext._get_tls_geo())
        



    @classmethod
    def get_ipj_for_predefined_esri_gcs(cls, p1, p2):
        """
        Fills an :class:`geosoft.gxapi.GXIPJ` with a predefined ESRI GCS
        """
        gxapi_cy.WrapARCMAP.get_ipj_for_predefined_esri_gcs(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def get_ipj_for_predefined_esri_pcs(cls, p1, p2):
        """
        Fills an :class:`geosoft.gxapi.GXIPJ` with a predefined ESRI PCS
        """
        gxapi_cy.WrapARCMAP.get_ipj_for_predefined_esri_pcs(GXContext._get_tls_geo(), p1._wrapper, p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer