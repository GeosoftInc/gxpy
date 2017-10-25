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
    plotting profiles in a map. It is a container of :class:`geosoft.gxapi.GXSTK` class objects.
    
    See also:         :class:`geosoft.gxapi.GXSTK` class.
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXMSTK`
        
        :returns: A null :class:`geosoft.gxapi.GXMSTK`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXMSTK` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXMSTK`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_stk(self):
        """
        Create and add a :class:`geosoft.gxapi.GXSTK` object to :class:`geosoft.gxapi.GXMSTK`

        **Note:**

        Index to the added :class:`geosoft.gxapi.GXSTK` object is the last one in :class:`geosoft.gxapi.GXMSTK` container.
        """
        ret_val = self._wrapper.add_stk()
        return GXSTK(ret_val)




    def chan_list_vv(self, p2, p3, p4, p5, p6, p7):
        """
        Save channel names in VVs based on channel types

        **Note:**

        Terms 'used' and 'unused' indicate that the a channel name
        in database also 'in' and 'not in' the :class:`geosoft.gxapi.GXMSTK` object respectively
        """
        self._wrapper.chan_list_vv(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper)
        



    @classmethod
    def create(cls):
        """
        Create :class:`geosoft.gxapi.GXMSTK`.
        """
        ret_val = gxapi_cy.WrapMSTK.create(GXContext._get_tls_geo())
        return GXMSTK(ret_val)






    def draw_profile(self, p2, p3, p4):
        """
        Draw multiple profiles in map
        """
        self._wrapper.draw_profile(p2._wrapper, p3, p4._wrapper)
        




    def set_y_axis_direction(self, p2):
        """
        Set the Y-axis direction - normal or inverted
        """
        self._wrapper.set_y_axis_direction(p2)
        




    def find_stk2(self, p2, p3, p4):
        """
        Find index of :class:`geosoft.gxapi.GXSTK` from a string of group names and X/Y channels

        **Note:**

        Format of the input string:
        
        Map group name + " ( " + X channel name + " , " + Y channel name + " )"
        
        for example, string "DATA ( DIST , MAG )"  indicates a map group name of DATA,
        X channel name of DIST and Y channel name of MAG.
        """
        p3.value = self._wrapper.find_stk2(p2.encode(), p3.value, p4._wrapper)
        




    def get_stk(self, p2):
        """
        Get a specific :class:`geosoft.gxapi.GXSTK` object from a :class:`geosoft.gxapi.GXMSTK` object
        (Index of 0 gets the first :class:`geosoft.gxapi.GXSTK` in the :class:`geosoft.gxapi.GXMSTK`)
        """
        ret_val = self._wrapper.get_stk(p2)
        return GXSTK(ret_val)




    def delete_stk(self, p2):
        """
        Delete a :class:`geosoft.gxapi.GXSTK` object

        **Note:**

        0 is the first one
        """
        self._wrapper.delete_stk(p2)
        




    def find_stk(self, p2, p3, p4, p6, p8):
        """
        Find index of :class:`geosoft.gxapi.GXSTK` from a string of group names and X/Y channels

        **Note:**

        Format of the input string:
        
        Map group name + " ( " + X channel name + " , " + Y channel name + " )"
        
        for example, string "DATA ( DIST , MAG )"  indicates a map group name of DATA,
        X channel name of DIST and Y channel name of MAG.
        """
        p3.value, p4.value, p6.value, p8.value = self._wrapper.find_stk(p2.encode(), p3.value, p4.value.encode(), p6.value.encode(), p8.value.encode())
        




    def get_num_stk(self):
        """
        Get the number of :class:`geosoft.gxapi.GXSTK` objects in a :class:`geosoft.gxapi.GXMSTK` object
        """
        ret_val = self._wrapper.get_num_stk()
        return ret_val




    def read_ini(self, p2):
        """
        Read multiple profiles parameters from an INI file
        """
        self._wrapper.read_ini(p2._wrapper)
        




    def save_profile(self, p2):
        """
        Save multiple profile INI parameters in a :class:`geosoft.gxapi.GXWA` file of INI format
        """
        self._wrapper.save_profile(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer