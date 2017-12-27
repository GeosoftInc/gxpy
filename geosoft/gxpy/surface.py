"""
Geosoft surface dataset.  A surface dataset contains one or more 3D surfaces, each defined by a mesh
of triangular facets.

:Classes:

    ============ ==========================================================================
    `GeoSurface` Geosoft geosurface, subclass of `geosoft.gxpy.spatialdata.SpatialData`
    ============ ==========================================================================

.. seealso:: `geosoft.gxpy.spatialdata`, `geosoft.gxapi.GXSURFACE`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_surface.py>`_
    
"""
import os

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import coordinate_system as gxcs
from . import utility as gxu
from . import spatialdata as gxspd

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
    Delete all files associated with this surface name.

    :param surface_name: name of the surface file

    .. versionadded:: 9.3.1
    """
    gxspd.delete_files(surface_name)


# constants
MODE_READ = gxspd.MODE_READ             #:
MODE_READWRITE = gxspd.MODE_READWRITE   #: file exists, but can change properties
MODE_NEW = gxspd.MODE_NEW               #:


class SurfaceDataset(gxspd.SpatialData):
    """
    Surface dataset class.

    A Surface dataset contains one or more `Surface` items, which are stored in a .geosoft_surface file.

    :Constructors:

        ======================= ============================================
        :meth:`open`            open an existing surface dataset
        :meth:`new`             create a new surface dataset
        ======================= ============================================

    .. versionadded:: 9.3.1
    """

    def _close(self, pop=True):

        if hasattr(self, '_open'):
            if self._open:

                self._gxsurface = None
                super(SurfaceDataset, self)._close(pop=pop)

    def __init__(self, name=None, gxsurface=None, mode=None, overwrite=False, persist=True):

        self._file_name = _surface_file_name(name)
        self._name = _surface_name(self._file_name)

        super().__init__(name=self._name, file_name=self._file_name,
                         mode=mode,
                         overwrite=overwrite,
                         persist=persist,
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
        return self._surfaces(item)

    @classmethod
    def open(cls, name, gxapi_surface=None, mode=MODE_READ):
        """
        Open an existing surface dataset.

        :param name:        name of the surface dataset. If a name only the surface is resolved from the
                            project. If a file name or complete path, the surface is resolved from
                            the file system outside of the current project.
        :param gxapi_surface:   `gxapi.GXSURFACE` instance.
        :param mode:        open mode:

            =================  ======================================================================
            MODE_READ          only read the surface dataset, properties cannot be changed
            MODE_READWRITE     surface dataset stays the same, but properties and metadata may change
            =================  ======================================================================

        .. versionadded:: 9.3.1
        """

        if gxapi_surface is None:
            gxapi_surface = gxapi.GXSURFACE.open(_surface_file_name(name), mode)
        surface_dataset = cls(name, gxapi_surface, mode=mode)

        return surface_dataset

    @classmethod
    def new(cls, name, temp=False, overwrite=False, coordinate_system=None):
        """
        Create a new surface dataset

        :param name:        dataset name, or a path to a persistent file. A file with extension `.geosoft_surface`
                            will be created for surface instances that will persist (`temp=True`).
        :param temp:        True to create a temporary surface dataset which will be removed after use
        :param overwrite:   True to overwrite existing persistent surface dataset file
        :param coordinate_system:   coordinate system as required to create from `geosoft.gxpy.Coordinate_system`

        .. versionadded:: 9.3.1
        """

        if not temp:
            file_name = _surface_file_name(name)
            if not overwrite:
                if os.path.isfile(file_name):
                    raise SurfaceException(_t('Cannot overwrite existing surface dataset {}'.format(file_name)))
        else:
            file_name = gx.GXpy().temp_file('.geosoft_surface')

        gxsurface = gxapi.GXSURFACE.create(file_name, gxcs.Coordinate_system(coordinate_system).gxipj)
        surface_dataset = cls(name, gxsurface, mode=MODE_NEW, overwrite=overwrite, persist=(not temp))

        return surface_dataset

    def _refresh_surfaces(self):
        if self._surfaces is None:
            gxlst = gxapi.GXLST.create(1024)
            self.gxsurface.get_surface_items(gxlst)
            self._surfaces = gxu.dict_from_lst(gxlst, ordered=True)

    @property
    def gxsurface(self):
        """`gxapi.GXSURFACE` instance handle"""
        return self._gxsurface

    @property
    def extent(self):
        """ (min_x, min_y, min_z, max_x, max_y, max_z) extent to the outer-cell edges of the surface."""
        rx0 = gxapi.float_ref()
        ry0 = gxapi.float_ref()
        rz0 = gxapi.float_ref()
        rx1 = gxapi.float_ref()
        ry1 = gxapi.float_ref()
        rz1 = gxapi.float_ref()
        self.gxsurface.get_extents(rx0, ry0, rz0, rx1, ry1, rz1)
        return (rx0.value, ry0.value, rz0.value,
                rx1.value, ry1.value, rz1.value)

    @property
    def surface_dict(self):
        self._refresh_surfaces()
        return self._surfaces

    @property
    def surface_names(self):
        return list(self.surface_dict.values())

    @property
    def surface_id(self):
        return list(self.surface_dict.keys())

    @property
    def surface_count(self):
        return len(self.surface_dict)
