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



    def add_polygon(self, v_vx, v_vy):
        """
        Add a polygon to the polygon file.
        """
        self._wrapper.add_polygon(v_vx._wrapper, v_vy._wrapper)
        




    def add_polygon_ex(self, v_vx, v_vy, exclude):
        """
        Add a polygon to the polygon file.
        """
        self._wrapper.add_polygon_ex(v_vx._wrapper, v_vy._wrapper, exclude)
        




    def change_ipj(self, ipj):
        """
        Set the projection.

        **Note:**

        The `GXPLY` is re-projected to the new projection.
        """
        self._wrapper.change_ipj(ipj._wrapper)
        




    def clear(self):
        """
        Clear/remove all polygons from the `GXPLY`.
        """
        self._wrapper.clear()
        




    def copy(self, srce):
        """
        Destroys a `GXPLY` Object
        """
        self._wrapper.copy(srce._wrapper)
        



    @classmethod
    def create(cls):
        """
        Creates a Polygon Object.
        """
        ret_val = gxapi_cy.WrapPLY.create(GXContext._get_tls_geo())
        return GXPLY(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create an `GXPLY` Object from a `GXBF`
        """
        ret_val = gxapi_cy.WrapPLY.create_s(GXContext._get_tls_geo(), bf._wrapper)
        return GXPLY(ret_val)






    def extent(self, min_x, min_y, max_x, max_y):
        """
        Get the extent of the current polygon.

        **Note:**

        If there are no polygons in the `GXPLY` object, returns dummies.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.extent(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_ipj(self, ipj):
        """
        Get the projection.
        """
        self._wrapper.get_ipj(ipj._wrapper)
        




    def get_polygon(self, v_vx, v_vy, poly):
        """
        Get a polygon from the `GXPLY`
        """
        self._wrapper.get_polygon(v_vx._wrapper, v_vy._wrapper, poly)
        




    def get_polygon_ex(self, v_vx, v_vy, poly, exclude):
        """
        Get a polygon from the `GXPLY`
        """
        exclude.value = self._wrapper.get_polygon_ex(v_vx._wrapper, v_vy._wrapper, poly, exclude.value)
        




    def clip_area(self, min_x, min_y, max_x, max_y):
        """
        Clip a polygon to an area
        """
        ret_val = self._wrapper.clip_area(min_x, min_y, max_x, max_y)
        return ret_val




    def clip_line_int(self, min_x, min_y, max_x, max_y, vv, inc, p8):
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
        ret_val, p8.value = self._wrapper.clip_line_int(min_x, min_y, max_x, max_y, vv._wrapper, inc, p8.value)
        return ret_val




    def clip_ply(self, ppl_yb, ppl_yc):
        """
        Clip one polygon against another

        **Note:**

        Resulting clipped polygon only has inclusive
        regions of the clipped area.  Exclusion polygons
        are treated as included areas.
        """
        ret_val = self._wrapper.clip_ply(ppl_yb._wrapper, ppl_yc._wrapper)
        return ret_val




    def get_description(self, desc):
        """
        Get the `GXPLY` description string
        """
        desc.value = self._wrapper.get_description(desc.value.encode())
        




    def num_poly(self):
        """
        Get the number of polygons.
        """
        ret_val = self._wrapper.num_poly()
        return ret_val




    def load_table(self, table):
        """
        Loads Polygons from a Polygon file.
        """
        self._wrapper.load_table(table.encode())
        




    def area(self):
        """
        Compute the Area of a polygon

        **Note:**

        Excluded polygons have negative area.
        """
        ret_val = self._wrapper.area()
        return ret_val




    def rectangle(self, min_x, min_y, max_x, max_y):
        """
        Creates a polygon from a rectangular area.
        """
        self._wrapper.rectangle(min_x, min_y, max_x, max_y)
        




    def rotate(self, x, y, rot):
        """
        Rotate a polygon about a point.
        """
        self._wrapper.rotate(x, y, rot)
        




    def save_table(self, table):
        """
        Save Polygons to a Polygon file.
        """
        self._wrapper.save_table(table.encode())
        




    def serial(self, bf):
        """
        Serialize an `GXPLY` to a `GXBF`
        """
        self._wrapper.serial(bf._wrapper)
        




    def set_description(self, desc):
        """
        Set the `GXPLY` description string
        """
        self._wrapper.set_description(desc.encode())
        




    def set_ipj(self, ipj):
        """
        Set the projection.

        **Note:**

        This changes the projection information only.
        """
        self._wrapper.set_ipj(ipj._wrapper)
        




    def thin(self, thin):
        """
        Thin polygons to a desired resolution

        **Note:**

        Points on the polygon that deviate from a line drawn between
        neighboring points by more than the thining resolution will
        be removed.
        """
        self._wrapper.thin(thin)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer