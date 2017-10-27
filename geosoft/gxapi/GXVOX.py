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
    o sample a voxel at specific locations, use the `GXVOXE` class.
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
        A null (undefined) instance of `GXVOX`
        
        :returns: A null `GXVOX`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVOX` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVOX`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def calc_stats(self, st):
        """
        Calculate Statistics
        """
        self._wrapper.calc_stats(st._wrapper)
        



    @classmethod
    def create(cls, name):
        """
        Create a handle to an `GXVOX` object
        """
        ret_val = gxapi_cy.WrapVOX.create(GXContext._get_tls_geo(), name.encode())
        return GXVOX(ret_val)




    def create_pg(self):
        """
        Create a 3D `GXPG` from a `GXVOX` object
        """
        ret_val = self._wrapper.create_pg()
        return GXPG(ret_val)




    def create_type_pg(self, type):
        """
        Create a 3D `GXPG` from a `GXVOX` object with a specific Type
        """
        ret_val = self._wrapper.create_type_pg(type)
        return GXPG(ret_val)






    def dump(self, name):
        """
        Export all layers of this `GXVOX` in all directions.
        """
        self._wrapper.dump(name.encode())
        




    def export_img(self, name, dir):
        """
        Export all layers of this `GXVOX` into grid files.
        """
        self._wrapper.export_img(name.encode(), dir)
        




    def export_to_grids(self, name, dir, start, incr, num, cell_size, interp):
        """
        Export all layers of this `GXVOX` into grid files, with optional cell size.

        **Note:**

        If the cell size is not specified, then:
        1. If the cell sizes are uniform in a given direction, that size is used
        2. If the cell sizes are variable in a given direction, then the smallest size is used
        """
        self._wrapper.export_to_grids(name.encode(), dir, start, incr, num, cell_size, interp)
        



    @classmethod
    def export_xml(cls, voxel, crc, file):
        """
        Export a `GXVOX` to a compressed XML file
        """
        crc.value = gxapi_cy.WrapVOX.export_xml(GXContext._get_tls_geo(), voxel.encode(), crc.value, file.encode())
        




    def export_seg_y(self, output_segy_filename, sample_interval):
        """
        Export a voxel to a depth SEG-Y file
        """
        self._wrapper.export_seg_y(output_segy_filename.encode(), sample_interval)
        



    @classmethod
    def export_ji_gs_xml(cls, voxel, file):
        """
        Export a `GXVOX` to a compressed XML file. Verbose version.
        """
        gxapi_cy.WrapVOX.export_ji_gs_xml(GXContext._get_tls_geo(), voxel.encode(), file.encode())
        




    def export_xyz(self, xyz, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export a Voxel to an XYZ File
        """
        self._wrapper.export_xyz(xyz.encode(), dir, rev_x, rev_y, rev_z, dummies)
        




    def filter(self, filter, filter_file, n_passes, interpolate_dummies, output_vox):
        """
        Apply a 3D filter to a voxel.
        """
        self._wrapper.filter(filter, filter_file.encode(), n_passes, interpolate_dummies, output_vox.encode())
        



    @classmethod
    def generate_db(cls, voxel_file, db, symb):
        """
        Generate a `GXVOX` from a Database
        """
        gxapi_cy.WrapVOX.generate_db(GXContext._get_tls_geo(), voxel_file.encode(), db._wrapper, symb)
        



    @classmethod
    def generate_vector_voxel_from_db(cls, voxel_file, db, type, symb_x, symb_y, symb_z, inc, dec):
        """
        Generate a vector voxel `GXVOX` from a Database
        """
        gxapi_cy.WrapVOX.generate_vector_voxel_from_db(GXContext._get_tls_geo(), voxel_file.encode(), db._wrapper, type, symb_x, symb_y, symb_z, inc, dec)
        



    @classmethod
    def generate_pg(cls, name, pg, ox, oy, oz, cx, cy, cz, ipj, meta):
        """
        Generate a `GXVOX` from a 3D Pager
        """
        ret_val = gxapi_cy.WrapVOX.generate_pg(GXContext._get_tls_geo(), name.encode(), pg._wrapper, ox, oy, oz, cx, cy, cz, ipj._wrapper, meta._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_constant_value(cls, name, value, type, ox, oy, oz, cx, cy, cz, cell_count_x, cell_count_y, cell_count_z, ipj, meta):
        """
        Generate a `GXVOX` with a constant value
        """
        ret_val = gxapi_cy.WrapVOX.generate_constant_value(GXContext._get_tls_geo(), name.encode(), value, type, ox, oy, oz, cx, cy, cz, cell_count_x, cell_count_y, cell_count_z, ipj._wrapper, meta._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_pgvv(cls, name, pg, ox, oy, oz, cx, cy, cz, ipj, meta):
        """
        Generate a `GXVOX` from a 3D Pager, cells sizes passed in VVs.

        **Note:**

        The input cell size VVs' lengths must match the input `GXPG` dimensions.
        """
        ret_val = gxapi_cy.WrapVOX.generate_pgvv(GXContext._get_tls_geo(), name.encode(), pg._wrapper, ox, oy, oz, cx._wrapper, cy._wrapper, cz._wrapper, ipj._wrapper, meta._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_constant_value_vv(cls, name, value, type, ox, oy, oz, cx, cy, cz, ipj, meta):
        """
        Generate a `GXVOX` with a constant value, cells sizes passed in VVs.
        """
        ret_val = gxapi_cy.WrapVOX.generate_constant_value_vv(GXContext._get_tls_geo(), name.encode(), value, type, ox, oy, oz, cx._wrapper, cy._wrapper, cz._wrapper, ipj._wrapper, meta._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def init_generate_by_subset_pg(cls, data_type, nx, ny, nz):
        """
        Initialize the generate of a `GXVOX` from a series of 3D subset pagers

        **Note:**

        Call `init_generate_by_subset_pg` first, then add a series of subset PGs using `add_generate_by_subset_pg`, and finally
        serialize using `end_generate_by_subset_pg`
        """
        ret_val = gxapi_cy.WrapVOX.init_generate_by_subset_pg(GXContext._get_tls_geo(), data_type, nx, ny, nz)
        return GXVOX(ret_val)




    def add_generate_by_subset_pg(self, pg, dir, offset):
        """
        Add a subset 3D  pagers. These should be "slabs", 16 wide in the input direction, and the size of the
        full voxel in the other two directions.

        **Note:**

        See `init_generate_by_subset_pg` and `end_generate_by_subset_pg`.
        """
        self._wrapper.add_generate_by_subset_pg(pg._wrapper, dir, offset)
        




    def end_generate_by_subset_pg(self, name, ox, oy, oz, cx, cy, cz, ipj, meta):
        """
        Output the voxel, after adding all the subset PGs.

        **Note:**

        You must begin by calling `init_generate_by_subset_pg` and add data using `add_generate_by_subset_pg`.
        """
        self._wrapper.end_generate_by_subset_pg(name.encode(), ox, oy, oz, cx, cy, cz, ipj._wrapper, meta._wrapper)
        




    def get_area(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the area of the voxel.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._wrapper.get_area(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_gocad_location(self, origin_x, origin_y, origin_z, vect_xx, vect_xy, vect_xz, vect_yx, vect_yy, vect_yz, vect_zx, vect_zy, vect_zz):
        """
        Get the location of a voxel with origin and scaled xyz vectors for use with GOCAD.

        **Note:**

        This is used for GOCAD voxel calculations, and begins with the
        origin at (0,0,0), not the actual location of the corner point.
        """
        origin_x.value, origin_y.value, origin_z.value, vect_xx.value, vect_xy.value, vect_xz.value, vect_yx.value, vect_yy.value, vect_yz.value, vect_zx.value, vect_zy.value, vect_zz.value = self._wrapper.get_gocad_location(origin_x.value, origin_y.value, origin_z.value, vect_xx.value, vect_xy.value, vect_xz.value, vect_yx.value, vect_yy.value, vect_yz.value, vect_zx.value, vect_zy.value, vect_zz.value)
        




    def get_grid_section_cell_sizes(self, az, cell_size_x, cell_size_y):
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
        cell_size_x.value, cell_size_y.value = self._wrapper.get_grid_section_cell_sizes(az, cell_size_x.value, cell_size_y.value)
        




    def get_info(self, type, array, x, y, z):
        """
        Get information about a voxel.
        """
        type.value, array.value, x.value, y.value, z.value = self._wrapper.get_info(type.value, array.value, x.value, y.value, z.value)
        




    def get_ipj(self, ipj):
        """
        Get the projection of the voxel.
        """
        self._wrapper.get_ipj(ipj._wrapper)
        




    def get_limits(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the range of indices with non-dummy data.

        **Note:**

        Find the non-dummy volume of a `GXVOX` object. If the voxel is all dummies,
        returns `iMAX` for the minima, and `iMIN` for the maxima.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._wrapper.get_limits(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_limits_xyz(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the range in true XYZ of non-dummy data.

        **Note:**

        Find the non-dummy volume of a `GXVOX` in true (X, Y, Z). This method
        works for voxels which are rotated or oriented in 3D, and returns
        the true min and max X, Y and Z limits in the data.
        The bounds are the bounds for the voxel
        center points. If the voxel is all dummies,
        returns `rMAX` for the minima, and `rMIN` for the maxima.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._wrapper.get_limits_xyz(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_location(self, origin_x, origin_y, origin_z, vv_x, vv_y, vv_z):
        """
        Get Location information
        """
        origin_x.value, origin_y.value, origin_z.value = self._wrapper.get_location(origin_x.value, origin_y.value, origin_z.value, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        




    def get_location_points(self, vv_x, vv_y, vv_z):
        """
        Get the computed location points.
        """
        self._wrapper.get_location_points(vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        




    def get_meta(self, meta):
        """
        Get the metadata of a voxel.
        """
        self._wrapper.get_meta(meta._wrapper)
        




    def get_double_location(self, origin_x, origin_y, origin_z, vect_xx, vect_xy, vect_xz, vect_yx, vect_yy, vect_yz, vect_zx, vect_zy, vect_zz):
        """
        Get the location of a voxel with origin and scaled xyz vectors
        """
        origin_x.value, origin_y.value, origin_z.value, vect_xx.value, vect_xy.value, vect_xz.value, vect_yx.value, vect_yy.value, vect_yz.value, vect_zx.value, vect_zy.value, vect_zz.value = self._wrapper.get_double_location(origin_x.value, origin_y.value, origin_z.value, vect_xx.value, vect_xy.value, vect_xz.value, vect_yx.value, vect_yy.value, vect_yz.value, vect_zx.value, vect_zy.value, vect_zz.value)
        




    def get_simple_location(self, origin_x, origin_y, origin_z, cell_x, cell_y, cell_z):
        """
        Get Simple Location information
        """
        origin_x.value, origin_y.value, origin_z.value, cell_x.value, cell_y.value, cell_z.value = self._wrapper.get_simple_location(origin_x.value, origin_y.value, origin_z.value, cell_x.value, cell_y.value, cell_z.value)
        




    def get_stats(self):
        """
        Get precomputed statistics on this object.
        """
        ret_val = self._wrapper.get_stats()
        return GXST(ret_val)




    def get_tpat(self, tpat):
        """
        Get a copy of a thematic voxel's `GXTPAT` object.

        **Note:**

        Each row in the `GXTPAT` object corresponds to a stored index
        value in the thematic voxel. The `GXTPAT` should NOT be modified
        by the addition or deletion of items, if it is to be
        restored into the `GXVOX` object, but the CODE, LABEL, DESCRIPTION
        or COLOR info can be changed.
        The `GXTPAT` object is stored inside the `GXVOX` `GXMETA` object.
        """
        self._wrapper.get_tpat(tpat._wrapper)
        



    @classmethod
    def grid_points(cls, name, error, cell_size, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, vv_x, vv_y, vv_z, vv_d, ipj):
        """
        Grid a `GXVOX` from point `GXVV`'s.
        """
        ret_val = gxapi_cy.WrapVOX.grid_points(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_d._wrapper, ipj._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def grid_points_z(cls, name, error, cell_size, cell_size_z, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, vv_x, vv_y, vv_z, vv_d, ipj):
        """
        Grid a `GXVOX` from point `GXVV`'s (using variable Z's)
        """
        ret_val = gxapi_cy.WrapVOX.grid_points_z(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, cell_size_z.encode(), var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_d._wrapper, ipj._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def grid_points_z_ex(cls, name, error, cell_size, cell_size_z, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, strike, dip, plunge, along_strike_weight, down_dip_weight, type, vv_x, vv_y, vv_z, vv_d, ipj):
        """
        Grid a `GXVOX` from point `GXVV`'s (using variable Z's)
        """
        ret_val, slope.value, range.value, sill.value = gxapi_cy.WrapVOX.grid_points_z_ex(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, cell_size_z.encode(), var_only, min_radius, max_radius, min_points, max_points, model, power, slope.value, range.value, nugget, sill.value, strike, dip, plunge, along_strike_weight, down_dip_weight, type, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_d._wrapper, ipj._wrapper)
        return GXVOX(ret_val)




    def can_append_to(self, surface_file):
        """
        Check if this voxel can append to a surface file.
        """
        ret_val = self._wrapper.can_append_to(surface_file.encode())
        return ret_val




    def get_cell_size_strings(self, loc_x, loc_y, loc_z, scale_x, scale_y, scale_z):
        """
        Get the Location Strings
        """
        loc_x.value, loc_y.value, loc_z.value = self._wrapper.get_cell_size_strings(loc_x.value.encode(), loc_y.value.encode(), loc_z.value.encode(), scale_x, scale_y, scale_z)
        




    def is_thematic(self):
        """
        Is this a thematic voxel?

        **Note:**

        A thematic voxel is one where the stored integer values
        represent indices into an internally stored `GXTPAT` object.
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




    def set_cell_size_strings(self, loc_x, loc_y, loc_z):
        """
        Set the Location Strings
        """
        ret_val = self._wrapper.set_cell_size_strings(loc_x.encode(), loc_y.encode(), loc_z.encode())
        return ret_val



    @classmethod
    def log_grid_points_z_ex(cls, name, error, cell_size, cell_size_z, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, strike, dip, plunge, along_strike_weight, down_dip_weight, log_opt, min_log, type, vv_x, vv_y, vv_z, vv_d, ipj):
        """
        Log grid a `GXVOX` from point `GXVV`'s (using variable Z's)
        """
        ret_val, slope.value, range.value, sill.value = gxapi_cy.WrapVOX.log_grid_points_z_ex(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, cell_size_z.encode(), var_only, min_radius, max_radius, min_points, max_points, model, power, slope.value, range.value, nugget, sill.value, strike, dip, plunge, along_strike_weight, down_dip_weight, log_opt, min_log, type, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_d._wrapper, ipj._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def krig(cls, name, cell_size, type, vv_x, vv_y, vv_z, vv_d, ipj, reg):
        """
        A more compact and extensible form of `log_grid_points_z_ex`.

        **Note:**

        Optional Parameters.
        
        If these values are not set in the `GXREG`, then default parameters will be used.
        
        ERROR_VOXEL:		Name of error `GXVOX` ("" for none)
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
        MAX_Z:				Maximum Z (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)A more compact and extensible form of `log_grid_points_z_ex`. Only the most
        basic parameters are entered directly. Optional parameters are passed via a `GXREG` object.
        """
        ret_val = gxapi_cy.WrapVOX.krig(GXContext._get_tls_geo(), name.encode(), cell_size, type, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_d._wrapper, ipj._wrapper, reg._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def math(cls, master, mastervar, output, outvar, formula, lst):
        """
        Produces a new voxes using a formula on existing voxels/Grids

        **Note:**

        The input voxels must all be of the same type.
        """
        ret_val = gxapi_cy.WrapVOX.math(GXContext._get_tls_geo(), master.encode(), mastervar.encode(), output.encode(), outvar.encode(), formula.encode(), lst._wrapper)
        return GXVOX(ret_val)




    def merge(self, vox2, reg, output_vox):
        """
        Merge two Voxels.
        """
        self._wrapper.merge(vox2._wrapper, reg._wrapper, output_vox.encode())
        



    @classmethod
    def nearest_neighbour_grid(cls, name, cell_size, max_radius, type, vv_x, vv_y, vv_z, vv_d, ipj):
        """
        Grid a `GXVOX` from point `GXVV`'s using the Nearest Neighbours method.
        """
        ret_val = gxapi_cy.WrapVOX.nearest_neighbour_grid(GXContext._get_tls_geo(), name.encode(), cell_size, max_radius, type, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_d._wrapper, ipj._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def compute_cell_size(cls, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Compute the Cell size based on specific Area
        """
        ret_val = gxapi_cy.WrapVOX.compute_cell_size(GXContext._get_tls_geo(), min_x, min_y, min_z, max_x, max_y, max_z)
        return ret_val




    def re_grid(self, vox_to_regrid, reg, output_vox):
        """
        Regrid a Voxel.
        """
        self._wrapper.re_grid(vox_to_regrid._wrapper, reg._wrapper, output_vox.encode())
        




    def resample_pg(self, ipj, orig_x, orig_y, orig_z, spacing_x, spacing_y, spacing_z, size_x, size_y, size_z, min_z, max_z, interp):
        """
        Resample a voxel over an input volume to a `GXPG`.

        **Note:**

        Creates and dummies a `GXPG` object based on the input
        dimensions, then resamples the voxel to the pager
        at the locations determined by input projection, origin and spacings.
        """
        ret_val = self._wrapper.resample_pg(ipj._wrapper, orig_x, orig_y, orig_z, spacing_x, spacing_y, spacing_z, size_x, size_y, size_z, min_z, max_z, interp)
        return GXPG(ret_val)




    def rescale_cell_sizes(self, scale):
        """
        Multiply all cell sizes by a fixed factor.

        **Note:**

        This is useful, for instance for converting sizes in one
        unit to sizes in another unit if changing the projection
        and the projection's unit changes, since the voxel inherits
        its projection's units.
        """
        self._wrapper.rescale_cell_sizes(scale)
        




    def sample_cdi(self, db, line, x_ch, y_ch, elev_ch, negative_depths_down, topo_ch, mode, out_ch):
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
        self._wrapper.sample_cdi(db._wrapper, line, x_ch, y_ch, elev_ch, negative_depths_down, topo_ch, mode, out_ch.encode())
        




    def sample_cdi_to_topography(self, db, line, x_ch, y_ch, zvv, mode, out_ch, topo_ch):
        """
        Sample a voxel at fixed elevations along a path in a CDI database, and output them to an array channel, deleting leading dummy values, and
        writing the elevation of the first non-dummy item to a topography channel.
        """
        self._wrapper.sample_cdi_to_topography(db._wrapper, line, x_ch, y_ch, zvv._wrapper, mode, out_ch.encode(), topo_ch.encode())
        




    def sample_vv(self, xvv, yvv, zvv, interp, dvv):
        """
        Sample a voxel at multiple locations.

        **Note:**

        Sample at voxel at XYZ locations input in VVs. Values returned in a `GXVV`.
        """
        self._wrapper.sample_vv(xvv._wrapper, yvv._wrapper, zvv._wrapper, interp, dvv._wrapper)
        




    def set_ipj(self, ipj):
        """
        Set the projection of the voxel.
        """
        self._wrapper.set_ipj(ipj._wrapper)
        




    def set_location(self, origin_x, origin_y, origin_z, vv_x, vv_y, vv_z):
        """
        Set Location information
        """
        self._wrapper.set_location(origin_x, origin_y, origin_z, vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        




    def set_meta(self, meta):
        """
        Set the metadata of a voxel.
        """
        self._wrapper.set_meta(meta._wrapper)
        




    def set_origin(self, origin, origin_x, origin_y, origin_z):
        """
        Set the Voxel Origin
        """
        self._wrapper.set_origin(origin, origin_x, origin_y, origin_z)
        




    def set_simple_location(self, origin_x, origin_y, origin_z, cell_x, cell_y, cell_z):
        """
        Set Simple Location information
        """
        self._wrapper.set_simple_location(origin_x, origin_y, origin_z, cell_x, cell_y, cell_z)
        




    def set_tpat(self, tpat):
        """
        Set a thematic voxel's `GXTPAT` object.

        **Note:**

        Each row in the `GXTPAT` object corresponds to a stored index
        value in the thematic voxel. The `GXTPAT` should NOT be modified
        by the addition or deletion of items, if it is to be
        restored into the `GXVOX` object, but the CODE, LABEL, DESCRIPTION
        or COLOR info can be changed.
        The `GXTPAT` object is stored inside the `GXVOX` `GXMETA` object.
        """
        self._wrapper.set_tpat(tpat._wrapper)
        




    def slice_ipj(self, name, ipj, mode, orig_x, orig_y, cell_size_x, cell_size_y, size_x, size_y):
        """
        Extract a slice of a voxel based on an `GXIPJ`
        """
        self._wrapper.slice_ipj(name.encode(), ipj._wrapper, mode, orig_x, orig_y, cell_size_x, cell_size_y, size_x, size_y)
        




    def slice_multi_layer_ipj(self, name, ipj, mode, orig_x, orig_y, cell_size_x, cell_size_y, size_x, size_y, layers, start_elev, elev_inc):
        """
        Extract multiple slices of a voxel based on an `GXIPJ`
        """
        self._wrapper.slice_multi_layer_ipj(name.encode(), ipj._wrapper, mode, orig_x, orig_y, cell_size_x, cell_size_y, size_x, size_y, layers, start_elev, elev_inc)
        




    def subset_to_double_extents(self, output_vox):
        """
        Subset a `GXVOX` to real extents.
        """
        self._wrapper.subset_to_double_extents(output_vox.encode())
        



    @classmethod
    def sync(cls, name):
        """
        Syncronize the Metadata for this Voxel
        """
        gxapi_cy.WrapVOX.sync(GXContext._get_tls_geo(), name.encode())
        




    def window_ply(self, pply, mask, min_z, max_z, output_vox, clip_dummies):
        """
        Window a `GXVOX` to a `GXPLY` file and Z.

        **Note:**

        The voxel is windowed horizontally to the input `GXPLY` file.
        Optionally, it will be windowed to the input Z range as well.
        The output can be clipped to the non-dummied cells.
        """
        self._wrapper.window_ply(pply._wrapper, mask, min_z, max_z, output_vox.encode(), clip_dummies)
        




    def window_xyz(self, min_x, min_y, min_z, max_x, max_y, max_z, output_vox, clip_dummies):
        """
        Window a `GXVOX` to ranges in X, Y and Z.

        **Note:**

        The six minima and maxima are optional.
        The output can be clipped to the non-dummied cells.
        """
        self._wrapper.window_xyz(min_x, min_y, min_z, max_x, max_y, max_z, output_vox.encode(), clip_dummies)
        




    def write_xml(self, file):
        """
        Export the `GXVOX` to XML
        """
        self._wrapper.write_xml(file.encode())
        




    def convert_numeric_to_thematic(self, vv_translate, output_vox):
        """
        Convert numeric voxel to thematic (lithology) voxel
        """
        self._wrapper.convert_numeric_to_thematic(vv_translate._wrapper, output_vox.encode())
        




    def convert_thematic_to_numeric(self, vv_translate, output_vox):
        """
        Convert thematic (lithology) voxel to numeric voxel
        """
        self._wrapper.convert_thematic_to_numeric(vv_translate._wrapper, output_vox.encode())
        




    def convert_velocity_to_density(self, input_scaling_factor, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename):
        """
        Produces a density voxel using the velocity values in this voxel.
        """
        self._wrapper.convert_velocity_to_density(input_scaling_factor, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename.encode())
        




    def convert_velocity_in_range_to_density(self, input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename):
        """
        Produces a density voxel using the velocity values in this voxel, as long as the velocity values are in range.
        """
        self._wrapper.convert_velocity_in_range_to_density(input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename.encode())
        




    def convert_density_to_velocity(self, input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename):
        """
        Produces a velocity voxel using the density values in this voxel.
        """
        self._wrapper.convert_density_to_velocity(input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename.encode())
        




    def invert_z(self, output_voxel_filename):
        """
        Convert an inverted voxel to normal orientation
        """
        self._wrapper.invert_z(output_voxel_filename.encode())
        



    @classmethod
    def dw_grid_db(cls, voxel, db, x, y, z, data, reg):
        """
        `dw_grid_db`     Inverse-distance weighting gridding method, `GXDB` version, 3D.

        **Note:**

        3D cells take on the averaged values within a search radius, weighted inversely by distance.
        
        Weighting can be controlled using the power and slope properties;
        
        weighting = 1 / (distance^wtpower + 1/slope) where distance is in
        units of grid cells (X dimenstion). Default is 0.0,
        
        If the blanking distance is set, all cells whose center point is not within the blanking distance of
        at least one data point are set to dummy.
        
        `GXREG` Parameters:
        
        X0, Y0, Z0, DX, DY, DZ: Voxel origin, and cell sizes (required)
        WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters
        SEARCH_RADIUS: Distance weighting limit (default = 4 * CUBE_ROOT(DX*DY*DZ))
        BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 * CUBE_ROOT(DX*DY*DZ))
        LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?
        LOG_BASE: One of `VV_LOG_BASE_10` (default) or `VV_LOG_BASE_E`
        LOG_NEGATIVE: One of `VV_LOG_NEGATIVE_NO` (default) or `VV_LOG_NEGATIVE_YES`
        """
        gxapi_cy.WrapVOX.dw_grid_db(GXContext._get_tls_geo(), voxel.encode(), db._wrapper, x, y, z, data, reg._wrapper)
        



    @classmethod
    def tin_grid_db(cls, voxel, db, x, y, z, data, method, z_cell, reg):
        """
        `tin_grid_db`   `GXTIN`-Gridding, `GXDB` version, 3D.

        **Note:**

        Designed for data in array channels position vertically at single XY locations.
        Creates a `GXTIN` using the XY locations and uses the coefficients for the top layer on
        each layer below to make it efficient.
        
        `GXREG` Parameters:
        
        X0, Y0, Z0, DX, DY, DZ: Voxel origin, and cell sizes (required)
        NX, NY, NZ: Voxel dimensions.
        DZ and NZ are used only if the input cell sizes `GXVV` is of zero length.
        """
        gxapi_cy.WrapVOX.tin_grid_db(GXContext._get_tls_geo(), voxel.encode(), db._wrapper, x, y, z, data, method, z_cell._wrapper, reg._wrapper)
        



    @classmethod
    def get_multi_voxset_guid(cls, voxel_file, p_uuid_string):
        """
        Get the UUID
        """
        p_uuid_string.value = gxapi_cy.WrapVOX.get_multi_voxset_guid(GXContext._get_tls_geo(), voxel_file.encode(), p_uuid_string.value.encode())
        



    @classmethod
    def generate_gocad(cls, name, header, property, ipj):
        """
        Generate a `GXVOX` from a GOCAD File
        """
        ret_val = gxapi_cy.WrapVOX.generate_gocad(GXContext._get_tls_geo(), name.encode(), header.encode(), property.encode(), ipj._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_oriented_gocad(cls, name, header, property, ipj, orientation):
        """
        Generate a `GXVOX` from a GOCAD File

        **Note:**

        Allows the Orientation flag to be specified.
        """
        ret_val = gxapi_cy.WrapVOX.generate_oriented_gocad(GXContext._get_tls_geo(), name.encode(), header.encode(), property.encode(), ipj._wrapper, orientation)
        return GXVOX(ret_val)



    @classmethod
    def generate_ubc(cls, name, mesh, mod, dummy, ipj):
        """
        Generate a `GXVOX` from a UBC File
        """
        ret_val = gxapi_cy.WrapVOX.generate_ubc(GXContext._get_tls_geo(), name.encode(), mesh.encode(), mod.encode(), dummy, ipj._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_xyz(cls, name, ra, type, ipj):
        """
        Generate a `GXVOX` from an XYZ File
        """
        gxapi_cy.WrapVOX.generate_xyz(GXContext._get_tls_geo(), name.encode(), ra._wrapper, type, ipj._wrapper)
        



    @classmethod
    def list_gocad_properties(cls, header, lst):
        """
        List all the properties available in this GOCAD file.
        """
        gxapi_cy.WrapVOX.list_gocad_properties(GXContext._get_tls_geo(), header.encode(), lst._wrapper)
        




    def export_db(self, db, chan, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export a Voxel to a database

        **Note:**

        The database lines contain a slice of the voxel at a time.
        """
        self._wrapper.export_db(db._wrapper, chan.encode(), dir, rev_x, rev_y, rev_z, dummies)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer