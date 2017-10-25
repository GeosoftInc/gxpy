### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXPG import GXPG
from .GXST import GXST


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVOX:
    """
    GXVOX class.

    High Performance 3D Grid. Designed for accessing
    3D grids quickly using slices. It designed arround
    non-uniform multi-resolution  compressed storage.
    o sample a voxel at specific locations, use the :class:`geosoft.gxapi.GXVOXE` class.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVOX(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXVOX`
        
        :returns: A null :class:`geosoft.gxapi.GXVOX`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXVOX` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXVOX`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def calc_stats(self, p2):
        """
        Calculate Statistics
        """
        self._wrapper.calc_stats(p2._wrapper)
        



    @classmethod
    def create(cls, p1):
        """
        Create a handle to an :class:`geosoft.gxapi.GXVOX` object
        """
        ret_val = gxapi_cy.WrapVOX.create(GXContext._get_tls_geo(), p1.encode())
        return GXVOX(ret_val)




    def create_pg(self):
        """
        Create a 3D :class:`geosoft.gxapi.GXPG` from a :class:`geosoft.gxapi.GXVOX` object
        """
        ret_val = self._wrapper.create_pg()
        return GXPG(ret_val)




    def create_type_pg(self, p2):
        """
        Create a 3D :class:`geosoft.gxapi.GXPG` from a :class:`geosoft.gxapi.GXVOX` object with a specific Type
        """
        ret_val = self._wrapper.create_type_pg(p2)
        return GXPG(ret_val)






    def dump(self, p2):
        """
        Export all layers of this :class:`geosoft.gxapi.GXVOX` in all directions.
        """
        self._wrapper.dump(p2.encode())
        




    def export_img(self, p2, p3):
        """
        Export all layers of this :class:`geosoft.gxapi.GXVOX` into grid files.
        """
        self._wrapper.export_img(p2.encode(), p3)
        




    def export_to_grids(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Export all layers of this :class:`geosoft.gxapi.GXVOX` into grid files, with optional cell size.

        **Note:**

        If the cell size is not specified, then:
        1. If the cell sizes are uniform in a given direction, that size is used
        2. If the cell sizes are variable in a given direction, then the smallest size is used
        """
        self._wrapper.export_to_grids(p2.encode(), p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def export_xml(cls, p1, p2, p3):
        """
        Export a :class:`geosoft.gxapi.GXVOX` to a compressed XML file
        """
        p2.value = gxapi_cy.WrapVOX.export_xml(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.encode())
        




    def export_seg_y(self, p2, p3):
        """
        Export a voxel to a depth SEG-Y file
        """
        self._wrapper.export_seg_y(p2.encode(), p3)
        



    @classmethod
    def export_ji_gs_xml(cls, p1, p2):
        """
        Export a :class:`geosoft.gxapi.GXVOX` to a compressed XML file. Verbose version.
        """
        gxapi_cy.WrapVOX.export_ji_gs_xml(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        




    def export_xyz(self, p2, p3, p4, p5, p6, p7):
        """
        Export a Voxel to an XYZ File
        """
        self._wrapper.export_xyz(p2.encode(), p3, p4, p5, p6, p7)
        




    def filter(self, p2, p3, p4, p5, p6):
        """
        Apply a 3D filter to a voxel.
        """
        self._wrapper.filter(p2, p3.encode(), p4, p5, p6.encode())
        



    @classmethod
    def generate_db(cls, p1, p2, p3):
        """
        Generate a :class:`geosoft.gxapi.GXVOX` from a Database
        """
        gxapi_cy.WrapVOX.generate_db(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3)
        



    @classmethod
    def generate_vector_voxel_from_db(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Generate a vector voxel :class:`geosoft.gxapi.GXVOX` from a Database
        """
        gxapi_cy.WrapVOX.generate_vector_voxel_from_db(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def generate_pg(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Generate a :class:`geosoft.gxapi.GXVOX` from a 3D Pager
        """
        ret_val = gxapi_cy.WrapVOX.generate_pg(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7, p8, p9._wrapper, p10._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_constant_value(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Generate a :class:`geosoft.gxapi.GXVOX` with a constant value
        """
        ret_val = gxapi_cy.WrapVOX.generate_constant_value(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13._wrapper, p14._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_pgvv(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Generate a :class:`geosoft.gxapi.GXVOX` from a 3D Pager, cells sizes passed in VVs.

        **Note:**

        The input cell size VVs' lengths must match the input :class:`geosoft.gxapi.GXPG` dimensions.
        """
        ret_val = gxapi_cy.WrapVOX.generate_pgvv(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_constant_value_vv(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Generate a :class:`geosoft.gxapi.GXVOX` with a constant value, cells sizes passed in VVs.
        """
        ret_val = gxapi_cy.WrapVOX.generate_constant_value_vv(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def init_generate_by_subset_pg(cls, p1, p2, p3, p4):
        """
        Initialize the generate of a :class:`geosoft.gxapi.GXVOX` from a series of 3D subset pagers

        **Note:**

        Call InitGenerateBySubsetPG_VOX first, then add a series of subset PGs using AddGenerateBySubsetPG_VOX, and finally
        serialize using EndGenerateBySubsetPG_VOX
        """
        ret_val = gxapi_cy.WrapVOX.init_generate_by_subset_pg(GXContext._get_tls_geo(), p1, p2, p3, p4)
        return GXVOX(ret_val)




    def add_generate_by_subset_pg(self, p2, p3, p4):
        """
        Add a subset 3D  pagers. These should be "slabs", 16 wide in the input direction, and the size of the
        full voxel in the other two directions.

        **Note:**

        See InitGenerateBySubsetPG_VOX and EndGenerateBySubsetPG_VOX.
        """
        self._wrapper.add_generate_by_subset_pg(p2._wrapper, p3, p4)
        




    def end_generate_by_subset_pg(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Output the voxel, after adding all the subset PGs.

        **Note:**

        You must begin by calling InitGenerateBySubsetPG_VOX and add data using AddGenerateBySubsetPG_VOX.
        """
        self._wrapper.end_generate_by_subset_pg(p2.encode(), p3, p4, p5, p6, p7, p8, p9._wrapper, p10._wrapper)
        




    def get_area(self, p2, p3, p4, p5, p6, p7):
        """
        Get the area of the voxel.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_area(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_gocad_location(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13):
        """
        Get the location of a voxel with origin and scaled xyz vectors for use with GOCAD.

        **Note:**

        This is used for GOCAD voxel calculations, and begins with the
        origin at (0,0,0), not the actual location of the corner point.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value = self._wrapper.get_gocad_location(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value)
        




    def get_grid_section_cell_sizes(self, p2, p3, p4):
        """
        Get default cell sizes in X and Y for a section grid.

        **Note:**

        This function determines default cell sizes for a vertical grid
        slicing a voxel. It tries to match the "X" and "Y" sizes (in the grid
        coordinates) with the projection of the voxel's cells onto the grid
        plane. It uses a few simple rules:
        
        If the voxel is rotated about a horizontal axis (i.e. if its own "Z" axis
        is not vertical, then both cell sizes are set to the smallest voxel dimension
        (a single volume pixel) in X, Y and Z.
        
        If the voxel is "horizontal", then the angle between the
        section azimuth and the voxel's own X and Y axes is used to
        calculate a value which varies between the minimum X size and the
        minimum Y size, and this is used for the grid's "X" cell size.
        (in other words, if the section is parallel to the voxel "X" axis,
        then the returned "X" cells size is equal to the voxel's minimum "Y" cell size.
        The grid's "Y" cell size is set to the voxel's minimum "Z" cell size.
        """
        p3.value, p4.value = self._wrapper.get_grid_section_cell_sizes(p2, p3.value, p4.value)
        




    def get_info(self, p2, p3, p4, p5, p6):
        """
        Get information about a voxel.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_info(p2.value, p3.value, p4.value, p5.value, p6.value)
        




    def get_ipj(self, p2):
        """
        Get the projection of the voxel.
        """
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_limits(self, p2, p3, p4, p5, p6, p7):
        """
        Get the range of indices with non-dummy data.

        **Note:**

        Find the non-dummy volume of a :class:`geosoft.gxapi.GXVOX` object. If the voxel is all dummies,
        returns :attr:`geosoft.gxapi.iMAX` for the minima, and :attr:`geosoft.gxapi.iMIN` for the maxima.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_limits(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_limits_xyz(self, p2, p3, p4, p5, p6, p7):
        """
        Get the range in true XYZ of non-dummy data.

        **Note:**

        Find the non-dummy volume of a :class:`geosoft.gxapi.GXVOX` in true (X, Y, Z). This method
        works for voxels which are rotated or oriented in 3D, and returns
        the true min and max X, Y and Z limits in the data.
        The bounds are the bounds for the voxel
        center points. If the voxel is all dummies,
        returns :attr:`geosoft.gxapi.rMAX` for the minima, and :attr:`geosoft.gxapi.rMIN` for the maxima.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_limits_xyz(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_location(self, p2, p3, p4, p5, p6, p7):
        """
        Get Location information
        """
        p2.value, p3.value, p4.value = self._wrapper.get_location(p2.value, p3.value, p4.value, p5._wrapper, p6._wrapper, p7._wrapper)
        




    def get_location_points(self, p2, p3, p4):
        """
        Get the computed location points.
        """
        self._wrapper.get_location_points(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def get_meta(self, p2):
        """
        Get the metadata of a voxel.
        """
        self._wrapper.get_meta(p2._wrapper)
        




    def get_double_location(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13):
        """
        Get the location of a voxel with origin and scaled xyz vectors
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value = self._wrapper.get_double_location(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value)
        




    def get_simple_location(self, p2, p3, p4, p5, p6, p7):
        """
        Get Simple Location information
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_simple_location(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_stats(self):
        """
        Get precomputed statistics on this object.
        """
        ret_val = self._wrapper.get_stats()
        return GXST(ret_val)




    def get_tpat(self, p2):
        """
        Get a copy of a thematic voxel's :class:`geosoft.gxapi.GXTPAT` object.

        **Note:**

        Each row in the :class:`geosoft.gxapi.GXTPAT` object corresponds to a stored index
        value in the thematic voxel. The :class:`geosoft.gxapi.GXTPAT` should NOT be modified
        by the addition or deletion of items, if it is to be
        restored into the :class:`geosoft.gxapi.GXVOX` object, but the CODE, LABEL, DESCRIPTION
        or COLOR info can be changed.
        The :class:`geosoft.gxapi.GXTPAT` object is stored inside the :class:`geosoft.gxapi.GXVOX` :class:`geosoft.gxapi.GXMETA` object.
        """
        self._wrapper.get_tpat(p2._wrapper)
        



    @classmethod
    def grid_points(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20):
        """
        Grid a :class:`geosoft.gxapi.GXVOX` from point :class:`geosoft.gxapi.GXVV`'s.
        """
        ret_val = gxapi_cy.WrapVOX.grid_points(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16._wrapper, p17._wrapper, p18._wrapper, p19._wrapper, p20._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def grid_points_z(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21):
        """
        Grid a :class:`geosoft.gxapi.GXVOX` from point :class:`geosoft.gxapi.GXVV`'s (using variable Z's)
        """
        ret_val = gxapi_cy.WrapVOX.grid_points_z(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4.encode(), p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17._wrapper, p18._wrapper, p19._wrapper, p20._wrapper, p21._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def grid_points_z_ex(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26):
        """
        Grid a :class:`geosoft.gxapi.GXVOX` from point :class:`geosoft.gxapi.GXVV`'s (using variable Z's)
        """
        ret_val, p12.value, p13.value, p15.value = gxapi_cy.WrapVOX.grid_points_z_ex(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4.encode(), p5, p6, p7, p8, p9, p10, p11, p12.value, p13.value, p14, p15.value, p16, p17, p18, p19, p20, p21, p22._wrapper, p23._wrapper, p24._wrapper, p25._wrapper, p26._wrapper)
        return GXVOX(ret_val)




    def can_append_to(self, p2):
        """
        Check if this voxel can append to a surface file.
        """
        ret_val = self._wrapper.can_append_to(p2.encode())
        return ret_val




    def get_cell_size_strings(self, p2, p4, p6, p8, p9, p10):
        """
        Get the Location Strings
        """
        p2.value, p4.value, p6.value = self._wrapper.get_cell_size_strings(p2.value.encode(), p4.value.encode(), p6.value.encode(), p8, p9, p10)
        




    def is_thematic(self):
        """
        Is this a thematic voxel?

        **Note:**

        A thematic voxel is one where the stored integer values
        represent indices into an internally stored :class:`geosoft.gxapi.GXTPAT` object.
        Thematic voxels contain their own color definitions, and
        normal numerical operations, such as applying ITRs for display,
        are not valid.
        """
        ret_val = self._wrapper.is_thematic()
        return ret_val




    def is_vector_voxel(self):
        """
        Is this a vector voxel?

        **Note:**

        A vector voxel is one where each data element consists of 3 4-byte float values.
        Vector voxels normally have the file type "geosoft_vectorvoxel".
        """
        ret_val = self._wrapper.is_vector_voxel()
        return ret_val




    def set_cell_size_strings(self, p2, p3, p4):
        """
        Set the Location Strings
        """
        ret_val = self._wrapper.set_cell_size_strings(p2.encode(), p3.encode(), p4.encode())
        return ret_val



    @classmethod
    def log_grid_points_z_ex(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28):
        """
        Log grid a :class:`geosoft.gxapi.GXVOX` from point :class:`geosoft.gxapi.GXVV`'s (using variable Z's)
        """
        ret_val, p12.value, p13.value, p15.value = gxapi_cy.WrapVOX.log_grid_points_z_ex(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4.encode(), p5, p6, p7, p8, p9, p10, p11, p12.value, p13.value, p14, p15.value, p16, p17, p18, p19, p20, p21, p22, p23, p24._wrapper, p25._wrapper, p26._wrapper, p27._wrapper, p28._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def krig(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        A more compact and extensible form of LogGridPointsZEx_VOX.

        **Note:**

        Optional Parameters.
        
        If these values are not set in the :class:`geosoft.gxapi.GXREG`, then default parameters will be used.
        
        ERROR_VOXEL:		Name of error :class:`geosoft.gxapi.GXVOX` ("" for none)
        CELLSIZEZ:      Z Cell size string (space delimited, "" for default)
        RADIUS_MIN:		Minimum Search Radius (REAL) (Default = 4) (Blanking Distance)
        RADIUS_MAX:		Maximum Search Radius (REAL) (Default = 16)
        SEARCH_MIN:		Minimum Search Points (INT) (Default = 16)
        SEARCH_MAX:		Maximum Search Points (INT) (Default = 32)
        VARIOGRAM_ONLY: Set to 1 to calculate the variogram only (INT) (Default = 0)
        MODEL:				Variogram Model number 1-power, 2-sperical, 3-gaussian, 4-exponential  (INT) (Default = 2)
        POWER:          Power (Default = DUMMY)
        SLOPE:          Slope (REAL) (if input is DUMMY, value calculated and set on return)
        RANGE:          Range (REAL) (if input is DUMMY, value calculated and set on return)
        SILL :          Sill (REAL) (if input is DUMMY, value calculated and set on return)
        STRIKE:				Strike (REAL) (Default = 0)
        DIP:					Dip (REAL)	(Default = 90)
        PLUNGE:				Plunge (REAL) (Default = 0)
        STRIKE WEIGHT:	Along-Strike Weight (REAL) (Default = 1)
        DIP_WEIGHT:      Down-Dip Weight (REAL) (Default = 1)
        LOG_OPT:			One of `VOX_GRID_LOGOPT` (Default = 0)
        MIN_LOG:			Log Minimum (REAL)	(Default = 1)
        MIN_X:				Minimum X (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. multiple of cell size chosen)
        MAX_X:				Maximum X (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)
        MIN_Y:				Minimum Y (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. external multiple of cell size chosen)
        MAX_Y:				Maximum Y (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)
        MIN_Z:				Minimum Z (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. multiple of cell size chosen)
        MAX_Z:				Maximum Z (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)A more compact and extensible form of LogGridPointsZEx_VOX. Only the most
        basic parameters are entered directly. Optional parameters are passed via a :class:`geosoft.gxapi.GXREG` object.
        """
        ret_val = gxapi_cy.WrapVOX.krig(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def math(cls, p1, p2, p3, p4, p5, p6):
        """
        Produces a new voxes using a formula on existing voxels/Grids

        **Note:**

        The input voxels must all be of the same type.
        """
        ret_val = gxapi_cy.WrapVOX.math(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6._wrapper)
        return GXVOX(ret_val)




    def merge(self, p2, p3, p4):
        """
        Merge two Voxels.
        """
        self._wrapper.merge(p2._wrapper, p3._wrapper, p4.encode())
        



    @classmethod
    def nearest_neighbour_grid(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Grid a :class:`geosoft.gxapi.GXVOX` from point :class:`geosoft.gxapi.GXVV`'s using the Nearest Neighbours method.
        """
        ret_val = gxapi_cy.WrapVOX.nearest_neighbour_grid(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def compute_cell_size(cls, p1, p2, p3, p4, p5, p6):
        """
        Compute the Cell size based on specific Area
        """
        ret_val = gxapi_cy.WrapVOX.compute_cell_size(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6)
        return ret_val




    def re_grid(self, p2, p3, p4):
        """
        Regrid a Voxel.
        """
        self._wrapper.re_grid(p2._wrapper, p3._wrapper, p4.encode())
        




    def resample_pg(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Resample a voxel over an input volume to a :class:`geosoft.gxapi.GXPG`.

        **Note:**

        Creates and dummies a :class:`geosoft.gxapi.GXPG` object based on the input
        dimensions, then resamples the voxel to the pager
        at the locations determined by input projection, origin and spacings.
        """
        ret_val = self._wrapper.resample_pg(p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14)
        return GXPG(ret_val)




    def rescale_cell_sizes(self, p2):
        """
        Multiply all cell sizes by a fixed factor.

        **Note:**

        This is useful, for instance for converting sizes in one
        unit to sizes in another unit if changing the projection
        and the projection's unit changes, since the voxel inherits
        its projection's units.
        """
        self._wrapper.rescale_cell_sizes(p2)
        




    def sample_cdi(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Sample a voxel at locations/elevations in a CDI database.

        **Note:**

        A "CDI" database does not need to be conductivity/depth.
        It normally contains an array channel of depth values for
        each (X, Y) location, with corresponding data array channels of
        values taken at those (X, Y, Z) locations.
        If the optional elevation channel is used, its value is used as an
        offset to the depth channel values. Depths are positive down by
        default; use the "Negative depths down" parameter if the depths
        become more negative as you go deeper.
        """
        self._wrapper.sample_cdi(p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10.encode())
        




    def sample_cdi_to_topography(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Sample a voxel at fixed elevations along a path in a CDI database, and output them to an array channel, deleting leading dummy values, and
        writing the elevation of the first non-dummy item to a topography channel.
        """
        self._wrapper.sample_cdi_to_topography(p2._wrapper, p3, p4, p5, p6._wrapper, p7, p8.encode(), p9.encode())
        




    def sample_vv(self, p2, p3, p4, p5, p6):
        """
        Sample a voxel at multiple locations.

        **Note:**

        Sample at voxel at XYZ locations input in VVs. Values returned in a :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.sample_vv(p2._wrapper, p3._wrapper, p4._wrapper, p5, p6._wrapper)
        




    def set_ipj(self, p2):
        """
        Set the projection of the voxel.
        """
        self._wrapper.set_ipj(p2._wrapper)
        




    def set_location(self, p2, p3, p4, p5, p6, p7):
        """
        Set Location information
        """
        self._wrapper.set_location(p2, p3, p4, p5._wrapper, p6._wrapper, p7._wrapper)
        




    def set_meta(self, p2):
        """
        Set the metadata of a voxel.
        """
        self._wrapper.set_meta(p2._wrapper)
        




    def set_origin(self, p2, p3, p4, p5):
        """
        Set the Voxel Origin
        """
        self._wrapper.set_origin(p2, p3, p4, p5)
        




    def set_simple_location(self, p2, p3, p4, p5, p6, p7):
        """
        Set Simple Location information
        """
        self._wrapper.set_simple_location(p2, p3, p4, p5, p6, p7)
        




    def set_tpat(self, p2):
        """
        Set a thematic voxel's :class:`geosoft.gxapi.GXTPAT` object.

        **Note:**

        Each row in the :class:`geosoft.gxapi.GXTPAT` object corresponds to a stored index
        value in the thematic voxel. The :class:`geosoft.gxapi.GXTPAT` should NOT be modified
        by the addition or deletion of items, if it is to be
        restored into the :class:`geosoft.gxapi.GXVOX` object, but the CODE, LABEL, DESCRIPTION
        or COLOR info can be changed.
        The :class:`geosoft.gxapi.GXTPAT` object is stored inside the :class:`geosoft.gxapi.GXVOX` :class:`geosoft.gxapi.GXMETA` object.
        """
        self._wrapper.set_tpat(p2._wrapper)
        




    def slice_ipj(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Extract a slice of a voxel based on an :class:`geosoft.gxapi.GXIPJ`
        """
        self._wrapper.slice_ipj(p2.encode(), p3._wrapper, p4, p5, p6, p7, p8, p9, p10)
        




    def slice_multi_layer_ipj(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13):
        """
        Extract multiple slices of a voxel based on an :class:`geosoft.gxapi.GXIPJ`
        """
        self._wrapper.slice_multi_layer_ipj(p2.encode(), p3._wrapper, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        




    def subset_to_double_extents(self, p2):
        """
        Subset a :class:`geosoft.gxapi.GXVOX` to real extents.
        """
        self._wrapper.subset_to_double_extents(p2.encode())
        



    @classmethod
    def sync(cls, p1):
        """
        Syncronize the Metadata for this Voxel
        """
        gxapi_cy.WrapVOX.sync(GXContext._get_tls_geo(), p1.encode())
        




    def window_ply(self, p2, p3, p4, p5, p6, p7):
        """
        Window a :class:`geosoft.gxapi.GXVOX` to a :class:`geosoft.gxapi.GXPLY` file and Z.

        **Note:**

        The voxel is windowed horizontally to the input :class:`geosoft.gxapi.GXPLY` file.
        Optionally, it will be windowed to the input Z range as well.
        The output can be clipped to the non-dummied cells.
        """
        self._wrapper.window_ply(p2._wrapper, p3, p4, p5, p6.encode(), p7)
        




    def window_xyz(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Window a :class:`geosoft.gxapi.GXVOX` to ranges in X, Y and Z.

        **Note:**

        The six minima and maxima are optional.
        The output can be clipped to the non-dummied cells.
        """
        self._wrapper.window_xyz(p2, p3, p4, p5, p6, p7, p8.encode(), p9)
        




    def write_xml(self, p2):
        """
        Export the :class:`geosoft.gxapi.GXVOX` to XML
        """
        self._wrapper.write_xml(p2.encode())
        




    def convert_numeric_to_thematic(self, p2, p3):
        """
        Convert numeric voxel to thematic (lithology) voxel
        """
        self._wrapper.convert_numeric_to_thematic(p2._wrapper, p3.encode())
        




    def convert_thematic_to_numeric(self, p2, p3):
        """
        Convert thematic (lithology) voxel to numeric voxel
        """
        self._wrapper.convert_thematic_to_numeric(p2._wrapper, p3.encode())
        




    def convert_velocity_to_density(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Produces a density voxel using the velocity values in this voxel.
        """
        self._wrapper.convert_velocity_to_density(p2, p3, p4, p5, p6, p7, p8, p9, p10.encode())
        




    def convert_velocity_in_range_to_density(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Produces a density voxel using the velocity values in this voxel, as long as the velocity values are in range.
        """
        self._wrapper.convert_velocity_in_range_to_density(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12.encode())
        




    def convert_density_to_velocity(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Produces a velocity voxel using the density values in this voxel.
        """
        self._wrapper.convert_density_to_velocity(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12.encode())
        




    def invert_z(self, p2):
        """
        Convert an inverted voxel to normal orientation
        """
        self._wrapper.invert_z(p2.encode())
        



    @classmethod
    def dw_grid_db(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        IDWGridDB_VOX     Inverse-distance weighting gridding method, :class:`geosoft.gxapi.GXDB` version, 3D.

        **Note:**

        3D cells take on the averaged values within a search radius, weighted inversely by distance.
        
        Weighting can be controlled using the power and slope properties;
        
        weighting = 1 / (distance^wtpower + 1/slope) where distance is in
        units of grid cells (X dimenstion). Default is 0.0,
        
        If the blanking distance is set, all cells whose center point is not within the blanking distance of
        at least one data point are set to dummy.
        
        :class:`geosoft.gxapi.GXREG` Parameters:
        
        X0, Y0, Z0, DX, DY, DZ: Voxel origin, and cell sizes (required)
        WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters
        SEARCH_RADIUS: Distance weighting limit (default = 4 * CUBE_ROOT(DX*DY*DZ))
        BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 * CUBE_ROOT(DX*DY*DZ))
        LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?
        LOG_BASE: One of :attr:`geosoft.gxapi.VV_LOG_BASE_10` (default) or :attr:`geosoft.gxapi.VV_LOG_BASE_E`
        LOG_NEGATIVE: One of :attr:`geosoft.gxapi.VV_LOG_NEGATIVE_NO` (default) or :attr:`geosoft.gxapi.VV_LOG_NEGATIVE_YES`
        """
        gxapi_cy.WrapVOX.dw_grid_db(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7._wrapper)
        



    @classmethod
    def tin_grid_db(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        TINGridDB_VOX   :class:`geosoft.gxapi.GXTIN`-Gridding, :class:`geosoft.gxapi.GXDB` version, 3D.

        **Note:**

        Designed for data in array channels position vertically at single XY locations.
        Creates a :class:`geosoft.gxapi.GXTIN` using the XY locations and uses the coefficients for the top layer on
        each layer below to make it efficient.
        
        :class:`geosoft.gxapi.GXREG` Parameters:
        
        X0, Y0, Z0, DX, DY, DZ: Voxel origin, and cell sizes (required)
        NX, NY, NZ: Voxel dimensions.
        DZ and NZ are used only if the input cell sizes :class:`geosoft.gxapi.GXVV` is of zero length.
        """
        gxapi_cy.WrapVOX.tin_grid_db(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7, p8._wrapper, p9._wrapper)
        



    @classmethod
    def get_multi_voxset_guid(cls, p1, p2):
        """
        Get the UUID
        """
        p2.value = gxapi_cy.WrapVOX.get_multi_voxset_guid(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def generate_gocad(cls, p1, p2, p3, p4):
        """
        Generate a :class:`geosoft.gxapi.GXVOX` from a GOCAD File
        """
        ret_val = gxapi_cy.WrapVOX.generate_gocad(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_oriented_gocad(cls, p1, p2, p3, p4, p5):
        """
        Generate a :class:`geosoft.gxapi.GXVOX` from a GOCAD File

        **Note:**

        Allows the Orientation flag to be specified.
        """
        ret_val = gxapi_cy.WrapVOX.generate_oriented_gocad(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4._wrapper, p5)
        return GXVOX(ret_val)



    @classmethod
    def generate_ubc(cls, p1, p2, p3, p4, p5):
        """
        Generate a :class:`geosoft.gxapi.GXVOX` from a UBC File
        """
        ret_val = gxapi_cy.WrapVOX.generate_ubc(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4, p5._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_xyz(cls, p1, p2, p3, p4):
        """
        Generate a :class:`geosoft.gxapi.GXVOX` from an XYZ File
        """
        gxapi_cy.WrapVOX.generate_xyz(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4._wrapper)
        



    @classmethod
    def list_gocad_properties(cls, p1, p2):
        """
        List all the properties available in this GOCAD file.
        """
        gxapi_cy.WrapVOX.list_gocad_properties(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        




    def export_db(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Export a Voxel to a database

        **Note:**

        The database lines contain a slice of the voxel at a time.
        """
        self._wrapper.export_db(p2._wrapper, p3.encode(), p4, p5, p6, p7, p8)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer