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
        A null (undefined) instance of `GXARCMAP`
        
        :returns: A null `GXARCMAP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXARCMAP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXARCMAP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def change_size(cls, x, y):
        """
        Changes the custom page size of the ArcGIS Map document.
        """
        gxapi_cy.WrapARCMAP.change_size(GXContext._get_tls_geo(), x, y)
        



    @classmethod
    def display_in_3d_view(cls, file):
        """
        Display a file in 3D view
        """
        gxapi_cy.WrapARCMAP.display_in_3d_view(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def export_feature_layer_by_name_to_3d_file(cls, mxd_file, dataframe_name, layer_name, output_file):
        """
        Exports the shapes from a feature layer of the ArcMap document to a 3D File.
        """
        gxapi_cy.WrapARCMAP.export_feature_layer_by_name_to_3d_file(GXContext._get_tls_geo(), mxd_file.encode(), dataframe_name.encode(), layer_name.encode(), output_file.encode())
        



    @classmethod
    def export_selected_feature_layer_to_3d_file(cls, output_file):
        """
        Exports the shapes from the currently selected feature layer (if any) in ArcMap to a 3D file (only on oriented frames i.e. sections).
        """
        gxapi_cy.WrapARCMAP.export_selected_feature_layer_to_3d_file(GXContext._get_tls_geo(), output_file.encode())
        



    @classmethod
    def get_current_document_info(cls, mxd, layer, map):
        """
        Get some info on the current `GXMXD <geosoft.gxapi.GXMXD>` in ArcMap and selected layer (if any)
        """
        mxd.value, layer.value, map.value = gxapi_cy.WrapARCMAP.get_current_document_info(GXContext._get_tls_geo(), mxd.value.encode(), layer.value.encode(), map.value.encode())
        



    @classmethod
    def get_selected_layer_info(cls, layer_number, layer, map):
        """
        Get the name info on the specified selected layer
        """
        layer.value, map.value = gxapi_cy.WrapARCMAP.get_selected_layer_info(GXContext._get_tls_geo(), layer_number, layer.value.encode(), map.value.encode())
        



    @classmethod
    def get_number_of_selected_layers(cls):
        """
        Get the number of selected layers in the TOC
        
        Returns									 The number of layers selected.
        """
        ret_val = gxapi_cy.WrapARCMAP.get_number_of_selected_layers(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def load_map(cls, map, extra_csv, layer_tag, flags):
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
        ret_val = gxapi_cy.WrapARCMAP.load_map(GXContext._get_tls_geo(), map.encode(), extra_csv.encode(), layer_tag.encode(), flags)
        return ret_val



    @classmethod
    def load_map_ex(cls, map, view, extra_csv, layer_tag, flags):
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
        ret_val = gxapi_cy.WrapARCMAP.load_map_ex(GXContext._get_tls_geo(), map.encode(), view.encode(), extra_csv.encode(), layer_tag.encode(), flags)
        return ret_val



    @classmethod
    def load_shape(cls, shp, delete_existing):
        """
        Load a shape file into ArcMap.
        """
        ret_val = gxapi_cy.WrapARCMAP.load_shape(GXContext._get_tls_geo(), shp.encode(), delete_existing)
        return ret_val



    @classmethod
    def load_spf(cls, shp, num_shp):
        """
        Load all the shape files generated by importing a SPF into ArcMap.
        """
        ret_val = gxapi_cy.WrapARCMAP.load_spf(GXContext._get_tls_geo(), shp.encode(), num_shp)
        return ret_val



    @classmethod
    def load_lyr(cls, file):
        """
        Load a LYR file to the current data frame
        """
        gxapi_cy.WrapARCMAP.load_lyr(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def load_map(cls, map, view, extra_csv, layer_tag, fit, activate, prefix):
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
        gxapi_cy.WrapARCMAP.load_map(GXContext._get_tls_geo(), map.encode(), view.encode(), extra_csv.encode(), layer_tag.encode(), fit, activate, prefix)
        



    @classmethod
    def load_map_view(cls, map, view, layer, all):
        """
        Load a Geosoft Map as a layer into the current data frame
        """
        gxapi_cy.WrapARCMAP.load_map_view(GXContext._get_tls_geo(), map.encode(), view.encode(), layer.encode(), all)
        



    @classmethod
    def load_raster(cls, file):
        """
        Load a raster file to the current data frame

        **Note:**

        Loads any file type recognized as "raster" formats by ARC `GXGIS <geosoft.gxapi.GXGIS>`.
        This includes geosoft GRD files.
        """
        gxapi_cy.WrapARCMAP.load_raster(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def load_shape(cls, file, layer_prefix, layer_suffix):
        """
        Load a `GXSHP <geosoft.gxapi.GXSHP>` file to the current data frame

        **Note:**

        The input layer name is created using the (optional) prefix and suffix as follows:
        
        Prefix_NAME_Suffix
        """
        gxapi_cy.WrapARCMAP.load_shape(GXContext._get_tls_geo(), file.encode(), layer_prefix.encode(), layer_suffix.encode())
        



    @classmethod
    def map_view_to_shape(cls, map, view, shp, lst):
        """
        Create `GXSHP <geosoft.gxapi.GXSHP>` file(s) from a Geosoft Map view.

        **Note:**

        The output `GXSHP <geosoft.gxapi.GXSHP>` file name(s) are made up as follows
        (where NAME is the input `GXSHP <geosoft.gxapi.GXSHP>` file name):
        
              NAME_pt.shp    (point objects)
              NAME_ln.shp    (line or arc objects)
              NAME_pg.shp    (polygon objects)
        """
        gxapi_cy.WrapARCMAP.map_view_to_shape(GXContext._get_tls_geo(), map.encode(), view.encode(), shp.encode(), lst._wrapper)
        



    @classmethod
    def query_size(cls, x, y):
        """
        Query the page size in mm of the entire map page.
        """
        x.value, y.value = gxapi_cy.WrapARCMAP.query_size(GXContext._get_tls_geo(), x.value, y.value)
        



    @classmethod
    def show_layer_by_name_in_3d(cls, mxd_file, dataframe_name, layer_name):
        """
        Shows a layer in ArcMap in a 3D view in an `GXMXD <geosoft.gxapi.GXMXD>`
        """
        gxapi_cy.WrapARCMAP.show_layer_by_name_in_3d(GXContext._get_tls_geo(), mxd_file.encode(), dataframe_name.encode(), layer_name.encode())
        



    @classmethod
    def show_selected_layers_in_3d(cls):
        """
        Shows the selected layers in ArcMap in a 3D view
        """
        gxapi_cy.WrapARCMAP.show_selected_layers_in_3d(GXContext._get_tls_geo())
        



    @classmethod
    def get_ipj_for_predefined_esri_gcs(cls, ipj, esri_gcs_code):
        """
        Fills an `GXIPJ <geosoft.gxapi.GXIPJ>` with a predefined ESRI GCS
        """
        gxapi_cy.WrapARCMAP.get_ipj_for_predefined_esri_gcs(GXContext._get_tls_geo(), ipj._wrapper, esri_gcs_code)
        



    @classmethod
    def get_ipj_for_predefined_esri_pcs(cls, ipj, esri_pcs_code):
        """
        Fills an `GXIPJ <geosoft.gxapi.GXIPJ>` with a predefined ESRI PCS
        """
        gxapi_cy.WrapARCMAP.get_ipj_for_predefined_esri_pcs(GXContext._get_tls_geo(), ipj._wrapper, esri_pcs_code)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer