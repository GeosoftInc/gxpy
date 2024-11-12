#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
"""
Geosoft dap server handling.

:Classes:

    ======================= ===============================================================
    `DapClient`             Geosoft dap client
    `DataType`              data type
    `GridExtractFormat`     return format for extracting a grid
    `ExtractProgressStatus` progress
    `DataExtract`           data extraction
    `BoundingBox`           bounding box
    `DataCard`              data information
    `SearchFilter`          search filter
    `ResultFilter`          result filter
    `SearchParameters`      search parameters
    ======================= ===============================================================

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_dap.py>`_

.. versionadded:: 9.4
"""

import time
import os
from json import dumps, loads
from requests import get, post, exceptions
from enum import Enum
from collections.abc import Sequence

import geosoft
from . import gx as gx
from . import coordinate_system as gxcs
from . import geometry as gxgeo
from . import system as gxsys
from . import utility as gxu


__version__ = geosoft.__version__

def _t(s):
    return geosoft.gxpy.system.translate(s)


def _json_default(o):
    return o.__dict__


def _decode_object(o):
    # print(str(o))
    if 'CoordinateSystem' in o:
        b = BoundingBox(coordinate_system=o['CoordinateSystem'])
        b.__dict__.update(o)
        return b
    else:
        d = DataCard()
        d.__dict__.update(o)
        d.Type = DataType(d.Type)
        return d


class DapClientException(geosoft.GXRuntimeError):
    """
    Exceptions from `geosoft.gxpy.dap`.
    """
    pass


class DataType(Enum):
    """Supported data types"""
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

    def datatype_default_extension(item):
        if not isinstance(item, DataType):
            item = DataType(item)
        ext_list = ('map',  # 0
                    'grd',  # 1
                    'png',  # 2
                    'csv',  # 3
                    'gdb',  # 4
                    'unknown',  # 5
                    'spf',  # 6
                    'unknown',  # 7
                    'geosoft_voxel',  # 8
                    'ArcGIS',  # 9
                    'png',  # 10
                    'png',  # 11
                    'grd',  # 12
                    'zip',  # 13
                    'zip',  # 14
                    'unknown',  # 15
                    '3dv',  # 16
                    'geosoft_geostring',  # 17
                    'GMSYS3D',  # 18
                    'geosoft_voxi',  # 19
                    'pdf',  # 20
                    'geosoft_geosurface',  # 21
                    'GMSYS2D',  # 22
                    'geosoft_vector_voxel',  # 23
                    'unknown')  # 24
        return ext_list[item.value]

    def extract_url(item):
        if not isinstance(item, DataType):
            item = DataType(item)
        return 'dataset/extract/' + item.name.lower() + '/'


class GridExtractFormat(Enum):
    GeosoftCompressed = 0
    GeosoftUncompressed = 1
    ESRIBinaryRaster = 2
    BIL = 3
    Geopak = 4
    GXFText = 5
    GXFCompressed = 6
    ODDFPC = 7
    ODDFUnix = 8
    SurferV6 = 9
    SurferV7 = 10
    USGSPC = 11
    USGSUnix = 12
    ERMapper = 13


class ExtractProgressStatus(Enum):
   Prepare = 0
   Extract = 1
   Compress = 2
   Complete = 3
   Cancelled = 4
   Failed = 5

class DataExtract:
    """
    Data extraction instance.

    :param filename:    name of the data file
    :param extents:     data extent as a `BoundingBox` or `geosoft.gxpy.geopmetry.Point2` instance
    :param resolution:  desired resolution in the distance units of the extents coordinate system
    :param format:      one of the extraction formats for the data type, default is the first format.

    .. versionadded:: 9.4
    """

    def __init__(self, filename, extents=None, resolution=0, format=0):
        extents = BoundingBox(extents)
        self.BoundingBox = extents
        self.Filename = filename
        self.Resolution = resolution
        if not isinstance(format, int):
            format = format.value
        self.Format = format

    def __str__(self):
        return 'Resolution: %s, Format: %s, Extents: %s' % (self.Resolution, self.Format, self.BoundingBox)

    def __repr__(self):
        return 'DataExtract(extents=%r,filename=%r,resolution=%r,format=%r)' % (
        self.BoundingBox, self.Filename, self.Resolution, self.Format)


class BoundingBox:
    """
    Bounding box instance.

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
                 coordinate_system="WGS 84"):

        if isinstance(minx, BoundingBox):
            extent = minx
            self.MinX = extent.MinX
            self.MinY = extent.MinY
            self.MinZ = extent.MinZ
            self.MaxX = extent.MaxX
            self.MaxY = extent.MaxY
            self.MaxZ = extent.MaxZ
            self.CoordinateSystem = extent.CoordinateSystem

        else:
            try:
                self.MinX = float(minx)
                self.MinY = float(miny)
                self.MinZ = float(minz)
                self.MaxX = float(maxx)
                self.MaxY = float(maxy)
                self.MaxZ = float(maxz)
                self.CoordinateSystem = gxcs.Coordinate_system(coordinate_system).xml

            except (TypeError, ValueError):
                extent = minx
                if not isinstance(extent, gxgeo.Point2):
                    extent = gxgeo.Point2(extent, coordinate_system=coordinate_system)
                self.MinX, self.MinY, self.MinZ, self.MaxX, self.MaxY, self.MaxZ = extent.extent_xyz
                self.CoordinateSystem = extent.coordinate_system.xml

    def __str__(self):
        a = '[%s, %s, %s] - [%s, %s %s], %s'
        b = (self.MinX, self.MinY, self.MinZ, self.MaxX, self.MaxY, self.MaxZ, self.CoordinateSystem)
        return a % b

    def __repr__(self):
        a = 'BoundingBox(minx=%r,miny=%r,minz=%r,maxx=%r,maxy=%r,maxz=%r,coordinate_system=%r)'
        b = (self.MinX, self.MinY, self.MinZ, self.MaxX, self.MaxY, self.MaxZ, self.CoordinateSystem)
        return a % b


class DataCard(gxgeo.Geometry):
    """
    Single dataset information instance.

    :param dap:             `DapClient` instance
    :param id:              `Id` unique dataset identifier property
    :param title:           `Title` property
    :param type:            `Type` dataset type, one of `DataType` values.
    :param hierarchy:       `Hierarchy` location in the catalog hierarchy
    :param stylesheet:      `Stylesheet` metadata style sheet
    :param extents:         `Extents` is a `BoundingBox` instance
    :param has_original:    `HasOriginal` True if the original data is available

    .. versionadded:: 9.4
    """

    def __init__(self, dap=None, id=None, title=None, type=0, hierarchy=None, stylesheet=None, extents=None,
                 has_original=False):

        self._dap = dap

        if extents is None:
            extents = BoundingBox()
        self._extent = None

        self.Id = id
        self.Title = title
        self.Type = type
        self.Hierarchy = hierarchy
        self.Stylesheet = stylesheet
        self.Extents = extents
        self.HasOriginal = has_original
        super().__init__(name=title)

    def __str__(self):
        a = 'Id: %s, Title: %s, Type: %s, Hierarchy: %s'
        b = (self.Id, self.Title, self.Type, self.Hierarchy)
        return a % b

    def __repr__(self):
        a = 'Dataset(id=%r, title=%r, type=%r, hierarchy=%r, stylesheet=%r, has_original=%r)'
        b = (self.Id, self.Title, self.Type, self.Hierarchy, self.Stylesheet, self.HasOriginal)
        return a % b

    @property
    def dap_client(self):
        """
        `DapClient` instance for this dataset, may be None if card is not yet associated with a server.

        .. versionadded:: 9.4
        """
        return self._dap

    @dap_client.setter
    def dap_client(self, dap):
        self._dap = dap

    @property
    def extent(self):
        if self._extent is None:
            sp = self.spatial_properties
            p1 = (sp['NativeMinX'], sp['NativeMinY'], sp['NativeMinZ'])
            p2 = (sp['NativeMaxX'], sp['NativeMaxY'], sp['NativeMaxZ'])
            cs = gxcs.Coordinate_system(sp['CoordinateSystem'])
            self._extent = gxgeo.Point2((p1, p2), coordinate_system=cs)
        return self._extent

    @property
    def info(self):
        """
        Dataset info: http://dap.geosoft.com/REST/dataset/help/operations/GetDatasetById

        .. versionadded:: 9.4
        """

        return self._dap.post('dataset/info/' + str(self.Id))

    @property
    def edition(self):
        """
        Edition: http://dap.geosoft.com/REST/dataset/help/operations/GetEdition

        .. versionadded:: 9.4
        """

        return self._dap.get('dataset/edition/' + str(self.Id))

    @property
    def disclaimer(self):
        """
        Disclaimer: http://dap.geosoft.com/REST/dataset/help/operations/GetDisclaimer

        .. versionadded:: 9.4
        """

        return self._dap.get('dataset/disclaimer/' + str(self.Id))

    @property
    def permission(self):
        """
        Permission: http://dap.geosoft.com/REST/dataset/help/operations/GetPermission

        .. versionadded:: 9.4
        """

        return self._dap.get('dataset/permission/' + str(self.Id))

    @property
    def metadata(self):
        """
        Metadata: http://dap.geosoft.com/REST/dataset/help/operations/GetMetadata

        .. versionadded:: 9.4
        """

        return self._dap.get('dataset/metadata/' + str(self.Id))

    @property
    def grid_properties(self):
        """
        Grid data properties, `None` if not a grid dataset.

        http://dap.geosoft.com/REST/dataset/help/operations/GetGridProperties

        .. versionadded:: 9.4
        """
        if self.Type == DataType.Grid:
            return self._dap.get('dataset/properties/grid/' + str(self.Id))
        return None

    @property
    def document_properties(self):
        """
        Properties of the dataset as a document.

        http://dap.geosoft.com/REST/dataset/help/operations/GetDocumentProperties

        .. versionadded:: 9.4
        """
        try:
            return self._dap.get('dataset/properties/document/' + str(self.Id))
        except Exception:
            return None

    @property
    def point_properties(self):
        """
        Point properties, `None` if not a point (hxyz) dataset.

        http://dap.geosoft.com/REST/dataset/help/operations/GetHXYZProperties

        .. versionadded:: 9.4
        """
        if self.Type == DataType.Point:
            return self._dap.get('dataset/properties/hxyz/' + str(self.Id))
        return None

    @property
    def map_properties(self):
        """
        Map properties, `None` if not a map.

        http://dap.geosoft.com/REST/dataset/help/operations/GetMapProperties

        .. versionadded:: 9.4
        """
        if self.Type == DataType.Map:
            return self._dap.get('dataset/properties/map/' + str(self.Id))
        return None

    @property
    def voxel_properties(self):
        """
        Voxel properties, `None` if not a voxel.

        http://dap.geosoft.com/REST/dataset/help/operations/GetVoxelProperties

        .. versionadded:: 9.4
        """
        if self.Type == DataType.Voxel or self.Type == DataType.VectorVoxel:
            return self._dap.get('dataset/properties/voxel/' + str(self.Id))
        return None

    @property
    def spatial_properties(self):
        """
        Spatial properties: http://dap.geosoft.com/REST/dataset/help/operations/GetProperties

        .. versionadded:: 9.4
        """

        return self._dap.get('dataset/properties/' + str(self.Id))


class SearchFilter:
    """
    Search filter instance.

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
            extents = BoundingBox()

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
    Results filter instance.

    :param path:            to this location in the hierarchy
    :param depth:           to this depth in the hierarchy, default no depth limit
    :param start_index:     start index in the list
    :param max_results:     maximum results to include

    .. versionadded:: 9.4
    """

    def __init__(self, path=None, depth=2147483647, start_index=0, max_results=0, valid_path=False):
        self.Path = path
        self.Depth = depth
        self.StartIndex = start_index
        self.MaxResults = max_results
        if path is None:
            self.ValidPath = False
        else:
            self.ValidPath = True

    def __str__(self):
        return 'Path: %s, Depth: %s, StartIndex: %s, MaxResults: %s, ValidPath: %s' % (
        self.Path, self.Depth, self.StartIndex, self.MaxResults, self.ValidPath)

    def __repr__(self):
        return 'ResultFilter(path=%r,depth=%r,start_index=%r,max_results=%r,valid_path=%r)' % (
        self.Path, self.Depth, self.StartIndex, self.MaxResults, self.ValidPath)


class SearchParameters:
    """
    Search parameter instance, defined by a `SearchFilter` and a `ResultFilter`

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

class DapClient(Sequence):
    """
    DapClient class to communicate with a Geosoft DAP server.

    :param url:         url of the server, default is 'http://dap.geosoft.com/'
    :param get_catalog: `True` to get the server catalog.  If `False` (the default) call method `catalog()`
                        to get the retrieve the catalog from the server. The catalog is cached as
                        part of the instance.

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

    def __init__(self, url='http://dap.geosoft.com/', get_catalog=False):

        super().__init__()
        self._cat = []
        self._config = None
        self._http_headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        self._http_params = {'key': 'test'}

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
            raise DapClientException(_t('Server \'{}\' has a problem:\n{}'.format(self._url, str(e))))

        # dataset catalog
        if get_catalog:
            try:
                self.catalog()
            except exceptions.HTTPError as e:
                raise DapClientException(_t('Server \'{}\' has a problem:\n{}'.format(self._url, str(e))))

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

        card = None
        if not self._cat:
            self.catalog()
        if isinstance(item, int):
            if item < 0 or item >= len(self._cat):
                raise IndexError('catalog index {} out of range {}'.format(item, len(self._cat)))
            card = self._cat[item]
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
                    card = i
                    break
        if card:
            if card.dap_client is None:
                card.dap_client = self
            return card

        raise DapClientException('\'{}\' not found in catalog'.format(item))

    def _http_get(self, url, decoder=None, raw_content=False):

        response = get(self._rest_url + url,
                       params=self._http_params,
                       headers=self._http_headers)
        if (response.ok):
            if raw_content:
                return response.content
            else:
                return gxu.dict_from_http_response_text(response.text)
        else:
            response.raise_for_status()

    def _http_post(self, url, post_parameters=None, decoder=None):

        if post_parameters is not None:
            post_parameters = dumps(post_parameters, default=_json_default)

        response = post(self._rest_url + url,
                        data=post_parameters,
                        params=self._http_params,
                        headers=self._http_headers)

        if (response.ok):
            data = loads(response.content.decode('utf-8'), object_hook=decoder)
            return data
        else:
            response.raise_for_status()

    def datacard_from_id(self, id):
        """
        Return the `DataCard` instance based on the dataset ID #

        :param id: dataset id
        :return: `DataCard` instance

        .. versionadded:: 9.4
        """

        id = int(id)
        for card in self.catalog():
            if int(card.Id) == id:
                return card

        raise DapClientException('Id \'{}\' not found in catalog'.format(id))


    def get(self, what):
        """
        GET information from the server.

        :param what:    string of what to get. for example "dataset/properties/265" retrieves
                        the dataset properties for dataset 265.  See http://dap.geosoft.com/REST/dataset/help
                        for a list of the kinds of things you can get about a dataset.

        :return: requested info as a dict.
        """
        return self._http_get(what)

    def post(self, what):
        """
        POST information from the server.

        :param what:    string of what to post.

        :return: returned info as a dict.
        """
        return self._http_post(what)

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
            self._config = self._http_get('service/configuration')
        return self._config

    def catalog(self, search_parameters=None, refresh=False):
        """
        Return a filtered catalog list.

        :param search_parameters:   search filter, instance of `SearchParameters`
        :param refresh:             `True` to force a refresh, otherwise cached catalog is returned
        :return:                    list of server catalog entries as `DataCard` instances

        .. versionadded:: 9.4
        """

        if search_parameters is None:
            search_parameters = SearchParameters()

        if refresh or len(self._cat) == 0:
            self._cat = self._http_post('catalog/search', search_parameters, decoder=_decode_object)

        # assign this server to all cards
        for card in self._cat:
            card.dap_client = self

        return self._cat

    def fetch_data(self, datacard, filename=None, extent=None, resolution=None,
                   max_seconds=3600, progress=None, cadence=5):
        """
        Fetch data from the server.

        :param datacard:    `DataCard` instance, or a dataset description (hierarchy, title) or just title.
        :param filename:    file name in which to plase data, default is a temporary geosoft gris file.
        :param extent:      `geosoft.gxpy.geometry.Point2` instance, or a `BoundingBox` instance
        :param resolution:  data resolution in the length units of the extent coordinate system
        :param max_seconds: maximum number of seconds to wait for the process to finish
        :param progress:    callback that can report progress, for example `progress=print` will print to the console
        :param cadence:     time in seconds between checking on server preparation status.
        :return:            data file name, which may be a temporry file.  Temporary files will only persist
                            during the live of the current context.

        .. code::

            import geosoft.gxpy.gx as gx
            import geosoft.gxpy.dap_client as gxdap:

            gx.GXpy()

            with gxdap.DapClient() as dap:

                # some point data
                dataset = dap['Kimberlite Indicator Mineral Grain Chemistry']
                extent = gxgeo.Point2(((-112, 65), (-111, 65.5)), coordinate_system='NAD83')
                data_file = dap.fetch_data(dataset, extent=extent, resolution=0, progress=print)

        .. versionadded:: 9.4
        """

        if not isinstance(datacard, DataCard):
            datacard = self[datacard]

        if filename is None:
            filename = gx.gx().temp_file(DataType.datatype_default_extension(datacard.Type))
        folder, filename = os.path.split(filename)

        if resolution is None:
            url = 'dataset/extract/resolution/' + datacard.Id
            res = self._http_post(url, datacard.Extents)
            resolution = res['Default']

        pro = _t('\nFetching \'{}\'({}) from \'{}\' to file \'{}\'').\
            format(datacard.Title, datacard.Id, self._url, filename)
        gx.gx().log(pro)
        if progress:
            progress(pro)

        extract_parameters = DataExtract(extents=extent,
                                         resolution=resolution,
                                         filename=filename)

        urlx = DataType.extract_url(datacard.Type) + datacard.Id
        key = self._http_post(urlx, extract_parameters)
        time.sleep(1) # give it a second in case it is really fast

        url = 'dataset/extract/progress/' + key
        status = self._http_get(url)
        stage = status['Stage']
        seconds = 0
        while (stage != ExtractProgressStatus.Complete.value and
               stage != ExtractProgressStatus.Cancelled.value and
               seconds < max_seconds):
            if stage == ExtractProgressStatus.Failed.value:
                raise DapClientException(_t('Extraction failed, likely no data in this extent:\nurl: {}\nextract detail:\n{}').
                                         format(urlx, str(extract_parameters)))
            if progress:
                progress('{} {}%'.format(status['Message'], status['PercentComplete']))
            time.sleep(cadence)
            seconds += cadence
            status = self._http_get(url)
            stage = status['Stage']

        if stage == ExtractProgressStatus.Cancelled:
            return None

        info = self._http_get('dataset/extract/describe/' + key)
        zip_file = gx.gx().temp_file('zip')

        url = 'stream/dataset/extract/block/' + key + '/'
        with open(zip_file, 'wb') as out:  ## Open temporary file as bytes
            for index in range(info['NumberOfBlocks']):
                if progress:
                    progress(_t('Download block {} of {}').
                             format(index + 1, info['NumberOfBlocks']))
                out.write(self._http_get(url + str(index), raw_content=True))

        gxsys.unzip(zip_file, folder=folder)
        os.remove(zip_file)
        return_file = os.path.join(folder, filename)
        if not os.path.exists(return_file):
            raise DapClientException(_t('No result file, something went wrong.'))
        if progress:
            progress(_t('Fetch complete: {}').format(return_file))
        return return_file

    def fetch_image(self, datacard, extent=None, resolution=None):

        if not isinstance(datacard, DataCard):
            datacard = self[datacard]
            pass
