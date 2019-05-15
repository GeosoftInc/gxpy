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
class GXARCMAP(gxapi_cy.WrapARCMAP):
    """
    GXARCMAP class.

    This library is not a class. It contains various utilities
    used in maps and layers by the Geosoft extensions for ArcGIS.
    """

    def __init__(self, handle=0):
        super(GXARCMAP, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXARCMAP <geosoft.gxapi.GXARCMAP>`
        
        :returns: A null `GXARCMAP <geosoft.gxapi.GXARCMAP>`
        :rtype:   GXARCMAP
        """
        return GXARCMAP()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def change_size(cls, x, y):
        """
        Changes the custom page size of the ArcGIS Map document.
        
        :param x:  X Size (mm)
        :param y:  Y Size (mm)
        :type  x:  float
        :type  y:  float

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapARCMAP._change_size(GXContext._get_tls_geo(), x, y)
        



    @classmethod
    def display_in_3d_view(cls, file):
        """
        Display a file in 3D view
        
        :param file:  File Name
        :type  file:  str

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapARCMAP._display_in_3d_view(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def export_feature_layer_by_name_to_3d_file(cls, mxd_file, dataframe_name, layer_name, output_file):
        """
        Exports the shapes from a feature layer of the ArcMap document to a 3D File.
        
        :param mxd_file:        `GXMXD <geosoft.gxapi.GXMXD>` filename
        :param dataframe_name:  Dataframe name
        :param layer_name:      Layer name
        :param output_file:     Output file name
        :type  mxd_file:        str
        :type  dataframe_name:  str
        :type  layer_name:      str
        :type  output_file:     str

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapARCMAP._export_feature_layer_by_name_to_3d_file(GXContext._get_tls_geo(), mxd_file.encode(), dataframe_name.encode(), layer_name.encode(), output_file.encode())
        



    @classmethod
    def export_selected_feature_layer_to_3d_file(cls, output_file):
        """
        Exports the shapes from the currently selected feature layer (if any) in ArcMap to a 3D file (only on oriented frames i.e. sections).
        
        :param output_file:  Output file name
        :type  output_file:  str

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapARCMAP._export_selected_feature_layer_to_3d_file(GXContext._get_tls_geo(), output_file.encode())
        



    @classmethod
    def get_current_document_info(cls, mxd, layer, map):
        """
        Get some info on the current `GXMXD <geosoft.gxapi.GXMXD>` in ArcMap and selected layer (if any)
        
        :param mxd:    `GXMXD <geosoft.gxapi.GXMXD>` filename
        :param layer:  Selected Layer name (If a layer is selected)
        :param map:    Dataframe name containing selected layer (If a layer is selected)
        :type  mxd:    str_ref
        :type  layer:  str_ref
        :type  map:    str_ref

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        mxd.value, layer.value, map.value = gxapi_cy.WrapARCMAP._get_current_document_info(GXContext._get_tls_geo(), mxd.value.encode(), layer.value.encode(), map.value.encode())
        



    @classmethod
    def get_selected_layer_info(cls, layer_number, layer, map):
        """
        Get the name info on the specified selected layer
        
        :param layer_number:  Selected layer number
        :param layer:         Selected Layer name
        :param map:           Dataframe name containing selected layer
        :type  layer_number:  int
        :type  layer:         str_ref
        :type  map:           str_ref

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        layer.value, map.value = gxapi_cy.WrapARCMAP._get_selected_layer_info(GXContext._get_tls_geo(), layer_number, layer.value.encode(), map.value.encode())
        



    @classmethod
    def get_number_of_selected_layers(cls):
        """
        Get the number of selected layers in the TOC

        Returns									 The number of layers selected.
        
        :rtype:      int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapARCMAP._get_number_of_selected_layers(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def load_map(cls, map, extra_csv, layer_tag, flags):
        """
        Loads a Geosoft map into the ArcMap document.
        
        :param map:        Map File Name
        :param extra_csv:  Optional Extra Datasets CSV Filename (Rasters and shape files to display with layers)
        :param layer_tag:  Optional frame/layer tag (suffix)
        :param flags:      Combination of :ref:`ARCMAP_LOAD_FLAGS`
        :type  map:        str
        :type  extra_csv:  str
        :type  layer_tag:  str
        :type  flags:      int

        :returns:          0 - OK
                           1 - Error
                           -1 - Canceled
        :rtype:            int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The extra datasets CSV should contain the the following fields:

         ID          -  Unique identifier
         DATASOURCE  -  Filename
         TYPE        -  RASTER and SHAPE supported
         MAPMATCH    -  Map to associate with (used for grouping logic)
         VIEWMATCH   -  View to match with in associated map (used for grouping logic)
         ZONEFILE    -  Used for type RASTER
        """
        ret_val = gxapi_cy.WrapARCMAP._load_map(GXContext._get_tls_geo(), map.encode(), extra_csv.encode(), layer_tag.encode(), flags)
        return ret_val



    @classmethod
    def load_map_ex(cls, map, view, extra_csv, layer_tag, flags):
        """
        Loads a Geosoft map into the ArcMap document, specifying which View to use as Data view.
        
        :param map:        Map File Name
        :param view:       View Name
        :param extra_csv:  Optional Extra Datasets CSV Filename (Rasters and shape files to display with layers)
        :param layer_tag:  Optional frame/layer tag (suffix)
        :param flags:      Combination of :ref:`ARCMAP_LOAD_FLAGS`
        :type  map:        str
        :type  view:       str
        :type  extra_csv:  str
        :type  layer_tag:  str
        :type  flags:      int

        :returns:          0 - OK
                           1 - Error
                           -1 - Canceled
        :rtype:            int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The extra datasets CSV should contain the the following fields:

         ID          -  Unique identifier
         DATASOURCE  -  Filename
         TYPE        -  RASTER and SHAPE supported
         MAPMATCH    -  Map to associate with (used for grouping logic)
         VIEWMATCH   -  View to match with in associated map (used for grouping logic)
         ZONEFILE    -  Used for type RASTER
        """
        ret_val = gxapi_cy.WrapARCMAP._load_map_ex(GXContext._get_tls_geo(), map.encode(), view.encode(), extra_csv.encode(), layer_tag.encode(), flags)
        return ret_val



    @classmethod
    def load_shape(cls, shp, delete_existing):
        """
        Load a shape file into ArcMap.
        
        :param shp:              Shape file to load
        :param delete_existing:  Delete existing layers?
        :type  shp:              str
        :type  delete_existing:  int

        :returns:                0- OK, 1 - Error, -1 - Cancel
        :rtype:                  int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapARCMAP._load_shape(GXContext._get_tls_geo(), shp.encode(), delete_existing)
        return ret_val



    @classmethod
    def load_spf(cls, shp, num_shp):
        """
        Load all the shape files generated by importing a SPF into ArcMap.
        
        :param shp:      List of shape files to load
        :param num_shp:  Number of shape files
        :type  shp:      str
        :type  num_shp:  int

        :returns:        0- OK, 1 - Error, -1 - Cancel
        :rtype:          int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapARCMAP._load_spf(GXContext._get_tls_geo(), shp.encode(), num_shp)
        return ret_val



    @classmethod
    def load_lyr(cls, file):
        """
        Load a LYR file to the current data frame
        
        :param file:  File Name
        :type  file:  str

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapARCMAP._load_lyr(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def load_map(cls, map, view, extra_csv, layer_tag, fit, activate, prefix):
        """
        Loads a Geosoft map into the current ArcMap document
        
        :param map:        Map File Name
        :param view:       View Name
        :param extra_csv:  Optional Extra Datasets CSV Filename (Rasters and shape files to display with layers)
        :param layer_tag:  Optional frame/layer tag (suffix)
        :param fit:        Fit to map size
        :param activate:   Activate view (3D)
        :param prefix:     Layer name tag is prefix
        :type  map:        str
        :type  view:       str
        :type  extra_csv:  str
        :type  layer_tag:  str
        :type  fit:        int
        :type  activate:   bool
        :type  prefix:     bool

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The extra datasets CSV should contain the the following fields:

            ID          -  Unique identifier
            DATASOURCE  -  Filename
            TYPE        -  RASTER and SHAPE supported
            MAPMATCH    -  Map to associate with (used for grouping logic)
            VIEWMATCH   -  View to match with in associated map (used for grouping logic)
            ZONEFILE    -  Used for type RASTER
        """
        gxapi_cy.WrapARCMAP._load_map(GXContext._get_tls_geo(), map.encode(), view.encode(), extra_csv.encode(), layer_tag.encode(), fit, activate, prefix)
        



    @classmethod
    def load_map_view(cls, map, view, layer, all):
        """
        Load a Geosoft Map as a layer into the current data frame
        
        :param map:    Map File Name
        :param view:   View Name
        :param layer:  Layer Name
        :param all:    Pass TRUE to also render other views in map (Use second parameter view for location)
        :type  map:    str
        :type  view:   str
        :type  layer:  str
        :type  all:    int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapARCMAP._load_map_view(GXContext._get_tls_geo(), map.encode(), view.encode(), layer.encode(), all)
        



    @classmethod
    def load_raster(cls, file):
        """
        Load a raster file to the current data frame
        
        :param file:  File Name
        :type  file:  str

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Loads any file type recognized as "raster" formats by ARC `GXGIS <geosoft.gxapi.GXGIS>`.
        This includes geosoft GRD files.
        """
        gxapi_cy.WrapARCMAP._load_raster(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def load_raster_ex(cls, file):
        """
        Load a raster file to the current data frame and create associated files
        
        :param file:  File Name
        :type  file:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Loads any file type recognized as "raster" formats by ARC `GXGIS <geosoft.gxapi.GXGIS>`.
        This includes geosoft GRD files.
        """
        gxapi_cy.WrapARCMAP._load_raster_ex(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def load_shape(cls, file, layer_prefix, layer_suffix):
        """
        Load a `GXSHP <geosoft.gxapi.GXSHP>` file to the current data frame
        
        :param file:          File Name
        :param layer_prefix:  Layer Name Prefix: An underscore is added automatically
        :param layer_suffix:  Layer Name Suffix  An underscore is added automatically
        :type  file:          str
        :type  layer_prefix:  str
        :type  layer_suffix:  str

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The input layer name is created using the (optional) prefix and suffix as follows:

        Prefix_NAME_Suffix
        """
        gxapi_cy.WrapARCMAP._load_shape(GXContext._get_tls_geo(), file.encode(), layer_prefix.encode(), layer_suffix.encode())
        



    @classmethod
    def map_view_to_shape(cls, map, view, shp, lst):
        """
        Create `GXSHP <geosoft.gxapi.GXSHP>` file(s) from a Geosoft Map view.
        
        :param map:   Map File Name
        :param view:  View Name
        :param shp:   `GXSHP <geosoft.gxapi.GXSHP>` File Name
        :param lst:   List to fill with shape files created
        :type  map:   str
        :type  view:  str
        :type  shp:   str
        :type  lst:   GXLST

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The output `GXSHP <geosoft.gxapi.GXSHP>` file name(s) are made up as follows
        (where NAME is the input `GXSHP <geosoft.gxapi.GXSHP>` file name):

              NAME_pt.shp    (point objects)
              NAME_ln.shp    (line or arc objects)
              NAME_pg.shp    (polygon objects)
        """
        gxapi_cy.WrapARCMAP._map_view_to_shape(GXContext._get_tls_geo(), map.encode(), view.encode(), shp.encode(), lst)
        



    @classmethod
    def query_size(cls, x, y):
        """
        Query the page size in mm of the entire map page.
        
        :param x:  X Size (mm)
        :param y:  Y Size (mm)
        :type  x:  float_ref
        :type  y:  float_ref

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        x.value, y.value = gxapi_cy.WrapARCMAP._query_size(GXContext._get_tls_geo(), x.value, y.value)
        



    @classmethod
    def show_layer_by_name_in_3d(cls, mxd_file, dataframe_name, layer_name):
        """
        Shows a layer in ArcMap in a 3D view in an `GXMXD <geosoft.gxapi.GXMXD>`
        
        :param mxd_file:        `GXMXD <geosoft.gxapi.GXMXD>` filename
        :param dataframe_name:  Dataframe name
        :param layer_name:      Layer name
        :type  mxd_file:        str
        :type  dataframe_name:  str
        :type  layer_name:      str

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapARCMAP._show_layer_by_name_in_3d(GXContext._get_tls_geo(), mxd_file.encode(), dataframe_name.encode(), layer_name.encode())
        



    @classmethod
    def show_selected_layers_in_3d(cls):
        """
        Shows the selected layers in ArcMap in a 3D view
        

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapARCMAP._show_selected_layers_in_3d(GXContext._get_tls_geo())
        



    @classmethod
    def get_ipj_for_predefined_esri_gcs(cls, ipj, esri_gcs_code):
        """
        Fills an `GXIPJ <geosoft.gxapi.GXIPJ>` with a predefined ESRI GCS
        
        :param ipj:            `GXIPJ <geosoft.gxapi.GXIPJ>` to fill
        :param esri_gcs_code:  Predefined ESRI GCS Code
        :type  ipj:            GXIPJ
        :type  esri_gcs_code:  int

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapARCMAP._get_ipj_for_predefined_esri_gcs(GXContext._get_tls_geo(), ipj, esri_gcs_code)
        



    @classmethod
    def get_ipj_for_predefined_esri_pcs(cls, ipj, esri_pcs_code):
        """
        Fills an `GXIPJ <geosoft.gxapi.GXIPJ>` with a predefined ESRI PCS
        
        :param ipj:            `GXIPJ <geosoft.gxapi.GXIPJ>` to fill
        :param esri_pcs_code:  Predefined ESRI PCS Code
        :type  ipj:            GXIPJ
        :type  esri_pcs_code:  int

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapARCMAP._get_ipj_for_predefined_esri_pcs(GXContext._get_tls_geo(), ipj, esri_pcs_code)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer