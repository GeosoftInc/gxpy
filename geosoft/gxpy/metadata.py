"""
Class for handling metadata associated with various things in Geosoft.

Many data types in Geosoft can have an associated metadata onject that contains
data or application specific metadata.

:Classes:

    ================= ====================================================
    :class:`Metadata` metadata class
    ================= ====================================================

.. seealso:: :class:`geosoft.gxapi.GXMETA`

.. note::

    Regression tests provide usage examples:     
    `aggregate tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_metadata.py>`_

"""
import os
import yaml
import json
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, fromstring, XMLParser

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx

__version__ = geosoft.__version__

FORMAT_XML = 0
FORMAT_JSON = 1
FORMAT_YAML = 2

def _t(s):
    return geosoft.gxpy.system.translate(s)


class MetadataException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.metadata`.

    .. versionadded:: 9.3
    """
    pass


class Metadata:
    """

    .. versionadded:: 9.2
    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self._create_name()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __init__(self, metadata=None, form=FORMAT_XML):

        def s_to_yaml(s):
            if s.strip()[0] == '\\':
                return s[:-1].replace('\\', '', 1) + ':'
            else:
                return s[:-1].replace('=', ': ')

        def xml_to_dict(xml_object):
            dict_object = xml_object.__dict__
            if not dict_object:
                return xml_object
            for key, value in dict_object.items():
                dict_object[key] = xml_to_dict(value)
            return dict_object

        if isinstance(metadata, gxapi.GXMETA):

            temp_file_name = gx.gx.temp_file()
            metadata.write_text(gxapi.GXWA.create(temp_file_name, gxapi.WA_NEW))
            with open(temp_file_name, 'r') as f:
                ys = [s_to_yaml(s) for s in f]
            self._meta = yaml.load('\n'.join(ys))

        elif isinstance(metadata, str):
            if form == FORMAT_XML:
                with open('badxml.txt', 'w+') as f:
                    f.write(metadata)
                #parser = XMLParser(encoding="ASCII")
                self._meta = xml_to_dict(fromstring(metadata))
            elif form == FORMAT_YAML:
                self._meta = yaml.load(metadata)
            elif form == FORMAT_JSON:
                self._meta = json.loads(metadata)
            else:
                raise MetadataException(_t("Unrecognized metadata string format: {}".format(form)))

        else:
            self._meta = {}

    @property
    def metadata(self):
        """
        Returns a the metadata dictionary.
        
        :return: dictionary of the metadata content
        
        .. versionadded:: 9.3
        """
        return self._meta

    @metadata.setter
    def metadata(self, dict):
        self._meta = dict.copy()

    def xml(self, name='gx_metadata'):

        def buildxml(r, d):
            if isinstance(d, dict):
                for k, v in d.items():
                    s = SubElement(r, k)
                    buildxml(s, v)
            elif isinstance(d, tuple) or isinstance(d, list):
                for v in d:
                    s = SubElement(r, 'i')
                    buildxml(s, v)
            elif isinstance(d, str):
                try:
                    v = float(d)
                    r.text = d
                except ValueError:
                    r.text = '"{}"'.format(d)
            else:
                r.text = str(d)
            return r

        r = Element(name)
        et = buildxml(r, self._meta)
        sxml = tostring(et, encoding="unicode")
        return sxml

    def json(self):
        return json.dumps(self._meta)

    def yaml(self):
        return yaml.dump(self._meta)