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
class GXPJ(gxapi_cy.WrapPJ):
    """
    GXPJ class.

    The `GXPJ <geosoft.gxapi.GXPJ>` object is created from two `GXIPJ <geosoft.gxapi.GXIPJ>` objects,
    and is used for converting data in an OASIS database
    or map object from one map coordinate (projection)
    system to another.
    """

    def __init__(self, handle=0):
        super(GXPJ, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPJ <geosoft.gxapi.GXPJ>`
        
        :returns: A null `GXPJ <geosoft.gxapi.GXPJ>`
        :rtype:   GXPJ
        """
        return GXPJ()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def clip_ply(self, min_x, min_y, max_x, max_y, max_dev, pply):
        """
        Create a clip polygon from a projected area.
        
        :param min_x:    Min X (or Longitude...)
        :param min_y:    Min Y (or Latitude...)
        :param max_x:    Max X
        :param max_y:    Max Y
        :param max_dev:  Max deviation in degrees
        :param pply:     `GXPLY <geosoft.gxapi.GXPLY>` to be filled
        :type  min_x:    float
        :type  min_y:    float
        :type  max_x:    float
        :type  max_y:    float
        :type  max_dev:  float
        :type  pply:     GXPLY

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A rectangular area from (MinX, MinY) to (MaxX, MaxY)
        is projected throught the `GXPJ <geosoft.gxapi.GXPJ>`. The resulting (non-rectangular)
        area is then digitized along its edges, then thinned to
        remove near-collinear points. The thinning is done to any
        point whose neighbors subtend an angle greater than
        (180 degrees - maximum deviation).  (i.e. if max. dev = 0,
        only co-linear points would be removed).
        """
        self._clip_ply(min_x, min_y, max_x, max_y, max_dev, pply)
        




    def convert_vv(self, vv_x, vv_y):
        """
        Convert VVx/VVy from input projection to output projection.
        
        :param vv_x:  VVx
        :param vv_y:  VVy
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function is equivalent to `GXVV.project <geosoft.gxapi.GXVV.project>`.
        """
        self._convert_vv(vv_x, vv_y)
        




    def convert_vv3(self, vv_x, vv_y, vv_z):
        """
        Convert VVx/VVy/VVz projections
        
        :param vv_x:  VVx
        :param vv_y:  VVy
        :param vv_z:  VVz
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function is equivalent to `GXVV.project_3d <geosoft.gxapi.GXVV.project_3d>`.
        """
        self._convert_vv3(vv_x, vv_y, vv_z)
        




    def convert_xy(self, x, y):
        """
        Convert X, Y from input projection to output projection.
        
        :param x:   X  (or Longitude)
        :param y:   Y  (or Latitude)
        :type  x:   float_ref
        :type  y:   float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        x.value, y.value = self._convert_xy(x.value, y.value)
        




    def convert_xy_from_xyz(self, x, y, z):
        """
        Convert X, Y from input projection to output projection, taking Z into account
        
        :param x:   X  (or Longitude)
        :param y:   Y  (or Latitude)
        :param z:   Z  (or Depth - unchanged)
        :type  x:   float_ref
        :type  y:   float_ref
        :type  z:   float

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function is used (for instance) when projecting voxel model locations
        where the user expects that the vertical position will not change. The
        regular `convert_xyz <geosoft.gxapi.GXPJ.convert_xyz>` may result in shifts of hundreds, even a thousand
        meters in case where you are going from the geoid to an ellipsoid.
        The value of Z can have an important effect on the accuracy of the results, as
        the normal `convert_xy <geosoft.gxapi.GXPJ.convert_xy>` assumes a value of Z=0 internally and calls
        `convert_xyz <geosoft.gxapi.GXPJ.convert_xyz>`.
        """
        x.value, y.value = self._convert_xy_from_xyz(x.value, y.value, z)
        




    def convert_xyz(self, x, y, z):
        """
        Convert X,Y,Z from input projection to output projection.
        
        :param x:   X  (or Longitude)
        :param y:   Y  (or Latitude)
        :param z:   Z  (or Depth)
        :type  x:   float_ref
        :type  y:   float_ref
        :type  z:   float_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        x.value, y.value, z.value = self._convert_xyz(x.value, y.value, z.value)
        



    @classmethod
    def create(cls, input, output):
        """
        This method creates a projection object.
        
        :param input:   Input PRJ file name, "" for geodetic
        :param output:  Ouput PRJ file name, "" for geodetic
        :type  input:   str
        :type  output:  str

        :returns:       `GXPJ <geosoft.gxapi.GXPJ>` Object
        :rtype:         GXPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapPJ._create(GXContext._get_tls_geo(), input.encode(), output.encode())
        return GXPJ(ret_val)



    @classmethod
    def create_ipj(cls, ip_jin, ip_jout):
        """
        This method creates a projection object from IPJs.
        
        :param ip_jin:   Input Projection, (`GXIPJ <geosoft.gxapi.GXIPJ>`)0 for long/lat
        :param ip_jout:  Output Projection, (`GXIPJ <geosoft.gxapi.GXIPJ>`)0 for long/lat
        :type  ip_jin:   GXIPJ
        :type  ip_jout:  GXIPJ

        :returns:        `GXPJ <geosoft.gxapi.GXPJ>` Object
        :rtype:          GXPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If converting to/from long/lat in the natural coordinate
        system of the source/target, only the long/lat system
        can be passed as (`GXIPJ <geosoft.gxapi.GXIPJ>`)0.
        """
        ret_val = gxapi_cy.WrapPJ._create_ipj(GXContext._get_tls_geo(), ip_jin, ip_jout)
        return GXPJ(ret_val)



    @classmethod
    def create_rectified(cls, lon, lat, x, y, rot, scl, dir):
        """
        Create a rectified `GXPJ <geosoft.gxapi.GXPJ>` from lon,lat,rotation
        
        :param lon:  Longitude  at (X,Y) origin
        :param lat:  Latitude   at (X,Y) origin
        :param x:    (X,Y) origin
        :param rot:  Coordinate Y relative to geographic N (deg azm)
        :param scl:  Scale to convert X,Y to m.
        :param dir:  :ref:`PJ_RECT`
        :type  lon:  float
        :type  lat:  float
        :type  x:    float
        :type  y:    float
        :type  rot:  float
        :type  scl:  float
        :type  dir:  int

        :returns:    `GXPJ <geosoft.gxapi.GXPJ>` Object
        :rtype:      GXPJ

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Given an X,Y coordinate system, the lat/lon origin and
        angle of the coordinate system, this will create a `GXPJ <geosoft.gxapi.GXPJ>`
        to convert between X,Y coordinates and Lon,Lat.
        The Lon/Lat is determined using a Transverse Mercator
        projection with central meridian through the center
        of the coordinates on a WGS 84 datum.
        """
        ret_val = gxapi_cy.WrapPJ._create_rectified(GXContext._get_tls_geo(), lon, lat, x, y, rot, scl, dir)
        return GXPJ(ret_val)






    def elevation(self):
        """
        Get elevation correction method
        

        :returns:    :ref:`PJ_ELEVATION`
        :rtype:      int

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To determine the model in use, refer to the datum_trf column in the
        user\\csv\\datumtrf.csv file.  The datum and geoid model are named in
        the sqare brackets following the transform name as follows:

        name [datum_model:geoid]

        The datum_model is the name of the datum transformation model which will
        be in a file with extension .ll2 in the \\etc directory.  The geoid is the
        name of the geoid model which will be in a grid file with extension .grd
        in the \\etc directory.  If the geoid model is missing, this method will
        return `PJ_ELEVATION_NONE <geosoft.gxapi.PJ_ELEVATION_NONE>` and elevation coordinates will not be changed.
        """
        ret_val = self._elevation()
        return ret_val




    def is_input_ll(self):
        """
        Is the input projection a lat/long.
        

        :returns:    1 - Yes
                    0 - No
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_input_ll()
        return ret_val




    def is_output_ll(self):
        """
        Is the output projection a lat/long.
        

        :returns:    1 - Yes
                    0 - No
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_output_ll()
        return ret_val




    def project_bounding_rectangle(self, min_x, min_y, max_x, max_y):
        """
        Project a bounding rectangle.
        
        :param min_x:  Bounding Region Min X
        :param min_y:  Bounding Region Min Y
        :param max_x:  Bounding Region Max X
        :param max_y:  Bounding Region Max Y
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref

        .. versionadded:: 5.1.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A rectangular area from (dMinX, dMinY) to (dMaxX, dMaxY)
        is projected throught the `GXPJ <geosoft.gxapi.GXPJ>`. The resulting region area is
        then digitized along its edges and a new bounding rectangle
        is computed.  If there is a lot of curve through the
        projection the resulting bounding region may be slightly
        smaller than the true region.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._project_bounding_rectangle(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def project_bounding_rectangle2(self, min_x, min_y, max_x, max_y, err):
        """
        Project a bounding rectangle with error tolerance.
        
        :param min_x:  Bounding Region Min X
        :param min_y:  Bounding Region Min Y
        :param max_x:  Bounding Region Max X
        :param max_y:  Bounding Region Max Y
        :param err:    Maximum allowable projection error if <= 0.0, will use 0.005% of smallest dimension
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref
        :type  err:    float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is the same as `project_bounding_rectangle <geosoft.gxapi.GXPJ.project_bounding_rectangle>` except that the bounding
        rectangle will be limited to an area within which the projection can be
        performed to an accuracy better than the specified error tolerance.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._project_bounding_rectangle2(min_x.value, min_y.value, max_x.value, max_y.value, err)
        




    def project_bounding_rectangle_res(self, min_x, min_y, max_x, max_y, res):
        """
        Project a bounding rectangle with resolution.
        
        :param min_x:  Bounding Region Min X
        :param min_y:  Bounding Region Min Y
        :param max_x:  Bounding Region Max X
        :param max_y:  Bounding Region Max Y
        :param res:    Resolution
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref
        :type  res:    float_ref

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function behaves just like ProjBoundingRectangle_PJ
        except that it also computes an approximate resolution
        at the reprojected coordinate system from a given original
        resolution.
        """
        min_x.value, min_y.value, max_x.value, max_y.value, res.value = self._project_bounding_rectangle_res(min_x.value, min_y.value, max_x.value, max_y.value, res.value)
        




    def project_bounding_rectangle_res2(self, min_x, min_y, max_x, max_y, res, err):
        """
        Project a bounding rectangle with resolution and error tolerance.
        
        :param min_x:  Bounding Region Min X
        :param min_y:  Bounding Region Min Y
        :param max_x:  Bounding Region Max X
        :param max_y:  Bounding Region Max Y
        :param res:    Resolution
        :param err:    Maximum allowable projection error if <= 0.0, will use 0.005% of smallest dimension
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref
        :type  res:    float_ref
        :type  err:    float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is the same as `project_bounding_rectangle_res <geosoft.gxapi.GXPJ.project_bounding_rectangle_res>` except that the bounding
        rectangle will be limited to an area within which the projection can be
        performed to an accuracy better than the specified error tolerance.
        """
        min_x.value, min_y.value, max_x.value, max_y.value, res.value = self._project_bounding_rectangle_res2(min_x.value, min_y.value, max_x.value, max_y.value, res.value, err)
        




    def project_limited_bounding_rectangle(self, min_xl, min_yl, max_xl, max_yl, min_x, min_y, max_x, max_y):
        """
        Project a bounding rectangle with limits.
        
        :param min_xl:  Output limited bounding region Min X
        :param min_yl:  Min Y
        :param max_xl:  Max X
        :param max_yl:  Max Y
        :param min_x:   Bounding Region Min X
        :param min_y:   Min Y
        :param max_x:   Max X
        :param max_y:   Max Y
        :type  min_xl:  float
        :type  min_yl:  float
        :type  max_xl:  float
        :type  max_yl:  float
        :type  min_x:   float_ref
        :type  min_y:   float_ref
        :type  max_x:   float_ref
        :type  max_y:   float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The bounding rectangle will be limited to no larger
        than the area specified in the output projection.  This
        is useful when projecting from limits that are unreasonable
        in the target projection.

        .. seealso::

            `project_bounding_rectangle <geosoft.gxapi.GXPJ.project_bounding_rectangle>`.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._project_limited_bounding_rectangle(min_xl, min_yl, max_xl, max_yl, min_x.value, min_y.value, max_x.value, max_y.value)
        




    def setup_ldt(self):
        """
        Setup the `GXPJ <geosoft.gxapi.GXPJ>` with LDT check.
        

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** By default, a `GXPJ <geosoft.gxapi.GXPJ>` on the same datum will not apply a LDT,
        is intended for transformations between datums.  However,
        in some instances you might want to convert between LDTs on
        the same datum, such as when you have two sets of coordinates
        that you KNOW came from WGS84 and were placed on this datum
        using differnt LDT's.  If you want to combine such coordinate
        systems, one or the other should be converted to the other's
        LDT.  Note that a more logical way to do this would be to
        convert both sets back to their original WGS84 coordinates
        and combine in WGS84.
        """
        self._setup_ldt()
        




    def project_bounding_volume(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Project a bounding volume.
        
        :param min_x:  Min X
        :param min_y:  Min Y
        :param min_z:  Min Z
        :param max_x:  Max X
        :param max_y:  Max Y
        :param max_z:  Max Z
        :type  min_x:  float_ref
        :type  min_y:  float_ref
        :type  min_z:  float_ref
        :type  max_x:  float_ref
        :type  max_y:  float_ref
        :type  max_z:  float_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._project_bounding_volume(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer