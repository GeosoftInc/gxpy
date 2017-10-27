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
    Pattern Attributes:  (See DEFAULT.`GXPAT` in \\src\\etc for more inforation)
    Pattern:       The Pattern Index; defined in DEFAULT.`GXPAT`, or in the user's
    USER.`GXPAT` file. If not specified, defaults to 0 (solid fill).
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
    def null(cls):
        """
        A null (undefined) instance of `GXTPAT`
        
        :returns: A null `GXTPAT`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXTPAT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXTPAT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_color(self, code, label, descr, color):
        """
        Add a new color to the list

        **Note:**

        The new code must be unique; not in the existing list.
        """
        self._wrapper.add_color(code.encode(), label.encode(), descr.encode(), color)
        



    @classmethod
    def create(cls):
        """
        Creates an empty thematic pattern object.
        """
        ret_val = gxapi_cy.WrapTPAT.create(GXContext._get_tls_geo())
        return GXTPAT(ret_val)






    def code(self, code):
        """
        Find the index of a given thematic pattern
        """
        ret_val = self._wrapper.code(code.encode())
        return ret_val




    def get_solid_pattern(self, index, code, label, descr, color):
        """
        Get solid pattern info from the `GXTPAT`.

        **Note:**

        Returns the solid color, pattern foreground color, or symbol
        color, along with the code, label and description.
        """
        code.value, label.value, descr.value, color.value = self._wrapper.get_solid_pattern(index, code.value.encode(), label.value.encode(), descr.value.encode(), color.value)
        




    def size(self):
        """
        Returns the number of rows (items) in the `GXTPAT` object.
        """
        ret_val = self._wrapper.size()
        return ret_val




    def load_csv(self, file):
        """
        Load thematic patterns from a CSV file

        **Note:**

        The type of thematic patterns file is recognized from the types
        of fields found inside it.
        
        The following fields are identified. Only the "CODE" field is
        required, as the "default" thematic pattern is a solid black color.
        
        CODE   The pattern code (required by all types - CASE SENSITIVE)
        LABEL  Longer text identifier to use in legends etc. (up to 31 characters)
        DESCRIPTION Much longer text string (up to 127 characters).
        
        COLOR  Line color used in patterns, and for solid colors, the color.
        If only this field is found (and none below), the pattern file
        is assumed to be type TPAT_TYPE_COLOR.
        
        PATTERN         Geosoft pattern ID.
        PAT_SIZE        Pattern tile size, or symbol size (default 2mm)
        PAT_DENSITY     Pattern tile density (default 1.0)
        PAT_THICKNESS   Pattern line thickness as % of size (default 5)
        BACK_COLOR      Background color for the pattern. Also used for symbols
        (Default background is transparent).
        
        SYMBFONT        Symbol font (e.g. "symbols.gfn")
        SYMBNUM         Symbol number of the current font
        SYMBROT         Symbol rotation
        SYMBSCL         Additional scaling factor applied to the current size
        """
        self._wrapper.load_csv(file.encode())
        




    def setup_translation_vv(self, ltb, field, vv_values):
        """
        Initializes a `GXVV` used to map `GXTPAT` indices to output values

        **Note:**

        The input `GXLTB` object should have key values matching the `GXTPAT` codes.
        Whether the matches are case sensitive or not is dependent on how the
        `GXLTB` oject was created (see ltb.h).
        The `GXLTB` field values are converted to the output `GXVV` type.
        """
        self._wrapper.setup_translation_vv(ltb._wrapper, field, vv_values._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer