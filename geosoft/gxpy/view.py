"""
Views, both 2D and 3D.

.. note::

    Regression tests provide usage examples: `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_view.py>`_

"""
import os
from functools import wraps

import geosoft
import geosoft.gxapi as gxapi
from . import coordinate_system as gxcs
from . import utility as gxu
from . import map as gxmap

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class ViewException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.2
    """
    pass

def _plane_err(plane, view):
    raise ViewException(_t('Plane "{}" does not exist in view "{}"'.format(plane,view)))

VIEW_NAME_SIZE = 2080

READ_ONLY = gxapi.MVIEW_READ
WRITE_NEW = gxapi.MVIEW_WRITENEW
WRITE_OLD = gxapi.MVIEW_WRITEOLD

UNIT_VIEW = 0
UNIT_MAP = 2
UNIT_VIEW_UNWARPED = 3

GROUP_ALL = 0
GROUP_MARKED = 1
GROUP_VISIBLE = 2
GROUP_AGG = 3
GROUP_CSYMB = 4
GROUP_VOXD = 5

EXTENT_ALL = gxapi.MVIEW_EXTENT_ALL
EXTENT_VISIBLE = gxapi.MVIEW_EXTENT_VISIBLE
EXTENT_CLIPPED = gxapi.MVIEW_EXTENT_CLIP

class View:
    """
    Geosoft view class.

    :parameters:

        :name:          view name, default is "_unnamed_view".
        :map:           map instance, if not specified a new default map is created and deleted on closing
        :mode:          open view mode:

                        ::

                            gxpy.view.READ_ONLY
                            gxpy.view.WRITE_NEW
                            gxpy.view.WRITE_OLD

        The following are used with ``mode=gxpy.view.WRITE_NEW``:

        :cs:            coordinate system as a gxpy.coordinate_system.Coordinate_system instance, or one of the Coordinate_system
                        constructor types.
        :map_location:  (x, y) view location on the map, in map cm
        :area:          (min_x, min_y, max_x, max_y) area in view units
        :scale:         Map scale if a coordinate system is defined.  If the coordinate system is not
                        defined this is view units per map metre.
        :copy:          name of a view to copy into the new view.

    :properties:

        :map:               the Map instance that contains this view
        :name:              the name of the view
        :units_per_metre:   view units per view metres (eg. a view in 'ft' will be 3.28084).
        :units_per_map_cm:  view units per map cm. (eg. a view in ft, with a scale of 1:12000 returns 393.7 ft/cm)
        :unit_name:         view units name.
        :scale:             view scale, which is the # of view units per  unit on the printed map.
        :aspect:            ratio of the view x units to y units (x/y).  Usually this is 1.0.
        :extent:            extent of the visible (clipped) view in view units.
        :extent_map_cm:     extent of the visible view in map cm.

    .. versionadded:: 9.2
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self._close()

    def _close(self):
        if self._open:
            self.gxview = None
            self._pen = None
            self._map = None  # release map
            self._open = False

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __init__(self,
                 map,
                 name="_unnamed_view",
                 mode=WRITE_OLD,
                 cs=None,
                 map_location=(0, 0),
                 area=(0, 0, 30, 20),
                 scale=100,
                 copy=None):

        if type(map) is not geosoft.gxpy.map.Map:
            raise ViewException('First parameter is not a Map instance.')

        self._map = map
        self._name = map.classview(name)
        if mode == WRITE_OLD and not map.has_view(self._name):
            mode = WRITE_NEW
        self.gxview = gxapi.GXMVIEW.create(self._map.gxmap, self._name, mode)
        self._mode = mode
        self._lock = None
        self._open = True

        if mode == WRITE_NEW:
            self.locate(cs, map_location, area, scale)

            if copy:
                with View(map, name=copy, mode=READ_ONLY) as v:
                    v.gxview.mark_all_groups(1)
                    v.gxview.copy_marked_groups(self.gxview)

        else:
            ipj = gxapi.GXIPJ.create()
            self.gxview.get_ipj(ipj)
            self._cs = gxcs.Coordinate_system(ipj)
            metres_per = self.cs.metres_per_unit
            self._uname = self.cs.units_name
            if metres_per <= 0.:
                raise ViewException('Invalid units {}({})'.format(self._uname, metres_per))
            self._metres_per_unit = 1.0 / metres_per

    @property
    def lock(self):
        return self._lock

    @lock.setter
    def lock(self, group):
        if group:
            if self.lock:
                raise ViewException(_t('View is locked by group {}.', format(self.lock)))
            self._lock = group
        else:
            self._lock = None

    @property
    def cs(self):
        return self._cs

    @cs.setter
    def cs(self, cs):
        self._cs = gxcs.Coordinate_system(cs)
        metres_per = self._cs.metres_per_unit
        self._uname = self._cs.units_name
        if metres_per <= 0.:
            raise ViewException('Invalid units {}({})'.format(self._uname, metres_per))
        self._metres_per_unit = 1.0 / metres_per
        self.gxview.set_ipj(self._cs.gxipj)

    def close(self):
        """
        Close a view.  Use yo close a view outside of a with ... as: construct.
        
        .. versionadded:: 9.2
        """
        self._close()

    def locate(self,
               cs=None,
               map_location=None,
               area=None,
               scale=None):
        """
        Locate and scale the view on the map.

        :parameters:
            :cs:            coordinate system as a gxpy.coordinate_system.Coordinate_system instance, or one of the Coordinate_system
                            constructor types.
            :map_location:  New (x, y) view location on the map, in map cm.
            :area:          New (min_x, min_y, max_x, max_y) area in view units
            :scale:         New scale in view units per map metre, either as a single value or
                            (x_scale, y_scale)

        .. versionadded:: 9.2
        """

        if self._mode == READ_ONLY:
            raise ViewException('Cannot modify a READ_ONLY view.')

        # coordinate system
        self.cs = cs
        upm = 1.0 / self.cs.metres_per_unit

        if area == None:
            area = self.extent_clip

        # area and scale
        if hasattr(scale, "__iter__"):
            x_scale, y_scale = scale
        else:
            x_scale = y_scale = scale
        a_minx, a_miny, a_maxx, a_maxy = area
        mm_minx = map_location[0] * 10.0
        mm_miny = map_location[1] * 10.0
        mm_maxx = mm_minx + (a_maxx - a_minx) * 1000.0 / upm / x_scale
        mm_maxy = mm_miny + (a_maxy - a_miny) * 1000.0 / upm / y_scale
        self.gxview.fit_window(mm_minx, mm_miny, mm_maxx, mm_maxy,
                               a_minx, a_miny, a_maxx, a_maxy)
        self.gxview.set_window(a_minx, a_miny, a_maxx, a_maxy, UNIT_VIEW)
        # self.gxview.set_u_fac(1.0 / x_scale)

    @property
    def map(self):
        """ gxpy.Map instance that contains this view."""
        return self._map

    @property
    def name(self):
        """ Name of the view"""
        return self._name

    @property
    def is_3d(self):
        return bool(self.gxview.is_view_3d())

    @property
    def units_per_metre(self):
        return self._metres_per_unit

    @property
    def units_per_map_cm(self):
        return self.gxview.scale_mm() * 10.0

    @property
    def units_name(self):
        return self._uname

    def _groups(self, gtype=GROUP_ALL):

        def gdict(what):
            self.gxview.list_groups(gxlst, what)
            return gxu.dict_from_lst(gxlst)

        gxlst = gxapi.GXLST.create(VIEW_NAME_SIZE)

        if gtype == GROUP_ALL:
            return list(gdict(gxapi.MVIEW_GROUP_LIST_ALL))

        elif gtype == GROUP_MARKED:
            return list(gdict(gxapi.MVIEW_GROUP_LIST_MARKED))

        elif gtype == GROUP_VISIBLE:
            return list(gdict(gxapi.MVIEW_GROUP_LIST_VISIBLE))

        gd = gdict(gxapi.MVIEW_GROUP_LIST_ALL)
        aggs = []

        # gxapi mappings from local GROUP_NAME manifest
        isg = (None, None, None, gxapi.MVIEW_IS_AGG, gxapi.MVIEW_IS_CSYMB, gxapi.MVIEW_IS_VOXD)[gtype]

        for g in gd:
            if self.gxview.is_group(g, isg):
                aggs.append(g)
        return aggs

    @property
    def group_list(self):
        return self._groups()

    @property
    def group_list_marked(self):
        return self._groups(GROUP_MARKED)

    @property
    def group_list_visible(self):
        return self._groups(GROUP_VISIBLE)

    @property
    def group_list_agg(self):
        return self._groups(GROUP_AGG)

    @property
    def group_list_csymb(self):
        return self._groups(GROUP_CSYMB)

    @property
    def group_list_voxel(self):
        return self._groups(GROUP_VOXD)

    def has_group(self, group):
        """ Returns True if the map contains this group."""
        return self.gxview.exist_group(group)

    def _extent(self, what):
        xmin = gxapi.float_ref()
        ymin = gxapi.float_ref()
        xmax = gxapi.float_ref()
        ymax = gxapi.float_ref()
        self.gxview.extent(what, UNIT_VIEW, xmin, ymin, xmax, ymax)
        return xmin.value, ymin.value, xmax.value, ymax.value

    @property
    def extent_clip(self):
        return self._extent(gxapi.MVIEW_EXTENT_CLIP)

    @property
    def extent_all(self):
        return self._extent(gxapi.MVIEW_EXTENT_ALL)

    @property
    def extent_visible(self):
        return self._extent(gxapi.MVIEW_EXTENT_VISIBLE)

    def extent_map_cm(self, extent):
        """
        Return a view extent in map cm.

        :param extent: tuple returned an extent property.

        .. versionadded:: 9.2
        """
        xmin, ymin = self.view_to_map_cm(extent[0], extent[1])
        xmax, ymax = self.view_to_map_cm(extent[2], extent[3])
        return xmin, ymin, xmax, ymax

    @property
    def scale(self):
        return 1000.0 * self.gxview.scale_mm() * self.cs.metres_per_unit

    @property
    def aspect(self):
        return self.gxview.scale_ymm() / self.gxview.scale_mm()

    def extent_group(self, group, unit=UNIT_VIEW):
        xmin = gxapi.float_ref()
        ymin = gxapi.float_ref()
        xmax = gxapi.float_ref()
        ymax = gxapi.float_ref()
        self.gxview.get_group_extent(group, xmin, ymin, xmax, ymax, unit)
        return xmin.value, ymin.value, xmax.value, ymax.value

    def delete_group(self, group_name):
        """
        Delete a group from a map. Nothing happens if the view does not contain this group.

        :param group_name: Name of the group to delete.

        .. versionadded:: 9.2
        """

        self.gxview.delete_group(group_name)

    def map_cm_to_view(self, x, y=None):
        """
        Returns the location of this point on the map (in cm) to the view location in view units.
            
        :param x:   x, or a tupple (x,y), in map cm
        :param y:   y if x is not a tupple
        
        .. versionadded:: 9.2
        """

        if y is None:
            y = x[1]
            x = x[0]
        xr = gxapi.float_ref()
        xr.value = x * 10.0
        yr = gxapi.float_ref()
        yr.value = y * 10.0
        self.gxview.plot_to_view(xr, yr)
        return xr.value, yr.value

    def view_to_map_cm(self, x, y=None):
        """ 
        Returns the location of this point on the map in the view.
        
        :param x:   x, or a tupple (x,y), in view units
        :param y:   y if x is not a tupple
        
        .. versionadded:: 9.2
        """
        if y is None:
            y = x[1]
            x = x[0]
        xr = gxapi.float_ref()
        xr.value = x
        yr = gxapi.float_ref()
        yr.value = y
        self.gxview.view_to_plot(xr, yr)
        return xr.value / 10.0, yr.value / 10.0

    def get_class_name(self, view_class):
        """
        Get the name associated with a view class.

        :param view_class:  desired class in this view

        Common view class names are::

            'Plane'     the name of the default 2D drawing plane

        Other class names may be defined, though they are not used by Geosoft.

        :return: name associated with the class, '' if not defined.

        .. versionadded:: 9.2
        """
        sr = gxapi.str_ref()
        self.gxview.get_class_name(view_class, sr)
        return sr.value.lower()

    def set_class_name(self, view_class, name):
        """
        Set the name associated with a class.

        :param view_class:  class name in this view
        :param name:        name of the view associated with this class.

        Common view class names are::

            'Plane'     the name of the default 2D drawing plane

        .. versionadded:: 9.2
        """
        self.gxview.set_class_name(view_class, name)

class View_3d(View):
    """
    Geosoft 3D views are stored in a file with extension `.geosoft_3dv`.  A 3d view is required
    to draw 3D elements using gxpy.group.Draw_3d, which must be created from a View_3d instance.
    
    3D views also contain 2D drawing planes on which gxpy.group.Draw groups are placed.  A default 
    horizontal plane at elevation 0, named 'plane_0' is created when a new 3d view is created.
    
    Planes are flat by default, but can be provided a grid that defines the plane surface relief,
    which is intended for creating tinkgs like terrain surfaces on which 2d graphics are rendered.
    
    Planes can also be oriented within the 3D space to create sections, or for other more esoteric
    purposes.
    
    Constructors:

        ======== =============================
        `open()` open an existing geosoft_3dv
        `new()`  create a new geosoft_3dv
        ======== =============================
    
    Properties:
    
        TODO - complete...
        
    .. versionadded:: 9.2    
    """

    def __init__(self, file_name, mode, _internal=False, **kwargs):

        if not _internal:
            raise ViewException(_t("Must be called by a class constructor 'open' or 'new'"))

        file_name = gxmap.map_file_name(file_name, 'geosoft_3dv')
        map = gxmap.Map(file_name=file_name,
                          mode=mode,
                          _internal=True)
        super().__init__(map, '3D', **kwargs)


    @classmethod
    def new(cls, file_name=None, area_2d=None, overwrite=False, **kwargs):
        """
        Createa a new 3D view.
        
        :param file_name:   name for the new 3D view file (.geosoft_3dv added).  If not specified a
                            unique temporary file is created.
        :param area_2d:     2D drawing extent for the default 2D drawing plane
        :param overwrite:   True to overwrite an existing 3DV

        .. versionadded:: 9.2
        """

        if file_name is None:
            file_name = gxmap.unique_temporary_file_name('temp_3dv', 'geosoft_3dv')
        else:
            file_name = gxmap.map_file_name(file_name, 'geosoft_3dv')

        if not overwrite:
            if os.path.isfile(file_name):
                raise ViewException(_t('Cannot overwrite existing file: {}').format(file_name))

        g_3dv = cls(file_name, gxmap.WRITE_NEW, area=area_2d, _internal=True, **kwargs)

        mminx, mminy, mmaxx, mmaxy = g_3dv.extent_map_cm(g_3dv.extent_clip)
        vminx, vminy, vmaxx, vmaxy = g_3dv.extent_clip

        # make this a 3D view
        h3dn = gxapi.GX3DN.create()
        g_3dv.gxview.set_h_3dn(h3dn)
        g_3dv.gxview.fit_map_window_3d(mminx, mminy, mmaxx, mmaxy,
                                       vminx, vminy, vmaxx, vmaxy)

        if area_2d is not None:
            g_3dv.new_drawing_plane('plane_0')

        return g_3dv

    @classmethod
    def open(cls, file_name):
        """
        Open an existing geosoft_3dv file.
        
        :param file_name: name of the geosoft_3dv file
        
        .. versionadded:: 9.2
        """

        file_name = gxmap.map_file_name(file_name, 'geosoft_3dv')
        if not os.path.isfile(file_name):
            raise ViewException(_t('geosoft_3dv file not found: {}').format(file_name))

        g_3dv = cls(file_name, gxmap.WRITE_OLD, _internal=True)

        return g_3dv

    def __exit__(self, xtype, xvalue, xtraceback):
        self.close()

    def close(self):
        self.map.close()
        self._close()

    @property
    def file_name(self):
        return self.map.file_name

    @property
    def name(self):
        return self.map.name

    @property
    def current_3d_drawing_plane(self):
        s = gxapi.str_ref()
        try:
            self.gxview.get_def_plane(s)
            return s.value
        except gxapi.GXError:
            return None

    @current_3d_drawing_plane.setter
    def current_3d_drawing_plane(self, plane):
        if plane:
            if isinstance(plane, int):
                plane = self.plane_name(plane)
            self.gxview.set_def_plane(plane)

    @property
    def plane_list(self):
        gxlst = gxapi.GXLST.create(VIEW_NAME_SIZE)
        self.gxview.list_planes(gxlst)
        return list(gxu.dict_from_lst(gxlst))

    def plane_name(self, plane):
        """Return the name of a numbered plane"""
        if isinstance(plane, str):
            if self.gxview.find_plane(plane) == -1:
                _plane_err(plane, self.name)
            return plane
        gxlst = gxapi.GXLST.create(VIEW_NAME_SIZE)
        self.gxview.list_planes(gxlst)
        item = gxlst.find_item(gxapi.LST_ITEM_VALUE, str(plane))
        if item == -1:
            _plane_err(plane, self.name)
        sr = gxapi.str_ref()
        gxlst.gt_item(gxapi.LST_ITEM_NAME, item, sr)
        return sr.value

    def plane_number(self, plane):
        """Return the plane number of a plane, or None if plane does not exist."""
        if isinstance(plane, int):
            self.plane_name(plane)
            return plane
        plane_number = self.gxview.find_plane(plane)
        if plane_number == -1:
            _plane_err(plane, self.name)
        else:
            return plane_number

    def has_plane(self, plane):
        try:
            n = self.plane_number(plane)
            return True
        except ViewException:
            return False

    def groups_on_plane_list(self, plane):
        gxlst = gxapi.GXLST.create(VIEW_NAME_SIZE)
        if isinstance(plane, str):
            plane = self.plane_number(plane)
        self.gxview.list_plane_groups(plane, gxlst)
        return list(gxu.dict_from_lst(gxlst))

    def new_drawing_plane(self,
                          name,
                          rotation=(0., 0., 0.),
                          offset=(0., 0., 0.),
                          scale=(1., 1., 1.)):

        if self.has_plane(name):
            raise ViewException(_t('3D drawing plane "{}" exists.'.format(name)))

        self.gxview.create_plane(str(name))
        self.gxview.set_plane_equation(self.plane_number(name),
                                       rotation[0], rotation[1], rotation[2],
                                       offset[0], offset[1], offset[2],
                                       scale[0], scale[1], scale[2])