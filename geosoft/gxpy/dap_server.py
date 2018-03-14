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
import time
import os
from json import dumps, loads
from requests import get, post, exceptions
from enum import Enum
from collections.abc import Sequence

import geosoft
import geosoft.gxapi as gxapi
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


class DapServerException(geosoft.GXRuntimeError):
    """
    Exceptions from `geosoft.gxpy.dap`.
    """
    pass


class DataType(Enum):
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
                'pnd',  # 2
                'csv',  # 3
                'gdb',  # 4
                'docx',  # 5
                'spf',  # 6
                'Generic',  # 7
                'geosoft_voxel',  # 8
                'ArcGIS',  # 9
                'png',  # 10
                'PictureSection',  # 11
                'grd',  # 12
                'zip',  # 13
                'Drillhole',  # 14
                'NoData',  # 15
                '3dv',  # 16
                'geosoft_geostring',  # 17
                'GMSYS3D',  # 18
                'geosoft_voxi',  # 19
                'pdf',  # 20
                'geosoft_geosurface',  # 21
                'GMSYS2D',  # 22
                'geosoft_vector_voxel',  # 23
                'GeosoftOffline')  # 24
    return ext_list[item.value]


def datatype_extract_url(item):
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
    Extract data from the server.

    :param filename:    name of the data file
    :param extents:     data extent as a `BoundingBox` or `geosoft.gxpy.geopmetry.Point2` instance
    :param resolution:  desired resolution in the distance usins of the xtent coodinate system
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
        return 'GridExtract(extents=%r,filename=%r,resolution=%r,format=%r)' % (
        self.BoundingBox, self.Filename, self.Resolution, self.Format)


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


class DataCard:
    """
    Single dataset information instance.

    :param dap:             `Dap_server` instance
    :param id:              `Id`    unique identifier
    :param title:           `Title`
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
        self._has_properties = False

        if extents is None:
            extents = BoundingBox()

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

    @property
    def dap_server(self):
        """ `DapServer` instance for this dataset, may be None if card is not yet associated with a server."""
        return self._dap

    @dap_server.setter
    def dap_server(self, dap):
        self._dap = dap

    def get_extra_properties(self, refresh=False):
        """
        Get extra properties from the server.  The properties will become properties
        of this class instance, and these depend on the data type.  For example, all
        data types will have a `metadata` property and an `extents` property.

        :param refresh: `True` to force a property refresh from the server

        .. versionadded:: 9.4
        """

        def xprops(dt):
            return self._dap.get('dataset/properties/' + dt.lower() + '/' + str(self.Id))

        def get(d):
            props[d] = self._dap.get('dataset/' + d.lower() + '/' + str(self.Id))

        if refresh or not self._has_properties:
            self._has_properties = True

            props = {}
            # get('info') TODO: Ryan
            get('edition')
            get('extents')
            # get('legend') TODO Ryan
            get('metadata')
            get('disclaimer')
            get('permission')
            if self.Type == DataType.Grid:
                props['properties'] = xprops('grid')
            elif self.Type == DataType.Document:
                props['properties'] = xprops('document')
            elif self.Type == DataType.Point:
                props['properties'] = xprops('hxyz')
            elif self.Type == DataType.Map:
                props['properties'] = xprops('map')
            elif self.Type == DataType.Voxel:
                props['properties'] = xprops('voxel')
            else:
                props['properties'] = self._dap.get('dataset/properties/' + str(self.Id))

            self.__dict__ = {**self.__dict__, **props}


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
    :param get_catalog: `True` to get the server catalog.  If `False` (the default) the caller needs to call
                        method `catalog()` to get the data catalog from the server. The catalog is cached as
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
            if card.dap_server is None:
                card.dap_server = self
            return card

        raise DapServerException('\'{}\' not found in catalog'.format(item))

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

    def _http_post(self, url, post_parameters, decoder=None):

        response = post(self._rest_url + url,
                        data=dumps(post_parameters, default=_json_default),
                        params=self._http_params,
                        headers=self._http_headers)

        if (response.ok):
            data = loads(response.content.decode('utf-8'), object_hook=decoder)
            return data
        else:
            response.raise_for_status()

    def get(self, what):
        """
        Get information from the server.

        :param what:    string of what to get. for example "dataset/properties/265" retrieves
                        the dataset properties for dataset 265.  See http://dap.geosoft.com/REST/dataset/help
                        for a list of the kinds of things you can get about a dataset.

        :return: requested info as a dict.
        """
        return self._http_get(what)

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
            card.dap_server = self

        return self._cat

    def fetch_data(self, datacard, filename=None, extent=None, resolution=None,
                   max_seconds=3600, progress=None, cadence=5):
        """
        Fetch data from the server.

        :param datacard:    `DataCard` instance, or a dataset description (hierarchy, title) or just title.
        :param filename:    file name in which to plase data, default is a temporary geosoft gris file.
        :param extent:      `geosoft.gxpy.geometry.Point2` instance, or a `BoundingBox` instance
        :param resolution:  data resolution in the length usins of the extent coordinate system
        :param max_seconds: maximum number of seconds to wait for the process to finish
        :param progress:    callback that can report progress, for example `progress=print` will print to the console
        :param cadence:     time in seconds between checking on server preparation status.
        :return:            data file name, which may be a temporry file.  Temporary files will only persist
                            during the live of the current context.

        .. versionadded:: 9.4
        """

        if not isinstance(datacard, DataCard):
            datacard = self[datacard]

        if filename is None:
            filename = gx.gx().temp_file(datatype_default_extension(datacard.Type))
        folder, filename = os.path.split(filename)

        if resolution is None:
            url = 'dataset/extract/resolution/' + datacard.Id
            res = self._http_post(url, datacard.Extents)
            resolution = res['Default']

        if progress:
            progress(_t('\nFetching \'{}\'({}) from \'{}\' to file \'{}\'').
                     format(datacard.Title, datacard.Id, self._url, filename))

        extract_parameters = DataExtract(extents=extent,
                                         resolution=resolution,
                                         filename=filename)

        urlx = datatype_extract_url(datacard.Type) + datacard.Id
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
                raise DapServerException(_t('Extraction failed, likely no data in this extent:\nurl: {}\nextract detail:\n{}').
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
            raise DapServerException(_t('No result file, something went wrong.'))
        if progress:
            progress(_t('Fetch complete: {}').format(return_file))
        return return_file

    def fetch_image(self, datacard, extent=None, resolution=None):

        if not isinstance(datacard, DataCard):
            datacard = self[datacard]
            pass
