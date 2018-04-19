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
class GXMULTIGRID3DUTIL(gxapi_cy.WrapMULTIGRID3DUTIL):
    """
    GXMULTIGRID3DUTIL class.

    High Performance 3D Grid.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMULTIGRID3DUTIL <geosoft.gxapi.GXMULTIGRID3DUTIL>`
        
        :returns: A null `GXMULTIGRID3DUTIL <geosoft.gxapi.GXMULTIGRID3DUTIL>`
        :rtype:   GXMULTIGRID3DUTIL
        """
        return GXMULTIGRID3DUTIL()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def import_from_xyz(cls, name, ra, type, ipj):
        """
        Import XYZ file into a Multi-Voxset
        
        :param name:  Name of output Voxel file
        :param ra:    `GXRA <geosoft.gxapi.GXRA>` To import from
        :param type:  Data Type :ref:`GS_TYPES`
        :param ipj:   Projection
        :type  name:  str
        :type  ra:    GXRA
        :type  type:  int
        :type  ipj:   GXIPJ

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._import_from_xyz(GXContext._get_tls_geo(), name.encode(), ra, type, ipj)
        



    @classmethod
    def export_to_xyz(cls, grid3d_file, xyz, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to an XYZ File
        
        :param grid3d_file:  Input Voxel file
        :param xyz:          File Name
        :param dir:          :ref:`DIRECTION3D`
        :param rev_x:        Reverse X?
        :param rev_y:        Reverse Y?
        :param rev_z:        Reverse Z?
        :param dummies:      Write Dummies?
        :type  grid3d_file:  str
        :type  xyz:          str
        :type  dir:          int
        :type  rev_x:        bool
        :type  rev_y:        bool
        :type  rev_z:        bool
        :type  dummies:      bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._export_to_xyz(GXContext._get_tls_geo(), grid3d_file.encode(), xyz.encode(), dir, rev_x, rev_y, rev_z, dummies)
        



    @classmethod
    def export_to_binary(cls, grid3d_file, binary_file, dir, rev_x, rev_y, rev_z, swap, output_type):
        """
        Export contents of `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to a Binary File.
        
        :param grid3d_file:  Input Voxel file
        :param binary_file:  Binary file to write to
        :param dir:          :ref:`DIRECTION3D`
        :param rev_x:        Reverse X?
        :param rev_y:        Reverse Y?
        :param rev_z:        Reverse Z?
        :param swap:         Swap Bytes?
        :param output_type:  Output Type (Geosoft Type)
        :type  grid3d_file:  str
        :type  binary_file:  str
        :type  dir:          int
        :type  rev_x:        bool
        :type  rev_y:        bool
        :type  rev_z:        bool
        :type  swap:         bool
        :type  output_type:  int

        .. versionadded:: 9.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._export_to_binary(GXContext._get_tls_geo(), grid3d_file.encode(), binary_file.encode(), dir, rev_x, rev_y, rev_z, swap, output_type)
        



    @classmethod
    def export_to_xml(cls, grid3d_file, xml_file):
        """
        Export a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to XML
        
        :param grid3d_file:  Voxel file
        :param xml_file:     XML file
        :type  grid3d_file:  str
        :type  xml_file:     str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._export_to_xml(GXContext._get_tls_geo(), grid3d_file.encode(), xml_file.encode())
        



    @classmethod
    def check_equal_to_legacy_voxel(cls, grid3d_file, legacy_grid3d_file):
        """
        Compare `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to Legacy Voxel
        
        :param grid3d_file:         Voxel file
        :param legacy_grid3d_file:  Legacy Voxel file
        :type  grid3d_file:         str
        :type  legacy_grid3d_file:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._check_equal_to_legacy_voxel(GXContext._get_tls_geo(), grid3d_file.encode(), legacy_grid3d_file.encode())
        



    @classmethod
    def import_from_ubc(cls, name, mesh, mod, dummy, ipj):
        """
        Import UBC file into a MultiVoxset
        
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

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._import_from_ubc(GXContext._get_tls_geo(), name.encode(), mesh.encode(), mod.encode(), dummy, ipj)
        



    @classmethod
    def import_from_gocad(cls, name, header, property, ipj, orientation):
        """
        Imports a MultiVoxset from a GOCAD File
        
        :param name:         Name of output `GXVOX <geosoft.gxapi.GXVOX>`
        :param header:       Name of GOCAD Voxel file
        :param property:     Propert name to import
        :param orientation:  :ref:`GOCAD_ORIENTATION`
        :type  name:         str
        :type  header:       str
        :type  property:     str
        :type  ipj:          GXIPJ
        :type  orientation:  int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._import_from_gocad(GXContext._get_tls_geo(), name.encode(), header.encode(), property.encode(), ipj, orientation)
        



    @classmethod
    def list_properties_gocad(cls, header, lst):
        """
        List all the properties available in this GOCAD file.
        
        :param header:  Name of GOCAD Voxel file
        :param lst:     List object to populate
        :type  header:  str
        :type  lst:     GXLST

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._list_properties_gocad(GXContext._get_tls_geo(), header.encode(), lst)
        



    @classmethod
    def import_from_gdb(cls, grid3d_file, db, symb):
        """
        Imports from a Geosoft Database
        
        :param grid3d_file:  Name of output Voxel file
        :param db:           `GXDB <geosoft.gxapi.GXDB>` To import from
        :param symb:         Symbol to import data from
        :type  grid3d_file:  str
        :type  db:           GXDB
        :type  symb:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._import_from_gdb(GXContext._get_tls_geo(), grid3d_file.encode(), db, symb)
        



    @classmethod
    def import_from_vector_gdb(cls, grid3d_file, db, vector_type, symb_x, symb_y, symb_z, inc, dec):
        """
        Imports from a Vector Geosoft Database
        
        :param grid3d_file:  Voxel Name
        :param db:           `GXDB <geosoft.gxapi.GXDB>` To import from
        :param vector_type:  VECTOR_IMPORTImport XYZ, UVW or Amplitude/Inclination/Declination channels
        :param symb_x:       Symbol to import X, U or Amplitude data from
        :param symb_y:       Symbol to import Y, V or Inclination data from
        :param symb_z:       Symbol to import Z, W or Declination data from
        :param inc:          Inclination value for `VOX_VECTORVOX_UVW <geosoft.gxapi.VOX_VECTORVOX_UVW>` (-90° to 90°)
        :param dec:          Declination value for `VOX_VECTORVOX_UVW <geosoft.gxapi.VOX_VECTORVOX_UVW>` (-180° to 180°)
        :type  grid3d_file:  str
        :type  db:           GXDB
        :type  vector_type:  int
        :type  symb_x:       int
        :type  symb_y:       int
        :type  symb_z:       int
        :type  inc:          float
        :type  dec:          float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._import_from_vector_gdb(GXContext._get_tls_geo(), grid3d_file.encode(), db, vector_type, symb_x, symb_y, symb_z, inc, dec)
        



    @classmethod
    def export_to_segy(cls, grid3d_file, grid3d_name, output_segy_filename, sample_interval):
        """
        Export To SEGY
        
        :param grid3d_file:           Input Voxel file
        :param grid3d_name:           Voxel Name
        :param output_segy_filename:  Output Segy file
        :param sample_interval:       Sampling Internal
        :type  grid3d_file:           str
        :type  grid3d_name:           str
        :type  output_segy_filename:  str
        :type  sample_interval:       float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._export_to_segy(GXContext._get_tls_geo(), grid3d_file.encode(), grid3d_name.encode(), output_segy_filename.encode(), sample_interval)
        



    @classmethod
    def export_to_gdb(cls, grid3d_file, db, chan, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export To GDB
        
        :param grid3d_file:  Input Voxel file
        :param db:           Database
        :param chan:         Channel Name
        :param dir:          :ref:`DIRECTION3D`
        :param rev_x:        Reverse X?
        :param rev_y:        Reverse Y?
        :param rev_z:        Reverse Z?
        :param dummies:      Write Dummies?
        :type  grid3d_file:  str
        :type  db:           GXDB
        :type  chan:         str
        :type  dir:          int
        :type  rev_x:        bool
        :type  rev_y:        bool
        :type  rev_z:        bool
        :type  dummies:      bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._export_to_gdb(GXContext._get_tls_geo(), grid3d_file.encode(), db, chan.encode(), dir, rev_x, rev_y, rev_z, dummies)
        



    @classmethod
    def export_to_wa(cls, file_name, wa, dir, rev_x, rev_y, rev_z, dummy):
        """
        Export To GDB
        
        :param file_name:  Input Voxel file
        :param wa:         `GXWA <geosoft.gxapi.GXWA>` File
        :param dir:        :ref:`DIRECTION3D`
        :param rev_x:      Reverse X?
        :param rev_y:      Reverse Y?
        :param rev_z:      Reverse Z?
        :param dummy:      The Dummy string to write
        :type  file_name:  str
        :type  wa:         GXWA
        :type  dir:        int
        :type  rev_x:      bool
        :type  rev_y:      bool
        :type  rev_z:      bool
        :type  dummy:      str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._export_to_wa(GXContext._get_tls_geo(), file_name.encode(), wa, dir, rev_x, rev_y, rev_z, dummy.encode())
        



    @classmethod
    def convert_double_to_vector(cls, x_file_name, y_file_name, z_file_name, out_file_name, inclination, declination, rotated):
        """
        Convert 3 Double Voxels to a Vector Voxel
        
        :param x_file_name:    Input X Voxel file
        :param y_file_name:    Input Y Voxel file
        :param z_file_name:    Input Z Voxel file
        :param out_file_name:  Output Vector Voxel file
        :param inclination:    Inclination
        :param declination:    Declination
        :param rotated:        Rotated?
        :type  x_file_name:    str
        :type  y_file_name:    str
        :type  z_file_name:    str
        :type  out_file_name:  str
        :type  inclination:    float
        :type  declination:    float
        :type  rotated:        bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._convert_double_to_vector(GXContext._get_tls_geo(), x_file_name.encode(), y_file_name.encode(), z_file_name.encode(), out_file_name.encode(), inclination, declination, rotated)
        



    @classmethod
    def convert_vector_to_double(cls, file_name, x_file_name, y_file_name, z_file_name, rotated):
        """
        Convert a Vector Voxel to 3 double Voxels
        
        :param file_name:    Input Vector Voxel file
        :param x_file_name:  Output X Voxel file
        :param y_file_name:  Output Y Voxel file
        :param z_file_name:  Output Z Voxel file
        :param rotated:      Rotated?
        :type  file_name:    str
        :type  x_file_name:  str
        :type  y_file_name:  str
        :type  z_file_name:  str
        :type  rotated:      bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._convert_vector_to_double(GXContext._get_tls_geo(), file_name.encode(), x_file_name.encode(), y_file_name.encode(), z_file_name.encode(), rotated)
        



    @classmethod
    def convert_thematic_to_double(cls, input_grid3d_filename, translate_vv, output_grid3d_filename):
        """
        Convert Thematic MultiVoxset to Double MultiVoxset
        
        :param input_grid3d_filename:   Input grid3d filename
        :param translate_vv:            Translation VV handle
        :param output_grid3d_filename:  Output grid3d filename
        :type  input_grid3d_filename:   str
        :type  translate_vv:            GXVV
        :type  output_grid3d_filename:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._convert_thematic_to_double(GXContext._get_tls_geo(), input_grid3d_filename.encode(), translate_vv, output_grid3d_filename.encode())
        



    @classmethod
    def convert_double_to_thematic(cls, input_grid3d_filename, translate_vv, output_grid3d_filename):
        """
        Convert Double MultiVoxset to Thematic MultiVoxset
        
        :param input_grid3d_filename:   Input grid3d filename
        :param translate_vv:            Translation VV handle
        :param output_grid3d_filename:  Output grid3d filename
        :type  input_grid3d_filename:   str
        :type  translate_vv:            GXVV
        :type  output_grid3d_filename:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._convert_double_to_thematic(GXContext._get_tls_geo(), input_grid3d_filename.encode(), translate_vv, output_grid3d_filename.encode())
        



    @classmethod
    def convert_velocity_to_density(cls, input_grid3d_filename, input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_grid3d_filename):
        """
        Convert Velocity MultiVoxset to Density MultiVoxset
        
        :param input_grid3d_filename:   Input grid3d filename
        :param input_scaling_factor:    1.0, if this grid3d is in meters per second. Otherwise, a value by which each input cell is multiplied to convert it into meters per second.
        :param input_lower_bound:       Lower bound on velocity values, in meters per second. If the input value (after being pre-multiplied by dInputScalingFactor) is less than this value, the output cell value will be DUMMY.
        :param input_upper_bound:       Upper bound on velocity values, in meters per second. If the input value (after being pre-multiplied by dInputScalingFactor) is greater than this value, the output cell value will be DUMMY.
        :param a5:                      Coefficient of fifth-order polynomial term.
        :param a4:                      Coefficient of fourth-order polynomial term.
        :param a3:                      Coefficient of third-order polynomial term.
        :param a2:                      Coefficient of second-order polynomial term.
        :param a1:                      Coefficient of first-order polynomial term.
        :param a0:                      Constant offset of output.
        :param output_scaling_factor:   1.0, to produce an output grid3d that has units of g/cm^3. If different units are desired, pass in a different value, which will be multiplied into each output grid3d cell.
        :param output_grid3d_filename:  Output grid3d filename
        :type  input_grid3d_filename:   str
        :type  input_scaling_factor:    float
        :type  input_lower_bound:       float
        :type  input_upper_bound:       float
        :type  a5:                      float
        :type  a4:                      float
        :type  a3:                      float
        :type  a2:                      float
        :type  a1:                      float
        :type  a0:                      float
        :type  output_scaling_factor:   float
        :type  output_grid3d_filename:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._convert_velocity_to_density(GXContext._get_tls_geo(), input_grid3d_filename.encode(), input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_grid3d_filename.encode())
        



    @classmethod
    def convert_density_to_velocity(cls, input_grid3d_filename, input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_grid3d_filename):
        """
        Convert Density MultiVoxset to Velocity MultiVoxset
        
        :param input_grid3d_filename:   Input grid3d filename
        :param input_scaling_factor:    1.0, if this grid3d is in meters per second. Otherwise, a value by which each input cell is multiplied to convert it into meters per second.
        :param input_lower_bound:       Lower bound on velocity values, in meters per second. If the input value (after being pre-multiplied by dInputScalingFactor) is less than this value, the output cell value will be DUMMY.
        :param input_upper_bound:       Upper bound on velocity values, in meters per second. If the input value (after being pre-multiplied by dInputScalingFactor) is greater than this value, the output cell value will be DUMMY.
        :param a5:                      Coefficient of fifth-order polynomial term.
        :param a4:                      Coefficient of fourth-order polynomial term.
        :param a3:                      Coefficient of third-order polynomial term.
        :param a2:                      Coefficient of second-order polynomial term.
        :param a1:                      Coefficient of first-order polynomial term.
        :param a0:                      Constant offset of output.
        :param output_scaling_factor:   1.0, to produce an output grid3d that has units of g/cm^3. If different units are desired, pass in a different value, which will be multiplied into each output grid3d cell.
        :param output_grid3d_filename:  Output grid3d filename
        :type  input_grid3d_filename:   str
        :type  input_scaling_factor:    float
        :type  input_lower_bound:       float
        :type  input_upper_bound:       float
        :type  a5:                      float
        :type  a4:                      float
        :type  a3:                      float
        :type  a2:                      float
        :type  a1:                      float
        :type  a0:                      float
        :type  output_scaling_factor:   float
        :type  output_grid3d_filename:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._convert_density_to_velocity(GXContext._get_tls_geo(), input_grid3d_filename.encode(), input_scaling_factor, input_lower_bound, input_upper_bound, a5, a4, a3, a2, a1, a0, output_scaling_factor, output_grid3d_filename.encode())
        



    @classmethod
    def get_gocad_location(cls, input_grid3d_filename, origin_x, origin_y, origin_z, vect_xx, vect_xy, vect_xz, vect_yx, vect_yy, vect_yz, vect_zx, vect_zy, vect_zz):
        """
        Get the location of a grid3d with origin and scaled xyz vectors for use with GOCAD.
        
        :param input_grid3d_filename:  Input grid3d filename
        :param origin_x:               Origin X
        :param origin_y:               Origin Y
        :param origin_z:               Origin Z
        :param vect_xx:                VectX X
        :param vect_xy:                VectX Y
        :param vect_xz:                VectX Z
        :param vect_yx:                VectY X
        :param vect_yy:                VectY Y
        :param vect_yz:                VectY Z
        :param vect_zx:                VectZ X
        :param vect_zy:                VectZ Y
        :param vect_zz:                VectZ Z
        :type  input_grid3d_filename:  str
        :type  origin_x:               float_ref
        :type  origin_y:               float_ref
        :type  origin_z:               float_ref
        :type  vect_xx:                float_ref
        :type  vect_xy:                float_ref
        :type  vect_xz:                float_ref
        :type  vect_yx:                float_ref
        :type  vect_yy:                float_ref
        :type  vect_yz:                float_ref
        :type  vect_zx:                float_ref
        :type  vect_zy:                float_ref
        :type  vect_zz:                float_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        origin_x.value, origin_y.value, origin_z.value, vect_xx.value, vect_xy.value, vect_xz.value, vect_yx.value, vect_yy.value, vect_yz.value, vect_zx.value, vect_zy.value, vect_zz.value = gxapi_cy.WrapMULTIGRID3DUTIL._get_gocad_location(GXContext._get_tls_geo(), input_grid3d_filename.encode(), origin_x.value, origin_y.value, origin_z.value, vect_xx.value, vect_xy.value, vect_xz.value, vect_yx.value, vect_yy.value, vect_yz.value, vect_zx.value, vect_zy.value, vect_zz.value)
        



    @classmethod
    def create_double_constant(cls, name, value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj):
        """
        Generate a double MultiVoxset with a constant value
        
        :param name:    Name of output Voxel File
        :param value:   Constant Value to use - DUMMY for a trully sparse grid3d
        :param ox:      Origin X
        :param oy:      Origin Y
        :param oz:      Origin Z
        :param cell_x:  Cell Size X
        :param cell_y:  Cell Size Y
        :param cell_z:  Cell Size Z
        :param size_x:  Cell Count X
        :param size_y:  Cell Count Y
        :param size_z:  Cell Count Z
        :param ipj:     Projection
        :type  name:    str
        :type  value:   float
        :type  ox:      float
        :type  oy:      float
        :type  oz:      float
        :type  cell_x:  float
        :type  cell_y:  float
        :type  cell_z:  float
        :type  size_x:  int
        :type  size_y:  int
        :type  size_z:  int
        :type  ipj:     GXIPJ

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._create_double_constant(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj)
        



    @classmethod
    def create_thematic_constant(cls, name, value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj):
        """
        Generate a double MultiVoxset with a constant value
        
        :param name:    Name of output Voxel File
        :param value:   Constant Value to use - DUMMY for a trully sparse grid3d
        :param ox:      Origin X
        :param oy:      Origin Y
        :param oz:      Origin Z
        :param cell_x:  Cell Size X
        :param cell_y:  Cell Size Y
        :param cell_z:  Cell Size Z
        :param size_x:  Cell Count X
        :param size_y:  Cell Count Y
        :param size_z:  Cell Count Z
        :param ipj:     Projection
        :type  name:    str
        :type  value:   int
        :type  ox:      float
        :type  oy:      float
        :type  oz:      float
        :type  cell_x:  float
        :type  cell_y:  float
        :type  cell_z:  float
        :type  size_x:  int
        :type  size_y:  int
        :type  size_z:  int
        :type  ipj:     GXIPJ

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._create_thematic_constant(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj)
        



    @classmethod
    def create_vector_constant(cls, name, value_x, value_y, value_z, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj):
        """
        Generate a double MultiVoxset with a constant value
        
        :param name:     Name of output Voxel File
        :param value_x:  X Constant Value to use - DUMMY for a trully sparse grid3d
        :param value_y:  Y Constant Value to use - DUMMY for a trully sparse grid3d
        :param value_z:  Z Constant Value to use - DUMMY for a trully sparse grid3d
        :param ox:       Origin X
        :param oy:       Origin Y
        :param oz:       Origin Z
        :param cell_x:   Cell Size X
        :param cell_y:   Cell Size Y
        :param cell_z:   Cell Size Z
        :param size_x:   Cell Count X
        :param size_y:   Cell Count Y
        :param size_z:   Cell Count Z
        :param ipj:      Projection
        :type  name:     str
        :type  value_x:  float
        :type  value_y:  float
        :type  value_z:  float
        :type  ox:       float
        :type  oy:       float
        :type  oz:       float
        :type  cell_x:   float
        :type  cell_y:   float
        :type  cell_z:   float
        :type  size_x:   int
        :type  size_y:   int
        :type  size_z:   int
        :type  ipj:      GXIPJ

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._create_vector_constant(GXContext._get_tls_geo(), name.encode(), value_x, value_y, value_z, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj)
        



    @classmethod
    def create_double_constant_vv(cls, name, value, ox, oy, oz, cx, cy, cz, ipj):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        
        :param name:   Name of output Voxel
        :param value:  The contant Value to fill with - DUMMY for a trully sparse grid3d
        :param ox:     Origin X
        :param oy:     Origin Y
        :param oz:     Origin Z
        :param cx:     Cell Sizes X
        :param cy:     Cell Sizes Y
        :param cz:     Cell Sizes Z
        :param ipj:    Projection
        :type  name:   str
        :type  value:  float
        :type  ox:     float
        :type  oy:     float
        :type  oz:     float
        :type  cx:     GXVV
        :type  cy:     GXVV
        :type  cz:     GXVV
        :type  ipj:    GXIPJ

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._create_double_constant_vv(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cx, cy, cz, ipj)
        



    @classmethod
    def create_thematic_constant_vv(cls, name, value, ox, oy, oz, cx, cy, cz, ipj):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        
        :param name:   Name of output Voxel
        :param value:  The contant Value to fill with - DUMMY for a trully sparse grid3d
        :param ox:     Origin X
        :param oy:     Origin Y
        :param oz:     Origin Z
        :param cx:     Cell Sizes X
        :param cy:     Cell Sizes Y
        :param cz:     Cell Sizes Z
        :param ipj:    Projection
        :type  name:   str
        :type  value:  int
        :type  ox:     float
        :type  oy:     float
        :type  oz:     float
        :type  cx:     GXVV
        :type  cy:     GXVV
        :type  cz:     GXVV
        :type  ipj:    GXIPJ

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._create_thematic_constant_vv(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cx, cy, cz, ipj)
        



    @classmethod
    def create_vector_constant_vv(cls, name, x_value, y_value, z_value, ox, oy, oz, cx, cy, cz, ipj):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        
        :param name:     Name of output Voxel
        :param x_value:  The X contant Value to fill with - DUMMY for a trully sparse grid3d
        :param y_value:  The Y contant Value to fill with - DUMMY for a trully sparse grid3d
        :param z_value:  The Z contant Value to fill with - DUMMY for a trully sparse grid3d
        :param ox:       Origin X
        :param oy:       Origin Y
        :param oz:       Origin Z
        :param cx:       Cell Sizes X
        :param cy:       Cell Sizes Y
        :param cz:       Cell Sizes Z
        :param ipj:      Projection
        :type  name:     str
        :type  x_value:  float
        :type  y_value:  float
        :type  z_value:  float
        :type  ox:       float
        :type  oy:       float
        :type  oz:       float
        :type  cx:       GXVV
        :type  cy:       GXVV
        :type  cz:       GXVV
        :type  ipj:      GXIPJ

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._create_vector_constant_vv(GXContext._get_tls_geo(), name.encode(), x_value, y_value, z_value, ox, oy, oz, cx, cy, cz, ipj)
        



    @classmethod
    def export_to_voxel(cls, project_file, multi_voxset_uuid, multi_voxset_attribute, grid3d_file):
        """
        Exports a Multi-Voxset into a Voxel
        
        :param project_file:            Project file
        :param multi_voxset_uuid:       Multi-Voxset UUID
        :param multi_voxset_attribute:  Multi-Voxset attribute
        :param grid3d_file:             Output Voxel file
        :type  project_file:            str
        :type  multi_voxset_uuid:       str
        :type  multi_voxset_attribute:  str
        :type  grid3d_file:             str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._export_to_voxel(GXContext._get_tls_geo(), project_file.encode(), multi_voxset_uuid.encode(), multi_voxset_attribute.encode(), grid3d_file.encode())
        



    @classmethod
    def import_from_voxel(cls, project_file, grid3d_file, multi_voxset_attribute, p_uuid_string):
        """
        Import a Voxel directly into a Multi-Voxset
        
        :param project_file:            Project file
        :param grid3d_file:             Input Voxel file
        :param multi_voxset_attribute:  Multi-Voxset attribute
        :param p_uuid_string:           UUID string returned
        :type  project_file:            str
        :type  grid3d_file:             str
        :type  multi_voxset_attribute:  str
        :type  p_uuid_string:           str_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        p_uuid_string.value = gxapi_cy.WrapMULTIGRID3DUTIL._import_from_voxel(GXContext._get_tls_geo(), project_file.encode(), grid3d_file.encode(), multi_voxset_attribute.encode(), p_uuid_string.value.encode())
        



    @classmethod
    def import_from_datamine(cls, file, field, ipj, grid3d):
        """
        Create a Geosoft Voxel file from a Datamine block model file.
        
        :param file:    Datamine file name
        :param field:   Field to use for data
        :param ipj:     Projection to set
        :param grid3d:  Output grid3d file name
        :type  file:    str
        :type  field:   str
        :type  ipj:     GXIPJ
        :type  grid3d:  str

        .. versionadded:: 9.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Create a Geosoft Voxel file from a Datamine block model file.
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._import_from_datamine(GXContext._get_tls_geo(), file.encode(), field.encode(), ipj, grid3d.encode())
        



    @classmethod
    def compute_default_cell_size(cls, min_x, max_x, min_y, max_y, min_z, max_z):
        """
        Used if the user does not provide a default cell size.
        
        :param min_x:  MinX
        :param max_x:  MaxX
        :param min_y:  MinY
        :param max_y:  MaxY
        :param min_z:  MinZ
        :param max_z:  MaxZ
        :type  min_x:  float
        :type  max_x:  float
        :type  min_y:  float
        :type  max_y:  float
        :type  min_z:  float
        :type  max_z:  float

        :returns:      Default Cell Size
        :rtype:        float

        .. versionadded:: 9.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Compute a default cell size for a grid3d given a data range.
        """
        ret_val = gxapi_cy.WrapMULTIGRID3DUTIL._compute_default_cell_size(GXContext._get_tls_geo(), min_x, max_x, min_y, max_y, min_z, max_z)
        return ret_val



    @classmethod
    def filter(cls, input_file, output_file, filter, filter_file, n_passes, interpolate_dummies):
        """
        Apply a 3D filter to a grid3d.
        
        :param input_file:           Name of the input grid3d
        :param output_file:          Name of the output grid3d
        :param filter:               :ref:`FILTER3D`
        :param filter_file:          Filter file, if filter is `VOX_FILTER3D_FILE <geosoft.gxapi.VOX_FILTER3D_FILE>`
        :param n_passes:             Number of filter passes
        :param interpolate_dummies:  (1: interpolate dummies)
        :type  input_file:           str
        :type  output_file:          str
        :type  filter:               int
        :type  filter_file:          str
        :type  n_passes:             int
        :type  interpolate_dummies:  int

        .. versionadded:: 9.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._filter(GXContext._get_tls_geo(), input_file.encode(), output_file.encode(), filter, filter_file.encode(), n_passes, interpolate_dummies)
        



    @classmethod
    def generate_rbf_surface(cls, db, output_file, data_channel, isosurface_value, error_tolerance, max_iterations, desample, kernel, kernel_epsilon):
        """
        Creates a surface from an database using RBF.
        
        :param db:                Handle to a database
        :param output_file:       Name of the output grid3d
        :param data_channel:      Channel to grid`
        :param isosurface_value:  Isosurface value
        :param error_tolerance:   Error Tolerance
        :param max_iterations:    Maximum number of iterations (>0)
        :param desample:          Desample data (1) or use as is (0)
        :param kernel:            :ref:`RBFKERNEL`
        :param kernel_epsilon:    Kernel Epsilon
        :type  db:                GXDB
        :type  output_file:       str
        :type  data_channel:      str
        :type  isosurface_value:  float
        :type  error_tolerance:   float
        :type  max_iterations:    int
        :type  desample:          int
        :type  kernel:            int
        :type  kernel_epsilon:    float

        .. versionadded:: 9.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._generate_rbf_surface(GXContext._get_tls_geo(), db, output_file.encode(), data_channel.encode(), isosurface_value, error_tolerance, max_iterations, desample, kernel, kernel_epsilon)
        



    @classmethod
    def grid_direct_from_gdb(cls, output_grid3d_filename, origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, method, db, x_channel, y_channel, z_channel, data_channel):
        """
        Create a grid3d using direct gridding.
        
        :param output_grid3d_filename:  Output grid3d filename
        :param origin_x:                Voxel origin X
        :param origin_y:                Voxel origin Y
        :param origin_z:                Voxel origin Z
        :param cell_count_x:            Voxel cell count X
        :param cell_count_y:            Voxel cell count Y
        :param cell_count_z:            Voxel cell count Z
        :param cell_size_x:             Voxel cell size X
        :param cell_size_y:             Voxel cell size Y
        :param cell_size_z:             Voxel cell size Z
        :param method:                  :ref:`MULTIGRID3D_DIRECTGRID_METHOD`
        :param db:                      Database
        :param x_channel:               X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_channel:               Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_channel:               Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param data_channel:            Data channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :type  output_grid3d_filename:  str
        :type  origin_x:                float
        :type  origin_y:                float
        :type  origin_z:                float
        :type  cell_count_x:            int
        :type  cell_count_y:            int
        :type  cell_count_z:            int
        :type  cell_size_x:             float
        :type  cell_size_y:             float
        :type  cell_size_z:             float
        :type  method:                  int
        :type  db:                      GXDB
        :type  x_channel:               int
        :type  y_channel:               int
        :type  z_channel:               int
        :type  data_channel:            int

        .. versionadded:: 9.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The Z and Data channels may be array channels. If they are, the array sizes must match.
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._grid_direct_from_gdb(GXContext._get_tls_geo(), output_grid3d_filename.encode(), origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, method, db, x_channel, y_channel, z_channel, data_channel)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer