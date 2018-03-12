"""
Geosoft spatial data base class.

Spatial datasets are collections of geometric objects that have associated data, typically persisting in
a named file. Examples are Geosoft databases, grids, voxels, geosoft_surfaces.



:Classes:

    ============= ===================================================================================
    `SpatialData` base class for Geosoft spatial data, inherits from `geosoft.gxpy.geometry.Geometry`
    ============= ===================================================================================

"""
import os

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import utility as gxu
from . import geometry as gxgm
from . import coordinate_system as gxcs

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class SpatialException(geosoft.GXRuntimeError):
    """
    Exceptions from `geosoft.gxpy.spatial_data`.
    """
    pass


def delete_files(file_name):
    """
    Delete file and xml file

    :param file_name: base file name

    .. versionadded:: 9.3.1
    """

    def df(fn):
        try:
            os.remove(fn)
        except OSError:
            pass

    if file_name:

        df(file_name)
        df(file_name + '.xml')


MODE_READ = 0          #: existing dataset file open for read only
MODE_READWRITE = 1     #: open existing dataset file for read or write
MODE_NEW = 2           #: new dataset file


def find_meta_branch(meta, item):
    """
    Return the lowest branch in the meta dictionary that contains the item.

    ... versionadded:: 9.3.1
    """
    if item in meta:
        return meta
    for key, value in meta.items():
        if isinstance(value, dict):
            if item in value:
                return value
    for key, value in meta.items():
        if isinstance(value, dict):
            return find_meta_branch(value, item)
    return None


def coordinate_system_from_metadata(meta):
    """
    Return a `geosoft.gxpy.coordinate_system.Coordinate_system` instance from metadata.

    :param meta:    metadata dictionary
    :return:        `geosoft.gxpy.coordinate_system.Coordinate_system`, or None
    """
    try:
        geosoft = find_meta_branch(meta, 'geosoft')
        if geosoft:
            projection = find_meta_branch(geosoft['geosoft'], 'projection')
            if projection:
                return gxcs.Coordinate_system(projection['projection'])
    except:
        pass
    return None


def coordinate_system_from_metadata_file(file_name):
    """
    Return a `geosoft.gxpy.coordinate_system.Coordinate_system` instance from metadata.

    :param file_name:    spatial dataset name.
    :return:            `geosoft.gxpy.coordinate_system.Coordinate_system`, or None
    """
    return coordinate_system_from_metadata(gxu.geosoft_metadata(file_name))


def extent_from_metadata(meta):
    """
    Return spatial dataset extent from geosoft metadata.

    :param meta:                metadata dictionary
    :return:                    `geosoft.gxpy.geometry.Point2` instance

    .. versionadded:: 9.3.1
    """

    meta = find_meta_branch(meta, 'geosoft')
    if meta:
        cs = coordinate_system_from_metadata(meta)
        try:
            ex = meta['geosoft']['dataset']['georeference']['dataextents']['extent3d']
            minp = gxgm.Point((float(ex['@minx']), float(ex['@miny']), float(ex['@minz'])))
            maxp = gxgm.Point((float(ex['@maxx']), float(ex['@maxy']), float(ex['@maxz'])))
            return gxgm.Point2((minp, maxp), cs)

        except KeyError:
            pass

    return None


def extent_from_metadata_file(file_name):
    """
    Return spatial dataset extent from file metadata .xml file

    :param file_name:           spatial dataset file
    :return:                    `geosoft.gxpy.geometry.Point2` instance

    .. versionadded:: 9.3.1
    """
    return extent_from_metadata(gxu.geosoft_metadata(file_name))


class SpatialData(gxgm.Geometry):
    """
    Base class for spatial datasets.

    :param name:        dataset name.
    :param file_name:   file name for this dataset.
    :param mode:        file mode, MODE_READ, MODE_READWRITE or MODE_NEW.  The default is MODE_NEW.
    :param overwrite:   Default is False. If True will raise an error if MODE_NEW and file_name exists.
    :param gxobj:       Base GXAPI spatial dataset object, default is None.  If passed the base object is used
                        to resolve common named methods like *`get_ipj()`*.

    :Properties:
    
        properties of `geosoft.gxpy.geometry.Geometry` plus:

        ================== =============================================================
        `file_name`        file name
        `metadata`         metadata dictionary
        `unit_of_measure`  primary data unit of measurement
        ================== =============================================================

    .. versionadded:: 9.3.1
    """

    def __enter__(self):
        return self

    def __exit__(self, _type, value, traceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_close'):
            self._close()

    def _close(self):

        if hasattr(self, '_open'):
            if self._open:

                gx.pop_resource(self._open)
                self._open = None

                if self.file_name and self._metadata_changed and self._mode != MODE_READ:
                    with open(self._file_name + '.xml', 'w+') as f:
                        f.write(gxu.xml_from_dict(self._metadata))

                self._metadata = None
                self._gxobj = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __init__(self, name=None, file_name=None, mode=MODE_NEW, overwrite=False, **kwargs):

        if name is None:
            if file_name:
                name = os.path.splitext(os.path.basename(file_name))[0]
                
        super().__init__(name=name, **kwargs)

        if file_name is None:
            if mode != MODE_NEW:
                raise SpatialException(_t('Cannot read from an unnammed dataset'))

        else:

            if mode == MODE_NEW:
                if self.gxobj is None and not overwrite and os.path.exists(file_name):
                    raise SpatialException(_t('\'{}\' exists. Use overwrite=True to overwrite existing dataset file.').
                                           format(file_name))
            else:
                if not os.path.exists(file_name):
                    raise SpatialException(_t('Cannot find dataset file \'{}\'').
                                           format(file_name))

        self._file_name = file_name
        self._mode = mode
        self._metadata = None
        self._metadata_changed = False
        self._metadata_root = ''
        self._open = gx.track_resource(self.__class__.__name__, self._name)

    def _init_metadata(self):
        if not self._metadata:
            self._metadata = gxu.geosoft_metadata(self._file_name)
        self._metadata_root = tuple(self._metadata.items())[0][0]

    @property
    def file_name(self):
        """dataset primary file name"""
        return self._file_name

    def close(self):
        """close the dataset."""
        self._close()

    @property
    def dataset_mode(self):
        """Dataset open mode"""
        return self._mode

    @property
    def metadata(self):
        """
        Return the dataset metadata as a dictionary.  Can be set, in which case
        the dictionary items passed will be added to, or replace existing metadata.

        .. seealso:: Geosoft metadata
            `Schema <https://geosoftgxdev.atlassian.net/wiki/spaces/GXD93/pages/78184638/Geosoft+Metadata+Schema>`

        .. versionadded:: 9.3.1
        """
        if self._open is not None:
            self._init_metadata()
            return self._metadata[self._metadata_root]
        else:
            return None

    @metadata.setter
    def metadata(self, meta):
        self._init_metadata()
        self._metadata[self._metadata_root] = gxu.merge_dict(self._metadata[self._metadata_root], meta)
        self._metadata_changed = True

    @property
    def unit_of_measure(self):
        """
        Units of measurement (a string) for the primary scalar data associated with this dataset.

        Can be set.

        .. versionadded:: 9.3.1
        """
        try:
            uom = self.metadata['geosoft']['dataset']['geo:unitofmeasurement']['#text']
        except KeyError:
            uom = ''
        return uom

    @unit_of_measure.setter
    def unit_of_measure(self, uom):
        self.metadata = {'geosoft':
                             {'@xmlns': 'http://www.geosoft.com/schema/geo',
                              'dataset':
                                  {'geo:unitofmeasurement':
                                       {'@xmlns:geo': 'http://www.geosoft.com/schema/geo',
                                        '#text': str(uom)}}}}
