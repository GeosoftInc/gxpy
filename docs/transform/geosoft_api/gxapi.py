# e:\tfs\trunkmain\tools\build\utils\Python35\Lib\site-packages\geosoft_api\gxapi.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2493ea57b863ed7ce6975e5dfe065f3201ea8071
# Generated 2017-01-20 16:55:57.585716 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace http://www.geosoft.com/gxapi

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:38f5bb9a-df5b-11e6-97ef-3417ebe0bfbe')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.geosoft.com/gxapi', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.geosoft.com/gxapi}definitions uses Python identifier definitions
    __definitions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'definitions'), 'definitions', '__httpwww_geosoft_comgxapi_CTD_ANON_httpwww_geosoft_comgxapidefinitions', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 22, 2), )

    
    definitions = property(__definitions.value, __definitions.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}methodgroups uses Python identifier methodgroups
    __methodgroups = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'methodgroups'), 'methodgroups', '__httpwww_geosoft_comgxapi_CTD_ANON_httpwww_geosoft_comgxapimethodgroups', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 66, 2), )

    
    methodgroups = property(__methodgroups.value, __methodgroups.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_geosoft_comgxapi_CTD_ANON_httpwww_geosoft_comgxapidescription', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httpwww_geosoft_comgxapi_CTD_ANON_httpwww_geosoft_comgxapinotes', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 129, 1), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}verbatim_defines uses Python identifier verbatim_defines
    __verbatim_defines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verbatim_defines'), 'verbatim_defines', '__httpwww_geosoft_comgxapi_CTD_ANON_httpwww_geosoft_comgxapiverbatim_defines', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 130, 1), )

    
    verbatim_defines = property(__verbatim_defines.value, __verbatim_defines.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_geosoft_comgxapi_CTD_ANON_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 15, 3)
    __name._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 15, 3)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute handlename uses Python identifier handlename
    __handlename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'handlename'), 'handlename', '__httpwww_geosoft_comgxapi_CTD_ANON_handlename', pyxb.binding.datatypes.string)
    __handlename._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 16, 3)
    __handlename._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 16, 3)
    
    handlename = property(__handlename.value, __handlename.set, None, None)

    
    # Attribute nogxh uses Python identifier nogxh
    __nogxh = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nogxh'), 'nogxh', '__httpwww_geosoft_comgxapi_CTD_ANON_nogxh', pyxb.binding.datatypes.boolean)
    __nogxh._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 17, 3)
    __nogxh._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 17, 3)
    
    nogxh = property(__nogxh.value, __nogxh.set, None, None)

    
    # Attribute nocsharp uses Python identifier nocsharp
    __nocsharp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nocsharp'), 'nocsharp', '__httpwww_geosoft_comgxapi_CTD_ANON_nocsharp', pyxb.binding.datatypes.boolean)
    __nocsharp._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 18, 3)
    __nocsharp._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 18, 3)
    
    nocsharp = property(__nocsharp.value, __nocsharp.set, None, None)

    
    # Attribute nocpp uses Python identifier nocpp
    __nocpp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nocpp'), 'nocpp', '__httpwww_geosoft_comgxapi_CTD_ANON_nocpp', pyxb.binding.datatypes.boolean)
    __nocpp._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 19, 3)
    __nocpp._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 19, 3)
    
    nocpp = property(__nocpp.value, __nocpp.set, None, None)

    _ElementMap.update({
        __definitions.name() : __definitions,
        __methodgroups.name() : __methodgroups,
        __description.name() : __description,
        __notes.name() : __notes,
        __verbatim_defines.name() : __verbatim_defines
    })
    _AttributeMap.update({
        __name.name() : __name,
        __handlename.name() : __handlename,
        __nogxh.name() : __nogxh,
        __nocsharp.name() : __nocsharp,
        __nocpp.name() : __nocpp
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 23, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.geosoft.com/gxapi}definition uses Python identifier definition
    __definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'definition'), 'definition', '__httpwww_geosoft_comgxapi_CTD_ANON__httpwww_geosoft_comgxapidefinition', True, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 29, 2), )

    
    definition = property(__definition.value, __definition.set, None, None)

    _ElementMap.update({
        __definition.name() : __definition
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 30, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.geosoft.com/gxapi}defined_value uses Python identifier defined_value
    __defined_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'defined_value'), 'defined_value', '__httpwww_geosoft_comgxapi_CTD_ANON_2_httpwww_geosoft_comgxapidefined_value', True, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 42, 1), )

    
    defined_value = property(__defined_value.value, __defined_value.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_geosoft_comgxapi_CTD_ANON_2_httpwww_geosoft_comgxapidescription', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_geosoft_comgxapi_CTD_ANON_2_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 35, 6)
    __name._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 35, 6)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute constant uses Python identifier constant
    __constant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'constant'), 'constant', '__httpwww_geosoft_comgxapi_CTD_ANON_2_constant', pyxb.binding.datatypes.boolean)
    __constant._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 36, 6)
    __constant._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 36, 6)
    
    constant = property(__constant.value, __constant.set, None, None)

    
    # Attribute single_constant uses Python identifier single_constant
    __single_constant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'single_constant'), 'single_constant', '__httpwww_geosoft_comgxapi_CTD_ANON_2_single_constant', pyxb.binding.datatypes.boolean)
    __single_constant._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 37, 6)
    __single_constant._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 37, 6)
    
    single_constant = property(__single_constant.value, __single_constant.set, None, None)

    
    # Attribute null_handle uses Python identifier null_handle
    __null_handle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'null_handle'), 'null_handle', '__httpwww_geosoft_comgxapi_CTD_ANON_2_null_handle', pyxb.binding.datatypes.boolean)
    __null_handle._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 38, 6)
    __null_handle._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 38, 6)
    
    null_handle = property(__null_handle.value, __null_handle.set, None, None)

    
    # Attribute cpp_prefix uses Python identifier cpp_prefix
    __cpp_prefix = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cpp_prefix'), 'cpp_prefix', '__httpwww_geosoft_comgxapi_CTD_ANON_2_cpp_prefix', pyxb.binding.datatypes.string)
    __cpp_prefix._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 39, 6)
    __cpp_prefix._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 39, 6)
    
    cpp_prefix = property(__cpp_prefix.value, __cpp_prefix.set, None, None)

    _ElementMap.update({
        __defined_value.name() : __defined_value,
        __description.name() : __description
    })
    _AttributeMap.update({
        __name.name() : __name,
        __constant.name() : __constant,
        __single_constant.name() : __single_constant,
        __null_handle.name() : __null_handle,
        __cpp_prefix.name() : __cpp_prefix
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 43, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.geosoft.com/gxapi}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_geosoft_comgxapi_CTD_ANON_3_httpwww_geosoft_comgxapidescription', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'val'), 'val', '__httpwww_geosoft_comgxapi_CTD_ANON_3_val', pyxb.binding.datatypes.string)
    __val._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 47, 3)
    __val._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 47, 3)
    
    val = property(__val.value, __val.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_geosoft_comgxapi_CTD_ANON_3_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 48, 3)
    __type._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 48, 3)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_geosoft_comgxapi_CTD_ANON_3_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 49, 3)
    __name._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 49, 3)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute cpp_type uses Python identifier cpp_type
    __cpp_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cpp_type'), 'cpp_type', '__httpwww_geosoft_comgxapi_CTD_ANON_3_cpp_type', pyxb.binding.datatypes.string)
    __cpp_type._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 50, 3)
    __cpp_type._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 50, 3)
    
    cpp_type = property(__cpp_type.value, __cpp_type.set, None, None)

    _ElementMap.update({
        __description.name() : __description
    })
    _AttributeMap.update({
        __val.name() : __val,
        __type.name() : __type,
        __name.name() : __name,
        __cpp_type.name() : __cpp_type
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.geosoft.com/gxapi}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_geosoft_comgxapi_CTD_ANON_4_httpwww_geosoft_comgxapidescription', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute size_of_param uses Python identifier size_of_param
    __size_of_param = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size_of_param'), 'size_of_param', '__httpwww_geosoft_comgxapi_CTD_ANON_4_size_of_param', pyxb.binding.datatypes.int)
    __size_of_param._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 58, 3)
    __size_of_param._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 58, 3)
    
    size_of_param = property(__size_of_param.value, __size_of_param.set, None, None)

    
    # Attribute size_of_param_intval uses Python identifier size_of_param_intval
    __size_of_param_intval = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size_of_param_intval'), 'size_of_param_intval', '__httpwww_geosoft_comgxapi_CTD_ANON_4_size_of_param_intval', pyxb.binding.datatypes.boolean)
    __size_of_param_intval._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 59, 3)
    __size_of_param_intval._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 59, 3)
    
    size_of_param_intval = property(__size_of_param_intval.value, __size_of_param_intval.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_geosoft_comgxapi_CTD_ANON_4_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 60, 3)
    __type._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 60, 3)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute cstype uses Python identifier cstype
    __cstype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cstype'), 'cstype', '__httpwww_geosoft_comgxapi_CTD_ANON_4_cstype', pyxb.binding.datatypes.string)
    __cstype._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 61, 3)
    __cstype._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 61, 3)
    
    cstype = property(__cstype.value, __cstype.set, None, None)

    
    # Attribute defaultlength uses Python identifier defaultlength
    __defaultlength = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'defaultlength'), 'defaultlength', '__httpwww_geosoft_comgxapi_CTD_ANON_4_defaultlength', pyxb.binding.datatypes.string)
    __defaultlength._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 62, 3)
    __defaultlength._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 62, 3)
    
    defaultlength = property(__defaultlength.value, __defaultlength.set, None, None)

    
    # Attribute novariable uses Python identifier novariable
    __novariable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'novariable'), 'novariable', '__httpwww_geosoft_comgxapi_CTD_ANON_4_novariable', pyxb.binding.datatypes.boolean)
    __novariable._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 63, 3)
    __novariable._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 63, 3)
    
    novariable = property(__novariable.value, __novariable.set, None, None)

    _ElementMap.update({
        __description.name() : __description
    })
    _AttributeMap.update({
        __size_of_param.name() : __size_of_param,
        __size_of_param_intval.name() : __size_of_param_intval,
        __type.name() : __type,
        __cstype.name() : __cstype,
        __defaultlength.name() : __defaultlength,
        __novariable.name() : __novariable
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 67, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.geosoft.com/gxapi}methodgroup uses Python identifier methodgroup
    __methodgroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'methodgroup'), 'methodgroup', '__httpwww_geosoft_comgxapi_CTD_ANON_5_httpwww_geosoft_comgxapimethodgroup', True, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 73, 2), )

    
    methodgroup = property(__methodgroup.value, __methodgroup.set, None, None)

    _ElementMap.update({
        __methodgroup.name() : __methodgroup
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 74, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.geosoft.com/gxapi}method uses Python identifier method
    __method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'method'), 'method', '__httpwww_geosoft_comgxapi_CTD_ANON_6_httpwww_geosoft_comgxapimethod', True, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 81, 1), )

    
    method = property(__method.value, __method.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_geosoft_comgxapi_CTD_ANON_6_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 78, 6)
    __name._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 78, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __method.name() : __method
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 82, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.geosoft.com/gxapi}parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameters'), 'parameters', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapiparameters', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 112, 2), )

    
    parameters = property(__parameters.value, __parameters.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}returnval uses Python identifier returnval
    __returnval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnval'), 'returnval', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapireturnval', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 119, 2), )

    
    returnval = property(__returnval.value, __returnval.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}see_also uses Python identifier see_also
    __see_also = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'see_also'), 'see_also', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapisee_also', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 127, 2), )

    
    see_also = property(__see_also.value, __see_also.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapidescription', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapinotes', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 129, 1), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}cpp_decl uses Python identifier cpp_decl
    __cpp_decl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpp_decl'), 'cpp_decl', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapicpp_decl', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 131, 1), )

    
    cpp_decl = property(__cpp_decl.value, __cpp_decl.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}cpp_impl uses Python identifier cpp_impl
    __cpp_impl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpp_impl'), 'cpp_impl', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapicpp_impl', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 132, 1), )

    
    cpp_impl = property(__cpp_impl.value, __cpp_impl.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}python_impl uses Python identifier python_impl
    __python_impl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'python_impl'), 'python_impl', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapipython_impl', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 133, 1), )

    
    python_impl = property(__python_impl.value, __python_impl.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}python_import uses Python identifier python_import
    __python_import = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'python_import'), 'python_import', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapipython_import', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 134, 1), )

    
    python_import = property(__python_import.value, __python_import.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}dbus_xml uses Python identifier dbus_xml
    __dbus_xml = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dbus_xml'), 'dbus_xml', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapidbus_xml', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 135, 1), )

    
    dbus_xml = property(__dbus_xml.value, __dbus_xml.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}dbus_impl uses Python identifier dbus_impl
    __dbus_impl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dbus_impl'), 'dbus_impl', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapidbus_impl', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 136, 1), )

    
    dbus_impl = property(__dbus_impl.value, __dbus_impl.set, None, None)

    
    # Element {http://www.geosoft.com/gxapi}dbus_callback uses Python identifier dbus_callback
    __dbus_callback = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dbus_callback'), 'dbus_callback', '__httpwww_geosoft_comgxapi_CTD_ANON_7_httpwww_geosoft_comgxapidbus_callback', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 137, 1), )

    
    dbus_callback = property(__dbus_callback.value, __dbus_callback.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_geosoft_comgxapi_CTD_ANON_7_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 97, 3)
    __name._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 97, 3)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute module uses Python identifier module
    __module = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'module'), 'module', '__httpwww_geosoft_comgxapi_CTD_ANON_7_module', pyxb.binding.datatypes.string)
    __module._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 98, 3)
    __module._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 98, 3)
    
    module = property(__module.value, __module.set, None, None)

    
    # Attribute license uses Python identifier license
    __license = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'license'), 'license', '__httpwww_geosoft_comgxapi_CTD_ANON_7_license', pyxb.binding.datatypes.string)
    __license._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 99, 3)
    __license._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 99, 3)
    
    license = property(__license.value, __license.set, None, None)

    
    # Attribute available uses Python identifier available
    __available = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'available'), 'available', '__httpwww_geosoft_comgxapi_CTD_ANON_7_available', pyxb.binding.datatypes.string)
    __available._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 100, 3)
    __available._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 100, 3)
    
    available = property(__available.value, __available.set, None, None)

    
    # Attribute externalname uses Python identifier externalname
    __externalname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'externalname'), 'externalname', '__httpwww_geosoft_comgxapi_CTD_ANON_7_externalname', pyxb.binding.datatypes.string)
    __externalname._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 101, 3)
    __externalname._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 101, 3)
    
    externalname = property(__externalname.value, __externalname.set, None, None)

    
    # Attribute obsolete uses Python identifier obsolete
    __obsolete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'obsolete'), 'obsolete', '__httpwww_geosoft_comgxapi_CTD_ANON_7_obsolete', pyxb.binding.datatypes.boolean)
    __obsolete._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 102, 3)
    __obsolete._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 102, 3)
    
    obsolete = property(__obsolete.value, __obsolete.set, None, None)

    
    # Attribute nogxh uses Python identifier nogxh
    __nogxh = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nogxh'), 'nogxh', '__httpwww_geosoft_comgxapi_CTD_ANON_7_nogxh', pyxb.binding.datatypes.boolean)
    __nogxh._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 103, 3)
    __nogxh._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 103, 3)
    
    nogxh = property(__nogxh.value, __nogxh.set, None, None)

    
    # Attribute nocsharp uses Python identifier nocsharp
    __nocsharp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nocsharp'), 'nocsharp', '__httpwww_geosoft_comgxapi_CTD_ANON_7_nocsharp', pyxb.binding.datatypes.boolean)
    __nocsharp._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 104, 3)
    __nocsharp._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 104, 3)
    
    nocsharp = property(__nocsharp.value, __nocsharp.set, None, None)

    
    # Attribute guicall uses Python identifier guicall
    __guicall = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'guicall'), 'guicall', '__httpwww_geosoft_comgxapi_CTD_ANON_7_guicall', pyxb.binding.datatypes.boolean)
    __guicall._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 105, 3)
    __guicall._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 105, 3)
    
    guicall = property(__guicall.value, __guicall.set, None, None)

    
    # Attribute nocpp uses Python identifier nocpp
    __nocpp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nocpp'), 'nocpp', '__httpwww_geosoft_comgxapi_CTD_ANON_7_nocpp', pyxb.binding.datatypes.boolean)
    __nocpp._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 106, 3)
    __nocpp._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 106, 3)
    
    nocpp = property(__nocpp.value, __nocpp.set, None, None)

    
    # Attribute cpp_pre uses Python identifier cpp_pre
    __cpp_pre = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cpp_pre'), 'cpp_pre', '__httpwww_geosoft_comgxapi_CTD_ANON_7_cpp_pre', pyxb.binding.datatypes.string)
    __cpp_pre._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 107, 3)
    __cpp_pre._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 107, 3)
    
    cpp_pre = property(__cpp_pre.value, __cpp_pre.set, None, None)

    
    # Attribute cpp_post uses Python identifier cpp_post
    __cpp_post = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cpp_post'), 'cpp_post', '__httpwww_geosoft_comgxapi_CTD_ANON_7_cpp_post', pyxb.binding.datatypes.string)
    __cpp_post._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 108, 3)
    __cpp_post._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 108, 3)
    
    cpp_post = property(__cpp_post.value, __cpp_post.set, None, None)

    
    # Attribute dbus_exp_name uses Python identifier dbus_exp_name
    __dbus_exp_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dbus_exp_name'), 'dbus_exp_name', '__httpwww_geosoft_comgxapi_CTD_ANON_7_dbus_exp_name', pyxb.binding.datatypes.string)
    __dbus_exp_name._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 109, 3)
    __dbus_exp_name._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 109, 3)
    
    dbus_exp_name = property(__dbus_exp_name.value, __dbus_exp_name.set, None, None)

    _ElementMap.update({
        __parameters.name() : __parameters,
        __returnval.name() : __returnval,
        __see_also.name() : __see_also,
        __description.name() : __description,
        __notes.name() : __notes,
        __cpp_decl.name() : __cpp_decl,
        __cpp_impl.name() : __cpp_impl,
        __python_impl.name() : __python_impl,
        __python_import.name() : __python_import,
        __dbus_xml.name() : __dbus_xml,
        __dbus_impl.name() : __dbus_impl,
        __dbus_callback.name() : __dbus_callback
    })
    _AttributeMap.update({
        __name.name() : __name,
        __module.name() : __module,
        __license.name() : __license,
        __available.name() : __available,
        __externalname.name() : __externalname,
        __obsolete.name() : __obsolete,
        __nogxh.name() : __nogxh,
        __nocsharp.name() : __nocsharp,
        __guicall.name() : __guicall,
        __nocpp.name() : __nocpp,
        __cpp_pre.name() : __cpp_pre,
        __cpp_post.name() : __cpp_post,
        __dbus_exp_name.name() : __dbus_exp_name
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 113, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.geosoft.com/gxapi}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpwww_geosoft_comgxapi_CTD_ANON_8_httpwww_geosoft_comgxapiparameter', True, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 53, 1), )

    
    parameter = property(__parameter.value, __parameter.set, None, None)

    _ElementMap.update({
        __parameter.name() : __parameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 120, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.geosoft.com/gxapi}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_geosoft_comgxapi_CTD_ANON_9_httpwww_geosoft_comgxapidescription', False, pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_geosoft_comgxapi_CTD_ANON_9_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 124, 6)
    __type._UseLocation = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 124, 6)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __description.name() : __description
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


see_also = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'see_also'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 127, 2))
Namespace.addCategoryObject('elementBinding', see_also.name().localName(), see_also)

description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1))
Namespace.addCategoryObject('elementBinding', description.name().localName(), description)

notes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 129, 1))
Namespace.addCategoryObject('elementBinding', notes.name().localName(), notes)

verbatim_defines = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verbatim_defines'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 130, 1))
Namespace.addCategoryObject('elementBinding', verbatim_defines.name().localName(), verbatim_defines)

cpp_decl = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpp_decl'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 131, 1))
Namespace.addCategoryObject('elementBinding', cpp_decl.name().localName(), cpp_decl)

cpp_impl = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpp_impl'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 132, 1))
Namespace.addCategoryObject('elementBinding', cpp_impl.name().localName(), cpp_impl)

python_impl = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'python_impl'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 133, 1))
Namespace.addCategoryObject('elementBinding', python_impl.name().localName(), python_impl)

python_import = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'python_import'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 134, 1))
Namespace.addCategoryObject('elementBinding', python_import.name().localName(), python_import)

dbus_xml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dbus_xml'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 135, 1))
Namespace.addCategoryObject('elementBinding', dbus_xml.name().localName(), dbus_xml)

dbus_impl = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dbus_impl'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 136, 1))
Namespace.addCategoryObject('elementBinding', dbus_impl.name().localName(), dbus_impl)

dbus_callback = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dbus_callback'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 137, 1))
Namespace.addCategoryObject('elementBinding', dbus_callback.name().localName(), dbus_callback)

gxclass = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gxclass'), CTD_ANON, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 6, 1))
Namespace.addCategoryObject('elementBinding', gxclass.name().localName(), gxclass)

definitions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definitions'), CTD_ANON_, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 22, 2))
Namespace.addCategoryObject('elementBinding', definitions.name().localName(), definitions)

definition = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definition'), CTD_ANON_2, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 29, 2))
Namespace.addCategoryObject('elementBinding', definition.name().localName(), definition)

defined_value = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'defined_value'), CTD_ANON_3, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 42, 1))
Namespace.addCategoryObject('elementBinding', defined_value.name().localName(), defined_value)

parameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), CTD_ANON_4, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 53, 1))
Namespace.addCategoryObject('elementBinding', parameter.name().localName(), parameter)

methodgroups = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'methodgroups'), CTD_ANON_5, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 66, 2))
Namespace.addCategoryObject('elementBinding', methodgroups.name().localName(), methodgroups)

methodgroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'methodgroup'), CTD_ANON_6, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 73, 2))
Namespace.addCategoryObject('elementBinding', methodgroup.name().localName(), methodgroup)

method = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'method'), CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 81, 1))
Namespace.addCategoryObject('elementBinding', method.name().localName(), method)

parameters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameters'), CTD_ANON_8, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 112, 2))
Namespace.addCategoryObject('elementBinding', parameters.name().localName(), parameters)

returnval = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnval'), CTD_ANON_9, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 119, 2))
Namespace.addCategoryObject('elementBinding', returnval.name().localName(), returnval)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definitions'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 22, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'methodgroups'), CTD_ANON_5, scope=CTD_ANON, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 66, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 129, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verbatim_defines'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 130, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 9, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 9, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 10, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verbatim_defines')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 10, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 11, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 12, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'definitions')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 12, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 13, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'methodgroups')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 13, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 9, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 10, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 11, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 12, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 13, 4))
    counters.add(cc_4)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    final_update = set()
    symbol = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 8, 3)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definition'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 29, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 25, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'definition')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 25, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_6()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'defined_value'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 42, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 32, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 33, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 32, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'defined_value')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 33, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_7()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 45, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 45, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_8()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 56, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 56, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_9()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'methodgroup'), CTD_ANON_6, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 73, 2)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 69, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'methodgroup')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 69, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_10()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'method'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 81, 1)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 76, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'method')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 76, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_11()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameters'), CTD_ANON_8, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 112, 2)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnval'), CTD_ANON_9, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 119, 2)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'see_also'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 127, 2)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 129, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpp_decl'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 131, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpp_impl'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 132, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'python_impl'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 133, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'python_import'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 134, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dbus_xml'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 135, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dbus_impl'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 136, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dbus_callback'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 137, 1)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 84, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'see_also')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 84, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 85, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 85, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 86, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnval')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 87, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameters')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 88, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 89, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpp_decl')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 89, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 90, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpp_impl')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 90, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 91, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'python_impl')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 91, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 92, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'python_import')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 92, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 93, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dbus_xml')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 93, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 94, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dbus_impl')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 94, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 95, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dbus_callback')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 95, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 84, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 85, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 89, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 90, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 91, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 92, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 93, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 94, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 95, 4))
    counters.add(cc_8)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_13())
    sub_automata.append(_BuildAutomaton_14())
    sub_automata.append(_BuildAutomaton_15())
    sub_automata.append(_BuildAutomaton_16())
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    sub_automata.append(_BuildAutomaton_21())
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    sub_automata.append(_BuildAutomaton_24())
    final_update = set()
    symbol = pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 83, 6)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_12()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), CTD_ANON_4, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 53, 1)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 115, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 115, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_25()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 128, 1)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 122, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('e:\\tfs\\trunkmain\\tools\\source\\build\\gxapitools\\gxapi\\gxapi.xsd', 122, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_26()

