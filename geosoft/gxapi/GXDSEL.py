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
class GXDSEL:
    """
    GXDSEL class.

    The `GXDSEL <geosoft.gxapi.GXDSEL>` object is used to select subsets of data from the DATA object
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDSEL(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDSEL`
        
        :returns: A null `GXDSEL`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDSEL` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDSEL`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls):
        """
        Create a Selection object
        

        :returns:    `GXDSEL <geosoft.gxapi.GXDSEL>` handle, terminates if creation fails
        :rtype:      GXDSEL

        .. versionadded:: 5.0.3
        """
        ret_val = gxapi_cy.WrapDSEL.create(GXContext._get_tls_geo())
        return GXDSEL(ret_val)




    def data_significant_figures(self, sf):
        """
        Specify the data significant figures required
        
        :param sf:    Significant figures (positive, can be fractional)
        :type  sf:    float

        .. versionadded:: 5.0.8

        **Note:**

        This is the number of significant figures that you require for the data.
        You can reduce this number to achieve better compression ratios.
        This should only be used when there is one data type in the data.
        
        See sSpatialResolution_DSEL to set the desired spatial resolution.
        """
        self._wrapper.data_significant_figures(sf)
        






    def meta_query(self, query):
        """
        Specify a metadata query string.
        
        :param query:  Meta query string
        :type  query:  str

        .. versionadded:: 5.1.3
        """
        self._wrapper.meta_query(query.encode())
        




    def picture_quality(self, quality):
        """
        Specify the quality of pictures being returned.
        
        :param quality:  Quality
        :type  quality:  int

        .. versionadded:: 5.1.4

        **Note:**

        Affected Data Types: PICTURE
        """
        self._wrapper.picture_quality(quality)
        




    def request_all_info(self, request):
        """
        Request that all meta-data info be sent
        
        :param request:  TRUE to for all data, FALSE - for normal data
        :type  request:  int

        .. versionadded:: 5.1.3
        """
        self._wrapper.request_all_info(request)
        




    def select_area(self, pply):
        """
        Select a complex clipping area
        
        :param pply:  `GXPLY <geosoft.gxapi.GXPLY>` containing complex area (must contain a projection)
        :type  pply:  GXPLY

        .. versionadded:: 5.1.3

        **Note:**

        The DAP server may not handle clipping and may return
        more data than requested.
        """
        self._wrapper.select_area(pply._wrapper)
        




    def select_rect(self, min_x, min_y, max_x, max_y):
        """
        Select a rectangular area.
        
        :param min_x:  Min X
        :param min_y:  Min Y
        :param max_x:  Max X
        :param max_y:  Max Y
        :type  min_x:  float
        :type  min_y:  float
        :type  max_x:  float
        :type  max_y:  float

        .. versionadded:: 5.0.3
        """
        self._wrapper.select_rect(min_x, min_y, max_x, max_y)
        




    def select_resolution(self, res, force):
        """
        Specify the resolution desired
        
        :param res:    Minimum Resolution
        :param force:  TRUE to force this resolution, if possible
        :type  res:    float
        :type  force:  int

        .. versionadded:: 5.0.3

        **Note:**

        Resolution must be specified in the units of the selection `GXIPJ <geosoft.gxapi.GXIPJ>`.
        
        This will be the optimum data resoulution.  (grid cell for grids, data
        separation for other data types).
        You will normally get a reasonable resolution as near to or smaller than
        this unless sRequireResolution_DSEL has been set.
        
        Call sRequireResolution_DSEL with TRUE to force the client to re-sample
        the data to the resolution requested.
        """
        self._wrapper.select_resolution(res, force)
        




    def select_size(self, width, height):
        """
        Specify the image size desired
        
        :param width:   Image width in pixels
        :param height:  Image height in pixels
        :type  width:   int
        :type  height:  int

        .. versionadded:: 7.0
        """
        self._wrapper.select_size(width, height)
        




    def set_extract_as_document(self, value):
        """
        Specify that we want to extract this file as a document
        
        :param value:  TRUE (1) if we want as a document
        :type  value:  int

        .. versionadded:: 8.0
        """
        self._wrapper.set_extract_as_document(value)
        




    def set_ipj(self, ipj, force):
        """
        Set the desired projection
        
        :param ipj:    `GXIPJ <geosoft.gxapi.GXIPJ>` to set
        :param force:  TRUE to force reprojection, if possible
        :type  ipj:    GXIPJ
        :type  force:  int

        .. versionadded:: 5.0.8

        **Note:**

        If the server supports reprojection, the data will be
        reprojected at the server.
        
        If reprojection is not forced, the data may come in any projection.
        
        The spatial resolution and accuracy are accumed to be in the
        coordinate system defined by this `GXIPJ <geosoft.gxapi.GXIPJ>`.
        """
        self._wrapper.set_ipj(ipj._wrapper, force)
        




    def spatial_accuracy(self, acc):
        """
        Specify the spatial accuracy required.
        
        :param acc:   Spatial accuracy desired
        :type  acc:   float

        .. versionadded:: 5.0.8

        **Note:**

        Must be specified in the units of the selection `GXIPJ <geosoft.gxapi.GXIPJ>`.
        
        The spatial accuracy is used improve compression performance for
        the spatial component of the data returned.
        You can reduce this number to achieve better compression ratios.
        This should only be used when there is one data type in the data.
        """
        self._wrapper.spatial_accuracy(acc)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer