### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXMULTIGRID3D import GXMULTIGRID3D


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
    def export_to_segy(cls, multigrid3d_file, output_segy_filename, sample_interval):
        """
        Export To SEGY
        
        :param multigrid3d_file:      Input Voxel file
        :param output_segy_filename:  Output Segy file
        :param sample_interval:       Sampling Internal
        :type  multigrid3d_file:      str
        :type  output_segy_filename:  str
        :type  sample_interval:       float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._export_to_segy(GXContext._get_tls_geo(), multigrid3d_file.encode(), output_segy_filename.encode(), sample_interval)
        



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
    def convert_vector_to_double_using_rotation(cls, file_name, x_file_name, y_file_name, z_file_name, inclination, declination):
        """
        Convert a Vector Voxel to 3 double Voxels using an external rotation. Internal rotations are ignored.
        
        :param file_name:    Input Vector Voxel file
        :param x_file_name:  Output X Voxel file
        :param y_file_name:  Output Y Voxel file
        :param z_file_name:  Output Z Voxel file
        :param inclination:  Inclination
        :param declination:  Declination
        :type  file_name:    str
        :type  x_file_name:  str
        :type  y_file_name:  str
        :type  z_file_name:  str
        :type  inclination:  float
        :type  declination:  float

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._convert_vector_to_double_using_rotation(GXContext._get_tls_geo(), file_name.encode(), x_file_name.encode(), y_file_name.encode(), z_file_name.encode(), inclination, declination)
        



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
    def convert_double_to_thematic(cls, input_grid3d_filename, translate_vv, tpat, output_grid3d_filename):
        """
        Convert Double MultiVoxset to Thematic MultiVoxset
        
        :param input_grid3d_filename:   Input grid3d filename
        :param translate_vv:            Translation VV handle
        :param tpat:                    `GXTPAT <geosoft.gxapi.GXTPAT>` object
        :param output_grid3d_filename:  Output grid3d filename
        :type  input_grid3d_filename:   str
        :type  translate_vv:            GXVV
        :type  tpat:                    GXTPAT
        :type  output_grid3d_filename:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._convert_double_to_thematic(GXContext._get_tls_geo(), input_grid3d_filename.encode(), translate_vv, tpat, output_grid3d_filename.encode())
        



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
    def create_double_constant_copy(cls, name, value, source_name):
        """
        Generate a double MultiVoxset with a constant value based on an input voxel
        
        :param name:         Name of output Voxel File
        :param value:        Constant Value to use - DUMMY for a trully sparse grid3d
        :param source_name:  Name of voxel to model
        :type  name:         str
        :type  value:        float
        :type  source_name:  str

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._create_double_constant_copy(GXContext._get_tls_geo(), name.encode(), value, source_name.encode())
        



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
    def invert_z(cls, input_file, output_file):
        """
        Invert the Z values in the Grid3d.
        
        :param input_file:   Name of the input grid3d
        :param output_file:  Name of the output grid3d
        :type  input_file:   str
        :type  output_file:  str

        .. versionadded:: 9.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._invert_z(GXContext._get_tls_geo(), input_file.encode(), output_file.encode())
        



    @classmethod
    def extract_dem(cls, input_file, output_file):
        """
        Extract a DEM grid from a voxel.
        
        :param input_file:   Name of the input grid3d
        :param output_file:  Name of the output grid
        :type  input_file:   str
        :type  output_file:  str

        .. versionadded:: 9.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._extract_dem(GXContext._get_tls_geo(), input_file.encode(), output_file.encode())
        



    @classmethod
    def clip_to_polygon(cls, input_file, output_file, poly, clip_dummies):
        """
        Invert the Z values in the Grid3d.
        
        :param input_file:    Name of the input grid3d
        :param output_file:   Name of the output grid3d
        :param poly:          Polygons to clip to
        :param clip_dummies:  Clip Dummies (1) or leave them (0)
        :type  input_file:    str
        :type  output_file:   str
        :type  poly:          GXPLY
        :type  clip_dummies:  int

        .. versionadded:: 9.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._clip_to_polygon(GXContext._get_tls_geo(), input_file.encode(), output_file.encode(), poly, clip_dummies)
        



    @classmethod
    def generate_rbf(cls, db, output_file, data_channel, cell_size, error_tolerance, max_iterations, desample, kernel, kernel_epsilon):
        """
        Creates a VOXEL from an database using RBF.
        
        :param db:               Handle to a database
        :param output_file:      Name of the output grid3d
        :param data_channel:     Channel to grid`
        :param cell_size:        Cell size
        :param error_tolerance:  Error Tolerance
        :param max_iterations:   Maximum number of iterations (>0)
        :param desample:         Desample data (1) or use as is (0)
        :param kernel:           :ref:`RBFKERNEL`
        :param kernel_epsilon:   Kernel Epsilon
        :type  db:               GXDB
        :type  output_file:      str
        :type  data_channel:     str
        :type  cell_size:        float
        :type  error_tolerance:  float
        :type  max_iterations:   int
        :type  desample:         int
        :type  kernel:           int
        :type  kernel_epsilon:   float

        .. versionadded:: 9.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._generate_rbf(GXContext._get_tls_geo(), db, output_file.encode(), data_channel.encode(), cell_size, error_tolerance, max_iterations, desample, kernel, kernel_epsilon)
        



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
        



    @classmethod
    def grid_idw_from_gdb(cls, output_grid3d_filename, origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, db, x_channel, y_channel, z_channel, data_channel, weight_power, weight_slope, search_radius, blanking_distance, log, log_base, log_negative):
        """
        Create a grid3d using IDW gridding.
        
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
        :param db:                      Database
        :param x_channel:               X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_channel:               Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_channel:               Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param data_channel:            Data channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param weight_power:            Weight Power (default 2)
        :param weight_slope:            Weight Slope (default 1)
        :param search_radius:           Distance weighting limit (default = 4 * CUBE_ROOT(DX*DY*DZ))
        :param blanking_distance:       Dummy values farther from data than this distance. (default = 4 * CUBE_ROOT(DX*DY*DZ))
        :param log:                     Apply log transform to input data before gridding (0:No (default), 1:Yes)
        :param log_base:                One of `VV_LOG_BASE_10 <geosoft.gxapi.VV_LOG_BASE_10>` (default) or :const:`VV_LOG_BASE_E
        :param log_negative:            One of `VV_LOG_NEGATIVE_NO <geosoft.gxapi.VV_LOG_NEGATIVE_NO>` (default) or `VV_LOG_NEGATIVE_YES <geosoft.gxapi.VV_LOG_NEGATIVE_YES>`
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
        :type  db:                      GXDB
        :type  x_channel:               int
        :type  y_channel:               int
        :type  z_channel:               int
        :type  data_channel:            int
        :type  weight_power:            float
        :type  weight_slope:            float
        :type  search_radius:           float
        :type  blanking_distance:       float
        :type  log:                     int
        :type  log_base:                float
        :type  log_negative:            int

        .. versionadded:: 9.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The Z and Data channels may be array channels. If they are, the array sizes must match.
                          3D cells take on the averaged values within a search radius, weighted inversely by distance.

                       Weighting can be controlled using the power and slope properties;

                       weighting = 1 / (distance^wtpower + 1/slope) where distance is in
                       units of grid cells (X dimenstion). Default is 0.0,

                       If the blanking distance is set, all cells whose center point is not within the blanking distance of
                       at least one data point are set to dummy.
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._grid_idw_from_gdb(GXContext._get_tls_geo(), output_grid3d_filename.encode(), origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, db, x_channel, y_channel, z_channel, data_channel, weight_power, weight_slope, search_radius, blanking_distance, log, log_base, log_negative)
        



    @classmethod
    def get_data_extents(cls, filename, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the voxel size that has non-dummy data.
        
        :param filename:  input filename
        :param min_x:     Index of minimum valid data in X.
        :param min_y:     Index of minimum valid data in Y.
        :param min_z:     Index of minimum valid data in Z.
        :param max_x:     Index of maximum valid data in X.
        :param max_y:     Index of maximum valid data in Y.
        :param max_z:     Index of maximum valid data in Z.
        :type  filename:  str
        :type  min_x:     int_ref
        :type  min_y:     int_ref
        :type  min_z:     int_ref
        :type  max_x:     int_ref
        :type  max_y:     int_ref
        :type  max_z:     int_ref

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Find the non-dummy volume of a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` object. If the voxel is all dummies,
        returns `iMAX <geosoft.gxapi.iMAX>` for the minima, and `iMIN <geosoft.gxapi.iMIN>` for the maxima.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = gxapi_cy.WrapMULTIGRID3DUTIL._get_data_extents(GXContext._get_tls_geo(), filename.encode(), min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        



    @classmethod
    def get_data_ground_extents(cls, filename, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the voxel size in ground units that has non-dummy data.
        
        :param filename:  input filename
        :param min_x:     Ground location of minimum valid data in X.
        :param min_y:     Ground location of minimum valid data in Y.
        :param min_z:     Ground location of minimum valid data in Z.
        :param max_x:     Ground location of maximum valid data in X.
        :param max_y:     Ground location of maximum valid data in Y.
        :param max_z:     Ground location of maximum valid data in Z.
        :type  filename:  str
        :type  min_x:     float_ref
        :type  min_y:     float_ref
        :type  min_z:     float_ref
        :type  max_x:     float_ref
        :type  max_y:     float_ref
        :type  max_z:     float_ref

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Find the non-dummy volume of a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` object. If the voxel is all dummies,
        returns `iMAX <geosoft.gxapi.iMAX>` for the minima, and `iMIN <geosoft.gxapi.iMIN>` for the maxima.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = gxapi_cy.WrapMULTIGRID3DUTIL._get_data_ground_extents(GXContext._get_tls_geo(), filename.encode(), min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        



    @classmethod
    def grid_points_from_gdb(cls, name, error, cell_size, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, db, x_channel, y_channel, z_channel, data_channel, ipj):
        """
        Grid a grid3d from a database using kriging.
        
        :param name:          Output grid3d filename
        :param error:         Output error grid3d filename
        :param cell_size:     Cell size (DUMMY for default)
        :param var_only:      Variogram Only
        :param min_radius:    Minimum Search Radius (DUMMY for none)
        :param max_radius:    Maximum Search Radius (DUMMY for none)
        :param min_points:    Minimum Search Points
        :param max_points:    Maximum Search Points
        :param model:         Model number 1-power, 2-sperical, 3-gaussian, 4-exponential
        :param power:         Power
        :param slope:         Slope
        :param range:         Range
        :param nugget:        Nugget
        :param sill:          Sill
        :param type:          :ref:`GS_TYPES`
        :param db:            Database
        :param x_channel:     X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_channel:     Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_channel:     Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param data_channel:  Data channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :type  name:          str
        :type  error:         str
        :type  cell_size:     float
        :type  var_only:      int
        :type  min_radius:    float
        :type  max_radius:    float
        :type  min_points:    int
        :type  max_points:    int
        :type  model:         int
        :type  power:         float
        :type  slope:         float
        :type  range:         float
        :type  nugget:        float
        :type  sill:          float
        :type  type:          int
        :type  db:            GXDB
        :type  x_channel:     int
        :type  y_channel:     int
        :type  z_channel:     int
        :type  data_channel:  int
        :type  ipj:           GXIPJ

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._grid_points_from_gdb(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, db, x_channel, y_channel, z_channel, data_channel, ipj)
        



    @classmethod
    def grid_points_z_from_gdb(cls, name, error, cell_size, cell_size_z, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, db, x_channel, y_channel, z_channel, data_channel, ipj):
        """
        Grid a grid3d from a database (using variable Z's)
        
        :param name:          Output grid3d filename
        :param error:         Output error grid3d filename
        :param cell_size:     Cell size (DUMMY for default)
        :param cell_size_z:   Cell size in Z ("" for default)
        :param var_only:      Variogram Only
        :param min_radius:    Minimum Search Radius (DUMMY for none)
        :param max_radius:    Maximum Search Radius (DUMMY for none)
        :param min_points:    Minimum Search Points
        :param max_points:    Maximum Search Points
        :param model:         Model number 1-power, 2-sperical, 3-gaussian, 4-exponential
        :param power:         Power
        :param slope:         Slope
        :param range:         Range
        :param nugget:        Nugget
        :param sill:          Sill
        :param type:          :ref:`GS_TYPES`
        :param db:            Database
        :param x_channel:     X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_channel:     Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_channel:     Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param data_channel:  Data channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :type  name:          str
        :type  error:         str
        :type  cell_size:     float
        :type  cell_size_z:   str
        :type  var_only:      int
        :type  min_radius:    float
        :type  max_radius:    float
        :type  min_points:    int
        :type  max_points:    int
        :type  model:         int
        :type  power:         float
        :type  slope:         float
        :type  range:         float
        :type  nugget:        float
        :type  sill:          float
        :type  type:          int
        :type  db:            GXDB
        :type  x_channel:     int
        :type  y_channel:     int
        :type  z_channel:     int
        :type  data_channel:  int
        :type  ipj:           GXIPJ

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._grid_points_z_from_gdb(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, cell_size_z.encode(), var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, type, db, x_channel, y_channel, z_channel, data_channel, ipj)
        



    @classmethod
    def grid_points_z_ex_from_gdb(cls, name, error, cell_size, cell_size_z, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, strike, dip, plunge, along_strike_weight, down_dip_weight, type, db, x_channel, y_channel, z_channel, data_channel, ipj):
        """
        Grid a grid3d from a database (using variable Z's)
        
        :param name:                 Output grid3d filename
        :param error:                Output error grid3d filename
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
        :param db:                   Database
        :param x_channel:            X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_channel:            Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_channel:            Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param data_channel:         Data channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
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
        :type  db:                   GXDB
        :type  x_channel:            int
        :type  y_channel:            int
        :type  z_channel:            int
        :type  data_channel:         int
        :type  ipj:                  GXIPJ

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        slope.value, range.value, sill.value = gxapi_cy.WrapMULTIGRID3DUTIL._grid_points_z_ex_from_gdb(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, cell_size_z.encode(), var_only, min_radius, max_radius, min_points, max_points, model, power, slope.value, range.value, nugget, sill.value, strike, dip, plunge, along_strike_weight, down_dip_weight, type, db, x_channel, y_channel, z_channel, data_channel, ipj)
        



    @classmethod
    def log_grid_points_z_ex_from_gdb(cls, name, error, cell_size, cell_size_z, var_only, min_radius, max_radius, min_points, max_points, model, power, slope, range, nugget, sill, strike, dip, plunge, along_strike_weight, down_dip_weight, log_opt, min_log, type, db, x_channel, y_channel, z_channel, data_channel, ipj):
        """
        Log grid a grid3d from a database (using variable Z's)
        
        :param name:                 Output grid3d filename
        :param error:                Output error grid3d filename
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
        :param db:                   Database
        :param x_channel:            X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_channel:            Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_channel:            Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param data_channel:         Data channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
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
        :type  db:                   GXDB
        :type  x_channel:            int
        :type  y_channel:            int
        :type  z_channel:            int
        :type  data_channel:         int
        :type  ipj:                  GXIPJ

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        slope.value, range.value, sill.value = gxapi_cy.WrapMULTIGRID3DUTIL._log_grid_points_z_ex_from_gdb(GXContext._get_tls_geo(), name.encode(), error.encode(), cell_size, cell_size_z.encode(), var_only, min_radius, max_radius, min_points, max_points, model, power, slope.value, range.value, nugget, sill.value, strike, dip, plunge, along_strike_weight, down_dip_weight, log_opt, min_log, type, db, x_channel, y_channel, z_channel, data_channel, ipj)
        



    @classmethod
    def krig_from_gdb(cls, name, cell_size, type, db, x_channel, y_channel, z_channel, data_channel, ipj, reg):
        """
        A more compact and extensible form of `log_grid_points_z_ex_from_gdb <geosoft.gxapi.GXMULTIGRID3DUTIL.log_grid_points_z_ex_from_gdb>`.
        
        :param name:          Output grid3d filename
        :param cell_size:     Cell size (DUMMY for default)
        :param type:          :ref:`GS_TYPES`
        :param db:            Database
        :param x_channel:     X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_channel:     Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_channel:     Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param data_channel:  Data channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :type  name:          str
        :type  cell_size:     float
        :type  type:          int
        :type  db:            GXDB
        :type  x_channel:     int
        :type  y_channel:     int
        :type  z_channel:     int
        :type  data_channel:  int
        :type  ipj:           GXIPJ
        :type  reg:           GXREG

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Optional Parameters.

        If these values are not set in the `GXREG <geosoft.gxapi.GXREG>`, then default parameters will be used.

        ERROR_VOXEL:		Output error grid3d filename ("" for none)
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
        MAX_Z:				Maximum Z (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)A more compact and extensible form of `GXVOX.log_grid_points_z_ex <geosoft.gxapi.GXVOX.log_grid_points_z_ex>`. Only the most
        basic parameters are entered directly. Optional parameters are passed via a `GXREG <geosoft.gxapi.GXREG>` object.
        """
        gxapi_cy.WrapMULTIGRID3DUTIL._krig_from_gdb(GXContext._get_tls_geo(), name.encode(), cell_size, type, db, x_channel, y_channel, z_channel, data_channel, ipj, reg)
        



    @classmethod
    def create_subset(cls, input_name, output_name, offset_x, offset_y, offset_z, length_x, length_y, length_z):
        """
        Create a new MULTIGRID3D that is a subset of an exisiting MULTIGRID3D.
        
        :param input_name:   File Name of the MULTIGRID3D that will be subset
        :param output_name:  File Name of the MULTIGRID3D that will be created
        :param offset_x:     Starting location in X.
        :param offset_y:     Starting location in Y.
        :param offset_z:     Starting location in Z.
        :param length_x:     Number of items to copy in X.
        :param length_y:     Number of items to copy in Y.
        :param length_z:     Number of items to copy in Z.
        :type  input_name:   str
        :type  output_name:  str
        :type  offset_x:     int
        :type  offset_y:     int
        :type  offset_z:     int
        :type  length_x:     int
        :type  length_y:     int
        :type  length_z:     int
        :rtype:              GXMULTIGRID3D

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Creates a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` object that is a subset .
        """
        ret_val = gxapi_cy.WrapMULTIGRID3DUTIL._create_subset(GXContext._get_tls_geo(), input_name.encode(), output_name.encode(), offset_x, offset_y, offset_z, length_x, length_y, length_z)
        return GXMULTIGRID3D(ret_val)



    @classmethod
    def create_subset_from_double_extents(cls, input_name, output_name):
        """
        Create a new MULTIGRID3D that is a subset of the non-dummy extents.
        
        :param input_name:   File Name of the MULTIGRID3D that will be subset
        :param output_name:  File Name of the MULTIGRID3D that will be created
        :type  input_name:   str
        :type  output_name:  str
        :rtype:              GXMULTIGRID3D

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Creates a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` object that is a subset with all dummy data regions removed.
        """
        ret_val = gxapi_cy.WrapMULTIGRID3DUTIL._create_subset_from_double_extents(GXContext._get_tls_geo(), input_name.encode(), output_name.encode())
        return GXMULTIGRID3D(ret_val)





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer