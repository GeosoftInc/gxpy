#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXDATAMINE_wrap_create_voxel(const gx_string_type& arg1, const gx_string_type& arg2, GXIPJPtr arg3, GXMETAPtr arg4, const gx_string_type& arg5)
{
    GXDATAMINE::create_voxel(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDATAMINE_wrap_numeric_field_lst(const gx_string_type& arg1, GXLSTPtr arg2)
{
    GXDATAMINE::numeric_field_lst(arg1, arg2);
}

void gxPythonImportGXDATAMINE()
{

    class_<GXDATAMINE, boost::noncopyable> pyClass("GXDATAMINE",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		DATAMINE functions provide an interface to Datamine Software Limited files.\n"
            "   		See also GIS.GXH for various other Datamine-specific functions.\n"
            "   	\n\n"

            "\n\n**Note:**\n\n"

            "\n.. parsed-literal::\n\n"
            "   None.\n\n"
            , no_init);


    pyClass.def("create_voxel", &GXDATAMINE_wrap_create_voxel,
                "create_voxel((str)arg1, (str)arg2, (GXIPJ)arg3, (GXMETA)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Geosoft Voxel file from a Datamine block model file.\n\n"

                ":param arg1: Datamine file name\n"
                ":type arg1: str\n"
                ":param arg2: Field to use for data\n"
                ":type arg2: str\n"
                ":param arg3: Projection to set\n"
                ":type arg3: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg4: META to set\n"
                ":type arg4: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg5: Output voxel file name\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Geosoft Voxel file from a Datamine block model file.\n\n"
               ).staticmethod("create_voxel");
    pyClass.def("numeric_field_lst", &GXDATAMINE_wrap_numeric_field_lst,
                "numeric_field_lst((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return a LST containing the non-standard numeric fields in a Datamine file.\n\n"

                ":param arg1: Datamine file name\n"
                ":type arg1: str\n"
                ":param arg2: LST to populate\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					At this time, only GIS_DMTYPE_BLOCKMODEL files are supported.\n"
                "   					The field names go in the name part, and field indices (1 to N)\n"
                "   					in the value part.\n"
                "   				\n\n"
               ).staticmethod("numeric_field_lst");

    scope().attr("GIS_DMTYPE_STRING") = (int32_t)2;
    scope().attr("GIS_DMTYPE_WIREFRAME_TR") = (int32_t)8;
    scope().attr("GIS_DMTYPE_DTM") = (int32_t)16;
    scope().attr("GIS_DMTYPE_BLOCKMODEL") = (int32_t)32;
    scope().attr("GIS_DMTYPE_WIREFRAME_PT") = (int32_t)64;
    scope().attr("GIS_DMTYPE_POINTDATA") = (int32_t)1024;

}
