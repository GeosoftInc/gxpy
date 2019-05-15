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
class GXCSYMB(gxapi_cy.WrapCSYMB):
    """
    GXCSYMB class.

    This class is used for generating and modifying colored symbol objects.
    Symbol fills are assigned colors based on their Z values and a zone, Aggregate
    or `GXITR <geosoft.gxapi.GXITR>` file which defines what colors are associated with different ranges
    of Z values. The position of a symbol is defined by its X,Y coordinates.
    """

    def __init__(self, handle=0):
        super(GXCSYMB, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXCSYMB <geosoft.gxapi.GXCSYMB>`
        
        :returns: A null `GXCSYMB <geosoft.gxapi.GXCSYMB>`
        :rtype:   GXCSYMB
        """
        return GXCSYMB()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def set_angle(self, angle):
        """
        Set the symbol angle.
        
        :param angle:  Symbol angle
        :type  angle:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_angle(angle)
        




    def set_base(self, base):
        """
        Set base value to subtract from Z values.
        
        :param base:   Symbol Base
        :type  base:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_base(base)
        




    def set_dynamic_col(self, att):
        """
        Associate symbol edge or fill colors with Z data
        and color transform.
        
        :param att:    :ref:`CSYMB_COLOR`
        :type  att:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use this method after a call to `set_static_col <geosoft.gxapi.GXCSYMB.set_static_col>`. This method
        reestablishes the symbol color association with their Z data
        values and color transform.
        """
        self._set_dynamic_col(att)
        




    def set_fixed(self, fixed):
        """
        Set symbol sizing to fixed (or proportionate)
        
        :param fixed:  TRUE  = Fixed symbol sizing FALSE = Proportionate sizing
        :type  fixed:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_fixed(fixed)
        




    def set_number(self, number):
        """
        Set the symbol number.
        
        :param number:  Symbol number (0x1-0x1ffff)
        :type  number:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The lower 16 bits of the number is interpreted as UTF-16 with a valid Unicode character
        code point. GFN fonts wil produce valid symbols depending on the font for 0x01-0x7f and the degree,
        plus-minus and diameter symbol (latin small letter o with stroke) for 0xB0, 0xB1 and 0xF8 respectively.

        It is possible to check if a character is valid using `GXUNC.is_valid_utf16_char <geosoft.gxapi.GXUNC.is_valid_utf16_char>`. The high 16-bits are reserved
        for future use. Also see: `GXUNC.valid_symbol <geosoft.gxapi.GXUNC.valid_symbol>` and `GXUNC.validate_symbols <geosoft.gxapi.GXUNC.validate_symbols>`
        """
        self._set_number(number)
        




    def set_scale(self, scale):
        """
        Set the symbol scale.
        
        :param scale:  Symbol scale (> 0.0)
        :type  scale:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_scale(scale)
        




    def add_data(self, vv_x, vv_y, vv_z):
        """
        Add x,y,z data to a color symbol object.
        
        :param vv_x:   `GXVV <geosoft.gxapi.GXVV>` for X data
        :param vv_y:   `GXVV <geosoft.gxapi.GXVV>` for Y data
        :param vv_z:   `GXVV <geosoft.gxapi.GXVV>` for Z data
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV
        :type  vv_z:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._add_data(vv_x, vv_y, vv_z)
        



    @classmethod
    def create(cls, itr):
        """
        Create a `GXCSYMB <geosoft.gxapi.GXCSYMB>`.
        
        :param itr:  ZON, `GXAGG <geosoft.gxapi.GXAGG>`, or `GXITR <geosoft.gxapi.GXITR>` file name
        :type  itr:  str

        :returns:    `GXCSYMB <geosoft.gxapi.GXCSYMB>` handle
        :rtype:      GXCSYMB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapCSYMB._create(GXContext._get_tls_geo(), itr.encode())
        return GXCSYMB(ret_val)






    def get_itr(self, itr):
        """
        Get the `GXITR <geosoft.gxapi.GXITR>` of the `GXCSYMB <geosoft.gxapi.GXCSYMB>`
        
        :param itr:    `GXITR <geosoft.gxapi.GXITR>` object
        :type  itr:    GXITR

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_itr(itr)
        




    def set_font(self, font, geo_font, weight, italic):
        """
        Set the symbol font name.
        
        :param font:      Font name
        :param geo_font:  Geosoft font? (TRUE or FALSE)
        :param weight:    :ref:`MVIEW_FONT_WEIGHT`
        :param italic:    Italics? (TRUE or FALSE)
        :type  font:      str
        :type  geo_font:  int
        :type  weight:    int
        :type  italic:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_font(font.encode(), geo_font, weight, italic)
        




    def set_static_col(self, col, att):
        """
        Set a static color for the symbol edge or fill.
        
        :param col:    Color value
        :param att:    :ref:`CSYMB_COLOR`
        :type  col:    int
        :type  att:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use this method to set a STATIC color for symbol edge or fill.
        By default, both edge and fill colors vary according to their
        Z data values and a color transform.
        """
        self._set_static_col(col, att)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer