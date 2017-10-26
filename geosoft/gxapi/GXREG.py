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
class GXREG:
    """
    GXREG class.

    The `GXREG` class is used for storing and retrieving named
    variables. Many classes contain `GXREG` objects for storing
    information particular to the class.  The `GXMETA` class supersedes
    the `GXREG` class and is gradually replacing the use of the
    `GXREG` class in newer applications.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapREG(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXREG`
        
        :returns: A null `GXREG`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXREG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXREG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self):
        """
        Clears all the parameters in a `GXREG` object
        """
        self._wrapper.clear()
        




    def copy(self, srce):
        """
        Copy
        """
        self._wrapper.copy(srce._wrapper)
        



    @classmethod
    def create(cls, l_parm_length):
        """
        Create a handle to a `GXREG` object
        """
        ret_val = gxapi_cy.WrapREG.create(GXContext._get_tls_geo(), l_parm_length)
        return GXREG(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create a handle to a `GXREG` object from a `GXBF`
        """
        ret_val = gxapi_cy.WrapREG.create_s(GXContext._get_tls_geo(), bf._wrapper)
        return GXREG(ret_val)






    def get(self, parm, p3):
        """
        Gets a string for a specified parameter in the `GXREG` object
        """
        p3.value = self._wrapper.get(parm.encode(), p3.value.encode())
        




    def get_int(self, parm, p3):
        """
        Gets an int for a specified parameter in the `GXREG` object

        **Note:**

        If parameter is not present in `GXREG`, `iDUMMY` is returned.
        """
        p3.value = self._wrapper.get_int(parm.encode(), p3.value)
        




    def get_one(self, loc, parm, data):
        """
        Gets n-th entry of the `GXREG` object
        """
        parm.value, data.value = self._wrapper.get_one(loc, parm.value.encode(), data.value.encode())
        




    def get_double(self, parm, p3):
        """
        Gets an real for a specified parameter in the `GXREG` object

        **Note:**

        If parameter is not present in `GXREG`, `rDUMMY` is returned.
        """
        p3.value = self._wrapper.get_double(parm.encode(), p3.value)
        




    def entries(self):
        """
        Get the number of parms in a `GXREG` object
        """
        ret_val = self._wrapper.entries()
        return ret_val




    def load_ini(self, ini):
        """
        Load a registry from an INI file.

        **Note:**

        Items are loaded into the `GXREG` in the format "GROUP.ITEM".
        """
        self._wrapper.load_ini(ini.encode())
        




    def match_string(self, parm, data):
        """
        Replace a string with reg settings.
        """
        data.value = self._wrapper.match_string(parm.encode(), data.value.encode())
        




    def merge(self, srce, type):
        """
        Merge
        """
        self._wrapper.merge(srce._wrapper, type)
        




    def save_ini(self, p2):
        """
        Save a `GXREG` to an INI file.

        **Note:**

        Only `GXREG` parameters in the form "GROUP.ITEM" are
        dumped to the INI file, because they match the INI format
        which groups items under [GROUP] headings.
        Single-word items (without a separating period) are skipped.
        """
        self._wrapper.save_ini(p2.encode())
        




    def serial(self, bf):
        """
        Serialize a `GXREG` object into a file.
        """
        self._wrapper.serial(bf._wrapper)
        




    def set(self, parm, p3):
        """
        Sets a string parameter in the `GXREG` object

        **Note:**

        To remove a parameter completely, use one of the
        following:
        
        `set_int`(Reg, sParam, `iDUMMY`);
        or
        `set_double`(Reg, sParam, `rDUMMY`);
        """
        self._wrapper.set(parm.encode(), p3.encode())
        




    def set_int(self, parm, p3):
        """
        Sets an int for a specified parameter in the `GXREG` object
        """
        self._wrapper.set_int(parm.encode(), p3)
        




    def set_double(self, parm, p3):
        """
        Sets an real for a specified parameter in the `GXREG` object
        """
        self._wrapper.set_double(parm.encode(), p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer