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
class GXTRND:
    """
    GXTRND class.

    The `GXTRND` methods are used to determine trend directions in database data by locating
    maxima and minima along lines and joining them in a specified direction.
    The resulting trend lines are appended to the database and used by gridding methods
    such as Bigrid and Rangrid to enforce features in the specified direction.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTRND(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTRND`
        
        :returns: A null `GXTRND`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXTRND` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXTRND`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def get_max_min(cls, vv_x, vv_y, vv_z, vv_xm, v_vym, v_vzm, window, trnd):
        """
        Find the max/min nodes in a line.

        **Note:**

        Trend lines positions consist of X and Y VVs
        """
        gxapi_cy.WrapTRND.get_max_min(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_xm._wrapper, v_vym._wrapper, v_vzm._wrapper, window, trnd)
        



    @classmethod
    def get_mesh(cls, db, chan, window, max_length, mesh_vv, trnd):
        """
        Get the lines in a trend mesh.
        """
        gxapi_cy.WrapTRND.get_mesh(GXContext._get_tls_geo(), db._wrapper, chan.encode(), window, max_length, mesh_vv._wrapper, trnd)
        



    @classmethod
    def trnd_db(cls, db, chan, window, angle, deviation, max_length, deflection, min_length, resample, br_angle):
        """
        Uses a selected channel to find data trends in a database.
        """
        gxapi_cy.WrapTRND.trnd_db(GXContext._get_tls_geo(), db._wrapper, chan.encode(), window, angle, deviation, max_length, deflection, min_length, resample, br_angle)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer