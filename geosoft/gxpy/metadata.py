"""
Geosoft metadata.

:Classes:

    ================= =========================
    :class:`Metadata` metadata
    ================= =========================

.. seealso:: :mod:`geosoft.gxap_i.GXMETA`

.. note::

    Regression tests provide usage examples:
    `metadata tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_metadata.py>`_

.. versionadded:: 9.3
"""

import os
import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import utility as gxu
import json

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class MetadataException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.metadata`.

    .. versionadded:: 9.3
    """
    pass


META_TYPE_NODE = 0  #:
META_TYPE_ATTRIBUTE = 1  #:

META_INVALID = -1  #:
META_ROOT_NODE = -100  #:


def _umn(meta_type, node):
    name = node.strip('/')
    if meta_type == META_TYPE_NODE:
        return 'CLASS:/{}'.format(name)
    elif meta_type == META_TYPE_ATTRIBUTE:
        return 'ATTRIB:/{}'.format(name)


def get_node_from_meta_dict(meta_node, meta_dict):
    """
    Get the node content from a metadata dictionary.

    :param meta_node:   node wanted, '/' delimited. e.g. 'geosoft/dataset/title'
    :param meta_dict:   metadata dictionary (from `Metadata.meta_dict`)
    :return:            node content, or None if not found

    .. versionadded:: 9.3.1
    """
    if not meta_node:
        return None
    tree = meta_node.split('/')
    root = meta_dict
    for node in tree:
        if node:
            if node not in root:
                return None
            root = root[node]
    return root


def set_node_in_meta_dict(meta_node, meta_dict, content, replace=False):
    """
    Set a node in a metadata dictionary. Tree nodes are added if absent.

    :param meta_node:   node to set, '/' delimited. e.g. 'geosoft/dataset/title'
    :param meta_dict:   meta dictionary (from `Metadata.meta_dict`)
    :param content:     content to set to the node
    :param replace:     True to replace nodes that are attributes.  The default is False, in which case
                        an error is raised if a node in the tree is an attribute.

    .. versionadded:: 9.3.1
    """
    if meta_node[-1] == '/':
        meta_node = meta_node[:-1]
    tree = meta_node.split('/')
    root = meta_dict
    for node in tree[:-1]:
        if node not in root:
            root[node] = {}
        elif not isinstance(root[node], dict):
            if replace:
                root[node] = {}
            else:
                raise MetadataException(_t('Cannot replace attribte {}. All nodes in the tree must be dict.').
                                        format(root))
        root = root[node]

    root[tree[-1]] = content


class Metadata:
    """
    Simple interface to work with Geosoft metadata objects :class::`geosoft.gxapi.GXMETA`.

    :param gxmeta:  `geosoft.gxapi.GXMETA` instance, or None (default) in which case an
                     empty metadata instance is created.

    Geosoft metadata objects contain metadata organized as a tree of information, with
    each node of the tree containing 0 or more attributes and 0 or more nested nodes.

    While geosoft metadata can contain custom typed attributes and indeed any Geosoft object, this simple interface
    currently supports only Python types int, float, string and Python structures like tuple, arrays and
    dictionaries.

    Nodes are identified by a string in the form: `/node/[...]/` (eg. `'/geosoft/data/'`).

    Attributes are identified by a string in the form `/node/[...]/attribute` (eg. `'geosoft/data/keywords'`).

    .. versionadded:: 9.3
    """

    def __enter__(self):
        return self

    def __exit__(self, _type, _value, _traceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_gxmeta'):
            self._gxmeta = None

    def __init__(self, gxmeta=None):
        if gxmeta:
            self._gxmeta = gxmeta
        else:
            self._gxmeta = gxapi.GXMETA.create()

    @property
    def gxmeta(self):
        """
        The :class:`geosoft.gxapi.GXMETA` instance handle.

        .. versionadded:: 9.3
        """
        return self._gxmeta

    def meta_type(self, meta_node):
        """
        Return if the content of this node is a node (`META_TYPE_NODE`) or an attribute (`META_TYPE_ATTRIBUTE`).

        Returns `META_INVALID` if neither.

        :param meta_node:   metadata node as a string. e.g. 'geosoft/dataset/title'

        .. versionadded:: 9.3
        """
        if self.gxmeta.resolve_umn(_umn(META_TYPE_NODE, meta_node)) != META_INVALID:
            return META_TYPE_NODE
        elif self.gxmeta.resolve_umn(_umn(META_TYPE_ATTRIBUTE, meta_node)) != META_INVALID:
            return META_TYPE_ATTRIBUTE
        return META_INVALID

    def has_node(self, node_name):
        """
        Returns `True` if this node exists in the metadata.

        :param node_name: name of a node (eg. `'geosoft/data/'`)

        .. versionadded:: 9.3
        """
        return self.meta_type(node_name) == META_TYPE_NODE

    def has_attribute(self, attribute_name):
        """
        Returns `True` if this attribute exists in the metadata.

        :param attribute_name: name of a attribute (eg. `'geosoft/data/keywords'`)

        .. versionadded:: 9.3
        """
        return self.meta_type(attribute_name) == META_TYPE_ATTRIBUTE

    def node_token(self, node_name):
        """
        Returns the metadata token (integer) of a node.  The node is created if it does not exist.

        :param node_name:   name of the node (eg. `'my_metadata/parameters'`)
        :returns:           metadata token number

        .. versionadded::9.3
        """
        node_name = node_name.strip('/')
        tree = node_name.split('/')
        branch = META_ROOT_NODE
        for node in tree:
            branch = self.gxmeta.create_class(node, branch)
        return self.gxmeta.resolve_umn(_umn(META_TYPE_NODE, node_name))

    def attribute_token(self, attr_name):
        """
        Returns the metadata token (integer) of an attribute.

        :param attr_name:   name of the attribute (eg. `'my_metadata/parameters/frequency'`)
        :returns:           metadata token number or `META_INVALID` if the attribute does not exist.

        .. versionadded::9.3
        """
        if self.has_attribute(attr_name):
            return self.gxmeta.resolve_umn(_umn(META_TYPE_ATTRIBUTE, attr_name))
        return META_INVALID

    def node_attribute_token(self, attr_name):
        """
        returns the node and attribute number of an attribute.

        :param attr_name:   attribute name
        :returns:           (node token, attribute token)

        .. versionadded:: 9.3
        """
        node_attr = tuple(attr_name.strip('/').rsplit('/', 1))
        if len(node_attr) == 1:
            return 0, self.attribute_token(attr_name)
        node = node_attr[0]
        if not self.has_attribute(attr_name):
            raise MetadataException('Attribute "{}" not found'.format(attr_name))
        return self.node_token(node), self.attribute_token(attr_name)

    def set_attribute(self, attr_name, value):
        """
        Set an attribute to a value.  The attribute is created if it does not exist.

        :param attr_name:   attribute name (eg. `'/my_metadata/parameters/frequency'`)
        :param value:       int, float, string or a Python structure such as tuple, array or dict.

        .. versionadded:: 9.3
        """
        node_attr = attr_name.strip('/').rsplit('/', 1)
        if len(node_attr) < 2:
            node = ''
            attr = node_attr[0]
        else:
            node = node_attr[0]
            attr = node_attr[1]
        if self.has_attribute(attr_name):
            self.gxmeta.delete_attrib(self.attribute_token(attr_name))
        node = self.node_token(node)
        if isinstance(value, str):
            a = self.gxmeta.create_attrib(attr, node, gxapi.META_CORE_TYPE_String)
            self.gxmeta.set_attrib_string(node, a, value)
        elif isinstance(value, float):
            a = self.gxmeta.create_attrib(attr, node, gxapi.META_CORE_TYPE_R8)
            self.gxmeta.set_attrib_double(node, a, value)
        elif isinstance(value, int):
            a = self.gxmeta.create_attrib(attr, node, gxapi.META_CORE_TYPE_I4)
            self.gxmeta.set_attrib_int(node, a, value)
        else:
            jstr = '__json__{}'.format(json.dumps(value))
            a = self.gxmeta.create_attrib(attr, node, gxapi.META_CORE_TYPE_String)
            self.gxmeta.set_attrib_string(node, a, jstr)

    def get_attribute(self, attr_name):
        """
        Retrieve an attribute setting.

        :param attr_name:   attribute name (eg. '/my_metadata/parameters/frequency')
        :returns:           attribute setting

        .. versionadded:: 9.3
        """
        if not self.has_attribute(attr_name):
            return None
        node, attr = self.node_attribute_token(attr_name)
        sr = gxapi.str_ref()
        self.gxmeta.get_attrib_string(node, attr, sr)
        try:
            i = int(sr.value)
            return i
        except ValueError:
            try:
                f = float(sr.value)
                return f
            except ValueError:
                if sr.value.startswith('__json__'):
                    return json.loads(sr.value[8:])
                return sr.value

    def meta_dict(self):
        """
        Metadata content as a nested dictionary.

        Attributes will be normal Python objects where the attribute type is supported by Python. This
        includes basic types (like int and float), lists/tuples, and Python dictionaries.

        Geosoft objects in an attribute, will appear only as a descriptive text string.

        :return: nested dictionary structure of metadata

        .. versionadded:: 9.3
        """

        def parse_attr(s):
            parts = s.split('=', 1)
            if len(parts) >= 2:
                val = parts[1][1:-1]
                if val.startswith('__json__'):
                    val = val[8:].replace('\\"', '"')
                    val = json.loads(val)
                return parts[0].lstrip(), val
            else:
                return parts[0].lstrip(), None

        def add_meta(ff):

            def parse_node(s):
                nest = 0
                while s[0] == ' ':
                    nest += 1
                    s = s[3:]
                return s[1:], nest

            def read_node(ffl):
                _d = {}
                node_name, nest = parse_node(ffl[0])
                ffl = ffl[1:]
                while ffl:
                    while ffl[0].lstrip()[0] != '\\':
                        _name, val = parse_attr(ffl[0])
                        _d[_name] = val
                        ffl = ffl[1:]
                        if not ffl:
                            return node_name, _d, ffl
                    else:
                        _, next_nest = parse_node(ffl[0])
                        if next_nest <= nest:
                            return node_name, _d, ffl
                        nn, _dd, ffl = read_node(ffl)
                        _d[nn] = _dd
                return node_name, _d, ffl

            dct = {}
            while ff:
                if ff[0][0] != '\\':
                    name, val = parse_attr(ff[0])
                    dct[name] = val
                    ff = ff[1:]
                else:
                    name, dd, ff = read_node(ff)
                    dct[name] = dd
            return dct

        def metafile():
            mf = os.path.join(gx.gx().temp_folder(), 'meta_' + gxu.uuid())
            wa = gxapi.GXWA.create(mf, gxapi.WA_NEW)
            self.gxmeta.write_text(wa)
            wa = None
            return mf

        def metafile_to_list(metafile):
            ff = []
            with open(metafile, 'r') as f:
                for line in f:
                    line = line.rstrip()
                    if line:
                        ff.append(line)
            os.remove(metafile)
            return ff

        metalist = metafile_to_list(metafile())
        return add_meta(metalist)

    def update_dict(self, metadict, trunk_node=''):
        """
        Update the metadata from the content of a dictionary.

        :param metadict:    dictionary of metadata to add/update
        :param trunk:       trunk to which to add this meta, default is '' which adds from the root.

        .. versionadded:: 9.3.1
        """

        def update(tnode, new):
            for k, v in new.items():
                node = '{}/{}'.format(tnode, k)
                if isinstance(v, dict):
                    update(node, v)
                else:
                    self.set_attribute(node, v)

        update(trunk_node, metadict)
