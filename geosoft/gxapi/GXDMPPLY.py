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
class GXDMPPLY(gxapi_cy.WrapDMPPLY):
    """
    GXDMPPLY class.

    Datamine Multiple polygon object
    """

    def __init__(self, handle=0):
        super(GXDMPPLY, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDMPPLY <geosoft.gxapi.GXDMPPLY>`
        
        :returns: A null `GXDMPPLY <geosoft.gxapi.GXDMPPLY>`
        :rtype:   GXDMPPLY
        """
        return GXDMPPLY()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def clear(self):
        """
        Clear/remove all polygons from the `GXDMPPLY <geosoft.gxapi.GXDMPPLY>`.
        

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._clear()
        




    def copy(self, source):
        """
        Copy
        
        :param source:  Source
        :type  source:  GXDMPPLY

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._copy(source)
        



    @classmethod
    def create(cls):
        """
        Creates a `GXDMPPLY <geosoft.gxapi.GXDMPPLY>` object.
        

        :returns:    DMPLY Object
        :rtype:      GXDMPPLY

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapDMPPLY._create(GXContext._get_tls_geo())
        return GXDMPPLY(ret_val)






    def get_azimuth(self, p, az):
        """
        Get the azimuth of a given polygon.
        
        :param p:       Polygon number (1 to NP)
        :param az:      Azimuth (degrees) (o)
        :type  p:       int
        :type  az:      float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The azimuth is the equivalent section azimuth,
        equal to the azimuth of the normal vector plus
        90 degrees.
        """
        az.value = self._get_azimuth(p, az.value)
        




    def get_extents(self, p, x, y, z, w, h):
        """
        Get the center, width and height of a given polygon.
        
        :param p:       Polygon number (1 to NP)
        :param x:       Center point X (o)
        :param y:       Center point Y (o)
        :param z:       Center point Z (o)
        :param w:       Width of polygon (in its plane) (o)
        :param h:       Height of polygon (Z extent) (o)
        :type  p:       int
        :type  x:       float_ref
        :type  y:       float_ref
        :type  z:       float_ref
        :type  w:       float_ref
        :type  h:       float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        x.value, y.value, z.value, w.value, h.value = self._get_extents(p, x.value, y.value, z.value, w.value, h.value)
        




    def get_joins(self, p, vv):
        """
        Get join lines for each vertex in a specific polygon.
        
        :param p:       Polygon number (1 to N)
        :param vv:      INT `GXVV <geosoft.gxapi.GXVV>` of join indices (1 to NJoins).
        :type  p:       int
        :type  vv:      GXVV

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If a specific vertex is not joined, the returned value is 0.
        If the vertex is joined, then the index of the join line (1 to NJoins)
        is returned.
        """
        self._get_joins(p, vv)
        




    def get_normal_vectors(self, p, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        """
        Get the normal vectors of a given polygon.
        
        :param p:       Polygon number (1 to NP)
        :param x1:      X component (o) (Horizontal azimuth vector)
        :param y1:      Y component (o)
        :param z1:      Z component (o)
        :param x2:      X component (o) (Down-dip, in the vertical plane)
        :param y2:      Y component (o)
        :param z2:      Z component (o)
        :param x3:      X component (o) (Normal vector)
        :param y3:      Y component (o)
        :param z3:      Z component (o)
        :type  p:       int
        :type  x1:      float_ref
        :type  y1:      float_ref
        :type  z1:      float_ref
        :type  x2:      float_ref
        :type  y2:      float_ref
        :type  z2:      float_ref
        :type  x3:      float_ref
        :type  y3:      float_ref
        :type  z3:      float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Three normalized vectors are returned.
        The first is horizontal, in the plane of the polygon.
        The second is in the vertical plane, corresponding to the
        "down-dip" direction.
        The third is the normal vector to the polygon plane.
        """
        x1.value, y1.value, z1.value, x2.value, y2.value, z2.value, x3.value, y3.value, z3.value = self._get_normal_vectors(p, x1.value, y1.value, z1.value, x2.value, y2.value, z2.value, x3.value, y3.value, z3.value)
        




    def get_poly(self, p, vv_x, vv_y, vv_z):
        """
        Get a specific polygon from a `GXDMPPLY <geosoft.gxapi.GXDMPPLY>` object.
        
        :param p:       Polygon number (1 to NP) (i)
        :param vv_x:    X Locations (o)
        :param vv_y:    Y Locations (o)
        :param vv_z:    Z Locations (o)
        :type  p:       int
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_z:    GXVV

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Get the number of points from the `GXVV <geosoft.gxapi.GXVV>` length.
        """
        self._get_poly(p, vv_x, vv_y, vv_z)
        




    def get_swing(self, p, az):
        """
        Get the swing of a given polygon.
        
        :param p:       Polygon number (1 to NP)
        :param az:      Swing (degrees) (o)
        :type  p:       int
        :type  az:      float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The swing is the equivalent section swing,
        equal to zero for vertical plates, and increasing
        as the normal vector goes from horizontal upward.
        """
        az.value = self._get_swing(p, az.value)
        




    def get_vertex(self, p, v, x, y, z):
        """
        Get a vertex location from a `GXDMPPLY <geosoft.gxapi.GXDMPPLY>` object.
        
        :param p:       Polygon number (1 to NP)
        :param v:       Vertex number (1 to NV)
        :param x:       X Location (o)
        :param y:       Y Location (o)
        :param z:       Z Location (o)
        :type  p:       int
        :type  v:       int
        :type  x:       float_ref
        :type  y:       float_ref
        :type  z:       float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        x.value, y.value, z.value = self._get_vertex(p, v, x.value, y.value, z.value)
        




    def num_joins(self):
        """
        Get the number of joining lines in a `GXDMPPLY <geosoft.gxapi.GXDMPPLY>` object.
        

        :returns:       Number of joining lines
        :rtype:         int

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._num_joins()
        return ret_val




    def num_polys(self):
        """
        Get the number of polygons in a `GXDMPPLY <geosoft.gxapi.GXDMPPLY>` object.
        

        :returns:       Number of polygons
        :rtype:         int

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The value returned is the "NP" used in function descriptions
        below.
        """
        ret_val = self._num_polys()
        return ret_val




    def num_vertices(self, p):
        """
        Get the number of vertices in a polygon.
        
        :param p:       Polygon number (1 to NP)
        :type  p:       int

        :returns:       Number of vertices in a polygon
        :rtype:         int

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The value returned is the "NV" used in function descriptions
        below.
        """
        ret_val = self._num_vertices(p)
        return ret_val




    def load(self, file):
        """
        Loads a Datamine polygon file.
        
        :param file:    Name of the file to load
        :type  file:    str

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._load(file.encode())
        




    def move_vertex(self, p, v, x, y, z):
        """
        Moves a vertex and any associated lines.
        
        :param p:       Polygon number (1 to NP)
        :param v:       Vertex number (1 to NV)
        :param x:       New location X
        :param y:       New location Y
        :param z:       New location Z
        :type  p:       int
        :type  v:       int
        :type  x:       float
        :type  y:       float
        :type  z:       float

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._move_vertex(p, v, x, y, z)
        




    def project_poly(self, p, xp, yp, zp, az, swing, vv_x, vv_y, vv_z):
        """
        Project a polygon onto a vertical plane.
        
        :param p:       Polygon number (1 to NP)
        :param xp:      X location of plane origin in 3D
        :param yp:      Y location of plane origin in 3D
        :param zp:      Z location of plane origin in 3D
        :param az:      Azimuth of the plane in degrees
        :param swing:   Swing of the plane in degrees
        :param vv_x:    X (horizontal along-section locations on vertical plane  (o)
        :param vv_y:    Y (vertical locations on vertical plane  (o)
        :param vv_z:    Z (horizontal distances perpendicular to the plane  (o)
        :type  p:       int
        :type  xp:      float
        :type  yp:      float
        :type  zp:      float
        :type  az:      float
        :type  swing:   float
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_z:    GXVV

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Gives the location in plane coordinates of a selected polygon,
        after it has been projected perpendicularly onto the plane.

        Plane coodinates: X - horizontal in plane
                          Y - "vertical" in plane (can be a swing)
                          Z - horizontal, "perpendicular" to plane (RH)
        """
        self._project_poly(p, xp, yp, zp, az, swing, vv_x, vv_y, vv_z)
        




    def re_project_poly(self, p, xp, yp, zp, az, vv_x, vv_y, vv_x3, vv_y3, vv_z3):
        """
        Recover polygon locations from 2D locations on vertical plane.
        
        :param p:       Polygon number (1 to lNP) (i)
        :param xp:      X location of plane origin in 3D (i)
        :param yp:      Y location of plane origin in 3D (i)
        :param zp:      Z location of plane origin in 3D (i)
        :param az:      Azimuth of the plane in degrees (i)
        :param vv_x:    X locations on vertical plane  (i)
        :param vv_y:    Y (actually Z) locations on vertical plane  (i)
        :param vv_x3:   X Locations of polygon (o)
        :param vv_y3:   Y Locations of polygon (o)
        :param vv_z3:   Z Locations of polygon (o)
        :type  p:       int
        :type  xp:      float
        :type  yp:      float
        :type  zp:      float
        :type  az:      float
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_x3:   GXVV
        :type  vv_y3:   GXVV
        :type  vv_z3:   GXVV

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This is the inverse operation of `project_poly <geosoft.gxapi.GXDMPPLY.project_poly>`.

        Input the 2D locations on the projected vertical plane. These locations
        are projected back onto the original polygon plane.
        """
        self._re_project_poly(p, xp, yp, zp, az, vv_x, vv_y, vv_x3, vv_y3, vv_z3)
        




    def save(self, file):
        """
        Save to a Datamine polygon file
        
        :param file:    Name of the file to save to
        :type  file:    str

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._save(file.encode())
        




    def set_poly(self, p, vv_x, vv_y, vv_z):
        """
        Set a specific polygon into a `GXDMPPLY <geosoft.gxapi.GXDMPPLY>` object.
        
        :param p:       Polygon number (1 to NP) (i)
        :param vv_x:    X Locations (i)
        :param vv_y:    Y Locations (i)
        :param vv_z:    Z Locations (i)
        :type  p:       int
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_z:    GXVV

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Get the number of points from the `GXVV <geosoft.gxapi.GXVV>` length.
        """
        self._set_poly(p, vv_x, vv_y, vv_z)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer