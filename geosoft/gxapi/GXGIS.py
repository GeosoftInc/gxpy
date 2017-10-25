### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIPJ import GXIPJ


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXGIS:
    """
    GXGIS class.

    The :class:`geosoft.gxapi.GXGIS` class is used for the import, export,
    and interrogation of :class:`geosoft.gxapi.GXGIS` Data stored in external formats,
    such as MapInfo® TAB files.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGIS(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXGIS`
        
        :returns: A null :class:`geosoft.gxapi.GXGIS`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXGIS` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXGIS`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1, p2, p3):
        """
        Creates a :class:`geosoft.gxapi.GXGIS` Object
        """
        ret_val = gxapi_cy.WrapGIS.create(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return GXGIS(ret_val)




    def create_map2_d(self, p2, p3, p4, p5):
        """
        CreateMap2D_GIS   Create a new 2D map for :class:`geosoft.gxapi.GXGIS` imports.

        **Note:**

        This function was created to minimize duplication in
        creation of new maps with 2D views.
        """
        self._wrapper.create_map2_d(p2.encode(), p3, p4._wrapper, p5)
        






    def get_bpr_models_lst(self, p2, p3):
        """
        Get a :class:`geosoft.gxapi.GXLST` of block models contained in a Gemcom BPR or BRP2 file

        **Note:**

        The Returned :class:`geosoft.gxapi.GXLST` has items in the following format:
        
        Name:  If there is only one sub-directory with models, then only
        the block model name "Rock Type_5" is required to ensure uniqueness.
        If there is more than one sub-directory, then the name is set
        to (.e.g.) "[Standard]Rock Type_5"
        Value: Sub-directory file path  "Standard\\Rock Type_5.BLK", (includes the extension).
        
        The Gemcom BPR and BPR2 files keep their block models in one
        or more sub-directories, identified in the ``*.CAT`` file located
        beside the input BPR or BPR2.
        """
        self._wrapper.get_bpr_models_lst(p2.encode(), p3._wrapper)
        




    def get_ipj(self):
        """
        Get the :class:`geosoft.gxapi.GXGIS` :class:`geosoft.gxapi.GXIPJ`

        **Note:**

        This is your copy, you must destroy it.
        If the :class:`geosoft.gxapi.GXGIS` does not have an :class:`geosoft.gxapi.GXIPJ`, an :class:`geosoft.gxapi.GXIPJ` with
        no warp and UNKNOWN projection is returned.
        """
        ret_val = self._wrapper.get_ipj()
        return GXIPJ(ret_val)




    def get_meta(self, p2):
        """
        Get the :class:`geosoft.gxapi.GXGIS` :class:`geosoft.gxapi.GXMETA`
        """
        self._wrapper.get_meta(p2._wrapper)
        




    def get_range(self, p2, p3, p4, p5, p6, p7):
        """
        Get the range of data in the :class:`geosoft.gxapi.GXGIS`
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_range(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        



    @classmethod
    def datamine_type(cls, p1):
        """
        Returns the type of a Datamine file.

        **Note:**

        Terminates if file is not a Datamine file.
        A datamine file can contain fields from a multitude
        of types, so use iAnd_MATH or iOr_MATH to determine if
        the file contains the required data.
        """
        ret_val = gxapi_cy.WrapGIS.datamine_type(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def get_file_name(self, p2):
        """
        Get the file name
        """
        p2.value = self._wrapper.get_file_name(p2.value.encode())
        



    @classmethod
    def is_mi_map_file(cls, p1):
        """
        Returns TRUE if file is a MapInfo MAP file.

        **Note:**

        It is important not to overwrite a MapInfo MAP file
        with a Geosoft one. Use this function to test the MAP
        file (looks at the first few bytes).
        """
        ret_val = gxapi_cy.WrapGIS.is_mi_map_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def is_mi_raster_tab_file(cls, p1):
        """
        Returns TRUE if file is a MapInfo Raster TAB file.
        """
        ret_val = gxapi_cy.WrapGIS.is_mi_raster_tab_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def is_mi_rotated_raster_tab_file(cls, p1):
        """
        Returns TRUE if file is a rotated MapInfo Raster TAB file.

        **Note:**

        Returns 1 if:
        
            a) This is a MapInfo RASTER file
            b) A three-point warp is defined.
            c) The warp requires a rotation in order to exactly map
               the input and output warp points. The rotation must
               be at least 1.e-6 radians.
        
        This function will register an error (and return 0)
        if problems are encountered opening or reading the TAB file.
        """
        ret_val = gxapi_cy.WrapGIS.is_mi_rotated_raster_tab_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def is_shp_file_3d(self):
        """
        Returns TRUE if an ArcView :class:`geosoft.gxapi.GXSHP` file is type POINTZ, ARCZ, POLYGONZ or MULTIPOINTZ

        **Note:**

        :class:`geosoft.gxapi.GXSHP` files come in 2D and 3D forms.
        Fails if not :attr:`geosoft.gxapi.GIS_TYPE_ARCVIEW`.
        """
        ret_val = self._wrapper.is_shp_file_3d()
        return ret_val




    def is_shp_file_point(self):
        """
        Returns TRUE if an ArcView :class:`geosoft.gxapi.GXSHP` file is type POINT or POINTZ

        **Note:**

        Fails if not :attr:`geosoft.gxapi.GIS_TYPE_ARCVIEW`.
        """
        ret_val = self._wrapper.is_shp_file_point()
        return ret_val




    def num_attribs(self):
        """
        The number of attribute fields in the :class:`geosoft.gxapi.GXGIS` dataset
        """
        ret_val = self._wrapper.num_attribs()
        return ret_val




    def num_shapes(self):
        """
        The number of shape entities in the :class:`geosoft.gxapi.GXGIS` dataset
        """
        ret_val = self._wrapper.num_shapes()
        return ret_val



    @classmethod
    def scan_mi_raster_tab_file(cls, p1, p2, p4):
        """
        Scan and set up a MapInf RASTER.

        **Note:**

        This will create a GI file for the raster image.
        """
        p2.value = gxapi_cy.WrapGIS.scan_mi_raster_tab_file(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4._wrapper)
        




    def load_ascii(self, p2):
        """
        Save :class:`geosoft.gxapi.GXGIS` attribute table information (string fields) into a :class:`geosoft.gxapi.GXWA`.

        **Note:**

        All string fields (excluding X/Y and numerical fields) will be saved into the :class:`geosoft.gxapi.GXWA` columns.
        
        e field names are saved in the first line, followed by a blank line.
        e field columns are separated by a tab (delimited character).
        """
        self._wrapper.load_ascii(p2._wrapper)
        




    def load_gdb(self, p2):
        """
        Load :class:`geosoft.gxapi.GXGIS` table information into a GDB.

        **Note:**

        All fields of the database will be loaded into the group.
        
        Channels will use the same name (or a allowable alias) as
        the :class:`geosoft.gxapi.GXGIS` field name.
        
        If a channel does not exist, it will be created based on the
        characteristics of the :class:`geosoft.gxapi.GXGIS` field.
        
        If a channel exists, it will be used as-is.
        """
        self._wrapper.load_gdb(p2._wrapper)
        




    def load_map(self, p2):
        """
        Load :class:`geosoft.gxapi.GXGIS` table drawing into a :class:`geosoft.gxapi.GXMVIEW`.

        **Note:**

        The :class:`geosoft.gxapi.GXGIS` drawing will be drawin in the current group.
        """
        self._wrapper.load_map(p2._wrapper)
        




    def load_map_ex(self, p2, p3):
        """
        Load :class:`geosoft.gxapi.GXGIS` table drawing into a :class:`geosoft.gxapi.GXMAP`.

        **Note:**

        The :class:`geosoft.gxapi.GXGIS` drawing will be drawin in the current group.
        """
        self._wrapper.load_map_ex(p2._wrapper, p3.encode())
        




    def load_meta_groups_map(self, p2, p3, p4, p5, p6):
        """
        Load :class:`geosoft.gxapi.GXGIS` table drawing into a :class:`geosoft.gxapi.GXMVIEW`.

        **Note:**

        The :class:`geosoft.gxapi.GXGIS` drawing will be drawn in the current group.
        A group will be created for every entity and data items
        containing an entity's field will be added to the Meta
        information of every group into the class specified.
        Note that the map may grow very large for big datasets.
        """
        self._wrapper.load_meta_groups_map(p2._wrapper, p3._wrapper, p4, p5.encode(), p6.encode())
        




    def load_ply(self, p2):
        """
        Load :class:`geosoft.gxapi.GXGIS` table drawing into a Multi-Polygon object.
        """
        self._wrapper.load_ply(p2._wrapper)
        




    def load_shapes_gdb(self, p2):
        """
        Load :class:`geosoft.gxapi.GXGIS` shapes table information into separate lines in a GDB.

        **Note:**

        All fields of the database will be loaded into the group.
        
        Channels will use the same name (or a allowable alias) as
        the :class:`geosoft.gxapi.GXGIS` field name.
        
        If a channel does not exist, it will be created based on the
        characteristics of the :class:`geosoft.gxapi.GXGIS` field.
        
        If a channel exists, it will be used as-is.
        
        The shape ID will be used as the line numbers.
        """
        self._wrapper.load_shapes_gdb(p2._wrapper)
        




    def set_dm_wireframe_pt_file(self, p2):
        """
        Specify the wireframe point file corresponding to the input file.

        **Note:**

        Datamine wireframe models are specified by pairs of files,
        the first is the triangle node file, and the second gives
        the XYZ locations of the node points. This
        function allows you to specify the latter when reading the
        first, so that the full model can be decoded.
        """
        self._wrapper.set_dm_wireframe_pt_file(p2.encode())
        




    def set_ipj(self, p2):
        """
        Save the :class:`geosoft.gxapi.GXIPJ` back to :class:`geosoft.gxapi.GXGIS` file
        """
        self._wrapper.set_ipj(p2._wrapper)
        




    def set_lst(self, p2):
        """
        Save a :class:`geosoft.gxapi.GXLST` of items inside the :class:`geosoft.gxapi.GXGIS` object for special use.

        **Note:**

        If the :class:`geosoft.gxapi.GXGIS` :class:`geosoft.gxapi.GXLST` object already exists, it is destroyed and
        recreated to match the size of the input :class:`geosoft.gxapi.GXLST`, before the
        input :class:`geosoft.gxapi.GXLST` is copied to it.
        """
        self._wrapper.set_lst(p2._wrapper)
        




    def set_meta(self, p2):
        """
        Save the :class:`geosoft.gxapi.GXMETA` back to :class:`geosoft.gxapi.GXGIS`
        """
        self._wrapper.set_meta(p2._wrapper)
        




    def set_triangulation_object_index(self, p2):
        """
        Set the triangulation object index (Micromine)
        """
        self._wrapper.set_triangulation_object_index(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer