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

    The `GXSBF` class provides a means of storing data in a
    file-type directory structure within a workspace, database
    or map. Each of these three objects contains its own `GXSBF` object,
    which may be accessed using the `h_get_sys`, `h_get_db` and
    `h_get_map` functions. To access data in a file, or create a
    new file in the `GXSBF` object, call the CreatSBF_BF function (see `GXBF`),
    which will return a `GXBF` object to use.
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
        A null (undefined) instance of `GXSBF`
        
        :returns: A null `GXSBF`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXSBF` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXSBF`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def create(self, file, status):
        """
        Create a child `GXSBF` object inside an `GXSBF`.
        """
        ret_val = self._wrapper.create(file.encode(), status)
        return GXSBF(ret_val)




    def create_obj_list(self, lst, type):
        """
        Fills an `GXLST` with embedded storage names of an `GXSBF`.

        **Note:**

        Function will populate an `GXLST` object with embedded files (`SBF_TYPE_FILES`),
        directories (`SBF_TYPE_DIRS`), or both (pass `SBF_TYPE_BOTH`) in an `GXSBF`.
        Along with the Name of the file or directory, a constant "dir" or "file" string is written
        to the `GXLST` also.
        """
        self._wrapper.create_obj_list(lst._wrapper, type)
        




    def del_dir(self, dir):
        """
        Delete a directory (storage) from this storage.
        """
        self._wrapper.del_dir(dir.encode())
        




    def del_file(self, file):
        """
        Delete a file from this storage.
        """
        self._wrapper.del_file(file.encode())
        





    @classmethod
    def h_get_db(cls, db):
        """
        Get the embedded file storage from a database.
        """
        ret_val = gxapi_cy.WrapSBF.h_get_db(GXContext._get_tls_geo(), db._wrapper)
        return GXSBF(ret_val)



    @classmethod
    def h_get_map(cls, map):
        """
        Get the embedded file storage from a map.
        """
        ret_val = gxapi_cy.WrapSBF.h_get_map(GXContext._get_tls_geo(), map._wrapper)
        return GXSBF(ret_val)



    @classmethod
    def h_get_sys(cls):
        """
        Get the main embedded file storage (in workspace).
        """
        ret_val = gxapi_cy.WrapSBF.h_get_sys(GXContext._get_tls_geo())
        return GXSBF(ret_val)




    def exist_dir(self, dir):
        """
        Check to see if a directory (storage) exists inside this storage.
        """
        ret_val = self._wrapper.exist_dir(dir.encode())
        return ret_val




    def exist_file(self, file):
        """
        Check to see if a file exists inside this storage.
        """
        ret_val = self._wrapper.exist_file(file.encode())
        return ret_val




    def save_log(self, dir, file, file_save, p5):
        """
        Save an embedded file to an ASCII file.
        """
        self._wrapper.save_log(dir.encode(), file.encode(), file_save.encode(), p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer