### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXLPT import GXLPT
from .GXMETA import GXMETA
from .GXREG import GXREG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMAP(gxapi_cy.WrapMAP):
    """
    GXMAP class.

    MAPs are containers for `GXMVIEW <geosoft.gxapi.GXMVIEW>` objects. A view is a 3-D translation
    and a clip window on a map. Graphic entities can be drawn in an `GXMVIEW <geosoft.gxapi.GXMVIEW>`.
    It is recommended that the `GXMAP <geosoft.gxapi.GXMAP>` class be instantiated by first creating
    an `GXEMAP <geosoft.gxapi.GXEMAP>` object and calling the `GXEMAP.lock <geosoft.gxapi.GXEMAP.lock>` function.
    (See the explanation on the distinction between the `GXMAP <geosoft.gxapi.GXMAP>` and `GXEMAP <geosoft.gxapi.GXEMAP>` classes).
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMAP <geosoft.gxapi.GXMAP>`
        
        :returns: A null `GXMAP <geosoft.gxapi.GXMAP>`
        :rtype:   GXMAP
        """
        return GXMAP()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Export



    def export_all_in_view(self, name, view, pix_size, dpi, bits, dither, format, options):
        """
        Export the entire map in view units to an external format. View and Group names are removed and plane spatial coordinates will be in the units of the map.
        
        :param name:      File Name To Export
        :param view:      View to export coordinates in
        :param pix_size:  Resolution in view units of one pixel (or dummy, will be used if DPI is dummy)
        :param dpi:       Resolution in DPI (will override view resolution if not dummy, map page size will be used to determine pixel size of output)
        :param bits:      :ref:`MAP_EXPORT_BITS`
        :param dither:    :ref:`MAP_EXPORT_METHOD`
        :param format:    :ref:`MAP_EXPORT_FORMAT`
        :param options:   Extended Options String (format specific)
        :type  name:      str
        :type  view:      str
        :type  pix_size:  float
        :type  dpi:       float
        :type  bits:      int
        :type  dither:    int
        :type  format:    str
        :type  options:   str

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_all_in_view(name.encode(), view.encode(), pix_size, dpi, bits, dither, format.encode(), options.encode())
        




    def export_all_raster(self, name, view, size_x, size_y, dpi, bits, dither, format, options):
        """
        Export the entire map to map to a non-geo raster format.
        
        :param name:     File Name To Export
        :param view:     View to export coordinates in
        :param size_x:   Number of Pixels in X (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)
        :param size_y:   Number of Pixels in Y (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)
        :param dpi:      Resolution in DPI (will override X and Y if not dummy, map page size will be used to determine pixel size of output)
        :param bits:     :ref:`MAP_EXPORT_BITS`
        :param dither:   :ref:`MAP_EXPORT_METHOD`
        :param format:   :ref:`MAP_EXPORT_RASTER_FORMAT`
        :param options:  Extended Options String (format specific)
        :type  name:     str
        :type  view:     str
        :type  size_x:   int
        :type  size_y:   int
        :type  dpi:      float
        :type  bits:     int
        :type  dither:   int
        :type  format:   str
        :type  options:  str

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_all_raster(name.encode(), view.encode(), size_x, size_y, dpi, bits, dither, format.encode(), options.encode())
        




    def export_area_in_view(self, name, view, pix_size, dpi, bits, dither, min_x, min_y, max_x, max_y, format, options):
        """
        Export an area of a map in view units to an external format
        
        :param name:      File Name To Export
        :param view:      View to export coordinates in
        :param pix_size:  Resolution in view units of one pixel (or dummy, will be used if DPI is dummy)
        :param dpi:       Resolution in DPI (will override view resolution if not dummy, map page size will be used to determine pixel size of output)
        :param bits:      :ref:`MAP_EXPORT_BITS`
        :param dither:    :ref:`MAP_EXPORT_METHOD`
        :param min_x:     Area To Export Min X location in view units
        :param min_y:     Area To Export Min Y location in view units
        :param max_x:     Area To Export Max X location in view units
        :param max_y:     Area To Export Max Y location in view units
        :param format:    :ref:`MAP_EXPORT_FORMAT`
        :param options:   Extended Options String (format specific)
        :type  name:      str
        :type  view:      str
        :type  pix_size:  float
        :type  dpi:       float
        :type  bits:      int
        :type  dither:    int
        :type  min_x:     float
        :type  min_y:     float
        :type  max_x:     float
        :type  max_y:     float
        :type  format:    str
        :type  options:   str

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_area_in_view(name.encode(), view.encode(), pix_size, dpi, bits, dither, min_x, min_y, max_x, max_y, format.encode(), options.encode())
        




    def export_area_raster(self, name, view, min_x, min_y, max_x, max_y, size_x, size_y, dpi, bits, dither, format, options):
        """
        Export an area of a map to a non-geo raster format.
        
        :param name:     File Name To Export
        :param view:     View to export coordinates in
        :param min_x:    Area To Export Min X location in view units
        :param min_y:    Area To Export Min Y location in view units
        :param max_x:    Area To Export Max X location in view units
        :param max_y:    Area To Export Max Y location in view units
        :param size_x:   Number of Pixels in X (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)
        :param size_y:   Number of Pixels in Y (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)
        :param dpi:      Resolution in DPI (will override X and Y if not dummy, map page size will be used to determine pixel size of output)
        :param bits:     :ref:`MAP_EXPORT_BITS`
        :param dither:   :ref:`MAP_EXPORT_METHOD`
        :param format:   :ref:`MAP_EXPORT_RASTER_FORMAT`
        :param options:  Extended Options String (format specific)
        :type  name:     str
        :type  view:     str
        :type  min_x:    float
        :type  min_y:    float
        :type  max_x:    float
        :type  max_y:    float
        :type  size_x:   int
        :type  size_y:   int
        :type  dpi:      float
        :type  bits:     int
        :type  dither:   int
        :type  format:   str
        :type  options:  str

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_area_raster(name.encode(), view.encode(), min_x, min_y, max_x, max_y, size_x, size_y, dpi, bits, dither, format.encode(), options.encode())
        




    def render_bitmap(self, view, min_x, min_y, max_x, max_y, file, max_res):
        """
        Render a map to a bitmap.
        
        :param view:     View we exporting units in
        :param min_x:    MinX
        :param min_y:    MinY
        :param max_x:    MaxX
        :param max_y:    MaxY
        :param file:     File to generate (BMP or PNG, otherwise extension forced to BMP)
        :param max_res:  Maximum resolution in either direction, -1 for none (will change the pixel density of image if exceeded)
        :type  view:     str
        :type  min_x:    float
        :type  min_y:    float
        :type  max_x:    float
        :type  max_y:    float
        :type  file:     str
        :type  max_res:  int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._render_bitmap(view.encode(), min_x, min_y, max_x, max_y, file.encode(), max_res)
        




    def render_view_bitmap(self, view, group, min_x, min_y, max_x, max_y, file, max_res):
        """
        Render a map view to a bitmap.
        
        :param view:     `GXMVIEW <geosoft.gxapi.GXMVIEW>` object
        :param group:    group (-1 for all)
        :param min_x:    MinX
        :param min_y:    MinY
        :param max_x:    MaxX
        :param max_y:    MaxY
        :param file:     File to generate (BMP or PNG, otherwise extension forced to BMP)
        :param max_res:  Maximum resolution in either direction, -1 for none (will change the pixel density of image if exceeded)
        :type  view:     GXMVIEW
        :type  group:    int
        :type  min_x:    float
        :type  min_y:    float
        :type  max_x:    float
        :type  max_y:    float
        :type  file:     str
        :type  max_res:  int

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._render_view_bitmap(view, group, min_x, min_y, max_x, max_y, file.encode(), max_res)
        




