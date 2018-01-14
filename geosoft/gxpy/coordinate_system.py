"""
Coodinate systems

:Classes:

    ============================= ======================================================
    :class:`Coordinate_system`    define a coordinate system
    :class:`Coordinate_translate` translate coordinates between coordinate systems
    :class:`Wkt`                  well-know coordinate system for ESRI interoperability
    ============================= ======================================================

Coordinate systems describe how cartesian coordinates are located ralative to the Earth.  Cartesian coordinates
are right-handed (x, y, z) spatial ordinates that describe locations within a coordinate system frame of reference.
For coordinates relative to a horizontal plane, positive z is up, usually equivalent to elevation relative to
a vertical datum.

Coordinate systems can be oriented in three dimensions using an `orientation` definition, which defines an (x0, y0, z0)
origin and rotation (rx, ry, rz) around the X, Y and then Z axis relative to a base coordinate system.  

Base coordinate systems are usually defined by "well-known" coordinate system projections on a datum of the earth.

**Coordinate System Name**

A coordinate system will also have a descriptive name that identifies the base system with a datum and "well-known"
map projection description, plus optional orientation and vertical reference datum if defined.  Orientation
parameters are enclosed in `<>` that define `<x0, y0, z0, rx, ry, rz>` (eg. `<400000, 6200000,0,0,-90,0>`).
If a vertical reference datum is defined it will appear as a string in square brackets, for example  `[CGVD28]`.

Example coordinate system names:
    
    .. code::
    
        "NAD83 / UTM zone 15N"
        "NAD83 / UTM zone 15N <450000,6250000,0,0,0,-25>" # oriented system, rotated -25 degrees
        "NAD83 / UTM zone 15N [NAVD88]"
        "NAD83 / UTM zone 15N <450000,6250000,0,0,0,-25> [NAVD88]"

The descriptive name for "well-known" coordinate systems is sufficient to describe the coordinate system from
the `EPSG Geodetic Registry <http://www.epsg.org/>`_. To fully locate ad-hoc coordinates you will need
the parameters defined in the GXF stings.  See :attr:`Coordinate_system.gxf`.

.. seealso:: :class:`geosoft.gxapi.GXIPJ`

.. note::

    Regression tests provide usage examples:     
    `tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_coordinate_system.py>`_
"""

import json
import numpy as np
import geosoft
import geosoft.gxapi as gxapi
from . import utility as gxu
from . import dataframe as gxdf
from . import vv as gxvv

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


#############
# Constants

# 'HCS' and 'hcs' refer to Horizontal Coordinate System
# 'VCS' and 'vcs' refer to Vertical Coordinate System

NAME = None  #:
NAME_HCS = gxapi.IPJ_NAME_PCS  #:
NAME_PROJECTION = gxapi.IPJ_NAME_PROJECTION  #:
NAME_METHOD = gxapi.IPJ_NAME_METHOD  #:
NAME_DATUM = gxapi.IPJ_NAME_DATUM  #:
NAME_ELLIPSOID = gxapi.IPJ_NAME_ELLIPSOID  #:
NAME_LDATUM = gxapi.IPJ_NAME_LDATUM  #:
NAME_UNIT = gxapi.IPJ_NAME_UNIT_ABBR  #:
NAME_UNIT_FULL = gxapi.IPJ_NAME_UNIT_FULL  #:
NAME_TYPE = gxapi.IPJ_NAME_TYPE  #:
NAME_LLDATUM = gxapi.IPJ_NAME_LLDATUM  #:
NAME_METHOD_PARMS = gxapi.IPJ_NAME_METHOD_PARMS  #:
NAME_METHOD_LABEL = gxapi.IPJ_NAME_METHOD_LABEL  #:
NAME_DATUM_PARMS = gxapi.IPJ_NAME_DATUM_PARMS  #:
NAME_LDATUM_PARMS = gxapi.IPJ_NAME_LDATUM_PARMS  #:
NAME_GEOID = gxapi.IPJ_NAME_GEOID  #:
NAME_LDATUMDESCRIPTION = gxapi.IPJ_NAME_LDATUMDESCRIPTION  #:
NAME_METHOD_PARMS_NATIVE = gxapi.IPJ_NAME_METHOD_PARMS_NATIVE  #:
NAME_ORIENTATION = gxapi.IPJ_NAME_ORIENTATION_PARMS  #:
NAME_VCS = -1  #:
NAME_HCS_VCS = -2  #:

LIST_COORDINATESYSTEM = gxapi.IPJ_PARM_LST_COORDINATESYSTEM  #:
LIST_DATUM = gxapi.IPJ_PARM_LST_DATUM  #:
LIST_PROJECTION = gxapi.IPJ_PARM_LST_PROJECTION  #:
LIST_UNITS = gxapi.IPJ_PARM_LST_UNITS  #:
LIST_UNITSDESCRIPTION = gxapi.IPJ_PARM_LST_UNITSDESCRIPTION  #:
LIST_LOCALDATUMDESCRIPTION = gxapi.IPJ_PARM_LST_LOCALDATUMDESCRIPTION  #:
LIST_LOCALDATUMNAME = gxapi.IPJ_PARM_LST_LOCALDATUMNAME  #:

PARM_DATUM = 'datum'  #:
PARM_PROJECTION = 'transform'  #:
PARM_UNITS = 'units'  #:
PARM_LOCAL_DATUM = 'datumtrf'  #:


class CSException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.coordinate_system`.

    .. versionadded:: 9.2
    """
    pass


def parameters(what, key):
    """
    Get a dictionary of parameters for a coordinate system item.  Parameters are maintained in 
    csv coordinate system table files in the Geosoft Desktop Applications `csv` folder.

    :param what:
            | PARM_DATUM (from `datum.csv`)
            | PARM_PROJECTION (from `transform.csv`)
            | PARM_UNITS (from `units.csv`)
            | PARM_LOCAL_DATUM (from `datumtrf.csv`)
    :param key:     parameter key to find and return
    :raises CSException: if table or key not found.

    .. versionadded:: 9.2
    """

    try:
        dct = gxdf.table_record(what, key)
    except gxdf.DfException as e:
        raise CSException(str(e))
    return dct


def parameter_exists(what, key):
    """
    Test if a parameter set exists in a coordinate system table.
    
    :param what:    see :func:`parameters`
    :param key:     parameter key
    :returns:       True if table/key exists
    
    .. versionadded:: 9.2
    """
    try:
        parameters(what, key)
    except CSException:
        return False
    else:
        return True


def name_list(what, datum_filter=''):
    """
    Get a list of coordinate system names
    
    :param what:
            | LIST_COORDINATESYSTEM
            | LIST_DATUM
            | LIST_PROJECTION
            | LIST_UNITS
            | LIST_LOCALDATUMDESCRIPTION
            | LIST_LOCALDATUMNAME
            | LIST_UNITSDESCRIPTION

    :param datum_filter: name of a datum to filter results

    :returns: sorted list of names

    .. versionadded:: 9.2
    """

    lst = gxapi.GXLST.create(1000)
    gxapi.GXIPJ.get_list(what, datum_filter, lst)
    namelist = list(gxu.dict_from_lst(lst))
    namelist.sort(key=str.lower)
    return namelist


def _extract(s, frame):
    c1, c2, *_ = frame
    s = s.strip(' \t"\'')
    end = s.rfind(c2)
    if end > 1:
        start = s.rfind(c1)
        sub = s[start + 1: end]
        s = s[:start] + s[end+1:]
    else:
        sub = ''
    return s.strip(' \t"\''), sub.strip(' \t"\'')


def hcs_orient_vcs_from_name(name):
    """
    Split a full coordinate system name into its components. A name has the form "hcs <orient> [vcs]"
    :param name:
    :returns: hcs, orient, vcs

    .. versionadded:: 9.2
    """

    name, vcs = _extract(name, '[]')
    hcs, orient = _extract(name, '<>')

    return hcs, orient, vcs


def name_from_hcs_orient_vcs(hcs, orient=None, vcs=None):
    """
    Construct a coordinate system name from an hcs, orientation and vcs.  If orient or vcs are None or
    empty, the name will not include these parts.

    :param hcs:     horizontal coordinate system string
    :param orient:  orientation string
    :param vcs:     vertical coordinate system string
    :returns: "hcs <orient> [vcs]"

    .. versionadded:: 9.2
    """

    if orient:
        orient = ' <' + orient + '>'
    else:
        orient = ''

    if vcs:
        vcs = ' [' + vcs + ']'
    else:
        vcs = ''

    return hcs + orient + vcs


def list_from_wktsrs(wkt):
    """
    Return a list from a wkt spatial reference string.
    
    .. versionadded:: 9.2
    """

    def first_item(wkts):
        n = 0
        i = 0
        for c in wkts:
            if n == 0 and c == ',':
                return wkts[:i].strip(' '), wkts[i + 1:].strip(' ')
            i += 1
            if c == '[':
                n += 1
            elif c == ']':
                n -= 1
        return wkts.strip(' '), ''

    def parse_item(wkts):
        if wkts[0] == '"':
            return wkts[1:-1]

        if '[' in wkts:
            bkt = wkts.find('[')
            items = list_from_wktsrs(wkts[bkt + 1:-1])
            dct = {'key': wkts[:bkt], 'name': items[0]}
            if len(items) > 1:
                dct['items'] = items[1:]
            return dct

        return wkts

    wkt = wkt.strip()
    wktlst = []
    while wkt:
        first, wkt = first_item(wkt)
        wktlst.append(parse_item(first))

    return wktlst


def find_key(wkt, k):
    """
    Find a key in the wkt, return it's name and items.
    
    .. versionadded:: 9.2
    """

    for w in wkt:
        if type(w) is dict:
            if w['key'] == k:
                return w['name'], w.get('items', [])

            # try the kids
            name, items = find_key(w.get('items', []), k)
            if name:
                return name, items

    return '', []


def wkt_vcs(vcs):
    """
    Compose a wkt VERTCS block from a Geosoft vcs string.
    
    .. versionadded:: 9.2
    """
    return 'VERTCS["' + vcs + '"]'


class Wkt:
    """
    Helper class to parse WKT-formatted spatial reference strings.
    
    :param wkt: wkt (well-known text) string that describes a coordinate system.
    
    .. versionadded:: 9.2
    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __enter__(self):
        return self

    def __exit__(self, _type, _value, _traceback):
        pass

    def __init__(self, wkt):

        self._wkt = list_from_wktsrs(wkt)

        self.pcs, _ = find_key(self._wkt, 'PROJCS')
        self.gcs, _ = find_key(self._wkt, 'GEOGCS')
        self.vcs, _ = find_key(self._wkt, 'VERTCS')

    @property
    def name(self):
        """
        Return the ESRI coordinate system WKT string
        
        .. versionadded:: 9.2
        """

        if self.pcs:
            name = self.pcs
        else:
            name = self.gcs
        if self.vcs:
            name += ' [{}]'.format(self.vcs)

        return name.strip()

    def find_key(self, k):
        """
        Return the name and list of items for a key
        
        :param k:   the key to look for in the wkt
        :returns:   name ('' if not found), list of parameters, ([] if no items)
        
        .. versionadded:: 9.2
        """
        return find_key(self._wkt, k)


class Coordinate_system:
    """
    Coordinate system class. A coordinate system defines a horizontal and vertical reference
    system to locate (x, y, z) cartesian coordinates relative to the Earth.

    :param coordinate_system:  a coordinate system can be created from a number of different forms:
    
                - Geosoft name string (ie. "WGS 84 / UTM zone 32N [geodetic]")
                 
                - ESRI WKT string (ie. "PROJCS["WGS_1984_UTM_Zone_35N",GEOGCS[...")
                 
                - a dictionary that contains the coordinate system properties (see **Dictionary Structure** below.)
                  
                - a JSON string that contains the coordinate system properties
                  
                - a list that contains the 5 
                  `GXF coordinate system strings <http://www.geosoft.com/resources/goto/GXF-Grid-eXchange-File>`_.
                  For example: ``['"WGS 84 / UTM zone 32N [geodetic]", "WGS 84", "UTM zone 32N", "", ""]``
                
                - :class:`geosoft.gxapi.GXIPJ` instance
                 
                - :class:`Coordinate_system` instance, returns a copy

                - None to create an '*Unknown' coordinate system.
                
                For examples refer to
                `tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_coordinate_system.py>`_

    :Dictionary Structure:
    
        :Geosoft:       

            .. code::
    
                {   "type": "Geosoft",
                    "name": name
                    "datum": datum
                    "method": method
                    "units": units
                    "local_datum": local datum transform
                    "orientation": x0, y0, z0, xR, yR, zR
                    "vcs": "vertical coordinate system"
                }
            
            
        :local:
        
            type "local" can be used to locate local coordinates in situations where one only has
            the (longitude, latitude) of a point on local coordinate system and the orientation
            of the local axis relative to geographic North.  Internally an Oblique Stereographic 
            projection is created with an origin at the defined origin point.
        
            .. code::
                
                {   "type": "local",
                    "lon_lat": (lon, lat) required longitude, latitude of "origin", in degrees
                    "origin": (x0, y0) location of "lon_lat" on the local coordinate system, default is (0,0)
                    "azimuth": azimuth of rotation of local axiz relative to North.
                    "elevation": elevation of the origin in the vertical coordinate system, default is 0.
                    "datum": datum, default is "WGS 84"        
                    "local_datum": local datum transform, default is the default for the datum
                    "scale_factor": local scale factor, default is 0.9996 to be similar to UTM locally
                    "vcs": "vertical coordinate system" default is undefined.
                }

            :Example:
            
                cs = geosoft.gxpy.Coordinate_system({'type': 'local', 'lon_lat': (-96, 43), 'azimuth': 25})

        :EPSG: (http://www.epsg.org/)

            .. code::

                {   "type": "EPSG"
                    "code": EPSG_code_number
                    "orientation": x0, y0, z0, xR, yR, zR
                }

        :ESRI: (http://webhelp.esri.com/arcgisserver/9.3/java/index.htm#geodatabases/the_ogc-607957855.htm)

            .. code::

                {   "type": "ESRI",
                    "wkt": wkt format string, starts with "PROJCS[" or "GEOGCS["
                    "orientation": x0, y0, z0, xR, yR, zR
                    "vcs": "vertical coordinate system"
                }

    .. versionadded:: 9.2
        supercedes `ipj` module.
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
        if hasattr(self, '_gxapi_ipj'):
            self._gxapi_ipj = None

    def __init__(self, coordinate_system=None):

        self._dict = None
        self._gxapi_ipj = gxapi.GXIPJ.create()

        if coordinate_system is None:
            coordinate_system = '*unknown'

        if isinstance(coordinate_system, str):
            self._from_str(coordinate_system)

        elif isinstance(coordinate_system, gxapi.GXIPJ):
            s1 = gxapi.str_ref()
            s2 = gxapi.str_ref()
            s3 = gxapi.str_ref()
            s4 = gxapi.str_ref()
            s5 = gxapi.str_ref()
            coordinate_system.get_gxf(s1, s2, s3, s4, s5)
            self._from_gxf((s1.value, s2.value, s3.value, s4.value, s5.value))

        elif isinstance(coordinate_system, Coordinate_system):
            self._from_gxf(coordinate_system.gxf)

        elif isinstance(coordinate_system, dict):
            self._from_dict(coordinate_system)
        else:
            self._from_gxf(coordinate_system)

    def __eq__(self, other):
        return self.same_as(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def local(cls, lon_lat=(0, 0), origin=(0, 0), azimuth=0, elevation=0, datum="WGS 84",
              local_datum=None, scale_factor=0.9996, vcs=None):
        """
        Create an ad-hoc local coordinate system.

        :param lon_lat:         (longitude, latitude) of the center
        :param origin:          (x, y) to assign to the center
        :param azimuth:         local rotation of the system relative to geographic North, in degrees azimuth
        :param elevation:       elevation for z = 0.
        :param datum:           datum, default is "WGS 84"
        :param local_datum:     local datum, default will be the default for the specified datum
        :param scale_factor:    central scale factor. The default is 0.9996 as the most common map system
                                is UTM and thus relative distances in the local system will be similar,
                                though not the same, as UTM.
        :param vcs:             name for the vertical coordinate system reference, default is unknown

        Local coordinate systems are simple cartesian systems established for a specific purpose without
        complete geodetic control, but for which one knows or can estimate the longitude, latitude of a point
        on the local coordinate system. In this way local coordinates can be located reasonably well relative
        to the Earth and and other Earth-refeerenced data.

        The local system will be constructed as an oblique stereographic projection centered at the system
        origin, which is similar to what one sees when looking at maps in Google maps.

        .. versionadded:: 9.3.1
        """
        csdict = {'type': 'local',
                  'lon_lat':lon_lat,
                  'origin': origin,
                  'azimuth': azimuth,
                  'elevation': elevation,
                  'datum': datum,
                  'scale_factor': scale_factor}
        if local_datum:
            csdict['local_datum'] = local_datum
        if vcs:
            csdict['vcs'] = vcs

        return cls(csdict)

    @property
    def gxipj(self):
        """ :class:`geosoft.gxapi.GXIPJ` instance"""
        return self._gxapi_ipj

    @property
    def name(self):
        """ coordinate system name as 'datum / projection <orientation> [vcs]' """
        return self.gxf[0]

    @property
    def units_name(self):
        """ name of the distance units (abbreviation)"""
        return self.cs_name(NAME_UNIT)

    @property
    def unit_of_measure(self):
        """ same as units_name, provided for naming consistency with other usage in gxpy."""
        return self.units_name

    @property
    def metres_per_unit(self):
        """ the number metres per distance unit of the coordinate system."""
        fr = gxapi.float_ref()
        sr = gxapi.str_ref()
        self.gxipj.get_units(fr, sr)
        return fr.value

    @property
    def hcs(self):
        """ horizontal coordinate system name"""
        return self.cs_name(NAME_HCS)
                
    @property
    def vcs(self):
        """ Vertical coordinate system name.  Can be set."""
        return self.cs_name(NAME_VCS)

    @vcs.setter
    def vcs(self, vcs):
        self.gxipj.set_vcs(vcs)

    @property
    def is_oriented(self):
        """True if the coordinate system has an orientation."""
        return '<' in self.hcs

    @property
    def is_known(self):
        """
        True if this is a known coordinate system.

        .. versionadded:: 9.3
        """
        return self.name.lower() != '*unknown'

    def coordinate_dict(self):
        """
        Returns "Geosoft" dictionary of coordinate system attributes.

        .. versionadded:: 9.2
        """

        if self._dict is None:

            # initially from GXF values
            gxf1, gxf2, gxf3, gxf4, gxf5 = self.gxf
            hcs, orient, vcs = hcs_orient_vcs_from_name(gxf1)
            self._dict = {"type": "Geosoft",
                          "name": self.name,
                          "datum": gxf2,
                          "projection": gxf3,
                          "units": gxf4,
                          "local_datum": gxf5,
                          "orientation": orient,
                          "vcs": vcs
                          }

        return self._dict

    def same_hcs(self, other):
        """
        Return True if the HCS are the same.
        
        .. versionadded:: 9.2
        """
        def same_units(a, b):
            a = a.coordinate_dict()['units']
            b = b.coordinate_dict()['units']
            if not (a and b):
                return True
            else:
                return a == b

        def same_orientation(a, b):
            return a._dict['orientation'] == b._dict['orientation']

        if not same_units(self, other) or not same_orientation(self, other):
            return False
        if not(self.is_known) or not(other.is_known):
            return True
        else:
            return bool(self.gxipj.coordinate_systems_are_the_same(other.gxipj))

    def same_vcs(self, other):
        """
        Return True if the VCS are the same.
        
        .. versionadded:: 9.2
        """
        svcs = self.vcs
        ovcs = other.vcs
        if (svcs == '') or (ovcs == ''):
            return True
        else:
            return svcs == ovcs

    def same_as(self, other):
        """
        Return True if both coordinate systems (HCS and VCS) are the same. 
        
        .. versionadded:: 9.2
        """
        if other is None:
            return True
        if not isinstance(other, Coordinate_system):
            other = Coordinate_system(other)
        return self.same_hcs(other) and self.same_vcs(other)

    def _from_str(self, cstr):
        """
        Setup coordinate systems from a string.
        
        .. versionadded:: 9.2
        """
        
        # json string
        if cstr[0] == '{':
            try:
                jsondict = json.loads(cstr)
            except ValueError:
                # try replacing single quotes
                jstr = cstr.replace('"', '\\"').replace("'", '"')
                try:
                    jsondict = json.loads(jstr)
                except ValueError:
                    raise ValueError(_t('"Invalid JSON coordinate system string: "{}"').format(cstr))
                
            self._from_dict(jsondict)

        # ESRI WKT
        elif 'GEOGCS[' in cstr:
            self.gxipj.set_esri(cstr)
            vcs, _ = Wkt(cstr).find_key('VERTCS')
            if vcs:
                self.vcs = vcs

        else:
            self._from_gxf([cstr, '', '', '', ''])

    def _from_gxf(self, gxfs):

        def raise_gxf_error():
            raise CSException(_t('Unknown coordinate system:' +
                                 '\n       name> {}' +
                                 '\n      datum> {}' +
                                 '\n projection> {}' +
                                 '\n      units> {}' +
                                 '\nlocal datum> {}')
                              .format(gxfs[0], gxfs[1], gxfs[2], gxfs[3], gxfs[4]))

        gxf1, gxf2, gxf3, gxf4, gxf5 = gxfs
        hcs, orient, vcs = hcs_orient_vcs_from_name(gxf1)

        # if we get a name only, and it has a datum and projection, copy these.
        # The challenge with a name only is that the "datum / projection" must exist as
        # a known coordinate system, otherwise we cannot resolve it.  Users some times
        # combine projections with different datums so copying the values allows for this

        if (gxf2 == '') and (gxf3 == ''):
            if '/' in hcs:
                datum, projection, *_ = hcs.strip('"').split('/')
                gxf2 = datum.strip()
                gxf3 = projection.strip()
            else:
                gxf2 = hcs

        # units only
        if (gxf1 != '*unknown') and not (gxf3 or gxf4 or gxf5) and parameter_exists(PARM_UNITS, gxf1):
            self.gxipj.set_gxf('', '', '', gxf1, '')

        else:
            try:
                self.gxipj.set_gxf(gxf1, gxf2, gxf3, gxf4, gxf5)

            except (geosoft.gxapi.GXAPIError, geosoft.gxapi.GXError):
                raise_gxf_error()
            else:
                if gxf1 != "*unknown":
                    if ('*unknown' in self.name) and (gxf2 or gxf3 or gxf5):
                        raise_gxf_error()

    def _from_dict(self, csdict):
        """
        Create an IPJ from a dictionary.

        .. versionadded:: 9.2
        """

        cstype = csdict.get('type', '').lower()
        if (not cstype) or (cstype == 'geosoft'):
            s1, orient, vcs = hcs_orient_vcs_from_name(csdict.get('name', ''))
            orient = csdict.get('orientation', orient)
            vcs = csdict.get('vcs', vcs)
            s1 = name_from_hcs_orient_vcs(s1, orient, vcs)
            s2 = csdict.get('datum', '')
            s3 = csdict.get('projection', '')
            s4 = csdict.get('units', '')
            s5 = csdict.get('local_datum', '')
            self._from_gxf([s1, s2, s3, s4, s5])

        elif cstype == 'esri':
            wkt = csdict.get('wkt', None)

            if wkt is None:
                raise ValueError("'ESRI missing 'wkt' property.")
            
            # add vertical datum reference from dict if not in the wkt
            vcs = csdict.get('vcs', '')
            if vcs and ('VERTCS[' not in wkt):
                wkt += wkt_vcs(vcs)

            # clear any existing coordinate system - bug GX does not clear prior orientation
            self.gxipj.set_gxf('WGS 84 <0,0,0,0,0,0>', '', '', '', '')
            self.gxipj.set_esri(wkt)

            # add orientation and vcs
            orient = csdict.get('orientation', '')
            if orient or vcs:
                gxfs = self.gxf
                gxfs[0] = name_from_hcs_orient_vcs(gxfs[0], orient, vcs)
                self._from_gxf(gxfs)

        elif cstype == "epsg":
            code = csdict.get('code', None)
            if code is None:
                raise ValueError("'EPSG missing 'code' property.")
            orient = csdict.get('orientation', '')
            self._from_gxf([str(code) + orient, '', '', '', ''])

        elif cstype == 'local':
            # must at least have a latitude and longitude
            lon, lat = csdict.get('lon_lat', (None, None))
            if (lat is None) or (lon is None):
                raise CSException(_t("Local must define 'lon_lat' of the local origin."))
            x0, y0 = csdict.get('origin', (0, 0))
            azimuth = csdict.get('azimuth', 0.0)

            sf = csdict.get('scale_factor', 0.9996)
            units = csdict.get('units', 'm')
            datum = csdict.get('datum', 'WGS 84')
            ldatum = csdict.get('ldatum', '')
            elevation = csdict.get('elevation', 0.0)

            proj = '"Oblique Stereographic",{},{},{},0,0'.format(lat, lon, sf)
            vcs = csdict.get('vcs', '')
            if (azimuth == 0.0) and (elevation == 0.0):
                orient = ''
            else:
                orient = '0,0,{},0,0,{}'.format(elevation, azimuth)

            name = '{} / *Local({},{},{},{})'.format(datum, lat, lon, x0, y0)
            name_azimuth = name_from_hcs_orient_vcs(name, orient, vcs)
            self._from_gxf([name_azimuth, datum, proj, units, ldatum])

            if (x0 != 0) or (y0 != 0):
                xx0, yy0, _ = self.xyz_from_oriented(np.array((-x0, -y0, 0)))
                proj = '"Oblique Stereographic",{},{},{},{},{}'.format(lat, lon, sf, -xx0, -yy0)
                self._from_gxf([name, datum, proj, units, ldatum])

        else:
            raise ValueError("Projection type '{}' not supported.".format(cstype))

    @property
    def gxf(self):
        """
        The GXF string list from ipj. (http://www.geosoft.com/resources/goto/GXF-Grid-eXchange-File)
    
        The first string (gxf[0]) is the coordinate system name in the form:
             
             `datum / projection <x0,y0,z0,rx,ry,rz> [vcs]`
             
        The orientation parameters are between the '<>', and will be omitted if all 0.
        
        'vcs' is the vertical coordinate system, and is omitted if the vcs is undefined. 
    
        .. versionadded:: 9.2
        """

        s1 = gxapi.str_ref()
        s2 = gxapi.str_ref()
        s3 = gxapi.str_ref()
        s4 = gxapi.str_ref()
        s5 = gxapi.str_ref()
        self.gxipj.get_gxf(s1, s2, s3, s4, s5)
        lst = [s1.value.replace('"', '').strip(), s2.value, s3.value, s4.value, s5.value]
        return lst

    @gxf.setter
    def gxf(self, gxfs):
        self._from_gxf(gxfs)

    @property
    def esri_wkt(self):
        """
        ESRI Well-Known-Text (wkt) format coordinate string

        .. versionadded:: 9.3
        """
        sr = gxapi.str_ref()
        self._gxapi_ipj.get_esri(sr)
        return sr.value

    @esri_wkt.setter
    def esri_wkt(self, gxfs):
        self._from_str(gxfs)

    @property
    def json(self):
        """
        JSON formatted coordinate system string.

        .. versionadded:: 9.3
        """
        return json.dumps(self.coordinate_dict())

    @json.setter
    def json(self, json_str):
        self._from_str(json_str)

    def cs_name(self, what=NAME):
        """
        Return requested name.

        :param what:
                | NAME
                | NAME_HCS
                | NAME_VCS
                | NAME_HCS_VCS
                | NAME_PROJECTION
                | NAME_METHOD
                | NAME_DATUM
                | NAME_ELLIPSOID
                | NAME_LDATUM
                | NAME_UNIT
                | NAME_UNIT_FULL
                | NAME_TYPE
                | NAME_LLDATUM
                | NAME_METHOD_PARMS
                | NAME_METHOD_LABEL
                | NAME_DATUM_PARMS
                | NAME_LDATUM_PARMS
                | NAME_GEOID
                | NAME_LDATUMDESCRIPTION
                | NAME_METHOD_PARMS_NATIVE
                | NAME_ORIENTATION

        If 'what' is not specified, gxipj.NAME assumed, which returns the coordinate system display name.

        :returns: The name requested

        .. versionadded:: 9.2
        """

        s = gxapi.str_ref()
        if what == NAME:
            return self.gxf[0]
        else:
            csname, *_ = self.gxf
            hcs, orient, vcs = hcs_orient_vcs_from_name(csname)
            if what == NAME_HCS_VCS:
                return name_from_hcs_orient_vcs(hcs, orient, vcs)
            if what == NAME_HCS:
                return name_from_hcs_orient_vcs(hcs, orient, None)
            if what == NAME_VCS:
                return vcs
            if what == NAME_DATUM:
                return hcs.split('/')[0].strip()
            if what == NAME_PROJECTION:
                if '/' in hcs:
                    return hcs.split('/')[1].strip()
                else:
                    return ''

            self.gxipj.get_name(what, s)
            return s.value

    def _oriented_xyz(self, direction, xyz, column_ordered=False):
        """
        Return oriented (x, y, z) coordinates from true base (x, y, z) coordinates.

        :param xyz:             (x, y, z) or iterable
        :param column_ordered:  if xyz is iterable, and this is True, the data is assumed to be
                                column ordered and the results are returned column ordered.
        :returns:               (x, y, z) in un-oriented space

        .. versionadded:: 9.2
        """

        if not isinstance(xyz, np.ndarray):
            xyz = np.array(xyz)

        if xyz.ndim == 1:
            x = (xyz[0],)
            y = (xyz[1],)
            z = (xyz[2],)
        else:
            if column_ordered:
                x, y, z = xyz[0, :], xyz[1, :], xyz[2, :]
            else:
                x, y, z = xyz[:, 0], xyz[:, 1], xyz[:, 2]

        x = gxvv.GXvv(x, dtype=float)
        y = gxvv.GXvv(y, dtype=float)
        z = gxvv.GXvv(z, dtype=float)

        self.gxipj.convert_orientation_warp_vv(x.gxvv, y.gxvv, z.gxvv, direction)

        if xyz.ndim == 1:
            return x[0][0], y[0][0], z[0][0]
        else:
            xyz_column = np.array([x.np, y.np, z.np])
            if column_ordered:
                return xyz_column
            else:
                return xyz_column.swapaxes(0, 1)

    def oriented_from_xyz(self, xyz, column_ordered=False):
        """
        Return oriented (x, y, z) coordinates from true base (x, y, z) coordinates.

        :param xyz:             (x, y, z) or iterable
        :param column_ordered:  if xyz is iterable, and this is True, the data is assumed to be
                                column ordered and the results are returned column ordered.
        :returns:               (x, y, z) in un-oriented space

        .. versionadded:: 9.2
        """
        return self._oriented_xyz(0, xyz, column_ordered=column_ordered)

    def xyz_from_oriented(self, xyz, column_ordered=False):
        """
        Return true base (x, y, z) coordinates from oriented (x, y, z) coordinates.

        :param xyz:             (x, y, z) or iterable
        :param column_ordered:  if xyz is iterable, and this is True, the data is assumed to be
                                column ordered and the results are returned column ordered.
        :returns:               (x, y, z) in oriented space

        .. versionadded:: 9.2
        """
        return self._oriented_xyz(1, xyz, column_ordered=column_ordered)


class Coordinate_translate:
    """
    Class to reproject coordinates between different coordinate systems.

    :params cs_from:  from :class:`Coordinate_system`
    :params cs_to:    to :class:`Coordinate_system`

    .. versionadded:: 9.2
    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "PJ from \'{}\' to \'{}\'".format(str(self._cs_from), str(self._cs_to))

    def __enter__(self):
        return self

    def __exit__(self, xtype, value, traceback):
        pass

    _cs_from = None
    _cs_to = None
    _sr = gxapi.str_ref()

    def __init__(self, cs_from, cs_to):
        if not isinstance(cs_from, Coordinate_system):
            cs_from = Coordinate_system(cs_from)
        self._cs_from = cs_from
        if not isinstance(cs_to, Coordinate_system):
            cs_to = Coordinate_system(cs_to)
        self._cs_to = cs_to
        self._pj = gxapi.GXPJ.create_ipj(cs_from.gxipj, cs_to.gxipj)

    def convert_vv(self, xvv, yvv, zvv=None):
        """
        Project vv locations in-place.

        :param xvv:     x locations as `geosoft.gxpy.vv.GXvv` instance
        :param yvv:     y locations as `geosoft.gxpy.vv.GXvv` instance
        :param zvv:     optional z locations as `geosoft.gxpy.vv.GXvv` instance

        .. versionadded:: 9.3.1
        """

        xvvin = yvvin = zvvin = None
        if not xvv.is_float64:
            xvvin = xvv
            xvv = gxvv.GXvv(xvv, dtype=np.float64)
        if not yvv.is_float64:
            yvvin = yvv
            yvv = gxvv.GXvv(yvv, dtype=np.float64)
        if zvv and not zvv.is_float64:
            zvvin = zvv
            zvv = gxvv.GXvv(zvv, dtype=np.float64)

        if zvv:
            self._pj.convert_vv3(xvv.gxvv, yvv.gxvv, zvv.gxvv)
        else:
            self._pj.convert_vv(xvv.gxvv, yvv.gxvv)

        if xvvin:
            xvvin.set_data(xvv)
        if yvvin:
            yvvin.set_data(yvv)
        if zvvin:
            zvvin.set_data(zvv)

    def convert(self, xyz, in_place=False):
        """
        Project data in array in which first columns are x,y or x,y,z.

        Coordinates are reprojected in-place.

        :param xyz: numply shape (n,2) or (n,3+), or list, or a single (x, y, z) tuple.
                    Array dimension (n,2) for (x, y), (n,3+) for x,y,z.
                    Only numpy arrays may have dimensions above 3.
        :param in_place: if True, numpy array data is converted in-place.  Ignored for list or tuple

        :example:
            Given an array shape (500,6), which represents 500 data records with 6 columns
            in which the first 3 columns are coordinates X, Y and Z.

            .. code::

                data = np.zeros((10,5), dtype='float') #then fill the array with some data

                xy_only = pj.convert(data[:,2])     #transform x,y
                xyz_only = pj.convert(data[:,3])    #transform x,y and z
                all = pj.convert(data)              #transform x,y and z with data returned
                
        :returns:   projected data in the same form as passed (numpy array, list, or (x,y,z))

        .. versionadded:: 9.2

        .. versionchanged:: 9.3.1 conversion methods will return results in the same type as the input data.
        """

        xyz_in = xyz
        if not isinstance(xyz, np.ndarray):
            xyz = np.array(xyz)
        npoints = xyz.shape[0]

        if npoints == 0:
            if in_place:
                return xyz
            if isinstance(xyz, np.ndarray):
                return np.array([[]])
            return [[]]

        if xyz.ndim < 2:
            xyz = xyz.reshape((-1, xyz.shape[0]))
            flatten_return = True
        else:
            flatten_return = False
        nd = xyz.shape[1]
        if nd < 2:
            raise CSException(_t('Data must have dimension 2 (x,y) or 3 for (x,y,z) or higher.'))

        vvx = gxvv.GXvv(xyz[:, 0])
        vvy = gxvv.GXvv(xyz[:, 1])
        if nd >= 3:
            vvz = gxvv.GXvv(xyz[:, 2])
        else:
            vvz = None
        self.convert_vv(vvx, vvy, vvz)

        if in_place:
            xyz[:, 0] = vvx.np
            xyz[:, 1] = vvy.np
            if nd > 2:
                xyz[:, 2] = vvz.np
            return xyz

        if nd >= 3:
            xyz = np.array([vvx.np, vvy.np, vvz.np]).T
        else:
            xyz = np.array([vvx.np, vvy.np]).T

        if flatten_return:
            xyz = xyz.flatten()

        if isinstance(xyz_in, np.ndarray):
            return xyz

        elif hasattr(xyz_in, '__iter__'):
            return list(xyz)

        if nd >= 3:
            return xyz[0, 0], xyz[0, 1], xyz[0, 2]
        else:
            return xyz[0, 0], xyz[0, 1]
