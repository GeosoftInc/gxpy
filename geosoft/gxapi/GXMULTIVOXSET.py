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
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_xyz(GXContext._get_tls_geo(), name.encode(), ra._wrapper, type, ipj._wrapper)
        



    @classmethod
    def export_to_xyz(cls, voxel_file, xyz, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export a `GXMULTIVOXSET <geosoft.gxapi.GXMULTIVOXSET>` to an XYZ File
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_xyz(GXContext._get_tls_geo(), voxel_file.encode(), xyz.encode(), dir, rev_x, rev_y, rev_z, dummies)
        



    @classmethod
    def export_to_binary(cls, voxel_file, binary_file, dir, rev_x, rev_y, rev_z, swap, output_type):
        """
        Export contents of `GXMULTIVOXSET <geosoft.gxapi.GXMULTIVOXSET>` to a Binary File.
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_binary(GXContext._get_tls_geo(), voxel_file.encode(), binary_file.encode(), dir, rev_x, rev_y, rev_z, swap, output_type)
        



    @classmethod
    def export_to_xml(cls, voxel_file, xml_file):
        """
        Export a `GXMULTIVOXSET <geosoft.gxapi.GXMULTIVOXSET>` to XML
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_xml(GXContext._get_tls_geo(), voxel_file.encode(), xml_file.encode())
        



    @classmethod
    def check_equal_to_legacy_voxel(cls, voxel_file, legacy_voxel_file):
        """
        Compare `GXMULTIVOXSET <geosoft.gxapi.GXMULTIVOXSET>` to Legacy Voxel
        """
        gxapi_cy.WrapMULTIVOXSET.check_equal_to_legacy_voxel(GXContext._get_tls_geo(), voxel_file.encode(), legacy_voxel_file.encode())
        



    @classmethod
    def import_from_ubc(cls, name, mesh, mod, dummy, ipj):
        """
        Import UBC file into a MultiVoxset
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_ubc(GXContext._get_tls_geo(), name.encode(), mesh.encode(), mod.encode(), dummy, ipj._wrapper)
        



    @classmethod
    def import_from_gocad(cls, name, header, property, ipj, orientation):
        """
        Imports a MultiVoxset from a GOCAD File
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_gocad(GXContext._get_tls_geo(), name.encode(), header.encode(), property.encode(), ipj._wrapper, orientation)
        



    @classmethod
    def list_properties_gocad(cls, header, lst):
        """
        List all the properties available in this GOCAD file.
        """
        gxapi_cy.WrapMULTIVOXSET.list_properties_gocad(GXContext._get_tls_geo(), header.encode(), lst._wrapper)
        



    @classmethod
    def import_from_gdb(cls, voxel_file, db, symb):
        """
        Imports from a Geosoft Database
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_gdb(GXContext._get_tls_geo(), voxel_file.encode(), db._wrapper, symb)
        



    @classmethod
    def import_from_vector_gdb(cls, voxel_file, db, vector_type, symb_x, symb_y, symb_z, inc, dec):
        """
        Imports from a Vector Geosoft Database
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_vector_gdb(GXContext._get_tls_geo(), voxel_file.encode(), db._wrapper, vector_type, symb_x, symb_y, symb_z, inc, dec)
        



    @classmethod
    def export_to_segy(cls, voxel_file, voxel_name, output_segy_filename, sample_interval):
        """
        Export To SEGY
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_segy(GXContext._get_tls_geo(), voxel_file.encode(), voxel_name.encode(), output_segy_filename.encode(), sample_interval)
        



    @classmethod
    def export_to_gdb(cls, voxel_file, db, chan, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export To GDB
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_gdb(GXContext._get_tls_geo(), voxel_file.encode(), db._wrapper, chan.encode(), dir, rev_x, rev_y, rev_z, dummies)
        



    @classmethod
    def export_to_wa(cls, file_name, wa, dir, rev_x, rev_y, rev_z, dummy):
        """
        Export To GDB
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_wa(GXContext._get_tls_geo(), file_name.encode(), wa._wrapper, dir, rev_x, rev_y, rev_z, dummy.encode())
        



    @classmethod
    def convert_double_to_vector(cls, x_file_name, y_file_name, z_file_name, out_file_name, inclination, declination, rotated):
        """
        Convert 3 Double Voxels to a Vector Voxel
        """
        gxapi_cy.WrapMULTIVOXSET.convert_double_to_vector(GXContext._get_tls_geo(), x_file_name.encode(), y_file_name.encode(), z_file_name.encode(), out_file_name.encode(), inclination, declination, rotated)
        



    @classmethod
    def convert_vector_to_double(cls, file_name, x_file_name, y_file_name, z_file_name):
        """
        Convert a Vector Voxel to 3 double Voxels
        """
        gxapi_cy.WrapMULTIVOXSET.convert_vector_to_double(GXContext._get_tls_geo(), file_name.encode(), x_file_name.encode(), y_file_name.encode(), z_file_name.encode())
        



    @classmethod
    def create_double_constant(cls, name, value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj):
        """
        Generate a double MultiVoxset with a constant value
        """
        gxapi_cy.WrapMULTIVOXSET.create_double_constant(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj._wrapper)
        



    @classmethod
    def create_thematic_constant(cls, name, value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj):
        """
        Generate a double MultiVoxset with a constant value
        """
        gxapi_cy.WrapMULTIVOXSET.create_thematic_constant(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj._wrapper)
        



    @classmethod
    def create_vector_constant(cls, name, value_x, value_y, value_z, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj):
        """
        Generate a double MultiVoxset with a constant value
        """
        gxapi_cy.WrapMULTIVOXSET.create_vector_constant(GXContext._get_tls_geo(), name.encode(), value_x, value_y, value_z, ox, oy, oz, cell_x, cell_y, cell_z, size_x, size_y, size_z, ipj._wrapper)
        



    @classmethod
    def create_double_constant_vv(cls, name, value, ox, oy, oz, cx, cy, cz, ipj):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        """
        gxapi_cy.WrapMULTIVOXSET.create_double_constant_vv(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cx._wrapper, cy._wrapper, cz._wrapper, ipj._wrapper)
        



    @classmethod
    def create_thematic_constant_vv(cls, name, value, ox, oy, oz, cx, cy, cz, ipj):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        """
        gxapi_cy.WrapMULTIVOXSET.create_thematic_constant_vv(GXContext._get_tls_geo(), name.encode(), value, ox, oy, oz, cx._wrapper, cy._wrapper, cz._wrapper, ipj._wrapper)
        



    @classmethod
    def create_vector_constant_vv(cls, name, x_value, y_value, z_value, ox, oy, oz, cx, cy, cz, ipj):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        """
        gxapi_cy.WrapMULTIVOXSET.create_vector_constant_vv(GXContext._get_tls_geo(), name.encode(), x_value, y_value, z_value, ox, oy, oz, cx._wrapper, cy._wrapper, cz._wrapper, ipj._wrapper)
        



    @classmethod
    def export_to_voxel(cls, project_file, multi_voxset_uuid, multi_voxset_attribute, voxel_file):
        """
        Exports a Multi-Voxset into a Voxel
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_voxel(GXContext._get_tls_geo(), project_file.encode(), multi_voxset_uuid.encode(), multi_voxset_attribute.encode(), voxel_file.encode())
        



    @classmethod
    def import_from_voxel(cls, project_file, voxel_file, multi_voxset_attribute, p_uuid_string):
        """
        Import a Voxel directly into a Multi-Voxset
        """
        p_uuid_string.value = gxapi_cy.WrapMULTIVOXSET.import_from_voxel(GXContext._get_tls_geo(), project_file.encode(), voxel_file.encode(), multi_voxset_attribute.encode(), p_uuid_string.value.encode())
        



    @classmethod
    def import_from_datamine(cls, file, field, ipj, voxel):
        """
        Create a Geosoft Voxel file from a Datamine block model file.

        **Note:**

        Create a Geosoft Voxel file from a Datamine block model file.
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_datamine(GXContext._get_tls_geo(), file.encode(), field.encode(), ipj._wrapper, voxel.encode())
        



    @classmethod
    def compute_default_cell_size(cls, min_x, max_x, min_y, max_y, min_z, max_z):
        """
        Used if the user does not provide a default cell size.

        **Note:**

        Compute a default cell size for a voxel given a data range.
        """
        ret_val = gxapi_cy.WrapMULTIVOXSET.compute_default_cell_size(GXContext._get_tls_geo(), min_x, max_x, min_y, max_y, min_z, max_z)
        return ret_val



    @classmethod
    def filter(cls, input_file, output_file, filter, filter_file, n_passes, interpolate_dummies):
        """
        Apply a 3D filter to a voxel.
        """
        gxapi_cy.WrapMULTIVOXSET.filter(GXContext._get_tls_geo(), input_file.encode(), output_file.encode(), filter, filter_file.encode(), n_passes, interpolate_dummies)
        



    @classmethod
    def grid_direct_from_gdb(cls, output_voxel_filename, origin_x, origin_y, origin_z, cell_count_x, cell_count_y, cell_count_z, cell_size_x, cell_size_y, cell_size_z, method, db, x_channel, y_channel, z_channel, data_channel):
        """
        Create a voxel using direct gridding.

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