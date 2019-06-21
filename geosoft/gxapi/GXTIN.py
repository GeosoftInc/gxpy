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
class GXTIN(gxapi_cy.WrapTIN):
    """
    GXTIN class.

    The `GXTIN <geosoft.gxapi.GXTIN>` class calculates the Delaunay triangulation of the
    positions in a database. This is the "best" set of triangles
    that can be formed from irregularly distributed points. The
    serialized `GXTIN <geosoft.gxapi.GXTIN>` files can be used for gridding using the
    Tin-based Nearest Neighbour Algorithm, or for plotting the
    Delaunay triangles or Voronoi cells to a map.
    """

    def __init__(self, handle=0):
        super(GXTIN, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTIN <geosoft.gxapi.GXTIN>`
        
        :returns: A null `GXTIN <geosoft.gxapi.GXTIN>`
        :rtype:   GXTIN
        """
        return GXTIN()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def copy(self, source):
        """
        Copy `GXTIN <geosoft.gxapi.GXTIN>`
        
        :param source:  Source `GXTIN <geosoft.gxapi.GXTIN>`
        :type  source:  GXTIN

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._copy(source)
        



    @classmethod
    def create(cls, vv_x, vv_y, vv_z):
        """
        This method creates a `GXTIN <geosoft.gxapi.GXTIN>` object.
        
        :param vv_x:  X positions
        :param vv_y:  Y positions
        :param vv_z:  Z values (optional)
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        :returns:     `GXTIN <geosoft.gxapi.GXTIN>` Object
        :rtype:       GXTIN

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** CreateTIN does the `GXTIN <geosoft.gxapi.GXTIN>` calculation.
        The Z values are not required, and a 0-length `GXVV <geosoft.gxapi.GXVV>` can be used to indicate
        the values are not to be used.
        """
        ret_val = gxapi_cy.WrapTIN._create(GXContext._get_tls_geo(), vv_x, vv_y, vv_z)
        return GXTIN(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create `GXTIN <geosoft.gxapi.GXTIN>` from a serialized source
        
        :param bf:  `GXBF <geosoft.gxapi.GXBF>` from which to read `GXTIN <geosoft.gxapi.GXTIN>`
        :type  bf:  GXBF

        :returns:    `GXTIN <geosoft.gxapi.GXTIN>` Object
        :rtype:      GXTIN

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapTIN._create_s(GXContext._get_tls_geo(), bf)
        return GXTIN(ret_val)





    @classmethod
    def export_xml(cls, tin, crc, file):
        """
        Export a `GXTIN <geosoft.gxapi.GXTIN>` object as XML
        
        :param tin:   `GXTIN <geosoft.gxapi.GXTIN>` file
        :param crc:   CRC returned (Currently this is not implemented)
        :param file:  Output XML file
        :type  tin:   str
        :type  crc:   int_ref
        :type  file:  str

        .. versionadded:: 6.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        crc.value = gxapi_cy.WrapTIN._export_xml(GXContext._get_tls_geo(), tin.encode(), crc.value, file.encode())
        




    def get_convex_hull(self, ply):
        """
        Get the convex hull of the `GXTIN <geosoft.gxapi.GXTIN>`.
        
        :param ply:  `GXPLY <geosoft.gxapi.GXPLY>` object
        :type  ply:  GXPLY

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The convex hull is the outside boundary of the
        triangulated region.
        """
        self._get_convex_hull(ply)
        




    def get_ipj(self, ipj):
        """
        Get the projection.
        
        :param ipj:  `GXIPJ <geosoft.gxapi.GXIPJ>` in which to place the `GXTIN <geosoft.gxapi.GXTIN>` projection
        :type  ipj:  GXIPJ

        .. versionadded:: 5.0.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._get_ipj(ipj)
        




    def get_joins(self, vv_joins, vv_index, vv_num):
        """
        Get joins from a `GXTIN <geosoft.gxapi.GXTIN>` mesh.
        
        :param vv_joins:  Joins `GXVV <geosoft.gxapi.GXVV>` (adjacent nodes)
        :param vv_index:  Index `GXVV <geosoft.gxapi.GXVV>`
        :param vv_num:    Number `GXVV <geosoft.gxapi.GXVV>`
        :type  vv_joins:  GXVV
        :type  vv_index:  GXVV
        :type  vv_num:    GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The join information is returned in three VVs.

            - The joins `GXVV <geosoft.gxapi.GXVV>` is a list off the adjacent nodes for
              each node, arranged for 1st node, 2nd node etc.
            - The index `GXVV <geosoft.gxapi.GXVV>` gives the starting index in the
              joins `GXVV <geosoft.gxapi.GXVV>` for the adjacent nodes to each node.
            - The number `GXVV <geosoft.gxapi.GXVV>` gives the number of adjacent nodes
              for each node.

        All VVs must be type `GS_LONG <geosoft.gxapi.GS_LONG>`.
        """
        self._get_joins(vv_joins, vv_index, vv_num)
        




    def get_mesh(self, vv):
        """
        Get lines from a `GXTIN <geosoft.gxapi.GXTIN>` mesh.
        
        :param vv:   `GXVV <geosoft.gxapi.GXVV>` of type GS_D2LINE (returned)
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._get_mesh(vv)
        




    def get_nodes(self, vvx, vvy, vvz):
        """
        Get the X,Y locations and Z values of the `GXTIN <geosoft.gxapi.GXTIN>` nodes.
        
        :param vvx:  X `GXVV <geosoft.gxapi.GXVV>`
        :param vvy:  Y `GXVV <geosoft.gxapi.GXVV>`
        :param vvz:  Z `GXVV <geosoft.gxapi.GXVV>`
        :type  vvx:  GXVV
        :type  vvy:  GXVV
        :type  vvz:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If this is not a Z-valued `GXTIN <geosoft.gxapi.GXTIN>`, the Z values will
        be dummies.
        """
        self._get_nodes(vvx, vvy, vvz)
        




    def get_triangles(self, tri_vv_pt1, tri_vv_pt2, tri_vv_pt3):
        """
        Get the triangle nodes.
        
        :param tri_vv_pt1:  Node 1 `GXVV <geosoft.gxapi.GXVV>`
        :param tri_vv_pt2:  Node 2 `GXVV <geosoft.gxapi.GXVV>`
        :param tri_vv_pt3:  Node3 `GXVV <geosoft.gxapi.GXVV>`
        :type  tri_vv_pt1:  GXVV
        :type  tri_vv_pt2:  GXVV
        :type  tri_vv_pt3:  GXVV

        .. versionadded:: 8.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._get_triangles(tri_vv_pt1, tri_vv_pt2, tri_vv_pt3)
        




    def get_triangle(self, index, x0, y0, x1, y1, x2, y2):
        """
        Get the locations of the vertices of a specific triangle
        
        :param index:  Triangle index [0...N-1]
        :param x0:     X0
        :param y0:     Y0
        :param x1:     X1
        :param y1:     Y1
        :param x2:     X2
        :param y2:     Y2
        :type  index:  int
        :type  x0:     float_ref
        :type  y0:     float_ref
        :type  x1:     float_ref
        :type  y1:     float_ref
        :type  x2:     float_ref
        :type  y2:     float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        x0.value, y0.value, x1.value, y1.value, x2.value, y2.value = self._get_triangle(index, x0.value, y0.value, x1.value, y1.value, x2.value, y2.value)
        




    def get_voronoi_edges(self, vv):
        """
        Get line segments defining Voronoi cells.
        
        :param vv:   `GXVV <geosoft.gxapi.GXVV>` of GS_D2LINE type (create with type -32)
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._get_voronoi_edges(vv)
        




    def is_z_valued(self):
        """
        Does the `GXTIN <geosoft.gxapi.GXTIN>` contain Z values with each X,Y?
        

        :returns:    Returns 1 if Z values are defined in the `GXTIN <geosoft.gxapi.GXTIN>`
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._is_z_valued()
        return ret_val




    def locate_triangle(self, t, x, y):
        """
        Get the index of the triangle containing X, Y.
        
        :param t:    Seed triangle (can be iDummy or <0)
        :param x:    Target X location
        :param y:    Target Y location
        :type  t:    int
        :type  x:    float
        :type  y:    float

        :returns:    The index of the triangle containing X, Y.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Index returned begins at 0, but could be negative.

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
        ret_val = self._locate_triangle(t, x, y)
        return ret_val




    def nodes(self):
        """
        Returns the number of nodes in the `GXTIN <geosoft.gxapi.GXTIN>`
        

        :returns:    The number of nodes in the `GXTIN <geosoft.gxapi.GXTIN>`
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._nodes()
        return ret_val




    def interp_vv(self, vvx, vvy, vvz):
        """
        Interp TINned values using the natural neighbour method.
        
        :param vvx:  `GXVV <geosoft.gxapi.GXVV>` X locations to interpolate (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :param vvy:  `GXVV <geosoft.gxapi.GXVV>` Y locations to interpolate (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :param vvz:  `GXVV <geosoft.gxapi.GXVV>` Interpolated Z values (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :type  vvx:  GXVV
        :type  vvy:  GXVV
        :type  vvz:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXTIN <geosoft.gxapi.GXTIN>` have been created using max length = `rDUMMY <geosoft.gxapi.rDUMMY>` to
        ensure that the `GXTIN <geosoft.gxapi.GXTIN>` has a convex hull (otherwise the
        routine that locates the triangle for a given location may fail).
        The `GXTIN <geosoft.gxapi.GXTIN>` must also have been created using the Z values.
        Values located outside the convex hull are set to `rDUMMY <geosoft.gxapi.rDUMMY>`.
        The method is based on the following paper:

        Sambridge, M., Braun, J., and McQueen, H., 1995,
        Geophysical parameterization and interpolation of irregular
        data using natural neighbours:
        Geophysical Journal International, 122 p. 837-857.
        """
        self._interp_vv(vvx, vvy, vvz)
        




    def triangles(self):
        """
        Returns the number of triangles in the `GXTIN <geosoft.gxapi.GXTIN>`.
        

        :returns:    The number of triangles in the `GXTIN <geosoft.gxapi.GXTIN>`
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._triangles()
        return ret_val




    def linear_interp_vv(self, vvx, vvy, vvz):
        """
        Interp TINned values using the linear interpolation
        
        :param vvx:  `GXVV <geosoft.gxapi.GXVV>` X locations to interpolate (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :param vvy:  `GXVV <geosoft.gxapi.GXVV>` Y locations to interpolate (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :param vvz:  `GXVV <geosoft.gxapi.GXVV>` Interpolated Z values (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :type  vvx:  GXVV
        :type  vvy:  GXVV
        :type  vvz:  GXVV

        .. versionadded:: 5.1.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXTIN <geosoft.gxapi.GXTIN>` have been created using max length = `rDUMMY <geosoft.gxapi.rDUMMY>` to
        ensure that the `GXTIN <geosoft.gxapi.GXTIN>` has a convex hull (otherwise the
        routine that locates the triangle for a given location may fail).
        The `GXTIN <geosoft.gxapi.GXTIN>` must also have been created using the Z values.
        Values located outside the convex hull are set to `rDUMMY <geosoft.gxapi.rDUMMY>`.

        The values are set assuming that each `GXTIN <geosoft.gxapi.GXTIN>` triangle defines a
        plane.
        """
        self._linear_interp_vv(vvx, vvy, vvz)
        




    def nearest_vv(self, vvx, vvy, vvz):
        """
        Interp TINned values using the nearest neighbour.
        
        :param vvx:  `GXVV <geosoft.gxapi.GXVV>` X locations to interpolate (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :param vvy:  `GXVV <geosoft.gxapi.GXVV>` Y locations to interpolate (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :param vvz:  `GXVV <geosoft.gxapi.GXVV>` Interpolated Z values (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :type  vvx:  GXVV
        :type  vvy:  GXVV
        :type  vvz:  GXVV

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXTIN <geosoft.gxapi.GXTIN>` have been created using max length = `rDUMMY <geosoft.gxapi.rDUMMY>` to
        ensure that the `GXTIN <geosoft.gxapi.GXTIN>` has a convex hull (otherwise the
        routine that locates the triangle for a given location may fail).
        The `GXTIN <geosoft.gxapi.GXTIN>` must also have been created using the Z values.
        Values located outside the convex hull are set to `rDUMMY <geosoft.gxapi.rDUMMY>`.

        Within each voronoi triangle, the Z value of node closest to the input
        X,Y location is returned.
        """
        self._nearest_vv(vvx, vvy, vvz)
        




    def range_xy(self, x_min, y_min, x_max, y_max):
        """
        Find the range in X and Y of the TINned region.
        
        :param x_min:  Min X  (returned)
        :param y_min:  Min Y
        :param x_max:  Max X
        :param y_max:  Max Y
        :type  x_min:  float_ref
        :type  y_min:  float_ref
        :type  x_max:  float_ref
        :type  y_max:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The TINned range is the range of X and Y covered by
        the `GXTIN <geosoft.gxapi.GXTIN>` triangles. It can thus be less than the full
        X and Y range of the nodes themselves, if a full
        convex hull is not calculated.
        """
        x_min.value, y_min.value, x_max.value, y_max.value = self._range_xy(x_min.value, y_min.value, x_max.value, y_max.value)
        




    def serial(self, bf):
        """
        Serialize `GXTIN <geosoft.gxapi.GXTIN>`
        
        :param bf:   `GXBF <geosoft.gxapi.GXBF>` in which to write `GXTIN <geosoft.gxapi.GXTIN>`
        :type  bf:   GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._serial(bf)
        




    def set_ipj(self, ipj):
        """
        Set the projection.
        
        :param ipj:  `GXIPJ <geosoft.gxapi.GXIPJ>` to place in the `GXTIN <geosoft.gxapi.GXTIN>`
        :type  ipj:  GXIPJ

        .. versionadded:: 5.0.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_ipj(ipj)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer