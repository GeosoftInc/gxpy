### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
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
class GXMAP:
    """
    GXMAP class.

    MAPs are containers for `GXMVIEW` objects. A view is a 3-D translation
    and a clip window on a map. Graphic entities can be drawn in an `GXMVIEW`.
    It is recommended that the `GXMAP` class be instantiated by first creating
    an `GXEMAP` object and calling the `GXEMAP.lock`() function.
    (See the explanation on the distinction between the `GXMAP` and `GXEMAP` classes).
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMAP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMAP`
        
        :returns: A null `GXMAP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXMAP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXMAP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Export



    def export_all_in_view(self, name, view, pix_size, dpi, bits, dither, format, options):
        """
        Export the entire map in view units to an external format. View and Group names are removed and plane spatial coordinates will be in the units of the map.
        """
        self._wrapper.export_all_in_view(name.encode(), view.encode(), pix_size, dpi, bits, dither, format.encode(), options.encode())
        




    def export_all_raster(self, name, view, size_x, size_y, dpi, bits, dither, format, options):
        """
        Export the entire map to map to a non-geo raster format.
        """
        self._wrapper.export_all_raster(name.encode(), view.encode(), size_x, size_y, dpi, bits, dither, format.encode(), options.encode())
        




    def export_area_in_view(self, name, view, pix_size, dpi, bits, dither, min_x, min_y, max_x, max_y, format, options):
        """
        Export an area of a map in view units to an external format
        """
        self._wrapper.export_area_in_view(name.encode(), view.encode(), pix_size, dpi, bits, dither, min_x, min_y, max_x, max_y, format.encode(), options.encode())
        




    def export_area_raster(self, name, view, min_x, min_y, max_x, max_y, size_x, size_y, dpi, bits, dither, format, options):
        """
        Export an area of a map to a non-geo raster format.
        """
        self._wrapper.export_area_raster(name.encode(), view.encode(), min_x, min_y, max_x, max_y, size_x, size_y, dpi, bits, dither, format.encode(), options.encode())
        




    def render_bitmap(self, view, min_x, min_y, max_x, max_y, file, p8):
        """
        Render a map to a bitmap.
        """
        self._wrapper.render_bitmap(view.encode(), min_x, min_y, max_x, max_y, file.encode(), p8)
        




# 3D View



    def create_linked_3d_view(self, mview, view_name, min_x, min_y, max_x, max_y):
        """
        Create a 3D View in this map that is linked to a `GXMVIEW` in a 3D View file.
        """
        self._wrapper.create_linked_3d_view(mview._wrapper, view_name.encode(), min_x, min_y, max_x, max_y)
        




# Miscellaneous



    def agg_list(self, lst, optn):
        """
        Get a list of all aggregates in this map.

        **Note:**

        List items are returned as view/agg/layer.
        The layer name is optional

        .. seealso::

            `GXLST` class.
        """
        self._wrapper.agg_list(lst._wrapper, optn)
        




    def agg_list_ex(self, lst, optn, mode):
        """
        Get a list of aggregates in this map based on a mode

        **Note:**

        List items are returned as view/agg/layer.
        The layer name is optional

        .. seealso::

            `GXLST` class.
        """
        self._wrapper.agg_list_ex(lst._wrapper, optn, mode)
        




    def clean(self):
        """
        Clean up empty groups in all views in map.
        """
        self._wrapper.clean()
        




    def commit(self):
        """
        Commit any changes to a map.
        """
        self._wrapper.commit()
        




    def copy_map_to_view(self, dest_map, dest_view):
        """
        Copy entire map into one view in output map.
        """
        self._wrapper.copy_map_to_view(dest_map.encode(), dest_view.encode())
        




    def crc_map(self, crc, file):
        """
        Generate an XML CRC of a `GXMAP`
        """
        crc.value = self._wrapper.crc_map(crc.value, file.encode())
        



    @classmethod
    def create(cls, name, mode):
        """
        Create a `GXMAP`.
        """
        ret_val = gxapi_cy.WrapMAP.create(GXContext._get_tls_geo(), name.encode(), mode)
        return GXMAP(ret_val)



    @classmethod
    def current(cls):
        """
        This method returns the Current map opened.

        **Note:**

        If there is no current map, and running interactively,
        the user is prompted to open a map.
        """
        ret_val = gxapi_cy.WrapMAP.current(GXContext._get_tls_geo())
        return GXMAP(ret_val)




    def delete_view(self, name):
        """
        Deletes a view in this map.

        **Note:**

        If the view does not exist, nothing happens.
        """
        self._wrapper.delete_view(name.encode())
        






    def discard(self):
        """
        Discard all changes made to the map.
        """
        self._wrapper.discard()
        




    def dup_map(self, ma_pd, content):
        """
        Duplicate copy of current map.

        **Note:**

        Before version 6.2 text in maps were displayed with a character set
        defining how characters above ASCII 127 would be displayed. 6.2 introduced
        Unicode in the core montaj engine that eliminated the need for such a setting and
        greatly increased the number of symbols that can be used. The only caveat
        of the new system is that text may appear corrupted (especially with GFN fonts) in
        versions prior to 6.2 that render maps created in version 6.2 and later.
        The constant `DUPMAP_COPY_PRE62` provides a way to create maps that can be
        distributed to versions prior to 6.2.
        """
        self._wrapper.dup_map(ma_pd._wrapper, content)
        




    def get_lpt(self):
        """
        Get the `GXLPT` Object of a `GXMAP`.
        """
        ret_val = self._wrapper.get_lpt()
        return GXLPT(ret_val)




    def get_map_size(self, xmin, ymin, xmax, ymax):
        """
        Get the size of the Map.
        """
        xmin.value, ymin.value, xmax.value, ymax.value = self._wrapper.get_map_size(xmin.value, ymin.value, xmax.value, ymax.value)
        




    def get_meta(self):
        """
        Get the map's `GXMETA`

        **Note:**

        If the map has no `GXMETA`, an empty `GXMETA` will be created.
        """
        ret_val = self._wrapper.get_meta()
        return GXMETA(ret_val)




    def get_reg(self):
        """
        Get the map's `GXREG`

        **Note:**

        If the map has no `GXREG`, an empty `GXREG` will be created.
        """
        ret_val = self._wrapper.get_reg()
        return GXREG(ret_val)




    def group_list(self, lst):
        """
        Get a list of all views/groups in this map.

        **Note:**

        Returns all groups in the form "ViewName\\GroupName"
        To get a `GXLST` of groups in a specific map view, use
        the `GXMVIEW.list_groups` function.

        .. seealso::

            `GXLST` class.
            `GXMVIEW.list_groups`
        """
        self._wrapper.group_list(lst._wrapper)
        




    def group_list_ex(self, lst, mode):
        """
        Get a list of views/groups in this map for this mode

        .. seealso::

            `GXLST` class.
        """
        self._wrapper.group_list_ex(lst._wrapper, mode)
        




    def duplicate_view(self, view, n_view, copy):
        """
        Duplicate an entire view
        """
        n_view.value = self._wrapper.duplicate_view(view.encode(), n_view.value.encode(), copy)
        




    def exist_view(self, name):
        """
        Checks to see if a view exists.
        """
        ret_val = self._wrapper.exist_view(name.encode())
        return ret_val




    def get_class_name(self, cl, name):
        """
        Get a class name.

        **Note:**

        Map class names are intended to be used to record the
        names of certain view classes in the map, such as the
        "Data", "Base" and "Section" views.
        
        There can only be one name for each class, but it can
        be changed.  This lets the "Data" class name change,
        for example, so plotting can select which class to plot
        to.
        
        If a name is not set, the class name is set and
        returned.
        """
        name.value = self._wrapper.get_class_name(cl.encode(), name.value.encode())
        




    def get_file_name(self, name):
        """
        Get the name of the map.
        """
        name.value = self._wrapper.get_file_name(name.value.encode())
        




    def get_map_name(self, name):
        """
        Get the Map Name of the Map.
        """
        name.value = self._wrapper.get_map_name(name.value.encode())
        




    def packed_files(self):
        """
        The number of packed files in the current map.
        """
        ret_val = self._wrapper.packed_files()
        return ret_val




    def un_pack_files_ex(self, force, errors):
        """
        UnPack all files from map to workspace.

        **Note:**

        The option to force will simply overwrite the files.
        When the non-force option is in effect the method will
        stop if any files are going to be overwritting. These
        file names will end up in the Errors string.
        """
        errors.value = self._wrapper.un_pack_files_ex(force, errors.value.encode())
        




    def un_pack_files_to_folder(self, force, dir, errors):
        """
        UnPack all files from map to workspace.
        """
        errors.value = self._wrapper.un_pack_files_to_folder(force, dir.encode(), errors.value.encode())
        




    def pack_files(self):
        """
        Pack all files in the map so that it can be mailed.
        """
        self._wrapper.pack_files()
        




    def render(self, name):
        """
        Render a map to file/device.
        """
        self._wrapper.render(name.encode())
        




    def resize_all(self):
        """
        Resize a map to the extents of all views.

        **Note:**

        This is the same as `resize_all_ex` with
        `MVIEW_EXTENT_CLIP`.
        """
        self._wrapper.resize_all()
        




    def resize_all_ex(self, ext):
        """
        `resize_all` with selection of view extent type selection.

        **Note:**

        `MVIEW_EXTENT_VISIBLE` gives a more "reasonable" map size, and won't
        clip off labels outside a graph window.
        """
        self._wrapper.resize_all_ex(ext)
        




    def get_map_scale(self):
        """
        Get the current map scale

        **Note:**

        If there is a "Data" view, the scale is derived from
        this view.
        
        If their is no data view, the scale is derived
        from the first view that is not scaled in mm.
        otherwise, the scale is 1000 (mm).
        
        All views must be closed, or open read-only.
        """
        ret_val = self._wrapper.get_map_scale()
        return ret_val




    def save_as_mxd(self, mxd):
        """
        Save as ArcGIS `GXMXD`
        """
        self._wrapper.save_as_mxd(mxd.encode())
        




    def set_class_name(self, cl, name):
        """
        Set a class name.

        **Note:**

        Map class names are intended to be used to record the
        names of certain view classes in the map, such as the
        "Data", "Base" and "Section" views.
        
        There can only be one name for each class, but it can
        be changed.  This lets the "Data" class name change,
        for example, so plotting can select which class to plot
        to.
        
        If a name is not set, the class name is set and
        returned.
        """
        self._wrapper.set_class_name(cl.encode(), name.encode())
        




    def set_current(self):
        """
        Sets the current map to this map.
        """
        self._wrapper.set_current()
        




    def set_map_name(self, name):
        """
        Set the Map Name of the Map.
        """
        self._wrapper.set_map_name(name.encode())
        




    def set_map_scale(self, scale):
        """
        Set the current map scale

        **Note:**

        All views in the map will be resized for the new
        map scale.
        """
        self._wrapper.set_map_scale(scale)
        




    def set_map_size(self, xmin, ymin, xmax, ymax):
        """
        Set the size of the Map.

        **Note:**

        The map size is area on the `GXMAP` that contains graphics
        to be plotted.  The area can be bigger or smaller that
        the current views.  In the absense of any other information
        only the area defined by the map size is plotted.

        .. seealso::

            SetSizeViews_MAP
        """
        self._wrapper.set_map_size(xmin, ymin, xmax, ymax)
        




    def set_meta(self, meta):
        """
        Write a `GXMETA` to a map.
        """
        self._wrapper.set_meta(meta._wrapper)
        




    def set_reg(self, reg):
        """
        Write a `GXREG` to a map.
        """
        self._wrapper.set_reg(reg._wrapper)
        



    @classmethod
    def sync(cls, map):
        """
        Syncronize the Metadata
        """
        gxapi_cy.WrapMAP.sync(GXContext._get_tls_geo(), map.encode())
        




    def un_pack_files(self):
        """
        UnPack all files from map to workspace.
        """
        self._wrapper.un_pack_files()
        




    def view_list(self, lst):
        """
        Get a list of all views in this map.

        .. seealso::

            `GXLST` class.
        """
        self._wrapper.view_list(lst._wrapper)
        




    def view_list_ex(self, lst, mode):
        """
        Get a list of views of certain types in this map
        """
        self._wrapper.view_list_ex(lst._wrapper, mode)
        




    def get_data_proj(self):
        """
        Get the projection type of the Data view of a map.
        """
        ret_val = self._wrapper.get_data_proj()
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer