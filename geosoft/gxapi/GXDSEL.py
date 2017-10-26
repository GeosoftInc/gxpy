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
class GXDSEL:
    """
    GXDSEL class.

    The `GXDSEL` object is used to select subsets of data from the DATA object
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
        """
        ret_val = gxapi_cy.WrapDSEL.create(GXContext._get_tls_geo())
        return GXDSEL(ret_val)




    def data_significant_figures(self, sf):
        """
        Specify the data significant figures required

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
        """
        self._wrapper.meta_query(query.encode())
        




    def picture_quality(self, quality):
        """
        Specify the quality of pictures being returned.

        **Note:**

        Affected Data Types: PICTURE
        """
        self._wrapper.picture_quality(quality)
        




    def request_all_info(self, request):
        """
        Request that all meta-data info be sent
        """
        self._wrapper.request_all_info(request)
        




    def select_area(self, pply):
        """
        Select a complex clipping area

        **Note:**

        The DAP server may not handle clipping and may return
        more data than requested.
        """
        self._wrapper.select_area(pply._wrapper)
        




    def select_rect(self, min_x, min_y, max_x, max_y):
        """
        Select a rectangular area.
        """
        self._wrapper.select_rect(min_x, min_y, max_x, max_y)
        




    def select_resolution(self, res, force):
        """
        Specify the resolution desired

        **Note:**

        Resolution must be specified in the units of the selection `GXIPJ`.
        
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
        """
        self._wrapper.select_size(width, height)
        




    def set_extract_as_document(self, value):
        """
        Specify that we want to extract this file as a document
        """
        self._wrapper.set_extract_as_document(value)
        




    def set_ipj(self, ipj, force):
        """
        Set the desired projection

        **Note:**

        If the server supports reprojection, the data will be
        reprojected at the server.
        
        If reprojection is not forced, the data may come in any projection.
        
        The spatial resolution and accuracy are accumed to be in the
        coordinate system defined by this `GXIPJ`.
        """
        self._wrapper.set_ipj(ipj._wrapper, force)
        




    def spatial_accuracy(self, acc):
        """
        Specify the spatial accuracy required.

        **Note:**

        Must be specified in the units of the selection `GXIPJ`.
        
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