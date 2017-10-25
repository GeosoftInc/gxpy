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
class GXSBF:
    """
    GXSBF class.

    The :class:`geosoft.gxapi.GXSBF` class provides a means of storing data in a
    file-type directory structure within a workspace, database
    or map. Each of these three objects contains its own :class:`geosoft.gxapi.GXSBF` object,
    which may be accessed using the hGetSYS_SBF, hGetDB_SBF and
    hGetMAP_SBF functions. To access data in a file, or create a
    new file in the :class:`geosoft.gxapi.GXSBF` object, call the CreatSBF_BF function (see :class:`geosoft.gxapi.GXBF`),
    which will return a :class:`geosoft.gxapi.GXBF` object to use.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSBF(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXSBF`
        
        :returns: A null :class:`geosoft.gxapi.GXSBF`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXSBF` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXSBF`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def create(self, p2, p3):
        """
        Create a child :class:`geosoft.gxapi.GXSBF` object inside an :class:`geosoft.gxapi.GXSBF`.
        """
        ret_val = self._wrapper.create(p2.encode(), p3)
        return GXSBF(ret_val)




    def create_obj_list(self, p2, p3):
        """
        Fills an :class:`geosoft.gxapi.GXLST` with embedded storage names of an :class:`geosoft.gxapi.GXSBF`.

        **Note:**

        Function will populate an :class:`geosoft.gxapi.GXLST` object with embedded files (:attr:`geosoft.gxapi.SBF_TYPE_FILES`),
        directories (:attr:`geosoft.gxapi.SBF_TYPE_DIRS`), or both (pass :attr:`geosoft.gxapi.SBF_TYPE_BOTH`) in an :class:`geosoft.gxapi.GXSBF`.
        Along with the Name of the file or directory, a constant "dir" or "file" string is written
        to the :class:`geosoft.gxapi.GXLST` also.
        """
        self._wrapper.create_obj_list(p2._wrapper, p3)
        




    def del_dir(self, p2):
        """
        Delete a directory (storage) from this storage.
        """
        self._wrapper.del_dir(p2.encode())
        




    def del_file(self, p2):
        """
        Delete a file from this storage.
        """
        self._wrapper.del_file(p2.encode())
        





    @classmethod
    def h_get_db(cls, p1):
        """
        Get the embedded file storage from a database.
        """
        ret_val = gxapi_cy.WrapSBF.h_get_db(GXContext._get_tls_geo(), p1._wrapper)
        return GXSBF(ret_val)



    @classmethod
    def h_get_map(cls, p1):
        """
        Get the embedded file storage from a map.
        """
        ret_val = gxapi_cy.WrapSBF.h_get_map(GXContext._get_tls_geo(), p1._wrapper)
        return GXSBF(ret_val)



    @classmethod
    def h_get_sys(cls):
        """
        Get the main embedded file storage (in workspace).
        """
        ret_val = gxapi_cy.WrapSBF.h_get_sys(GXContext._get_tls_geo())
        return GXSBF(ret_val)




    def exist_dir(self, p2):
        """
        Check to see if a directory (storage) exists inside this storage.
        """
        ret_val = self._wrapper.exist_dir(p2.encode())
        return ret_val




    def exist_file(self, p2):
        """
        Check to see if a file exists inside this storage.
        """
        ret_val = self._wrapper.exist_file(p2.encode())
        return ret_val




    def save_log(self, p2, p3, p4, p5):
        """
        Save an embedded file to an ASCII file.
        """
        self._wrapper.save_log(p2.encode(), p3.encode(), p4.encode(), p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer