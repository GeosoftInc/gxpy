"""
Geosoft dap server handling.

:Classes:

    ===== ==========================================================================
    `Dap` Geosoft dap server
    ===== ==========================================================================

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_dap.py>`_

.. versionadded:: 9.4
"""
from json import dumps, loads
from requests import get, post, exceptions
from enum import Enum
from collections.abc import Sequence

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import coordinate_system as gxcs


__version__ = geosoft.__version__

def _t(s):
    return geosoft.gxpy.system.translate(s)


class DapServerException(geosoft.GXRuntimeError):
    """
    Exceptions from `geosoft.gxpy.dap`.
    """
    pass


class DatasetType(Enum):
    Map = 0
    Grid = 1
    Picture = 2
    Point = 3
    Database = 4
    Document = 5
    SPF = 6
    Generic = 7
    Voxel = 8
    ArcGIS = 9
    ImageServer = 10
    PictureSection = 11
    GridSection = 12
    ProjectZip = 13
    Drillhole = 14
    NoData = 15
    ThreeDV = 16
    Geostring = 17
    GMSYS3D = 18
    VOXI = 19
    PDF = 20
    Geosurface = 21
    GMSYS2D = 22
    VectorVoxel = 23
    GeosoftOffline = 24

def _json_default(o):
    return o.__dict__


def _decode_object(o):
    if 'CoordinateSystem' in o:
        b = BoundingBox(cs_as_xml=False, coordinate_system=o['CoordinateSystem'])
        b.__dict__.update(o)
        return b
    else:
        d = Dataset()
        d.__dict__.update(o)
        d.Type = DatasetType(d.Type)
        return d


def _http_get(url, headers=None, decoder=None):
    if headers is None:
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = get(url, headers=headers)
    if (response.ok):
        data = loads(response.content.decode('utf-8'), object_hook=decoder)
        return data
    else:
        response.raise_for_status()


def _http_post(url, post_parameters, headers=None, decoder=None):

    if headers is None:
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = post(url, data=dumps(post_parameters, default=_json_default), headers=headers)

    if (response.ok):
        data = loads(response.content.decode('utf-8'), object_hook=decoder)
        return data
    else:
        response.raise_for_status()


class BoundingBox:
    """
    Create a bounding box instance.

    :param minx:                `MinX`
    :param miny:                `MinY`
    :param minz:                `MinZ`
    :param maxx:                `MaxX`
    :param maxy:                `MaxY`
    :param maxz:                `MaxZ`
    :param coordinate_system:   `CoordinateSystem`
                                any supported coordinate system representation. Default is "WGS 84".
    :param cs_as_xml:           True to force the coordinate_system to be xml.
    """

    def __init__(self, minx=-180, miny=-90, minz=0, maxx=180, maxy=90, maxz=0,
                 coordinate_system="WGS 84", cs_as_xml=False):
        self.MinX = minx
        self.MinY = miny
        self.MinZ = minz
        self.MaxX = maxx
        self.MaxY = maxy
        self.MaxZ = maxz
        if cs_as_xml:
            try:
                self.CoordinateSystem = gxcs.Coordinate_system(coordinate_system).xml
            except gxcs.CSException:
                self.CoordinateSystem = gxcs.Coordinate_system().xml
        else:
            self.CoordinateSystem = coordinate_system

    def __str__(self):
        a = '[%s, %s, %s] - [%s, %s %s], %s'
        b = (self.MinX, self.MinY, self.MinZ, self.MaxX, self.MaxY, self.MaxZ, self.CoordinateSystem)
        return a % b

    def __repr__(self):
        a = 'BoundingBox(minx=%r,miny=%r,minz=%r,maxx=%r,maxy=%r,maxz=%r,coordinate_system=%r)'
        b = (self.MinX, self.MinY, self.MinZ, self.MaxX, self.MaxY, self.MaxZ, self.CoordinateSystem)
        return a % b


class Dataset:
    """
    Single dataset information instance.

    :param id:              `Id`    unique identifier
    :param title:           `Title`
    :param type:            `Type` dataset type, one of `DatasetType`.
    :param hierarchy:       `Hierarchy` location in the catalog hierarchy
    :param stylesheet:      `Stylesheet` metadata style sheet
    :param extents:         `Extents` is a `BoundingBox` instance
    :param has_original:    `HasOriginal` True if the original data is available

    .. versionadded:: 9.4
    """

    def __init__(self, id=None, title=None, type=0, hierarchy=None, stylesheet=None, extents=None,
                 has_original=False):

        if extents is None:
            extents = BoundingBox(cs_as_xml=False)

        self.Id = id
        self.Title = title
        self.Type = type
        self.Hierarchy = hierarchy
        self.Stylesheet = stylesheet
        self.Extents = extents
        self.HasOriginal = has_original

    def __str__(self):
        a = 'Id: %s, Title: %s, Type: %s, Hierarchy: %s, Extents: %s'
        b = (self.Id, self.Title, self.Type, self.Hierarchy, self.Extents)
        return a % b

    def __repr__(self):
        a = 'Dataset(id=%r,title=%r,type=%r,hierarchy=%r,stylesheet=%r,extents=%r,has_original=%r)'
        b = (self.Id, self.Title, self.Type, self.Hierarchy, self.Stylesheet, self.Extents, self.HasOriginal)
        return a % b


class SearchFilter:
    """
    Search filter

    :param free_text_query:             title/keyword search filter
    :param structured_metadata_query:
    :param extents:                     `BoundingBox` instance
    :param entirely_within:             `True` for completely enclosed data, `False` for intersecting data.
    :param version:                     minimum version, default is 1.

    .. versionadded:: 9.4
    """

    def __init__(self, free_text_query=None, structured_metadata_query=None, extents=None,
                 entirely_within=False, version=1):

        if extents is None:
            extents = BoundingBox(cs_as_xml=True)

        self.FreeTextQuery = free_text_query
        self.StructuredMetadataQuery = structured_metadata_query
        self.BoundingBox = extents
        self.EntirelyWithin = int(entirely_within)
        self.RequestVersion = version

    def __str__(self):
        a = 'FreeTextQuery: %s, StructuredMetadataQuery: %s, EntirelyWithin: %s, Extents: %s'
        b = (self.FreeTextQuery, self.StructuredMetadataQuery, self.EntirelyWithin, self.BoundingBox)
        return a % b

    def __repr__(self):
        a = 'SearchFilter(free_text_query=%r,structured_metadata_query=%r,extents=%r,entirely_within=%r,version=%r)'
        b = (self.FreeTextQuery,
             self.StructuredMetadataQuery,
             self.BoundingBox,
             self.EntirelyWithin,
             self.RequestVersion)
        return a % b


class ResultFilter:
    """
    Limit results.

    :param path:            to this location in the hierarchy
    :param depth:           to this depth in the hierarchy
    :param start_index:     start index in the list
    :param max_results:     maximum results to include
    :param valid_path:      TODO: Ryan, what is this?

    .. versionadded:: 9.4
    """

    def __init__(self, path=None, depth=2147483647, start_index=0, max_results=0, valid_path=False):
        self.Path = path
        self.Depth = depth
        self.StartIndex = start_index
        self.MaxResults = max_results
        self.ValidPath = valid_path

    def __str__(self):
        return 'Path: %s, Depth: %s, StartIndex: %s, MaxResults: %s, ValidPath: %s' % (
        self.Path, self.Depth, self.StartIndex, self.MaxResults, self.ValidPath)

    def __repr__(self):
        return 'ResultFilter(path=%r,depth=%r,start_index=%r,max_results=%r,valid_path=%r)' % (
        self.Path, self.Depth, self.StartIndex, self.MaxResults, self.ValidPath)


class SearchParameters:
    """
    Search parameters, defined by a `SearchFilter` and a `ResultFilter`

    :param search_filter:   `SearchFilter` instance
    :param result_filter:   `ResultFilter` instance

    .. versionadded:: 9.4
    """

    def __init__(self, search_filter=None, result_filter=None):

        if search_filter is None:
            search_filter = SearchFilter()
        if result_filter is None:
            result_filter = ResultFilter()
        self.SearchFilter = search_filter
        self.ResultFilter = result_filter

    def __str__(self):
        return 'SearchFilter: %s, ResultFilter: %s' % (self.SearchFilter, self.ResultFilter)

    def __repr__(self):
        return 'SearchParameters(search_filter=%r,result_filter=%r)' % (self.SearchFilter, self.ResultFilter)

class DapServer(Sequence):
    """
    DapServer class to communicate with a Geosoft DAP server.

    :param url:         url of the server, default is 'http://dap.geosoft.com/'
    :param get_catalog: `True` (the default) to get the server catalog.  If `False` the caller needs to call
                        method `catalog` to get the data catalog from the server.

    .. versionadded:: 9.4
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        pass

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        if self._config is None:
            name = _t('unknown name')
        else:
            name = self._config['Name']
        datasets = len(self._cat)
        if datasets == 0:
            datasets = '?'
        return '{}: {} ({} datasets)'.format(self._url, name, datasets)

    def __init__(self, url='http://dap.geosoft.com/', get_catalog=True):

        super().__init__()
        self._cat = []
        self._config = None

        # establish url and rest url
        url = url.lower()
        if url[-1] != '/':
            url = url + '/'
        if url[-5:] == 'rest/':
            self._rest_url = url
            self._url = url[:-5]
        else:
            self._rest_url = url + 'rest/'
            self._url = url

        # configuration
        try:
            c = self.configuration
        except exceptions.HTTPError as e:
            raise DapServerException(_t('Server \'{}\' has a problem:\n{}'.format(self._url, str(e))))

        # dataset catalog

        if get_catalog:
            try:
                self.catalog()
            except exceptions.HTTPError as e:
                raise DapServerException(_t('Server \'{}\' has a problem:\n{}'.format(self._url, str(e))))

        self._next = 0

    def __len__(self):
        return len(self._cat)

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= len(self._cat):
            self._next = 0
            raise StopIteration
        else:
            ds = self._cat[self._next]
            self._next += 1
            return ds

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._cat[item]
        else:
            if isinstance(item, str):
                title = item
                hierarchy = None
            else:
                hierarchy, title, *_ = tuple(item)
            for i in self._cat:
                if hierarchy and i.Hierarchy != hierarchy:
                    continue
                if i.Title == title:
                    return i
        return None

    @property
    def url(self):
        """ Server url."""
        return self._url

    @property
    def configuration(self):
        """
        Return service configuration info.

        See http://dap.geosoft.com/REST/service/help/operations/GetConfiguration

        .. versionadded:: 9.4
        """
        if self._config is None:
            self._config = _http_get(self._rest_url + 'service/configuration?key=test')
        return self._config

    def catalog(self, search_parameters=None, refresh=False):
        """
        Return a filtered catalog list.

        :param search_parameters:   search filter, instance of `SearchParameters`
        :param refresh:             force a refresh
        :return:                    list of server catalog entries

        .. versionadded:: 9.4
        """

        if search_parameters is None:
            search_parameters = SearchParameters()

        if refresh or len(self._cat) == 0:
            self._cat = _http_post(self._rest_url + 'catalog/search?key=test', search_parameters, decoder=_decode_object)
        return self._cat
