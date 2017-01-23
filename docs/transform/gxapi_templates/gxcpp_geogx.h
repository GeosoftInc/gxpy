{% extends "gxcpp.h" %}

{% block headers_start %}
#define C_MICROSOFT
#include <gx_extern.h>
#include <gx_lib.h>
{% endblock %}

{% block namespace_part %}geogx{% endblock %} {

{% block gx_context_private %}	
void *pGeo;
bool destroyGeo;
static thread_local std::weak_ptr<GXContext> currentContext;

GXContext(void *_pGeo)
	: pGeo(_pGeo)
	, destroyGeo(false)
{
}

GXContext(const gx_string_type& application, const gx_string_type& version, HWND hParentWnd)
	: pGeo(nullptr)
	, destroyGeo(true)
{
	gx_string_char_type geoError[4096];
	pGeo = pCreate_GEO(application.c_str(), version.c_str(), 0, hParentWnd, 0, geoError, _countof(geoError));
	if (pGeo == nullptr)
	{
		gx_string_type error = gx_string_literal("Unable to initialize Geosoft libraries: ");
		error += geoError;
		throw GXAPIError(error);
	}
}

void throw_on_error()
{
	long lTerminateReason = 0;
	if (iCheckTerminate_SYS(pGeo, &lTerminateReason))
	{
		auto iErr = iCheckError_SYS(pGeo);
		assert(iErr != 0);

		if (lTerminateReason == 0)
			throw GXExit();
		else if (lTerminateReason == -1)
			throw GXCancel();
		else
		{
			int32_t error_number;
			gx_string_type error_message, error_module;
			int32_t moduleSize = STR_DEFAULT * STRING_CHAR_SIZE;
			int32_t messageSize = STR_ERROR * STRING_CHAR_SIZE;
			error_module.resize(STR_DEFAULT);
			error_message.resize(STR_ERROR);
			short ret = sGetError_GEO(pGeo, (gx_string_char_type*)error_module.data(), moduleSize, (gx_string_char_type*)error_message.data(), messageSize, reinterpret_cast<long*>(&error_number));
			error_module.resize(gx_string_len(error_module.c_str()));
			error_message.resize(gx_string_len(error_message.c_str()));
			if (error_number == 21023 || error_number == 21031 || // These two due to GXX asserts, Abort_SYS etc
				error_number == 31009 || error_number == 31011) // wrapper bind errors
				throw GXAPIError(error_message);
			else
				throw GXError(error_message, error_module, error_number);
		}
	}
}

{% endblock gx_context_private %}

{% block gx_context_public %}
void * _internal_p() { return pGeo; }
static GXContextPtr create_internal(void *pGeo)
{
	if (auto cur_ctx = currentContext.lock())
		return cur_ctx;

	auto ctx = GXContextPtr(new GXContext(pGeo));
	currentContext = ctx;
	return ctx;
}
static GXContextPtr create(const gx_string_type& application, const gx_string_type& version, HWND hParentWnd = nullptr)
{
	if (auto cur_ctx = currentContext.lock())
		return cur_ctx;

	auto ctx = GXContextPtr(new GXContext(application, version, hParentWnd));
	currentContext = ctx;
	return ctx;
}
static GXContextPtr current()
{
	 if (auto cur_ctx = currentContext.lock())
		return cur_ctx;
	else
		throw GXAPIError(gx_string_literal("A GXContext has not been created on this thread, or has been destroyed."));
}

HWND get_main_wnd()
{
	return hGetMainWnd_GEO();
}

HWND get_active_wnd()
{
	return hGetActiveMainWnd_GEO();
}

void enable_application_windows(bool enable)
{
	EnableApplicationWindows_GEO(enable);
}

~GXContext()
{
	if (destroyGeo && pGeo)
		Destroy_GEO(pGeo);
}
{% endblock gx_context_public %}

{% block method_body %}
{% if gxclass.is_method_static(method) %}GXContextPtr gx_ = GXContext::current();{% endif %}
{%- if method.cpp_impl %}{{ method.cpp_impl }}{% else -%}
{%- for parameter_info in gxclass.get_method_int_parameter_infos(method) -%}
{%- if not parameter_info.self_handle and not parameter_info.ext_index -%}
		int32_t paramSize{{ loop.index0 }} = {{ parameter_info.parameter.defaultlength }} * STRING_CHAR_SIZE;
{% endif -%}
{%- endfor -%}
{%- for parameter_info in gxclass.get_method_int_parameter_infos(method) -%}
{%- if parameter_info.size_parameter_index -%}
		param{{ parameter_info.ext_index }}.resize({{ parameter_info.size_parameter.defaultlength }});
{% endif -%}
{%- if parameter_info.parameter.cpp_type() == 'bool' -%}long paramBool{{ parameter_info.ext_index }} = param{{ parameter_info.ext_index }} ? 1 : 0;
{% endif -%}
{%- endfor -%}

{% if method.cpp_return_type() != 'void' %}{% if method.returns_class() %}int32_t ret = {% else %}{{ method.cpp_return_type() }} ret = {{ method.cpp_return_cast() }}{% endif %}{% endif -%}
{% if method.is_app() %}App_{% endif %}{{ method.external_name() }}(
gx_->pGeo
{%- for parameter_info in gxclass.get_method_int_parameter_infos(method) -%}
, {%if parameter_info.self_handle -%}
reinterpret_cast<const long*>(&handle_)
{%- else -%}
{%- if parameter_info.gxclass -%}
reinterpret_cast<const long*>(&gx_->handle(param{{ parameter_info.ext_index }}))
{%- else -%}
{%- if not parameter_info.ext_index -%}
{%- if not parameter_info.parameter.is_val_type() -%}reinterpret_cast<const long*>(&{%- endif -%}paramSize{{ loop.index0 }} )
{%- else -%}
{%- if parameter_info.parameter.cpp_type() == 'const gx_string_type&' -%}
param{{ parameter_info.ext_index }}.c_str()
{%- else -%}
{%- if parameter_info.parameter.cpp_type() == 'gx_string_type&' -%}
(gx_string_char_type*)param{{ parameter_info.ext_index }}.data()
{%- else -%}
{%- if not parameter_info.parameter.is_val_type() and not parameter_info.parameter.is_param_in_type() -%}{{ parameter_info.parameter.cpp_cast_start() }}&{%- endif -%}param{%- if parameter_info.parameter.cpp_type() == 'bool' -%}Bool{%- endif -%}{{ parameter_info.ext_index }}{{ parameter_info.parameter.cpp_cast_end() }}
{%- endif -%}
{%- endif -%}
{%- endif -%}
{%- endif -%}
{%- endif -%}
{%- endfor -%}
		);{%- if not gxclass.ext_method_name(method) == "destroy" and not gxclass.ext_method_name(method) == "destroy_ex" -%}
		gx_->throw_on_error();
{%- endif -%}{%- for parameter_info in gxclass.get_method_int_parameter_infos(method) -%}
{%- if parameter_info.size_parameter_index -%}
		param{{ parameter_info.ext_index }}.resize(gx_string_len(param{{ parameter_info.ext_index }}.c_str()));
{% endif -%}
{%- if parameter_info.parameter.cpp_type() == 'bool' and parameter_info.parameter.is_var_type() -%}
		param{{ parameter_info.ext_index }} = paramBool{{ parameter_info.ext_index }} != 0 ? true : false;
{% endif -%}
{%- endfor -%}
		{%- if method.cpp_return_type() != 'void' %}
			return {% if method.returns_class() %}gx_->createPtr<GX{{ method.get_return_class().name }}>(ret){% else %}ret{% endif %};
		{% endif -%}
{%- endif -%}
{% endblock method_body %}
