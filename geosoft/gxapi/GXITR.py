### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXREG import GXREG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXITR:
    """
    GXITR class.

    The `GXITR` class provides access to `GXITR` files. An `GXITR` file maps
    ranges of values to specific colors. The `GXITR` object is typically
    used in conjunction with `GXMVIEW` objects (see `GXMVIEW` and `GXMVU`).

    **Note:**

    Histogram ranges and color zone ranges
    
    Histogram bins are defined with inclusive minima and exclusive maxima;
    for instance if Min = 0 and Inc = 1, then the second bin would include
    all values z such that  0 <= z < 1 (the first bin has all values < 0).
    
    Color zones used in displaying grids (`GXITR`, ZON etc...) are the
    opposite, with exclusive minima and inclusive maxima.
    For instance, if a zone is defined from 0 to 1, then it would
    contain all values of z such that 0 < z <= 1.
    
    These definitions mean that it is impossible to perfectly assign
    `GXITR` colors to individual bars of a histogram. The best work-around
    when the data values are integers is to define the color zones using
    0.5 values between the integers. A general work-around is to make the
    number of histogram bins much larger than the number of color zones.
    
    The `ITR_NULL` is used to hold a NULL handle to an `GXITR` class.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapITR(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXITR`
        
        :returns: A null `GXITR`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXITR` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXITR`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def change_brightness(self, p2):
        """
        Change the brightness.

        **Note:**

        0.0 brightness does nothing.
        -1.0 to 0.0 makes colors darker, -1.0 is black
        0.0 to 1.0 makes colors lighter, 1.0 is white
        """
        self._wrapper.change_brightness(p2)
        




    def color_vv(self, p2, p3):
        """
        Get color transform of a `GXVV`.

        **Note:**

        If the input value is a dummy, then the output color
        is 0 (no color).
        """
        self._wrapper.color_vv(p2._wrapper, p3._wrapper)
        




    def copy(self, p2):
        """
        Copies ITRs
        """
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls):
        """
        Create an `GXITR` object
        """
        ret_val = gxapi_cy.WrapITR.create(GXContext._get_tls_geo())
        return GXITR(ret_val)



    @classmethod
    def create_file(cls, p1):
        """
        Create an `GXITR` object from an itr, tbl, zon, lut file.
        """
        ret_val = gxapi_cy.WrapITR.create_file(GXContext._get_tls_geo(), p1.encode())
        return GXITR(ret_val)



    @classmethod
    def create_img(cls, p1, p2, p3, p4):
        """
        Create an `GXITR` for an image.

        **Note:**

        The `ITR_ZONE_DEFAULT` model will ask the `GXIMG` to provide
        a model if it can.
        
        If a shaded relief model is selected, a shaded image
        will be created and a shaded image file will be created with
        the same name as the original grid but with the suffux "_s"
        added to the name part of the grid.
        """
        ret_val = gxapi_cy.WrapITR.create_img(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        return GXITR(ret_val)



    @classmethod
    def create_map(cls, p1, p2):
        """
        Create `GXITR` from Map with `GXAGG` Group name.
        """
        ret_val = gxapi_cy.WrapITR.create_map(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return GXITR(ret_val)



    @classmethod
    def create_s(cls, p1):
        """
        Create an `GXITR` object from a `GXBF`
        """
        ret_val = gxapi_cy.WrapITR.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXITR(ret_val)






    def equal_area(self, p2, p3):
        """
        Calculate an equal area transform.
        """
        self._wrapper.equal_area(p2._wrapper, p3)
        




    def get_data_limits(self, p2, p3):
        """
        Get `GXITR` max/min data limits.

        **Note:**

        In some ITRs, especially those defined and
        embedded inside grid (`GXIMG`) objects, the
        actual data minimum and maximum values are
        stored. This function retrieves those values.
        This is NOT true of all `GXITR` objects, and in
        those cases dummy values will be returned.
        """
        p2.value, p3.value = self._wrapper.get_data_limits(p2.value, p3.value)
        




    def get_reg(self):
        """
        Get the `GXITR`'s `GXREG`
        """
        ret_val = self._wrapper.get_reg()
        return GXREG(ret_val)




    def get_zone_color(self, p2, p3):
        """
        Get the color in a zone of the `GXITR`

        **Note:**

        Valid indices are 0 to N-1, where N is the size of the `GXITR`.
        """
        p3.value = self._wrapper.get_zone_color(p2, p3.value)
        




    def color_value(self, p2):
        """
        Transform single data value to color
        """
        ret_val = self._wrapper.color_value(p2)
        return ret_val




    def get_size(self):
        """
        Get the number of zones in an `GXITR`
        """
        ret_val = self._wrapper.get_size()
        return ret_val




    def get_zone_model_type(self):
        """
        Get the `GXITR` zone model (e.g. Linear, LogLin, Equal Area).

        **Note:**

        This function may be used to determine if a color
        transform is included in an `GXITR`.
        """
        ret_val = self._wrapper.get_zone_model_type()
        return ret_val




    def linear(self, p2, p3, p4):
        """
        Calculate a linear transform.
        """
        self._wrapper.linear(p2, p3, p4)
        




    def load_a(self, p2):
        """
        Load to an ASCII file, ZON, TBL or ER-Mapper LUT
        """
        self._wrapper.load_a(p2.encode())
        




    def log_linear(self, p2, p3, p4):
        """
        Calculate a log transform.

        **Note:**

        The function name is a misnomer. This is a pure log transform.
        """
        self._wrapper.log_linear(p2, p3, p4)
        




    def normal(self, p2, p3, p4, p5):
        """
        Calculate a normal distribution transform.
        """
        self._wrapper.normal(p2, p3, p4, p5)
        




    def power_zone(self, p2):
        """
        Modified `GXITR` zone values to 10 (or e) raized to the power of the values
        """
        self._wrapper.power_zone(p2)
        




    def get_brightness(self):
        """
        Get the brightness setting of the `GXITR`

        **Note:**

        Brightness can range from -1.0 (black) to 1.0 (white).
        This brightness control is relative to the normal color
        when the `GXITR` is created.

        .. seealso::

            `change_brightness`, `GXAGG.get_brightness`, `GXAGG.change_brightness`
        """
        ret_val = self._wrapper.get_brightness()
        return ret_val




    def get_zone_value(self, p2):
        """
        Get the value in a zone of the `GXITR`

        **Note:**

        Valid indices are 0 to N-2, where N is the size of the `GXITR`.
        """
        ret_val = self._wrapper.get_zone_value(p2)
        return ret_val




    def save_a(self, p2):
        """
        Save to an ASCII file, ZON, TBL or ER-Mapper LUT
        """
        self._wrapper.save_a(p2.encode())
        




    def save_file(self, p2):
        """
        Save to any type (based on the extension of the input file name).
        """
        self._wrapper.save_file(p2.encode())
        




    def serial(self, p2):
        """
        Serialize an `GXITR` to a `GXBF`
        """
        self._wrapper.serial(p2._wrapper)
        



    @classmethod
    def set_agg_map(cls, p1, p2, p3):
        """
        Set `GXITR` to an `GXAGG` in map

        **Note:**

        See the `create_map` function
        """
        gxapi_cy.WrapITR.set_agg_map(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper)
        




    def set_bright_contrast(self, p2, p3):
        """
        Set the brightness of the `GXITR` colors

        **Note:**

        Brightness settings:
        0.0   - black
        0.5   - normal (no change)
        1.0   - white
        
        Contrast
        0.0   - flat
        1.0   - full contrast (normal)
        """
        self._wrapper.set_bright_contrast(p2, p3)
        




    def set_color_model(self, p2):
        """
        Set the color model of an `GXITR`.
        """
        self._wrapper.set_color_model(p2)
        




    def set_data_limits(self, p2, p3):
        """
        Set `GXITR` max/min data limits.
        """
        self._wrapper.set_data_limits(p2, p3)
        




    def set_size(self, p2):
        """
        Set the number of zones in an `GXITR`
        """
        self._wrapper.set_size(p2)
        




    def set_zone_color(self, p2, p3):
        """
        Set the color in a zone of the `GXITR`

        **Note:**

        Valid indices are 0 to N-1, where N is the size of the `GXITR`.
        """
        self._wrapper.set_zone_color(p2, p3)
        




    def set_zone_value(self, p2, p3):
        """
        Set the value in a zone of the `GXITR`

        **Note:**

        Valid indices are 0 to N-2, where N is the size of the `GXITR`.
        """
        self._wrapper.set_zone_value(p2, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer