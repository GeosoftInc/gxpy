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



    def clip_ply(self, p2, p3, p4, p5, p6, p7):
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
        self._wrapper.clip_ply(p2, p3, p4, p5, p6, p7._wrapper)
        




    def convert_vv(self, p2, p3):
        """
        Convert VVx/VVy from input projection to output projection.

        **Note:**

        This function is equivalent to `GXVV.project`.
        """
        self._wrapper.convert_vv(p2._wrapper, p3._wrapper)
        




    def convert_vv3(self, p2, p3, p4):
        """
        Convert VVx/VVy/VVz projections

        **Note:**

        This function is equivalent to `GXVV.project_3d`.
        """
        self._wrapper.convert_vv3(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def convert_xy(self, p2, p3):
        """
        Convert X, Y from input projection to output projection.
        """
        p2.value, p3.value = self._wrapper.convert_xy(p2.value, p3.value)
        




    def convert_xy_from_xyz(self, p2, p3, p4):
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
        p2.value, p3.value = self._wrapper.convert_xy_from_xyz(p2.value, p3.value, p4)
        




    def convert_xyz(self, p2, p3, p4):
        """
        Convert X,Y,Z from input projection to output projection.
        """
        p2.value, p3.value, p4.value = self._wrapper.convert_xyz(p2.value, p3.value, p4.value)
        



    @classmethod
    def create(cls, p1, p2):
        """
        This method creates a projection object.
        """
        ret_val = gxapi_cy.WrapPJ.create(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return GXPJ(ret_val)



    @classmethod
    def create_ipj(cls, p1, p2):
        """
        This method creates a projection object from IPJs.

        **Note:**

        If converting to/from long/lat in the natural coordinate
        system of the source/target, only the long/lat system
        can be passed as (`GXIPJ`)0.
        """
        ret_val = gxapi_cy.WrapPJ.create_ipj(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        return GXPJ(ret_val)



    @classmethod
    def create_rectified(cls, p1, p2, p3, p4, p5, p6, p7):
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
        ret_val = gxapi_cy.WrapPJ.create_rectified(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7)
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




    def project_bounding_rectangle(self, p2, p3, p4, p5):
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
        p2.value, p3.value, p4.value, p5.value = self._wrapper.project_bounding_rectangle(p2.value, p3.value, p4.value, p5.value)
        




    def project_bounding_rectangle2(self, p2, p3, p4, p5, p6):
        """
        Project a bounding rectangle with error tolerance.

        **Note:**

        This is the same as `project_bounding_rectangle` except that the bounding
        rectangle will be limited to an area within which the projection can be
        performed to an accuracy better than the specified error tolerance.
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.project_bounding_rectangle2(p2.value, p3.value, p4.value, p5.value, p6)
        




    def project_bounding_rectangle_res(self, p2, p3, p4, p5, p6):
        """
        Project a bounding rectangle with resolution.

        **Note:**

        This function behaves just like ProjBoundingRectangle_PJ
        except that it also computes an approximate resolution
        at the reprojected coordinate system from a given original
        resolution.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.project_bounding_rectangle_res(p2.value, p3.value, p4.value, p5.value, p6.value)
        




    def project_bounding_rectangle_res2(self, p2, p3, p4, p5, p6, p7):
        """
        Project a bounding rectangle with resolution and error tolerance.

        **Note:**

        This is the same as `project_bounding_rectangle_res` except that the bounding
        rectangle will be limited to an area within which the projection can be
        performed to an accuracy better than the specified error tolerance.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.project_bounding_rectangle_res2(p2.value, p3.value, p4.value, p5.value, p6.value, p7)
        




    def project_limited_bounding_rectangle(self, p2, p3, p4, p5, p6, p7, p8, p9):
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
        p6.value, p7.value, p8.value, p9.value = self._wrapper.project_limited_bounding_rectangle(p2, p3, p4, p5, p6.value, p7.value, p8.value, p9.value)
        




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