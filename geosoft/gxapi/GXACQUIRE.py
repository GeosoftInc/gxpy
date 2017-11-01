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
class GXACQUIRE:
    """
    GXACQUIRE class.

    This class is used to import acQuire data. It uses the
    public acQuire API.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapACQUIRE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXACQUIRE`
        
        :returns: A null `GXACQUIRE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXACQUIRE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXACQUIRE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls):
        """
        Create an acQuire object
        

        :returns:    acQuire Object
        :rtype:      GXACQUIRE

        .. versionadded:: 6.0
        """
        ret_val = gxapi_cy.WrapACQUIRE.create(GXContext._get_tls_geo())
        return GXACQUIRE(ret_val)




    def delete_empty_chan(self, db):
        """
        Delete empty channels
        
        :param db:     Database
        :type  db:     GXDB

        .. versionadded:: 6.0
        """
        self._wrapper.delete_empty_chan(db._wrapper)
        






    def import_hole(self, proj, dir, para, geo_vv, delete, convert):
        """
        Import Drillhole data acQuire database into a GDB
        
        :param proj:     Project name
        :param dir:      Project directory
        :param para:     Parameter File
        :param geo_vv:   List of geology name database
        :param delete:   0: Write to existing databases (overwrite holes), 1: Delete existing databases.
        :param convert:  Convert Negatives (0,1)
        :type  proj:     str
        :type  dir:      str
        :type  para:     str
        :type  geo_vv:   GXVV
        :type  delete:   int
        :type  convert:  int

        :returns:        0 - Ok
                         1 - Error (Will not stop GX)
        :rtype:          int

        .. versionadded:: 6.0.1

        **Note:**

        Point data and polygon data are saved into Dnnn lines in GDB,
        nnn representing incremental number starting from 0
        """
        ret_val = self._wrapper.import_hole(proj.encode(), dir.encode(), para.encode(), geo_vv._wrapper, delete, convert)
        return ret_val




    def import_point(self, db, para, convert):
        """
        Import Point Sample data acQuire database into a GDB
        
        :param db:       Geosoft GDB
        :param para:     Parameter File
        :param convert:  Convert Negatives (0,1)
        :type  db:       GXDB
        :type  para:     str
        :type  convert:  int

        :returns:        0 - Ok
                         1 - Error (Will not stop GX)
        :rtype:          int

        .. versionadded:: 6.0.1

        **Note:**

        Data existing in the receiving GDB file will be over-written.
        Point data and polygon data are saved into Dnnn lines in GDB,
        nnn representing incremental number starting from 0
        """
        ret_val = self._wrapper.import_point(db._wrapper, para.encode(), convert)
        return ret_val




    def selection_tool(self, selection_file, mode):
        """
        Run the acQuire Selection Tool.
        
        :param selection_file:  Selection File Name
        :param mode:            :ref:`ACQUIRE_SEL`
        :type  selection_file:  str
        :type  mode:            int

        :returns:               0 - Ok
                                1 - if user cancels
        :rtype:                 int

        .. versionadded:: 6.0.1

        **Note:**

        The selection file will be loaded (if present) and then
        the user can make selections then the selections are saved
        back in the selection file.
        """
        ret_val = self._wrapper.selection_tool(selection_file.encode(), mode)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer