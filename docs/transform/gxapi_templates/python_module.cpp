{% import 'macros.i' as macros %}
#include "stdafx.h"

using namespace boost::python;
using boost::python::init;

PyObject* PyGXCancel;
PyObject* PyGXExit;
PyObject* PyGXError;
PyObject* PyGXAPIError;

void translate_gx_cancel(GXCancel const& e)
{
	PyErr_SetNone(PyGXCancel);
}

void translate_gx_exit(GXExit const& e)
{
	PyErr_SetNone(PyGXExit);
}


void translate_gx_api_error(GXAPIError const& e)
{
    auto message = PyUnicode_FromWideChar(e.message().c_str(), -1);
    auto utf8_message = PyUnicode_AsUTF8String(message);
    Py_DECREF(message);
    PyErr_SetString(PyGXAPIError, PyBytes_AsString(utf8_message));
    Py_DECREF(utf8_message);
}


static int
set_error_attr(PyObject *err, const char *name, int value)
{
	PyObject *v = PyLong_FromLong(value);

	if (v == NULL || PyObject_SetAttrString(err, name, v) == -1) {
		Py_XDECREF(v);
		return 0;
	}
	Py_DECREF(v);
	return 1;
}

static int
set_error_attr(PyObject *err, const char *name, gx_string_type value)
{
	PyObject *v = PyUnicode_FromWideChar(value.c_str(), -1);

	if (v == NULL || PyObject_SetAttrString(err, name, v) == -1) {
		Py_XDECREF(v);
		return 0;
	}
	Py_DECREF(v);
	return 1;
}

void translate_gx_error(GXError const& e)
{
	auto message = PyUnicode_FromWideChar(e.message().c_str(), -1);
	auto err = PyObject_CallFunction(PyGXError, "O", message);
	Py_DECREF(message);
	if (err != NULL
		&& set_error_attr(err, "module", e.module())
		&& set_error_attr(err, "number", e.error_number())) {
		PyErr_SetObject(PyGXError, err);
	}
	Py_XDECREF(err);
}

template<typename T>
np::ndarray make_ndarray(size_t elements, int32_t& gs_type, size_t& total_size)
{
	gs_type = gs_cpp_type<T>::type();
	total_size = elements*sizeof(T);
	return np::empty(bp::make_tuple(elements), np::dtype::get_builtin<T>());
}

np::ndarray make_ndarray(size_t elements, bp::object dtype_obj, int32_t& gs_type, size_t& total_size)
{
	np::dtype dt(dtype_obj);

	if (np::equivalent(dt, np::dtype::get_builtin<int8_t>()))
		return make_ndarray<int8_t>(elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<uint8_t>()))
		return make_ndarray<uint8_t>(elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<int16_t>()))
		return make_ndarray<int16_t>(elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<uint16_t>()))
		return make_ndarray<uint16_t>(elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<int32_t>()))
		return make_ndarray<int32_t>(elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<uint32_t>()))
		return make_ndarray<uint32_t>(elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<int64_t>()))
		return make_ndarray<int64_t>(elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<uint64_t>()))
		return make_ndarray<uint64_t>(elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<float>()))
		return make_ndarray<float>(elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<double>()))
		return make_ndarray<double>(elements, gs_type, total_size);
	else
        throw GXAPIError(gx_string_literal("Numpy array type does not map to supported GS_TYPES"));
}

template<typename T>
np::ndarray make_contiguous_ndarray(np::ndarray np_array, size_t& elements, int32_t& gs_type, size_t& total_size)
{
	elements = 1;
	for (int i = 0; i < np_array.get_nd(); i++)
		elements *= np_array.shape(i);
	gs_type = gs_cpp_type<T>::type();
	total_size = elements*sizeof(T);

	if (np_array.get_flags() & np::ndarray::C_CONTIGUOUS)
		return np_array;
	else
		return np::from_object(np_array, np::ndarray::C_CONTIGUOUS);
}

np::ndarray validate_and_make_contiguous_ndarray(np::ndarray np_array, size_t& elements, int32_t& gs_type, size_t& total_size)
{
	auto dt = np_array.get_dtype();

	if (np::equivalent(dt, np::dtype::get_builtin<int8_t>()))
		return make_contiguous_ndarray<int8_t>(np_array, elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<uint8_t>()))
		return make_contiguous_ndarray<uint8_t>(np_array, elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<int16_t>()))
		return make_contiguous_ndarray<int16_t>(np_array, elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<uint16_t>()))
		return make_contiguous_ndarray<uint16_t>(np_array, elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<int32_t>()))
		return make_contiguous_ndarray<int32_t>(np_array, elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<uint32_t>()))
		return make_contiguous_ndarray<uint32_t>(np_array, elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<int64_t>()))
		return make_contiguous_ndarray<int64_t>(np_array, elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<uint64_t>()))
		return make_contiguous_ndarray<uint64_t>(np_array, elements, gs_type, total_size);
	else if (np::equivalent(dt, np::dtype::get_builtin<float>()))
		return make_contiguous_ndarray<float>(np_array, elements, gs_type, total_size);
    else if (np::equivalent(dt, np::dtype::get_builtin<double>()))
        return make_contiguous_ndarray<double>(np_array, elements, gs_type, total_size);
    else
        throw GXAPIError(gx_string_literal("Numpy array type does not map to supported GS_TYPES"));
}

np::ndarray validate_and_make_2d_contiguous_ndarray(np::ndarray np_array, size_t& num_rows, size_t& num_columns, int32_t& gs_type, size_t& total_size)
{
    if (np_array.get_nd() != 2)
        throw GXAPIError(gx_string_literal("Only 2D Numpy arrays supported for this method"));
    num_rows = np_array.shape(0);
    num_columns = np_array.shape(1);

	size_t elements;
	return validate_and_make_contiguous_ndarray(np_array, elements, gs_type, total_size);
}

/* TODO  Expose CGEO::GetPtrVM and CGEO::GetPtrVV" the way we do in C# */
{% for gxclass in classes %}{% if not gxclass.name == "GEO" %} 
void gxPythonImportGX{{ gxclass.name }}();{% endif %}{% endfor %}


{{ macros.export_ref("double", "float_ref", "GEO_DUMMY::rDUMMY") }}
{{ macros.export_ref("int32_t", "int_ref", "GEO_DUMMY::iDUMMY") }}
{{ macros.export_ref("bool", "bool_ref", "false" ) }}
{{ macros.export_ref("const std::wstring&", "str_ref", 'L""') }}

GXContextPtr gx_context_create_internal(size_t iGeo)
{
	return GXContext::create_internal(reinterpret_cast<void*>(iGeo));
}

size_t gx_context_internal_p(GXContextPtr self)
{
	return reinterpret_cast<size_t>(self->_internal_p());
}

inline size_t GXContext_wrap_get_main_wnd(GXContextPtr self)
{
	return (size_t)self->get_main_wnd();
}

inline size_t GXContext_wrap_get_active_wnd(GXContextPtr self)
{
    return (size_t)self->get_active_wnd();
}

inline GXContextPtr GXContext_wrap_create(const gx_string_type& application, const gx_string_type& version, size_t hParentWnd = 0)
{
    return GXContext::create(application, version, (HWND)hParentWnd);
}

BOOST_PYTHON_FUNCTION_OVERLOADS(create_member_overloads, GXContext_wrap_create, 2, 3)

HWND hWndConsole = nullptr;

inline bool has_ui_console(GXContextPtr self)
{
    return hWndConsole && ::IsWindow(hWndConsole);
}

inline bool is_ui_console_visible(GXContextPtr self)
{
    return has_ui_console(self) && ::IsWindowVisible(hWndConsole);
}

inline void show_ui_console(GXContextPtr self, bool show)
{
    if (has_ui_console(self))
    {
        if (show)
        {
            ShowWindow(hWndConsole, SW_SHOW);
            BringWindowToTop(hWndConsole);
        }
        else
            ShowWindow(hWndConsole, SW_HIDE);
    }
}

inline void clear_ui_console(GXContextPtr self)
{
    if (has_ui_console(self))
    {
        COORD coordScreen = { 0, 0 };
        DWORD cCharsWritten;
        CONSOLE_SCREEN_BUFFER_INFO csbi;
		DWORD dwConSize;

		HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
		GetConsoleScreenBufferInfo(hStdOut, &csbi);
		dwConSize = csbi.dwSize.X * csbi.dwSize.Y;
		FillConsoleOutputCharacter(hStdOut, (TCHAR) ' ', dwConSize, coordScreen, &cCharsWritten);
		GetConsoleScreenBufferInfo(hStdOut, &csbi);
		FillConsoleOutputAttribute(hStdOut, csbi.wAttributes, dwConSize, coordScreen, &cCharsWritten);
		SetConsoleCursorPosition(hStdOut, coordScreen);
	}
}


struct stdout_stream_helper
{
	void write(char *stuff)
	{
		DWORD RetVal;
		WriteFile(GetStdHandle(STD_OUTPUT_HANDLE), stuff, (DWORD)strlen(stuff), &RetVal, NULL);
	}

	void flush()
	{
		FlushFileBuffers(GetStdHandle(STD_OUTPUT_HANDLE));
	}
};

struct stdin_stream_helper
{
    // Only readline supported for now (Python input call works)
    std::wstring readline()
    {
		 if (hWndConsole && ::IsWindow(hWndConsole))
		 {
			 ShowWindow(hWndConsole, SW_SHOW);
			 BringWindowToTop(hWndConsole);

			 wchar_t lpBuffer[1024];
			 DWORD nRead;

			 ReadConsole(GetStdHandle(STD_INPUT_HANDLE), lpBuffer, 1023, &nRead, NULL);
			 lpBuffer[nRead] = '\0';
			 return lpBuffer;
		 }
		 else
			 return L"";
    }
};
struct stderr_stream_helper
{
	void write(char *stuff)
	{
		DWORD RetVal;
		WriteFile(GetStdHandle(STD_ERROR_HANDLE), stuff, (DWORD)strlen(stuff), &RetVal, NULL);
	}

	void flush()
	{
		FlushFileBuffers(GetStdHandle(STD_ERROR_HANDLE));
    }
};

inline void gx_redirect_std_streams()
{
	hWndConsole = GetConsoleWindow();
	if (hWndConsole)
	{
		object main = import("__main__");
		object py_ = main.attr("__dict__");
		exec(
			"import sys\n"
			"import geosoft.gxapi as gxapi\n"
			"sys.stdout = gxapi._stdout_stream_helper()\n"
			"sys.stdin = gxapi._stdin_stream_helper()\n"
			"sys.stderr = gxapi._stderr_stream_helper()\n", py_, py_);
	}
}

{% set build_version_components = build_version.split('.') %}

BOOST_PYTHON_MODULE(gxapi)
{
	docstring_options local_docstring_options(true, false, false);

	np::initialize();

	scope().attr("__gxapi_version__") = "{{ build_version }}";

	 PyGXCancel = PyErr_NewException("geosoft.gxapi.GXCancel", PyExc_SystemExit, NULL);
	 scope().attr("GXCancel") = detail::new_reference(PyGXCancel);
	 register_exception_translator<GXCancel>(&translate_gx_cancel);

	 PyGXExit = PyErr_NewException("geosoft.gxapi.GXExit", PyExc_SystemExit, NULL);
	 scope().attr("GXExit") = detail::new_reference(PyGXExit);
	 register_exception_translator<GXExit>(&translate_gx_exit);

    PyGXAPIError = PyErr_NewException("geosoft.gxapi.GXAPIError", PyExc_RuntimeError, NULL);
    scope().attr("GXAPIError") = detail::new_reference(PyGXAPIError);
    register_exception_translator<GXAPIError>(&translate_gx_api_error);

	 PyGXError = PyErr_NewException("geosoft.gxapi.GXError", PyExc_RuntimeError, NULL);
	 scope().attr("GXError") = detail::new_reference(PyGXError);
    register_exception_translator<GXError>(&translate_gx_error);
	 
	gxExportfloat_ref();
	gxExportint_ref();
	gxExportbool_ref();
    gxExportstr_ref();

	 class_<stdout_stream_helper>("_stdout_stream_helper")
		 .def("write", &stdout_stream_helper::write)
		 .def("flush", &stdout_stream_helper::flush);
	 class_<stderr_stream_helper>("_stderr_stream_helper")
		 .def("write", &stderr_stream_helper::write)
		 .def("flush", &stderr_stream_helper::flush);

	 class_<stdin_stream_helper>("_stdin_stream_helper")
		 .def("readline", &stdin_stream_helper::readline); 


    class_<GXContext, std::shared_ptr<GXContext>> pyGXClass("GXContext", no_init);
    pyGXClass.def("_create_internal", gx_context_create_internal).staticmethod("_create_internal");
    pyGXClass.def("_redirect_std_streams", gx_redirect_std_streams).staticmethod("_redirect_std_streams");
    
	pyGXClass.def("_internal_p", gx_context_internal_p);
    pyGXClass.def("create", &GXContext_wrap_create, create_member_overloads(
                      args("application", "version", "parent_wnd_id"))).staticmethod("create");
    pyGXClass.def("current", &GXContext::current).staticmethod("current");
    
	 pyGXClass.def("get_main_wnd_id", &GXContext_wrap_get_main_wnd);
    pyGXClass.def("get_active_wnd_id", &GXContext_wrap_get_main_wnd);
    pyGXClass.def("enable_application_windows", &GXContext::enable_application_windows);

    pyGXClass.def("clear_ui_console", &clear_ui_console);
    pyGXClass.def("show_ui_console", &show_ui_console);
    pyGXClass.def("has_ui_console", &has_ui_console);

    pyGXClass.def("is_ui_console_visible", &is_ui_console_visible);

/* TODO  Expose CGEO::GetPtrVM and CGEO::GetPtrVV" the way we do in C# */
{% for gxclass in classes %}{% if not gxclass.name == "GEO" %} 
    gxPythonImportGX{{ gxclass.name }}();{% endif %}{% endfor %}
}
