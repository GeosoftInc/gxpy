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
class GXPLY(gxapi_cy.WrapPLY):
    """
    GXPLY class.

    The `GXPLY <geosoft.gxapi.GXPLY>` object contains the definitions for one or more
    polygons, and does import and export of polygon files.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPLY <geosoft.gxapi.GXPLY>`
        
        :returns: A null `GXPLY <geosoft.gxapi.GXPLY>`
        :rtype:   GXPLY
        """
        return GXPLY()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def add_polygon(self, vv_x, vv_y):
        """
        Add a polygon to the polygon file.
        
        :param vv_x:  X `GXVV <geosoft.gxapi.GXVV>`.
        :param vv_y:  Y `GXVV <geosoft.gxapi.GXVV>`.
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._add_polygon(vv_x, vv_y)
        




    def add_polygon_ex(self, vv_x, vv_y, exclude):
        """
        Add a polygon to the polygon file.
        
        :param vv_x:     X `GXVV <geosoft.gxapi.GXVV>`.
        :param vv_y:     Y `GXVV <geosoft.gxapi.GXVV>`.
        :param exclude:  bExclude
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  exclude:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._add_polygon_ex(vv_x, vv_y, exclude)
        




    def change_ipj(self, ipj):
        """
        Set the projection.
        
        :param ipj:   `GXIPJ <geosoft.gxapi.GXIPJ>` to place in the `GXPLY <geosoft.gxapi.GXPLY>`
        :type  ipj:   GXIPJ

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXPLY <geosoft.gxapi.GXPLY>` is re-projected to the new projection.
        """
        self._change_ipj(ipj)
        




    def clear(self):
        """
        Clear/remove all polygons from the `GXPLY <geosoft.gxapi.GXPLY>`.
        

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._clear()
        




    def copy(self, srce):
        """
        Copies one `GXPLY <geosoft.gxapi.GXPLY>` Object to another
        
        :param srce:  Source
        :type  srce:  GXPLY

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(srce)
        




    def is_valid(self):
        """
        Ensure a polygon is valid
        
        :rtype:       int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_valid()
        return ret_val




    def combine(self, srce, exclude):
        """
        Combines two `GXPLY <geosoft.gxapi.GXPLY>` Object with another
        
        :param srce:     Source
        :param exclude:  Make all the polygons copied excluded? - if not they will be copied as they are.
        :type  srce:     GXPLY
        :type  exclude:  int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._combine(srce, exclude)
        



    @classmethod
    def create(cls):
        """
        Creates a Polygon Object.
        

        :returns:    `GXPLY <geosoft.gxapi.GXPLY>` Handle
        :rtype:      GXPLY

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapPLY._create(GXContext._get_tls_geo())
        return GXPLY(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create an `GXPLY <geosoft.gxapi.GXPLY>` Object from a `GXBF <geosoft.gxapi.GXBF>`
        
        :param bf:  `GXBF <geosoft.gxapi.GXBF>` to serialize from
        :type  bf:  GXBF

        :returns:    `GXPLY <geosoft.gxapi.GXPLY>` Handle
        :rtype:      GXPLY

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapPLY._create_s(GXContext._get_tls_geo(), bf)
        return GXPLY(ret_val)






    def extent(self, min_x, min_y, max_x, max_y):
        """
        Get the extent of the current polygon.
        
        :param min_x:  Min X
        :param min_y:  Min Y
        :param max_x:  Max X
        :param max_y:  Max Y
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If there are no polygons in the `GXPLY <geosoft.gxapi.GXPLY>` object, returns dummies.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._extent(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def get_ipj(self, ipj):
        """
        Get the projection.
        
        :param ipj:   `GXIPJ <geosoft.gxapi.GXIPJ>` in which to place the `GXPLY <geosoft.gxapi.GXPLY>` projection
        :type  ipj:   GXIPJ

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_ipj(ipj)
        




    def get_polygon(self, vv_x, vv_y, poly):
        """
        Get a polygon from the `GXPLY <geosoft.gxapi.GXPLY>`
        
        :param vv_x:  X `GXVV <geosoft.gxapi.GXVV>`.
        :param vv_y:  Y `GXVV <geosoft.gxapi.GXVV>`.
        :param poly:  Polygon number
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  poly:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_polygon(vv_x, vv_y, poly)
        




    def get_polygon_ex(self, vv_x, vv_y, poly, exclude):
        """
        Get a polygon from the `GXPLY <geosoft.gxapi.GXPLY>`
        
        :param vv_x:     X `GXVV <geosoft.gxapi.GXVV>`.
        :param vv_y:     Y `GXVV <geosoft.gxapi.GXVV>`.
        :param poly:     Polygon number
        :param exclude:  TRUE if exclusion polygon
        :type  vv_x:     GXVV
        :type  vv_y:     GXVV
        :type  poly:     int
        :type  exclude:  int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        exclude.value = self._get_polygon_ex(vv_x, vv_y, poly, exclude.value)
        




    def clip_area(self, min_x, min_y, max_x, max_y):
        """
        Clip a polygon to an area
        
        :param min_x:  Min X
        :param min_y:  Min Y
        :param max_x:  Max X
        :param max_y:  Max y
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float

        :returns:      :ref:`PLY_CLIP`
        :rtype:        int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._clip_area(min_x, min_y, max_x, max_y)
        return ret_val




    def clip_line_int(self, min_x, min_y, max_x, max_y, vv, inc, first):
        """
        Clips a line in or out of the polygons for intersections (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`).
        Intersections are returned as fiducials down the line stored in `GXVV <geosoft.gxapi.GXVV>`
        starting at the first point of the line.
        Examples:
        No intersection: `PLY_LINE_CLIP_OUTSIDE <geosoft.gxapi.PLY_LINE_CLIP_OUTSIDE>`, 0 intersections
        Starts outside, ends inside: `PLY_LINE_CLIP_OUTSIDE <geosoft.gxapi.PLY_LINE_CLIP_OUTSIDE>`, 1 intersection
        Starts outside, intersects then ends inside or outside: `PLY_LINE_CLIP_OUTSIDE <geosoft.gxapi.PLY_LINE_CLIP_OUTSIDE>`, 2 intersections
        Starts inside, ends inside : `PLY_LINE_CLIP_INSIDE <geosoft.gxapi.PLY_LINE_CLIP_INSIDE>`, 1 intersection (gives end-of-line)
        Starts inside, ends outside : `PLY_LINE_CLIP_INSIDE <geosoft.gxapi.PLY_LINE_CLIP_INSIDE>`, 1 intersection
        
        :param min_x:  Min X of line to clip
        :param min_y:  Min Y of line to clip
        :param max_x:  Max X of line to clip
        :param max_y:  Max y of line to clip
        :param vv:     DOUBLE `GXVV <geosoft.gxapi.GXVV>` holding intersection fids
        :param inc:    Data element increment (precision)
        :param first:  First point value (:ref:`PLY_LINE_CLIP` value)
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float
        :type  vv:     GXVV
        :type  inc:    float
        :type  first:  int_ref

        :returns:      0, Terminates on error (you can ignore this value)
        :rtype:        int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, first.value = self._clip_line_int(min_x, min_y, max_x, max_y, vv, inc, first.value)
        return ret_val




    def clip_ply(self, pply_b, pply_c):
        """
        Clip one polygon against another
        
        :param pply_b:  Polygon B
        :param pply_c:  Resulting clipped region
        :type  pply_b:  GXPLY
        :type  pply_c:  GXPLY

        :returns:       :ref:`PLY_CLIP`
        :rtype:         int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Resulting clipped polygon only has inclusive
        regions of the clipped area.  Exclusion polygons
        are treated as included areas.
        """
        ret_val = self._clip_ply(pply_b, pply_c)
        return ret_val




    def clip_point(self, x, y):
        """
        Clips a point in or out of the polygon.
        Point is inside: `PLY_POINT_CLIP_INSIDE <geosoft.gxapi.PLY_POINT_CLIP_INSIDE>`
        Point is outside: `PLY_POINT_CLIP_OUTSIDE <geosoft.gxapi.PLY_POINT_CLIP_OUTSIDE>`
        An error occurred: `PLY_POINT_CLIP_ERROR <geosoft.gxapi.PLY_POINT_CLIP_ERROR>`
        
        :param x:     Point X
        :param y:     Point Y
        :type  x:     float
        :type  y:     float

        :returns:     :ref:`PLY_POINT_CLIP`
        :rtype:       int

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._clip_point(x, y)
        return ret_val




    def get_description(self, desc):
        """
        Get the `GXPLY <geosoft.gxapi.GXPLY>` description string
        
        :param desc:  Polygon description
        :type  desc:  str_ref

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        desc.value = self._get_description(desc.value.encode())
        




    def num_poly(self):
        """
        Get the number of polygons.
        

        :returns:     Number of polygons in the `GXPLY <geosoft.gxapi.GXPLY>`.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_poly()
        return ret_val




    def load_table(self, table):
        """
        Loads Polygons from a Polygon file.
        
        :param table:  Name of the polygon file File contains coordinates of one or more polygons
        :type  table:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._load_table(table.encode())
        




    def area(self):
        """
        Compute the Area of a polygon
        

        :returns:     Area of a polygon
        :rtype:       float

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Excluded polygons have negative area.
        """
        ret_val = self._area()
        return ret_val




    def rectangle(self, min_x, min_y, max_x, max_y):
        """
        Creates a polygon from a rectangular area.
        
        :param min_x:  Min X
        :param min_y:  Min Y
        :param max_x:  Max X
        :param max_y:  Max Y
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._rectangle(min_x, min_y, max_x, max_y)
        




    def rotate(self, x, y, rot):
        """
        Rotate a polygon about a point.
        
        :param x:     Rotation point, X
        :param y:     Rotation point, Y
        :param rot:   Rotation angle, CCW in degrees
        :type  x:     float
        :type  y:     float
        :type  rot:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._rotate(x, y, rot)
        




    def save_table(self, table):
        """
        Save Polygons to a Polygon file.
        
        :param table:  Name of the polygon file
        :type  table:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._save_table(table.encode())
        




    def serial(self, bf):
        """
        Serialize an `GXPLY <geosoft.gxapi.GXPLY>` to a `GXBF <geosoft.gxapi.GXBF>`
        
        :param bf:   `GXBF <geosoft.gxapi.GXBF>` to serialize to
        :type  bf:   GXBF

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial(bf)
        




    def set_description(self, desc):
        """
        Set the `GXPLY <geosoft.gxapi.GXPLY>` description string
        
        :param desc:  Polygon description
        :type  desc:  str

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_description(desc.encode())
        




    def set_ipj(self, ipj):
        """
        Set the projection.
        
        :param ipj:   `GXIPJ <geosoft.gxapi.GXIPJ>` to place in the `GXPLY <geosoft.gxapi.GXPLY>`
        :type  ipj:   GXIPJ

        .. versionadded:: 5.0.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This changes the projection information only.
        """
        self._set_ipj(ipj)
        




    def thin(self, thin):
        """
        Thin polygons to a desired resolution
        
        :param thin:  Thining resolution
        :type  thin:  float

        .. versionadded:: 5.1.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Points on the polygon that deviate from a line drawn between
        neighboring points by more than the thining resolution will
        be removed.
        """
        self._thin(thin)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer