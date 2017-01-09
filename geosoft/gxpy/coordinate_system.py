import json
import geosoft
import geosoft.gxapi as gxapi
from . import utility as gxu

__version__ = geosoft.__version__


# translation hook
def _(s):
    return s

#############
# Constants

NAME = None
NAME_PCS = gxapi.IPJ_NAME_PCS
NAME_PROJECTION = gxapi.IPJ_NAME_PROJECTION
NAME_METHOD = gxapi.IPJ_NAME_METHOD
NAME_DATUM = gxapi.IPJ_NAME_DATUM
NAME_ELLIPSOID = gxapi.IPJ_NAME_ELLIPSOID
NAME_LDATUM = gxapi.IPJ_NAME_LDATUM
NAME_UNIT = gxapi.IPJ_NAME_UNIT_ABBR
NAME_UNIT_FULL = gxapi.IPJ_NAME_UNIT_FULL
NAME_TYPE = gxapi.IPJ_NAME_TYPE
NAME_LLDATUM = gxapi.IPJ_NAME_LLDATUM
NAME_METHOD_PARMS = gxapi.IPJ_NAME_METHOD_PARMS
NAME_METHOD_LABEL = gxapi.IPJ_NAME_METHOD_LABEL
NAME_DATUM_PARMS = gxapi.IPJ_NAME_DATUM_PARMS
NAME_LDATUM_PARMS = gxapi.IPJ_NAME_LDATUM_PARMS
NAME_GEOID = gxapi.IPJ_NAME_GEOID
NAME_LDATUMDESCRIPTION = gxapi.IPJ_NAME_LDATUMDESCRIPTION
NAME_METHOD_PARMS_NATIVE = gxapi.IPJ_NAME_METHOD_PARMS_NATIVE
NAME_ORIENTATION = gxapi.IPJ_NAME_ORIENTATION_PARMS

LIST_COORDINATESYSTEM = gxapi.IPJ_PARM_LST_COORDINATESYSTEM
LIST_DATUM = gxapi.IPJ_PARM_LST_DATUM
LIST_PROJECTION = gxapi.IPJ_PARM_LST_PROJECTION
LIST_UNITS = gxapi.IPJ_PARM_LST_UNITS
LIST_UNITSDESCRIPTION = gxapi.IPJ_PARM_LST_UNITSDESCRIPTION
LIST_LOCALDATUMDESCRIPTION = gxapi.IPJ_PARM_LST_LOCALDATUMDESCRIPTION
LIST_LOCALDATUMNAME = gxapi.IPJ_PARM_LST_LOCALDATUMNAME


class CSException(Exception):
    '''
    Exceptions from this module.

    .. versionadded:: 9.2
    '''
    pass


def names(what, datum_filter=''):
    """
    Get a list of coordinate system names

    :param what:
            | gxipj.LIST_COORDINATESYSTEM
            | gxipj.LIST_DATUM
            | gxipj.LIST_PROJECTION
            | gxipj.LIST_UNITS
            | gxipj.LIST_LOCALDATUMDESCRIPTION
            | gxipj.LIST_LOCALDATUMNAME
            | gxipj.LIST_UNITSDESCRIPTION

    :param datum_filter:
            name of a datum to filter results

    :returns:   sorted list of names

    .. versionadded:: 9.2
    """

    lst = gxapi.GXLST.create(1000)
    gxapi.GXIPJ.get_list(what, datum_filter, lst)
    namelist = list(gxu.dict_from_lst(lst).keys())
    namelist.sort(key=str.lower)
    del lst
    return namelist


class GXcs():
    """
    Coordinate system class. A coordinate system defines a horizontal and vertical reference
    system to locate (x, y, z) cartesian coordinates relative to the Earth.

    :param vcs:     The vertical coordinate as a descriptive name.
    :param hcs:     The horizontal coordinate system as a Geosoft name string (ie. "WGS 84 / UTM zone 32N")
                    an ESRI WKT string (ie. "PROJCS["WGS_1984_UTM_Zone_35N",GEOGCS[..."), a dictionary that
                    contains the coordinate system properties, a JSON string that contains the coordinate
                    system properties, or a list that contains the 5 GXF coordinate system strings.

    Dictionary and JSON string keys are defined as follows:

        :LocalGrid:

            A local grid requires only the latitude and longitude of the local grid
            origin, though generally an azimuth of rotation the local grid axis with
            respect to true North is generally expected.  Other properties may also be
            specified if further detail is known or desired.
            An "Oblique Stereographic" coordinate system is constructed centred
            on the local grid origin such that the stereographic plan touches the
            elipsoid of the earth at that point.  The "scalefactor" can be used to
            adjust for intended area of use.  The default scale factor ensures
            length units are comparable to UTM length units (0.9996).

            .. code::

                {   "type": "LocalGrid"
                    "properties": {
                        "latitude": value or string in form "(+/-) deg.mm.ss.ss (N/S)"
                        "longitude: value or string
                        "azimuth": value (rotation in degrees azimuth, default is 0.0)
                        "elevation": value (elevation of map plane, default is 0.0)
                        "datum": string (name of the datum, default is "WGS 84")
                        "ldatum": string (local datum transform, default determined from datum)
                        "units": string (unit name, default is "m")
                        "scalefactor": value (central scale factor, default is 0.9996)
                     }
                }

        :EPSG: (http://spatialreference.org/)

            .. code::

                {   "type": "EPSG"
                    "properties": {
                        "code": EPSG_code_number
                    },
                    "orientation": "<x0,y0,z0,xR,yR,zR>"
                }

        :Geosoft: (http://www.geosoft.com/resources/goto/GXF-Grid-eXchange-File)

            .. code::

                {   "type": "Geosoft",
                    "properties": {
                        "name": name
                        "datum": datum
                        "method": method
                        "units": units
                        "local_datum": local datum transform
                    },
                    "orientation": "<x0,y0,z0,xR,yR,zR>"
                }

            See see http://www.geosoft.com/resources/goto/GXF-Grid-eXchange-File for GXF string reference

        :ESRI: (http://webhelp.esri.com/arcgisserver/9.3/java/index.htm#geodatabases/the_ogc-607957855.htm)

            .. code::

                {   "type": "ESRI",
                    "properties": {
                        "wkt": wkt format string, starts with "PROJCS[" or "GEOGCS["
                    },
                    "orientation": "<x0,y0,z0,xR,yR,zR>"
                }

        :"orientation":

            .. note::

                Only orientations of "<0, 0, 0, 0, 0, 0>" are currently supported.  Oriented coordinate
                systems will be added at some point in the future.

            *FUTURE:* In Geosoft coordinate systems, a cartesian system can be oriented arbitrarily
            in three dimensions relative to a base coordinate system.  This requires the definition
            of the local origin location on the base system, and the rotation in degrees clockwise
            (azimuth in plan view) around each of the three base system axis, as defined by the
            "orientation" description, which is a set of 6 values within angle brackets:

            .. code::

                "<oX,oY,oZ,rX,rY,rX>"

            The orientation string can be appended to the name, or added as it's own key "orientation"

            For example, a local grid with origin at (550000,6250000) rotated at azimuth 15 degrees
            (clockwise) from the base "UTM zone 15N" Northings and Eastings on "WGS 84" would be:

            .. code::

                {"type":"Geosoft","properties":{"name":"WGS 84 / UTM zone 15N <550000,6250000,0,0,0,15>"}}

            or:

            .. code::

                {"type":"Geosoft","properties":{"name":"WGS 84 / UTM zone 15N"},
                                                "orientation":"<550000,6250000,0,0,0,15>"}

    .. versionadded:: 9.2
        supercedes `ipj` module.
    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __init__(self, hcs=None, vcs=None):
        self._init_ipj = hcs
        self._gxapi_ipj = None
        self._vcs = vcs
        self._dict = None

    def __eq__(self, cs):
        if self.gxipj is None:
            return cs.gxipj is None
        if cs.gxipj is None:
            return self.gxipj is None
        return self.gxipj.coordinate_systems_are_the_same_within_a_small_tolerance(cs.gxipj)
        
    @property
    def gxipj(self):
        """ gxapi.GXIPJ instance """
        if self._gxapi_ipj is None:
            self._setup_ipj()
        return self._gxapi_ipj
    
    def _setup_ipj(self):
        """ Setup the horizontal coordinate system. """
        if self._gxapi_ipj is None:
            self._gxapi_ipj = gxapi.GXIPJ.create()
            if self._init_ipj is not None:
                if isinstance(self._init_ipj, str):
                    self._from_str(self._init_ipj)
                elif isinstance(self._init_ipj, dict):
                    self._from_dict(self._init_ipj)
                else:
                    self._from_gxf(self._init_ipj)

    @property
    def hcs(self):
        """ horizontal coordinate system as a json string """
        return(self.to_json())
                
    @property
    def vcs(self):
        """ vertical coordinate system as a string """
        return(self._vcs)

    def _from_str(self, cstr):
        """ setup coordinate systems from a string """
        
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
                    raise ValueError("Invalid JSON coordinate system string <{}>".format(cstr))
                
            self._from_dict(jsondict)

        # ESRI WKT
        elif 'GEOGCS[' in cstr:
            self.gxipj.set_esri(cstr)

        else:
            self._from_gxf([cstr.strip(' \t"\''), '', '', '', ''])

            

    def _from_gxf(self, gxfs):

        # if we get a name only, and it has a datum and projection, copy these.
        # The challenge with a name only is that the "datum / projection" must exist as
        # a known coordinate system, otherwise we cannot resolve it.  Users some times
        # combine projections with different datums so copying the values allows for this

        if (gxfs[1] == '') and (gxfs[2] == '') and ('/' in gxfs[0]):
            dp = gxfs[0].strip('"').split('/')
            gxfs[1] = dp[0].strip()
            orient = dp[1].find('<')
            if orient == -1:
                gxfs[2] = dp[1].strip()
            else:
                gxfs[2] = dp[1][0:orient].strip()

        # get ipj from gxf, error if unknown
        sref = gxapi.str_ref()
        self.gxipj.set_gxf(gxfs[0], gxfs[1], gxfs[2], gxfs[3], gxfs[4])
        self.gxipj.get_display_name(sref)
        if sref.value == '*unknown':
            raise CSException(_('Unknown coordinate system:\n>{}\n>{}\n>{}\n>{}\n>{}').format(
                gxfs[0],
                gxfs[1],
                gxfs[2],
                gxfs[3],
                gxfs[4]))

    def _from_dict(self, csdict):
        """
        Create an IPJ from a string, which can be a valid coordinate system name string or a JSON
        format string that defines the coordinate system type and properties as follows:

        .. versionadded:: 9.2
        """

        cstype = csdict.get('type', None)
        properties = csdict.get('properties', {})
        orientation = csdict.get('orientation', '')
        if orientation == '':
            orientation = properties.get('orientation', '')

        if cstype is None or properties is None:
            raise ValueError("Missing 'type' and/or 'properties' keys.")

        cstype = cstype.lower()
        if cstype == 'geosoft':
            s1 = properties.get('name', '')
            if s1.find('<') == -1:
                s1 = s1 + orientation
            s2 = properties.get('datum', '')
            s3 = properties.get('projection', '')
            s4 = properties.get('units', '')
            s5 = properties.get('local_datum', '')
            self._from_gxf([s1, s2, s3, s4, s5])

        elif cstype == 'esri':
            wkt = properties.get('wkt', None)
            if wkt is None:
                raise ValueError("'ESRI missing 'wkt' property.")

            # clear any existing coordinate system (bug GX does not clear prior orientation)

            self.gxipj.set_gxf('WGS 84 <0,0,0,0,0,0>', '', '', '', '')
            self.gxipj.set_esri(wkt)

            # add orientation
            if len(orientation) > 0:
                gxfs = self.to_gxf()
                gxfs[0] = gxfs[0] + orientation
                self._from_gxf(gxfs)

        elif cstype == "epsg":
            code = properties.get('code', None)
            if code is None:
                raise ValueError("'EPSG JSON string missing 'code' property.")
            self._from_gxf([str(code) + orientation, '', '', '', ''])

        elif cstype == 'localgrid':
            # must at least have a latitude and longitude
            lat = properties.get('latitude', None)
            lon = properties.get('longitude', None)
            if (lat is None) or (lon is None):
                raise ValueError("'Localgrid must define latitude and longitude properties of the local origin.")
            sf = properties.get('scalefactor', 0.9996)

            datum = properties.get('datum', 'WGS 84')
            proj = '"Oblique Stereographic",' + str(lat) + ',' + str(lon) + ',' + str(sf) + ',0,0'.replace('"', '\\"')
            units = properties.get('units', 'm')
            ldatum = properties.get('ldatum', '')
            azimuth = properties.get('azimuth', 0.0)
            elevation = properties.get('elevation', 0.0)
            if (azimuth == 0.0) and (elevation == 0.0):
                orient = ''
            else:
                orient = '<0,0,' + str(elevation) + ',0,0,' + str(azimuth) + '>'

            # construct a name
            name = datum + ' / *Local grid [' + str(lat) + ',' + str(lon) + ']' + orient
            self._from_gxf([name, datum, proj, units, ldatum])

        else:
            raise ValueError("Projection type '{}' not supported.".format(cstype))


    @property
    def coordinate_dict(self):
        """
        Dictionary of coordinate system attributes.

        .. versionadded:: 9.2
        """

        if self._dict is None:

            # initially from GXF values
            gxfs = self.to_gxf()
            gxf_dict = {"type": "Geosoft",
                        "properties": {
                            "name": gxfs[0],
                            "datum": gxfs[1],
                            "projection": gxfs[2],
                            "units": gxfs[3],
                            "local_datum": gxfs[4]}}

            # break out names
            name_dict = {'name': gxf_dict['properties']['name'].replace('"', ' ').strip()}
            parts = name_dict['name'].partition('<')
            if parts[2] == '':
                name_dict['orientation'] = '<0,0,0,0,0,0>'
            else:
                name_dict['orientation'] = '<' + parts[2].strip()
            name_dict['baseName'] = parts[0].strip()
            parts = parts[0].partition('/')
            name_dict['datumName'] = parts[0].strip()
            name_dict['projectionName'] = parts[2].strip()
            name_dict['projectionType'] = gxf_dict['properties']['projection'].split(',', 1)[0].replace('"', '')
            name_dict['unitName'] = gxf_dict['properties']['units'].split(',', 1)[0].replace('"', '')
            name_dict['localDatumName'] = gxf_dict['properties']['local_datum'].split(',', 1)[0].replace('"', '')

            # merge the dicts
            self._dict = dict(list(name_dict.items()) + list(gxf_dict.items()))

        return self._dict

    def to_gxf(self):
        """
        Get GXF string list from ipj.
        Returns list of 5 GXF strings.

        .. versionadded:: 9.2
        """

        s1 = gxapi.str_ref()
        s2 = gxapi.str_ref()
        s3 = gxapi.str_ref()
        s4 = gxapi.str_ref()
        s5 = gxapi.str_ref()
        self.gxipj.get_gxf(s1, s2, s3, s4, s5)
        lst = [s1.value.replace('"', ' ').strip(), s2.value, s3.value, s4.value, s5.value]
        return lst

    def to_json(self):
        """
        Return a JSON formatted projection in the form:

        .. code::

            {
               "baseName": "DHDN / Okarito 2000",
               "datumName": "DHDN",
               "localDatumName": "DHDN to WGS 84 (1)",
               "name": "DHDN / Okarito 2000 <25000,1000000,50,90,0,15>",
               "orientation": "<25000,1000000,50,90,0,15>",
               "projectionName": "Okarito 2000",
               "projectionType": "Transverse Mercator",
               "properties": {
                  "datum": "DHDN,6377397.155,0.0816968312225275,0",
                  "local_datum": "\"DHDN to WGS 84 (1)\",582,105,414,1.04,0.35,-3.08,8.29999999996112",
                  "name": "DHDN / Okarito 2000 <25000,1000000,50,90,0,15>",
                  "projection": "\"Transverse Mercator\",-43.11,170.260833333333,1,400000,800000",
                  "units": "m,1"
               },
               "type": "Geosoft",
               "unitName": "m"
            }

        .. versionadded:: 9.2
        """
        return json.dumps(self.coordinate_dict)

    def name(self, what=None):
        """
        Return requested name.

        :param what:
                | gxipj.NAME
                | gxipj.NAME_PCS
                | gxipj.NAME_PROJECTION
                | gxipj.NAME_METHOD
                | gxipj.NAME_DATUM
                | gxipj.NAME_ELLIPSOID
                | gxipj.NAME_LDATUM
                | gxipj.NAME_UNIT
                | gxipj.NAME_UNIT_FULL
                | gxipj.NAME_TYPE
                | gxipj.NAME_LLDATUM
                | gxipj.NAME_METHOD_PARMS
                | gxipj.NAME_METHOD_LABEL
                | gxipj.NAME_DATUM_PARMS
                | gxipj.NAME_LDATUM_PARMS
                | gxipj.NAME_GEOID
                | gxipj.NAME_LDATUMDESCRIPTION
                | gxipj.NAME_METHOD_PARMS_NATIVE
                | gxipj.NAME_ORIENTATION

        If 'what' is not specified, gxipj.NAME assumed, which returns the coordinate system display name.

        :return: The name requested

        .. versionadded:: 9.2
        """

        sref = gxapi.str_ref()
        if what is None:
            self.gxipj.get_display_name(sref)
        else:
            self.gxipj.get_name(what, sref)
        return sref.value

    def units(self):
        """
        :return: tuple (factor, abbreviation), where factor is multiplier to convert to metres

        .. versionadded:: 9.2
        """

        sref = gxapi.str_ref()
        fref = gxapi.float_ref()
        self.gxipj.get_units(fref, sref)
        return fref.value, sref.value


class GXpj:
    """
    Class to reproject coordinates.

    :params cs_from:  GXcs from coordinate system
    :params cs_to:    GXcs to coordinate system

    .. versionadded:: 9.2
    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "PJ from \'{}\' to \'{}\'".format(str(self._cs_from), str(self._cs_to))

    _cs_from = None
    _cs_to = None
    _sr = gxapi.str_ref()

    def __init__(self, cs_from, cs_to):
        self._cs_from = cs_from
        self._cs_to = cs_to
        self._pj = gxapi.GXPJ.create_ipj(cs_from.gxipj, cs_to.gxipj)

    def convert(self, xyz):
        """
        Project data in array in which first columns are x,y or x,y,z.

        Coordinates are reprojected in-place.

        :param xyz:
                | numpy array shape (,3+) for (x,y,z) conversion
                | numpy array shape (,2) for x,y conversion

        :example:
            Given an array shape (500,6), which represents 500 data records with 6 columns
            in which the first 3 columns are coordinates X, Y and Z.

            .. code::

                data = np.zeros((10,5), dtype='float') #then fill the array with some data

                pj.convert(data[:,2])       #transform x,y
                pj.convert(data[:,3])       #transform x,y and z
                pj.convert(data)            #transform x,y and z (same as previous line)

        .. versionadded:: 9.2
        """

        npoints = xyz.shape[0]
        if npoints == 0:
            return

        nd = xyz.shape[1]
        if nd < 2:
            raise CSException(_('Data must have minimum dimension 2 (x,y) or 3 for (x,y,z).'))

        vvx = gxapi.GXVV.create_ext(gxapi.GS_DOUBLE, npoints)
        vvy = gxapi.GXVV.create_ext(gxapi.GS_DOUBLE, npoints)
        vvx.set_data_np(0, xyz[:, 0])
        vvy.set_data_np(0, xyz[:, 1])

        if nd >= 3:
            vvz = gxapi.GXVV.create_ext(gxapi.GS_DOUBLE, npoints)
            vvz.set_data_np(0, xyz[:, 2])
            self._pj.convert_vv3(vvx, vvy, vvz)
            xyz[:, 2] = vvz.get_data_np(0, npoints, 'f8')
        else:
            self._pj.convert_vv(vvx, vvy)

        xyz[:, 0] = vvx.get_data_np(0, npoints, 'f8')
        xyz[:, 1] = vvy.get_data_np(0, npoints, 'f8')
