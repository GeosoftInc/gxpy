"""
Geosoft surface dataset.  A surface dataset contains one or more 3D surfaces, each defined by a mesh
of triangular facets.

:Classes:

    ================ ====================================================================
    `SurfaceDataset` Geosoft_surface dataset, contains zero or more `Surface` instances
    `Surface`        Surfaces, which are a set of triangles
    ================ ====================================================================

.. seealso:: `geosoft.gxpy.spatialdata`, `geosoft.gxapi.GXSURFACE`, `geosoft.gxapi.GXSURFACEITEM`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_surface.py>`_
    
"""
import os
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import coordinate_system as gxcs
from . import utility as gxu
from . import spatialdata as gxspd
from . import view as gxview
from . import group as gxgrp
from . import vox as gxvox
from . import vv as gxvv

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class SurfaceException(Exception):
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

RENDER_STYLE_SMOOTH = gxapi.SURFACERENDER_SMOOTH    #:
RENDER_STYLE_FILL = gxapi.SURFACERENDER_FILL        #:
RENDER_STYLE_EDGES = gxapi.SURFACERENDER_EDGES      #:


class SurfaceDataset(gxspd.SpatialData):
    """
    Surface dataset class.

    A Surface dataset is stored in a .geosoft_surface file and contains one or more `Surface` instances.

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

    def __init__(self, name, file_name=None, gxsurface=None, mode=None, overwrite=False):

        if file_name is None:
            file_name = _surface_file_name(name)
        self._file_name = file_name
        self._name = _surface_name(name)

        super().__init__(name=self._name, file_name=self._file_name,
                         mode=mode,
                         overwrite=overwrite,
                         gxobject=gxsurface)

        self._gxsurface = gxsurface
        self._next = 0
        self._surfaces = None

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
            item = self.surface_guid[item]
        gxsurfaceitem = self._gxsurface.get_surface_item(item)
        return Surface(gxsurfaceitem, surface_dataset=self)

    def __len__(self):
        return self.surface_count

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

        return surface_dataset

    @classmethod
    def new(cls, name, temp=False, overwrite=False, coordinate_system=None):
        """
        Create a new surface dataset.

        :param name:        dataset name, or a path to a persistent file.
        :param temp:        True to create a temporary surface dataset.
        :param overwrite:   True to overwrite existing persistent surface dataset file
        :param coordinate_system:   coordinate system as required to create from `geosoft.gxpy.Coordinate_system`

        .. versionadded:: 9.3.1
        """

        if temp:
            file_name = gx.GXpy().temp_file('.geosoft_surface')
            overwrite = True
        else:
            file_name = _surface_file_name(name)

        gxsurface = gxapi.GXSURFACE.create(file_name, gxcs.Coordinate_system(coordinate_system).gxipj)
        surface_dataset = cls(name,
                              file_name=file_name,
                              gxsurface=gxsurface,
                              mode=MODE_NEW,
                              overwrite=overwrite)

        return surface_dataset

    @classmethod
    def vox_surface(cls, vox, surfaces, name=None, file_name=None,
                    color=None, transparency=None,
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
        :param transparency:    transparency 0 t0 1. (1. is opaque), or a list of transparencies.
                                For a list of surfaces default transparency is applied in increasingly
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
            file_name = gx.GXpy().temp_file('.geosoft_surface')
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
            color = (gxgrp.C_GREY,
                     gxgrp.C_GREEN,
                     gxgrp.C_YELLOW,
                     gxgrp.C_BLUE,
                     gxgrp.C_MAGENTA,
                     gxgrp.C_RED,
                     gxgrp.C_CYAN)
        elif not hasattr(color, '__iter__'):
            color = (color,)
    
        if transparency is None:
            transparency = []
            max_transparent_surfaces = min(gxgrp.MAX_TRANSPARENT, len(surfaces))
            for i in range(max_transparent_surfaces):
                transparency.append((i + 1) * (1. / max_transparent_surfaces))
        elif not hasattr(transparency, '__iter__'):
            transparency = (transparency,)
    
        transparent_count = 0  # cannot have more than MAX_TRANSPARENT transparent surfaces
        with gxview.View_3d.new() as v3d:
            v3d_file = v3d.file_name
            for i in range(len(surfaces)):

                icolor = gxgrp.Color(color[i % len(color)])
                trans = transparency[min(i, len(transparency) - 1)]
                if trans < 1.:
                    if transparent_count > gxgrp.MAX_TRANSPARENT:
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
    def gxsurface(self):
        """`geosoft.gxapi.GXSURFACE` instance handle"""
        return self._gxsurface

    @property
    def surface_dict(self):
        """dictionary of surfaces keyed by GUID, values are the surface names"""
        self._refresh_surfaces()
        return self._surfaces

    @property
    def surface_names(self):
        """list of surface names"""
        return list(self.surface_dict.values())

    @property
    def surface_guid(self):
        """list of surface GUID"""
        return list(self.surface_dict.keys())

    @property
    def surface_count(self):
        """number of surfaces in the dataset"""
        return len(self.surface_dict)

    def add_surface(self, surface):
        """
        Add a surface to the surface dataset

        :param surface: `Surface` instance to add

        .. versionadded:: 9.3.1
        """

        if surface.coordinate_system.is_known:
            if not self.coordinate_system.is_known:
                self.coordinate_system = surface.coordinate_system
            elif surface.coordinate_system != self.coordinate_system:
                raise SurfaceException('Coordinate systems are not the same.')
        self._gxsurface.add_surface_item(surface.gxsurfaceitem)


class Surface(gxspd.SpatialData):
    """
    A single surface contained in a surface dataset.

    :param surface:         surface name or a `geosoft.gxapi.GXSURFACEITEM` instance
    :param surface_type:    surface type as a descriptive name, such as "ISOSURFACE"
    :param surface_dataset: optional `SurfaceDataset` instance in which to place a new `Surface`

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

                if self._add and self._surface_dataset:
                    self._surface_dataset.add_surface(self)

                self._gxsurfaceitem = None
                self._surface_dataset = None
                self._properties = None
                self._computed_properties = None
                self._cs = None
                super(Surface, self)._close()

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return str((self.guid, self.name, self.surface_type))

    def __init__(self, surface, surface_type='none', surface_dataset=None):

        self._add = False
        if isinstance(surface, str):
            if surface_dataset:
                self._add = True
            surface = gxapi.GXSURFACEITEM.create(surface_type, surface)

        self._gxsurfaceitem = surface
        self._surface_dataset = surface_dataset
        self._properties = None
        self._computed_properties = None
        self._cs = None

        super().__init__(gxobject=self._gxsurfaceitem)

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
    def compontent_count(self):
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
    def triangles_count(self):
        """number of triangular facets"""
        vert = gxapi.int_ref()
        tri = gxapi.int_ref()
        self._gxsurfaceitem.get_geometry_info(vert, tri)
        return tri.value

    @property
    def render_color(self):
        """rendering colour as a `geosoft.gxpy.group.Color` instance"""
        color = gxapi.int_ref()
        trans = gxapi.float_ref()
        style = gxapi.int_ref()
        self._gxsurfaceitem.get_default_render_properties(color, trans, style)
        return gxgrp.Color(color.value)

    @property
    def render_transparency(self):
        """group transparency, 0.0 (transparent) to 1.0 (opaque)"""
        color = gxapi.int_ref()
        trans = gxapi.float_ref()
        style = gxapi.int_ref()
        self._gxsurfaceitem.get_default_render_properties(color, trans, style)
        return trans.value

    @property
    def render_style(self):
        """surface rendering style, one of RENDER_STYLE constants"""
        color = gxapi.int_ref()
        trans = gxapi.float_ref()
        style = gxapi.int_ref()
        self._gxsurfaceitem.get_default_render_properties(color, trans, style)
        return style.value

    @property
    def coordinate_system(self):
        """
        `geosoft.gxpy.coordinate_system.Coordinate_system` instance of the surface.

        Can be set using any constructor supported by `geosoft.gxpy.coordinate_system.Coordinate_system`.
        """

        if self._surface_dataset:
            return self._surface_dataset.coordinate_system
        if self._cs is None:
            self._cs = gxcs.Coordinate_system()
        return self._cs

    @coordinate_system.setter
    def coordinate_system(self, cs):
        if not isinstance(cs, gxcs.Coordinate_system):
            cs = gxcs.Coordinate_system(cs)
        self._cs = cs

    @property
    def metadata(self):
        """Return the parent surface dataset metadata as a dictionary."""
        if self._surface_dataset:
            return self._surface_dataset.metadata
        else:
            return {}

    def get_mesh_vv(self, component=0):
        """
        Returns mesh data as a set of VV.

        :param component: component number from a multi-component surface
        :return: vertex_x, vertex_y, vertex_z, triangle_point_1, triangle_point_2, triangle_point_3

        .. versionadded:: 9.3.1
        """

        vx = gxvv.GXvv()
        vy = gxvv.GXvv()
        vz = gxvv.GXvv()
        t1 = gxvv.GXvv(dtype=np.int)
        t2 = gxvv.GXvv(dtype=np.int)
        t3 = gxvv.GXvv(dtype=np.int)
        self._gxsurfaceitem.get_mesh(component,
                                     vx.gxvv, vy.gxvv, vz.gxvv,
                                     t1.gxvv, t2.gxvv, t3.gxvv)
        return vx, vy, vz, t1, t2, t3

    def get_mesh_np(self, component=0):
        """
        Returns mesh data as a set of numpy arrays.

        :param component: component number from a multi-component surface
        :return: vertex_x, vertex_y, vertex_z, triangle_point_1, triangle_point_2, triangle_point_3

        .. versionadded:: 9.3.1
        """

        vx, vy, vz, t1, t2, t3 = self.get_mesh_vv(component)
        return vx.np, vy.np, vz.np, t1.np, t2.np, t3.np
