"""
Views, which can be 2D or 3D, contain groups of graphical elements that can be displayed to a user in a Geosoft
Map viewer or a Geosoft 3D viewer.  Geosoft maps can contain any number of 2D or 3D views.

Views contain one or more :class:`geosoft.gxpy.group.Group` instances.  2D views can contain 2D groups, while
3D views can contain both 2D and 3D groups.

:Classes:
    :`View`:        single 2D plane view
    :`View_3d`:     3D view in a `geosoft.3dv` file, or a 3D view on a 2D map.
    :`CrookedPath`: defines the path for a crooked section.

Both 2D and 3D views can be placed on a :class:`geosoft.gxpy.map.Map`, though 3D views
are stored in a `geosoft_3dv` file which can also be viewed separately from a map.

:Constants:
    :READ_ONLY: `geosoft.gxapi.MVIEW_READ`
    :WRITE_NEW: `geosoft.gxapi.MVIEW_WRITENEW`
    :WRITE_OLD: `geosoft.gxapi.MVIEW_WRITEOLD`
    :UNIT_VIEW: 0
    :UNIT_MAP: 2
    :UNIT_VIEW_UNWARPED: 3
    :GROUP_ALL: 0
    :GROUP_MARKED: 1
    :GROUP_VISIBLE: 2
    :GROUP_AGG: 3
    :GROUP_CSYMB: 4
    :GROUP_VOXD: 5
    :GROUP_VECTORVOX: 6
    :GROUP_SURFACE: 7
    :EXTENT_ALL: `geosoft.gxapi.MVIEW_EXTENT_ALL`
    :EXTENT_VISIBLE: `geosoft.gxapi.MVIEW_EXTENT_VISIBLE`
    :EXTENT_CLIPPED: `geosoft.gxapi.MVIEW_EXTENT_CLIP`

.. seealso:: :mod:`geosoft.gxpy.map`, :mod:`geosoft.gxpy.group`

   :mod:`geosoft.geosoft.gxapi.GXMVIEW`

.. note::

    Regression tests provide usage examples:
    `View tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_view.py>`_

"""
import os
import numpy as np
from typing import NamedTuple

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import coordinate_system as gxcs
from . import utility as gxu
from . import map as gxmap
from . import metadata as gxmeta
from . import geometry as gxgeo
from . import spatialdata as gxspd
from . import vv as gxvv


__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class ViewException(geosoft.GXRuntimeError):
    """
    Exceptions from :mod:`geosoft.gxpy.view`.

    .. versionadded:: 9.2
    """
    pass


def _crooked_path_from_ipj(gxipj):
    if gxipj.get_orientation() != gxapi.IPJ_ORIENT_SECTION_CROOKED:
        raise ViewException(_t('This coordinate system does not define a crooked path'))
    dvv = gxvv.GXvv()
    xvv = gxvv.GXvv()
    yvv = gxvv.GXvv()
    log_z = gxapi.int_ref()
    gxipj.get_crooked_section_view_v_vs(dvv.gxvv, xvv.gxvv, yvv.gxvv, log_z)
    return dvv, xvv, yvv, log_z.value


class CrookedPath(gxgeo.Geometry):
    """
    Description of a crooked (x, y) path that defines a crooked-section view, or a crooked-section grid.

    .. versionadded:: 9.4
    """

    def __str__(self):
        return 'CrookedPath "{}", {} points'.format(self.name, len(self))

    def __init__(self, xy_path, log_z=False, **kw):

        super().__init__(**kw)

        if isinstance(xy_path, gxcs.Coordinate_system):
            self.coordinate_system = xy_path
            xy_path = xy_path.gxipj

        if isinstance(xy_path, gxapi.GXIPJ):
            d, x, y, self._log_z = _crooked_path_from_ipj(xy_path)
            self._xy = np.empty((x.length, 2))
            self._xy[:, 0] = x.np
            self._xy[:, 1] = y.np
            self.coordinate_system = gxcs.Coordinate_system(xy_path)

        else:
            if not isinstance(xy_path, gxgeo.PPoint):
                xy_path = gxgeo.PPoint(xy_path, coordinate_system=self.coordinate_system)
            self._xy = xy_path.xy
            self.coordinate_system = xy_path.coordinate_system
            self._log_z = bool(log_z)

        # calculate a distance along the path
        dnp = np.zeros(len(self._xy), dtype=np.float64)
        dx = (self._xy[1:, 0] - self._xy[:-1, 0]) ** 2
        dy = (self._xy[1:, 1] - self._xy[:-1, 1]) ** 2
        dxy = np.sqrt((dx + dy))
        dnp[1:] = dxy
        self._distances = dnp.cumsum()

    def __len__(self):
        return len(self._xy)

    @property
    def xy(self):
        """Path trace as an array (npoints, 2)."""
        return self._xy

    @property
    def distances(self):
        """Distances along path points as an array (npoints) starting at 0."""
        return self._distances

    @property
    def ppoint(self):
        """Path trace as a `geosoft.gxpy.geometry.PPoint` instance."""
        return gxgeo.PPoint(self._xy, coordinate_system=self.coordinate_system)

    def set_in_geosoft_ipj(self, coordinate_system):
        """
        Set the crooked-path in the `geosoft.gxapi.GXIPJ` instance of the coordinate system.

        Geosoft stores crooked-path information in the GXIPJ, from which views are able to

        :param coordinate_system:

        .. versionadded:: 9.4
        """

        # make vv's to set the path
        dvv = gxvv.GXvv(self._distances)
        xvv = gxvv.GXvv(self._xy[:, 0])
        yvv = gxvv.GXvv(self._xy[:, 1])
        coordinate_system.gxipj.set_crooked_section_view(dvv.gxvv, xvv.gxvv, yvv.gxvv, self._log_z)

    @property
    def extent(self):
        return self.ppoint.extent


class PlaneReliefSurfaceInfo(NamedTuple):
    """
    Information about a relief surface assigned to a plane. The following properties are represented:

    surface_grid_name:   grid file name
    refine:              relief refinement between 1 (low) and 4 (high). Default is 3.
    base:                base value in grid, will be at z=0.  Default is 0.
    scale:               scale to apply to grid after removing base, default is 1.
    min:                 minimum clip in unscaled grid values
    max:                 maximum clip in unscaled grid values

    .. versionadded:: 9.9
    """
    surface_grid_name: str
    refine: int
    base: float
    scale: float
    min: float
    max: float


def delete_files(v3d_file):
    """
    Delete a v3d file with associated files. Just calls `geosoft.gxpy.map.delete_files`.
    The view must be closed.

    :param v3d_file: View_3d file name

    .. versionadded:: 9.3.1
    """
    gxmap.delete_files(v3d_file)


def _plane_err(plane, view):
    raise ViewException(_t('Plane "{}" does not exist in view "{}"'.format(plane, view)))


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
GROUP_VECTORVOX = 6
GROUP_SURFACE = 7

_group_selector = (None, None, None,
                   gxapi.MVIEW_IS_AGG,
                   gxapi.MVIEW_IS_CSYMB,
                   gxapi.MVIEW_IS_VOXD,
                   gxapi.MVIEW_IS_VECTOR3D,
                   None)

EXTENT_ALL = gxapi.MVIEW_EXTENT_ALL
EXTENT_VISIBLE = gxapi.MVIEW_EXTENT_VISIBLE
EXTENT_CLIPPED = gxapi.MVIEW_EXTENT_CLIP


class View(gxgeo.Geometry):
    """
    Geosoft view class.

    :Constructors:
        :`open`: open an existing view in a map
        :`new`:  create a new view in a map

    .. versionadded:: 9.2
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_close'):
            self._close()

    def _close(self):
        if hasattr(self, '_open'):
            if self._open:
                self._gxview = None
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
                 coordinate_system=None,
                 map_location=(0, 0),
                 area=(0, 0, 30, 20),
                 scale=100,
                 copy=None,
                 gxmview=None,
                 **kwargs):

        if not isinstance(map, geosoft.gxpy.map.Map):
            raise ViewException(_t('First argument must be a map.'))

        super().__init__(**kwargs)

        self._gx = gx.gx()
        self._map = map

        if gxmview is not None:
            name_ref = gxapi.str_ref()
            gxmview.get_name(name_ref)
            name = name_ref.value
            self._name = map.classview(name)
            self._gxview = gxmview
        else:
            self._name = map.classview(name)
            if mode == WRITE_OLD and not map.has_view(self._name):
                mode = WRITE_NEW
            self._gxview = gxapi.GXMVIEW.create(self._map.gxmap, self._name, mode)

        self._mode = mode
        self._lock = None
        self._open = True
        self._cs = None
        self._clip_mode = False

        if mode == WRITE_NEW:
            self.locate(coordinate_system, map_location, area, scale)

            if copy:
                with View(map, name=copy, mode=READ_ONLY) as v:
                    v.gxview.mark_all_groups(1)
                    v.gxview.copy_marked_groups(self.gxview)

        else:
            ipj = gxapi.GXIPJ.create()
            self.gxview.get_ipj(ipj)
            self._cs = gxcs.Coordinate_system(ipj)
            metres_per = self._cs.metres_per_unit
            self._uname = self._cs.units_name
            if metres_per <= 0.:
                raise ViewException(_t('Invalid units {}({})'.format(self._uname, metres_per)))
            self._metres_per_unit = 1.0 / metres_per

    @classmethod
    def from_gxapi(cls, gxmap, gxmview):
        """
        Instantiate View from gxapi instance.

        :param gxmap:      a gxapi.CGXMAP
        :param gxmview:    a gxapi.CGXMVIEW

        .. versionadded:: 9.9
        """
        return cls(geosoft.gxpy.map.Map.from_gxapi(gxmap), gxmview=gxmview)


    @classmethod
    def new(cls,
            map=None,
            name="_unnamed_view",
            coordinate_system=None,
            map_location=(0, 0),
            area=(0, 0, 30, 20),
            scale=100,
            copy=None,
            crooked_path=None):
        """
        Create a new view on a map.

        :parameters:

            :map:               :class:`geosoft.gxpy.map.Map` instance, if not specified a new unique default map is
                                created and deleted when this session finished.
            :name:              view name, default is "_unnamed_view".
            :coordinate_system: coordinate system as a `geosoft.gxpy.coordinate_system.Coordinate_system` instance, or
                                one of the Coordinate_system constructor types.
            :map_location:      (x, y) view location on the map, in map cm, default (0, 0)
            :area:              (min_x, min_y, max_x, max_y) area in view units, default (0, 0, 30, 20)
            :scale:             Map scale if a coordinate system is defined.  If the coordinate system is not
                                defined this is view units per map metre.
            :copy:              name of a view to copy into the new view.
            :crooked_path:      provide a `CrookedPath` instance to create a section view along a wandering path.
                                Should the coordinate system already contain a crooked path it will be replaced.

        .. versionadded:: 9.2
        """

        if map is None:
            map = gxmap.Map.new()

        view = cls(map,
                   mode=WRITE_NEW,
                   name=name,
                   coordinate_system=coordinate_system,
                   map_location=map_location,
                   area=area,
                   scale=scale,
                   copy=copy)

        if crooked_path:
            if not isinstance(crooked_path, CrookedPath):
                crooked_path = CrookedPath(crooked_path, coordinate_system=view.coordinate_system)
            crooked_path.set_in_geosoft_ipj(view.coordinate_system)

        return view

    @classmethod
    def open(cls, map, view_name, read_only=False):
        """
        Open an en existing view on a map.

        :param map:         :class:`geosoft.gxpy.map.Map`
        :param view_name:   name of the view
        :param read_only:   True to open read-only

        .. versionadded:: 9.2
        """
        if not map.has_view(view_name):
            raise ViewException(_t('Map does not have a view named \'{}\''.format(view_name)))
        if read_only:
            mode = READ_ONLY
        else:
            mode = WRITE_OLD
        view = cls(map, name=view_name, mode=mode)
        return view

    @property
    def lock(self):
        """
        True if the view is locked by a group.  Only one group may hold a lock on a view at the
        same time.  When drawing with groups you should use a `with gxgrp.Draw(...) as g:`
        which will ensure group locks are properly created and released.
        """
        return self._lock

    @lock.setter
    def lock(self, group):
        if group:
            if self.lock:
                raise ViewException(_t('View is locked by group {}.').format(self.lock))
            self._lock = group
        else:
            self._lock = None

    @property
    def is_crooked_path(self):
        """True if this grid follows a crooked path section."""
        return self.coordinate_system.gxipj.get_orientation() == gxapi.IPJ_ORIENT_SECTION_CROOKED

    def crooked_path(self):
        """
        Return the `CrookedPath` instance for a crooked-path view.

        .. versionadded::9.4
        """
        if not self.is_crooked_path:
            raise ViewException(_t("This is not a crooked-path view."))
        return CrookedPath(self.coordinate_system)

    @property
    def clip(self):
        """
        Current view clip mode for groups, applies to groups following in this stream. Can be set.

        .. versionadded:: 9.3.1
        """
        return self._clip_mode

    @clip.setter
    def clip(self, mode):
        self._clip_mode = bool(mode)
        self.gxview.group_clip_mode(int(mode))

    @property
    def metadata(self):
        """
        Return the view/map metadata as a dictionary.  Can be set, in which case
        the dictionary items passed will be added to, or replace existing metadata.
        All views on a map share the metadata with the map.

        .. versionadded:: 9.2
        """
        return self.map.metadata

    @metadata.setter
    def metadata(self, meta):
        self.map.metadata = meta

    @property
    def coordinate_system(self):
        """ :class:`geosoft.gxpy.coordinate_system.Coordinate_system` instance of the view."""
        if self._cs is None:
            self._cs = gxcs.Coordinate_system()
        return self._cs

    @property
    def gxview(self):
        """ The :class:`geosoft.gxapi.GXIPJ` instance handle."""
        return self._gxview

    @coordinate_system.setter
    def coordinate_system(self, cs):
        if not isinstance(cs, gxcs.Coordinate_system):
            cs = gxcs.Coordinate_system(cs)
        self._cs = gxcs.Coordinate_system(cs)
        metres_per = self._cs.metres_per_unit
        self._uname = self._cs.units_name
        if metres_per <= 0.:
            raise ViewException(_t('Invalid units {}({})'.format(self._uname, metres_per)))
        self._metres_per_unit = 1.0 / metres_per
        self.gxview.set_ipj(self._cs.gxipj)

    @property
    def map_scale(self):
        """
        Map scale for this view.

        Can be set, in which case the entire view will move on the map.
        """
        return self.gxview.get_map_scale()

    @map_scale.setter
    def map_scale(self, s):
        if s > 0.0:
            self.gxview.re_scale(s)

    def close(self):
        """
        Close a view.  Use to close a view when working outside of a `with ... as:` construct.

        .. versionadded:: 9.2
        """
        self._close()

    def add_child_files(self, file_list):
        """
        Add files to the list of child files for this view.

        :param file_list: file, or a list of files to add

        .. versionaddded 9.3.1
        """
        meta = self.metadata
        node = 'geosoft/dataset/map/views/' + self.name + '/child_files'
        child_files = gxmeta.get_node_from_meta_dict(node, meta)
        if child_files is None:
            child_files = []
        if isinstance(file_list, str):
            child_files.append(file_list)
        else:
            for f in file_list:
                if f not in child_files:
                    child_files.append(f)
        gxmeta.set_node_in_meta_dict(node, meta, child_files)
        self.metadata = meta

    def locate(self,
               coordinate_system=None,
               map_location=None,
               area=None,
               scale=None):
        """
        Locate and scale the view on the map.

        :parameters:
            :coordinate_system: coordinate system as a class:`gxpy.coordinate_system.Coordinate_system` instance,
                                or one of the Coordinate_system constructor types.
            :map_location:      New (x, y) view location on the map, in map cm.
            :area:              New (min_x, min_y, max_x, max_y) area in view units
            :scale:             New scale in view units per map metre, either as a single value or
                                (x_scale, y_scale), defaults to the current x scale.

        .. versionadded:: 9.2
        """

        if self._mode == READ_ONLY:
            raise ViewException(_t('Cannot modify a READ_ONLY view.'))

        # coordinate system
        if coordinate_system:
            self.coordinate_system = coordinate_system
        upm = self.units_per_metre

        if area is None:
            area = self.extent_clip

        # area and scale
        if scale is None:
            if self.scale is None:
                raise ViewException(_t('A scale is required.'))
            scale = self.scale
        if hasattr(scale, "__iter__"):
            x_scale, y_scale = scale
        else:
            x_scale = y_scale = scale
        a_minx, a_miny, a_maxx, a_maxy = area
        if map_location is None:
            map_location = (0., 0.)
        mm_minx = map_location[0] * 10.0
        mm_miny = map_location[1] * 10.0
        mm_maxx = mm_minx + (a_maxx - a_minx) * 1000.0 / upm / x_scale
        mm_maxy = mm_miny + (a_maxy - a_miny) * 1000.0 / upm / y_scale
        self.gxview.fit_window(mm_minx, mm_miny, mm_maxx, mm_maxy,
                               a_minx, a_miny, a_maxx, a_maxy)
        self.gxview.set_window(a_minx, a_miny, a_maxx, a_maxy, UNIT_VIEW)

    @property
    def map(self):
        """ :class:`geosoft.gxpy.map.Map` instance that contains this view."""
        return self._map

    @property
    def name(self):
        """ Name of the view"""
        return self._name

    @property
    def is_3d(self):
        """True if this is a 3D view"""
        return bool(self.gxview.is_view_3d())

    @property
    def units_per_metre(self):
        """view units per view metres (eg. a view in 'ft' will be 3.28084)"""
        return 1.0 / self.coordinate_system.metres_per_unit

    @property
    def units_per_map_cm(self):
        """view units per map cm. (eg. a view in ft, with a scale of 1:12000 returns 393.7 ft/cm)"""
        return self.gxview.scale_mm() * 10.0

    @property
    def units_name(self):
        """name of the view distance units"""
        return self.coordinate_system.units_name

    @property
    def guid(self):
        """
        The view GUID.

        .. versionadded:: 9.3
        """
        sr = gxapi.str_ref()
        self.gxview.get_guid(sr)
        return sr.value

    def mdf(self, base_view=None):
        """
        Returns the Map Description File specification for this view as a data view.

        :param base_view:   name of the base view on the map from which to calculate margins.  If not specified
                            only the left and bottom margin is calculated based on the view clip minimum
                            location and the right and top margins will be 0.
        :returns:           ((x_size, y_size, margin_bottom, margin_right, margin_top, margin_left),
                             (scale, units_per_metre, x_origin, y_origin))

        .. versionadded: 9.2
        """

        view_mnx, view_mny, view_mxx, view_mxy = self.extent_clip
        map_mnx, map_mny = self.view_to_map_cm(view_mnx, view_mny)
        map_mxx, map_mxy = self.view_to_map_cm(view_mxx, view_mxy)

        if base_view:
            if not isinstance(base_view, View):
                base_view = View(self.map, base_view)
            _, _, mapx, mapy = base_view.extent_clip
            mapx, mapy = base_view.view_to_map_cm(mapx, mapy)
        else:
            mapx, mapy = map_mxx, map_mxy

        m1 = (mapx, mapy, map_mny, mapx - map_mxx, mapy - map_mxy, map_mnx)
        m2 = (self.scale, self.units_per_metre, view_mnx, view_mny)
        return m1, m2

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

        # filter by type wanted
        gd = gdict(gxapi.MVIEW_GROUP_LIST_ALL)
        groups = []
        if gtype == GROUP_SURFACE:
            for g in gd:
                if g[:5] == 'SURF_':
                    groups.append(g)
        else:
            isg = _group_selector[gtype]
            for g in gd:
                if self.gxview.is_group(g, isg):
                    groups.append(g)
        return groups

    @property
    def group_list(self):
        """list of group names in this view"""
        return self._groups()

    @property
    def group_list_marked(self):
        """list of marked group names in this view"""
        return self._groups(GROUP_MARKED)

    @property
    def group_list_visible(self):
        """list of visible group names in this view"""
        return self._groups(GROUP_VISIBLE)

    @property
    def group_list_agg(self):
        """list of aggregate group names in this view"""
        return self._groups(GROUP_AGG)

    @property
    def group_list_csymb(self):
        """list of csymb group names in this view"""
        return self._groups(GROUP_CSYMB)

    @property
    def group_list_voxel(self):
        """list of voxel group names in this view"""
        return self._groups(GROUP_VOXD)

    @property
    def group_list_vectorvoxel(self):
        """list of vectorvoxel group names in this view"""
        return self._groups(GROUP_VECTORVOX)

    @property
    def group_list_surface(self):
        """list of surface group names in this view"""
        return self._groups(GROUP_SURFACE)

    def has_group(self, group):
        """ Returns True if the map contains this group by name."""
        return bool(self.gxview.exist_group(group))

    def _extent(self, what):
        xmin = gxapi.float_ref()
        ymin = gxapi.float_ref()
        xmax = gxapi.float_ref()
        ymax = gxapi.float_ref()
        self.gxview.extent(what, UNIT_VIEW, xmin, ymin, xmax, ymax)
        return xmin.value, ymin.value, xmax.value, ymax.value

    @property
    def extent(self):
        """
        View clip extent as a `geosoft.gxpy.geometry.Point2`.

        .. versionadded:: 9.3.1
        """

        cs = self.coordinate_system
        ex2d = self.extent_clip
        if self.is_crooked_path:
            min_x, min_y, max_x, max_y = self.crooked_path().extent_xy
            min_z = cs.xyz_from_oriented((ex2d[0], ex2d[1], 0.0))[2]
            max_z = cs.xyz_from_oriented((ex2d[0], ex2d[3], 0.0))[2]

        else:
            xyz0 = cs.xyz_from_oriented((ex2d[0], ex2d[1], 0.0))
            xyz1 = cs.xyz_from_oriented((ex2d[2], ex2d[1], 0.0))
            xyz2 = cs.xyz_from_oriented((ex2d[2], ex2d[3], 0.0))
            xyz3 = cs.xyz_from_oriented((ex2d[0], ex2d[3], 0.0))

            min_x = min(xyz0[0], xyz1[0], xyz2[0], xyz3[0])
            min_y = min(xyz0[1], xyz1[1], xyz2[1], xyz3[1])
            min_z = min(xyz0[2], xyz1[2], xyz2[2], xyz3[2])
            max_x = max(xyz0[0], xyz1[0], xyz2[0], xyz3[0])
            max_y = max(xyz0[1], xyz1[1], xyz2[1], xyz3[1])
            max_z = max(xyz0[2], xyz1[2], xyz2[2], xyz3[2])

        return gxgeo.Point2(((min_x, min_y, min_z), (max_x, max_y, max_z)), self.coordinate_system)

    @property
    def extent_clip(self):
        """clip extent of the view as (x_min, y_min, x_max, y_max)"""
        return self._extent(gxapi.MVIEW_EXTENT_CLIP)

    @property
    def extent_all(self):
        """extent of all groups in the view as (x_min, y_min, x_max, y_max)"""
        return self._extent(gxapi.MVIEW_EXTENT_ALL)

    @property
    def extent_visible(self):
        """extent of visible groups in the view as (x_min, y_min, x_max, y_max)"""
        return self._extent(gxapi.MVIEW_EXTENT_VISIBLE)

    def extent_map_cm(self, extent=None):
        """
        Return an extent in map cm.

        :param extent: tuple returned from one of the extent properties.  Default is :attr:`extent_clip`.

        .. versionadded:: 9.2
        """

        if extent is None:
            extent = self.extent_clip

        xmin, ymin = self.view_to_map_cm(extent[0], extent[1])
        xmax, ymax = self.view_to_map_cm(extent[2], extent[3])
        return xmin, ymin, xmax, ymax

    @property
    def scale(self):
        """map scale for the view"""
        return 1000.0 * self.gxview.scale_mm() * self.coordinate_system.metres_per_unit

    @property
    def aspect(self):
        """view aspect ratio, usually 1."""
        return self.gxview.scale_ymm() / self.gxview.scale_mm()

    def extent_group(self, group, unit=UNIT_VIEW):
        """
        Extent of a group

        :param group:   group name
        :param unit:    units:

                        ::

                            UNIT_VIEW
                            UNIT_MAP

        :returns: extent as (x_min, y_min, x_max, y_max)

        .. versionadded: 9.2
        """
        xmin = gxapi.float_ref()
        ymin = gxapi.float_ref()
        xmax = gxapi.float_ref()
        ymax = gxapi.float_ref()
        self.gxview.get_group_extent(group, xmin, ymin, xmax, ymax, unit)
        if unit == UNIT_MAP:
            xmin.value *= 0.1
            xmax.value *= 0.1
            ymin.value *= 0.1
            ymax.value *= 0.1
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

        :param x:   x, or a tuple (x,y), in map cm
        :param y:   y if x is not a tuple

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

        :param x:   x, or a tuple (x,y), in view units
        :param y:   y if x is not a tuple

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
            'Section'   a section view

        Other class names may be defined, though they are not used by Geosoft.

        :returns: name associated with the class, '' if not defined.

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
            'Section'   a section view


        .. versionadded:: 9.2
        """
        self.gxview.set_class_name(view_class, name)


class View_3d(View):
    """
    Geosoft 3D views, which contain 3D drawing groups.

    Geosoft 3D views are stored in a file with extension `.geosoft_3dv`.  A 3d view is required
    to draw 3D elements using :class:`geosoft.gxpy.group.Draw_3d`, which must be created from a
    :class:`geosoft.gxpy.view.View_3d` instance.

    3D views also contain 2D drawing planes on which :class:`geosoft.gxpy.group.Draw` groups are placed.
    A default horizontal plane at elevation 0, named 'plane_0' is created when a new 3d view is created.

    Planes are horizontal and flat by default, but can be provided a grid that defines the plane surface relief,
    which is intended for creating things like terrain surfaces on which 2d graphics are rendered.

    Planes can also be oriented within the 3D space to create sections, or for other more esoteric
    purposes.

    :Constructors:

        ============ =============================
        :meth:`open` open an existing geosoft_3dv
        :meth:`new`  create a new geosoft_3dv
        ============ =============================

    .. versionadded:: 9.2
    """

    def __init__(self, file_name, mode, _internal=False,
                 map=None, gxmview=None, **kwargs):

        if not _internal:
            raise ViewException(_t("Must be called by a class constructor 'open' or 'new' or 'from_gxapi'"))

        if map and gxmview:
            super().__init__(map, gxmview=gxmview, **kwargs)
        else:
            file_name = geosoft.gxpy.map.map_file_name(file_name, 'geosoft_3dv')
            map = geosoft.gxpy.map.Map(file_name=file_name,
                                       mode=mode,
                                       _internal=True)
            super().__init__(map, '3D', **kwargs)
        self._extent3d = None

    def _extent_union(self, extent):
        """Expand the extent"""
        if self._extent is None:
            self._extent = gxgeo.Point2(extent, self.coordinate_system)
        else:
            self._extent = self._extent.union(extent)

    @classmethod
    def from_gxapi(cls, gxmap, gxmview):
        """
        Instantiate View_3d from gxapi instance.

        :param gxmap:      a gxapi.CGXMAP
        :param gxmview:    a gxapi.CGXMVIEW

        .. versionadded:: 9.9
        """
        return cls(file_name=None, mode=WRITE_OLD, _internal=True,
                   map=geosoft.gxpy.map.Map.from_gxapi(gxmap), gxmview=gxmview)

    @classmethod
    def new(cls, file_name=None, area_2d=None, overwrite=False, **kwargs):
        """
        Create a new 3D view.

        :param file_name:   name for the new 3D view file (.geosoft_3dv added).  If not specified a
                            unique temporary file is created.
        :param area_2d:     2D drawing extent for the default 2D drawing plane
        :param overwrite:   True to overwrite an existing 3DV

        .. versionadded:: 9.2
        """

        if file_name is None:
            file_name = gx.gx().temp_file('.geosoft_3dv')
        else:
            file_name = geosoft.gxpy.map.map_file_name(file_name, 'geosoft_3dv')

        if not overwrite:
            if os.path.isfile(file_name):
                raise ViewException(_t('Cannot overwrite existing file: {}').format(file_name))

        g_3dv = cls(file_name, geosoft.gxpy.map.WRITE_NEW, area=area_2d, _internal=True, **kwargs)

        map_minx, map_miny, map_maxx, map_maxy = g_3dv.extent_map_cm(g_3dv.extent_clip)
        view_minx, view_miny, view_maxx, view_maxy = g_3dv.extent_clip

        # make this a 3D view
        h3dn = gxapi.GX3DN.create()
        g_3dv.gxview.set_3dn(h3dn)
        g_3dv.gxview.fit_map_window_3d(map_minx, map_miny, map_maxx, map_maxy,
                                       view_minx, view_miny, view_maxx, view_maxy)

        return g_3dv

    @classmethod
    def open(cls, file_name, **kw):
        """
        Open an existing geosoft_3dv file.

        :param file_name: name of the geosoft_3dv file

        .. versionadded:: 9.2
        """

        file_name = geosoft.gxpy.map.map_file_name(file_name, 'geosoft_3dv')
        if not os.path.isfile(file_name):
            raise ViewException(_t('geosoft_3dv file not found: {}').format(file_name))

        g_3dv = cls(file_name, geosoft.gxpy.map.WRITE_OLD, _internal=True)

        # read extents from the metadata
        try:
            g_3dv.add_extent(gxspd.extent_from_metadata(g_3dv.metadata))
        except KeyError:
            pass

        return g_3dv

    def __exit__(self, xtype, xvalue, xtraceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, 'close'):
            self.close()

    def close(self):
        """close the view, releases resources."""
        if hasattr(self, 'map'):
            if self.map:
                self.map.close()
        if hasattr(self, '_close'):
            self._close()

    def add_extent(self, extent):
        """
        Expand current extent to include this extent.
        :param extent:  extent as a `geosoft.gxpy.geometry.Geometry` or Point2 constructor

        TODO: review once issue #75 is resolved.

        .. versionadded:: 9.3.1
        """
        self._extent3d = gxgeo.extent_union(self._extent3d, extent)

    @property
    def extent(self):
        """
        Extent of 3D objects in this view.

        :return:    `geosoft.gxpy.geometry.Point2` instance

        TODO: review once issue #75 is resolved.

        .. versionadded:: 9.3.1
        """
        return self._extent3d

    @property
    def file_name(self):
        """ the `geosoft_3dv` file name"""
        return self.map.file_name

    @property
    def name(self):
        """the view name"""
        return self.map.name

    @property
    def current_3d_drawing_plane(self):
        """Current drawing plane name in a 3D view, `None` if not defined.  Can be set to a plane number or name."""
        if len(self.plane_list):
            s = gxapi.str_ref()
            self.gxview.get_def_plane(s)
            return s.value
        else:
            return None

    @current_3d_drawing_plane.setter
    def current_3d_drawing_plane(self, plane):
        if plane:
            if isinstance(plane, int):
                plane = self.plane_name(plane)
            if plane not in self.plane_list:
                self.new_drawing_plane(plane)
            self.gxview.set_def_plane(plane)

    @property
    def current_3d_drawing_plane_number(self):
        """The current drawing plane number, can be set."""
        return self.plane_number(self.current_3d_drawing_plane)

    @current_3d_drawing_plane_number.setter
    def current_3d_drawing_plane_number(self, plane):
        self.current_3d_drawing_plane = plane

    @property
    def plane_list(self):
        """list of drawing planes in the view"""
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
        if plane:
            if isinstance(plane, int):
                self.plane_name(plane)
                return plane
            plane_number = self.gxview.find_plane(plane)
            if plane_number == -1:
                _plane_err(plane, self.name)
            else:
                return plane_number
        else:
            return None

    def delete_plane(self, plane):
        """
        Delete a plane, and all content

        :param plane: plane number or plane name

        .. versionadded:: 9.3.1
        """
        if isinstance(plane, str):
            plane = self.plane_number(plane)
        try:
            self.gxview.delete_plane(plane, True)
        except gxapi.GXError:
            pass

    def has_plane(self, plane):
        """
        True if the view contains plane

        :param plane: name of the plane
        :returns: True if the plane exists in the view

        .. versionadded:: 9.2
        """
        try:
            self.plane_number(plane)
            return True
        except ViewException:
            return False

    def groups_on_plane_list(self, plane=0):
        """
        List of groups on a plane.

        :param plane: name of the plane or plane number
        :returns: list of groups on the plane

        .. versionadded:: 9.2
        """
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
        """
        Create a new drawing plane in a 3d view.

        :param name:        name of the plane, overwritten if it exists
        :param rotation:    plane rotation as (rx, ry, rz), default (0, 0, 0)
        :param offset:      (x, y, z) offset of the plane, default (0, 0, 0)
        :param scale:       (xs, ys, zs) axis scaling, default (1, 1, 1)

        .. versionadded::9.2
        """
        if self.has_plane(name):
            raise ViewException(_t('3D drawing plane "{}" exists.'.format(name)))

        self.gxview.create_plane(str(name))
        self.gxview.set_plane_equation(self.plane_number(name),
                                       rotation[0], rotation[1], rotation[2],
                                       offset[0], offset[1], offset[2],
                                       scale[0], scale[1], scale[2])



    def get_plane_relief_surface_info(self, plane):
        """
        Get relief surface parameters for a plane.

        :param plane:   plane number or plane name
        :returns:       relief surface properties
        :rtype:         :class:`geosoft.gxpy.view.PlaneReliefSurfaceInfo`

                .. versionadded::9.2
        """

        if isinstance(plane, str):
            plane = self.plane_number(plane)

        surface_grid_name = gxapi.str_ref()
        sample = gxapi.int_ref()
        base = gxapi.float_ref()
        scale = gxapi.float_ref()
        min_ref = gxapi.float_ref()
        max_ref = gxapi.float_ref()
        self.gxview.get_plane_surface(plane, surface_grid_name)
        self.gxview.get_plane_surf_info(plane, sample, base, scale, min_ref, max_ref)

        refine = 1 + int(sample.value / 16)

        min_val = None if min_ref.value == gxapi.rDUMMY else min_ref.value
        max_val = None if max_ref.value == gxapi.rDUMMY else max_ref.value

        return PlaneReliefSurfaceInfo(surface_grid_name.value, refine,
                                      base.value, scale.value, min_val, max_val)


    def set_plane_relief_surface(self, surface_grid_name, refine=3, base=0, scale=1, min=None, max=None):
        """
        Establish a relief surface for the current plane based on a grid.

        :param surface_grid_name:   grid file name
        :param refine:              relief refinement between 1 (low) and 4 (high). Default is 3.
        :param base:                base value in grid, will be at z=0.  Default is 0.
        :param scale:               scale to apply to grid after removing base, default is 1.
        :param min:                 minimum clip in unscaled grid values
        :param max:                 maximum clip in unscaled grid values

        .. versionadded:: 9.3
        """

        if not self.current_3d_drawing_plane:
            name = os.path.basename(surface_grid_name).split('.')[0]
            self.current_3d_drawing_plane = name

        self.gxview.set_plane_surface(self.current_3d_drawing_plane_number, surface_grid_name)
        if min is None:
            min = gxapi.rDUMMY
        if max is None:
            max = gxapi.rDUMMY
        refine = int(refine)
        if refine <= 1:
            refine = 1
        elif refine >= 4:
            refine = 48
        else:
            refine = (refine - 1) * 16
        self.gxview.set_plane_surf_info(self.current_3d_drawing_plane_number, refine, base, scale, min, max)
