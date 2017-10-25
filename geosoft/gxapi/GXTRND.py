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
    def get_max_min(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Find the max/min nodes in a line.

        **Note:**

        Trend lines positions consist of X and Y VVs
        """
        gxapi_cy.WrapTRND.get_max_min(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7, p8)
        



    @classmethod
    def get_mesh(cls, p1, p2, p3, p4, p5, p6):
        """
        Get the lines in a trend mesh.
        """
        gxapi_cy.WrapTRND.get_mesh(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5._wrapper, p6)
        



    @classmethod
    def trnd_db(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Uses a selected channel to find data trends in a database.
        """
        gxapi_cy.WrapTRND.trnd_db(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer