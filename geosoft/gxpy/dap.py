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
import os
import numpy as np
import json
import requests
from enum import Enum
from collections.abc import Sequence

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import coordinate_system as gxcs
from . import vv as gxvv
from . import utility as gxu
from . import spatialdata as gxspd
from . import geometry as gxgm

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class DapException(geosoft.GXRuntimeError):
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


class BoundingBox:
    def __init__(self, minx=-180, miny=-90, minz=0, maxx=180, maxy=90, maxz=0,
                 coordinate_system='<?xml version="1.0" encoding="UTF-8"?><projection type="GEOGRAPHIC" name="WGS 84" ellipsoid="WGS 84" datum="WGS 84" wellknown_epsg="4326" datumtrf="WGS 84" datumtrf_description="[WGS 84] World" radius="6378137" eccentricity="0.08181919084" xmlns="http://www.geosoft.com/schema/geo"><shift x="0" y="0" z="0"/><units name="dega" unit_scale="1"/></projection>'):
        self.MinX = minx
        self.MinY = miny
        self.MinZ = minz
        self.MaxX = maxx
        self.MaxY = maxy
        self.MaxZ = maxz
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
    def __init__(self, id=None, title=None, type=0, hierarchy=None, stylesheet=None, extents=BoundingBox(),
                 has_original=False):
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
    def __init__(self, free_text_query=None, structured_metadata_query=None, extents=BoundingBox(),
                 entirely_within=False, version=1):
        self.FreeTextQuery = free_text_query
        self.StructuredMetadataQuery = structured_metadata_query
        self.BoundingBox = extents
        self.EntirelyWithin = entirely_within
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

def jsonDefault(o):
    return o.__dict__

def decodeObject(o):
    if 'CoordinateSystem' in o:
        b = BoundingBox()
        b.__dict__.update(o)
        return b
    else:
        d = Dataset()
        d.__dict__.update(o)
        d.Type = DatasetType(d.Type)
        return d


class ResultFilter:
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
    def __init__(self, search_filter=SearchFilter(), result_filter=ResultFilter()):
        self.SearchFilter = search_filter
        self.ResultFilter = result_filter

    def __str__(self):
        return 'SearchFilter: %s, ResultFilter: %s' % (self.SearchFilter, self.ResultFilter)

    def __repr__(self):
        return 'SearchParameters(search_filter=%r,result_filter=%r)' % (self.SearchFilter, self.ResultFilter)

class Dap(Sequence):
    """
    Dap class.

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
        if len(self._cat) > 0:
            return '{}({} datasets)'.format(self._url, len(self._cat))
        return self._url

    def __init__(self, url='http://dap.geosoft.com/', get_catalog=True):

        super().__init__()

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

        # dataset catalog
        self._cat = []
        if get_catalog:
            try:
                self.catalog()
            except requests.exceptions.HTTPError as e:
                raise DapException(_t('Server \'{}\' has a problem:\n{}'.format(self._url, str(e))))

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

    def _search(self, search_parameters=None):

        if search_parameters is None:
            search_parameters = SearchParameters()

        search_url = self._rest_url + 'catalog/search?key=test'

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.post(search_url, data=json.dumps(search_parameters, default=jsonDefault), headers=headers)
        if (response.ok):
            data = json.loads(response.content, object_hook=decodeObject)
            return data
        else:
            response.raise_for_status()

    @property
    def url(self):
        """ Server url."""
        return self._url

    def catalog(self, search_filter=None, refresh=False):
        """
        Return a filtered catalog list.

        :param filter:  search filter
        :param refresh: force a refresh
        :return:        list of server catalog entries

        .. versionadded:: 9.4
        """
        if refresh or len(self) == 0:
            self._cat = self._search(search_filter)
        return self._cat
