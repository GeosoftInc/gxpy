"""
Geosoft aggregate images

:Classes:

    ======================== ====================================================
    :class:`Aggregate_image` image constructed from one or more grid/image layers
    ======================== ====================================================
    
Geosoft aggregates are "aggregations" of one or more grid layers that together create a
georeferenced image that can be placed in a map view or rendered on a plane in a 3D view.

.. seealso:: :class:`geosoft.gxapi.GXAGG`

.. note::

    Regression tests provide usage examples:     
    `aggregate tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_agg.py>`_

"""
import os

import geosoft
import geosoft.gxapi as gxapi
from . import gx
from . import vv as gxvv
from . import grid as gxgrd
from . import map as gxmap
from . import view as gxview
from . import group as gxgroup
from . import geometry as gxgm
from . import utility as gxu
from . import coordinate_system as gxcs

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class AggregateException(geosoft.GXRuntimeError):
    """
    Exceptions from :mod:`geosoft.gxpy.agg`.

    .. versionadded:: 9.2
    """
    pass

ZONE_DEFAULT = 0 #:
ZONE_LINEAR = 1 #:
ZONE_NORMAL = 2 #:
ZONE_EQUALAREA = 3 #:
ZONE_SHADE = 4 #:
ZONE_LOGLINEAR = 5 #:
ZONE_LAST = 6 #:

class Aggregate_image(gxgm.Geometry):
    """
    The AGG class supports the creation of aggregate images from one or more grid data sets. Aggregates
    can be placed into a 2D or 3D view for display.

    :param grid_file:   if specified, the :meth:`add_layer()` method is called with remaining parameters
                        to create a single-image aggregate.

    :Constructors:

        ============= ===========================
        :meth:`open`: open an existing aggregate
        :meth:`new`:  create a new aggregate
        ============= ===========================
        
    .. versionadded:: 9.2
    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self._create_name()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_gxagg'):
            self._gxagg = None

    def __init__(self):
        self._gxagg = None
        self._base_properties = None
        self._extent = None
        super().__init__()

    @classmethod
    def new(cls, grid_file=None, **kwargs):
        """
        Create a new aggregate from a grid.
        
        :param grid_file: grid file name

        :meth:`add_layer` is called to add the grid as a layer.
        
        .. versionadded:: 9.2
        """

        agg = cls()
        agg._gxagg = gxapi.GXAGG.create()
        if grid_file is not None:
            agg.add_layer(grid_file, **kwargs)
        return agg

    @classmethod
    def open(cls, gxagg):
        """
        Create an :class:`Aggregate_image` from a :class:`geosoft.gxapi.GXAGG` instance.
        
        :param gxagg: :class:`geosoft.gxapi.GXAGG` instance
        
        .. versionadded:: 9.2
        """

        agg = cls()
        if not isinstance(gxagg, gxapi.GXAGG):
            raise AggregateException(_t('A gxapi.GXAGG isstance is required.'))
        agg._gxagg = gxagg
        return agg

    def close(self):
        """Close an Aggregate, releases resources."""
        self._gxagg = None

    def _set_properties(self):
        if self.layer_count > 0:
            with gxgrd.Grid.open(self.layer_file_names[0]) as g:
                self._base_properties = g.properties()
                self._extent = gxgm.Point2(g.extent)
                self._extent_2d = g.extent_cell_2d()

    @property
    def extent(self):
        return self._extent

    @property
    def extent_2d(self):
        return self._extent_2d

    @property
    def gxagg(self):
        """ The :class:`geosoft.gxapi.GXAGG` instance handle."""
        return self._gxagg

    @property
    def layer_count(self):
        """Number of layers in the aggregate."""
        return self.gxagg.num_layers()

    @property
    def brightness(self):
        """ Aggregate brightness between -1 (black) and +1 (white)."""
        return self.gxagg.get_brightness()

    @brightness.setter
    def brightness(self, adjustment):
        a = max(-1.0, min(adjustment, 1.0))
        self.gxagg.change_brightness(a)

    @property
    def name(self):
        """Name of the Aggregate_image."""
        return self._create_name()

    @property
    def layer_file_names(self):
        """
        Return list of layer files in the aggregate.

        .. versionadded:: 9.2
        """

        vv = gxvv.GXvv(dtype='U1024')
        self.gxagg.list_img(vv.gxvv)
        return list(vv.np)

    @property
    def spatial_properties(self):
        """
        Returns the spatial properties of the base layer in the aggregate.

        :return: (nx, ny, x0, y0, dx, dy, rot)

        .. versionadded:: 9.3.1
        """
        x0 = self._base_properties['x0']
        y0 = self._base_properties['y0']
        dx = self._base_properties['dx']
        dy = self._base_properties['dy']
        nx = self._base_properties['nx']
        ny = self._base_properties['ny']
        rot = self._base_properties['rot']
        return nx, ny, x0, y0, dx, dy, rot

    @property
    def coordinate_system(self):
        """
        Returns the aggregate coordinate_system, which is the same as the first layer.

        :return: pixel size in units of the coordinate system

        .. versionadded:: 9.3.1
        """
        return self._base_properties['coordinate_system']

    def _layer_index(self, layer):
        if isinstance(layer, str):
            layer = layer.lower()
            for l in range(self.layer_count):
                if layer == self.layer_file_names[l].lower():
                    return l
            raise AggregateException(_t('Layer \'{}\' not found.'.format(layer)))

        if layer >= self.layer_count:
            raise AggregateException(
                _t('Layer \'{}\' ot of range for aggregate with {} layers.'.format(layer, self.layer_count)))
        return layer

    def _create_name(self):
        s = ''
        layernames = self.layer_file_names
        if not layernames:
            return s
        names = []
        for fn in layernames:
            names.append(os.path.basename(fn).split('.')[0])
        for fn in names:
            # ignore shaded layers if parent is here.
            if fn[-2:] == '_s':
                if fn[:-2] in names:
                    continue
                i = str.rfind(fn[:-2], '_')
                if i > 1 and fn[:i] in names:
                    continue
            s = s + fn + ', '
        return s[:-2]

    def add_layer(self,
                  grid_file,
                  color_map=None,
                  zone=None,
                  shade=False,
                  minimum=None,
                  maximum=None,
                  contour=None):
        """
        Add an image layer to an aggregate

        :param grid_file:       The name of a grid file (image or data) to add.
        :param color_map:       :class:`gxpy.group.Color_map` instance, or the name of a file, which may be 
                                `.tbl`, `.zon`, `.itr`, or `.agg`.
        :param zone:            Colour distribution method:

            ::

                ZONE_DEFAULT        as set by user global default settings
                ZONE_LINEAR         linearly distributed
                ZONE_NORMAL         normal (Gaussian) distribution
                ZONE_EQUALAREA      each color will occupy an equal area on the image
                ZONE_LOGLINEAR      logarithmic linear distribution
                ZONE_LAST           last used coloring for this grid file
                ZONE_SHADE          Displays the shaded image version of the grid. The shaded image is
                                    a grid file will with '_s' appended to the file name.  If it does not
                                    exist, a shaded image with illumination inclination and declination
                                    both set to 45 degrees is automatically created.
                                    
        :param shade:           True, to add a shading layer
        :param minimum:         Minimum data value. All grid values less than or equal to the
                                minimum will be assigned the first color in the table.  The default is
                                calculated from the data.
        :param maximum:         Maximum data value.  All grid values greater than or equal to the maximum
                                will be assigned the last color in the table.  The default is calculated from
                                the data.
        :param contour:         Break colors on this interval, colors will be thinned if necessary.
                                

        .. versionadded:: 9.2
        """

        if (color_map is None):
            if zone == ZONE_SHADE:
                color_map = 'lgray.tbl'
        if (color_map is None) or (isinstance(color_map, str)):
            color_map = geosoft.gxpy.group.Color_map(color_map)
        color_map_file = color_map.save_file()

        try:
            if grid_file is not None:
                if zone is None:
                    zone = ZONE_DEFAULT
                if minimum is None:
                    minimum = gxapi.rDUMMY
                if maximum is None:
                    maximum = gxapi.rDUMMY
                if contour is None:
                    contour = gxapi.rDUMMY
                self.gxagg.layer_img_ex(grid_file,
                                        zone,
                                        color_map_file,
                                        minimum,
                                        maximum,
                                        contour)
                if shade and (zone != ZONE_SHADE):
                    self.gxagg.layer_img(grid_file, ZONE_SHADE, 'lgray.tbl', gxapi.rDUMMY)
        finally:
            if os.path.exists(color_map_file):
                os.remove(color_map_file)
            with gxgrd.Grid.open(grid_file) as g:
                color_map.units = g.unit_of_measure

        if self._base_properties is None:
            self._set_properties()


    def layer_color_map(self, layer=0):
        """
        Return the :class:`geosoft.gxpy.group.Color_map` of a layer.
        
        :param layer: layer number or layer name
        :returns: :class:`geosoft.gxpy.group.Color_map`

        .. versionadded:: 9.2
        """

        layer = self._layer_index(layer)
        itr = gxapi.GXITR.create()
        self.gxagg.get_layer_itr(layer, itr)
        cmap = geosoft.gxpy.group.Color_map(itr)
        cmap.title = os.path.basename(self.layer_file_names[layer]).split('.')[0]

        with gxgrd.Grid.open(self.layer_file_names[layer]) as g:
            cmap.unit_of_measure = g.unit_of_measure

        return cmap

    def layer_unit_of_measure(self, layer=0):
        """
        Return the unit of measurement for the specified layer

        :param layer: layer number or layer name

        .. versionadded:: 9.3
        """

        layer = self._layer_index(layer)
        with gxgrd.Grid.open(self.layer_file_names[layer]) as g:
            uom = g.unit_of_measure
        return uom

    def figure_map(self, file_name=None, title=None, legend_label=None,
                   features=['SCALE', 'LEGEND', 'NEATLINE'], **kwargs):
        """
        Create a figure map file from an aggregate.

        :param file_name:       the name of the map, if None a default map is created.
        :param overwrite:       True to overwrite existing image file
        :param title:           Title added to the image
        :param legend_label:    If plotting a legend make this the legned title.  The default is the title in the
                                first aggregate layer colour map.
        :param features:        list of features to place on the map, default is ('SCALE', 'LEGEND', 'NEATLINE')

                                    =========== =========================================
                                    'SCALE'     show a scale bar
                                    'LEGEND'    show an aggregate colour legend
                                    'NEATLINE'  draw a neat-line around the image
                                    'ANNOT_XY'  annotate map coordinates
                                    'ANNOT_LL'  annotate map Latitude, Longitude
                                    'CONTOUR'   contour the first layer in the aggregate
                                    =========== =========================================

        :param kwargs:          passed to `geosoft.gxpy.map.Map.new`

        .. versionadded:: 9.3
        """

        ref_grid_name = self.layer_file_names[0]
        ref_grid = gxgrd.Grid.open(ref_grid_name)

        # uppercase features, use a dict so we pop things we use and report error
        if isinstance(features, str):
            features = (features,)
        feature_list = {}
        if features is not None:
            for f in features:
                feature_list[f.upper()] = None
            if 'ALL' in feature_list:
                feature_list = {'ALL': None,
                                'LEGEND': None,
                                'CONTOUR': None}
        features = list(feature_list.keys())

        # setup margins
        if not ('margins' in kwargs):

            bottom_margin = 1.0
            if title:
                bottom_margin += len(title.split('\n')) * 1.0
            if 'ALL' in feature_list or 'SCALE' in feature_list:
                bottom_margin += 1.2

            right_margin = 1
            if 'ALL' in feature_list or 'LEGEND' in feature_list:
                right_margin += 3.5
            kwargs['margins'] = (1, right_margin, bottom_margin, 1)
        kwargs['coordinate_system'] = ref_grid.coordinate_system

        gmap = gxmap.Map.figure(ref_grid.extent_xy,
                                file_name=file_name,
                                features=features,
                                title=title,
                                **kwargs)

        with gxview.View.open(gmap, "data") as v:

            ref_grid = None
            gxgroup.Aggregate_group.new(v, self)

            if 'CONTOUR' in features:
                gxgroup.contour(v, 'contour', ref_grid_name)

            if 'LEGEND' in features:
                if self.layer_count > 1:
                    cmap2 = self.layer_color_map(1)
                else:
                    cmap2=None
                gxgroup.legend_color_bar(v, 'legend',
                                         title=legend_label,
                                         location=(1, 0),
                                         cmap=self.layer_color_map(0),
                                         cmap2=cmap2)

        return gmap

    def image_file(self, image_file=None, image_type=gxmap.RASTER_FORMAT_PNG, pix_width=None, display_area=None):
        """
        Save the aggregate as a georeferenced image file.

        :param image_file:  image file name. The extension should be consistent with the image_type.
                            If not specified a temporary PNG file is created.
        :param image_type:  image type, one ot the RASTER_FORMAT constants in `geosoft.gxpy.map`.
        :param pix_width:   desired image width in pixels, default is the width of the aggregate base layer
        :param display_area:    `geosoft.gxpy.geometry.Point2` instance, which defines the desired display
                                area. The display area coordinate system can be different from the grid.

        :return:            image file name.

        .. versionadded:: 9.3.1
        """

        if self.layer_count == 0:
            raise AggregateException(_t('Aggregate has no layers'))

        if display_area is None:
            data_area = self.extent_2d
            coordinate_system = self.coordinate_system
        else:
            data_area = display_area.extent_xy
            if not gxcs.is_known(display_area.coordinate_system):
                coordinate_system = self.coordinate_system
            else:
                coordinate_system = display_area.coordinate_system



        if image_file is None:
            image_file = gx.gx().temp_file('.png')
            image_type = gxmap.RASTER_FORMAT_PNG

        nx, _, _, _, dx, *_ = self.spatial_properties

        if pix_width is None or pix_width <= 0:
            pix_width = nx

        with gxmap.Map.new(data_area=data_area,
                           coordinate_system=coordinate_system,
                           margins=(0, 0, 0, 0),
                           inside_margin=0) as gmap:
            gmap.remove_on_close()
            
            with gxview.View.open(gmap, "data") as v:
                gxgroup.Aggregate_group.new(v, self)

            gmap.image_file(image_file, type=image_type, pix_width=pix_width)

        return image_file
