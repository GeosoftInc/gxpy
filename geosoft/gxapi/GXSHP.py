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
class GXSHP:
    """
    GXSHP class.

    The :class:`GXSHP` class is used to create ESRI shape files.

    **Note:**

    Shape files contain a single "geometry" type, e.g.
    points, arcs or polygons. They may be accompanied by
    a DBF file containing attribute data.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSHP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXSHP':
        """
        A null (undefined) instance of :class:`GXSHP`
        
        :returns: A null :class:`GXSHP`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXSHP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXSHP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def append_item(self) -> None:
        self._wrapper.append_item()
        



    @classmethod
    def create(cls, p1: str, p2: int) -> 'GXSHP':
        ret_val = gxapi_cy.WrapSHP.create(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXSHP(ret_val)






    def add_int_field(self, p2: str) -> int:
        ret_val = self._wrapper.add_int_field(p2.encode())
        return ret_val




    def add_double_field(self, p2: str, p3: int) -> int:
        ret_val = self._wrapper.add_double_field(p2.encode(), p3)
        return ret_val




    def add_string_field(self, p2: str, p3: int) -> int:
        ret_val = self._wrapper.add_string_field(p2.encode(), p3)
        return ret_val




    def find_field(self, p2: str) -> int:
        ret_val = self._wrapper.find_field(p2.encode())
        return ret_val




    def max_id_num(self) -> int:
        ret_val = self._wrapper.max_id_num()
        return ret_val




    def num_fields(self) -> int:
        ret_val = self._wrapper.num_fields()
        return ret_val




    def num_records(self) -> int:
        ret_val = self._wrapper.num_records()
        return ret_val




    def type(self) -> int:
        ret_val = self._wrapper.type()
        return ret_val



    @classmethod
    def open(cls, p1: str) -> 'GXSHP':
        ret_val = gxapi_cy.WrapSHP.open(GXContext._get_tls_geo(), p1.encode())
        return GXSHP(ret_val)




    def set_arc(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.set_arc(p2._wrapper, p3._wrapper)
        




    def set_arc_z(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.set_arc_z(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def set_int(self, p2: int, p3: int) -> None:
        self._wrapper.set_int(p2, p3)
        




    def set_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2._wrapper)
        




    def set_point(self, p2: float, p3: float) -> None:
        self._wrapper.set_point(p2, p3)
        




    def set_point_z(self, p2: float, p3: float, p4: float) -> None:
        self._wrapper.set_point_z(p2, p3, p4)
        




    def set_polygon(self, p2: 'GXVV', p3: 'GXVV', p4: int) -> None:
        self._wrapper.set_polygon(p2._wrapper, p3._wrapper, p4)
        




    def set_polygon_z(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: int) -> None:
        self._wrapper.set_polygon_z(p2._wrapper, p3._wrapper, p4._wrapper, p5)
        




    def set_double(self, p2: int, p3: float) -> None:
        self._wrapper.set_double(p2, p3)
        




    def set_string(self, p2: int, p3: str) -> None:
        self._wrapper.set_string(p2, p3.encode())
        




    def write_item(self) -> None:
        self._wrapper.write_item()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer