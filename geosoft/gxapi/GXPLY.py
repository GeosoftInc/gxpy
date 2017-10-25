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
class GXPLY:
    """
    GXPLY class.

    The `GXPLY` object contains the definitions for one or more
    polygons, and does import and export of polygon files.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPLY(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPLY`
        
        :returns: A null `GXPLY`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXPLY` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXPLY`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_polygon(self, p2, p3):
        """
        Add a polygon to the polygon file.
        """
        self._wrapper.add_polygon(p2._wrapper, p3._wrapper)
        




    def add_polygon_ex(self, p2, p3, p4):
        """
        Add a polygon to the polygon file.
        """
        self._wrapper.add_polygon_ex(p2._wrapper, p3._wrapper, p4)
        




    def change_ipj(self, p2):
        """
        Set the projection.

        **Note:**

        The `GXPLY` is re-projected to the new projection.
        """
        self._wrapper.change_ipj(p2._wrapper)
        




    def clear(self):
        """
        Clear/remove all polygons from the `GXPLY`.
        """
        self._wrapper.clear()
        




    def copy(self, p2):
        """
        Destroys a `GXPLY` Object
        """
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls):
        """
        Creates a Polygon Object.
        """
        ret_val = gxapi_cy.WrapPLY.create(GXContext._get_tls_geo())
        return GXPLY(ret_val)



    @classmethod
    def create_s(cls, p1):
        """
        Create an `GXPLY` Object from a `GXBF`
        """
        ret_val = gxapi_cy.WrapPLY.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXPLY(ret_val)






    def extent(self, p2, p3, p4, p5):
        """
        Get the extent of the current polygon.

        **Note:**

        If there are no polygons in the `GXPLY` object, returns dummies.
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.extent(p2.value, p3.value, p4.value, p5.value)
        




    def get_ipj(self, p2):
        """
        Get the projection.
        """
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_polygon(self, p2, p3, p4):
        """
        Get a polygon from the `GXPLY`
        """
        self._wrapper.get_polygon(p2._wrapper, p3._wrapper, p4)
        




    def get_polygon_ex(self, p2, p3, p4, p5):
        """
        Get a polygon from the `GXPLY`
        """
        p5.value = self._wrapper.get_polygon_ex(p2._wrapper, p3._wrapper, p4, p5.value)
        




    def clip_area(self, p2, p3, p4, p5):
        """
        Clip a polygon to an area
        """
        ret_val = self._wrapper.clip_area(p2, p3, p4, p5)
        return ret_val




    def clip_line_int(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Clips a line in or out of the polygons for intersections (`GS_DOUBLE`).
        Intersections are returned as fiducials down the line stored in `GXVV`
        starting at the first point of the line.
        Examples:
        No intersection: `PLY_LINE_CLIP_OUTSIDE`, 0 intersections
        Starts outside, ends inside: `PLY_LINE_CLIP_OUTSIDE`, 1 intersection
        Starts outside, intersects then ends inside or outside: `PLY_LINE_CLIP_OUTSIDE`, 2 intersections
        Starts inside, ends inside : `PLY_LINE_CLIP_INSIDE`, 1 intersection (gives end-of-line)
        Starts inside, ends outside : `PLY_LINE_CLIP_INSIDE`, 1 intersection
        """
        ret_val, p8.value = self._wrapper.clip_line_int(p2, p3, p4, p5, p6._wrapper, p7, p8.value)
        return ret_val




    def clip_ply(self, p2, p3):
        """
        Clip one polygon against another

        **Note:**

        Resulting clipped polygon only has inclusive
        regions of the clipped area.  Exclusion polygons
        are treated as included areas.
        """
        ret_val = self._wrapper.clip_ply(p2._wrapper, p3._wrapper)
        return ret_val




    def get_description(self, p2):
        """
        Get the `GXPLY` description string
        """
        p2.value = self._wrapper.get_description(p2.value.encode())
        




    def num_poly(self):
        """
        Get the number of polygons.
        """
        ret_val = self._wrapper.num_poly()
        return ret_val




    def load_table(self, p2):
        """
        Loads Polygons from a Polygon file.
        """
        self._wrapper.load_table(p2.encode())
        




    def area(self):
        """
        Compute the Area of a polygon

        **Note:**

        Excluded polygons have negative area.
        """
        ret_val = self._wrapper.area()
        return ret_val




    def rectangle(self, p2, p3, p4, p5):
        """
        Creates a polygon from a rectangular area.
        """
        self._wrapper.rectangle(p2, p3, p4, p5)
        




    def rotate(self, p2, p3, p4):
        """
        Rotate a polygon about a point.
        """
        self._wrapper.rotate(p2, p3, p4)
        




    def save_table(self, p2):
        """
        Save Polygons to a Polygon file.
        """
        self._wrapper.save_table(p2.encode())
        




    def serial(self, p2):
        """
        Serialize an `GXPLY` to a `GXBF`
        """
        self._wrapper.serial(p2._wrapper)
        




    def set_description(self, p2):
        """
        Set the `GXPLY` description string
        """
        self._wrapper.set_description(p2.encode())
        




    def set_ipj(self, p2):
        """
        Set the projection.

        **Note:**

        This changes the projection information only.
        """
        self._wrapper.set_ipj(p2._wrapper)
        




    def thin(self, p2):
        """
        Thin polygons to a desired resolution

        **Note:**

        Points on the polygon that deviate from a line drawn between
        neighboring points by more than the thining resolution will
        be removed.
        """
        self._wrapper.thin(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer