#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXGDPtr GXGD_wrap_create(const gx_string_type& arg1, int32_t arg2)
{
    GXGDPtr ret = GXGD::create(arg1, (GD_STATUS)arg2);
    return ret;
}

void gxPythonImportGXGD()
{

    class_<GXGD, GXGDPtr> pyClass("GXGD",
                                  "\n.. parsed-literal::\n\n"
                                  "   This class provides access to Geosoft grid files using an old interface.\n"
                                  "   Only the \\ :func:`geosoft.gxapi.GXDU.sample_gd`\\  function uses this class.  Use the IMG class\n"
                                  "   instead.\n\n"
                                  , no_init);

    pyClass.def("null", &GXGD::null, "null() -> GXGD\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXGD`\n\n:returns: A null :class:`geosoft.gxapi.GXGD`\n:rtype: :class:`geosoft.gxapi.GXGD`\n").staticmethod("null");
    pyClass.def("is_null", &GXGD::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXGD is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXGD`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXGD::_internal_handle);
    pyClass.def("create", &GXGD_wrap_create,
                "create((str)arg1, (int)arg2) -> GXGD:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates a GD object.\n\n"

                ":param arg1: Name of the Grid File\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`GD_STATUS`\\ \n"
                ":type arg2: int\n"
                ":returns: Handle to the GD object\n"
                ":rtype: :class:`geosoft.gxapi.GXGD`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");

    scope().attr("GD_STATUS_READONLY") = (int32_t)0;
    scope().attr("GD_STATUS_NEW") = (int32_t)1;
    scope().attr("GD_STATUS_OLD") = (int32_t)2;

}
