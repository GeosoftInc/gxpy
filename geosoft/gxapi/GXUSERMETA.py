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
class GXUSERMETA:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapUSERMETA(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXUSERMETA':
        """
        A null (undefined) instance of :class:`GXUSERMETA`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXUSERMETA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXUSERMETA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: int) -> 'GXUSERMETA':
        ret_val = gxapi_cy.WrapUSERMETA.create(GXContext._get_tls_geo(), p1)
        return GXUSERMETA(ret_val)



    @classmethod
    def create_s(cls, p1: str) -> 'GXUSERMETA':
        ret_val = gxapi_cy.WrapUSERMETA.create_s(GXContext._get_tls_geo(), p1.encode())
        return GXUSERMETA(ret_val)






    def get_data_creation_date(self, p2: float_ref) -> None:
        p2.value = self._wrapper.get_data_creation_date(p2.value)
        




    def get_extents2d(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_extents2d(p2.value, p3.value, p4.value, p5.value)
        




    def get_extents3d(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_extents3d(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_meta_creation_date(self, p2: float_ref) -> None:
        p2.value = self._wrapper.get_meta_creation_date(p2.value)
        




    def get_xml_format(self, p2: int_ref) -> None:
        p2.value = self._wrapper.get_xml_format(p2.value)
        




    def compare(self, p2: 'GXUSERMETA') -> int:
        ret_val = self._wrapper.compare(p2._wrapper)
        return ret_val




    def get_data_creator(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_data_creator(p2.value.encode())
        




    def get_format(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_format(p2.value.encode())
        




    def get_meta_creator(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_meta_creator(p2.value.encode())
        




    def get_project(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_project(p2.value.encode())
        




    def get_title(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_title(p2.value.encode())
        




    def serial(self, p2: int, p3: str) -> None:
        self._wrapper.serial(p2, p3.encode())
        




    def set_data_creation_date(self, p2: float) -> None:
        self._wrapper.set_data_creation_date(p2)
        




    def set_data_creator(self, p2: str) -> None:
        self._wrapper.set_data_creator(p2.encode())
        




    def set_extents2d(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.set_extents2d(p2, p3, p4, p5)
        




    def set_extents3d(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.set_extents3d(p2, p3, p4, p5, p6, p7)
        




    def set_format(self, p2: str) -> None:
        self._wrapper.set_format(p2.encode())
        




    def set_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2._wrapper)
        




    def set_meta_creation_date(self, p2: float) -> None:
        self._wrapper.set_meta_creation_date(p2)
        




    def set_meta_creator(self, p2: str) -> None:
        self._wrapper.set_meta_creator(p2.encode())
        




    def set_project(self, p2: str) -> None:
        self._wrapper.set_project(p2.encode())
        




    def set_title(self, p2: str) -> None:
        self._wrapper.set_title(p2.encode())
        



    @classmethod
    def update_extents2_d(cls, p1: str, p2: 'GXIPJ', p3: float, p4: float, p5: float, p6: float) -> None:
        gxapi_cy.WrapUSERMETA.update_extents2_d(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6)
        



    @classmethod
    def update_file_type(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapUSERMETA.update_file_type(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def save_file_lineage(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapUSERMETA.save_file_lineage(GXContext._get_tls_geo(), p1.encode(), p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer