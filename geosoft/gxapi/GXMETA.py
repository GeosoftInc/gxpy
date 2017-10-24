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
class GXMETA:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMETA(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXMETA':
        """
        A null (undefined) instance of :class:`GXMETA`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMETA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMETA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Attribute



    def create_attrib(self, p2: str, p3: int, p4: int) -> int:
        ret_val = self._wrapper.create_attrib(p2.encode(), p3, p4)
        return ret_val




    def delete_attrib(self, p2: int) -> None:
        self._wrapper.delete_attrib(p2)
        




# Browser



    def set_attribute_editable(self, p2: int, p3: int) -> None:
        self._wrapper.set_attribute_editable(p2, p3)
        




    def set_attribute_visible(self, p2: int, p3: int) -> None:
        self._wrapper.set_attribute_visible(p2, p3)
        




# Class



    def create_class(self, p2: str, p3: int) -> int:
        ret_val = self._wrapper.create_class(p2.encode(), p3)
        return ret_val




    def delete_class(self, p2: int) -> None:
        self._wrapper.delete_class(p2)
        




# Core



    def copy(self, p2: 'GXMETA') -> None:
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls) -> 'GXMETA':
        ret_val = gxapi_cy.WrapMETA.create(GXContext._get_tls_geo())
        return GXMETA(ret_val)



    @classmethod
    def create_s(cls, p1: 'GXBF') -> 'GXMETA':
        ret_val = gxapi_cy.WrapMETA.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXMETA(ret_val)






    def serial(self, p2: 'GXBF') -> None:
        self._wrapper.serial(p2._wrapper)
        




# Get Data



    def find_data(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.find_data(p2, p3)
        return ret_val




    def get_attrib_bool(self, p2: int, p3: int, p4: int_ref) -> None:
        p4.value = self._wrapper.get_attrib_bool(p2, p3, p4.value)
        




    def get_attrib_enum(self, p2: int, p3: int, p4: int_ref) -> None:
        p4.value = self._wrapper.get_attrib_enum(p2, p3, p4.value)
        




    def get_attrib_int(self, p2: int, p3: int, p4: int_ref) -> None:
        p4.value = self._wrapper.get_attrib_int(p2, p3, p4.value)
        




    def get_attrib_double(self, p2: int, p3: int, p4: float_ref) -> None:
        p4.value = self._wrapper.get_attrib_double(p2, p3, p4.value)
        




    def get_attrib_string(self, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = self._wrapper.get_attrib_string(p2, p3, p4.value.encode())
        




    def has_value(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.has_value(p2, p3)
        return ret_val




# Import/Export



    def export_table_csv(self, p2: int, p3: str) -> None:
        self._wrapper.export_table_csv(p2, p3.encode())
        




    def import_table_csv(self, p2: int, p3: str) -> None:
        self._wrapper.import_table_csv(p2, p3.encode())
        




    def write_text(self, p2: 'GXWA') -> None:
        self._wrapper.write_text(p2._wrapper)
        




# Item



    def delete_all_items(self, p2: int) -> None:
        self._wrapper.delete_all_items(p2)
        




    def delete_item(self, p2: int) -> None:
        self._wrapper.delete_item(p2)
        




    def h_creat_item(self, p2: str, p3: int) -> int:
        ret_val = self._wrapper.h_creat_item(p2.encode(), p3)
        return ret_val




    def h_get_next_item(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.h_get_next_item(p2, p3)
        return ret_val




# Object



    def get_attrib_obj(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.get_attrib_obj(p2, p3, p4)
        




    def set_attrib_obj(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.set_attrib_obj(p2, p3, p4)
        




# Set Data



    def set_attrib_bool(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.set_attrib_bool(p2, p3, p4)
        




    def set_attrib_enum(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.set_attrib_enum(p2, p3, p4)
        




    def set_attrib_int(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.set_attrib_int(p2, p3, p4)
        




    def set_attrib_double(self, p2: int, p3: int, p4: float) -> None:
        self._wrapper.set_attrib_double(p2, p3, p4)
        




    def set_attrib_string(self, p2: int, p3: int, p4: str) -> None:
        self._wrapper.set_attrib_string(p2, p3, p4.encode())
        




    def set_empty_attrib(self, p2: int, p3: int) -> None:
        self._wrapper.set_empty_attrib(p2, p3)
        




# Transfer



    def h_copy_across_attribute(self, p2: 'GXMETA', p3: int) -> int:
        ret_val = self._wrapper.h_copy_across_attribute(p2._wrapper, p3)
        return ret_val




    def h_copy_across_class(self, p2: 'GXMETA', p3: int) -> int:
        ret_val = self._wrapper.h_copy_across_class(p2._wrapper, p3)
        return ret_val




    def h_copy_across_data(self, p2: 'GXMETA', p3: int) -> int:
        ret_val = self._wrapper.h_copy_across_data(p2._wrapper, p3)
        return ret_val




    def h_copy_across_item(self, p2: 'GXMETA', p3: int) -> int:
        ret_val = self._wrapper.h_copy_across_item(p2._wrapper, p3)
        return ret_val




    def h_copy_across_type(self, p2: 'GXMETA', p3: int) -> int:
        ret_val = self._wrapper.h_copy_across_type(p2._wrapper, p3)
        return ret_val




    def move_datas_across(self, p2: 'GXMETA', p3: int, p4: int) -> None:
        self._wrapper.move_datas_across(p2._wrapper, p3, p4)
        




# Type



    def create_type(self, p2: str, p3: int, p4: int) -> int:
        ret_val = self._wrapper.create_type(p2.encode(), p3, p4)
        return ret_val




    def delete_data(self, p2: int) -> None:
        self._wrapper.delete_data(p2)
        




    def delete_type(self, p2: int) -> None:
        self._wrapper.delete_type(p2)
        




# UMN



    def get_obj_name(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_obj_name(p2, p3.value.encode())
        




    def resolve_umn(self, p2: str) -> int:
        ret_val = self._wrapper.resolve_umn(p2.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer