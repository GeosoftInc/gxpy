{% import 'macros.i' as macros %}
#include "stdafx.h"

using namespace boost::python;
using boost::python::init;

{% set class_name = "GX" ~ gxclass.name %}

// Dummy classes
{% if gxclass.nocpp %} 
class {{ class_name }} {};
{% endif %}


{% for methodgroup in gxclass.methodgroups.methodgroup %}{% for method in methodgroup.method %}{%if method.python_impl %}
{{ method.python_impl }}
{% elif not method.obsolete and not method.nocpp and not gxclass.ext_method_name(method) == "destroy" and not gxclass.ext_method_name(method) == "destroy_ex" %}
inline {{ method.python_wrap_return_type() }} {{ class_name }}_wrap_{{ gxclass.ext_method_name(method) }}(
{%- if not gxclass.is_method_static(method) %}{{ class_name }}Ptr self{% endif %}
{%- for parameter_info in gxclass.get_method_ext_parameter_infos(method) -%}
{% if not gxclass.is_method_static(method) and loop.first %}, {% endif %}
{{ parameter_info.parameter.cpp_python_wrap_type() }} {%if not parameter_info.parameter.is_param_in_type() %}arg{{ parameter_info.index }}{% endif %}
{%- if not loop.last -%}, {% endif -%}
{%- endfor -%})
    {
{% if method.cpp_return_type() != 'void' %}{{ method.cpp_return_type() }} ret = {% endif -%}
{%- if gxclass.is_method_static(method) %}{{ class_name }}::{% else %}self->{% endif %}{{ gxclass.ext_method_name(method) }}(
{%- for parameter_info in gxclass.get_method_ext_parameter_infos(method) -%}
{%- if parameter_info.gx_parameter -%}
gxapi
{%- else -%}
{%if not parameter_info.parameter.is_param_in_type() %}{{ parameter_info.parameter.cpp_python_wrap_cast() }}arg{{ parameter_info.index }}{% endif %}
{%- endif -%}
{%- if not loop.last -%}, {% endif -%}
{%- endfor -%});
{% if method.cpp_return_type() != 'void' %}return ret;{% endif %}
	}
{% endif %}{% endfor %}
{% endfor %}

void gxPythonImport{{ class_name }}()
{
{% if not gxclass.name == "GEOSOFT" %} 
	class_<{{ class_name }}, {% if gxclass.is_static() %}boost::noncopyable{% else %}{{ class_name }}Ptr{% endif %}> pyClass("{{ class_name }}", {{ gxclass.get_python_docstring() }} , no_init);

{% if not gxclass.is_static() %}
    pyClass.def("null", &{{ class_name }}::null, "null() -> {{ class_name }}\n\nA null (undefined) instance of :class:`geosoft.gxapi.{{ class_name }}`\n\n:returns: A null :class:`geosoft.gxapi.{{ class_name }}`\n:rtype: :class:`geosoft.gxapi.{{ class_name }}`\n").staticmethod("null");
	 pyClass.def("is_null", &{{ class_name }}::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.{{ class_name }} is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.{{ class_name }}`, False otherwise.\n:rtype: bool`\n");
	pyClass.def("_internal_handle", &{{ class_name }}::_internal_handle);{% endif %}

{% for methodgroup in gxclass.methodgroups.methodgroup %}{% for method in methodgroup.method %}{%if method.python_import %}
{{ method.python_import }}
{% elif not method.obsolete and not method.nocpp and not gxclass.ext_method_name(method) == "destroy" and not gxclass.ext_method_name(method) == "destroy_ex" %}
{% set method_name = gxclass.ext_method_name(method) %}
{% set py_method_name = gxclass.py_method_name(method) %}
pyClass.def("{{ py_method_name }}", &{{ class_name }}_wrap_{{ method_name }}, {{ gxclass.get_python_method_docstring(method) }}){% if gxclass.is_method_static(method) %}.staticmethod("{{ py_method_name }}"){% endif %};
{% endif %}{% endfor %}{% endfor %}
{% endif %}

{% for definition in gxclass.definitions.definition %}{% if not definition.name == "GEO_BOOL" and not definition.null_handle %}
{% for defined_value in definition.defined_value %}
	scope().attr("{{ defined_value.name }}") = {{ defined_value.get_python_value() }};
{% endfor %}
{% endif %}{% endfor %}	
}

