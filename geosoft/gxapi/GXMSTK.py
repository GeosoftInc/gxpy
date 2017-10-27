### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXSTK import GXSTK


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMSTK:
    """
    GXMSTK class.

    Multi-profile stack
    This class is used for storing data of multiple profiles and
    plotting profiles in a map. It is a container of `GXSTK` class objects.
    
    See also:         `GXSTK` class.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMSTK(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMSTK`
        
        :returns: A null `GXMSTK`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXMSTK` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXMSTK`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_stk(self):
        """
        Create and add a `GXSTK` object to `GXMSTK`

        **Note:**

        Index to the added `GXSTK` object is the last one in `GXMSTK` container.
        """
        ret_val = self._wrapper.add_stk()
        return GXSTK(ret_val)




    def chan_list_vv(self, db, num_ch_vv, str_ch_vv, x_ch_vv, prof_ch_vv, prof_ch__un_used_vv):
        """
        Save channel names in VVs based on channel types

        **Note:**

        Terms 'used' and 'unused' indicate that the a channel name
        in database also 'in' and 'not in' the `GXMSTK` object respectively
        """
        self._wrapper.chan_list_vv(db._wrapper, num_ch_vv._wrapper, str_ch_vv._wrapper, x_ch_vv._wrapper, prof_ch_vv._wrapper, prof_ch__un_used_vv._wrapper)
        



    @classmethod
    def create(cls):
        """
        Create `GXMSTK`.
        """
        ret_val = gxapi_cy.WrapMSTK.create(GXContext._get_tls_geo())
        return GXMSTK(ret_val)






    def draw_profile(self, db, line, map):
        """
        Draw multiple profiles in map
        """
        self._wrapper.draw_profile(db._wrapper, line, map._wrapper)
        




    def set_y_axis_direction(self, direction):
        """
        Set the Y-axis direction - normal or inverted
        """
        self._wrapper.set_y_axis_direction(direction)
        




    def find_stk2(self, str_val, index, vv_rtd):
        """
        Find index of `GXSTK` from a string of group names and X/Y channels

        **Note:**

        Format of the input string:
        
        Map group name + " ( " + X channel name + " , " + Y channel name + " )"
        
        for example, string "DATA ( DIST , MAG )"  indicates a map group name of DATA,
        X channel name of DIST and Y channel name of MAG.
        """
        index.value = self._wrapper.find_stk2(str_val.encode(), index.value, vv_rtd._wrapper)
        




    def get_stk(self, num):
        """
        Get a specific `GXSTK` object from a `GXMSTK` object
        (Index of 0 gets the first `GXSTK` in the `GXMSTK`)
        """
        ret_val = self._wrapper.get_stk(num)
        return GXSTK(ret_val)




    def delete_stk(self, num):
        """
        Delete a `GXSTK` object

        **Note:**

        0 is the first one
        """
        self._wrapper.delete_stk(num)
        




    def find_stk(self, str_val, index, group, x_ch, y_ch):
        """
        Find index of `GXSTK` from a string of group names and X/Y channels

        **Note:**

        Format of the input string:
        
        Map group name + " ( " + X channel name + " , " + Y channel name + " )"
        
        for example, string "DATA ( DIST , MAG )"  indicates a map group name of DATA,
        X channel name of DIST and Y channel name of MAG.
        """
        index.value, group.value, x_ch.value, y_ch.value = self._wrapper.find_stk(str_val.encode(), index.value, group.value.encode(), x_ch.value.encode(), y_ch.value.encode())
        




    def get_num_stk(self):
        """
        Get the number of `GXSTK` objects in a `GXMSTK` object
        """
        ret_val = self._wrapper.get_num_stk()
        return ret_val




    def read_ini(self, ra):
        """
        Read multiple profiles parameters from an INI file
        """
        self._wrapper.read_ini(ra._wrapper)
        




    def save_profile(self, wa):
        """
        Save multiple profile INI parameters in a `GXWA` file of INI format
        """
        self._wrapper.save_profile(wa._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer