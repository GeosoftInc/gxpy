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
class GXTC:
    """
    GXTC class.

    The :class:`GXTC` object is used in gravitational modelling to create
    a terrain correction grid from a topography grid. This is
    accomplished with a call first to Grregter_TC, which determines
    the terrain correction from an input topography grid, then
    to Grterain_TC, which calculates the actual corrections at
    the input positions.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTC(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXTC':
        """
        A null (undefined) instance of :class:`GXTC`
        
        :returns: A null :class:`GXTC`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXTC` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXTC`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: 'GXIMG', p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: int, p9: float, p10: int) -> 'GXTC':
        ret_val = gxapi_cy.WrapTC.create(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        return GXTC(ret_val)



    @classmethod
    def create_ex(cls, p1: 'GXIMG', p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: int, p9: float, p10: int, p11: int) -> 'GXTC':
        ret_val = gxapi_cy.WrapTC.create_ex(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)
        return GXTC(ret_val)






    def grregter(self, p2: 'GXIMG', p3: 'GXIMG') -> None:
        self._wrapper.grregter(p2._wrapper, p3._wrapper)
        




    def grterain(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXIMG', p8: float) -> None:
        self._wrapper.grterain(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8)
        




    def grterain2(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXIMG', p9: float) -> None:
        self._wrapper.grterain2(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9)
        




    def g_gterain(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: float, p7: float, p8: int) -> None:
        self._wrapper.g_gterain(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer