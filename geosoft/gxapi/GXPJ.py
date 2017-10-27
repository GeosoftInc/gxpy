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
class GXPJ:
    """
    GXPJ class.

    The `GXPJ` object is created from two `GXIPJ` objects,
    and is used for converting data in an OASIS database
    or map object from one map coordinate (projection)
    system to another.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPJ(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPJ`
        
        :returns: A null `GXPJ`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXPJ` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXPJ`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clip_ply(self, min_x, min_y, max_x, max_y, max_dev, pply):
        """
        Create a clip polygon from a projected area.

        **Note:**

        A rectangular area from (MinX, MinY) to (MaxX, MaxY)
        is projected throught the `GXPJ`. The resulting (non-rectangular)
        area is then digitized along its edges, then thinned to
        remove near-collinear points. The thinning is done to any
        point whose neighbors subtend an angle greater than
        (180 degrees - maximum deviation).  (i.e. if max. dev = 0,
        only co-linear points would be removed).
        """
        self._wrapper.clip_ply(min_x, min_y, max_x, max_y, max_dev, pply._wrapper)
        




    def convert_vv(self, vv_x, vv_y):
        """
        Convert VVx/VVy from input projection to output projection.

        **Note:**

        This function is equivalent to `GXVV.project`.
        """
        self._wrapper.convert_vv(vv_x._wrapper, vv_y._wrapper)
        




    def convert_vv3(self, vv_x, vv_y, vv_z):
        """
        Convert VVx/VVy/VVz projections

        **Note:**

        This function is equivalent to `GXVV.project_3d`.
        """
        self._wrapper.convert_vv3(vv_x._wrapper, vv_y._wrapper, vv_z._wrapper)
        




    def convert_xy(self, x, y):
        """
        Convert X, Y from input projection to output projection.
        """
        x.value, y.value = self._wrapper.convert_xy(x.value, y.value)
        




    def convert_xy_from_xyz(self, x, y, z):
        """
        Convert X, Y from input projection to output projection, taking Z into account

        **Note:**

        This function is used (for instance) when projecting voxel model locations
        where the user expects that the vertical position will not change. The
        regular `convert_xyz` may result in shifts of hundreds, even a thousand
        meters in case where you are going from the geoid to an ellipsoid.
        The value of Z can have an important effect on the accuracy of the results, as
        the normal `convert_xy` assumes a value of Z=0 internally and calls
        `convert_xyz`.
        """
        x.value, y.value = self._wrapper.convert_xy_from_xyz(x.value, y.value, z)
        




    def convert_xyz(self, x, y, z):
        """
        Convert X,Y,Z from input projection to output projection.
        """
        x.value, y.value, z.value = self._wrapper.convert_xyz(x.value, y.value, z.value)
        



    @classmethod
    def create(cls, input, output):
        """
        This method creates a projection object.
        """
        ret_val = gxapi_cy.WrapPJ.create(GXContext._get_tls_geo(), input.encode(), output.encode())
        return GXPJ(ret_val)



    @classmethod
    def create_ipj(cls, ip_jin, ip_jout):
        """
        This method creates a projection object from IPJs.

        **Note:**

        If converting to/from long/lat in the natural coordinate
        system of the source/target, only the long/lat system
        can be passed as (`GXIPJ`)0.
        """
        ret_val = gxapi_cy.WrapPJ.create_ipj(GXContext._get_tls_geo(), ip_jin._wrapper, ip_jout._wrapper)
        return GXPJ(ret_val)



    @classmethod
    def create_rectified(cls, lon, lat, x, y, rot, scl, dir):
        """
        Create a rectified `GXPJ` from lon,lat,rotation

        **Note:**

        Given an X,Y coordinate system, the lat/lon origin and
        angle of the coordinate system, this will create a `GXPJ`
        to convert between X,Y coordinates and Lon,Lat.
        The Lon/Lat is determined using a Transverse Mercator
        projection with central meridian through the center
        of the coordinates on a WGS 84 datum.
        """
        ret_val = gxapi_cy.WrapPJ.create_rectified(GXContext._get_tls_geo(), lon, lat, x, y, rot, scl, dir)
        return GXPJ(ret_val)






    def elevation(self):
        """
        Get elevation correction method

        **Note:**

        To determine the model in use, refer to the datum_trf column in the
        user\\csv\\datumtrf.csv file.  The datum and geoid model are named in
        the sqare brackets following the transform name as follows:
        
        name [datum_model:geoid]
        
        The datum_model is the name of the datum transformation model which will
        be in a file with extension .ll2 in the \\etc directory.  The geoid is the
        name of the geoid model which will be in a grid file with extension .grd
        in the \\etc directory.  If the geoid model is missing, this method will
        return `PJ_ELEVATION_NONE` and elevation coordinates will not be changed.
        """
        ret_val = self._wrapper.elevation()
        return ret_val




    def is_input_ll(self):
        """
        Is the input projection a lat/long.
        """
        ret_val = self._wrapper.is_input_ll()
        return ret_val




    def is_output_ll(self):
        """
        Is the output projection a lat/long.
        """
        ret_val = self._wrapper.is_output_ll()
        return ret_val




    def project_bounding_rectangle(self, min_x, min_y, max_x, max_y):
        """
        Project a bounding rectangle.

        **Note:**

        A rectangular area from (dMinX, dMinY) to (dMaxX, dMaxY)
        is projected throught the `GXPJ`. The resulting region area is
        then digitized along its edges and a new bounding rectangle
        is computed.  If there is a lot of curve through the
        projection the resulting bounding region may be slightly
        smaller than the true region.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.project_bounding_rectangle(min_x.value, min_y.value, max_x.value, max_y.value)
        




    def project_bounding_rectangle2(self, min_x, min_y, max_x, max_y, err):
        """
        Project a bounding rectangle with error tolerance.

        **Note:**

        This is the same as `project_bounding_rectangle` except that the bounding
        rectangle will be limited to an area within which the projection can be
        performed to an accuracy better than the specified error tolerance.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.project_bounding_rectangle2(min_x.value, min_y.value, max_x.value, max_y.value, err)
        




    def project_bounding_rectangle_res(self, min_x, min_y, max_x, max_y, res):
        """
        Project a bounding rectangle with resolution.

        **Note:**

        This function behaves just like ProjBoundingRectangle_PJ
        except that it also computes an approximate resolution
        at the reprojected coordinate system from a given original
        resolution.
        """
        min_x.value, min_y.value, max_x.value, max_y.value, res.value = self._wrapper.project_bounding_rectangle_res(min_x.value, min_y.value, max_x.value, max_y.value, res.value)
        




    def project_bounding_rectangle_res2(self, min_x, min_y, max_x, max_y, res, err):
        """
        Project a bounding rectangle with resolution and error tolerance.

        **Note:**

        This is the same as `project_bounding_rectangle_res` except that the bounding
        rectangle will be limited to an area within which the projection can be
        performed to an accuracy better than the specified error tolerance.
        """
        min_x.value, min_y.value, max_x.value, max_y.value, res.value = self._wrapper.project_bounding_rectangle_res2(min_x.value, min_y.value, max_x.value, max_y.value, res.value, err)
        




    def project_limited_bounding_rectangle(self, min_xl, min_yl, max_xl, max_yl, min_x, min_y, max_x, max_y):
        """
        Project a bounding rectangle with limits.

        **Note:**

        The bounding rectangle will be limited to no larger
        than the area specified in the output projection.  This
        is useful when projecting from limits that are unreasonable
        in the target projection.

        .. seealso::

            `project_bounding_rectangle`.
        """
        min_x.value, min_y.value, max_x.value, max_y.value = self._wrapper.project_limited_bounding_rectangle(min_xl, min_yl, max_xl, max_yl, min_x.value, min_y.value, max_x.value, max_y.value)
        




    def setup_ldt(self):
        """
        Setup the `GXPJ` with LDT check.

        **Note:**

        By default, a `GXPJ` on the same datum will not apply a LDT,
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
        self._wrapper.setup_ldt()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer