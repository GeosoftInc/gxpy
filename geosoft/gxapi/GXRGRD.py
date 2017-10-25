### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIMG import GXIMG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXRGRD:
    """
    GXRGRD class.

    The :class:`geosoft.gxapi.GXRGRD` object is used as a storage place for the control
    parameters which the Rangrid (minimum curvature) program needs to execute. The
    Run_RGRD function executes the Rangrid program using the :class:`geosoft.gxapi.GXRGRD` object.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapRGRD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXRGRD`
        
        :returns: A null :class:`geosoft.gxapi.GXRGRD`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXRGRD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXRGRD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self):
        """
        Clears all the parameters in a :class:`geosoft.gxapi.GXRGRD` object

        **Note:**

        DLL name _Clear_RGRD
        """
        self._wrapper.clear()
        



    @classmethod
    def create(cls):
        """
        Create a handle to a Rangrid object

        **Note:**

        The Rangrid object is initially empty. It will store the
        control file parameters which the Rangrid program needs
        to execute. Use the LoadParms_RGRD method to get the
        control file parameters into the :class:`geosoft.gxapi.GXRGRD` object.
        """
        ret_val = gxapi_cy.WrapRGRD.create(GXContext._get_tls_geo())
        return GXRGRD(ret_val)



    @classmethod
    def create_img(cls, p1, p2, p3, p4, p5, p6):
        """
        Run Rangrid directly on XYZ :class:`geosoft.gxapi.GXVV` data, output to an :class:`geosoft.gxapi.GXIMG`.

        **Note:**

        If the grid file name is defined, the :class:`geosoft.gxapi.GXIMG` is tied to a new output file.
        If the grid file name is not defined, the :class:`geosoft.gxapi.GXIMG` is memory-based; not
        tied to a file.
        """
        ret_val = gxapi_cy.WrapRGRD.create_img(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5.encode(), p6.encode())
        return GXIMG(ret_val)






    def default(self, p2, p3):
        """
        Set the defaults.
        """
        ret_val = self._wrapper.default(p2.encode(), p3._wrapper)
        return ret_val




    def load_parms(self, p2):
        """
        Retrieves a Rangrid object's control parameters from a file,
        or sets the parameters to default if the file doesn't exist.

        **Note:**

        If the control file name passed into this function is a file
        which does not exist, then the defaults for a Rangrid control
        file will be generated and put into the :class:`geosoft.gxapi.GXRGRD` object.
        Otherwise, the control file's settings are retrieved from
        the file and loaded into the :class:`geosoft.gxapi.GXRGRD` object.
        """
        ret_val = self._wrapper.load_parms(p2.encode())
        return ret_val




    def run(self, p2, p3):
        """
        Executes the Rangrid program, using the input channel and
        output file parameters.
        """
        ret_val = self._wrapper.run(p2._wrapper, p3._wrapper)
        return ret_val



    @classmethod
    def run2(cls, p1, p2, p3, p4, p5, p6):
        """
        Executes the Rangrid program directly on a database.
        """
        ret_val = gxapi_cy.WrapRGRD.run2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode())
        return ret_val




    def save_parms(self, p2):
        """
        Puts the Rangrid object's control parameters back into
        its control file.

        **Note:**

        If the control file did not previously exist, it will be
        created. Otherwise, the old file will be overwritten.
        """
        ret_val = self._wrapper.save_parms(p2.encode())
        return ret_val



    @classmethod
    def run_vv(cls, p1, p2, p3, p4, p5, p6):
        """
        Executes the Rangrid program directly on input data VVs.
        """
        gxapi_cy.WrapRGRD.run_vv(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5.encode(), p6.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer