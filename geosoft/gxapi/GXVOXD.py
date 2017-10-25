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
class GXVOXD:
    """
    GXVOXD class.

    :class:`geosoft.gxapi.GXVOX` Display object.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVOXD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXVOXD`
        
        :returns: A null :class:`geosoft.gxapi.GXVOXD`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXVOXD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXVOXD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1, p2, p3, p4):
        """
        Create a new :class:`geosoft.gxapi.GXVOXD`

        **Note:**

        Fails if the :class:`geosoft.gxapi.GXVOX` object is NOT thematic.
        (See the CreateThematic_VOXD function.)
        """
        ret_val = gxapi_cy.WrapVOXD.create(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        return GXVOXD(ret_val)



    @classmethod
    def create_itr(cls, p1, p2):
        """
        Create a new :class:`geosoft.gxapi.GXVOXD` with our own :class:`geosoft.gxapi.GXITR`

        **Note:**

        Fails if the :class:`geosoft.gxapi.GXVOX` object is thematic.
        (See the CreateThematic_VOXD function.)
        """
        ret_val = gxapi_cy.WrapVOXD.create_itr(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        return GXVOXD(ret_val)



    @classmethod
    def create_thematic(cls, p1):
        """
        Create a new :class:`geosoft.gxapi.GXVOXD` for a thematic :class:`geosoft.gxapi.GXVOX` object.

        **Note:**

        A thematic voxel is one where the stored integer values
        represent indices into an internally stored :class:`geosoft.gxapi.GXTPAT` object.
        Thematic voxels contain their own color definitions, and
        normal numerical operations, such as applying ITRs for display,
        are not valid.
        
        To determine if a :class:`geosoft.gxapi.GXVOX` object is thematic, use the
        iIsThematic_VOXD function.
        
        Fails if the :class:`geosoft.gxapi.GXVOX` object is NOT thematic.
        """
        ret_val = gxapi_cy.WrapVOXD.create_thematic(GXContext._get_tls_geo(), p1._wrapper)
        return GXVOXD(ret_val)




    def is_thematic(self):
        """
        Is this a thematic voxel?

        **Note:**

        A thematic voxel is one where the stored integer values
        represent indices into an internally stored :class:`geosoft.gxapi.GXTPAT` object.
        Thematic voxels contain their own color definitions, and
        normal numerical operations, such as applying ITRs for display,
        are not valid.
        """
        ret_val = self._wrapper.is_thematic()
        return ret_val




    def get_thematic_info(self, p2, p3):
        """
        Get a copy of a thematic voxel's :class:`geosoft.gxapi.GXTPAT` object and a :class:`geosoft.gxapi.GXVV` containing the current display selections.
        """
        self._wrapper.get_thematic_info(p2._wrapper, p3._wrapper)
        




    def set_thematic_selection(self, p2):
        """
        Get a copy of a thematic voxel's :class:`geosoft.gxapi.GXTPAT` object and a :class:`geosoft.gxapi.GXVV` containing the current display selections.
        """
        self._wrapper.set_thematic_selection(p2._wrapper)
        






    def get_draw_controls(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Get the draw controls
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value = self._wrapper.get_draw_controls(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value)
        




    def get_name(self, p2):
        """
        Gets the file name of the voxel.
        """
        p2.value = self._wrapper.get_name(p2.value.encode())
        




    def get_itr(self, p2):
        """
        Get the :class:`geosoft.gxapi.GXITR` of the :class:`geosoft.gxapi.GXVOXD`
        """
        self._wrapper.get_itr(p2._wrapper)
        




    def get_shell_controls(self, p2, p3):
        """
        Get the shell controls
        """
        p2.value, p3.value = self._wrapper.get_shell_controls(p2.value, p3.value)
        




    def set_draw_controls(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Set the draw controls
        """
        self._wrapper.set_draw_controls(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def set_itr(self, p2):
        """
        Set the :class:`geosoft.gxapi.GXITR` of the :class:`geosoft.gxapi.GXVOXD`
        """
        self._wrapper.set_itr(p2._wrapper)
        




    def set_shell_controls(self, p2, p3):
        """
        Set the shell controls
        """
        self._wrapper.set_shell_controls(p2, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer