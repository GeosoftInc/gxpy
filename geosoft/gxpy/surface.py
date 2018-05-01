"""
Geosoft surfaces

:Classes:

    ================ ====================================================================
    `SurfaceDataset` Geosoft_surface dataset, contains zero or more `Surface` instances
    `Surface`        Surfaces defined by one or more `geosoft.geometry.Mesh` instances
    ================ ====================================================================

.. seealso:: `geosoft.gxpy.spatialdata`, `geosoft.gxapi.GXSURFACE`, `geosoft.gxapi.GXSURFACEITEM`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_surface.py>`_
    
"""
import os
import numpy as np
from collections.abc import Sequence

import geosoft
import geosoft.gxapi as gxapi
from . import gx
from . import coordinate_system as gxcs
from . import utility as gxu
from . import spatialdata as gxspd
from . import view as gxview
from . import vox as gxvox
from . import vv as gxvv
from . import group as gxg
from . import map as gxmap
from . import geometry as gxgm

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class SurfaceException(geosoft.GXRuntimeError):
    """
    Exceptions from :mod:`geosoft.gxpy.surface`.
    """
    pass


def _surface_file_name(name):
    ext = os.path.splitext(name)[1].lower()
    if ext == '.geosoft_surface':
        return name
    return name + '.geosoft_surface'


def _surface_name(name):
    basename = os.path.basename(name)
    return os.path.splitext(basename)[0]


def delete_files(surface_name):
    """
    Delete all files associated with this surface dataset.

    :param surface_name: name of the surface dataset file

    .. versionadded:: 9.3.1
    """
    gxspd.delete_files(_surface_file_name(surface_name))


# constants
MODE_READ = gxspd.MODE_READ             #:
MODE_READWRITE = gxspd.MODE_READWRITE   #: file exists, but can change properties
MODE_NEW = gxspd.MODE_NEW               #:
MODE_APPEND = MODE_READWRITE            #: append to existing surface dataset

STYLE_FLAT = gxapi.SURFACERENDER_FILL  #:
STYLE_SMOOTH = gxapi.SURFACERENDER_SMOOTH   #:
STYLE_EDGE = gxapi.SURFACERENDER_EDGES  #:


class SurfaceDataset(gxspd.SpatialData, Sequence):
    """
    Surface dataset, which contains one or more `Surface` instances.

    A Surface dataset is stored in a .geosoft_surface file.

    Iterating yields `Surface` instances.

    :Constructors:

        ======================= ============================================
        :meth:`open`            open an existing surface dataset
        :meth:`new`             create a new surface dataset
        :meth:`vox_surface`     isosurfaces created from a vox.
        ======================= ============================================

    .. versionadded:: 9.3.1
    """

    def _close(self):

        if hasattr(self, '_open'):
            if self._open:

                self._gxsurface = None
                self._surfaces = None
                super(SurfaceDataset, self)._close()
                pass

    def __init__(self, name, file_name=None, gxsurface=None, mode=None, overwrite=False):

        if file_name is None:
            file_name = _surface_file_name(name)
        self._file_name = file_name
        self._name = _surface_name(name)

        super().__init__(name=self._name, file_name=self._file_name,
                         mode=mode,
                         overwrite=overwrite,
                         gxobj=gxsurface)

        self._gxsurface = gxsurface
        self._next = 0
        self._surfaces = None
        self._new = False

    def __len__(self):
        return self.surface_count

    def __iter__(self):
        self._refresh_surfaces()
        return self

    def __next__(self):
        if self._next >= self.surface_count:
            self._next = 0
            raise StopIteration
        else:
            surface = self.__getitem__(self._next)
            self._next += 1
            return surface

    def __getitem__(self, item):
        if isinstance(item, int):
            item = self.surface_name_list[item]
        gxsurfaceitem = self._gxsurface.get_surface_item(self.surface_guid(item))
        return Surface(gxsurfaceitem, surface_dataset=self, render_properties=None)

    @classmethod
    def open(cls, name, file_name=None, mode=MODE_READ, gxapi_surface=None):
        """
        Open an existing surface dataset.

        :param name:            name of the surface dataset.
        :param file_name:       file name of the surface dataset file, default is name.geosoft_surface.
        :param mode:            open mode: MODE_READ or MODE_READWRITE
        :param gxapi_surface:   `geosoft.gxapi.GXSURFACE` instance, or None to open the named surface file.

        .. versionadded:: 9.3.1
        """

        if file_name is None:
            file_name = _surface_file_name(name)
        if gxapi_surface is None:
            gxapi_surface = gxapi.GXSURFACE.open(_surface_file_name(file_name), mode)

        surface_dataset = cls(name, file_name=file_name, gxsurface=gxapi_surface, mode=mode)
        surface_dataset._new = False

        return surface_dataset

    @classmethod
    def new(cls, name=None, temp=False, overwrite=False, coordinate_system=None):
        """
        Create a new surface dataset.

        :param name:        dataset name, or a path to a persistent file. If None a temporary dataset is created.
        :param temp:        True to create a temporary surface dataset.
        :param overwrite:   True to overwrite existing persistent surface dataset file
        :param coordinate_system:   coordinate system as required to create from `geosoft.gxpy.Coordinate_system`

        .. versionadded:: 9.3.1
        """

        if name is None:
            temp = True
        if temp:
            file_name = gx.gx().temp_file('.geosoft_surface')
            overwrite = True
            if name is None:
                name = _surface_name(file_name)
        else:
            file_name = _surface_file_name(name)

        if os.path.exists(file_name) and not overwrite:
            raise SurfaceException(_t('\'{}\' exists. Use overwrite=True to overwrite existing surface dataset file.').
                                   format(file_name))

        gxsurface = gxapi.GXSURFACE.create(file_name, gxcs.Coordinate_system(coordinate_system).gxipj)
        surface_dataset = cls(name,
                              file_name=file_name,
                              gxsurface=gxsurface,
                              mode=MODE_NEW)
        surface_dataset._new = True

        return surface_dataset

    @classmethod
    def vox_surface(cls, vox, surfaces, name=None, file_name=None,
                    color=None, opacity=None,
                    mode=MODE_NEW, temp=False, overwrite=False):
        """
        Add voxel isosurfaces to a surface dataset.
    
        :param vox:             `geosoft.gxpy.Vox` instance
        :param surfaces:        surface value, or a list of surface values
        :param name:            Surface dataset name. The default will be vox.name.
        :param file_name:       optional file name if different from name root, ignored if temp=True
        :param color:           surface color, or a list of colors,
                                For a list of surfaces, the default colour of each surface cycles through a list of
                                (C_GREY, C_GREEN, C_YELLOW, C_BLUE, C_MAGENTA, C_RED, C_CYAN). If only one surface
                                the default color is `gxgroup.C_GREY`.
        :param opacity:         opacity 0 t0 1. (1. is opaque), or a list of opacities.
                                For a list of surfaces default opacity is applied in increasingly
                                opaque steps in the order of the surface list, such that the 5'th
                                and higher surfaces are opaque.
        :param mode:            MODE_NEW to create a new surface dataset. MODE_APPEND to append to existing dataset.
        :param temp:            True to create a temporary surface dataset.
        :param overwrite:       True to overwrite if dataset exists and MODE_NEW.

        .. versionadded:: 9.3.1
        """
    
        if name is None:
            name = vox.name
        if temp:
            file_name = gx.gx().temp_file('.geosoft_surface')
            overwrite = True
        elif file_name is None:
            file_name = _surface_file_name(name)
    
        if mode == MODE_NEW:
            if os.path.exists(file_name) and not overwrite:
                raise SurfaceException(_t("Cannot overwrite existing surface dataset: {}").format(file_name))
            gxspd.delete_files(file_name)

        if not hasattr(surfaces, '__iter__'):
            surfaces = (surfaces,)
    
        if color is None:
            color = (gxg.C_GREY,
                     gxg.C_GREEN,
                     gxg.C_YELLOW,
                     gxg.C_BLUE,
                     gxg.C_MAGENTA,
                     gxg.C_RED,
                     gxg.C_CYAN)
        elif not hasattr(color, '__iter__'):
            color = (color,)
    
        if opacity is None:
            opacity = []
            max_transparent_surfaces = min(gxg.MAX_TRANSPARENT, len(surfaces))
            for i in range(max_transparent_surfaces):
                opacity.append((i + 1) * (1. / max_transparent_surfaces))
        elif not hasattr(opacity, '__iter__'):
            opacity = (opacity,)
    
        transparent_count = 0  # cannot have more than MAX_TRANSPARENT transparent surfaces
        with gxview.View_3d.new() as v3d:
            v3d_file = v3d.file_name
            for i in range(len(surfaces)):

                icolor = gxg.Color(color[i % len(color)])
                trans = opacity[min(i, len(opacity) - 1)]
                if trans < 1.:
                    if transparent_count > gxg.MAX_TRANSPARENT:
                        trans = 1.
                    else:
                        transparent_count += 1

                gxapi.GXMVU.plot_voxel_surface2(v3d.gxview,
                                                vox.gxvox,
                                                surfaces[i],
                                                icolor.int_value,
                                                1.,
                                                trans,
                                                file_name)
        gxview.delete_files(v3d_file)
        sd = SurfaceDataset.open(name, file_name=file_name)
        sd.unit_of_measure = vox.unit_of_measure
        return sd

    def _refresh_surfaces(self):
        if self._surfaces is None:
            gxlst = gxapi.GXLST.create(1024)
            self.gxsurface.get_surface_items(gxlst)
            self._surfaces = gxu.dict_from_lst(gxlst, ordered=True)

    @property
    def is_new(self):
        """True if this is a new surface dataset. Can only add to new datasets."""
        return self._new

    @property
    def gxsurface(self):
        """`geosoft.gxapi.GXSURFACE` instance handle"""
        return self._gxsurface

    @property
    def surface_dict(self):
        """dictionary of surfaces keyed by GUID, values are the surface names"""
        self._refresh_surfaces()
        return self._surfaces

    @property
    def surface_name_list(self):
        """list of surface names"""
        return list(self.surface_dict.values())

    @property
    def surface_count(self):
        """number of surfaces in the dataset"""
        return len(self.surface_dict)

    def surface_guid(self, name):
        """
        Return the guid of a surface based on the name.

        :param name:    Name of the surface.  The first matching surface name is returned.
        :return:        guid of the surface, or None if the surface not found

        .. versionadded:: 9.3.1
        """

        # just return the name if it is already a guid
        if name in self.surface_dict:
            return name
        name = name.lower()
        for guid, sname in self.surface_dict.items():
            if sname.lower() == name:
                return guid
        return None

    def has_surface(self, name):
        """returns True if this surface name or guid exists in the surface dataset."""
        if self.surface_guid(name) is None:
            return False
        return True

    def add_surface(self, surface):
        """
        Add a surface to the surface dataset.  One can only add surfaces to new datasets.

        :param surface: `Surface` instance to add

        .. versionadded:: 9.3.1
        """
        if not self.is_new:
            raise SurfaceException(_t('Cannot add new surfaces to an existing surface dataset.'))

        if self.has_surface(surface.name):
            raise SurfaceException(_t('Cannot overwrite existing surface {}').format(surface.name))

        if surface.faces_count == 0:
            raise SurfaceException(_t('Cannot add an empty surface.'))

        if gxcs.is_known(surface.coordinate_system):
            if not gxcs.is_known(self.coordinate_system):
                self.coordinate_system = surface.coordinate_system
            elif surface.coordinate_system != self.coordinate_system:
                raise SurfaceException('Coordinate systems are not the same.')
        self._gxsurface.add_surface_item(surface.gxsurfaceitem)
        self._surfaces = None

    def add_surface_dataset(self, surface_dataset):
        """
        Add the surfaces from an existing surface dataset.

        :param surface_dataset: `SurfaceDataset` instance or a file name

        .. versionadded:: 9.3.1
        """

        if isinstance(surface_dataset, str):
            surface_dataset = SurfaceDataset.open(surface_dataset)
        for s in surface_dataset:
            self.add_surface(s)

    def view_3d(self, file_name=None, overwrite=True, plane_2d=False):
        """
        Create a 3d view (`geosoft.gxpy.view.View_3d`) that contains this `SurfaceDataset`.

        :param file_name:   the name of a file for the 3d view. If None a temporary 3d view created.
        :param overwrite:   True to overwrite existing file
        :param plane_2d:    True to keep the 2D plane.  Only keep it if you intend to draw on it otherwise a grey
                            plane will appear in the view.

        .. versionadded:: 9.3
        """

        v3d = gxview.View_3d.new(file_name, overwrite=overwrite)
        render(v3d, self)
        if not plane_2d:
            v3d.delete_plane(0)

        return v3d

    def figure_map(self, file_name=None, overwrite=True, title=None, legend_label=None,
                   features=('LEGEND', 'NEATLINE'), **kwargs):
        """
        Create a figure view file from an SurfaceDataset.

        :param file_name:       the name of a file for the 3d view. If None a temporary 3d view created.
        :param overwrite:       True to overwrite existing file
        :param title:           Title added to the image
        :param legend_label:    If plotting a legend make this the legend title.  The default is the unit_of_measure.
        :param features:        list of features to place on the map, default is ('SCALE', 'LEGEND', 'NEATLINE')

                                    =========== =========================================
                                    'LEGEND'    draw a surface legend
                                    'NEATLINE'  draw a neat-line around the image
                                    =========== =========================================

        :param kwargs:          passed to `geosoft.gxpy.map.Map.new`

        .. versionadded:: 9.3
        """

        # uppercase features, use a dict so we pop things we use and report error
        if isinstance(features, str):
            features = (features,)
        feature_list = {}
        if features is not None:
            for f in features:
                feature_list[f.upper()] = None
        features = list(feature_list.keys())

        # setup margins
        if not ('margins' in kwargs):

            bottom_margin = 1.0
            if title:
                bottom_margin += len(title.split('\n')) * 1.0

            right_margin = 1
            if 'LEGEND' in feature_list:
                right_margin += 4.0
            kwargs['margins'] = (1, right_margin, bottom_margin, 1)

        gmap = gxmap.Map.figure((0, 0, 100, 100),
                                file_name=file_name,
                                overwrite=overwrite,
                                features=features,
                                title=title,
                                **kwargs)

        with gxview.View.open(gmap, "data") as v:

            if 'LEGEND' in features:
                pass # TODO: draw a surface legend

        area = gxview.View.open(gmap, gmap.current_data_view).extent_map_cm()
        area = (area[0] * 10., area[1] * 10., area[2] * 10., area[3] * 10.)

        gmap.create_linked_3d_view(self.view_3d(), area_on_map=area)

        return gmap


class Surface(gxspd.SpatialData, Sequence):
    """
    A single surface, which contains one or more `geosoft.gxpy.geometry.Mesh` instances.

    :param surface:             surface name or a `geosoft.gxapi.GXSURFACEITEM` instance.
    :param surface_type:        surface type as a descriptive name, such as "ISOSURFACE"
    :param surface_dataset:     optional `SurfaceDataset` instance in which to place a new `Surface`
    :param mesh:                optional `geosoft.gxpy.geometry.Mesh` instance, or tuple (faces, verticies).
    :param coordinate_system:   mesh coordinate system, which will become the surface coordinate system.
    :param render_properties:   (color, opacity, style), default is
                                (`geosoft.gxpy.group.C_GREY`, 1.0, `STYLE_FLAT`)

    Iterating yields component `geosoft.gxpy.geometry.Mesh` instances.

    .. versionadded:: 9.3.1
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

                if self._add and self._surface_dataset is not None:
                    if gxcs.is_known(self._surface_dataset.coordinate_system):
                        self.coordinate_system = self._surface_dataset.coordinate_system
                    elif gxcs.is_known(self.coordinate_system):
                        self._surface_dataset.coordinate_system = self.coordinate_system
                    self._surface_dataset.add_surface(self)

                self._gxsurfaceitem = None
                self._surface_dataset = None
                self._cs = None
                super(Surface, self)._close()

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return str((self.guid, self.name, self.surface_type))

    def __init__(self, surface, surface_type='none', surface_dataset=None,
                 mesh=None, coordinate_system=None, render_properties=None):

        if isinstance(surface, str):
            if surface_dataset and surface_dataset.has_surface(surface):
                raise SurfaceException(_t('Cannot overwrite existing surface ({}) in dataset ({}).')
                                       .format(surface, surface_dataset.name))

            surface = gxapi.GXSURFACEITEM.create(surface_type, surface)
            self._new_surface = True
            self._add = True  # always add new surfaces
        else:
            self._new_surface = False
            self._add = False

        self._gxsurfaceitem = surface
        self._surface_dataset = surface_dataset
        self._properties = None
        self._computed_properties = None
        self._next = 0
        self.render_properties = render_properties

        super().__init__(gxobj=self._gxsurfaceitem)

        if coordinate_system is None and surface_dataset is not None:
            if gxcs.is_known(surface_dataset.coordinate_system):
                coordinate_system = surface_dataset.coordinate_system
        self.coordinate_system = coordinate_system
        self._extent = None
        if mesh:
            if not isinstance(mesh, gxgm.Mesh):
                mesh = gxgm.Mesh(mesh, name=self.name + '_0')
            self.add_mesh(mesh, render_properties=render_properties)
        elif self.faces_count:
            for m in self:
                self._update_extent(m.extent_xyz)

    def __len__(self):
        return self.component_count

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self.component_count:
            self._next = 0
            raise StopIteration
        else:
            item = self._next
            self._next += 1
            return self.__getitem__(item)

    def __getitem__(self, item):
        return self.mesh(item)

    def _update_extent(self, ext):
        if self._extent is None:
            self._extent = ext
        else:
            self._extent = (min(self._extent[0], ext[0]),
                            min(self._extent[1], ext[1]),
                            min(self._extent[2], ext[2]),
                            max(self._extent[3], ext[3]),
                            max(self._extent[4], ext[4]),
                            max(self._extent[5], ext[5]))

    def _get_mesh_vv(self, component=0):

        f1 = gxvv.GXvv(dtype=np.int)
        f2 = gxvv.GXvv(dtype=np.int)
        f3 = gxvv.GXvv(dtype=np.int)
        vx = gxvv.GXvv()
        vy = gxvv.GXvv()
        vz = gxvv.GXvv()
        self._gxsurfaceitem.get_mesh(component,
                                     vx.gxvv, vy.gxvv, vz.gxvv,
                                     f1.gxvv, f2.gxvv, f3.gxvv)
        return (f1, f2, f3), (vx, vy, vz)

    @property
    def extent(self):
        """
        Return the surface extent as a `geosoft.gxpy.geometry.Point2` instance.

        .. versionadded:: 9.3.1
        """
        pmin = gxgm.Point((self._extent[0], self._extent[1], self._extent[2]))
        pmax = gxgm.Point((self._extent[3], self._extent[4], self._extent[5]))
        return gxgm.Point2((pmin, pmax), self.coordinate_system)


    def properties(self, refresh=False):
        """
        Surface properties from `geosoft.gxapi.GXSURFACEITEM.get_properties_ex`.

        :param refresh: if True, computed properties will be refreshed on next access.

        .. versionadded:: 9.3.1
        """

        if refresh:
            self._properties = None

        if not self._properties:

            stype = gxapi.str_ref()
            name = gxapi.str_ref()
            source_guid = gxapi.str_ref()
            source_name = gxapi.str_ref()
            source_measure = gxapi.float_ref()
            second_source_guid = gxapi.str_ref()
            second_source_name = gxapi.str_ref()
            second_source_option = gxapi.int_ref()
            second_source_measure = gxapi.float_ref()
            second_source_measure2 = gxapi.float_ref()
            self._gxsurfaceitem.get_properties_ex(stype, name,
                                                  source_guid, source_name, source_measure,
                                                  second_source_guid, second_source_name, second_source_option,
                                                  second_source_measure, second_source_measure2)
            self._properties = {'type': stype.value,
                                'name': name.value,
                                'source_guid': source_guid.value,
                                'source_dataset': source_name.value,
                                'source_measure': source_measure.value,
                                'second_source_guid': second_source_guid.value,
                                'second_source_dataset': second_source_name.value,
                                'second_source_option': second_source_option.value,
                                'second_source_measure': second_source_measure.value,
                                'second_source_measure2': second_source_measure2.value}

        return self._properties

    def computed_properties(self, refresh=False):
        """
        Surface properties  by `geosoft.gxapi.GXSURFACEITEM.compute_extended_info`.

        :param refresh: if True, computed properties will be refreshed on next access.

        .. versionadded:: 9.3.1
        """

        if refresh:
            self._computed_properties = None

        if not self._computed_properties:

            comp = gxapi.int_ref()
            vert = gxapi.int_ref()
            edge = gxapi.int_ref()
            trng = gxapi.int_ref()
            incn = gxapi.int_ref()
            invd = gxapi.int_ref()
            intr = gxapi.int_ref()
            self._gxsurfaceitem.compute_extended_info(comp, vert, edge, trng, incn, invd, intr)
            self._computed_properties = {'components': comp.value,
                                         'verticies': vert.value,
                                         'edges': edge.value,
                                         'triangles': trng.value,
                                         'inconsistent': incn.value,
                                         'invalid': invd.value,
                                         'intersect': intr.value}

        return self._computed_properties

    @property
    def gxsurfaceitem(self):
        """the `geosoft.gxapi.GXSURFACEITEM` instance"""
        return self._gxsurfaceitem

    @property
    def guid(self):
        """The GUID of this surface"""
        guid = gxapi.str_ref()
        self._gxsurfaceitem.get_guid(guid)
        return guid.value

    @property
    def name(self):
        """the name of this surface"""
        return self.properties()['name']

    @property
    def surface_type(self):
        """the defined surface type string"""
        return self.properties()['type']

    @property
    def source_dataset(self):
        """the source dataset from which this surface was derived"""
        return self.properties()['source_dataset']

    @property
    def source_measure(self):
        """the source measure"""
        return self.properties()['source_measure']

    @property
    def unit_of_measure(self):
        """the unit of measure for data defined by this surface, often the isosurface value"""

        if self._surface_dataset:
            return self._surface_dataset.unit_of_measure

        source = self.properties()['source_name']
        if source:
            try:
                return gxvox.Vox.open(source).unit_of_measure
            except geosoft.gxapi.GXError:
                pass
        return ''

    @property
    def component_count(self):
        """number of components to this surface, usually 1"""
        return self._gxsurfaceitem.num_components()

    @property
    def verticies_count(self):
        """number of verticies"""
        vert = gxapi.int_ref()
        tri = gxapi.int_ref()
        self._gxsurfaceitem.get_geometry_info(vert, tri)
        return vert.value

    @property
    def faces_count(self):
        """number of triangular faces"""
        vert = gxapi.int_ref()
        tri = gxapi.int_ref()
        self._gxsurfaceitem.get_geometry_info(vert, tri)
        return tri.value

    @property
    def render_properties(self):
        """The rendering properties for this surface as (color, opacity, style). Can be set."""
        color = gxapi.int_ref()
        trans = gxapi.float_ref()
        style = gxapi.int_ref()
        self._gxsurfaceitem.get_default_render_properties(color, trans, style)
        return gxg.Color(color.value), trans.value, style.value

    @render_properties.setter
    def render_properties(self, props):
        if self._new_surface:
            if props is None:
                props = (gxg.C_GREY, 1.0, STYLE_FLAT)
            c, t, s = props
            if isinstance(c, gxg.Color):
                c = c.int_value
            self._gxsurfaceitem.set_default_render_properties(c, t, s)

    @property
    def render_color(self):
        """rendering colour as a `geosoft.gxpy.group.Color` instance"""
        return self.render_properties[0]

    @render_color.setter
    def render_color(self, c):
        _, t, s = self.render_properties
        self.render_properties = (c, t, s)

    @property
    def render_opacity(self):
        """group opacity, 0.0 (transparent) to 1.0 (opaque)"""
        return self.render_properties[1]

    @render_opacity.setter
    def render_opacity(self, t):
        c, _, s = self.render_properties
        self.render_properties = (c, t, s)

    @property
    def render_style(self):
        """surface rendering style, one of STYLE constants"""
        return self.render_properties[2]

    @render_style.setter
    def render_style(self, s):
        c, t, _ = self.render_properties
        self.render_properties = (c, t, s)

    @property
    def metadata(self):
        """Return the parent surface dataset metadata as a dictionary."""
        if self._surface_dataset:
            return self._surface_dataset.metadata
        else:
            return {}

    def mesh(self, component=0):
        """
        Returns a component mesh as `geosoft.gxpy.geometry.Mesh` instance

        :param component:   component number from a multi-component surface
        :return:            (triangle_index_1, triangle_index_2, triangle_index_3), (vertex_x, vertex_y, vertex_z)
                            as `geosoft.gxpy.vv.GXvv` instances

        .. versionadded:: 9.3.1
        """

        f1 = gxvv.GXvv(dtype=np.int)
        f2 = gxvv.GXvv(dtype=np.int)
        f3 = gxvv.GXvv(dtype=np.int)
        vx = gxvv.GXvv()
        vy = gxvv.GXvv()
        vz = gxvv.GXvv()
        self._gxsurfaceitem.get_mesh(component,
                                     vx.gxvv, vy.gxvv, vz.gxvv,
                                     f1.gxvv, f2.gxvv, f3.gxvv)
        return gxgm.Mesh(((f1, f2, f3), (vx, vy, vz)))

    def add_mesh(self, mesh, render_properties=None, coordinate_system=None):
        """
        Add a vv mesh to a new surface.

        :param mesh:        mesh as ((f1vv, f2vv, f3vv), (xvv, yvv, zvv))
        :param render_properties:  (color, opacity, style), where colour is a `geosoft.gxpy.group.Color`
                            instance or a 32-bit Geosoft color integer, opacity is a value between
                            0. (invisible) and 1. (opaque), and style is STYLE_FLAT, STYLE_SMOOTH or
                            STYLE_EDGE.
        :param coordinate_system: coordinate system for the verticies, default is the same as the surface
        :returns:           component number, which will always be the last component.

        .. versionadded:: 9.3
        """

        if not self._new_surface:
            raise SurfaceException(_t('Cannot add to an existing surface ({}) in surface dataset ({})')
                                   .format(self.name, self._surface_dataset.name))

        if not isinstance(mesh, gxgm.Mesh):
            mesh = gxgm.Mesh(mesh)
        f1vv, f2vv, f3vv = mesh.faces_vv()
        xvv, yvv, zvv = mesh.verticies_vv()

        if coordinate_system is None:
            coordinate_system = self.coordinate_system
        if self._surface_dataset is not None:
            required_cs = self._surface_dataset.coordinate_system
        else:
            required_cs = self.coordinate_system
        if coordinate_system != required_cs:
            gxcs.Coordinate_translate(coordinate_system, required_cs).convert_vv(xvv, yvv, zvv)

        self._gxsurfaceitem.add_mesh(xvv.gxvv, yvv.gxvv, zvv.gxvv,
                                     f1vv.gxvv, f2vv.gxvv, f3vv.gxvv)
        self._add = True

        # extent
        self._update_extent(mesh.extent_xyz)

        if render_properties:
            self.render_properties = render_properties

        return self.component_count - 1


def render(view, surface, group_name=None, overwrite=False):
    """
    Render a surface, surface dataset or surface dataset file in a 3D view.

    :param view:        `geosoft.view.View_3d` instance
    :param surface:     `Surface` instance, `SurfaceDataset` instance or a geosoft_surface file name.
    :param group_name:  name for the group, which defaults to the source name
    :param overwrite:   True to overwrite existing group

    .. note::
        For a `Surface` or a `SurfaceDataset` instance a surface dataset file is created with a name constructed
        from the view name and the fies name: *view_name.group_name.geosoft_surface*.

    .. versionadded:: 9.3.1
    """

    if group_name is None:
        if isinstance(surface, str):
            group_name = _surface_name(surface)
        else:
            group_name = surface.name

    if view.has_group(group_name) and not overwrite:
        raise SurfaceException(_t('Cannot overwerwrite existing group: {}').format(group_name))

    if not isinstance(surface, str):

        surface_dataset_file_name = _surface_file_name(view.file_name + '.' + surface.name)
        with SurfaceDataset.new(surface_dataset_file_name, overwrite=overwrite,
                                coordinate_system=view.coordinate_system) as new_sd:
            if isinstance(surface, Surface):
                surface = (surface, )
            for s in surface:
                new_sd.add_surface(s)

        surface = surface_dataset_file_name

    gxg.surface_group_from_file(view, surface, group_name=group_name, overwrite=overwrite)