# 3D View



    def create_linked_3d_view(self, mview, view_name, min_x, min_y, max_x, max_y):
        """
        Create a 3D View in this map that is linked to a `GXMVIEW <geosoft.gxapi.GXMVIEW>` in a 3D View file.
        
        :param mview:      `GX3DV <geosoft.gxapi.GX3DV>`'s 3D `GXMVIEW <geosoft.gxapi.GXMVIEW>`
        :param view_name:  New view name
        :param min_x:      X minimum in mm
        :param min_y:      Y minimun in mm
        :param max_x:      X maximum in mm
        :param max_y:      Y maximum in mm
        :type  mview:      GXMVIEW
        :type  view_name:  str
        :type  min_x:      float
        :type  min_y:      float
        :type  max_x:      float
        :type  max_y:      float

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._create_linked_3d_view(mview, view_name.encode(), min_x, min_y, max_x, max_y)
        




# Miscellaneous



    def agg_list(self, lst, optn):
        """
        Get a list of all aggregates in this map.
        
        :param lst:   List to hold the views (allow up to 96 characters)
        :param optn:  0 - view/agg only 1 - view/agg/layer
        :type  lst:   GXLST
        :type  optn:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** List items are returned as view/agg/layer.
        The layer name is optional

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class.
        """
        self._agg_list(lst, optn)
        




    def agg_list_ex(self, lst, optn, mode):
        """
        Get a list of aggregates in this map based on a mode
        
        :param lst:   List to hold the views (allow up to 96 characters)
        :param optn:  0 - view/agg only 1 - view/agg/layer
        :param mode:  :ref:`MAP_LIST_MODE`
        :type  lst:   GXLST
        :type  optn:  int
        :type  mode:  int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** List items are returned as view/agg/layer.
        The layer name is optional

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class.
        """
        self._agg_list_ex(lst, optn, mode)
        




    def clean(self):
        """
        Clean up empty groups in all views in map.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._clean()
        




    def commit(self):
        """
        Commit any changes to a map.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._commit()
        




    def copy_map_to_view(self, dest_map, dest_view):
        """
        Copy entire map into one view in output map.
        
        :param dest_map:   Destination `GXMAP <geosoft.gxapi.GXMAP>` name
        :param dest_view:  Name of View
        :type  dest_map:   str
        :type  dest_view:  str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy_map_to_view(dest_map.encode(), dest_view.encode())
        




    def crc_map(self, crc, file):
        """
        Generate an XML CRC of a `GXMAP <geosoft.gxapi.GXMAP>`
        
        :param crc:   CRC returned
        :param file:  Name of xml to generate (.zip added)
        :type  crc:   int_ref
        :type  file:  str

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        crc.value = self._crc_map(crc.value, file.encode())
        



    @classmethod
    def create(cls, name, mode):
        """
        Create a `GXMAP <geosoft.gxapi.GXMAP>`.
        
        :param name:  `GXMAP <geosoft.gxapi.GXMAP>` file name
        :param mode:  :ref:`MAP_OPEN`
        :type  name:  str
        :type  mode:  int

        :returns:     `GXMAP <geosoft.gxapi.GXMAP>` Object
        :rtype:       GXMAP

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMAP._create(GXContext._get_tls_geo(), name.encode(), mode)
        return GXMAP(ret_val)



    @classmethod
    def current(cls):
        """
        This method returns the Current map opened.
        

        :returns:    `GXMAP <geosoft.gxapi.GXMAP>` Object
        :rtype:      GXMAP

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If there is no current map, and running interactively,
        the user is prompted to open a map.
        """
        ret_val = gxapi_cy.WrapMAP._current(GXContext._get_tls_geo())
        return GXMAP(ret_val)




    def delete_view(self, name):
        """
        Deletes a view in this map.
        
        :param name:  View Name to delete
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the view does not exist, nothing happens.
        """
        self._delete_view(name.encode())
        






    def discard(self):
        """
        Discard all changes made to the map.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._discard()
        




    def dup_map(self, ma_pd, content):
        """
        Duplicate copy of current map.
        
        :param ma_pd:    Destination `GXMAP <geosoft.gxapi.GXMAP>` object
        :param content:  :ref:`DUPMAP`
        :type  ma_pd:    GXMAP
        :type  content:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Before version 6.2 text in maps were displayed with a character set
        defining how characters above ASCII 127 would be displayed. 6.2 introduced
        Unicode in the core montaj engine that eliminated the need for such a setting and
        greatly increased the number of symbols that can be used. The only caveat
        of the new system is that text may appear corrupted (especially with GFN fonts) in
        versions prior to 6.2 that render maps created in version 6.2 and later.
        The constant `DUPMAP_COPY_PRE62 <geosoft.gxapi.DUPMAP_COPY_PRE62>` provides a way to create maps that can be
        distributed to versions prior to 6.2.
        """
        self._dup_map(ma_pd, content)
        




    def get_lpt(self):
        """
        Get the `GXLPT <geosoft.gxapi.GXLPT>` Object of a `GXMAP <geosoft.gxapi.GXMAP>`.
        

        :returns:    `GXLPT <geosoft.gxapi.GXLPT>` Object
        :rtype:      GXLPT

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_lpt()
        return GXLPT(ret_val)




    def get_map_size(self, xmin, ymin, xmax, ymax):
        """
        Get the size of the Map.
        
        :param xmin:  X minimum in mm
        :param ymin:  Y minimun in mm
        :param xmax:  X maximum in mm
        :param ymax:  Y maximum in mm
        :type  xmin:  float_ref
        :type  ymin:  float_ref
        :type  xmax:  float_ref
        :type  ymax:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        xmin.value, ymin.value, xmax.value, ymax.value = self._get_map_size(xmin.value, ymin.value, xmax.value, ymax.value)
        




    def get_meta(self):
        """
        Get the map's `GXMETA <geosoft.gxapi.GXMETA>`
        

        :returns:    `GXMETA <geosoft.gxapi.GXMETA>` Object
        :rtype:      GXMETA

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the map has no `GXMETA <geosoft.gxapi.GXMETA>`, an empty `GXMETA <geosoft.gxapi.GXMETA>` will be created.
        """
        ret_val = self._get_meta()
        return GXMETA(ret_val)




    def get_reg(self):
        """
        Get the map's `GXREG <geosoft.gxapi.GXREG>`
        

        :returns:    `GXREG <geosoft.gxapi.GXREG>` Object
        :rtype:      GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the map has no `GXREG <geosoft.gxapi.GXREG>`, an empty `GXREG <geosoft.gxapi.GXREG>` will be created.
        """
        ret_val = self._get_reg()
        return GXREG(ret_val)




    def group_list(self, lst):
        """
        Get a list of all views/groups in this map.
        
        :param lst:  List to hold the view/groups.  Names may be up to 2080 characters in length.
        :type  lst:  GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns all groups in the form "ViewName\\GroupName"
        To get a `GXLST <geosoft.gxapi.GXLST>` of groups in a specific map view, use
        the `GXMVIEW.list_groups <geosoft.gxapi.GXMVIEW.list_groups>` function.

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class.
            `GXMVIEW.list_groups <geosoft.gxapi.GXMVIEW.list_groups>`
        """
        self._group_list(lst)
        




    def group_list_ex(self, lst, mode):
        """
        Get a list of views/groups in this map for this mode
        
        :param lst:   List to hold the views.  View names may be up to 2080 characters in length.
        :param mode:  :ref:`MAP_LIST_MODE`
        :type  lst:   GXLST
        :type  mode:  int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class.
        """
        self._group_list_ex(lst, mode)
        




    def duplicate_view(self, view, n_view, copy):
        """
        Duplicate an entire view
        
        :param view:    Name of view to duplicate
        :param n_view:  Name of new view created (pass in "" and the new name is returned)
        :param copy:    Copy all groups
        :type  view:    str
        :type  n_view:  str_ref
        :type  copy:    bool

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        n_view.value = self._duplicate_view(view.encode(), n_view.value.encode(), copy)
        




    def exist_view(self, name):
        """
        Checks to see if a view exists.
        
        :param name:  View name
        :type  name:  str

        :returns:     0 view does not exist.
                      1 view exists.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._exist_view(name.encode())
        return ret_val




    def get_class_name(self, cl, name):
        """
        Get a class name.
        
        :param cl:    Class
        :param name:  Name
        :type  cl:    str
        :type  name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Map class names are intended to be used to record the
        names of certain view classes in the map, such as the
        "Data", "Base" and "Section" views.

        There can only be one name for each class, but it can
        be changed.  This lets the "Data" class name change,
        for example, so plotting can select which class to plot
        to.

        If a name is not set, the class name is set and
        returned.
        """
        name.value = self._get_class_name(cl.encode(), name.value.encode())
        




    def get_file_name(self, name):
        """
        Get the name of the map.
        
        :param name:  Returned map file name
        :type  name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value = self._get_file_name(name.value.encode())
        




    def get_map_name(self, name):
        """
        Get the Map Name of the Map.
        
        :param name:  Returned map name
        :type  name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value = self._get_map_name(name.value.encode())
        




    def packed_files(self):
        """
        The number of packed files in the current map.
        

        :returns:    The number of packed files in map.
        :rtype:      int

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._packed_files()
        return ret_val




    def un_pack_files_ex(self, force, errors):
        """
        UnPack all files from map to workspace.
        
        :param force:   (0 - Produce errors, 1 - Force overwrites)
        :param errors:  List of files that are problematic returned
        :type  force:   int
        :type  errors:  str_ref

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The option to force will simply overwrite the files.
        When the non-force option is in effect the method will
        stop if any files are going to be overwritting. These
        file names will end up in the Errors string.
        """
        errors.value = self._un_pack_files_ex(force, errors.value.encode())
        




    def un_pack_files_to_folder(self, force, dir, errors):
        """
        UnPack all files from map to workspace.
        
        :param force:   (0 - Produce errors, 1 - Force overwrites)
        :param dir:     Directory to place unpacked files in.
        :param errors:  List of files that are problematic returned
        :type  force:   int
        :type  dir:     str
        :type  errors:  str_ref

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        errors.value = self._un_pack_files_to_folder(force, dir.encode(), errors.value.encode())
        




    def pack_files(self):
        """
        Pack all files in the map so that it can be mailed.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._pack_files()
        




    def render(self, name):
        """
        Render a map to file/device.
        
        :param name:  Plot file/device
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._render(name.encode())
        




    def resize_all(self):
        """
        Resize a map to the extents of all views.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is the same as `resize_all_ex <geosoft.gxapi.GXMAP.resize_all_ex>` with
        `MVIEW_EXTENT_CLIP <geosoft.gxapi.MVIEW_EXTENT_CLIP>`.
        """
        self._resize_all()
        




    def resize_all_ex(self, ext):
        """
        `resize_all <geosoft.gxapi.GXMAP.resize_all>` with selection of view extent type selection.
        
        :param ext:  :ref:`MVIEW_EXTENT`
        :type  ext:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** `MVIEW_EXTENT_VISIBLE <geosoft.gxapi.MVIEW_EXTENT_VISIBLE>` gives a more "reasonable" map size, and won't
        clip off labels outside a graph window.
        """
        self._resize_all_ex(ext)
        




    def get_map_scale(self):
        """
        Get the current map scale
        

        :returns:    The current map scale
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If there is a "Data" view, the scale is derived from
        this view.

        If their is no data view, the scale is derived
        from the first view that is not scaled in mm.
        otherwise, the scale is 1000 (mm).

        All views must be closed, or open read-only.
        """
        ret_val = self._get_map_scale()
        return ret_val




    def save_as_mxd(self, mxd):
        """
        Save as ArcGIS `GXMXD <geosoft.gxapi.GXMXD>`
        
        :param mxd:  Geosoft map file name
        :type  mxd:  str

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._save_as_mxd(mxd.encode())
        




    def set_class_name(self, cl, name):
        """
        Set a class name.
        
        :param cl:    Class
        :param name:  Name
        :type  cl:    str
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Map class names are intended to be used to record the
        names of certain view classes in the map, such as the
        "Data", "Base" and "Section" views.

        There can only be one name for each class, but it can
        be changed.  This lets the "Data" class name change,
        for example, so plotting can select which class to plot
        to.

        If a name is not set, the class name is set and
        returned.
        """
        self._set_class_name(cl.encode(), name.encode())
        




    def set_current(self):
        """
        Sets the current map to this map.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_current()
        




    def set_map_name(self, name):
        """
        Set the Map Name of the Map.
        
        :param name:  Map Name
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_map_name(name.encode())
        




    def set_map_scale(self, scale):
        """
        Set the current map scale
        
        :param scale:  New map scale (must be > 0).
        :type  scale:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All views in the map will be resized for the new
        map scale.
        """
        self._set_map_scale(scale)
        




    def set_map_size(self, xmin, ymin, xmax, ymax):
        """
        Set the size of the Map.
        
        :param xmin:  X minimum in mm
        :param ymin:  Y minimun in mm
        :param xmax:  X maximum in mm
        :param ymax:  Y maximum in mm
        :type  xmin:  float
        :type  ymin:  float
        :type  xmax:  float
        :type  ymax:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The map size is area on the `GXMAP <geosoft.gxapi.GXMAP>` that contains graphics
        to be plotted.  The area can be bigger or smaller that
        the current views.  In the absense of any other information
        only the area defined by the map size is plotted.

        .. seealso::

            SetSizeViews_MAP
        """
        self._set_map_size(xmin, ymin, xmax, ymax)
        




    def set_meta(self, meta):
        """
        Write a `GXMETA <geosoft.gxapi.GXMETA>` to a map.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` to write to map
        :type  meta:  GXMETA

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_meta(meta)
        




    def set_reg(self, reg):
        """
        Write a `GXREG <geosoft.gxapi.GXREG>` to a map.
        
        :param reg:  `GXREG <geosoft.gxapi.GXREG>` to write to map
        :type  reg:  GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_reg(reg)
        



    @classmethod
    def sync(cls, map):
        """
        Syncronize the Metadata
        
        :param map:  Geosoft map file name
        :type  map:  str

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMAP._sync(GXContext._get_tls_geo(), map.encode())
        




    def un_pack_files(self):
        """
        UnPack all files from map to workspace.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._un_pack_files()
        




    def view_list(self, lst):
        """
        Get a list of all views in this map.
        
        :param lst:  List to hold the views.  View names may be up to 2080 characters in length.
        :type  lst:  GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `GXLST <geosoft.gxapi.GXLST>` class.
        """
        self._view_list(lst)
        




    def view_list_ex(self, lst, mode):
        """
        Get a list of views of certain types in this map
        
        :param lst:   List to hold the views.  View names may be up to 2080 characters in length.
        :param mode:  :ref:`MAP_LIST_MODE`
        :type  lst:   GXLST
        :type  mode:  int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._view_list_ex(lst, mode)
        




    def get_data_proj(self):
        """
        Get the projection type of the Data view of a map.
        

        :returns:    Project type as an integer
        :rtype:      int

        .. versionadded:: 8.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_data_proj()
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer