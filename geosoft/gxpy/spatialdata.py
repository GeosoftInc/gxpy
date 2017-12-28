"""
Geosoft spatial data base class.

:Classes:

    ============= =======================================================
    `SpatialData` Geosoft spatial data base class
    ============= =======================================================

"""
import os

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import coordinate_system as gxcs
from . import utility as gxu

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class SpatialException(Exception):
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


class SpatialData:
    """
    Base class for spatial datasets.

    :param name:        dataset name.
    :param file_name:   persistent file name for this dataset.
    :param mode:        file mode, MODE_READ, MODE_READWRITE or MODE_NEW.  The default is MODE_NEW.
    :param overwrite:   Default is False. If True will raise an error if MODE_NEW and file_name exists.
    :param persist:     True to persist a MODE_NEW dataset.  If False, dataset files are deleted upon closing.
    :param gxobject:    Base GXAPI spatial dataset object, default is None.  If passed the base object is used
                        to resolve common named methods like get_ipj().

    :Properties:

        ================== =============================================================
        name               dataset name
        file_name          persistent file name
        metadata           metadata dictionary
        unit_of_measure    primary data unit of measurement
        coordinate_system  spatial coordinate system
        extent             spatial extent (min_x, min_y, min_z, max_x, max_y, max_z)
        extent_2d          2D spatial extent (min_x, min_y, max_x, max_y)
        extent_minimum     minimum spatial point (min_x, min_y, min_z)
        extent_maximum     maximum spatial point (max_x, max_y, max_z)
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

                if self.file_name and self._metadata_changed and self._mode != MODE_READ:
                    with open(self._file_name + '.xml', 'w+') as f:
                        f.write(gxu.xml_from_dict(self._metadata))

                self._metadata = None

                if self.file_name and not self._persist:
                    delete_files(self._file_name)

                gx.pop_resource(self._open)
                self._open = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __init__(self, name=None, file_name=None, mode=MODE_NEW, overwrite=False, persist=True, gxobject=None):

        if name is None:
            if file_name:
                name = os.path.splitext(os.path.basename(file_name))[0]

        if file_name is None:
            if mode != MODE_NEW:
                raise SpatialException(_t('Cannot read from an unnammed dataset'))
            persist = False

        else:

            if mode == MODE_NEW:
                if os.path.exists(file_name) and not overwrite:
                    raise SpatialException(_t('\'{}\' exists. Use overwrite=True to overwrite existing dataset file.').
                                           format(file_name))
            else:
                if not os.path.exists(file_name):
                    raise SpatialException(_t('Cannot find dataset file \'{}\'').
                                           format(file_name))
                persist = True

        self._file_name = file_name
        self._name = name
        self._mode = mode
        self._metadata = None
        self._metadata_changed = False
        self._metadata_root = ''
        self._cs = None
        self._persist = persist
        self._gxobject = gxobject
        self._open = gx.track_resource(self.__class__.__name__, self._name)

    def _init_metadata(self):
        if not self._metadata:
            self._metadata = gxu.geosoft_metadata(self._file_name)
        self._metadata_root = tuple(self._metadata.items())[0][0]

    @property
    def name(self):
        """dataset name"""
        return self._name

    @property
    def file_name(self):
        """dataset primary file name"""
        return self._file_name

    def close(self):
        """close the dataset."""
        self._close()

    @property
    def extent(self):
        """ (min_x, min_y, min_z, max_x, max_y, max_z) dataset extent."""
        if self._gxobject and hasattr(self._gxobject, 'get_extents'):
            rx0 = gxapi.float_ref()
            ry0 = gxapi.float_ref()
            rz0 = gxapi.float_ref()
            rx1 = gxapi.float_ref()
            ry1 = gxapi.float_ref()
            rz1 = gxapi.float_ref()
            self._gxobject.get_extents(rx0, ry0, rz0, rx1, ry1, rz1)
            return (rx0.value, ry0.value, rz0.value,
                    rx1.value, ry1.value, rz1.value)
        else:
            return None, None, None, None, None, None

    @property
    def extent_2d(self):
        """ Horizontal (min_x, min_y, max_x, max_y) extent of the dataset."""
        ex = self.extent
        return ex[0], ex[1], ex[3], ex[4]

    @property
    def extent_minimum(self):
        """ minimum dataset extent (min_x, min_y, min_z)"""
        ex = self.extent
        return ex[0], ex[1], ex[2]

    @property
    def extent_maximum(self):
        """ maximum dataset extent (max_x, max_y, max_z)"""
        ex = self.extent
        return ex[3], ex[4], ex[5]

    @property
    def coordinate_system(self):
        """
        `geosoft.gxpy.coordinate_system.Coordinate_system` instance of the dataset.

        Can be set using any constructor supported by `geosoft.gxpy.coordinate_system.Coordinate_system`.
        """
        if self._gxobject and hasattr(self._gxobject, 'get_ipj'):
            ipj = gxapi.GXIPJ.create()
            self._gxobject.get_ipj(ipj)
            return gxcs.Coordinate_system(ipj)
        else:
            if self._cs is None:
                self._cs = gxcs.Coordinate_system()
            return self._cs

    @coordinate_system.setter
    def coordinate_system(self, cs):
        if not isinstance(cs, gxcs.Coordinate_system):
            cs = gxcs.Coordinate_system(cs)
        if self._gxobject and hasattr(self._gxobject, 'set_ipj'):
            self._gxobject.set_ipj(gxcs.Coordinate_system(cs).gxipj)
        else:
            self._cs = cs

    @property
    def persist(self):
        """If True, the default,  a MODE_NEW dataset will persist after closing. Can be set."""
        return self._persist
    
    @persist.setter
    def persist(self, p):
        p = bool(p)
        if self.file_name is None:
            if p:
                raise SpatialException(_t('Cannot persist an unnamed dataset.'))
        else:
            if self.mode != MODE_NEW and not p:
                raise SpatialException(
                    _t('Cannot change persist status to False for a dataset not opened for MODE_NEW.'))
            self._persist = p

    @property
    def mode(self):
        """Open mode"""
        return self._mode

    @property
    def metadata(self):
        """
        Return the dataset metadata as a dictionary.  Can be set, in which case
        the dictionary items passed will be added to, or replace existing metadata.

        .. seealso::
            `Geosoft metadata schema <https://geosoftgxdev.atlassian.net/wiki/spaces/GXD93/pages/78184638/Geosoft+Metadata+Schema>`

        .. versionadded:: 9.3.1
        """
        self._init_metadata()
        return self._metadata[self._metadata_root]

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
        self.metadata = {'geosoft': {'dataset': {'geo:unitofmeasurement': {'#text': str(uom)}}}}
        self.metadata = {
            'geosoft': {'dataset': {'geo:unitofmeasurement': {'@xmlns:geo': 'http://www.geosoft.com/schema/geo'}}}}

