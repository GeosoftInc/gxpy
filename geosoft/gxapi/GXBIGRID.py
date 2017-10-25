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
class GXBIGRID:
    """
    GXBIGRID class.

    The Bigrid class is used to grid data using a optimized algorithm that
    assumes data is collected in semi-straight lines.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapBIGRID(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXBIGRID`
        
        :returns: A null `GXBIGRID`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXBIGRID` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXBIGRID`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self):
        """
        Clears all the parameters in a `GXBIGRID` object
        """
        self._wrapper.clear()
        



    @classmethod
    def create(cls):
        """
        Create a handle to a Bigrid object

        **Note:**

        The Bigrid object is initially empty. It will store the
        control file parameters which the Bigrid program needs
        to execute. Use the LoadParms_BIGRID method to get the
        control file parameters into the `GXBIGRID` object.
        """
        ret_val = gxapi_cy.WrapBIGRID.create(GXContext._get_tls_geo())
        return GXBIGRID(ret_val)






    def load_parms(self, p2):
        """
        Retrieves a Bigrid object's control parameters from a file,
        or sets the parameters to default if the file doesn't exist.

        **Note:**

        If the control file name passed into this function is a file
        which does not exist, then the defaults for a Bigrid control
        file will be generated and put into the `GXBIGRID` object.
        Otherwise, the control file's settings are retrieved from
        the file and loaded into the `GXBIGRID` object.
        """
        ret_val = self._wrapper.load_parms(p2.encode())
        return ret_val




    def load_warp(self, p2, p3, p4):
        """
        Load a warp projection.
        """
        ret_val = self._wrapper.load_warp(p2.encode(), p3.encode(), p4.encode())
        return ret_val




    def run(self, p2, p3, p4):
        """
        Executes the Bigrid program, using the input channel and
        output file parameters.
        """
        self._wrapper.run(p2.encode(), p3._wrapper, p4._wrapper)
        




    def run2(self, p2, p3, p4, p5):
        """
        Executes the Bigrid program, using the input channel and
        output file parameters with a projection handle.
        """
        self._wrapper.run2(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper)
        




    def save_parms(self, p2):
        """
        Puts the Bigrid object's control parameters back into
        its control file.

        **Note:**

        If the control file did not previously exist, it will be
        created. Otherwise, the old file will be overwritten.
        """
        self._wrapper.save_parms(p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer