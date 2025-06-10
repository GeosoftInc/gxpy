#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.

### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
import warnings
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIPJ import GXIPJ


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXGIS(gxapi_cy.WrapGIS):
    """
    GXGIS class.

    The `GXGIS <geosoft.gxapi.GXGIS>` class is used for the import, export,
    and interrogation of `GXGIS <geosoft.gxapi.GXGIS>` Data stored in external formats,
    such as MapInfo® TAB files.
    """

    def __init__(self, handle=0):
        super(GXGIS, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGIS <geosoft.gxapi.GXGIS>`
        
        :returns: A null `GXGIS <geosoft.gxapi.GXGIS>`
        :rtype:   GXGIS
        """
        return GXGIS()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, file, info, type):
        """
        
        Creates a `GXGIS <geosoft.gxapi.GXGIS>` Object
        
        :param file:  Data source (file)
        :param info:  Data qualifying information if required.
        :param type:  :ref:`GIS_TYPE`
        :type  file:  str
        :type  info:  str
        :type  type:  int

        :returns:     `GXGIS <geosoft.gxapi.GXGIS>` Object
        :rtype:       GXGIS

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = gxapi_cy.WrapGIS._create(GXContext._get_tls_geo(), file.encode(), info.encode(), type)
        return GXGIS(ret_val)




    def create_map_2d(self, map, map_scale, ipj, map2_d):
        """
        
        `create_map_2d <geosoft.gxapi.GXGIS.create_map_2d>`   Create a new 2D map for `GXGIS <geosoft.gxapi.GXGIS>` imports.
        
        :param map:        Map name
        :param map_scale:  Map scale (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param ipj:        Projection (no orientation)
        :param map2_d:     :ref:`GIS_MAP2D`
        :type  map:        str
        :type  map_scale:  float
        :type  ipj:        GXIPJ
        :type  map2_d:     int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function was created to minimize duplication in
        creation of new maps with 2D views.
        """
        
        self._create_map_2d(map.encode(), map_scale, ipj, map2_d)
        






    def get_bpr_models_lst(self, file, lst):
        """
        
        Get a `GXLST <geosoft.gxapi.GXLST>` of block models contained in a Gemcom BPR or BRP2 file
        
        :param file:  BPR or BPR2 file
        :param lst:   Returned `GXLST <geosoft.gxapi.GXLST>` of block models
        :type  file:  str
        :type  lst:   GXLST

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Returned `GXLST <geosoft.gxapi.GXLST>` has items in the following format:

        Name:  If there is only one sub-directory with models, then only
        the block model name "Rock Type_5" is required to ensure uniqueness.
        If there is more than one sub-directory, then the name is set
        to (.e.g.) "[Standard]Rock Type_5"
        Value: Sub-directory file path  "Standard\\Rock Type_5.BLK", (includes the extension).

        The Gemcom BPR and BPR2 files keep their block models in one
        or more sub-directories, identified in the ``*.CAT`` file located
        beside the input BPR or BPR2.
        """
        
        self._get_bpr_models_lst(file.encode(), lst)
        




    def get_ipj(self):
        """
        
        Get the `GXGIS <geosoft.gxapi.GXGIS>` `GXIPJ <geosoft.gxapi.GXIPJ>`
        

        :returns:    `GXIPJ <geosoft.gxapi.GXIPJ>` handle
                     NULL if error
        :rtype:      GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is your copy, you must destroy it.
        If the `GXGIS <geosoft.gxapi.GXGIS>` does not have an `GXIPJ <geosoft.gxapi.GXIPJ>`, an `GXIPJ <geosoft.gxapi.GXIPJ>` with
        no warp and UNKNOWN projection is returned.
        """
        
        ret_val = self._get_ipj()
        return GXIPJ(ret_val)




    def get_meta(self, meta):
        """
        
        Get the `GXGIS <geosoft.gxapi.GXGIS>` `GXMETA <geosoft.gxapi.GXMETA>`
        
        :param meta:  Meta object to store `GXGIS <geosoft.gxapi.GXGIS>` meta information
        :type  meta:  GXMETA

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        self._get_meta(meta)
        




    def get_range(self, x_min, x_max, y_min, y_max, z_min, z_max):
        """
        
        Get the range of data in the `GXGIS <geosoft.gxapi.GXGIS>`
        
        :param x_min:  X min
        :param x_max:  X max
        :param y_min:  Y min
        :param y_max:  Y max
        :param z_min:  Z min
        :param z_max:  Z max
        :type  x_min:  float_ref
        :type  x_max:  float_ref
        :type  y_min:  float_ref
        :type  y_max:  float_ref
        :type  z_min:  float_ref
        :type  z_max:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        x_min.value, x_max.value, y_min.value, y_max.value, z_min.value, z_max.value = self._get_range(x_min.value, x_max.value, y_min.value, y_max.value, z_min.value, z_max.value)
        



    @classmethod
    def datamine_type(cls, file):
        """
        
        Returns the type of a Datamine file.
        
        :param file:  Name of input datamine file
        :type  file:  str

        :returns:     Datamine file types - bitwise AND of types.
        :rtype:       int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Terminates if file is not a Datamine file.
        A datamine file can contain fields from a multitude
        of types, so use `GXMATH.and_ <geosoft.gxapi.GXMATH.and_>` or `GXMATH.or_ <geosoft.gxapi.GXMATH.or_>` to determine if
        the file contains the required data.
        """
        
        ret_val = gxapi_cy.WrapGIS._datamine_type(GXContext._get_tls_geo(), file.encode())
        return ret_val




    def get_file_name(self, name):
        """
        
        Get the file name
        
        :param name:  Returned file name
        :type  name:  str_ref

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        name.value = self._get_file_name(name.value.encode())
        



    @classmethod
    def is_mi_map_file(cls, map):
        """
        
        Returns TRUE if file is a MapInfo MAP file.
        
        :param map:  Name of input map file
        :type  map:  str

        :returns:    0 if not a MapInfo MAP file
                     1 if it is.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** It is important not to overwrite a MapInfo MAP file
        with a Geosoft one. Use this function to test the MAP
        file (looks at the first few bytes).
        """
        
        ret_val = gxapi_cy.WrapGIS._is_mi_map_file(GXContext._get_tls_geo(), map.encode())
        return ret_val



    @classmethod
    def is_mi_raster_tab_file(cls, tab):
        """
        
        Returns TRUE if file is a MapInfo Raster TAB file.
        
        :param tab:  Name of input tab file
        :type  tab:  str

        :returns:    0 if not a MapInfo Raster TAB file
                     1 if it is.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = gxapi_cy.WrapGIS._is_mi_raster_tab_file(GXContext._get_tls_geo(), tab.encode())
        return ret_val



    @classmethod
    def is_mi_rotated_raster_tab_file(cls, tab):
        """
        
        Returns TRUE if file is a rotated MapInfo Raster TAB file.
        
        :param tab:  Name of input tab file
        :type  tab:  str

        :returns:    0 if not a rotated MapInfo Raster TAB file
                     1 if it is (see conditions below).
        :rtype:      int

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns 1 if:

            a) This is a MapInfo RASTER file
            b) A three-point warp is defined.
            c) The warp requires a rotation in order to exactly map
               the input and output warp points. The rotation must
               be at least 1.e-6 radians.

        This function will register an error (and return 0)
        if problems are encountered opening or reading the TAB file.
        """
        
        ret_val = gxapi_cy.WrapGIS._is_mi_rotated_raster_tab_file(GXContext._get_tls_geo(), tab.encode())
        return ret_val




    def is_shp_file_3d(self):
        """
        
        Returns TRUE if an ArcView `GXSHP <geosoft.gxapi.GXSHP>` file is type POINTZ, ARCZ, POLYGONZ or MULTIPOINTZ
        

        :returns:    0 if the `GXSHP <geosoft.gxapi.GXSHP>` file is 2D
                     1 if the `GXSHP <geosoft.gxapi.GXSHP>` file is of type POINTZ, ARCZ, POLYGONZ or MULTIPOINTZ
        :rtype:      int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** `GXSHP <geosoft.gxapi.GXSHP>` files come in 2D and 3D forms.
        Fails if not `GIS_TYPE_ARCVIEW <geosoft.gxapi.GIS_TYPE_ARCVIEW>`.
        """
        
        ret_val = self._is_shp_file_3d()
        return ret_val




    def is_shp_file_point(self):
        """
        
        Returns TRUE if an ArcView `GXSHP <geosoft.gxapi.GXSHP>` file is type POINT or POINTZ
        

        :returns:    0 if the `GXSHP <geosoft.gxapi.GXSHP>` file is not points
                     if the `GXSHP <geosoft.gxapi.GXSHP>` file is of type POINT or POINTZ
        :rtype:      int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Fails if not `GIS_TYPE_ARCVIEW <geosoft.gxapi.GIS_TYPE_ARCVIEW>`.
        """
        
        ret_val = self._is_shp_file_point()
        return ret_val




    def num_attribs(self):
        """
        
        The number of attribute fields in the `GXGIS <geosoft.gxapi.GXGIS>` dataset
        

        :returns:    The number of attribute fields
        :rtype:      int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = self._num_attribs()
        return ret_val




    def num_shapes(self):
        """
        
        The number of shape entities in the `GXGIS <geosoft.gxapi.GXGIS>` dataset
        

        :returns:    The number of shape entities
        :rtype:      int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = self._num_shapes()
        return ret_val



    @classmethod
    def scan_mi_raster_tab_file(cls, tab, file, ipj):
        """
        
        Scan and set up a MapInf RASTER.
        
        :param tab:   Name of input file
        :param file:  Name of Raster file (an `GXIMG <geosoft.gxapi.GXIMG>` `GXDAT <geosoft.gxapi.GXDAT>`)
        :param ipj:   Projection
        :type  tab:   str
        :type  file:  str_ref
        :type  ipj:   GXIPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This will create a GI file for the raster image.
        """
        
        file.value = gxapi_cy.WrapGIS._scan_mi_raster_tab_file(GXContext._get_tls_geo(), tab.encode(), file.value.encode(), ipj)
        




    def load_ascii(self, wa):
        """
        
        Save `GXGIS <geosoft.gxapi.GXGIS>` attribute table information (string fields) into a `GXWA <geosoft.gxapi.GXWA>`.
        
        :param wa:   `GXWA <geosoft.gxapi.GXWA>` object
        :type  wa:   GXWA

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All string fields (excluding X/Y and numerical fields) will be saved into the `GXWA <geosoft.gxapi.GXWA>` columns.

        e field names are saved in the first line, followed by a blank line.
        e field columns are separated by a tab (delimited character).
        """
        
        self._load_ascii(wa)
        




    def load_gdb(self, db):
        """
        
        Load `GXGIS <geosoft.gxapi.GXGIS>` table information into a GDB.
        
        :param db:   Database
        :type  db:   GXDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All fields of the database will be loaded into the group.

        Channels will use the same name (or a allowable alias) as
        the `GXGIS <geosoft.gxapi.GXGIS>` field name.

        If a channel does not exist, it will be created based on the
        characteristics of the `GXGIS <geosoft.gxapi.GXGIS>` field.

        If a channel exists, it will be used as-is.
        """
        
        self._load_gdb(db)
        




    def load_map(self, mview):
        """
        
        Load `GXGIS <geosoft.gxapi.GXGIS>` table drawing into a `GXMVIEW <geosoft.gxapi.GXMVIEW>`.
        
        :param mview:  View in which to place `GXGIS <geosoft.gxapi.GXGIS>` drawing.
        :type  mview:  GXMVIEW

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXGIS <geosoft.gxapi.GXGIS>` drawing will be drawin in the current group.
        """
        
        self._load_map(mview)
        




    def load_map_ex(self, map, view_name):
        """
        
        Load `GXGIS <geosoft.gxapi.GXGIS>` table drawing into a `GXMAP <geosoft.gxapi.GXMAP>`.
        
        :param map:        Map handle
        :param view_name:  Name of existing data view
        :type  map:        GXMAP
        :type  view_name:  str

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXGIS <geosoft.gxapi.GXGIS>` drawing will be drawin in the current group.
        """
        
        self._load_map_ex(map, view_name.encode())
        




    def load_meta_groups_map(self, mview, meta, ph_object, prefix, name_field):
        """
        
        Load `GXGIS <geosoft.gxapi.GXGIS>` table drawing into a `GXMVIEW <geosoft.gxapi.GXMVIEW>`.
        
        :param mview:       View in which to place `GXGIS <geosoft.gxapi.GXGIS>` drawing.
        :param ph_object:   Class
        :param prefix:      Group Name prefix
        :param name_field:  Name field (Empty to use ID of entity)
        :type  mview:       GXMVIEW
        :type  meta:        GXMETA
        :type  ph_object:   int
        :type  prefix:      str
        :type  name_field:  str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXGIS <geosoft.gxapi.GXGIS>` drawing will be drawn in the current group.
        A group will be created for every entity and data items
        containing an entity's field will be added to the Meta
        information of every group into the class specified.
        Note that the map may grow very large for big datasets.
        """
        
        self._load_meta_groups_map(mview, meta, ph_object, prefix.encode(), name_field.encode())
        




    def load_ply(self, ply):
        """
        
        Load `GXGIS <geosoft.gxapi.GXGIS>` table drawing into a Multi-Polygon object.
        
        :param ply:  Polygon object in which to place `GXGIS <geosoft.gxapi.GXGIS>` shapes.
        :type  ply:  GXPLY

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        self._load_ply(ply)
        




    def load_shapes_gdb(self, db):
        """
        
        Load `GXGIS <geosoft.gxapi.GXGIS>` shapes table information into separate lines in a GDB.
        
        :param db:   Database
        :type  db:   GXDB

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All fields of the database will be loaded into the group.

        Channels will use the same name (or a allowable alias) as
        the `GXGIS <geosoft.gxapi.GXGIS>` field name.

        If a channel does not exist, it will be created based on the
        characteristics of the `GXGIS <geosoft.gxapi.GXGIS>` field.

        If a channel exists, it will be used as-is.

        The shape ID will be used as the line numbers.
        """
        
        self._load_shapes_gdb(db)
        




    def set_dm_wireframe_pt_file(self, file):
        """
        
        Specify the wireframe point file corresponding to the input file.
        
        :param file:  Name of the wireframe point file
        :type  file:  str

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Datamine wireframe models are specified by pairs of files,
        the first is the triangle node file, and the second gives
        the XYZ locations of the node points. This
        function allows you to specify the latter when reading the
        first, so that the full model can be decoded.
        """
        
        self._set_dm_wireframe_pt_file(file.encode())
        




    def set_ipj(self, ipj):
        """
        
        Save the `GXIPJ <geosoft.gxapi.GXIPJ>` back to `GXGIS <geosoft.gxapi.GXGIS>` file
        
        :param ipj:  `GXIPJ <geosoft.gxapi.GXIPJ>` to save
        :type  ipj:  GXIPJ

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        self._set_ipj(ipj)
        




    def set_lst(self, lst):
        """
        
        Save a `GXLST <geosoft.gxapi.GXLST>` of items inside the `GXGIS <geosoft.gxapi.GXGIS>` object for special use.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object to save to `GXGIS <geosoft.gxapi.GXGIS>` `GXLST <geosoft.gxapi.GXLST>`.
        :type  lst:  GXLST

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the `GXGIS <geosoft.gxapi.GXGIS>` `GXLST <geosoft.gxapi.GXLST>` object already exists, it is destroyed and
        recreated to match the size of the input `GXLST <geosoft.gxapi.GXLST>`, before the
        input `GXLST <geosoft.gxapi.GXLST>` is copied to it.
        """
        
        self._set_lst(lst)
        




    def set_meta(self, meta):
        """
        
        Save the `GXMETA <geosoft.gxapi.GXMETA>` back to `GXGIS <geosoft.gxapi.GXGIS>`
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to save to `GXGIS <geosoft.gxapi.GXGIS>` meta
        :type  meta:  GXMETA

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        self._set_meta(meta)
        




    def set_triangulation_object_index(self, i_toi):
        """
        
        Set the triangulation object index (Micromine)
        
        :param i_toi:  Triangulation object index
        :type  i_toi:  int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        self._set_triangulation_object_index(i_toi)
        




# Deprecated


    @classmethod
    def invert_warp(cls, ipj, ny):
        """
        
        .. deprecated:: 2024.2 Use ScanMIRaseterFile_GIS 
        See deprecation note
        
        :param ipj:  Not used
        :param ny:   Not used
        :type  ipj:  GXIPJ
        :type  ny:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        warnings.warn("""Deprecated since 2024.2, Use ScanMIRaseterFile_GIS""", )
        gxapi_cy.WrapGIS._invert_warp(GXContext._get_tls_geo(), ipj, ny)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer