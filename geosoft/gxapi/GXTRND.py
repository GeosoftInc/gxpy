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
class GXTRND:
    """
    GXTRND class.

    The :class:`GXTRND` methods are used to determine trend directions in database data by locating
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
    def null(cls) -> 'GXTRND':
        """
        A null (undefined) instance of :class:`GXTRND`
        
        :returns: A null :class:`GXTRND`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXTRND` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXTRND`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def get_max_min(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: float, p8: int) -> None:
        gxapi_cy.WrapTRND.get_max_min(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7, p8)
        



    @classmethod
    def get_mesh(cls, p1: 'GXDB', p2: str, p3: float, p4: float, p5: 'GXVV', p6: int) -> None:
        gxapi_cy.WrapTRND.get_mesh(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5._wrapper, p6)
        



    @classmethod
    def trnd_db(cls, p1: 'GXDB', p2: str, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float) -> None:
        gxapi_cy.WrapTRND.trnd_db(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer