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
class GXDMPPLY:
    """
    GXDMPPLY class.

    Datamine Multiple polygon object
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDMPPLY(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDMPPLY`
        
        :returns: A null `GXDMPPLY`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDMPPLY` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDMPPLY`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self):
        """
        Clear/remove all polygons from the `GXDMPPLY`.
        """
        self._wrapper.clear()
        




    def copy(self, p2):
        """
        Copy
        """
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls):
        """
        Creates a `GXDMPPLY` object.
        """
        ret_val = gxapi_cy.WrapDMPPLY.create(GXContext._get_tls_geo())
        return GXDMPPLY(ret_val)






    def get_azimuth(self, p2, p3):
        """
        Get the azimuth of a given polygon.

        **Note:**

        The azimuth is the equivalent section azimuth,
        equal to the azimuth of the normal vector plus
        90 degrees.
        """
        p3.value = self._wrapper.get_azimuth(p2, p3.value)
        




    def get_extents(self, p2, p3, p4, p5, p6, p7):
        """
        Get the center, width and height of a given polygon.
        """
        p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_extents(p2, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_joins(self, p2, p3):
        """
        Get join lines for each vertex in a specific polygon.

        **Note:**

        If a specific vertex is not joined, the returned value is 0.
        If the vertex is joined, then the index of the join line (1 to NJoins)
        is returned.
        """
        self._wrapper.get_joins(p2, p3._wrapper)
        




    def get_normal_vectors(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Get the normal vectors of a given polygon.

        **Note:**

        Three normalized vectors are returned.
        The first is horizontal, in the plane of the polygon.
        The second is in the vertical plane, corresponding to the
        "down-dip" direction.
        The third is the normal vector to the polygon plane.
        """
        p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value = self._wrapper.get_normal_vectors(p2, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value)
        




    def get_poly(self, p2, p3, p4, p5):
        """
        Get a specific polygon from a `GXDMPPLY` object.

        **Note:**

        Get the number of points from the `GXVV` length.
        """
        self._wrapper.get_poly(p2, p3._wrapper, p4._wrapper, p5._wrapper)
        




    def get_swing(self, p2, p3):
        """
        Get the swing of a given polygon.

        **Note:**

        The swing is the equivalent section swing,
        equal to zero for vertical plates, and increasing
        as the normal vector goes from horizontal upward.
        """
        p3.value = self._wrapper.get_swing(p2, p3.value)
        




    def get_vertex(self, p2, p3, p4, p5, p6):
        """
        Get a vertex location from a `GXDMPPLY` object.
        """
        p4.value, p5.value, p6.value = self._wrapper.get_vertex(p2, p3, p4.value, p5.value, p6.value)
        




    def num_joins(self):
        """
        Get the number of joining lines in a `GXDMPPLY` object.
        """
        ret_val = self._wrapper.num_joins()
        return ret_val




    def num_polys(self):
        """
        Get the number of polygons in a `GXDMPPLY` object.

        **Note:**

        The value returned is the "NP" used in function descriptions
        below.
        """
        ret_val = self._wrapper.num_polys()
        return ret_val




    def num_vertices(self, p2):
        """
        Get the number of vertices in a polygon.

        **Note:**

        The value returned is the "NV" used in function descriptions
        below.
        """
        ret_val = self._wrapper.num_vertices(p2)
        return ret_val




    def load(self, p2):
        """
        Loads a Datamine polygon file.
        """
        self._wrapper.load(p2.encode())
        




    def move_vertex(self, p2, p3, p4, p5, p6):
        """
        Moves a vertex and any associated lines.
        """
        self._wrapper.move_vertex(p2, p3, p4, p5, p6)
        




    def project_poly(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Project a polygon onto a vertical plane.

        **Note:**

        Gives the location in plane coordinates of a selected polygon,
        after it has been projected perpendicularly onto the plane.
        
        Plane coodinates: X - horizontal in plane
                          Y - "vertical" in plane (can be a swing)
                          Z - horizontal, "perpendicular" to plane (RH)
        """
        self._wrapper.project_poly(p2, p3, p4, p5, p6, p7, p8._wrapper, p9._wrapper, p10._wrapper)
        




    def re_project_poly(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Recover polygon locations from 2D locations on vertical plane.

        **Note:**

        This is the inverse operation of `project_poly`.
        
        Input the 2D locations on the projected vertical plane. These locations
        are projected back onto the original polygon plane.
        """
        self._wrapper.re_project_poly(p2, p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper)
        




    def save(self, p2):
        """
        Save to a Datamine polygon file
        """
        self._wrapper.save(p2.encode())
        




    def set_poly(self, p2, p3, p4, p5):
        """
        Set a specific polygon into a `GXDMPPLY` object.

        **Note:**

        Get the number of points from the `GXVV` length.
        """
        self._wrapper.set_poly(p2, p3._wrapper, p4._wrapper, p5._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer