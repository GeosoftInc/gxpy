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
class GXTPAT:
    """
    GXTPAT class.

    The full name of the pattern.
    ex: "felsic volcanics"
    Code:          Short-form of the pattern description. This is the value
    which typically appears (for instance) in the "Rock code"
    channel in a Wholeplot From-To data group.
    ex: "FVOL"
    The code is CASE-SENSITIVE.
    
    Label:         Text to use as a short-form in labels, graphs etc.
    By default, this is the same as the code.
    ex: "FVol."
    Pattern Attributes:  (See DEFAULT.:class:`GXPAT` in \\src\\etc for more inforation)
    Pattern:       The Pattern Index; defined in DEFAULT.:class:`GXPAT`, or in the user's
    USER.:class:`GXPAT` file. If not specified, defaults to 0 (solid fill).
    Size:          The pattern tile size. If not specified, defaults to 2.0mm.
    Density:       The tiling density. If not specified, defaults to 1.0.
    Thickness:     The line thickness in the tile, expressed as a integer
    percentage (0-100) of the tile size.
    Color:        The pattern line work color. If not specified, defaults to black.
    
    Background color: The pattern background color. If not specified, defaults to
    transparent (C_ANY_NONE)
    
    
    Symbols:
    
    Symbol Font     The name of the symbol font to use for a given symbol index
    
    Symbol Number   Index into the font.
    
    Symbol Rotation: Rotation in degrees CCW.
    
    Symbol Scaling  Additional scale factor to apply to symbol size (Default 1.0)
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTPAT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXTPAT':
        """
        A null (undefined) instance of :class:`GXTPAT`
        
        :returns: A null :class:`GXTPAT`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXTPAT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXTPAT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_color(self, p2: str, p3: str, p4: str, p5: int) -> None:
        self._wrapper.add_color(p2.encode(), p3.encode(), p4.encode(), p5)
        



    @classmethod
    def create(cls) -> 'GXTPAT':
        ret_val = gxapi_cy.WrapTPAT.create(GXContext._get_tls_geo())
        return GXTPAT(ret_val)






    def code(self, p2: str) -> int:
        ret_val = self._wrapper.code(p2.encode())
        return ret_val




    def get_solid_pattern(self, p2: int, p3: str_ref, p5: str_ref, p7: str_ref, p9: int_ref) -> None:
        p3.value, p5.value, p7.value, p9.value = self._wrapper.get_solid_pattern(p2, p3.value.encode(), p5.value.encode(), p7.value.encode(), p9.value)
        




    def size(self) -> int:
        ret_val = self._wrapper.size()
        return ret_val




    def load_csv(self, p2: str) -> None:
        self._wrapper.load_csv(p2.encode())
        




    def setup_translation_vv(self, p2: 'GXLTB', p3: int, p4: 'GXVV') -> None:
        self._wrapper.setup_translation_vv(p2._wrapper, p3, p4._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer