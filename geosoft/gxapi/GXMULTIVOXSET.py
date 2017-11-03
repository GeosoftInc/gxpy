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
class GXMULTIVOXSET:
    """
    GXMULTIVOXSET class.

    High Performance 3D Grid.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMULTIVOXSET(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMULTIVOXSET`
        
        :returns: A null `GXMULTIVOXSET`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXMULTIVOXSET` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXMULTIVOXSET`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_xyz(GXContext._get_tls_geo(), name.encode(), ra._wrapper, type, ipj._wrapper)
        



    @classmethod
    def export_to_xyz(cls, voxel_file, xyz, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export a `GXMULTIVOXSET <geosoft.gxapi.GXMULTIVOXSET>` to an XYZ File
        
        :param voxel_file:  Input Voxel file
        :param xyz:         File Name
        :param dir:         :ref:`DIRECTION3D`
        :param rev_x:       Reverse X?
        :param rev_y:       Reverse Y?
        :param rev_z:       Reverse Z?
        :param dummies:     Write Dummies?
        :type  voxel_file:  str
        :type  xyz:         str
        :type  dir:         int
        :type  rev_x:       bool
        :type  rev_y:       bool
        :type  rev_z:       bool
        :type  dummies:     bool

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_xyz(GXContext._get_tls_geo(), voxel_file.encode(), xyz.encode(), dir, rev_x, rev_y, rev_z, dummies)
        



    @classmethod
    def export_to_binary(cls, voxel_file, binary_file, dir, rev_x, rev_y, rev_z, swap, output_type):
        """
        Export contents of `GXMULTIVOXSET <geosoft.gxapi.GXMULTIVOXSET>` to a Binary File.
        
        :param voxel_file:   Input Voxel file
        :param binary_file:  Binary file to write to
        :param dir:          :ref:`DIRECTION3D`
        :param rev_x:        Reverse X?
        :param rev_y:        Reverse Y?
        :param rev_z:        Reverse Z?
        :param swap:         Swap Bytes?
        :param output_type:  Output Type (Geosoft Type)
        :type  voxel_file:   str
        :type  binary_file:  str
        :type  dir:          int
        :type  rev_x:        bool
        :type  rev_y:        bool
        :type  rev_z:        bool
        :type  swap:         bool
        :type  output_type:  int

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_binary(GXContext._get_tls_geo(), voxel_file.encode(), binary_file.encode(), dir, rev_x, rev_y, rev_z, swap, output_type)
        



    @classmethod
    def export_to_xml(cls, voxel_file, xml_file):
        """
        Export a `GXMULTIVOXSET <geosoft.gxapi.GXMULTIVOXSET>` to XML
        
        :param voxel_file:  Voxel file
        :param xml_file:    XML file
        :type  voxel_file:  str
        :type  xml_file:    str

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_xml(GXContext._get_tls_geo(), voxel_file.encode(), xml_file.encode())
        



    @classmethod
    def check_equal_to_legacy_voxel(cls, voxel_file, legacy_voxel_file):
        """
        Compare `GXMULTIVOXSET <geosoft.gxapi.GXMULTIVOXSET>` to Legacy Voxel
        
        :param voxel_file:         Voxel file
        :param legacy_voxel_file:  Legacy Voxel file
        :type  voxel_file:         str
        :type  legacy_voxel_file:  str

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.check_equal_to_legacy_voxel(GXContext._get_tls_geo(), voxel_file.encode(), legacy_voxel_file.encode())
        



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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_ubc(GXContext._get_tls_geo(), name.encode(), mesh.encode(), mod.encode(), dummy, ipj._wrapper)
        



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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_gocad(GXContext._get_tls_geo(), name.encode(), header.encode(), property.encode(), ipj._wrapper, orientation)
        



    @classmethod
    def list_properties_gocad(cls, header, lst):
        """
        List all the properties available in this GOCAD file.
        
        :param header:  Name of GOCAD Voxel file
        :param lst:     List object to populate
        :type  header:  str
        :type  lst:     GXLST

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.list_properties_gocad(GXContext._get_tls_geo(), header.encode(), lst._wrapper)
        



    @classmethod
    def import_from_gdb(cls, voxel_file, db, symb):
        """
        Imports from a Geosoft Database
        
        :param voxel_file:  Name of output Voxel file
        :param db:          `GXDB <geosoft.gxapi.GXDB>` To import from
        :param symb:        Symbol to import data from
        :type  voxel_file:  str
        :type  db:          GXDB
        :type  symb:        int

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_gdb(GXContext._get_tls_geo(), voxel_file.encode(), db._wrapper, symb)
        



    @classmethod
    def import_from_vector_gdb(cls, voxel_file, db, vector_type, symb_x, symb_y, symb_z, inc, dec):
        """
        Imports from a Vector Geosoft Database
        
        :param voxel_file:   Voxel Name
        :param db:           `GXDB <geosoft.gxapi.GXDB>` To import from
        :param vector_type:  VECTOR_IMPORTImport XYZ, UVW or Amplitude/Inclination/Declination channels
        :param symb_x:       Symbol to import X, U or Amplitude data from
        :param symb_y:       Symbol to import Y, V or Inclination data from
        :param symb_z:       Symbol to import Z, W or Declination data from
        :param inc:          Inclination value for `VOX_VECTORVOX_UVW <geosoft.gxapi.VOX_VECTORVOX_UVW>` (-90° to 90°)
        :param dec:          Declination value for `VOX_VECTORVOX_UVW <geosoft.gxapi.VOX_VECTORVOX_UVW>` (-180° to 180°)
        :type  voxel_file:   str
        :type  db:           GXDB
        :type  vector_type:  int
        :type  symb_x:       int
        :type  symb_y:       int
        :type  symb_z:       int
        :type  inc:          float
        :type  dec:          float

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_vector_gdb(GXContext._get_tls_geo(), voxel_file.encode(), db._wrapper, vector_type, symb_x, symb_y, symb_z, inc, dec)
        



    @classmethod
    def export_to_segy(cls, voxel_file, voxel_name, output_segy_filename, sample_interval):
        """
        Export To SEGY
        
        :param voxel_file:            Input Voxel file
        :param voxel_name:            Voxel Name
        :param output_segy_filename:  Output Segy file
        :param sample_interval:       Sampling Internal
        :type  voxel_file:            str
        :type  voxel_name:            str
        :type  output_segy_filename:  str
        :type  sample_interval:       float

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_segy(GXContext._get_tls_geo(), voxel_file.encode(), voxel_name.encode(), output_segy_filename.encode(), sample_interval)
        



    @classmethod
    def export_to_gdb(cls, voxel_file, db, chan, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export To GDB
        
        :param voxel_file:  Input Voxel file
        :param db:          Database
        :param chan:        Channel Name
        :param dir:         :ref:`DIRECTION3D`
        :param rev_x:       Reverse X?
        :param rev_y:       Reverse Y?
        :param rev_z:       Reverse Z?
        :param dummies:     Write Dummies?
        :type  voxel_file:  str
        :type  db:          GXDB
        :type  chan:        str
        :type  dir:         int
        :type  rev_x:       bool
        :type  rev_y:       bool
        :type  rev_z:       bool
        :type  dummies:     bool

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_gdb(GXContext._get_tls_geo(), voxel_file.encode(), db._wrapper, chan.encode(), dir, rev_x, rev_y, rev_z, dummies)
        



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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_wa(GXContext._get_tls_geo(), file_name.encode(), wa._wrapper, dir, rev_x, rev_y, rev_z, dummy.encode())
        



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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.convert_double_to_vector(GXContext._get_tls_geo(), x_file_name.encode(), y_file_name.encode(), z_file_name.encode(), out_file_name.encode(), inclination, declination, rotated)
        



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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.convert_vector_to_double(GXContext._get_tls_geo(), file_name.encode(), x_file_name.encode(), y_file_name.encode(), z_file_name.encode(), rotated)
        



    @classmethod
    def create_double_constant(cls, name, value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj):
        """
        Generate a double MultiVoxset with a constant value
        
        :param name:    Name of output Voxel File
        :param value:   Constant Value to use - DUMMY for a trully sparse voxel
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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.create_double_constant(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj._wrapper)
        



    @classmethod
    def create_thematic_constant(cls, name, value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj):
        """
        Generate a double MultiVoxset with a constant value
        
        :param name:    Name of output Voxel File
        :param value:   Constant Value to use - DUMMY for a trully sparse voxel
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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.create_thematic_constant(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj._wrapper)
        



    @classmethod
    def create_vector_constant(cls, name, value_x, value_y, value_z, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj):
        """
        Generate a double MultiVoxset with a constant value
        
        :param name:     Name of output Voxel File
        :param value_x:  X Constant Value to use - DUMMY for a trully sparse voxel
        :param value_y:  Y Constant Value to use - DUMMY for a trully sparse voxel
        :param value_z:  Z Constant Value to use - DUMMY for a trully sparse voxel
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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.create_vector_constant(GXContext._get_tls_geo(), name.encode(), value_x, value_y, value_z, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj._wrapper)
        



    @classmethod
    def create_double_constant_vv(cls, name, value, ox, oy, oz, cx, cy, cz, ipj):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        
        :param name:   Name of output Voxel
        :param value:  The contant Value to fill with - DUMMY for a trully sparse voxel
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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.create_double_constant_vv(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cx._wrapper, cy._wrapper, cz._wrapper, ipj._wrapper)
        



    @classmethod
    def create_thematic_constant_vv(cls, name, value, ox, oy, oz, cx, cy, cz, ipj):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        
        :param name:   Name of output Voxel
        :param value:  The contant Value to fill with - DUMMY for a trully sparse voxel
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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.create_thematic_constant_vv(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cx._wrapper, cy._wrapper, cz._wrapper, ipj._wrapper)
        



    @classmethod
    def create_vector_constant_vv(cls, name, x_value, y_value, z_value, ox, oy, oz, cx, cy, cz, ipj):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        
        :param name:     Name of output Voxel
        :param x_value:  The X contant Value to fill with - DUMMY for a trully sparse voxel
        :param y_value:  The Y contant Value to fill with - DUMMY for a trully sparse voxel
        :param z_value:  The Z contant Value to fill with - DUMMY for a trully sparse voxel
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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.create_vector_constant_vv(GXContext._get_tls_geo(), name.encode(), x_value, y_value, z_value, ox, oy, oz, cx._wrapper, cy._wrapper, cz._wrapper, ipj._wrapper)
        



    @classmethod
    def export_to_voxel(cls, project_file, multi_voxset_uuid, multi_voxset_attribute, voxel_file):
        """
        Exports a Multi-Voxset into a Voxel
        
        :param project_file:            Project file
        :param multi_voxset_uuid:       Multi-Voxset UUID
        :param multi_voxset_attribute:  Multi-Voxset attribute
        :param voxel_file:              Output Voxel file
        :type  project_file:            str
        :type  multi_voxset_uuid:       str
        :type  multi_voxset_attribute:  str
        :type  voxel_file:              str

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_voxel(GXContext._get_tls_geo(), project_file.encode(), multi_voxset_uuid.encode(), multi_voxset_attribute.encode(), voxel_file.encode())
        



    @classmethod
    def import_from_voxel(cls, project_file, voxel_file, multi_voxset_attribute, p_uuid_string):
        """
        Import a Voxel directly into a Multi-Voxset
        
        :param project_file:            Project file
        :param voxel_file:              Input Voxel file
        :param multi_voxset_attribute:  Multi-Voxset attribute
        :param p_uuid_string:           UUID string returned
        :type  project_file:            str
        :type  voxel_file:              str
        :type  multi_voxset_attribute:  str
        :type  p_uuid_string:           str_ref

        .. versionadded:: 9.3
        """
        p_uuid_string.value = gxapi_cy.WrapMULTIVOXSET.import_from_voxel(GXContext._get_tls_geo(), project_file.encode(), voxel_file.encode(), multi_voxset_attribute.encode(), p_uuid_string.value.encode())
        



    @classmethod
    def import_from_datamine(cls, file, field, ipj, voxel):
        """
        Create a Geosoft Voxel file from a Datamine block model file.
        
        :param file:   Datamine file name
        :param field:  Field to use for data
        :param ipj:    Projection to set
        :param voxel:  Output voxel file name
        :type  file:   str
        :type  field:  str
        :type  ipj:    GXIPJ
        :type  voxel:  str

        .. versionadded:: 9.3

        **Note:**

        Create a Geosoft Voxel file from a Datamine block model file.
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_datamine(GXContext._get_tls_geo(), file.encode(), field.encode(), ipj._wrapper, voxel.encode())
        



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

        .. versionadded:: 9.3

        **Note:**

        Compute a default cell size for a voxel given a data range.
        """
        ret_val = gxapi_cy.WrapMULTIVOXSET.compute_default_cell_size(GXContext._get_tls_geo(), min_x, max_x, min_y, max_y, min_z, max_z)
        return ret_val



    @classmethod
    def filter(cls, input_file, output_file, filter, filter_file, n_passes, interpolate_dummies):
        """
        Apply a 3D filter to a voxel.
        
        :param input_file:           Name of the input voxel
        :param output_file:          Name of the output voxel
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

        .. versionadded:: 9.3
        """
        gxapi_cy.WrapMULTIVOXSET.filter(GXContext._get_tls_geo(), input_file.encode(), output_file.encode(), filter, filter_file.encode(), n_passes, interpolate_dummies)
        



    @classmethod
    def grid_direct_from_gdb(cls, output_voxel_filename, origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, method, db, x_channel, y_channel, z_channel, data_channel):
        """
        Create a voxel using direct gridding.
        
        :param output_voxel_filename:  Output voxel filename
        :param origin_x:               Voxel origin X
        :param origin_y:               Voxel origin Y
        :param origin_z:               Voxel origin Z
        :param cell_count_x:           Voxel cell count X
        :param cell_count_y:           Voxel cell count Y
        :param cell_count_z:           Voxel cell count Z
        :param cell_size_x:            Voxel cell size X
        :param cell_size_y:            Voxel cell size Y
        :param cell_size_z:            Voxel cell size Z
        :param method:                 :ref:`MULTIVOXSET_DIRECTGRID_METHOD`
        :param db:                     Database
        :param x_channel:              X channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param y_channel:              Y channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param z_channel:              Z channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :param data_channel:           Data channel [`DB_LOCK_READONLY <geosoft.gxapi.DB_LOCK_READONLY>`]
        :type  output_voxel_filename:  str
        :type  origin_x:               float
        :type  origin_y:               float
        :type  origin_z:               float
        :type  cell_count_x:           int
        :type  cell_count_y:           int
        :type  cell_count_z:           int
        :type  cell_size_x:            float
        :type  cell_size_y:            float
        :type  cell_size_z:            float
        :type  method:                 int
        :type  db:                     GXDB
        :type  x_channel:              int
        :type  y_channel:              int
        :type  z_channel:              int
        :type  data_channel:           int

        .. versionadded:: 9.3

        **Note:**

        The Z and Data channels may be array channels. If they are, the array sizes must match.
        """
        gxapi_cy.WrapMULTIVOXSET.grid_direct_from_gdb(GXContext._get_tls_geo(), output_voxel_filename.encode(), origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, method, db._wrapper, x_channel, y_channel, z_channel, data_channel)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer