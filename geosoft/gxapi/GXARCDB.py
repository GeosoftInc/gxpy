### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXDAT import GXDAT


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXARCDB:
    """
    GXARCDB class.

    The `GXARCDB` class is used in ArcGIS to access table contents from
    data sources and layers.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapARCDB(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXARCDB`
        
        :returns: A null `GXARCDB`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXARCDB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXARCDB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def create_dat(self, x_field, y_field, d_field):
        """
        Create a handle to a ARCGIS table `GXDAT` 2D object
        """
        ret_val = self._wrapper.create_dat(x_field.encode(), y_field.encode(), d_field.encode())
        return GXDAT(ret_val)




    def create_dat_3d(self, x_field, y_field, z_field, d_field):
        """
        Create a handle to a ARCGIS table `GXDAT` 3D object
        """
        ret_val = self._wrapper.create_dat_3d(x_field.encode(), y_field.encode(), z_field.encode(), d_field.encode())
        return GXDAT(ret_val)



    @classmethod
    def current(cls):
        """
        This method return a handle to the current table
        """
        ret_val = gxapi_cy.WrapARCDB.current(GXContext._get_tls_geo())
        return GXARCDB(ret_val)




    def export_to_db(self, db, temp, line):
        """
        Export data from an `GXARCDB` table into a group in a Geosoft GDB using a template.

        **Note:**

        1. The import template can be in the local directory or the GEOSOFT
           directory.
        
        3. If the line already exists, the data will overwrite the existing data.
        """
        self._wrapper.export_to_db(db._wrapper, temp.encode(), line.encode())
        




    def field_lst(self, lst):
        """
        Place the list of field names in a `GXLST`.

        **Note:**

        If Z or M values are supported by the table geometry the strings
        "<Z Values>" and "<M Values>" will be added accordingly.
        """
        self._wrapper.field_lst(lst._wrapper)
        



    @classmethod
    def from_i_unknown(cls, unknown):
        """
        This method attempts to make a table handle from an IUnknown pointer
        
        Returns				 `GXARCDB` Handle, `ARCDB_NULL` if not successful
        """
        ret_val = gxapi_cy.WrapARCDB.from_i_unknown(GXContext._get_tls_geo(), unknown)
        return GXARCDB(ret_val)




    def get_ipj(self, ipj):
        """
        Get georeference information from a table.

        **Note:**

        If the table does not have an `GXIPJ`, the `GXIPJ` that is
        returned will have an unknown projection.
        """
        self._wrapper.get_ipj(ipj._wrapper)
        




    def exist_field(self, field):
        """
        This method checks to see if the specified field exists
        in the table.
        """
        ret_val = self._wrapper.exist_field(field.encode())
        return ret_val




    def get_i_unknown(self):
        """
        This method gets the IUnknown pointer
        """
        ret_val = self._wrapper.get_i_unknown()
        return ret_val




    def import_chem_database_wizard(self, temp, type):
        """
        Template creation for importing geochem data.
        """
        ret_val = self._wrapper.import_chem_database_wizard(temp.encode(), type)
        return ret_val



    @classmethod
    def sel_tbl_ex_gui(cls, table_type):
        """
        Select table `GXGUI` with table type.
        """
        ret_val, table_type.value = gxapi_cy.WrapARCDB.sel_tbl_ex_gui(GXContext._get_tls_geo(), table_type.value)
        return GXARCDB(ret_val)



    @classmethod
    def sel_tbl_gui(cls):
        """
        Select table `GXGUI`.

        **Note:**

        Terminates with Cancel on cancel, returns `ARCDB_NULL` if there are no valid tables in current document.
        """
        ret_val = gxapi_cy.WrapARCDB.sel_tbl_gui(GXContext._get_tls_geo())
        return GXARCDB(ret_val)





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer