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
class GXTIN:
    """
    GXTIN class.

    The `GXTIN` class calculates the Delaunay triangulation of the
    positions in a database. This is the "best" set of triangles
    that can be formed from irregularly distributed points. The
    serialized `GXTIN` files can be used for gridding using the
    Tin-based Nearest Neighbour Algorithm, or for plotting the
    Delaunay triangles or Voronoi cells to a map.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTIN(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTIN`
        
        :returns: A null `GXTIN`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXTIN` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXTIN`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def copy(self, p2):
        """
        Copy `GXTIN`
        """
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls, p1, p2, p3):
        """
        This method creates a `GXTIN` object.

        **Note:**

        CreateTIN does the `GXTIN` calculation.
        The Z values are not required, and a 0-length `GXVV` can be used to indicate
        the values are not to be used.
        """
        ret_val = gxapi_cy.WrapTIN.create(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        return GXTIN(ret_val)



    @classmethod
    def create_s(cls, p1):
        """
        Create `GXTIN` from a serialized source
        """
        ret_val = gxapi_cy.WrapTIN.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXTIN(ret_val)





    @classmethod
    def export_xml(cls, p1, p2, p3):
        """
        Export a `GXTIN` object as XML
        """
        p2.value = gxapi_cy.WrapTIN.export_xml(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.encode())
        




    def get_convex_hull(self, p2):
        """
        Get the convex hull of the `GXTIN`.

        **Note:**

        The convex hull is the outside boundary of the
        triangulated region.
        """
        self._wrapper.get_convex_hull(p2._wrapper)
        




    def get_ipj(self, p2):
        """
        Get the projection.
        """
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_joins(self, p2, p3, p4):
        """
        Get joins from a `GXTIN` mesh.

        **Note:**

        The join information is returned in three VVs.
        
            - The joins `GXVV` is a list off the adjacent nodes for
              each node, arranged for 1st node, 2nd node etc.
            - The index `GXVV` gives the starting index in the
              joins `GXVV` for the adjacent nodes to each node.
            - The number `GXVV` gives the number of adjacent nodes
              for each node.
        
        All VVs must be type `GS_LONG`.
        """
        self._wrapper.get_joins(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def get_mesh(self, p2):
        """
        Get lines from a `GXTIN` mesh.
        """
        self._wrapper.get_mesh(p2._wrapper)
        




    def get_nodes(self, p2, p3, p4):
        """
        Get the X,Y locations and Z values of the `GXTIN` nodes.

        **Note:**

        If this is not a Z-valued `GXTIN`, the Z values will
        be dummies.
        """
        self._wrapper.get_nodes(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def get_triangles(self, p2, p3, p4):
        """
        Get the triangle nodes.
        """
        self._wrapper.get_triangles(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def get_triangle(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Get the locations of the vertices of a specific triangle
        """
        p3.value, p4.value, p5.value, p6.value, p7.value, p8.value = self._wrapper.get_triangle(p2, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value)
        




    def get_voronoi_edges(self, p2):
        """
        Get line segments defining Voronoi cells.
        """
        self._wrapper.get_voronoi_edges(p2._wrapper)
        




    def is_z_valued(self):
        """
        Does the `GXTIN` contain Z values with each X,Y?
        """
        ret_val = self._wrapper.is_z_valued()
        return ret_val




    def locate_triangle(self, p2, p3, p4):
        """
        Get the index of the triangle containing X, Y.

        **Note:**

        Index returned begins at 0, but could be negative.
        
            -1: If X,Y is not contained in a triangle (or triangle not found)
        
            -2: If the location is on an edge
                This is for "fall-back" purposes only.
        
                Frequently edge positions are located as being part of
                a triangle, so do not rely on this result to determine
                if a node position is on an edge.
        
            -3: If the location is a vertex.
                This is for "fall-back" purposes only in the code.
                Normal operation is to include a node position
                inside a triangle, so do not rely on this result to determine
                if a node position is input.
        """
        ret_val = self._wrapper.locate_triangle(p2, p3, p4)
        return ret_val




    def nodes(self):
        """
        Returns the number of nodes in the `GXTIN`
        """
        ret_val = self._wrapper.nodes()
        return ret_val




    def interp_vv(self, p2, p3, p4):
        """
        Interp TINned values using the natural neighbour method.

        **Note:**

        The `GXTIN` have been created using max length = `rDUMMY` to
        ensure that the `GXTIN` has a convex hull (otherwise the
        routine that locates the triangle for a given location may fail).
        The `GXTIN` must also have been created using the Z values.
        Values located outside the convex hull are set to `rDUMMY`.
        The method is based on the following paper:
        
        Sambridge, M., Braun, J., and McQueen, H., 1995,
        Geophysical parameterization and interpolation of irregular
        data using natural neighbours:
        Geophysical Journal International, 122 p. 837-857.
        """
        self._wrapper.interp_vv(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def triangles(self):
        """
        Returns the number of triangles in the `GXTIN`.
        """
        ret_val = self._wrapper.triangles()
        return ret_val




    def linear_interp_vv(self, p2, p3, p4):
        """
        Interp TINned values using the linear interpolation

        **Note:**

        The `GXTIN` have been created using max length = `rDUMMY` to
        ensure that the `GXTIN` has a convex hull (otherwise the
        routine that locates the triangle for a given location may fail).
        The `GXTIN` must also have been created using the Z values.
        Values located outside the convex hull are set to `rDUMMY`.
        
        The values are set assuming that each `GXTIN` triangle defines a
        plane.
        """
        self._wrapper.linear_interp_vv(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def nearest_vv(self, p2, p3, p4):
        """
        Interp TINned values using the nearest neighbour.

        **Note:**

        The `GXTIN` have been created using max length = `rDUMMY` to
        ensure that the `GXTIN` has a convex hull (otherwise the
        routine that locates the triangle for a given location may fail).
        The `GXTIN` must also have been created using the Z values.
        Values located outside the convex hull are set to `rDUMMY`.
        
        Within each voronoi triangle, the Z value of node closest to the input
        X,Y location is returned.
        """
        self._wrapper.nearest_vv(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def range_xy(self, p2, p3, p4, p5):
        """
        Find the range in X and Y of the TINned region.

        **Note:**

        The TINned range is the range of X and Y covered by
        the `GXTIN` triangles. It can thus be less than the full
        X and Y range of the nodes themselves, if a full
        convex hull is not calculated.
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.range_xy(p2.value, p3.value, p4.value, p5.value)
        




    def serial(self, p2):
        """
        Serialize `GXTIN`
        """
        self._wrapper.serial(p2._wrapper)
        




    def set_ipj(self, p2):
        """
        Set the projection.
        """
        self._wrapper.set_ipj(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer