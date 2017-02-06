import os
import pickle
import shutil
import sys 
import re
import time
import functools
import filecmp
from subprocess import call
from collections import namedtuple, OrderedDict, Hashable

from geosoft_api import gxapi

GXApiCollectionInfo = namedtuple('GXApiCollectionInfo', ['classes', 'known_classes', 'known_class_handles', 'known_methods', 'known_definitions', 'known_definition_values'])
global_collection = 0

class memoized(object):
	'''Decorator. Caches a function's return value each time it is called.
	If called later with the same arguments, the cached value is returned
	(not reevaluated).
	'''
	def __init__(self, func):
	   self.func = func
	   self.cache = {}
	def __call__(self, *args):
		if not isinstance(args, Hashable):
			# uncacheable.  a list, for instance.
			# better to not cache than blow up.
			return self.func(*args)
		if args in self.cache:
			return self.cache[args]
		else:
			value = self.func(*args)
			self.cache[args] = value
			return value
	def __repr__(self):
		'''Return the function's docstring.'''
		return self.func.__doc__
	def __get__(self, obj, objtype):
		'''Support instance methods.'''
		return functools.partial(self.__call__, obj)

def convert_camel_case(name):
	s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
	s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
	return s2.replace("3_d", "_3d")

def is_class(type_name):
	return type_name in global_collection.known_classes or type_name in global_collection.known_class_handles
	
def get_class(type_name):
	if type_name in global_collection.known_classes:
		return global_collection.known_classes[type_name]
	elif type_name in global_collection.known_class_handles:
		return global_collection.known_class_handles[type_name]
	else:
		return None

def get_python_defintion_value(defintion_value):
	if defintion_value.val in global_collection.known_definition_values:
		return global_collection.known_definition_values[defintion_value.val]['defined_value'].get_python_value()
	else:
		if defintion_value.type == 'System.String':
			return '"' + defintion_value.val + '"'
		else:
			return "(" + defintion_value.get_cpp_const_type() + ")" + defintion_value.get_value_without_casts()

def parse_type(type_name):
	if type_name in global_collection.known_class_handles:
		return global_collection.known_class_handles[type_name].name
	else:
		return type_name

def get_cpp_return_cast(type_name):
	if type_name == "bool":
		return "0 != "
	elif type_name in global_collection.known_definitions:
		return "(" + type_name + ")"
	else:
		return ""

def get_is_cpp_long_equivalent(type_name):
	if type_name == 'int32_t': 
		return True
	elif type_name in global_collection.known_definitions:
		return not global_collection.known_definitions[type_name].constant
	return False
	
def get_cpp_type(type_name, no_pointer=False):
	if is_class(type_name):
		type_name = "GX" + parse_type(type_name)
		if not no_pointer:
			return type_name + "Ptr"
		else:
			return type_name
	else:
		return {
			'real': 'double',
			'int': 'int32_t',
			'intval': 'int32_t',
			'string': 'const gx_string_type&',
			'var string': 'gx_string_type&',
			'CRC': 'int32_t',
			'WND': 'int32_t',
			'PTMP': 'int32_t',
			'FILTER': 'int32_t',
			'DGW_OBJ': 'int32_t',
			'TB_FIELD': 'int32_t',
			'DB_SELECT': 'int32_t',
			'DB_SYMB': 'int32_t',
			'META_TOKEN': 'int32_t',
			'HANDLE': 'int32_t',
			'GEO_BOOL': 'bool'
		}.get(type_name, type_name)


def restructured_directive(start, contents):
	indent = '\n' + ' ' * (len(start) + 1)
	return start + " " + indent.join(contents.strip().split('\n')) + "\n"

def word_to_ref(word, allow_classes):
	if allow_classes and word in global_collection.known_classes:
		return "\\ :class:`geosoft.gxapi.GX" + word + "`\\ "
	elif word in global_collection.known_methods:
		method_info = global_collection.known_methods[word]
		method = method_info['method']
		gxclass = method_info['gxclass']
		return "\\ :func:`geosoft.gxapi.GX" + gxclass.name + "." + gxclass.py_method_name(method) + "`\\ "
	else:
		return word

def all_refs_repl(matchobj):
	return word_to_ref(matchobj.group(0), True)	

def subst_all_refs(description):
	return re.sub('\w+', all_refs_repl, description)

def non_class_refs_repl(matchobj):
	return word_to_ref(matchobj.group(0), False)	

def subst_non_class_refs(description):
	return re.sub('\w+', non_class_refs_repl, description)

def define_refs_repl(matchobj):
	if matchobj.group(1) == "GEO_BOOL":
		return "bool"
	else:
		definition_name = matchobj.group(1)
		if definition_name in global_collection.known_definitions:
			definition = global_collection.known_definitions[definition_name]
			if definition.null_handle:
				return "\\ :func:`geosoft.gxapi.GX" + definition_name.replace("_NULL", "") + ".null()`\\ "
		return "\\ :ref:`" + matchobj.group(1) + "`\\ "

def subst_defines(description):
	return re.sub('<define>(.+?)</define>', define_refs_repl, description)

def docstring_fixes(description):
	description = description.replace("GS_TRUE", "``True``")
	description = description.replace("GS_FALSE", "``False``")
	description = subst_defines(description)
	description = description.replace("*", "\\ `*`\\ ")
	description = description.replace("|", "\\ `|`\\ ")
	return description

def docstring_literal_para(description, para_id='.. parsed-literal::', sub_all_refs=False):
	if sub_all_refs:
		description = subst_all_refs(description)
	else:
		description = subst_non_class_refs(description)
	description = docstring_fixes(description)
	return '\n"\\n' + para_id + '\\n\\n"\n"   ' + '\\n"\n"   '.join(description.replace("\\", "\\\\").replace("\"", "\\\"").split('\n')) + '\\n\\n"\n'

def docstring_literal_note(description):
	return '\n"\\n\\n**Note:**\\n\\n"\n' + docstring_literal_para(description)

def docstring_literal_seealso(description):
	return docstring_literal_para(description, para_id = '.. seealso::', sub_all_refs=True)

def docstring_literal_version(version):
	return '\n"\\n.. versionadded:: ' + version + '\\n\\n"\n'

def multi_line_fixup(description):
	return description.replace("\\", "\\\\").replace("\"", "\\\"")

def docstring_multi_line(description):
	description = docstring_fixes(description)
	return '\n"' + '\\n"\n"'.join(description.replace("\\", "\\\\").replace("\"", "\\\"").split('\n')) + '\\n"\n'

def generate_sphinx_description(description):
	return (' '.join(description.replace("\\", "\\\\").replace("\"", "\\\"").split('\n'))).strip()

class defined_value_class(gxapi.defined_value.typeDefinition()):
	@memoized
	def get_value_without_casts(self):
		return self.val.replace("(unsigned long) ", "").replace("(__GS_INT64) ", "").replace("(__GS_UINT64) ", "")

	@memoized
	def get_cpp_value(self):
		if self.type == 'System.String':
			return 'gx_string_literal("' + self.val + '")'
		else:
			return self.get_value_without_casts()

	@memoized
	def get_python_value(self):
		return get_python_defintion_value(self)
	
	@memoized
	def get_cpp_const_type(self):
		if self.cpp_type:
			return self.cpp_type
		if self.type == 'System.String':
			return "gx_string_char_type*"
		if self.type == 'System.Int32':
			return "int32_t"
		if self.type == 'System.Single':
			return "float"
		if self.type == 'System.Double':
			return "double"

	@memoized
	def get_spec_type(self):
		if self.cpp_type:
			return self.cpp_type
		elif self.type == 'System.String':
			return "string"
		elif self.type == 'System.Int32':
			return "int32_t"
		elif self.type == 'System.Single':
			return "float"
		elif self.type == 'System.Double':
			return "double"
		else:
			return self.type

	@memoized
	def get_sphinx_docstring(self):
		return docstring_fixes(subst_non_class_refs(self.description))

gxapi.defined_value.typeDefinition()._SetSupersedingClass(defined_value_class)			  

class definition_class(gxapi.definition.typeDefinition()):
	@memoized
	def get_cpp_const_name(self, defined_value):
		if self.single_constant:
			return defined_value.name
		else:
			value_name = defined_value.name
			parts = self.name.split('_')
			for part in parts:
				if value_name.startswith(part + "_"):
					value_name = value_name[len(part) + 1:]
			return value_name

	@memoized
	def get_cpp_const_declaration(self, defined_value):
		return 'static const ' + defined_value.get_cpp_const_type() + " " + self.get_cpp_const_name(defined_value) + " = " + defined_value.get_cpp_value() + ";"

	@memoized
	def get_cpp_defined_value_name(self, defined_value):
		if self.cpp_prefix:
			return self.cpp_prefix + defined_value.name
		else:
			return defined_value.name 

	@memoized
	def get_sphinx_docstring(self):
		return docstring_fixes(subst_non_class_refs(self.description))
gxapi.definition.typeDefinition()._SetSupersedingClass(definition_class)			

def resolve_enum_type_from_description(type_name, description):
	if description and type_name == "int":
		defines = re.findall("<define>(.+?)</define>", description)
		if len(defines) == 1:
			if not defines[0] in global_collection.known_definitions:
				raise Exception('Unknown definition indicated for parameter or return value: ' + defines[0])
			return defines[0]
	return type_name
   
class parameter_class(gxapi.parameter.typeDefinition()):
	@memoized
	def is_class(self):
		return is_class(self.type)
	
	@memoized
	def is_var_type(self):
		return self.type != "var string" and self.type.startswith("var ")
	
	@memoized
	def get_type(self):
		if self.is_var_type():
			return self.type[4:]
		else:
			return self.type
	
	@memoized
	def __cpp_type(self, no_pointer):
		return get_cpp_type(resolve_enum_type_from_description(self.get_type(), self.description), no_pointer)

	def cpp_type(self, no_pointer=False):
		return self.__cpp_type(no_pointer)

	@memoized
	def cpp_python_wrap_type(self):
		if self.is_cpp_long_equivalent():
			type_name = "int32_t"
		else:
			type_name = self.cpp_type()

		if type_name == "gx_string_type&":
			return "str_ref&"
		elif self.is_var_type():
			if type_name == "int32_t":
				return "int_ref&"
			elif type_name == "double":
				return "float_ref&"
			elif type_name == "bool":
				return "bool_ref&"
			else:
				raise Exception("Unexpected var type: " + type_name)
		else:
			return type_name

	@memoized
	def cpp_python_docstring_type(self):
		if self.is_cpp_long_equivalent():
			type_name = "int32_t"
		else:
			type_name = self.cpp_type(no_pointer=True)
		if type_name == "double":
			type_name = "float"
		elif type_name == "int32_t":
			type_name = "int"
		elif type_name == "const gx_string_type&":
			type_name = "str"
		elif type_name == "gx_string_type&":
			type_name = "str_ref"
		if self.is_var_type():
			type_name = type_name + "_ref"
		return type_name

	@memoized
	def cpp_python_wrap_cast(self):
		type_name = self.cpp_type()

		if not type_name == "int32_t" and self.is_cpp_long_equivalent():
			if self.is_var_type():
				return "(" + type_name + "&)"
			else:
				return "(" + type_name + ")"
		else:
			return ""
		
	@memoized
	def is_val_type(self):
		return self.get_type() == 'intval' or self.get_type() == 'HWND' or self.get_type() == 'HDC'
		
	@memoized
	def is_param_in_type(self):
		return self.get_type().startswith("void (")		   
		
	@memoized
	def is_cpp_long_equivalent(self):
		if not self.is_val_type():
			return get_is_cpp_long_equivalent(self.cpp_type())
		else:
			return False

	@memoized
	def cpp_cast_start(self):
		if self.is_cpp_long_equivalent():
			if self.is_var_type():
				return "reinterpret_cast<long*>("
			else:
				return "reinterpret_cast<const long*>("
		else:
			return ""

	@memoized
	def cpp_cast_end(self):
		if self.is_cpp_long_equivalent():
			return ")"
		else:
			return ""

	@memoized
	def get_python_docstring(self):
		return docstring_literal_para(self.description)
gxapi.parameter.typeDefinition()._SetSupersedingClass(parameter_class)


class method_class(gxapi.method.typeDefinition()):
	@memoized
	def external_name(self):
		if self.externalname:
			return self.externalname
		else:
			return self.name
	
	@memoized
	def returns_class(self):
		return is_class(self.returnval.type)
		
	@memoized
	def get_return_class(self):
		return get_class(self.returnval.type)
		
	@memoized
	def __cpp_return_type(self, no_pointer):
		return get_cpp_type(resolve_enum_type_from_description(self.returnval.type, self.returnval.description), no_pointer = no_pointer)
		
	def cpp_return_type(self, no_pointer=False):
		return self.__cpp_return_type(no_pointer)

	@memoized
	def __python_wrap_return_type(self, no_pointer):
		type_name = self.cpp_return_type(no_pointer = no_pointer)
		if get_is_cpp_long_equivalent(type_name):
			return "int32_t"
		else:
			return type_name

	def python_wrap_return_type(self, no_pointer=False):
		return self.__python_wrap_return_type(no_pointer)

	@memoized
	def cpp_return_cast(self):
		return get_cpp_return_cast(self.cpp_return_type())
		
	@memoized
	def is_app(self):
		return self.license.endswith('_app')
gxapi.method.typeDefinition()._SetSupersedingClass(method_class)

class ext_parameter_info(object):
	def __init__(self, index=None, parameter=None, size_parameter=None, size_parameter_index=None, real_index=None):
		self.index = index
		self.parameter = parameter
		self.size_parameter_index = size_parameter_index
		self.size_parameter = size_parameter
		self.real_index = real_index

class int_parameter_info(object):
	def __init__(self, self_handle=False, ext_index=None, parameter=None, size_parameter=None, size_parameter_index=None,gxclass=None):
		self.self_handle = self_handle
		self.parameter = parameter
		self.size_parameter_index = size_parameter_index
		self.size_parameter = size_parameter
		self.ext_index = ext_index
		self.gxclass = gxclass

		
def get_rest_docstring_type_name(type_name):
	if type_name in ["float", "bool", "int", "str", "None"]:
		return type_name
	else:
		return ":class:`geosoft.gxapi." + type_name + "`"

class gx_class(gxapi.gxclass.typeDefinition()):
	@memoized
	def is_method_static(self, method):
		if len(method.parameters.parameter) > 0:
			return parse_type(method.parameters.parameter[0].type) != self.name
		else:
			return True

	@memoized
	def get_method_ext_parameter_infos(self, method):
		ext_parameter_infos = []
		static = self.is_method_static(method)
		size_of_parameters_set = set()
		for parameter in method.parameters.parameter:
			if parameter.size_of_param:
				size_of_parameters_set.add(parameter.size_of_param)
				
		index = 1
		for i, parameter in enumerate(method.parameters.parameter):
			if (i == 0 and not static) or i in size_of_parameters_set:
				continue
			size_parameter_index = parameter.size_of_param
			size_parameter = None
			if size_parameter_index:
				size_parameter = method.parameters.parameter[size_parameter_index] 
			ext_parameter_infos.append(ext_parameter_info(index=index, parameter=parameter, size_parameter=size_parameter, size_parameter_index=size_parameter_index, real_index=i))
			index = index + 1
		return ext_parameter_infos
		
	@memoized
	def get_method_int_parameter_infos(self, method):
		int_parameter_infos = []
		static = self.is_method_static(method)
		size_of_parameters_set = set()
		for parameter in method.parameters.parameter:
			if parameter.size_of_param:
				size_of_parameters_set.add(parameter.size_of_param)
		
		index = 1
		for i, parameter in enumerate(method.parameters.parameter):
			self_handle = False
			if i in size_of_parameters_set:
				ext_index = None
			elif i == 0 and not static:
				ext_index = None
				self_handle = True
			else:
				ext_index = index
				index = index + 1
			size_parameter_index = parameter.size_of_param
			size_parameter = None
			if size_parameter_index:
				size_parameter = method.parameters.parameter[size_parameter_index] 
			int_parameter_infos.append(int_parameter_info(self_handle=self_handle, ext_index=ext_index, parameter=parameter, size_parameter=size_parameter, size_parameter_index=size_parameter_index, gxclass=get_class(parameter.type)))
		return int_parameter_infos

	@memoized
	def is_static(self):
		for methodgroup in self.methodgroups.methodgroup:
			for method in methodgroup.method:
				if not self.is_method_static(method):
					return False
		return True
		
	def _ext_method_name_camel(self, method):
		if method.name == "iCheckError_SYS":
			return "iCheckError"
		method_postfix = "_" + self.name
		method_name = method.external_name()
		if method.name.endswith(method_postfix):
			method_name = method_name[0 : len(method_name) - len(method_postfix)]
		if method_name.startswith("_") or (method_name.startswith("I") and len(method_name) > 2 and (method_name[1] == 'i' or (method_name[1] >= 'A' and method_name[1] <= 'Z'))):
			return method_name[1:]
		return method_name

	def _ext_method_name_no_camel(self, method):
		return convert_camel_case(self._ext_method_name_camel(method))

	def _ext_method_name_real_to_double(self, method):
		return self._ext_method_name_no_camel((method)).replace("_real", "_double")

	def _ext_method_name_no_polish(self, method):
		method_name = self._ext_method_name_real_to_double(method)
		return_type = method.cpp_return_type()
		if method_name.startswith("i_") or method_name.startswith("r_"):
			return method_name[2:]
		else:
			return method_name

	@memoized
	def ext_method_name(self, method):
		method_name = self._ext_method_name_no_polish(method)
		if method.cpp_pre:
			method_name = method.cpp_pre + method_name
		if method.cpp_post:
			method_name = method_name + method.cpp_post
		if self.name == "MATH":
			method_name = method_name + "_" # Stops keyword and macro collisions everywhere
		return method_name
        
	@memoized
	def py_method_name(self, method):
		method_name = self.ext_method_name(method)
		return method_name.strip("_")

	def get_python_docstring(self):
		docstring = docstring_literal_para(self.description)
		if self.notes:
			docstring = docstring + docstring_literal_note(self.notes)
		return docstring

	def generate_sphinx_description(self):
		return generate_sphinx_description(self.description)

	def get_python_method_docstring(self, method):
		return_type = method.python_wrap_return_type(no_pointer = True)
		if return_type == "void":
			return_type = "None"
		elif return_type == "double":
			return_type = "float"
		elif return_type == "int32_t":
			return_type = "int"

		signature = self.py_method_name(method) + "("
		restructured_text_params = ""
		
		first_parameter = False
		for parameter_info in self.get_method_ext_parameter_infos(method):
			if first_parameter:
				signature = signature + ", "
			else:
				first_parameter = True
			type_name = parameter_info.parameter.cpp_python_docstring_type()
			arg_name = "arg" + str(parameter_info.index)

			signature = signature + "(" + type_name + ")" + arg_name
			
			restructured_text_params = restructured_text_params + restructured_directive(":param " + arg_name + ":", parameter_info.parameter.description)
			restructured_text_params = restructured_text_params + restructured_directive(":type " + arg_name + ":", get_rest_docstring_type_name(type_name))

		signature = signature + ") -> " + return_type + ":"
		if method.returnval.description:
			restructured_text_params = restructured_text_params + restructured_directive(":returns:", method.returnval.description)
		restructured_text_params = restructured_text_params + restructured_directive(":rtype:", get_rest_docstring_type_name(return_type))
		
		docstring = docstring_multi_line(signature) + docstring_literal_para(method.description) + docstring_multi_line(restructured_text_params) + docstring_literal_version(method.available) 
		
		if method.notes:
		    docstring = docstring + docstring_literal_note(method.notes)

		if method.see_also:
		    docstring = docstring + docstring_literal_seealso(method.see_also)
		
		return docstring		

gxapi.gxclass.typeDefinition()._SetSupersedingClass(gx_class)

def object_from_pickled_file(pickled_file_path):
	with open(pickled_file_path, 'rb') as f:
		return pickle.load(f)
	
def pickle_object_with_makedir(object, pickled_file_path):
	pickled_file_dir = os.path.dirname(pickled_file_path)
	if not os.path.exists(pickled_file_dir):
		os.makedirs(pickled_file_dir)
	with open(pickled_file_path, 'wb') as f:
		pickle.dump(object, f, pickle.HIGHEST_PROTOCOL)

def gxapi_pickle(api_file_path, pickled_file_path):
	pickle_object_with_makedir(gxapi.CreateFromDocument(open(api_file_path).read()), pickled_file_path)
		

def gxapi_api_collection_pickle(pickle_source_dirs, pickled_file_path):
	api_coll = GXApiCollectionInfo([], {}, {}, {}, {}, {})
	
	files_dict = {}
	for source_dir in pickle_source_dirs.split(';'):
		for root, subFolders, files in os.walk(source_dir):
			for file in files:
				files_dict[file] = os.path.join(root, file)
		
	for file in OrderedDict(sorted(files_dict.items())):
		gxclass = object_from_pickled_file(files_dict[file])
		api_coll.known_classes[gxclass.name] = gxclass
		if (gxclass.handlename):
			api_coll.known_class_handles[gxclass.handlename] = gxclass
		if gxclass.name == "GEOSOFT":
			api_coll.classes.insert(0, gxclass)
		else:
			api_coll.classes.append(gxclass)

		for methodgroup in gxclass.methodgroups.methodgroup:
			for method in methodgroup.method:
				api_coll.known_methods[method.name] =  { 'gxclass': gxclass, 'method': method }
		
		for definition in gxclass.definitions.definition:
			api_coll.known_definitions[definition.name] = definition
			for defined_value in definition.defined_value:
				api_coll.known_definition_values[defined_value.name] = { 'gxclass': gxclass, 'definition': definition, 'defined_value': defined_value }

	pickle_object_with_makedir(api_coll, pickled_file_path)

def render_template(j2env, namespace_parts, build_version, output_dir, template_name, sort_classes=False):
	output_file = os.path.join(output_dir, template_name)
	print('Rendering: ' + output_file)
	template = j2env.get_template(template_name)
	open(output_file, 'w+').write(template.render(build_version=build_version, classes=sorted(global_collection.classes , key=lambda gxclass: gxclass.name) if sort_classes else global_collection.classes, namespace_parts=namespace_parts))
	

def render_python_imports(j2env, namespace_parts, output_dir):
	template = j2env.get_template('python_import.cpp')
	
	for gxclass in global_collection.classes:
		# TODO Expose CGEO::GetPtrVM and CGEO::GetPtrVV the way we do in C# (remove
		# comments from python_module.cpp when completed)
		# TODO expose void * and callback methods in PG class in a sensible way and
		# remove the nocpp="true" atribute on them
		if not gxclass.name == "GEO": 
			output_file = os.path.join(output_dir, "python_import_" + gxclass.name + ".cpp")
			print('Rendering: ' + output_file)
			open(output_file, 'w+').write(template.render(gxclass=gxclass, namespace_parts=namespace_parts))
	

def render_sphinx_rsts(j2env, namespace_parts, output_dir):
	template = j2env.get_template('class.rst')
	
	for gxclass in global_collection.classes:
		# TODO Expose CGEO::GetPtrVM and CGEO::GetPtrVV the way we do in C# (remove
		# comments from python_module.cpp when completed)
		# TODO expose void * and callback methods in PG class in a sensible way and
		# remove the nocpp="true" atribute on them
		if not gxclass.name == "GEO": 
			output_file = os.path.join(output_dir, "GX" + gxclass.name + ".rst")
			print('Rendering: ' + output_file)
			open(output_file, 'w+').write(template.render(gxclass=gxclass, namespace_parts=namespace_parts))

def generate_code(pickled_collection_file, namespace, build_version, output_dir):
	from jinja2 import Environment, FileSystemLoader
	global global_collection
	global __j2env
	
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
	
	namespace_parts = namespace.split('::')

	tools_root = os.getenv('TOOLS_ROOT')
	templates_dir = os.path.join(tools_root, 'msbuild', 'gx_python', 'gxapi_templates')
	astyle_tool = os.path.join(tools_root, 'utils', 'astyle.exe')
	
	j2env = Environment(loader=FileSystemLoader(templates_dir), 
						trim_blocks = True,
						lstrip_blocks = True)
						
	global_collection = object_from_pickled_file(pickled_collection_file)

	start = time.perf_counter()
	render_template(j2env, namespace_parts, build_version, output_dir, 'gxcpp_geogx.h')
	render_template(j2env, namespace_parts, build_version, output_dir, 'python_ref_wrappers.h')
	render_template(j2env, namespace_parts, build_version, output_dir, 'python_module.cpp')
	render_template(j2env, namespace_parts, build_version, output_dir, 'index.rst', sort_classes=True)
	render_template(j2env, namespace_parts, build_version, output_dir, 'toc.rst', sort_classes=True)	
	render_python_imports(j2env, namespace_parts, output_dir)
	render_sphinx_rsts(j2env, namespace_parts, output_dir)
	
	print('Formatting source code...')
	if not 0 == call([astyle_tool, '-n', '-N', '--style=allman', os.path.join(output_dir, '*.h')]):
		raise Exception(astyle_tool + " error!")
	if not 0 == call([astyle_tool, '-n', '-N', '--style=allman', os.path.join(output_dir, '*.cpp')]):
		raise Exception(astyle_tool + " error!")
	elapsed = time.perf_counter() - start
	print("Generation completed in %s seconds" % elapsed)
