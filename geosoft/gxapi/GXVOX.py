### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
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
class GXVOX(gxapi_cy.WrapVOX):
    """
    GXVOX class.

    High Performance 3D Grid. Designed for accessing
    3D grids quickly using slices. It designed arround
    non-uniform multi-resolution  compressed storage.
    To sample a voxel at specific locations, use `GXVOXE <geosoft.gxapi.GXVOXE>`.
    """

    def __init__(self, handle=0):
        super(GXVOX, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVOX <geosoft.gxapi.GXVOX>`
        
        :returns: A null `GXVOX <geosoft.gxapi.GXVOX>`
        :rtype:   GXVOX
        """
        return GXVOX()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def calc_stats(self, st):
        """
        Calculate Statistics
        
        :param st:   `GXST <geosoft.gxapi.GXST>` Object
        :type  st:   GXST

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._calc_stats(st)
        



    @classmethod
    def create(cls, name):
        """
        Create a handle to an `GXVOX <geosoft.gxapi.GXVOX>` object
        
        :param name:  File Name
        :type  name:  str

        :returns:     `GXVOX <geosoft.gxapi.GXVOX>` handle, terminates if creation fails
        :rtype:       GXVOX

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapVOX._create(GXContext._get_tls_geo(), name.encode())
        return GXVOX(ret_val)




    def create_pg(self):
        """
        Create a 3D `GXPG <geosoft.gxapi.GXPG>` from a `GXVOX <geosoft.gxapi.GXVOX>` object
        

        :returns:    `GXPG <geosoft.gxapi.GXPG>` Object
        :rtype:      GXPG

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._create_pg()
        return GXPG(ret_val)




    def create_type_pg(self, type):
        """
        Create a 3D `GXPG <geosoft.gxapi.GXPG>` from a `GXVOX <geosoft.gxapi.GXVOX>` object with a specific Type
        
        :param type:  :ref:`GS_TYPES`
        :type  type:  int

        :returns:     `GXPG <geosoft.gxapi.GXPG>` Object
        :rtype:       GXPG

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._create_type_pg(type)
        return GXPG(ret_val)






    def dump(self, name):
        """
        Export all layers of this `GXVOX <geosoft.gxapi.GXVOX>` in all directions.
        
        :param name:  Name of grids (each layers adds _Dir_Z to the name)
        :type  name:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._dump(name.encode())
        




    def export_img(self, name, dir):
        """
        Export all layers of this `GXVOX <geosoft.gxapi.GXVOX>` into grid files.
        
        :param name:  Name of grids (each layers adds _Number to the name)
        :param dir:   :ref:`VOX_DIR`
        :type  name:  str
        :type  dir:   int

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_img(name.encode(), dir)
        




    def export_to_grids(self, name, dir, start, incr, num, cell_size, interp):
        """
        Export all layers of this `GXVOX <geosoft.gxapi.GXVOX>` into grid files, with optional cell size.
        
        :param name:       Name of grids (each layers adds _Number to the name)
        :param dir:        :ref:`VOX_DIR`
        :param start:      Starting index
        :param incr:       Increment in index
        :param num:        Total number of grids (-1 or `iDUMMY <geosoft.gxapi.iDUMMY>` for all)
        :param cell_size:  Cell size (can be `GS_R8DM <geosoft.gxapi.GS_R8DM>`)
        :param interp:     :ref:`VOX_SLICE_MODE`
        :type  name:       str
        :type  dir:        int
        :type  start:      int
        :type  incr:       int
        :type  num:        int
        :type  cell_size:  float
        :type  interp:     int

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the cell size is not specified, then:
        1. If the cell sizes are uniform in a given direction, that size is used
        2. If the cell sizes are variable in a given direction, then the smallest size is used
        """
        self._export_to_grids(name.encode(), dir, start, incr, num, cell_size, interp)
        



    @classmethod
    def export_xml(cls, voxel, crc, file):
        """
        Export a `GXVOX <geosoft.gxapi.GXVOX>` to a compressed XML file
        
        :param voxel:  Voxel file name
        :param crc:    CRC returned - not implemented - always returns 0.
        :param file:   Output XML file
        :type  voxel:  str
        :type  crc:    int_ref
        :type  file:   str

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        crc.value = gxapi_cy.WrapVOX._export_xml(GXContext._get_tls_geo(), voxel.encode(), crc.value, file.encode())
        




    def export_seg_y(self, output_segy_filename, sample_interval):
        """
        Export a voxel to a depth SEG-Y file
        
        :param output_segy_filename:  SEG-Y filename to create
        :param sample_interval:       Sampling interval (can be `GS_R8DM <geosoft.gxapi.GS_R8DM>` if input voxel has constant Z cell size)
        :type  output_segy_filename:  str
        :type  sample_interval:       float

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_seg_y(output_segy_filename.encode(), sample_interval)
        



    @classmethod
    def export_ji_gs_xml(cls, voxel, file):
        """
        Export a `GXVOX <geosoft.gxapi.GXVOX>` to a compressed XML file. Verbose version.
        
        :param voxel:  Voxel file name
        :param file:   Output XML file
        :type  voxel:  str
        :type  file:   str

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapVOX._export_ji_gs_xml(GXContext._get_tls_geo(), voxel.encode(), file.encode())
        




    def export_xyz(self, xyz, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export a Voxel to an XYZ File
        
        :param xyz:      File Name
        :param dir:      :ref:`VOX_DIRECTION`
        :param rev_x:    Reverse X ? (0/1)
        :param rev_y:    Reverse Y ? (0/1)
        :param rev_z:    Reverse Z ? (0/1)
        :param dummies:  Write Dummies? (0/1)
        :type  xyz:      str
        :type  dir:      int
        :type  rev_x:    int
        :type  rev_y:    int
        :type  rev_z:    int
        :type  dummies:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_xyz(xyz.encode(), dir, rev_x, rev_y, rev_z, dummies)
        




    def filter(self, filter, filter_file, n_passes, interpolate_dummies, output_vox):
        """
        Apply a 3D filter to a voxel.
        
        :param filter:               :ref:`VOX_FILTER3D`
        :param filter_file:          Filter file, if filter is `VOX_FILTER3D_FILE <geosoft.gxapi.VOX_FILTER3D_FILE>`
        :param n_passes:             Number of filter passes
        :param interpolate_dummies:  (1: interpolate dummies)
        :param output_vox:           Output voxel file name.
        :type  filter:               int
        :type  filter_file:          str
        :type  n_passes:             int
        :type  interpolate_dummies:  int
        :type  output_vox:           str

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._filter(filter, filter_file.encode(), n_passes, interpolate_dummies, output_vox.encode())
        



    @classmethod
    def generate_db(cls, voxel_file, db, symb):
        """
        Generate a `GXVOX <geosoft.gxapi.GXVOX>` from a Database
        
        :param voxel_file:  Voxel Name
        :param db:          `GXDB <geosoft.gxapi.GXDB>` To import from
        :param symb:        Symbol to import data from
        :type  voxel_file:  str
        :type  db:          GXDB
        :type  symb:        int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapVOX._generate_db(GXContext._get_tls_geo(), voxel_file.encode(), db, symb)
        



    @classmethod
    def generate_vector_voxel_from_db(cls, voxel_file, db, type, symb_x, symb_y, symb_z, inc, dec):
        """
        Generate a vector voxel `GXVOX <geosoft.gxapi.GXVOX>` from a Database
        
        :param voxel_file:  Voxel Name
        :param db:          `GXDB <geosoft.gxapi.GXDB>` To import from
        :param type:        VOX_VECTORVOX_IMPORTImport XYZ, UVW or Amplitude/Inclination/Declination channels
        :param symb_x:      Symbol to import X, U or Amplitude data from
        :param symb_y:      Symbol to import Y, V or Inclination data from
        :param symb_z:      Symbol to import Z, W or Declination data from
        :param inc:         Inclination value for `VOX_VECTORVOX_UVW <geosoft.gxapi.VOX_VECTORVOX_UVW>` (-90° to 90°)
        :param dec:         Declination value for `VOX_VECTORVOX_UVW <geosoft.gxapi.VOX_VECTORVOX_UVW>` (-180° to 180°)
        :type  voxel_file:  str
        :type  db:          GXDB
        :type  type:        int
        :type  symb_x:      int
        :type  symb_y:      int
        :type  symb_z:      int
        :type  inc:         float
        :type  dec:         float

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapVOX._generate_vector_voxel_from_db(GXContext._get_tls_geo(), voxel_file.encode(), db, type, symb_x, symb_y, symb_z, inc, dec)
        



    @classmethod
    def generate_pg(cls, name, pg, ox, oy, oz, cx, cy, cz, ipj, meta):
        """
        Generate a `GXVOX <geosoft.gxapi.GXVOX>` from a 3D Pager
        
        :param name:  Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param pg:    Pager with the Voxel Data
        :param ox:    Origin X
        :param oy:    Origin Y
        :param oz:    Origin Z
        :param cx:    Cell Size X
        :param cy:    Cell Size Y
        :param cz:    Cell Size Z
        :param ipj:   Projection
        :param meta:  Metadata
        :type  name:  str
        :type  pg:    GXPG
        :type  ox:    float
        :type  oy:    float
        :type  oz:    float
        :type  cx:    float
        :type  cy:    float
        :type  cz:    float
        :type  ipj:   GXIPJ
        :type  meta:  GXMETA

        :returns:     `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:       GXVOX

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapVOX._generate_pg(GXContext._get_tls_geo(), name.encode(), pg, ox, oy, oz, cx, cy, cz, ipj, meta)
        return GXVOX(ret_val)



    @classmethod
    def generate_pgvv(cls, name, pg, ox, oy, oz, cx, cy, cz, ipj, meta):
        """
        Generate a `GXVOX <geosoft.gxapi.GXVOX>` from a 3D Pager, cells sizes passed in VVs.
        
        :param name:  Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param pg:    Pager with the Voxel Data
        :param ox:    Origin X
        :param oy:    Origin Y
        :param oz:    Origin Z
        :param cx:    Cell Sizes X
        :param cy:    Cell Sizes Y
        :param cz:    Cell Sizes Z
        :param ipj:   Projection
        :param meta:  Metadata
        :type  name:  str
        :type  pg:    GXPG
        :type  ox:    float
        :type  oy:    float
        :type  oz:    float
        :type  cx:    GXVV
        :type  cy:    GXVV
        :type  cz:    GXVV
        :type  ipj:   GXIPJ
        :type  meta:  GXMETA

        :returns:     `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:       GXVOX

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The input cell size VVs' lengths must match the input `GXPG <geosoft.gxapi.GXPG>` dimensions.
        """
        ret_val = gxapi_cy.WrapVOX._generate_pgvv(GXContext._get_tls_geo(), name.encode(), pg, ox, oy, oz, cx, cy, cz, ipj, meta)
        return GXVOX(ret_val)



    @classmethod
    def init_generate_by_subset_pg(cls, data_type, nx, ny, nz):
        """
        Initialize the generate of a `GXVOX <geosoft.gxapi.GXVOX>` from a series of 3D subset pagers
        
        :param data_type:  :ref:`GS_TYPES`
        :param nx:         Points in X
        :param ny:         Points in Y
        :param nz:         Points in Z
        :type  data_type:  int
        :type  nx:         int
        :type  ny:         int
        :type  nz:         int

        :returns:          `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:            GXVOX

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Call `init_generate_by_subset_pg <geosoft.gxapi.GXVOX.init_generate_by_subset_pg>` first, then add a series of subset PGs using `add_generate_by_subset_pg <geosoft.gxapi.GXVOX.add_generate_by_subset_pg>`, and finally
        serialize using `end_generate_by_subset_pg <geosoft.gxapi.GXVOX.end_generate_by_subset_pg>`
        """
        ret_val = gxapi_cy.WrapVOX._init_generate_by_subset_pg(GXContext._get_tls_geo(), data_type, nx, ny, nz)
        return GXVOX(ret_val)




    def add_generate_by_subset_pg(self, pg, dir, offset):
        """
        Add a subset 3D  pagers. These should be "slabs", 16 wide in the input direction, and the size of the
        full voxel in the other two directions.
        
        :param pg:      Subset pager with the Voxel Data
        :param dir:     Subset orientation - the "16" (thin) dimension is in the other axis.:ref:`VOX_DIR`
        :param offset:  Offset of the subset `GXPG <geosoft.gxapi.GXPG>` corner, along the "thin" dimension.
        :type  pg:      GXPG
        :type  dir:     int
        :type  offset:  int

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `init_generate_by_subset_pg <geosoft.gxapi.GXVOX.init_generate_by_subset_pg>` and `end_generate_by_subset_pg <geosoft.gxapi.GXVOX.end_generate_by_subset_pg>`.
        """
        self._add_generate_by_subset_pg(pg, dir, offset)
        




    def end_generate_by_subset_pg(self, name, ox, oy, oz, cx, cy, cz, ipj, meta):
        """
        Output the voxel, after adding all the subset PGs.
        
        :param name:  Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param ox:    Origin X
        :param oy:    Origin Y
        :param oz:    Origin Z
        :param cx:    Cell Size X
        :param cy:    Cell Size Y
        :param cz:    Cell Size Z
        :param ipj:   Projection
        :param meta:  Metadata
        :type  name:  str
        :type  ox:    float
        :type  oy:    float
        :type  oz:    float
        :type  cx:    float
        :type  cy:    float
        :type  cz:    float
        :type  ipj:   GXIPJ
        :type  meta:  GXMETA

        .. versionadded:: 8.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** You must begin by calling `init_generate_by_subset_pg <geosoft.gxapi.GXVOX.init_generate_by_subset_pg>` and add data using `add_generate_by_subset_pg <geosoft.gxapi.GXVOX.add_generate_by_subset_pg>`.
        """
        self._end_generate_by_subset_pg(name.encode(), ox, oy, oz, cx, cy, cz, ipj, meta)
        




    def get_area(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the area of the voxel.
        
        :param min_x:  Min X
        :param min_y:  Min Y
        :param min_z:  Min Z
        :param max_x:  Max X
        :param max_y:  Max Y
        :param max_z:  Max Z
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  min_z:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref
        :type  max_z:  float_ref

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._get_area(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_gocad_location(self, origin_x, origin_y, origin_z, vect_xx, vect_xy, vect_xz, vect_yx, vect_yy, vect_yz, vect_zx, vect_zy, vect_zz):
        """
        Get the location of a voxel with origin and scaled xyz vectors for use with GOCAD.
        
        :param origin_x:  Origin X
        :param origin_y:  Origin Y
        :param origin_z:  Origin Z
        :param vect_xx:   VectX X
        :param vect_xy:   VectX Y
        :param vect_xz:   VectX Z
        :param vect_yx:   VectY X
        :param vect_yy:   VectY Y
        :param vect_yz:   VectY Z
        :param vect_zx:   VectZ X
        :param vect_zy:   VectZ Y
        :param vect_zz:   VectZ Z
        :type  origin_x:  float_ref
        :type  origin_y:  float_ref
        :type  origin_z:  float_ref
        :type  vect_xx:   float_ref
        :type  vect_xy:   float_ref
        :type  vect_xz:   float_ref
        :type  vect_yx:   float_ref
        :type  vect_yy:   float_ref
        :type  vect_yz:   float_ref
        :type  vect_zx:   float_ref
        :type  vect_zy:   float_ref
        :type  vect_zz:   float_ref

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is used for GOCAD voxel calculations, and begins with the
        origin at (0,0,0), not the actual location of the corner point.
        """
        origin_x.value, origin_y.value, origin_z.value, vect_xx.value, vect_xy.value, vect_xz.value, vect_yx.value, vect_yy.value, vect_yz.value, vect_zx.value, vect_zy.value, vect_zz.value = self._get_gocad_location(origin_x.value, origin_y.value, origin_z.value, vect_xx.value, vect_xy.value, vect_xz.value, vect_yx.value, vect_yy.value, vect_yz.value, vect_zx.value, vect_zy.value, vect_zz.value)
        




    def get_grid_section_cell_sizes(self, az, cell_size_x, cell_size_y):
        """
        Get default cell sizes in X and Y for a section grid.
        
        :param az:           Input section azimuth (degrees CCW from North)
        :param cell_size_x:  Returned X cell size (horizontal) in m
        :param cell_size_y:  Returned Y cell size (vertical) in m
        :type  az:           float
        :type  cell_size_x:  float_ref
        :type  cell_size_y:  float_ref

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function determines default cell sizes for a vertical grid
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
        cell_size_x.value, cell_size_y.value = self._get_grid_section_cell_sizes(az, cell_size_x.value, cell_size_y.value)
        




    def get_info(self, type, array, x, y, z):
        """
        Get information about a voxel.
        
        :param type:   Data Type
        :param array:  Array Size
        :param x:      Elements in X
        :param y:      Elements in Y
        :param z:      Elements in Z
        :type  type:   int_ref
        :type  array:  int_ref
        :type  x:      int_ref
        :type  y:      int_ref
        :type  z:      int_ref

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        type.value, array.value, x.value, y.value, z.value = self._get_info(type.value, array.value, x.value, y.value, z.value)
        




    def get_ipj(self, ipj):
        """
        Get the projection of the voxel.
        
        :param ipj:  `GXIPJ <geosoft.gxapi.GXIPJ>` object to save `GXVOX <geosoft.gxapi.GXVOX>`'s meta to
        :type  ipj:  GXIPJ

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_ipj(ipj)
        




    def get_limits(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the range of indices with non-dummy data.
        
        :param min_x:  Index of minimum valid data in X.
        :param min_y:  Index of minimum valid data in Y.
        :param min_z:  Index of minimum valid data in Z.
        :param max_x:  Index of maximum valid data in X.
        :param max_y:  Index of maximum valid data in Y.
        :param max_z:  Index of maximum valid data in Z.
        :type  min_x:  int_ref
        :type  min_y:  int_ref
        :type  min_z:  int_ref
        :type  max_x:  int_ref
        :type  max_y:  int_ref
        :type  max_z:  int_ref

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Find the non-dummy volume of a `GXVOX <geosoft.gxapi.GXVOX>` object. If the voxel is all dummies,
        returns `iMAX <geosoft.gxapi.iMAX>` for the minima, and `iMIN <geosoft.gxapi.iMIN>` for the maxima.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._get_limits(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_limits_xyz(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the range in true XYZ of non-dummy data.
        
        :param min_x:  Minimum valid data in X.
        :param min_y:  Minimum valid data in Y.
        :param min_z:  Minimum valid data in Z.
        :param max_x:  Maximum valid data in X.
        :param max_y:  Maximum valid data in Y.
        :param max_z:  Maximum valid data in Z.
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  min_z:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref
        :type  max_z:  float_ref

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Find the non-dummy volume of a `GXVOX <geosoft.gxapi.GXVOX>` in true (X, Y, Z). This method
        works for voxels which are rotated or oriented in 3D, and returns
        the true min and max X, Y and Z limits in the data.
        The bounds are the bounds for the voxel
        center points. If the voxel is all dummies,
        returns `rMAX <geosoft.gxapi.rMAX>` for the minima, and `rMIN <geosoft.gxapi.rMIN>` for the maxima.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._get_limits_xyz(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_location(self, origin_x, origin_y, origin_z, vv_x, vv_y, vv_z):
        """
        Get Location information
        
        :param origin_x:  Origin X
        :param origin_y:  Origin Y
        :param origin_z:  Origin Z
        :param vv_x:      Cell sizes in X
        :param vv_y:      Cell sizes in Y
        :param vv_z:      Cell sizes in Z
        :type  origin_x:  float_ref
        :type  origin_y:  float_ref
        :type  origin_z:  float_ref
        :type  vv_x:      GXVV
        :type  vv_y:      GXVV
        :type  vv_z:      GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        origin_x.value, origin_y.value, origin_z.value = self._get_location(origin_x.value, origin_y.value, origin_z.value, vv_x, vv_y, vv_z)
        




    def get_location_points(self, vv_x, vv_y, vv_z):
        """
        Get the computed location points.
        
        :param vv_x:  Locations in X
        :param vv_y:  Locations in Y
        :param vv_z:  Locations in Z
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_location_points(vv_x, vv_y, vv_z)
        




    def get_meta(self, meta):
        """
        Get the metadata of a voxel.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to save `GXVOX <geosoft.gxapi.GXVOX>`'s meta to
        :type  meta:  GXMETA

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_meta(meta)
        




    def get_double_location(self, origin_x, origin_y, origin_z, vect_xx, vect_xy, vect_xz, vect_yx, vect_yy, vect_yz, vect_zx, vect_zy, vect_zz):
        """
        Get the location of a voxel with origin and scaled xyz vectors
        
        :param origin_x:  Origin X
        :param origin_y:  Origin Y
        :param origin_z:  Origin Z
        :param vect_xx:   VectX X
        :param vect_xy:   VectX Y
        :param vect_xz:   VectX Z
        :param vect_yx:   VectY X
        :param vect_yy:   VectY Y
        :param vect_yz:   VectY Z
        :param vect_zx:   VectZ X
        :param vect_zy:   VectZ Y
        :param vect_zz:   VectZ Z
        :type  origin_x:  float_ref
        :type  origin_y:  float_ref
        :type  origin_z:  float_ref
        :type  vect_xx:   float_ref
        :type  vect_xy:   float_ref
        :type  vect_xz:   float_ref
        :type  vect_yx:   float_ref
        :type  vect_yy:   float_ref
        :type  vect_yz:   float_ref
        :type  vect_zx:   float_ref
        :type  vect_zy:   float_ref
        :type  vect_zz:   float_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        origin_x.value, origin_y.value, origin_z.value, vect_xx.value, vect_xy.value, vect_xz.value, vect_yx.value, vect_yy.value, vect_yz.value, vect_zx.value, vect_zy.value, vect_zz.value = self._get_double_location(origin_x.value, origin_y.value, origin_z.value, vect_xx.value, vect_xy.value, vect_xz.value, vect_yx.value, vect_yy.value, vect_yz.value, vect_zx.value, vect_zy.value, vect_zz.value)
        




    def get_simple_location(self, origin_x, origin_y, origin_z, cell_x, cell_y, cell_z):
        """
        Get Simple Location information
        
        :param origin_x:  Origin X
        :param origin_y:  Origin Y
        :param origin_z:  Origin Z
        :param cell_x:    Cell Sizes in X (`rDUMMY <geosoft.gxapi.rDUMMY>` if not uniform)
        :param cell_y:    Cell Sizes in Y (`rDUMMY <geosoft.gxapi.rDUMMY>` if not uniform)
        :param cell_z:    Cell Sizes in Z (`rDUMMY <geosoft.gxapi.rDUMMY>` if not uniform)
        :type  origin_x:  float_ref
        :type  origin_y:  float_ref
        :type  origin_z:  float_ref
        :type  cell_x:    float_ref
        :type  cell_y:    float_ref
        :type  cell_z:    float_ref

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        origin_x.value, origin_y.value, origin_z.value, cell_x.value, cell_y.value, cell_z.value = self._get_simple_location(origin_x.value, origin_y.value, origin_z.value, cell_x.value, cell_y.value, cell_z.value)
        




    def get_stats(self):
        """
        Get precomputed statistics on this object.
        

        :returns:    `GXST <geosoft.gxapi.GXST>` object
        :rtype:      GXST

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_stats()
        return GXST(ret_val)




    def get_tpat(self, tpat):
        """
        Get a copy of a thematic voxel's `GXTPAT <geosoft.gxapi.GXTPAT>` object.
        
        :param tpat:  `GXTPAT <geosoft.gxapi.GXTPAT>` object to get
        :type  tpat:  GXTPAT

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Each row in the `GXTPAT <geosoft.gxapi.GXTPAT>` object corresponds to a stored index
        value in the thematic voxel. The `GXTPAT <geosoft.gxapi.GXTPAT>` should NOT be modified
        by the addition or deletion of items, if it is to be
        restored into the `GXVOX <geosoft.gxapi.GXVOX>` object, but the CODE, LABEL, DESCRIPTION
        or COLOR info can be changed.
        The `GXTPAT <geosoft.gxapi.GXTPAT>` object is stored inside the `GXVOX <geosoft.gxapi.GXVOX>` `GXMETA <geosoft.gxapi.GXMETA>` object.
        """
        self._get_tpat(tpat)
        



    @classmethod
    def grid_points(cls, name, error, cell_size, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, vv_x, vv_y, vv_z, vv_d, ipj):
        """
        Grid a `GXVOX <geosoft.gxapi.GXVOX>` from point `GXVV <geosoft.gxapi.GXVV>`'s.
        
        :param name:        Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param error:       Name of error `GXVOX <geosoft.gxapi.GXVOX>` ("" for none)
        :param cell_size:   Cell size (DUMMY for default)
        :param var_only:    Variogram Only
        :param min_radius:  Minimum Search Radius (DUMMY for none)
        :param max_radius:  Maximum Search Radius (DUMMY for none)
        :param min_points:  Minimum Search Points
        :param max_points:  Maximum Search Points
        :param model:       Model number 1-power, 2-sperical, 3-gaussian, 4-exponential
        :param power:       Power
        :param slope:       Slope
        :param range:       Range
        :param nugget:      Nugget
        :param sill:        Sill
        :param type:        :ref:`GS_TYPES`
        :param vv_x:        X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:        Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:        Z `GXVV <geosoft.gxapi.GXVV>`
        :param vv_d:        Data `GXVV <geosoft.gxapi.GXVV>`
        :type  name:        str
        :type  error:       str
        :type  cell_size:   float
        :type  var_only:    int
        :type  min_radius:  float
        :type  max_radius:  float
        :type  min_points:  int
        :type  max_points:  int
        :type  model:       int
        :type  power:       float
        :type  slope:       float
        :type  range:       float
        :type  nugget:      float
        :type  sill:        float
        :type  type:        int
        :type  vv_x:        GXVV
        :type  vv_y:        GXVV
        :type  vv_z:        GXVV
        :type  vv_d:        GXVV
        :type  ipj:         GXIPJ

        :returns:           `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:             GXVOX

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapVOX._grid_points(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, vv_x, vv_y, vv_z, vv_d, ipj)
        return GXVOX(ret_val)



    @classmethod
    def grid_points_z(cls, name, error, cell_size, cell_size_z, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, vv_x, vv_y, vv_z, vv_d, ipj):
        """
        Grid a `GXVOX <geosoft.gxapi.GXVOX>` from point `GXVV <geosoft.gxapi.GXVV>`'s (using variable Z's)
        
        :param name:         Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param error:        Name of error `GXVOX <geosoft.gxapi.GXVOX>` ("" for none)
        :param cell_size:    Cell size (DUMMY for default)
        :param cell_size_z:  Cell size in Z ("" for default)
        :param var_only:     Variogram Only
        :param min_radius:   Minimum Search Radius (DUMMY for none)
        :param max_radius:   Maximum Search Radius (DUMMY for none)
        :param min_points:   Minimum Search Points
        :param max_points:   Maximum Search Points
        :param model:        Model number 1-power, 2-sperical, 3-gaussian, 4-exponential
        :param power:        Power
        :param slope:        Slope
        :param range:        Range
        :param nugget:       Nugget
        :param sill:         Sill
        :param type:         :ref:`GS_TYPES`
        :param vv_x:         X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:         Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:         Z `GXVV <geosoft.gxapi.GXVV>`
        :param vv_d:         Data `GXVV <geosoft.gxapi.GXVV>`
        :type  name:         str
        :type  error:        str
        :type  cell_size:    float
        :type  cell_size_z:  str
        :type  var_only:     int
        :type  min_radius:   float
        :type  max_radius:   float
        :type  min_points:   int
        :type  max_points:   int
        :type  model:        int
        :type  power:        float
        :type  slope:        float
        :type  range:        float
        :type  nugget:       float
        :type  sill:         float
        :type  type:         int
        :type  vv_x:         GXVV
        :type  vv_y:         GXVV
        :type  vv_z:         GXVV
        :type  vv_d:         GXVV
        :type  ipj:          GXIPJ

        :returns:            `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:              GXVOX

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapVOX._grid_points_z(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, cell_size_z.encode(), var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, vv_x, vv_y, vv_z, vv_d, ipj)
        return GXVOX(ret_val)



    @classmethod
    def grid_points_z_ex(cls, name, error, cell_size, cell_size_z, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, strike, dip, plunge, along_strike_weight, down_dip_weight, type, vv_x, vv_y, vv_z, vv_d, ipj):
        """
        Grid a `GXVOX <geosoft.gxapi.GXVOX>` from point `GXVV <geosoft.gxapi.GXVV>`'s (using variable Z's)
        
        :param name:                 Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param error:                Name of error `GXVOX <geosoft.gxapi.GXVOX>` ("" for none)
        :param cell_size:            Cell size (DUMMY for default)
        :param cell_size_z:          Cell size in Z ("" for default)
        :param var_only:             Variogram Only
        :param min_radius:           Minimum Search Radius (DUMMY for none)
        :param max_radius:           Maximum Search Radius (DUMMY for none)
        :param min_points:           Minimum Search Points
        :param max_points:           Maximum Search Points
        :param model:                Model number 1-power, 2-sperical, 3-gaussian, 4-exponential
        :param power:                Power
        :param slope:                Slope
        :param range:                Range
        :param nugget:               Nugget
        :param sill:                 Sill
        :param strike:               Strike
        :param dip:                  Dip
        :param plunge:               Plunge
        :param along_strike_weight:  Strike Weight
        :param down_dip_weight:      Dip Plane Weight
        :param type:                 :ref:`GS_TYPES`
        :param vv_x:                 X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:                 Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:                 Z `GXVV <geosoft.gxapi.GXVV>`
        :param vv_d:                 Data `GXVV <geosoft.gxapi.GXVV>`
        :type  name:                 str
        :type  error:                str
        :type  cell_size:            float
        :type  cell_size_z:          str
        :type  var_only:             int
        :type  min_radius:           float
        :type  max_radius:           float
        :type  min_points:           int
        :type  max_points:           int
        :type  model:                int
        :type  power:                float
        :type  slope:                float_ref
        :type  range:                float_ref
        :type  nugget:               float
        :type  sill:                 float_ref
        :type  strike:               float
        :type  dip:                  float
        :type  plunge:               float
        :type  along_strike_weight:  float
        :type  down_dip_weight:      float
        :type  type:                 int
        :type  vv_x:                 GXVV
        :type  vv_y:                 GXVV
        :type  vv_z:                 GXVV
        :type  vv_d:                 GXVV
        :type  ipj:                  GXIPJ

        :returns:                    `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:                      GXVOX

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, slope.value, range.value, sill.value = gxapi_cy.WrapVOX._grid_points_z_ex(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, cell_size_z.encode(), var_only, min_radius, max_radius, min_points, max_points, model, power, slope.value, range.value, nugget, sill.value, strike, dip, plunge, along_strike_weight, down_dip_weight, type, vv_x, vv_y, vv_z, vv_d, ipj)
        return GXVOX(ret_val)




    def can_append_to(self, surface_file):
        """
        Check if this voxel can append to a surface file.
        
        :param surface_file:  Surface file
        :type  surface_file:  str

        :returns:             1 if can append
        :rtype:               int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._can_append_to(surface_file.encode())
        return ret_val




    def get_cell_size_strings(self, loc_x, loc_y, loc_z, scale_x, scale_y, scale_z):
        """
        Get the Location Strings
        
        :param loc_x:    X String
        :param loc_y:    Y String
        :param loc_z:    Z String
        :param scale_x:  Scale to multiply X
        :param scale_y:  Scale to multiply Y
        :param scale_z:  Scale to multiply Z
        :type  loc_x:    str_ref
        :type  loc_y:    str_ref
        :type  loc_z:    str_ref
        :type  scale_x:  float
        :type  scale_y:  float
        :type  scale_z:  float

        .. versionadded:: 6.3.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        loc_x.value, loc_y.value, loc_z.value = self._get_cell_size_strings(loc_x.value.encode(), loc_y.value.encode(), loc_z.value.encode(), scale_x, scale_y, scale_z)
        




    def is_thematic(self):
        """
        Is this a thematic voxel?
        

        :returns:    1 if `GXVOX <geosoft.gxapi.GXVOX>` is thematic
        :rtype:      int

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A thematic voxel is one where the stored integer values
        represent indices into an internally stored `GXTPAT <geosoft.gxapi.GXTPAT>` object.
        Thematic voxels contain their own color definitions, and
        normal numerical operations, such as applying ITRs for display,
        are not valid.
        """
        ret_val = self._is_thematic()
        return ret_val




    def is_vector_voxel(self):
        """
        Is this a vector voxel?
        

        :returns:    1 if `GXVOX <geosoft.gxapi.GXVOX>` is a vector voxel
        :rtype:      int

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A vector voxel is one where each data element consists of 3 4-byte float values.
        Vector voxels normally have the file type "geosoft_vectorvoxel".
        """
        ret_val = self._is_vector_voxel()
        return ret_val




    def set_cell_size_strings(self, loc_x, loc_y, loc_z):
        """
        Set the Location Strings
        
        :param loc_x:  X String
        :param loc_y:  Y String
        :param loc_z:  Z String
        :type  loc_x:  str
        :type  loc_y:  str
        :type  loc_z:  str

        :returns:      0 - Ok
                       1 - Invalid data
        :rtype:        int

        .. versionadded:: 6.3.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._set_cell_size_strings(loc_x.encode(), loc_y.encode(), loc_z.encode())
        return ret_val



    @classmethod
    def log_grid_points_z_ex(cls, name, error, cell_size, cell_size_z, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, strike, dip, plunge, along_strike_weight, down_dip_weight, log_opt, min_log, type, vv_x, vv_y, vv_z, vv_d, ipj):
        """
        Log grid a `GXVOX <geosoft.gxapi.GXVOX>` from point `GXVV <geosoft.gxapi.GXVV>`'s (using variable Z's)
        
        :param name:                 Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param error:                Name of error `GXVOX <geosoft.gxapi.GXVOX>` ("" for none)
        :param cell_size:            Cell size (DUMMY for default)
        :param cell_size_z:          Cell size in Z ("" for default)
        :param var_only:             Variogram Only
        :param min_radius:           Minimum Search Radius (DUMMY for none)
        :param max_radius:           Maximum Search Radius (DUMMY for none)
        :param min_points:           Minimum Search Points
        :param max_points:           Maximum Search Points
        :param model:                Model number 1-power, 2-sperical, 3-gaussian, 4-exponential
        :param power:                Power
        :param slope:                Slope
        :param range:                Range
        :param nugget:               Nugget
        :param sill:                 Sill
        :param strike:               Strike
        :param dip:                  Dip
        :param plunge:               Plunge
        :param along_strike_weight:  Strike Weight
        :param down_dip_weight:      Dip Plane Weight
        :param log_opt:              :ref:`VOX_GRID_LOGOPT` Log Option
        :param min_log:              Minimum log
        :param type:                 :ref:`GS_TYPES`
        :param vv_x:                 X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:                 Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:                 Z `GXVV <geosoft.gxapi.GXVV>`
        :param vv_d:                 Data `GXVV <geosoft.gxapi.GXVV>`
        :type  name:                 str
        :type  error:                str
        :type  cell_size:            float
        :type  cell_size_z:          str
        :type  var_only:             int
        :type  min_radius:           float
        :type  max_radius:           float
        :type  min_points:           int
        :type  max_points:           int
        :type  model:                int
        :type  power:                float
        :type  slope:                float_ref
        :type  range:                float_ref
        :type  nugget:               float
        :type  sill:                 float_ref
        :type  strike:               float
        :type  dip:                  float
        :type  plunge:               float
        :type  along_strike_weight:  float
        :type  down_dip_weight:      float
        :type  log_opt:              int
        :type  min_log:              float
        :type  type:                 int
        :type  vv_x:                 GXVV
        :type  vv_y:                 GXVV
        :type  vv_z:                 GXVV
        :type  vv_d:                 GXVV
        :type  ipj:                  GXIPJ

        :returns:                    `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:                      GXVOX

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, slope.value, range.value, sill.value = gxapi_cy.WrapVOX._log_grid_points_z_ex(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, cell_size_z.encode(), var_only, min_radius, max_radius, min_points, max_points, model, power, slope.value, range.value, nugget, sill.value, strike, dip, plunge, along_strike_weight, down_dip_weight, log_opt, min_log, type, vv_x, vv_y, vv_z, vv_d, ipj)
        return GXVOX(ret_val)



    @classmethod
    def krig(cls, name, cell_size, type, vv_x, vv_y, vv_z, vv_d, ipj, reg):
        """
        A more compact and extensible form of `log_grid_points_z_ex <geosoft.gxapi.GXVOX.log_grid_points_z_ex>`.
        
        :param name:       Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param cell_size:  Cell size (DUMMY for default)
        :param type:       :ref:`GS_TYPES`
        :param vv_x:       X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:       Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:       Z `GXVV <geosoft.gxapi.GXVV>`
        :param vv_d:       Data `GXVV <geosoft.gxapi.GXVV>`
        :type  name:       str
        :type  cell_size:  float
        :type  type:       int
        :type  vv_x:       GXVV
        :type  vv_y:       GXVV
        :type  vv_z:       GXVV
        :type  vv_d:       GXVV
        :type  ipj:        GXIPJ
        :type  reg:        GXREG

        :returns:          `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:            GXVOX

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Optional Parameters.

        If these values are not set in the `GXREG <geosoft.gxapi.GXREG>`, then default parameters will be used.

        ERROR_VOXEL:		Name of error `GXVOX <geosoft.gxapi.GXVOX>` ("" for none)
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
        LOG_OPT:			One of :ref:`VOX_GRID_LOGOPT` (Default = 0)
        MIN_LOG:			Log Minimum (REAL)	(Default = 1)
        MIN_X:				Minimum X (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. multiple of cell size chosen)
        MAX_X:				Maximum X (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)
        MIN_Y:				Minimum Y (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. external multiple of cell size chosen)
        MAX_Y:				Maximum Y (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)
        MIN_Z:				Minimum Z (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. multiple of cell size chosen)
        MAX_Z:				Maximum Z (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)A more compact and extensible form of `log_grid_points_z_ex <geosoft.gxapi.GXVOX.log_grid_points_z_ex>`. Only the most
        basic parameters are entered directly. Optional parameters are passed via a `GXREG <geosoft.gxapi.GXREG>` object.
        """
        ret_val = gxapi_cy.WrapVOX._krig(GXContext._get_tls_geo(), name.encode(), cell_size, type, vv_x, vv_y, vv_z, vv_d, ipj, reg)
        return GXVOX(ret_val)



    @classmethod
    def math(cls, master, mastervar, output, outvar, formula, lst):
        """
        Produces a new voxes using a formula on existing voxels/Grids
        
        :param master:     Master `GXVOX <geosoft.gxapi.GXVOX>` Name
        :param mastervar:  Master `GXVOX <geosoft.gxapi.GXVOX>` Variable Name
        :param output:     Output `GXVOX <geosoft.gxapi.GXVOX>` Name
        :param outvar:     Output `GXVOX <geosoft.gxapi.GXVOX>` Variable Name
        :param formula:    Formula
        :param lst:        List of Voxels/Grids to use as inputs
        :type  master:     str
        :type  mastervar:  str
        :type  output:     str
        :type  outvar:     str
        :type  formula:    str
        :type  lst:        GXLST

        :returns:          VOXEL handle
        :rtype:            GXVOX

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The input voxels must all be of the same type.
        """
        ret_val = gxapi_cy.WrapVOX._math(GXContext._get_tls_geo(), master.encode(), mastervar.encode(), output.encode(), outvar.encode(), formula.encode(), lst)
        return GXVOX(ret_val)




    def merge(self, vox2, reg, output_vox):
        """
        Merge two Voxels.
        
        :param vox2:        `GXVOX <geosoft.gxapi.GXVOX>` object
        :param reg:         Parameters (see above)
        :param output_vox:  Output voxel file name.
        :type  vox2:        GXVOX
        :type  reg:         GXREG
        :type  output_vox:  str

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._merge(vox2, reg, output_vox.encode())
        



    @classmethod
    def nearest_neighbour_grid(cls, name, cell_size, max_radius, type, vv_x, vv_y, vv_z, vv_d, ipj):
        """
        Grid a `GXVOX <geosoft.gxapi.GXVOX>` from point `GXVV <geosoft.gxapi.GXVV>`'s using the Nearest Neighbours method.
        
        :param name:        Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param cell_size:   Cell size (DUMMY for default)
        :param max_radius:  Maximum radius (DUMMY for none)
        :param type:        :ref:`GS_TYPES`
        :param vv_x:        X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:        Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:        Z `GXVV <geosoft.gxapi.GXVV>`
        :param vv_d:        Data `GXVV <geosoft.gxapi.GXVV>`
        :type  name:        str
        :type  cell_size:   float
        :type  max_radius:  float
        :type  type:        int
        :type  vv_x:        GXVV
        :type  vv_y:        GXVV
        :type  vv_z:        GXVV
        :type  vv_d:        GXVV
        :type  ipj:         GXIPJ

        :returns:           `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:             GXVOX

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapVOX._nearest_neighbour_grid(GXContext._get_tls_geo(), name.encode(), cell_size, max_radius, type, vv_x, vv_y, vv_z, vv_d, ipj)
        return GXVOX(ret_val)



    @classmethod
    def compute_cell_size(cls, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Compute the Cell size based on specific Area
        
        :param min_x:  MinX
        :param min_y:  MinY
        :param min_z:  MinZ
        :param max_x:  MaxX
        :param max_y:  MaxY
        :param max_z:  MaxZ
        :type  min_x:  float
        :type  min_y:  float
        :type  min_z:  float
        :type  max_x:  float
        :type  max_y:  float
        :type  max_z:  float

        :returns:      Cell Size
        :rtype:        float

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapVOX._compute_cell_size(GXContext._get_tls_geo(), min_x, min_y, min_z, max_x, max_y, max_z)
        return ret_val




    def re_grid(self, vox_to_regrid, reg, output_vox):
        """
        Regrid a Voxel.
        
        :param vox_to_regrid:  `GXVOX <geosoft.gxapi.GXVOX>` object to regrid
        :param reg:            Parameters (not implemented)
        :param output_vox:     Output voxel file name.
        :type  vox_to_regrid:  GXVOX
        :type  reg:            GXREG
        :type  output_vox:     str

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._re_grid(vox_to_regrid, reg, output_vox.encode())
        




    def resample_pg(self, ipj, orig_x, orig_y, orig_z, spacing_x, spacing_y, spacing_z, size_x, size_y, size_z, min_z, max_z, interp):
        """
        Resample a voxel over an input volume to a `GXPG <geosoft.gxapi.GXPG>`.
        
        :param ipj:        Projection to use for Origin, Spacing values
        :param orig_x:     Origin X
        :param orig_y:     Origin Y
        :param orig_z:     Origin Z
        :param spacing_x:  Spacing in X
        :param spacing_y:  Spacing in Y
        :param spacing_z:  Spacing in Z
        :param size_x:     Samples in X
        :param size_y:     Samples in Y
        :param size_z:     Samples in Z
        :param min_z:      Minimum Z to resample (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param max_z:      Maximum Z to resample (can be `rDUMMY <geosoft.gxapi.rDUMMY>`)
        :param interp:     :ref:`VOX_SLICE_MODE`
        :type  ipj:        GXIPJ
        :type  orig_x:     float
        :type  orig_y:     float
        :type  orig_z:     float
        :type  spacing_x:  float
        :type  spacing_y:  float
        :type  spacing_z:  float
        :type  size_x:     int
        :type  size_y:     int
        :type  size_z:     int
        :type  min_z:      float
        :type  max_z:      float
        :type  interp:     int

        :returns:          `GXPG <geosoft.gxapi.GXPG>` object, terminates on error
        :rtype:            GXPG

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Creates and dummies a `GXPG <geosoft.gxapi.GXPG>` object based on the input
        dimensions, then resamples the voxel to the pager
        at the locations determined by input projection, origin and spacings.
        """
        ret_val = self._resample_pg(ipj, orig_x, orig_y, orig_z, spacing_x, spacing_y, spacing_z, size_x, size_y, size_z, min_z, max_z, interp)
        return GXPG(ret_val)




    def rescale_cell_sizes(self, scale):
        """
        Multiply all cell sizes by a fixed factor.
        
        :param scale:  Scaling factor (>0)
        :type  scale:  float

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is useful, for instance for converting sizes in one
        unit to sizes in another unit if changing the projection
        and the projection's unit changes, since the voxel inherits
        its projection's units.
        """
        self._rescale_cell_sizes(scale)
        




    def sample_cdi(self, db, line, x_ch, y_ch, elev_ch, negative_depths_down, topo_ch, mode, out_ch):
        """
        Sample a voxel at locations/elevations in a CDI database.
        
        :param db:                    CDI Database handle
        :param line:                  Line handle
        :param x_ch:                  X channel handle
        :param y_ch:                  Y channel handle
        :param elev_ch:               Depth array channel handle
        :param negative_depths_down:  Depths sign: 0 - positive down, 1 - negative down
        :param topo_ch:               Elevation channel handle (can be `NULLSYMB <geosoft.gxapi.NULLSYMB>`)
        :param mode:                  Interpolation mode: 0 - linear, 1 - nearest
        :param out_ch:                Output channel name
        :type  db:                    GXDB
        :type  line:                  int
        :type  x_ch:                  int
        :type  y_ch:                  int
        :type  elev_ch:               int
        :type  negative_depths_down:  int
        :type  topo_ch:               int
        :type  mode:                  int
        :type  out_ch:                str

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A "CDI" database does not need to be conductivity/depth.
        It normally contains an array channel of depth values for
        each (X, Y) location, with corresponding data array channels of
        values taken at those (X, Y, Z) locations.
        If the optional elevation channel is used, its value is used as an
        offset to the depth channel values. Depths are positive down by
        default; use the "Negative depths down" parameter if the depths
        become more negative as you go deeper.
        """
        self._sample_cdi(db, line, x_ch, y_ch, elev_ch, negative_depths_down, topo_ch, mode, out_ch.encode())
        




    def sample_cdi_to_topography(self, db, line, x_ch, y_ch, zvv, mode, out_ch, topo_ch):
        """
        Sample a voxel at fixed elevations along a path in a CDI database, and output them to an array channel, deleting leading dummy values, and
        writing the elevation of the first non-dummy item to a topography channel.
        
        :param db:       CDI Database handle
        :param line:     Line handle
        :param x_ch:     X channel handle
        :param y_ch:     Y channel handle
        :param zvv:      Z values to sample at each X, Y
        :param mode:     Interpolation mode: 0 - linear, 1 - nearest
        :param out_ch:   Output data array channel name
        :param topo_ch:  Output topography channel name
        :type  db:       GXDB
        :type  line:     int
        :type  x_ch:     int
        :type  y_ch:     int
        :type  zvv:      GXVV
        :type  mode:     int
        :type  out_ch:   str
        :type  topo_ch:  str

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._sample_cdi_to_topography(db, line, x_ch, y_ch, zvv, mode, out_ch.encode(), topo_ch.encode())
        




    def sample_vv(self, xvv, yvv, zvv, interp, dvv):
        """
        Sample a voxel at multiple locations.
        
        :param xvv:     X locations (input)
        :param yvv:     Y locations (input)
        :param zvv:     Z locations (input)
        :param interp:  Interpolation mode: 0 - linear, 1 - nearest
        :param dvv:     Returned values
        :type  xvv:     GXVV
        :type  yvv:     GXVV
        :type  zvv:     GXVV
        :type  interp:  int
        :type  dvv:     GXVV

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Sample at voxel at XYZ locations input in VVs. Values returned in a `GXVV <geosoft.gxapi.GXVV>`.
        """
        self._sample_vv(xvv, yvv, zvv, interp, dvv)
        




    def set_ipj(self, ipj):
        """
        Set the projection of the voxel.
        
        :param ipj:  `GXIPJ <geosoft.gxapi.GXIPJ>` object to save `GXVOX <geosoft.gxapi.GXVOX>`'s meta to
        :type  ipj:  GXIPJ

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_ipj(ipj)
        




    def set_location(self, origin_x, origin_y, origin_z, vv_x, vv_y, vv_z):
        """
        Set Location information
        
        :param origin_x:  Origin X
        :param origin_y:  Origin Y
        :param origin_z:  Origin Z
        :param vv_x:      Cell sizes in X
        :param vv_y:      Cell sizes in Y
        :param vv_z:      Cell sizes in Z
        :type  origin_x:  float
        :type  origin_y:  float
        :type  origin_z:  float
        :type  vv_x:      GXVV
        :type  vv_y:      GXVV
        :type  vv_z:      GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_location(origin_x, origin_y, origin_z, vv_x, vv_y, vv_z)
        




    def set_meta(self, meta):
        """
        Set the metadata of a voxel.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to add to `GXVOX <geosoft.gxapi.GXVOX>`'s meta
        :type  meta:  GXMETA

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_meta(meta)
        




    def set_origin(self, origin, origin_x, origin_y, origin_z):
        """
        Set the Voxel Origin
        
        :param origin:    Type of origin being set :ref:`VOX_ORIGIN`
        :param origin_x:  Origin X
        :param origin_y:  Origin Y
        :param origin_z:  Origin Z
        :type  origin:    int
        :type  origin_x:  float
        :type  origin_y:  float
        :type  origin_z:  float

        .. versionadded:: 6.3.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_origin(origin, origin_x, origin_y, origin_z)
        




    def set_simple_location(self, origin_x, origin_y, origin_z, cell_x, cell_y, cell_z):
        """
        Set Simple Location information
        
        :param origin_x:  Origin X
        :param origin_y:  Origin Y
        :param origin_z:  Origin Z
        :param cell_x:    Cell Sizes in X (`rDUMMY <geosoft.gxapi.rDUMMY>` if not changed)
        :param cell_y:    Cell Sizes in Y (`rDUMMY <geosoft.gxapi.rDUMMY>` if not changed)
        :param cell_z:    Cell Sizes in Z (`rDUMMY <geosoft.gxapi.rDUMMY>` if not changed)
        :type  origin_x:  float
        :type  origin_y:  float
        :type  origin_z:  float
        :type  cell_x:    float
        :type  cell_y:    float
        :type  cell_z:    float

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_simple_location(origin_x, origin_y, origin_z, cell_x, cell_y, cell_z)
        




    def set_tpat(self, tpat):
        """
        Set a thematic voxel's `GXTPAT <geosoft.gxapi.GXTPAT>` object.
        
        :param tpat:  `GXTPAT <geosoft.gxapi.GXTPAT>` object to store
        :type  tpat:  GXTPAT

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Each row in the `GXTPAT <geosoft.gxapi.GXTPAT>` object corresponds to a stored index
        value in the thematic voxel. The `GXTPAT <geosoft.gxapi.GXTPAT>` should NOT be modified
        by the addition or deletion of items, if it is to be
        restored into the `GXVOX <geosoft.gxapi.GXVOX>` object, but the CODE, LABEL, DESCRIPTION
        or COLOR info can be changed.
        The `GXTPAT <geosoft.gxapi.GXTPAT>` object is stored inside the `GXVOX <geosoft.gxapi.GXVOX>` `GXMETA <geosoft.gxapi.GXMETA>` object.
        """
        self._set_tpat(tpat)
        




    def slice_ipj(self, name, ipj, mode, orig_x, orig_y, cell_size_x, cell_size_y, size_x, size_y):
        """
        Extract a slice of a voxel based on an `GXIPJ <geosoft.gxapi.GXIPJ>`
        
        :param name:         Grid Name
        :param ipj:          Grid `GXIPJ <geosoft.gxapi.GXIPJ>` (includes orientation, etc)
        :param mode:         :ref:`VOX_SLICE_MODE`
        :param orig_x:       Grid Origin X
        :param orig_y:       Grid Origin Y
        :param cell_size_x:  Grid Cell Size in X
        :param cell_size_y:  Grid Cell Size in Y
        :param size_x:       Grid cells in X
        :param size_y:       Grid cells in Y
        :type  name:         str
        :type  ipj:          GXIPJ
        :type  mode:         int
        :type  orig_x:       float
        :type  orig_y:       float
        :type  cell_size_x:  float
        :type  cell_size_y:  float
        :type  size_x:       int
        :type  size_y:       int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._slice_ipj(name.encode(), ipj, mode, orig_x, orig_y, cell_size_x, cell_size_y, size_x, size_y)
        




    def slice_multi_layer_ipj(self, name, ipj, mode, orig_x, orig_y, cell_size_x, cell_size_y, size_x, size_y, layers, start_elev, elev_inc):
        """
        Extract multiple slices of a voxel based on an `GXIPJ <geosoft.gxapi.GXIPJ>`
        
        :param name:         Grid Name
        :param ipj:          Grid `GXIPJ <geosoft.gxapi.GXIPJ>` (includes orientation, etc)
        :param mode:         :ref:`VOX_SLICE_MODE`
        :param orig_x:       Grid Origin X
        :param orig_y:       Grid Origin Y
        :param cell_size_x:  Grid Cell Size in X
        :param cell_size_y:  Grid Cell Size in Y
        :param size_x:       Grid cells in X
        :param size_y:       Grid cells in Y
        :param layers:       Number of layers to extract
        :param start_elev:   Start elevation
        :param elev_inc:     Elevation increment
        :type  name:         str
        :type  ipj:          GXIPJ
        :type  mode:         int
        :type  orig_x:       float
        :type  orig_y:       float
        :type  cell_size_x:  float
        :type  cell_size_y:  float
        :type  size_x:       int
        :type  size_y:       int
        :type  layers:       int
        :type  start_elev:   float
        :type  elev_inc:     float

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._slice_multi_layer_ipj(name.encode(), ipj, mode, orig_x, orig_y, cell_size_x, cell_size_y, size_x, size_y, layers, start_elev, elev_inc)
        




    def subset_to_double_extents(self, output_vox):
        """
        Subset a `GXVOX <geosoft.gxapi.GXVOX>` to real extents.
        
        :param output_vox:  Output voxel file name.
        :type  output_vox:  str

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._subset_to_double_extents(output_vox.encode())
        



    @classmethod
    def sync(cls, name):
        """
        Syncronize the Metadata for this Voxel
        
        :param name:  Voxel name
        :type  name:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapVOX._sync(GXContext._get_tls_geo(), name.encode())
        




    def window_ply(self, pply, mask, min_z, max_z, output_vox, clip_dummies):
        """
        Window a `GXVOX <geosoft.gxapi.GXVOX>` to a `GXPLY <geosoft.gxapi.GXPLY>` file and Z.
        
        :param pply:          `GXPLY <geosoft.gxapi.GXPLY>` object
        :param mask:          Mask (0: inside `GXPLY <geosoft.gxapi.GXPLY>`, 1: outside `GXPLY <geosoft.gxapi.GXPLY>`)
        :param min_z:         Minimum Z (optional, `rDUMMY <geosoft.gxapi.rDUMMY>` for no minimum)
        :param max_z:         Maximum Z (optional, `rDUMMY <geosoft.gxapi.rDUMMY>` for no maximun)
        :param output_vox:    Output voxel file name.
        :param clip_dummies:  Clip extents to remove dummies (0: no (same size), 1: yes (smaller))
        :type  pply:          GXPLY
        :type  mask:          int
        :type  min_z:         float
        :type  max_z:         float
        :type  output_vox:    str
        :type  clip_dummies:  int

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The voxel is windowed horizontally to the input `GXPLY <geosoft.gxapi.GXPLY>` file.
        Optionally, it will be windowed to the input Z range as well.
        The output can be clipped to the non-dummied cells.
        """
        self._window_ply(pply, mask, min_z, max_z, output_vox.encode(), clip_dummies)
        




    def window_xyz(self, min_x, min_y, min_z, max_x, max_y, max_z, output_vox, clip_dummies):
        """
        Window a `GXVOX <geosoft.gxapi.GXVOX>` to ranges in X, Y and Z.
        
        :param min_x:         Minimum X (optional, `rDUMMY <geosoft.gxapi.rDUMMY>` for no minimum)
        :param min_y:         Minimum Y (optional, `rDUMMY <geosoft.gxapi.rDUMMY>` for no minimum)
        :param min_z:         Minimum Z (optional, `rDUMMY <geosoft.gxapi.rDUMMY>` for no minimum)
        :param max_x:         Maximum X (optional, `rDUMMY <geosoft.gxapi.rDUMMY>` for no maximun)
        :param max_y:         Maximum Y (optional, `rDUMMY <geosoft.gxapi.rDUMMY>` for no maximun)
        :param max_z:         Maximum Z (optional, `rDUMMY <geosoft.gxapi.rDUMMY>` for no maximun)
        :param output_vox:    Output voxel file name.
        :param clip_dummies:  Clip extents to remove dummies (0: no (same size), 1: yes (smaller))
        :type  min_x:         float
        :type  min_y:         float
        :type  min_z:         float
        :type  max_x:         float
        :type  max_y:         float
        :type  max_z:         float
        :type  output_vox:    str
        :type  clip_dummies:  int

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The six minima and maxima are optional.
        The output can be clipped to the non-dummied cells.
        """
        self._window_xyz(min_x, min_y, min_z, max_x, max_y, max_z, output_vox.encode(), clip_dummies)
        




    def write_xml(self, file):
        """
        Export the `GXVOX <geosoft.gxapi.GXVOX>` to XML
        
        :param file:  XML file to create
        :type  file:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._write_xml(file.encode())
        




    def convert_numeric_to_thematic(self, vv_translate, output_vox):
        """
        Convert numeric voxel to thematic (lithology) voxel
        
        :param vv_translate:  Translation `GXVV <geosoft.gxapi.GXVV>` handle.
        :param output_vox:    Output voxel file name.
        :type  vv_translate:  GXVV
        :type  output_vox:    str

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._convert_numeric_to_thematic(vv_translate, output_vox.encode())
        




    def convert_thematic_to_numeric(self, vv_translate, output_vox):
        """
        Convert thematic (lithology) voxel to numeric voxel
        
        :param vv_translate:  Translation `GXVV <geosoft.gxapi.GXVV>` handle.
        :param output_vox:    Output voxel file name.
        :type  vv_translate:  GXVV
        :type  output_vox:    str

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._convert_thematic_to_numeric(vv_translate, output_vox.encode())
        




    def convert_velocity_to_density(self, input_scaling_factor, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename):
        """
        Produces a density voxel using the velocity values in this voxel.
        
        :param input_scaling_factor:   1.0, if this voxel is in meters per second. Otherwise, a value by which each input cell is multiplied to convert it into meters per second.
        :param a5:                     Coefficient of fifth-order polynomial term.
        :param a4:                     Coefficient of fourth-order polynomial term.
        :param a3:                     Coefficient of third-order polynomial term.
        :param a2:                     Coefficient of second-order polynomial term.
        :param a1:                     Coefficient of first-order polynomial term.
        :param a0:                     Constant offset of output.
        :param output_scaling_factor:  1.0, to produce an output voxel that has units of g/cm^3. If different units are desired, pass in a different value, which will be multiplied into each output voxel cell.
        :param output_voxel_filename:  Filename of the output voxel.
        :type  input_scaling_factor:   float
        :type  a5:                     float
        :type  a4:                     float
        :type  a3:                     float
        :type  a2:                     float
        :type  a1:                     float
        :type  a0:                     float
        :type  output_scaling_factor:  float
        :type  output_voxel_filename:  str

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._convert_velocity_to_density(input_scaling_factor, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename.encode())
        




    def convert_velocity_in_range_to_density(self, input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename):
        """
        Produces a density voxel using the velocity values in this voxel, as long as the velocity values are in range.
        
        :param input_scaling_factor:   1.0, if this voxel is in meters per second. Otherwise, a value by which each input cell is multiplied to convert it into meters per second.
        :param input_lower_bound:      Lower bound on velocity values, in meters per second. If the input value (after being pre-multiplied by dInputScalingFactor) is less than this value, the output cell value will be DUMMY.
        :param input_upper_bound:      Upper bound on velocity values, in meters per second. If the input value (after being pre-multiplied by dInputScalingFactor) is greater than this value, the output cell value will be DUMMY.
        :param a5:                     Coefficient of fifth-order polynomial term.
        :param a4:                     Coefficient of fourth-order polynomial term.
        :param a3:                     Coefficient of third-order polynomial term.
        :param a2:                     Coefficient of second-order polynomial term.
        :param a1:                     Coefficient of first-order polynomial term.
        :param a0:                     Constant offset of output.
        :param output_scaling_factor:  1.0, to produce an output voxel that has units of g/cm^3. If different units are desired, pass in a different value, which will be multiplied into each output voxel cell.
        :param output_voxel_filename:  Filename of the output voxel.
        :type  input_scaling_factor:   float
        :type  input_lower_bound:      float
        :type  input_upper_bound:      float
        :type  a5:                     float
        :type  a4:                     float
        :type  a3:                     float
        :type  a2:                     float
        :type  a1:                     float
        :type  a0:                     float
        :type  output_scaling_factor:  float
        :type  output_voxel_filename:  str

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._convert_velocity_in_range_to_density(input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename.encode())
        




    def convert_density_to_velocity(self, input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename):
        """
        Produces a velocity voxel using the density values in this voxel.
        
        :param input_scaling_factor:   1.0, if this voxel is in g/cm^3. Otherwise, a value by which each input cell is multiplied to convert it into g/cm^3.
        :param input_lower_bound:      Lower bound on velocity values, in g/vm^3. If the input value (after being pre-multiplied by dInputScalingFactor) is less than this value, the output cell value will be DUMMY.
        :param input_upper_bound:      Upper bound on velocity values, in g/cm^3. If the input value (after being pre-multiplied by dInputScalingFactor) is greater than this value, the output cell value will be DUMMY.
        :param a5:                     Coefficient of fifth-order polynomial term.
        :param a4:                     Coefficient of fourth-order polynomial term.
        :param a3:                     Coefficient of third-order polynomial term.
        :param a2:                     Coefficient of second-order polynomial term.
        :param a1:                     Coefficient of first-order polynomial term.
        :param a0:                     Constant offset of output.
        :param output_scaling_factor:  1.0, to produce an output voxel that has units of meters per second. If different units are desired, pass in a different value, which will be multiplied into each output voxel cell.
        :param output_voxel_filename:  Filename of the output voxel.
        :type  input_scaling_factor:   float
        :type  input_lower_bound:      float
        :type  input_upper_bound:      float
        :type  a5:                     float
        :type  a4:                     float
        :type  a3:                     float
        :type  a2:                     float
        :type  a1:                     float
        :type  a0:                     float
        :type  output_scaling_factor:  float
        :type  output_voxel_filename:  str

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._convert_density_to_velocity(input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_voxel_filename.encode())
        




    def invert_z(self, output_voxel_filename):
        """
        Convert an inverted voxel to normal orientation
        
        :param output_voxel_filename:  Output voxel file name.
        :type  output_voxel_filename:  str

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._invert_z(output_voxel_filename.encode())
        



    @classmethod
    def dw_grid_db(cls, voxel, db, x, y, z, data, reg):
        """
        `dw_grid_db <geosoft.gxapi.GXVOX.dw_grid_db>`     Inverse-distance weighting gridding method, `GXDB <geosoft.gxapi.GXDB>` version, 3D.
        
        :param voxel:  Output voxel name
        :param db:     Database
        :param x:      X Channel [READONLY]
        :param y:      Y Channel [READONLY]
        :param z:      Z Channel [READONLY]
        :param data:   Data Channel [READONLY]
        :param reg:    Parameters (see above)
        :type  voxel:  str
        :type  db:     GXDB
        :type  x:      int
        :type  y:      int
        :type  z:      int
        :type  data:   int
        :type  reg:    GXREG

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** 3D cells take on the averaged values within a search radius, weighted inversely by distance.

        Weighting can be controlled using the power and slope properties;

        weighting = 1 / (distance^wtpower + 1/slope) where distance is in
        units of grid cells (X dimenstion). Default is 0.0,

        If the blanking distance is set, all cells whose center point is not within the blanking distance of
        at least one data point are set to dummy.

        `GXREG <geosoft.gxapi.GXREG>` Parameters:

        X0, Y0, Z0, DX, DY, DZ: Voxel origin, and cell sizes (required)
        WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters
        SEARCH_RADIUS: Distance weighting limit (default = 4 * CUBE_ROOT(DX*DY*DZ))
        BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 * CUBE_ROOT(DX*DY*DZ))
        LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?
        LOG_BASE: One of `VV_LOG_BASE_10 <geosoft.gxapi.VV_LOG_BASE_10>` (default) or `VV_LOG_BASE_E <geosoft.gxapi.VV_LOG_BASE_E>`
        LOG_NEGATIVE: One of `VV_LOG_NEGATIVE_NO <geosoft.gxapi.VV_LOG_NEGATIVE_NO>` (default) or `VV_LOG_NEGATIVE_YES <geosoft.gxapi.VV_LOG_NEGATIVE_YES>`
        """
        gxapi_cy.WrapVOX._dw_grid_db(GXContext._get_tls_geo(), voxel.encode(), db, x, y, z, data, reg)
        



    @classmethod
    def tin_grid_db(cls, voxel, db, x, y, z, data, method, z_cell, reg):
        """
        `tin_grid_db <geosoft.gxapi.GXVOX.tin_grid_db>`   `GXTIN <geosoft.gxapi.GXTIN>`-Gridding, `GXDB <geosoft.gxapi.GXDB>` version, 3D.
        
        :param voxel:   Output voxel name
        :param db:      Database
        :param x:       X Channel [READONLY]
        :param y:       Y Channel [READONLY]
        :param z:       Z Channel [READONLY]
        :param data:    Data Channel [READONLY]
        :param method:  Gridding method (0: Linear, 1: Natural Neighbour, 2: Nearest Neightbour
        :param z_cell:  Z Cell sizes (bottom to top)
        :param reg:     Parameters (see above)
        :type  voxel:   str
        :type  db:      GXDB
        :type  x:       int
        :type  y:       int
        :type  z:       int
        :type  data:    int
        :type  method:  int
        :type  z_cell:  GXVV
        :type  reg:     GXREG

        .. versionadded:: 8.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Designed for data in array channels position vertically at single XY locations.
        Creates a `GXTIN <geosoft.gxapi.GXTIN>` using the XY locations and uses the coefficients for the top layer on
        each layer below to make it efficient.

        `GXREG <geosoft.gxapi.GXREG>` Parameters:

        X0, Y0, Z0, DX, DY, DZ: Voxel origin, and cell sizes (required)
        NX, NY, NZ: Voxel dimensions.
        DZ and NZ are used only if the input cell sizes `GXVV <geosoft.gxapi.GXVV>` is of zero length.
        """
        gxapi_cy.WrapVOX._tin_grid_db(GXContext._get_tls_geo(), voxel.encode(), db, x, y, z, data, method, z_cell, reg)
        



    @classmethod
    def get_multi_voxset_guid(cls, voxel_file, p_uuid_string):
        """
        Get the UUID
        
        :param voxel_file:     Input Voxel file
        :param p_uuid_string:  UUID string returned
        :type  voxel_file:     str
        :type  p_uuid_string:  str_ref

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        p_uuid_string.value = gxapi_cy.WrapVOX._get_multi_voxset_guid(GXContext._get_tls_geo(), voxel_file.encode(), p_uuid_string.value.encode())
        



    @classmethod
    def generate_gocad(cls, name, header, property, ipj):
        """
        Generate a `GXVOX <geosoft.gxapi.GXVOX>` from a GOCAD File
        
        :param name:      Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param header:    Name of GOCAD Voxel file
        :param property:  Propert name to import
        :type  name:      str
        :type  header:    str
        :type  property:  str
        :type  ipj:       GXIPJ

        :returns:         `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:           GXVOX

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapVOX._generate_gocad(GXContext._get_tls_geo(), name.encode(), header.encode(), property.encode(), ipj)
        return GXVOX(ret_val)



    @classmethod
    def generate_oriented_gocad(cls, name, header, property, ipj, orientation):
        """
        Generate a `GXVOX <geosoft.gxapi.GXVOX>` from a GOCAD File
        
        :param name:         Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param header:       Name of GOCAD Voxel file
        :param property:     Propert name to import
        :param orientation:  :ref:`VOX_GOCAD_ORIENTATION`
        :type  name:         str
        :type  header:       str
        :type  property:     str
        :type  ipj:          GXIPJ
        :type  orientation:  int

        :returns:            `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:              GXVOX

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Allows the Orientation flag to be specified.
        """
        ret_val = gxapi_cy.WrapVOX._generate_oriented_gocad(GXContext._get_tls_geo(), name.encode(), header.encode(), property.encode(), ipj, orientation)
        return GXVOX(ret_val)



    @classmethod
    def generate_ubc(cls, name, mesh, mod, dummy, ipj):
        """
        Generate a `GXVOX <geosoft.gxapi.GXVOX>` from a UBC File
        
        :param name:   Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param mesh:   Name of UBC Mesh File
        :param mod:    Name of UBC Mod File
        :param dummy:  Dummy Value
        :param ipj:    Projection
        :type  name:   str
        :type  mesh:   str
        :type  mod:    str
        :type  dummy:  float
        :type  ipj:    GXIPJ

        :returns:      `GXVOX <geosoft.gxapi.GXVOX>` Object
        :rtype:        GXVOX

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapVOX._generate_ubc(GXContext._get_tls_geo(), name.encode(), mesh.encode(), mod.encode(), dummy, ipj)
        return GXVOX(ret_val)



    @classmethod
    def generate_xyz(cls, name, ra, type, ipj):
        """
        Generate a `GXVOX <geosoft.gxapi.GXVOX>` from an XYZ File
        
        :param name:  Voxel Name
        :param ra:    `GXRA <geosoft.gxapi.GXRA>` To import from
        :param type:  Data Type :ref:`GS_TYPES`
        :param ipj:   Projection
        :type  name:  str
        :type  ra:    GXRA
        :type  type:  int
        :type  ipj:   GXIPJ

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapVOX._generate_xyz(GXContext._get_tls_geo(), name.encode(), ra, type, ipj)
        



    @classmethod
    def list_gocad_properties(cls, header, lst):
        """
        List all the properties available in this GOCAD file.
        
        :param header:  Name of GOCAD Voxel file
        :param lst:     List object to populate
        :type  header:  str
        :type  lst:     GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapVOX._list_gocad_properties(GXContext._get_tls_geo(), header.encode(), lst)
        




    def export_db(self, db, chan, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export a Voxel to a database
        
        :param db:       Database
        :param chan:     Channel Name
        :param dir:      :ref:`VOX_DIRECTION`
        :param rev_x:    Reverse X ? (0/1)
        :param rev_y:    Reverse Y ? (0/1)
        :param rev_z:    Reverse Z ? (0/1)
        :param dummies:  Write Dummies? (0/1)
        :type  db:       GXDB
        :type  chan:     str
        :type  dir:      int
        :type  rev_x:    int
        :type  rev_y:    int
        :type  rev_z:    int
        :type  dummies:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The database lines contain a slice of the voxel at a time.
        """
        self._export_db(db, chan.encode(), dir, rev_x, rev_y, rev_z, dummies)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer