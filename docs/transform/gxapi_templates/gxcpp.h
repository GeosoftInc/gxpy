#pragma once
{% block headers_start %}
Define headers_start in derived template!!
{% endblock headers_start %}

#include "stdint.h"
#include <assert.h>
#include <memory>
#include <string>
#include <vector>
#include <exception>
#include <functional>

#ifdef _UNICODE
typedef wchar_t gx_string_char_type;
#define gx_string_len(a) ::wcslen(a)
typedef std::wstring gx_string_type;
#define STRING_CHAR_SIZE 2
#define gx_string_literal(x) L ## x
#else
typedef char gx_string_char_type;
#define gx_string_len(a) ::strlen(a)
typedef std::string gx_string_type;
#define STRING_CHAR_SIZE 1
#define gx_string_literal(x) x
#endif

#ifdef GXPYTHON
np::ndarray make_ndarray(size_t elements, bp::object dtype_obj, int32_t& gs_type, size_t& total_size);
np::ndarray validate_and_make_contiguous_ndarray(np::ndarray np_array, size_t& elements, int32_t& gs_type, size_t& total_size);
np::ndarray validate_and_make_2d_contiguous_ndarray(np::ndarray np_array, size_t& num_rows, size_t& num_columns, int32_t& gs_type, size_t& total_size);
#endif

{% for namespace_part in namespace_parts %}
namespace {{ namespace_part }} {
{% endfor %}
namespace {% block namespace_part %}Define namespace_part in derived template!!{% endblock %} {

{% for gxclass in classes %}
{% for definition in gxclass.definitions.definition %}{% if not definition.name == "GEO_BOOL" and not definition.constant and not definition.null_handle %}
enum {{ definition.name }}
{
{% for defined_value in definition.defined_value %}
{{ definition.get_cpp_defined_value_name(defined_value) }} = {{ defined_value.get_cpp_value() }}{% if not loop.last %},{% endif %}

{% endfor %}
};

{% endif %}{% endfor %}
{% endfor %}

template<typename T>
struct gs_cpp_type
{
private:
	gs_cpp_type() {}

public:
	static GS_TYPES type()
	{
		static_assert(false, "Type does not map to supported GS_TYPES");
	}
};

template<> struct gs_cpp_type<int8_t>    { static GS_TYPES type() { return GS_BYTE; } };
template<> struct gs_cpp_type<uint8_t>   { static GS_TYPES type() { return GS_UBYTE; } };
template<> struct gs_cpp_type<int16_t>   { static GS_TYPES type() { return GS_SHORT; } };
template<> struct gs_cpp_type<uint16_t>  { static GS_TYPES type() { return GS_USHORT; } };
template<> struct gs_cpp_type<int32_t>   { static GS_TYPES type() { return GS_LONG; } };
template<> struct gs_cpp_type<uint32_t>  { static GS_TYPES type() { return GS_ULONG; } };
template<> struct gs_cpp_type<int64_t>   { static GS_TYPES type() { return GS_LONG64; } };
template<> struct gs_cpp_type<uint64_t>  { static GS_TYPES type() { return GS_ULONG64; } };
template<> struct gs_cpp_type<float>     { static GS_TYPES type() { return GS_FLOAT; } };
template<> struct gs_cpp_type<double>    { static GS_TYPES type() { return GS_DOUBLE; } };



{% for gxclass in classes %}
{% for definition in gxclass.definitions.definition %}{% if not definition.name == "GEO_BOOL" and definition.constant and not definition.null_handle %}
{% if not definition.single_constant %}namespace {{ definition.name }} { {% endif %}

{% for defined_value in definition.defined_value %}
{{ definition.get_cpp_const_declaration(defined_value) }}
{% endfor %}
{% if not definition.single_constant %}}{% endif %}


{% endif %}{% endfor %}
{% endfor %}

class GXCancel : virtual public std::exception
{
};

class GXExit : virtual public std::exception
{
};

class GXError : virtual public std::exception
{
public:
	explicit GXError(const gx_string_type& message)
		: message_(message)
	{
	}

	explicit GXError(const gx_string_type& message, const gx_string_type& module, int32_t error_number)
		: message_(message)
		, module_(module)
		, error_number_(error_number)
	{
	}

	const gx_string_type& message() const { return message_; }
	const gx_string_type& module() const { return module_; }
	int32_t error_number() const { return error_number_; }

private:
	gx_string_type message_;
	gx_string_type module_;
	int32_t error_number_;
};

class GXAPIError : virtual public std::exception
{
public:
	explicit GXAPIError(const gx_string_type& message)
		: message_(message)
	{
	}
	
	gx_string_type message() const
	{
		return message_;
	}
private:
	gx_string_type message_;
};

{% for gxclass in classes %}{% if not gxclass.nocpp %}
class GX{{ gxclass.name }};
typedef std::shared_ptr<GX{{ gxclass.name }}> GX{{ gxclass.name }}Ptr;
{%endif %}{% endfor %}

class GXContext;
typedef std::shared_ptr<GXContext> GXContextPtr;
class GXContext : public std::enable_shared_from_this<GXContext>
{
private:
    
{% for gxclass in classes %}{% if not gxclass.nocpp %}
    friend class GX{{ gxclass.name }};
{%endif %}{% endfor %}

{% block gx_context_private %}	
{% endblock gx_context_private %}	


	template<class GXClass>
	std::shared_ptr<GXClass> createPtr(int32_t handle)
	{
		return std::shared_ptr<GXClass>(new GXClass(handle));
	}

	template<class GXClass>
	std::shared_ptr<GXClass> createNullHandlePtr()
	{
        	return std::shared_ptr<GXClass>(new GXClass(0));
	}

	static const int32_t null_handle = 0;
	template<class GXClass>
	const int32_t& handle(std::shared_ptr<GXClass> obj)
	{
		if (!obj)
                return null_handle;
		return obj->handle_;
	}

public:
{% block gx_context_public %}
{% endblock gx_context_public %}		
};	
	
{% for gxclass in classes %}{% if not gxclass.nocpp %}
{% set class_name = "GX" ~ gxclass.name %}
class {{ class_name }}
{
{% if gxclass.is_static() %}
private:
    {{ class_name }}();
    ~{{ class_name }}();
public:
{% else %}
private:
    friend class GXContext;
    
    GXContextPtr gx_;
    int32_t handle_;

    {{ class_name }}(int32_t handle) 
     : gx_(GXContext::current()), handle_(handle)
    {
    }

public:
    static {{ class_name }}Ptr null() { return GXContext::current()->createNullHandlePtr<{{ class_name }}>(); }
	 bool is_null() { return handle_ == 0; }

	int32_t _internal_handle() { return handle_; }

{% endif %}
    

{% for methodgroup in gxclass.methodgroups.methodgroup %}
    {% for method in methodgroup.method %}{% if not method.obsolete and not method.nocpp %}{% if not (gxclass.name == "BF" and gxclass.ext_method_name(method) == "destroy") -%}
{% if gxclass.ext_method_name(method) == "destroy" or gxclass.ext_method_name(method) == "destroy_ex" %}
~{{ class_name }}()
{% else %}
{%if method.cpp_decl %}{{ method.cpp_decl }}{% else %}
{% if gxclass.is_method_static(method) %}static {% endif %}
{{ method.cpp_return_type() }} {{ gxclass.ext_method_name(method) }}(
{%- for parameter_info in gxclass.get_method_ext_parameter_infos(method) -%}
{{ parameter_info.parameter.cpp_type() }}{%if parameter_info.parameter.is_var_type() %}&{% endif %} {%if not parameter_info.parameter.is_param_in_type() %}param{{ parameter_info.index }}{% endif %}
{%- if not loop.last -%}, {% endif -%}
{%- endfor -%}
)
{% endif %}{% endif %}
    {
{% if gxclass.ext_method_name(method) == "destroy" or gxclass.ext_method_name(method) == "destroy_ex" %}
        if (handle_ == 0)
            return;
{% endif %}
{% block method_body scoped %}{% endblock method_body %}
    }

{% endif %}{% endif %}{% endfor %}
{% endfor %}

};
{% endif %}{% endfor %}

#ifndef GX_EXLUDE_IMPL
thread_local std::weak_ptr<GXContext> GXContext::currentContext;
#endif // GX_EXLUDE_IMPL

}
{% for namespace_part in namespace_parts %}
} 
{% endfor %}