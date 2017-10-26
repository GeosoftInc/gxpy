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
class GXKGRD:
    """
    GXKGRD class.

    The `GXKGRD` object is used as a storage place for the control
    parameters that the Krigrid program needs to execute. The
    Run_KGRD function executes the Krigrid program using the
    `GXKGRD` object.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapKGRD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXKGRD`
        
        :returns: A null `GXKGRD`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXKGRD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXKGRD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self):
        """
        Clears all the parameters in a `GXKGRD` object
        """
        self._wrapper.clear()
        



    @classmethod
    def create(cls):
        """
        Create a handle to a Krigrid object

        **Note:**

        The Krigrid object is initially empty. It will store the
        control file parameters which the Krigrid program needs
        to execute. Use the LoadParms_KGRD method to get the
        control file parameters into the `GXKGRD` object.
        """
        ret_val = gxapi_cy.WrapKGRD.create(GXContext._get_tls_geo())
        return GXKGRD(ret_val)






    def load_parms(self, file):
        """
        Retrieves a Krigrid object's control parameters from a file.

        **Note:**

        If the control file name passed into this function is a file
        which does not exist, then the defaults for a Krigrid control
        file will be generated and put into the `GXKGRD` object.
        Otherwise, the control file's settings are retrieved from
        the file and loaded into the `GXKGRD` object.
        """
        ret_val = self._wrapper.load_parms(file.encode())
        return ret_val




    def run(self, zchan, in_dat, out_grd_dat, out_err_dat, in_var_name, out_var_name, vao, vi, vo):
        """
        Executes the Krigrid program, using the input channel and
        output file parameters.
        """
        ret_val = self._wrapper.run(zchan.encode(), in_dat._wrapper, out_grd_dat._wrapper, out_err_dat._wrapper, in_var_name.encode(), out_var_name.encode(), vao, vi, vo)
        return ret_val



    @classmethod
    def run2(cls, db, x, y, z, ctl, grd, err_grd, in_var, out_var, vao):
        """
        Executes the Krigrid program directly on a database.
        """
        ret_val = gxapi_cy.WrapKGRD.run2(GXContext._get_tls_geo(), db._wrapper, x.encode(), y.encode(), z.encode(), ctl.encode(), grd.encode(), err_grd.encode(), in_var.encode(), out_var.encode(), vao)
        return ret_val



    @classmethod
    def run3(cls, db, x, y, z, ctl, grd, err_grd, in_var, out_var, log_file, vao):
        """
        Executes the Krigrid program directly on a database and specifies the log file
        """
        ret_val = gxapi_cy.WrapKGRD.run3(GXContext._get_tls_geo(), db._wrapper, x.encode(), y.encode(), z.encode(), ctl.encode(), grd.encode(), err_grd.encode(), in_var.encode(), out_var.encode(), log_file.encode(), vao)
        return ret_val




    def save_parms(self, name):
        """
        Puts the Krigrid object's control parameters back into
        its control file.

        **Note:**

        If the control file did not previously exist, it will be
        created. Otherwise, the old file will be overwritten.
        """
        ret_val = self._wrapper.save_parms(name.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer