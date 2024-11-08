#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
"""
Geosoft vox display handling, which manages the rendering of a `geosoft.gxpy.vox.Vox` in a 3d view.

:Classes:
    :`VoxDisplay`: 3D visualization of a vox, which can be placed `geosoft.gxpy.view.View_3d`

:Constants:
    :ZONE_DEFAULT: 0
    :ZONE_LINEAR: 1
    :ZONE_NORMAL: 2
    :ZONE_EQUALAREA: 3
    :ZONE_SHADE: 4
    :ZONE_LOGLINEAR: 5
    :ZONE_LAST: 6
    :RENDER_FILL: 0
    :RENDER_EDGE: 1
    :RENDER_FILL_EDGE: 2
    :RENDER_SMOOTH: 3



.. seealso:: `geosoft.gxpy.vox.Vox`, `geosoft.gxpy.view.View_3d`, `geosoft.gxapi.GXVOXD`

.. note::

    Regression tests provide usage examples:
    `vox_display tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_vox_display.py>`_

.. versionadded:: 9.3.1
"""
import os

import geosoft
import geosoft.gxapi as gxapi
from . import gx
from . import view as gxview
from . import group as gxgroup
from . import vox as gxvox
from . import map as gxmap

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class VoxDisplayException(geosoft.GXRuntimeError):
    """
    Exceptions from :mod:`geosoft.gxpy.vox_display`.

    .. versionadded:: 9.2
    """
    pass


ZONE_DEFAULT = 0
ZONE_LINEAR = 1
ZONE_NORMAL = 2
ZONE_EQUALAREA = 3
ZONE_SHADE = 4
ZONE_LOGLINEAR = 5
ZONE_LAST = 6

RENDER_FILL = 0
RENDER_EDGE = 1
RENDER_FILL_EDGE = 2
RENDER_SMOOTH = 3

class VoxDisplay:
    """
    Creation and handling of vox displays. Vox displays can be placed into a 3D view for display.

    :Constructors:
        :`solid`:        create as a solid, each cell colored from a `geosoft.gxpy.group.Color_map`
        :`vector`:       create as a vector voxel as vectors colored from a `geosoft.gxpy.group.Color_map`
        :`gxapi_gxvoxd`: create from an existing `geosoft.gxapi.GXVOXD` instance

    .. versionadded:: 9.3.1
    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __enter__(self):
        return self

    def __exit__(self, _type, _value, _traceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_close'):
            self._close()

    def _close(self):
        if hasattr(self, '_open'):
            if self._open:
                gx.pop_resource(self._open)
                self._gxvoxd = None
                self._vox = None
                self._open = None

    def __init__(self, vox, name=None):
        self._gxvoxd = None
        self._vox = vox
        if name is None:
            if vox is not None:
                name = vox.name
        self._name = name
        self._vector = False
        self._vector_cone_specs = (1., 4., 0.25, 5000)
        self._open = gx.track_resource(self.__class__.__name__, name)

    @classmethod
    def solid(cls,
              vox,
              color_map=None,
              zone=ZONE_DEFAULT,
              contour=None):
        """
        Create a solid colored vox_display from a `geosoft.gxpy.vox.Vox` instance.

        :param vox:         `geosoft.gxpy.vox.Vox` instance
        :param color_map:   `gxpy.group.Color_map` instance, or the name of a file, which may be
                            `.tbl`, `.zon`, `.itr`, or `.agg`.
        :param zone:        Colour distribution method:

                =================== ==================================================
                ZONE_DEFAULT        as set by user global default settings
                ZONE_LINEAR         linearly distributed
                ZONE_NORMAL         normal (Gaussian) distribution
                ZONE_EQUALAREA      each color will occupy an equal area on the image
                ZONE_LOGLINEAR      logarithmic linear distribution
                ZONE_LAST           last used coloring for this vox
                =================== ==================================================

        :param contour:             break colours on even multiples of contour

        .. versionadded:: 9.3.1
        """

        voxd = cls(vox)

        if (color_map is None) or (isinstance(color_map, str)):
            color_map = geosoft.gxpy.group.Color_map(color_map)
        color_map_file = color_map.save_file()

        if contour is None:
            contour = gxapi.rDUMMY
        voxd._gxvoxd = gxapi.GXVOXD.create(vox.gxvox, color_map_file, zone, contour)
        return voxd

    @classmethod
    def vector(cls,
               vox,
               vector_cone_specs=(1., 4., 0.25, 5000),
               color_map=None,
               zone=ZONE_DEFAULT,
               contour=None):
        """
        Create a vector symbol vox_display from a `geosoft.gxpy.vox.Vox` instance.

        :param vox:                 `geosoft.gxpy.vox.Vox` instance
        :param vector_cone_specs:   Vector plotting specs
                                    (scale_cell_ratio, height_base_ratio, base_cell_ratio, max_cones).
                                    Default is (1., 4., 0.25, 5000). See `vector_cone_specs` property.
        :param color_map:   `gxpy.group.Color_map` instance, or the name of a file, which may be
                            `.tbl`, `.zon`, `.itr`, or `.agg`.
        :param zone:        Colour distribution method:

            ::

                ZONE_DEFAULT        as set by user global default settings
                ZONE_LINEAR         linearly distributed
                ZONE_NORMAL         normal (Gaussian) distribution
                ZONE_EQUALAREA      each color will occupy an equal area on the image
                ZONE_LOGLINEAR      logarithmic linear distribution
                ZONE_LAST           last used coloring for this vox

        :param contour:             break colours on even multiples of contour

        .. versionadded:: 9.3.1
        """

        if not vox.is_vectorvox:
            raise VoxDisplayException(_t('vox must be a vectorvoxel to create a vector swarm'))
        voxd = VoxDisplay.solid(vox, color_map, zone, contour)
        voxd._vector = True
        voxd._vector_cone_specs = vector_cone_specs
        return voxd

    @classmethod
    def gxapi_gxvoxd(cls, gxapi_voxd, name=None):
        """
        Create a VoxDisplay instance from a `geosoft.gxapi.GXVOXD` or a `geosoft.gxapi.GXVECTOR3D` instance.

        :param gxapi_voxd:  `geosoft.gxapi.VOXD` or `geosoft.gxapi.GXVECTOR3D` instance
        :param name:        name of the voxel, required for a vector voxel.

        .. versionadded 9.3.1
        """
        if isinstance(gxapi_voxd, gxapi.GXVOXD):
            if name is None:
                name = gxapi.str_ref()
                gxapi_voxd.get_name(name)
            name = name.value
        else:
            if not name:
                raise VoxDisplayException(_t('a name is required to open a GXVECTOR3D object'))

        try:
            vox = gxvox.Vox.open(name)
        except Exception:
            vox = None

        name = os.path.splitext(os.path.basename(name))[0]

        voxd = cls(vox, name=name)
        voxd._gxvoxd = gxapi_voxd

        return voxd

    @property
    def vox(self):
        """ `geosoft.gxpy.vox.Vox` instance"""
        return self._vox

    @property
    def name(self):
        """ instance name, same as the contained Vox name"""
        return self._name

    @property
    def unit_of_measure(self):
        """Unit of data measurement for the contained vox data."""
        return self.color_map.unit_of_measure

    @property
    def is_vector(self):
        """True if this is a vector style display"""
        return self._vector

    @property
    def vector_cone_specs(self):
        """
        Vector plotting specs: (scale_cell_ratio, height_base_ratio, base_cell_ratio, max_cones). Can be set.

        scale_cell_ratio scales the maximum cone length to the size of the smallest cell. If None, default is 1.

        height_base_ratio is the ration of the cone height to the base size. If None, default is 4.

        base_cell_ratio is the maximum base size relative to the minimum cell size. If None, default is 0.25.

        max_cones is the maximum number of cones to draw. Voxel is decimated to limit the cones. None to plot all
        cones, though typically this is limited to about 2000 to improve display performance.

        .. versionadded:: 9.3.1
        """
        return self._vector_cone_specs

    @vector_cone_specs.setter
    def vector_cone_specs(self, specs):
        sc, hb, bc, mx = specs
        if sc is None or sc <= 0.:
            sc = 1.0
        if hb is None or hb <= 0.:
            hb = 4.
        if bc is None or bc <= 0.:
            bc = 0.25
        if mx is not None and mx <= 0:
            mx = None
        self._vector_cone_specs = (sc, hb, bc, mx)

    @property
    def draw_controls(self):
        """
        Vox drawing settings, returned as a tuple:

        (box_on, opacity, extent) as (boolean, float, (min_x, min_y, min_z, max_x, max_y, max_z))

        Can be set.

        .. versionadded:: 9.3.1
        """

        if self.is_vector:
            return None, None, None

        box = gxapi.int_ref()
        trans = gxapi.float_ref()
        x0 = gxapi.float_ref()
        x1 = gxapi.float_ref()
        y0 = gxapi.float_ref()
        y1 = gxapi.float_ref()
        z0 = gxapi.float_ref()
        z1 = gxapi.float_ref()
        self.gxvoxd.get_draw_controls(box, trans, x0, y0, z0, x1, y1, z1)
        return bool(box.value), trans.value, (x0.value, y0.value, z0.value, x1.value, y1.value, z1.value)

    @draw_controls.setter
    def draw_controls(self, controls):
        if self.is_vector:
            raise VoxDisplayException(_t('cannot set draw controls for a vector display'))
        box, trans, extent = controls
        x0, y0, z0, x1, y1, z1 = extent
        self.gxvoxd.set_draw_controls(box, trans, x0, y0, z0, x1, y1, z1)

    @property
    def render_mode(self):
        rm = gxapi.int_ref()
        self.gxvoxd.get_render_mode(rm)
        return rm.value

    @render_mode.setter
    def render_mode(self, mode):
        if mode not in (RENDER_FILL, RENDER_EDGE, RENDER_FILL_EDGE, RENDER_SMOOTH):
            raise VoxDisplayException(_t('Invalid render mode {}').format(mode))
        self.gxvoxd.set_render_mode(mode)

    @property
    def gxvoxd(self):
        """The :class:`geosoft.gxapi.GXVOXD` instance handle, None for a vector display."""
        return self._gxvoxd

    @property
    def is_thematic(self):
        """True if this is a thematic vox display"""
        if self.is_vector:
            return False
        return bool(self.gxvoxd.is_thematic())

    @property
    def opacity(self):
        """Opacity between 0. (invisible) and 1. (opaque) can be set."""
        return self.draw_controls[1]

    @opacity.setter
    def opacity(self, t):
        controls = list(self.draw_controls)
        controls[1] = t
        self.draw_controls = controls

    @property
    def color_map(self):
        """Return the colour map for this vox"""
        itr = gxapi.GXITR.create()
        self.gxvoxd.get_itr(itr)
        cmap = geosoft.gxpy.group.Color_map(itr)
        cmap.title = self.name
        if self.vox:
            cmap.unit_of_measure = self.vox.unit_of_measure
        return cmap

    @property
    def shell_limits(self):
        """
        The data limits of the visible data shell for scalar data. Can be set.

        returns: (min, max) limits, data outside this range is transparent, None for no limit

        .. versionadded 9.3.1
        """
        vmin = gxapi.float_ref()
        vmax = gxapi.float_ref()
        self.gxvoxd.get_shell_controls(vmin, vmax)
        vmin = vmin.value
        vmax = vmax.value
        if vmin == gxapi.rDUMMY:
            vmin = None
        if vmax == gxapi.rDUMMY:
            vmax = None
        return vmin, vmax

    @shell_limits.setter
    def shell_limits(self, limits):
        vmin, vmax = limits
        if vmin is None:
            vmin = gxapi.rDUMMY
        if vmax is None:
            vmax = gxapi.rDUMMY
        self.gxvoxd.set_shell_controls(vmin, vmax)

    def view_3d(self, file_name=None, overwrite=True, plane_2d=False):
        """
        Create a 3d view (`geosoft.gxpy.view.View_3d`) from the instance.

        :param file_name:   the name of a file for the 3d view. If None a temporary 3d view created.
        :param overwrite:   True to overwrite existing file
        :param plane_2d:    True to keep the 2D plane.  Only keep it if you intend to draw on it otherwise a grey
                            plane will appear in the view.

        .. versionadded:: 9.3
        """

        v3d = gxview.View_3d.new(file_name, overwrite=overwrite)
        gxgroup.VoxDisplayGroup.new(v3d, self)
        if not plane_2d:
            v3d.delete_plane(0)

        return v3d

    def figure_map(self, file_name=None, overwrite=True,
                   title=None, legend_label=None,
                   features=('LEGEND', 'NEATLINE'), **kwargs):
        """
        Create a figure view file from the instance.

        :param file_name:       the name of a file for the 3d view. If None a temporary 3d view created.
        :param overwrite:       True to overwrite existing file
        :param title:           Title added to the image
        :param legend_label:    If plotting a legend make this the legned title.  The default is the title in the
                                first aggregate layer colour map.
        :param features:        list of features to place on the map, default is ('SCALE', 'LEGEND', 'NEATLINE')

                                    =========== =========================================
                                    'LEGEND'    show the colour legend
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
                right_margin += 3.5
            kwargs['margins'] = (1, right_margin, bottom_margin, 1)

        gmap = gxmap.Map.figure((0, 0, 100, 100),
                                file_name=file_name,
                                features=features,
                                title=title,
                                overwrite=overwrite,
                                **kwargs)

        with gxview.View.open(gmap, "data") as v:

            if 'LEGEND' in features:
                gxgroup.legend_color_bar(v, 'legend',
                                         title=legend_label,
                                         location=(1, 0),
                                         cmap=self.color_map)

        area = gxview.View.open(gmap, gmap.current_data_view).extent_map_cm()
        area = (area[0] * 10., area[1] * 10., area[2] * 10., area[3] * 10.)

        gmap.create_linked_3d_view(self.view_3d(), area_on_map=area)

        return gmap
