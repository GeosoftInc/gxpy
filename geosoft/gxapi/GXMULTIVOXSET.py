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
        A null (undefined) instance of :class:`geosoft.gxapi.GXMULTIVOXSET`
        
        :returns: A null :class:`geosoft.gxapi.GXMULTIVOXSET`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXMULTIVOXSET` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXMULTIVOXSET`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def import_from_xyz(cls, p1, p2, p3, p4):
        """
        Import XYZ file into a Multi-Voxset
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_xyz(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4._wrapper)
        



    @classmethod
    def export_to_xyz(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Export a :class:`geosoft.gxapi.GXMULTIVOXSET` to an XYZ File
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_xyz(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4, p5, p6, p7)
        



    @classmethod
    def export_to_binary(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Export contents of :class:`geosoft.gxapi.GXMULTIVOXSET` to a Binary File.
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_binary(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def export_to_xml(cls, p1, p2):
        """
        Export a :class:`geosoft.gxapi.GXMULTIVOXSET` to XML
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_xml(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def check_equal_to_legacy_voxel(cls, p1, p2):
        """
        Compare :class:`geosoft.gxapi.GXMULTIVOXSET` to Legacy Voxel
        """
        gxapi_cy.WrapMULTIVOXSET.check_equal_to_legacy_voxel(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def import_from_ubc(cls, p1, p2, p3, p4, p5):
        """
        Import UBC file into a MultiVoxset
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_ubc(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4, p5._wrapper)
        



    @classmethod
    def import_from_gocad(cls, p1, p2, p3, p4, p5):
        """
        Imports a MultiVoxset from a GOCAD File
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_gocad(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4._wrapper, p5)
        



    @classmethod
    def list_properties_gocad(cls, p1, p2):
        """
        List all the properties available in this GOCAD file.
        """
        gxapi_cy.WrapMULTIVOXSET.list_properties_gocad(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        



    @classmethod
    def import_from_gdb(cls, p1, p2, p3):
        """
        Imports from a Geosoft Database
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_gdb(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3)
        



    @classmethod
    def import_from_vector_gdb(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Imports from a Vector Geosoft Database
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_vector_gdb(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def export_to_segy(cls, p1, p2, p3, p4):
        """
        Export To SEGY
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_segy(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4)
        



    @classmethod
    def export_to_gdb(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Export To GDB
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_gdb(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3.encode(), p4, p5, p6, p7, p8)
        



    @classmethod
    def export_to_wa(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Export To GDB
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_wa(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7.encode())
        



    @classmethod
    def convert_double_to_vector(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Convert 3 Double Voxels to a Vector Voxel
        """
        gxapi_cy.WrapMULTIVOXSET.convert_double_to_vector(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5, p6, p7)
        



    @classmethod
    def convert_vector_to_double(cls, p1, p2, p3, p4):
        """
        Convert a Vector Voxel to 3 double Voxels
        """
        gxapi_cy.WrapMULTIVOXSET.convert_vector_to_double(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def create_double_constant(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Generate a double MultiVoxset with a constant value
        """
        gxapi_cy.WrapMULTIVOXSET.create_double_constant(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper)
        



    @classmethod
    def create_thematic_constant(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Generate a double MultiVoxset with a constant value
        """
        gxapi_cy.WrapMULTIVOXSET.create_thematic_constant(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper)
        



    @classmethod
    def create_vector_constant(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Generate a double MultiVoxset with a constant value
        """
        gxapi_cy.WrapMULTIVOXSET.create_vector_constant(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14._wrapper)
        



    @classmethod
    def create_double_constant_vv(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        """
        gxapi_cy.WrapMULTIVOXSET.create_double_constant_vv(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        



    @classmethod
    def create_thematic_constant_vv(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        """
        gxapi_cy.WrapMULTIVOXSET.create_thematic_constant_vv(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        



    @classmethod
    def create_vector_constant_vv(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Generate a double MultiVoxset with a constant value and non-uniform cell sizes
        """
        gxapi_cy.WrapMULTIVOXSET.create_vector_constant_vv(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper)
        



    @classmethod
    def export_to_voxel(cls, p1, p2, p3, p4):
        """
        Exports a Multi-Voxset into a Voxel
        """
        gxapi_cy.WrapMULTIVOXSET.export_to_voxel(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def import_from_voxel(cls, p1, p2, p3, p4):
        """
        Import a Voxel directly into a Multi-Voxset
        """
        p4.value = gxapi_cy.WrapMULTIVOXSET.import_from_voxel(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.value.encode())
        



    @classmethod
    def import_from_datamine(cls, p1, p2, p3, p4):
        """
        Create a Geosoft Voxel file from a Datamine block model file.

        **Note:**

        Create a Geosoft Voxel file from a Datamine block model file.
        """
        gxapi_cy.WrapMULTIVOXSET.import_from_datamine(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4.encode())
        



    @classmethod
    def compute_default_cell_size(cls, p1, p2, p3, p4, p5, p6):
        """
        Used if the user does not provide a default cell size.

        **Note:**

        Compute a default cell size for a voxel given a data range.
        """
        ret_val = gxapi_cy.WrapMULTIVOXSET.compute_default_cell_size(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6)
        return ret_val



    @classmethod
    def filter(cls, p1, p2, p3, p4, p5, p6):
        """
        Apply a 3D filter to a voxel.
        """
        gxapi_cy.WrapMULTIVOXSET.filter(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4.encode(), p5, p6)
        



    @classmethod
    def grid_direct_from_gdb(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16):
        """
        Create a voxel using direct gridding.

        **Note:**

        The Z and Data channels may be array channels. If they are, the array sizes must match.
        """
        gxapi_cy.WrapMULTIVOXSET.grid_direct_from_gdb(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper, p13, p14, p15, p16)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer