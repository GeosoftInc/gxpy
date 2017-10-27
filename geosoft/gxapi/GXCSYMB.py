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
class GXCSYMB:
    """
    GXCSYMB class.

    This class is used for generating and modifying colored symbol objects.
    Symbol fills are assigned colors based on their Z values and a zone, Aggregate
    or `GXITR <geosoft.gxapi.GXITR>` file which defines what colors are associated with different ranges
    of Z values. The position of a symbol is defined by its X,Y coordinates.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapCSYMB(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXCSYMB`
        
        :returns: A null `GXCSYMB`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXCSYMB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXCSYMB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def set_angle(self, angle):
        """
        Set the symbol angle.
        """
        self._wrapper.set_angle(angle)
        




    def set_base(self, base):
        """
        Set base value to subtract from Z values.
        """
        self._wrapper.set_base(base)
        




    def set_dynamic_col(self, att):
        """
        Associate symbol edge or fill colors with Z data
        and color transform.

        **Note:**

        Use this method after a call to `set_static_col <geosoft.gxapi.GXCSYMB.set_static_col>`. This method
        reestablishes the symbol color association with their Z data
        values and color transform.
        """
        self._wrapper.set_dynamic_col(att)
        




    def set_fixed(self, fixed):
        """
        Set symbol sizing to fixed (or proportionate)
        """
        self._wrapper.set_fixed(fixed)
        




    def set_number(self, number):
        """
        Set the symbol number.

        **Note:**

        The lower 16 bits of the number is interpreted as UTF-16 with a valid Unicode character
        code point. GFN fonts wil produce valid symbols depending on the font for 0x01-0x7f and the degree,
        plus-minus and diameter symbol (latin small letter o with stroke) for 0xB0, 0xB1 and 0xF8 respectively.
        
        It is possible to check if a character is valid using `GXUNC.is_valid_utf16_char <geosoft.gxapi.GXUNC.is_valid_utf16_char>`. The high 16-bits are reserved
        for future use. Also see: `GXUNC.valid_symbol <geosoft.gxapi.GXUNC.valid_symbol>` and `GXUNC.validate_symbols <geosoft.gxapi.GXUNC.validate_symbols>`
        """
        self._wrapper.set_number(number)
        




    def set_scale(self, scale):
        """
        Set the symbol scale.
        """
        self._wrapper.set_scale(scale)
        




    def add_data(self, vv_x, vv_y, vv_z):
        """
        Add x,y,z data to a color symbol object.
        """
        self._wrapper.add_data(vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        



    @classmethod
    def create(cls, itr):
        """
        Create a `GXCSYMB <geosoft.gxapi.GXCSYMB>`.
        """
        ret_val = gxapi_cy.WrapCSYMB.create(GXContext._get_tls_geo(), itr.encode())
        return GXCSYMB(ret_val)






    def get_itr(self, itr):
        """
        Get the `GXITR <geosoft.gxapi.GXITR>` of the `GXCSYMB <geosoft.gxapi.GXCSYMB>`
        """
        self._wrapper.get_itr(itr._wrapper)
        




    def set_font(self, font, geo_font, weight, italic):
        """
        Set the symbol font name.
        """
        self._wrapper.set_font(font.encode(), geo_font, weight, italic)
        




    def set_static_col(self, col, att):
        """
        Set a static color for the symbol edge or fill.

        **Note:**

        Use this method to set a STATIC color for symbol edge or fill.
        By default, both edge and fill colors vary according to their
        Z data values and a color transform.
        """
        self._wrapper.set_static_col(col, att)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer