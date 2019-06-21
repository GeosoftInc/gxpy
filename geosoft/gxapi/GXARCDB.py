### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXDAT import GXDAT


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXARCDB(gxapi_cy.WrapARCDB):
    """
    GXARCDB class.

    The `GXARCDB <geosoft.gxapi.GXARCDB>` class is used in ArcGIS to access table contents from
    data sources and layers.
    """

    def __init__(self, handle=0):
        super(GXARCDB, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXARCDB <geosoft.gxapi.GXARCDB>`
        
        :returns: A null `GXARCDB <geosoft.gxapi.GXARCDB>`
        :rtype:   GXARCDB
        """
        return GXARCDB()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def create_dat(self, x_field, y_field, d_field):
        """
        Create a handle to a ARCGIS table `GXDAT <geosoft.gxapi.GXDAT>` 2D object
        
        :param x_field:  Name of X field in table
        :param y_field:  Name of Y field in table
        :param d_field:  Name of Data field in table
        :type  x_field:  str
        :type  y_field:  str
        :type  d_field:  str

        :returns:        `GXDAT <geosoft.gxapi.GXDAT>`, terminates if creation fails
        :rtype:          GXDAT

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._create_dat(x_field.encode(), y_field.encode(), d_field.encode())
        return GXDAT(ret_val)




    def create_dat_3d(self, x_field, y_field, z_field, d_field):
        """
        Create a handle to a ARCGIS table `GXDAT <geosoft.gxapi.GXDAT>` 3D object
        
        :param x_field:  Name of X field in table
        :param y_field:  Name of Y field in table
        :param z_field:  Name of Z field in table
        :param d_field:  Name of Data field in table
        :type  x_field:  str
        :type  y_field:  str
        :type  z_field:  str
        :type  d_field:  str

        :returns:        `GXDAT <geosoft.gxapi.GXDAT>`, terminates if creation fails
        :rtype:          GXDAT

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._create_dat_3d(x_field.encode(), y_field.encode(), z_field.encode(), d_field.encode())
        return GXDAT(ret_val)



    @classmethod
    def current(cls):
        """
        This method return a handle to the current table
        

        :returns:    `GXARCDB <geosoft.gxapi.GXARCDB>` Handle, `ARCDB_NULL <geosoft.gxapi.ARCDB_NULL>` if no table selected
        :rtype:      GXARCDB

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapARCDB._current(GXContext._get_tls_geo())
        return GXARCDB(ret_val)




    def export_to_db(self, db, temp, line):
        """
        Export data from an `GXARCDB <geosoft.gxapi.GXARCDB>` table into a group in a Geosoft GDB using a template.
        
        :param db:     Database
        :param temp:   Import template name
        :param line:   Oasis montaj line name to create (overrides template value)
        :type  db:     GXDB
        :type  temp:   str
        :type  line:   str

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. The import template can be in the local directory or the GEOSOFT
           directory.

        3. If the line already exists, the data will overwrite the existing data.
        """
        self._export_to_db(db, temp.encode(), line.encode())
        




    def field_lst(self, lst):
        """
        Place the list of field names in a `GXLST <geosoft.gxapi.GXLST>`.
        
        :type  lst:    GXLST

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If Z or M values are supported by the table geometry the strings
        "<Z Values>" and "<M Values>" will be added accordingly.
        """
        self._field_lst(lst)
        



    @classmethod
    def from_i_unknown(cls, unknown):
        """
        This method attempts to make a table handle from an IUnknown pointer

        Returns				 `GXARCDB <geosoft.gxapi.GXARCDB>` Handle, `ARCDB_NULL <geosoft.gxapi.ARCDB_NULL>` if not successful
        
        :param unknown:  IUnknown pointer
        :type  unknown:  int
        :rtype:          GXARCDB

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapARCDB._from_i_unknown(GXContext._get_tls_geo(), unknown)
        return GXARCDB(ret_val)




    def get_ipj(self, ipj):
        """
        Get georeference information from a table.
        
        :param ipj:    `GXIPJ <geosoft.gxapi.GXIPJ>` to fill in
        :type  ipj:    GXIPJ

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the table does not have an `GXIPJ <geosoft.gxapi.GXIPJ>`, the `GXIPJ <geosoft.gxapi.GXIPJ>` that is
        returned will have an unknown projection.
        """
        self._get_ipj(ipj)
        




    def exist_field(self, field):
        """
        This method checks to see if the specified field exists
        in the table.
        
        :param field:  Name of Field
        :type  field:  str

        :returns:      0 - Field does not exist
                       1 - Field Exists
        :rtype:        int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._exist_field(field.encode())
        return ret_val




    def get_i_unknown(self):
        """
        This method gets the IUnknown pointer
        

        :returns:      IUnknown pointer
        :rtype:        int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_i_unknown()
        return ret_val




    def import_chem_database_wizard(self, temp, type):
        """
        Template creation for importing geochem data.
        
        :param temp:   Template to make
        :param type:   :ref:`IMPCH_TYPE`
        :type  temp:   str
        :type  type:   int

        :returns:      0-OK 1-Cancel
        :rtype:        int

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._import_chem_database_wizard(temp.encode(), type)
        return ret_val



    @classmethod
    def sel_tbl_ex_gui(cls, table_type):
        """
        Select table `GXGUI <geosoft.gxapi.GXGUI>` with table type.
        
        :param table_type:  :ref:`ARC_SELTBL_TYPE`
        :type  table_type:  int_ref

        :returns:           Handle to the table (Terminate on Error)
        :rtype:             GXARCDB

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, table_type.value = gxapi_cy.WrapARCDB._sel_tbl_ex_gui(GXContext._get_tls_geo(), table_type.value)
        return GXARCDB(ret_val)



    @classmethod
    def sel_tbl_gui(cls):
        """
        Select table `GXGUI <geosoft.gxapi.GXGUI>`.
        

        :returns:    Handle to the table
        :rtype:      GXARCDB

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Terminates with Cancel on cancel, returns `ARCDB_NULL <geosoft.gxapi.ARCDB_NULL>` if there are no valid tables in current document.
        """
        ret_val = gxapi_cy.WrapARCDB._sel_tbl_gui(GXContext._get_tls_geo())
        return GXARCDB(ret_val)





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer