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
class GXSHP(gxapi_cy.WrapSHP):
    """
    GXSHP class.

    The `GXSHP <geosoft.gxapi.GXSHP>` class is used to create ESRI shape files.

    **Note:**

    Shape files contain a single "geometry" type, e.g.
    points, arcs or polygons. They may be accompanied by
    a DBF file containing attribute data.
    """

    def __init__(self, handle=0):
        super(GXSHP, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSHP <geosoft.gxapi.GXSHP>`
        
        :returns: A null `GXSHP <geosoft.gxapi.GXSHP>`
        :rtype:   GXSHP
        """
        return GXSHP()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def append_item(self):
        """
        Append the current item and data to an old `GXSHP <geosoft.gxapi.GXSHP>` object.
        

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The currently stored `GXSHP <geosoft.gxapi.GXSHP>` item and data are written to the
        `GXSHP <geosoft.gxapi.GXSHP>` geometry and data files. (If no data fields have been
        defined, then the data file is not written).
        """
        self._append_item()
        



    @classmethod
    def create(cls, name, type):
        """
        Create a new `GXSHP <geosoft.gxapi.GXSHP>` object
        
        :param name:  File name
        :param type:  :ref:`SHP_GEOM_TYPE`
        :type  name:  str
        :type  type:  int

        :returns:     `GXSHP <geosoft.gxapi.GXSHP>` object
        :rtype:       GXSHP

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The file name is used to create the various files. The
        file type and extension are added:

        e.g. "filename.shp",
             "filename.dbf"

        The following geometry types are currently supported:

        Type                    Required geometry function.

        `SHP_GEOM_TYPE_POINT <geosoft.gxapi.SHP_GEOM_TYPE_POINT>`     `set_point <geosoft.gxapi.GXSHP.set_point>`
        `SHP_GEOM_TYPE_ARC <geosoft.gxapi.SHP_GEOM_TYPE_ARC>`       `set_arc <geosoft.gxapi.GXSHP.set_arc>`
        `SHP_GEOM_TYPE_POLYGON <geosoft.gxapi.SHP_GEOM_TYPE_POLYGON>`   `set_polygon <geosoft.gxapi.GXSHP.set_polygon>`

        `SHP_GEOM_TYPE_POINTZ <geosoft.gxapi.SHP_GEOM_TYPE_POINTZ>`    `set_point_z <geosoft.gxapi.GXSHP.set_point_z>`
        `SHP_GEOM_TYPE_ARCZ <geosoft.gxapi.SHP_GEOM_TYPE_ARCZ>`      `set_arc_z <geosoft.gxapi.GXSHP.set_arc_z>`
        `SHP_GEOM_TYPE_POLYGONZ <geosoft.gxapi.SHP_GEOM_TYPE_POLYGONZ>`  `set_polygon_z <geosoft.gxapi.GXSHP.set_polygon_z>`
        """
        ret_val = gxapi_cy.WrapSHP._create(GXContext._get_tls_geo(), name.encode(), type)
        return GXSHP(ret_val)






    def add_int_field(self, field):
        """
        Add an INT type data field to a shape file
        
        :param field:  Field name
        :type  field:  str

        :returns:      Index of the new field
        :rtype:        int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The returned field index should be used with the SetXXX_SHP
        functions to set individual data values.
        """
        ret_val = self._add_int_field(field.encode())
        return ret_val




    def add_double_field(self, field, dec):
        """
        Add a REAL type data field to a shape file
        
        :param field:  Field name
        :param dec:    Number of decimal places
        :type  field:  str
        :type  dec:    int

        :returns:      Index of the new field
        :rtype:        int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The returned field index should be used with the SetXXX_SHP
        functions to set individual data values.
        """
        ret_val = self._add_double_field(field.encode(), dec)
        return ret_val




    def add_string_field(self, field, width):
        """
        Add a string type data field to a shape file
        
        :param field:  Field name
        :param width:  Maximum number of characters in the string
        :type  field:  str
        :type  width:  int

        :returns:      Index of the new field
        :rtype:        int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The returned field index should be used with the SetXXX_SHP
        functions to set individual data values.
        """
        ret_val = self._add_string_field(field.encode(), width)
        return ret_val




    def find_field(self, field):
        """
        Find the index for a data field.
        
        :param field:  Field name
        :type  field:  str

        :returns:      The index, -1 if not found.
        :rtype:        int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._find_field(field.encode())
        return ret_val




    def max_id_num(self):
        """
        Get the max ID number.
        

        :returns:    The max ID number.
        :rtype:      int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._max_id_num()
        return ret_val




    def num_fields(self):
        """
        Get the field number.
        

        :returns:    The field number.
        :rtype:      int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_fields()
        return ret_val




    def num_records(self):
        """
        Get the record number.
        

        :returns:    The record number.
        :rtype:      int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_records()
        return ret_val




    def type(self):
        """
        Get the `GXSHP <geosoft.gxapi.GXSHP>` object's geometry type.
        

        :returns:    The `GXSHP <geosoft.gxapi.GXSHP>` object's geometry type (:ref:`SHP_GEOM_TYPE`)
        :rtype:      int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._type()
        return ret_val



    @classmethod
    def open(cls, name):
        """
        Open an old `GXSHP <geosoft.gxapi.GXSHP>` object
        
        :param name:  File name
        :type  name:  str

        :returns:     `GXSHP <geosoft.gxapi.GXSHP>` object
        :rtype:       GXSHP

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSHP._open(GXContext._get_tls_geo(), name.encode())
        return GXSHP(ret_val)




    def set_arc(self, vv_x, vv_y):
        """
        Write an XY arc (polyline) item.
        
        :param vv_x:  X locations
        :param vv_y:  Y locations
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Can ONLY be used for `SHP_GEOM_TYPE_ARC <geosoft.gxapi.SHP_GEOM_TYPE_ARC>` files.
        """
        self._set_arc(vv_x, vv_y)
        




    def set_arc_z(self, vv_x, vv_y, vv_z):
        """
        Write an XYZ arc (polyline) item.
        
        :param vv_x:  X locations
        :param vv_y:  Y locations
        :param vv_z:  Z locations
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Can ONLY be used for `SHP_GEOM_TYPE_ARCZ <geosoft.gxapi.SHP_GEOM_TYPE_ARCZ>` files.
        """
        self._set_arc_z(vv_x, vv_y, vv_z)
        




    def set_int(self, index, val):
        """
        Set a data value to a int.
        
        :param index:  Data field index
        :param val:    Input int value
        :type  index:  int
        :type  val:    int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The input value is converted to the field's data type.
        """
        self._set_int(index, val)
        




    def set_ipj(self, ipj):
        """
        Set a `GXSHP <geosoft.gxapi.GXSHP>` object's projection.
        
        :param ipj:  Input `GXIPJ <geosoft.gxapi.GXIPJ>`
        :type  ipj:  GXIPJ

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the `GXSHP <geosoft.gxapi.GXSHP>` object has a projection, and it
        is not `IPJ_TYPE_NONE <geosoft.gxapi.IPJ_TYPE_NONE>`, then it will be output
        to a file with the .prj extension when the
        first object is output.
        This function should be called BEFORE the first
        object is written.
        """
        self._set_ipj(ipj)
        




    def set_point(self, x, y):
        """
        Write an XY point item.
        
        :param x:    X location
        :param y:    Y location
        :type  x:    float
        :type  y:    float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Can ONLY be used for `SHP_GEOM_TYPE_POINT <geosoft.gxapi.SHP_GEOM_TYPE_POINT>` files.
        """
        self._set_point(x, y)
        




    def set_point_z(self, x, y, z):
        """
        Write an XYZ point item.
        
        :param x:    X location
        :param y:    Y location
        :param z:    Z location
        :type  x:    float
        :type  y:    float
        :type  z:    float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Can ONLY be used for `SHP_GEOM_TYPE_POINTZ <geosoft.gxapi.SHP_GEOM_TYPE_POINTZ>` files.
        """
        self._set_point_z(x, y, z)
        




    def set_polygon(self, vv_x, vv_y, inclusive):
        """
        Write an XY polygon item.
        
        :param vv_x:       X locations
        :param vv_y:       Y locations
        :param inclusive:  ``True`` for outer ring polygon (inclusive/island), ``False`` for inner ring (exclusive/hole)
        :type  vv_x:       GXVV
        :type  vv_y:       GXVV
        :type  inclusive:  bool

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Can ONLY be used for `SHP_GEOM_TYPE_POLYGON <geosoft.gxapi.SHP_GEOM_TYPE_POLYGON>` files.
        """
        self._set_polygon(vv_x, vv_y, inclusive)
        




    def set_polygon_z(self, vv_x, vv_y, vv_z, inclusive):
        """
        Write an XYZ polygon item.
        
        :param vv_x:       X locations
        :param vv_y:       Y locations
        :param vv_z:       Z locations
        :param inclusive:  ``True`` for outer ring polygon (inclusive/island), ``False`` for inner ring (exclusive/hole)
        :type  vv_x:       GXVV
        :type  vv_y:       GXVV
        :type  vv_z:       GXVV
        :type  inclusive:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Can ONLY be used for `SHP_GEOM_TYPE_POLYGONZ <geosoft.gxapi.SHP_GEOM_TYPE_POLYGONZ>` files.
        """
        self._set_polygon_z(vv_x, vv_y, vv_z, inclusive)
        




    def set_double(self, index, val):
        """
        Set a data value to a real.
        
        :param index:  Data field index
        :param val:    Input real value
        :type  index:  int
        :type  val:    float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The input value is converted to the field's data type.
        """
        self._set_double(index, val)
        




    def set_string(self, index, str_val):
        """
        Set a data value to a string.
        
        :param index:    Data field index
        :param str_val:  Input string value
        :type  index:    int
        :type  str_val:  str

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The input string is converted to the field's data type.
        """
        self._set_string(index, str_val.encode())
        




    def write_item(self):
        """
        Output the current item and data.
        

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The currently stored `GXSHP <geosoft.gxapi.GXSHP>` item and data are written to the
        `GXSHP <geosoft.gxapi.GXSHP>` geometry and data files. (If no data fields have been
        defined, then the data file is not written).
        """
        self._write_item()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer