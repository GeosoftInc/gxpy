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
class GXSHP:
    """
    GXSHP class.

    The `GXSHP` class is used to create ESRI shape files.

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
    def null(cls):
        """
        A null (undefined) instance of `GXSHP`
        
        :returns: A null `GXSHP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXSHP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXSHP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def append_item(self):
        """
        Append the current item and data to an old `GXSHP` object.

        **Note:**

        The currently stored `GXSHP` item and data are written to the
        `GXSHP` geometry and data files. (If no data fields have been
        defined, then the data file is not written).
        """
        self._wrapper.append_item()
        



    @classmethod
    def create(cls, name, type):
        """
        Create a new `GXSHP` object

        **Note:**

        The file name is used to create the various files. The
        file type and extension are added:
        
        e.g. "filename.shp",
             "filename.dbf"
        
        The following geometry types are currently supported:
        
        Type                    Required geometry function.
        
        `SHP_GEOM_TYPE_POINT`     `set_point`
        `SHP_GEOM_TYPE_ARC`       `set_arc`
        `SHP_GEOM_TYPE_POLYGON`   `set_polygon`
        
        `SHP_GEOM_TYPE_POINTZ`    `set_point_z`
        `SHP_GEOM_TYPE_ARCZ`      `set_arc_z`
        `SHP_GEOM_TYPE_POLYGONZ`  `set_polygon_z`
        """
        ret_val = gxapi_cy.WrapSHP.create(GXContext._get_tls_geo(), name.encode(), type)
        return GXSHP(ret_val)






    def add_int_field(self, field):
        """
        Add an INT type data field to a shape file

        **Note:**

        The returned field index should be used with the SetXXX_SHP
        functions to set individual data values.
        """
        ret_val = self._wrapper.add_int_field(field.encode())
        return ret_val




    def add_double_field(self, field, dec):
        """
        Add a REAL type data field to a shape file

        **Note:**

        The returned field index should be used with the SetXXX_SHP
        functions to set individual data values.
        """
        ret_val = self._wrapper.add_double_field(field.encode(), dec)
        return ret_val




    def add_string_field(self, field, width):
        """
        Add a string type data field to a shape file

        **Note:**

        The returned field index should be used with the SetXXX_SHP
        functions to set individual data values.
        """
        ret_val = self._wrapper.add_string_field(field.encode(), width)
        return ret_val




    def find_field(self, field):
        """
        Find the index for a data field.
        """
        ret_val = self._wrapper.find_field(field.encode())
        return ret_val




    def max_id_num(self):
        """
        Get the max ID number.
        """
        ret_val = self._wrapper.max_id_num()
        return ret_val




    def num_fields(self):
        """
        Get the field number.
        """
        ret_val = self._wrapper.num_fields()
        return ret_val




    def num_records(self):
        """
        Get the record number.
        """
        ret_val = self._wrapper.num_records()
        return ret_val




    def type(self):
        """
        Get the `GXSHP` object's geometry type.
        """
        ret_val = self._wrapper.type()
        return ret_val



    @classmethod
    def open(cls, name):
        """
        Open an old `GXSHP` object
        """
        ret_val = gxapi_cy.WrapSHP.open(GXContext._get_tls_geo(), name.encode())
        return GXSHP(ret_val)




    def set_arc(self, v_vx, v_vy):
        """
        Write an XY arc (polyline) item.

        **Note:**

        Can ONLY be used for `SHP_GEOM_TYPE_ARC` files.
        """
        self._wrapper.set_arc(v_vx._wrapper, v_vy._wrapper)
        




    def set_arc_z(self, v_vx, v_vy, v_vz):
        """
        Write an XYZ arc (polyline) item.

        **Note:**

        Can ONLY be used for `SHP_GEOM_TYPE_ARCZ` files.
        """
        self._wrapper.set_arc_z(v_vx._wrapper, v_vy._wrapper, v_vz._wrapper)
        




    def set_int(self, index, val):
        """
        Set a data value to a int.

        **Note:**

        The input value is converted to the field's data type.
        """
        self._wrapper.set_int(index, val)
        




    def set_ipj(self, ipj):
        """
        Set a `GXSHP` object's projection.

        **Note:**

        If the `GXSHP` object has a projection, and it
        is not `IPJ_TYPE_NONE`, then it will be output
        to a file with the .prj extension when the
        first object is output.
        This function should be called BEFORE the first
        object is written.
        """
        self._wrapper.set_ipj(ipj._wrapper)
        




    def set_point(self, x, y):
        """
        Write an XY point item.

        **Note:**

        Can ONLY be used for `SHP_GEOM_TYPE_POINT` files.
        """
        self._wrapper.set_point(x, y)
        




    def set_point_z(self, x, y, z):
        """
        Write an XYZ point item.

        **Note:**

        Can ONLY be used for `SHP_GEOM_TYPE_POINTZ` files.
        """
        self._wrapper.set_point_z(x, y, z)
        




    def set_polygon(self, v_vx, v_vy, inclusive):
        """
        Write an XY polygon item.

        **Note:**

        Can ONLY be used for `SHP_GEOM_TYPE_POLYGON` files.
        """
        self._wrapper.set_polygon(v_vx._wrapper, v_vy._wrapper, inclusive)
        




    def set_polygon_z(self, v_vx, v_vy, v_vz, inclusive):
        """
        Write an XYZ polygon item.

        **Note:**

        Can ONLY be used for `SHP_GEOM_TYPE_POLYGONZ` files.
        """
        self._wrapper.set_polygon_z(v_vx._wrapper, v_vy._wrapper, v_vz._wrapper, inclusive)
        




    def set_double(self, index, val):
        """
        Set a data value to a real.

        **Note:**

        The input value is converted to the field's data type.
        """
        self._wrapper.set_double(index, val)
        




    def set_string(self, index, str_val):
        """
        Set a data value to a string.

        **Note:**

        The input string is converted to the field's data type.
        """
        self._wrapper.set_string(index, str_val.encode())
        




    def write_item(self):
        """
        Output the current item and data.

        **Note:**

        The currently stored `GXSHP` item and data are written to the
        `GXSHP` geometry and data files. (If no data fields have been
        defined, then the data file is not written).
        """
        self._wrapper.write_item()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer