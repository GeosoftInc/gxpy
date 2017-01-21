#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXPDF3D_wrap_render(GXMVIEWPtr arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4)
{
    GXPDF3D::render(arg1, arg2, arg3, arg4);
}
inline void GXPDF3D_wrap_render_to_page(GXMVIEWPtr arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXPDF3D::render_to_page(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPDF3D_wrap_export2_d(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXPDF3D::export2_d(arg1, arg2, arg3, arg4, arg5);
}

void gxPythonImportGXPDF3D()
{

    class_<GXPDF3D, boost::noncopyable> pyClass("GXPDF3D",
            "\n.. parsed-literal::\n\n"
            "   The PDF3D class provides the ability to create 3D PDFs.\n\n"
            , no_init);


    pyClass.def("render", &GXPDF3D_wrap_render,
                "render((GXMVIEW)arg1, (str)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Render a voxel, voxsurf and/or gensurf to pdf\n\n"

                ":param arg1: MVIEW handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: filename\n"
                ":type arg2: str\n"
                ":param arg3: resolution\n"
                ":type arg3: int\n"
                ":param arg4: noclipping\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"
               ).staticmethod("render");
    pyClass.def("render_to_page", &GXPDF3D_wrap_render_to_page,
                "render_to_page((GXMVIEW)arg1, (str)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Render a voxel, voxsurf and/or gensurf to a specified page on a pdf\n\n"

                ":param arg1: MVIEW handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: filename\n"
                ":type arg2: str\n"
                ":param arg3: page number\n"
                ":type arg3: int\n"
                ":param arg4: resolution\n"
                ":type arg4: int\n"
                ":param arg5: noclipping\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               ).staticmethod("render_to_page");
    pyClass.def("export2_d", &GXPDF3D_wrap_export2_d,
                "export2_d((str)arg1, (str)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a 2D map to a PDF file.\n\n"

                ":param arg1: Input map file\n"
                ":type arg1: str\n"
                ":param arg2: Output PDF file\n"
                ":type arg2: str\n"
                ":param arg3: Create layers in PDF\n"
                ":type arg3: int\n"
                ":param arg4: Geospatial PDF\n"
                ":type arg4: int\n"
                ":param arg5: Open PDF after export\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               ).staticmethod("export2_d");


}
