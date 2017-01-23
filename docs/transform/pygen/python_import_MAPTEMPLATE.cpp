#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXMAPTEMPLATE_wrap_get_tmp_copy(GXMAPTEMPLATEPtr self, str_ref& arg1)
{
    self->get_tmp_copy(arg1);
}
inline void GXMAPTEMPLATE_wrap_update_from_tmp_copy(GXMAPTEMPLATEPtr self, const gx_string_type& arg1)
{
    self->update_from_tmp_copy(arg1);
}
inline void GXMAPTEMPLATE_wrap_commit(GXMAPTEMPLATEPtr self)
{
    self->commit();
}
inline GXMAPTEMPLATEPtr GXMAPTEMPLATE_wrap_create(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXMAPTEMPLATEPtr ret = GXMAPTEMPLATE::create(arg1, arg2, (MAPTEMPLATE_OPEN)arg3);
    return ret;
}
inline void GXMAPTEMPLATE_wrap_discard(GXMAPTEMPLATEPtr self)
{
    self->discard();
}
inline void GXMAPTEMPLATE_wrap_get_file_name(GXMAPTEMPLATEPtr self, str_ref& arg1)
{
    self->get_file_name(arg1);
}
inline void GXMAPTEMPLATE_wrap_create_map(GXMAPTEMPLATEPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->create_map(arg1, arg2);
}
inline void GXMAPTEMPLATE_wrap_refresh(GXMAPTEMPLATEPtr self)
{
    self->refresh();
}
inline void GXMAPTEMPLATE_wrap_render_preview(GXMAPTEMPLATEPtr self, HDC arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    self->render_preview(arg1, arg2, arg3, arg4, arg5);
}
inline void GXMAPTEMPLATE_wrap_render_preview_map_production(GXMAPTEMPLATEPtr self, HDC arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5)
{
    self->render_preview_map_production(arg1, arg2, arg3, arg4, arg5);
}

void gxPythonImportGXMAPTEMPLATE()
{

    class_<GXMAPTEMPLATE, GXMAPTEMPLATEPtr> pyClass("GXMAPTEMPLATE",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		A MAPTEMPLATE wraps and provides manipulation and usage for the XML content in map template files.\n"
            "   		See the annotated schema file maptemplate.xsd in the <GEOSOFT>\\maptemplate folder and the accompanying\n"
            "   		documentation in that folder for documentation on the file format.\n"
            "   	\n\n"
            , no_init);

    pyClass.def("null", &GXMAPTEMPLATE::null, "null() -> GXMAPTEMPLATE\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXMAPTEMPLATE`\n\n:returns: A null :class:`geosoft.gxapi.GXMAPTEMPLATE`\n:rtype: :class:`geosoft.gxapi.GXMAPTEMPLATE`\n").staticmethod("null");
    pyClass.def("is_null", &GXMAPTEMPLATE::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXMAPTEMPLATE is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXMAPTEMPLATE`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXMAPTEMPLATE::_internal_handle);
    pyClass.def("get_tmp_copy", &GXMAPTEMPLATE_wrap_get_tmp_copy,
                "get_tmp_copy((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a temporary XML file for manipulation of the map template.\n\n"

                ":param arg1: returned temporary map template file name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					After manipulating contents the object may be updated by a call to\n"
                "   					the UpdateFromTmpCopy method.\n"
                "   				\n\n"
               );
    pyClass.def("update_from_tmp_copy", &GXMAPTEMPLATE_wrap_update_from_tmp_copy,
                "update_from_tmp_copy((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Update the object contents from a temporary XML file that may have bee manipulated externally.\n\n"

                ":param arg1: Temporary map template file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method will not modify the original contents of the file until a call to the\n"
                "   					the Commit method is made or the object is destroyed. A call to the Discard method\n"
                "   					will restore the contents to that of the original file. The temporary file is not deleted\n"
                "   					and should be to not leak file resources.\n"
                "   				\n\n"
               );
    pyClass.def("commit", &GXMAPTEMPLATE_wrap_commit,
                "commit() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Commit any changes to the map template to disk\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("create", &GXMAPTEMPLATE_wrap_create,
                "create((str)arg1, (str)arg2, (int)arg3) -> GXMAPTEMPLATE:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a MAPTEMPLATE from an existing file.\n\n"

                ":param arg1: Map Template file name\n"
                ":type arg1: str\n"
                ":param arg2: Map Template base template to create from\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`MAPTEMPLATE_OPEN`\\ \n"
                ":type arg3: int\n"
                ":returns: MAPTEMPLATE Object\n"
                ":rtype: :class:`geosoft.gxapi.GXMAPTEMPLATE`\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The base template name should be the file name part of a geosoft_maptemplate\n"
                "   					file in the <geosoft>\\maptemplate or <geosoftuser>\\maptemplate folders. A base file\n"
                "   					in the user folder will override any in the Geosoft install dir.\n"
                "   				\n\n"
               ).staticmethod("create");
    pyClass.def("discard", &GXMAPTEMPLATE_wrap_discard,
                "discard() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Discard all changes made to the map template and reload from disk.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_file_name", &GXMAPTEMPLATE_wrap_get_file_name,
                "get_file_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the file name of the map template.\n\n"

                ":param arg1: returned map template file name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("create_map", &GXMAPTEMPLATE_wrap_create_map,
                "create_map((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a map from the map template\n\n"

                ":param arg1: New map file name (if it exists it will be overwritten)\n"
                ":type arg1: str\n"
                ":param arg2: Group name to use for settings\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("refresh", &GXMAPTEMPLATE_wrap_refresh,
                "refresh() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Refresh the map template with any newly saved items\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("render_preview", &GXMAPTEMPLATE_wrap_render_preview,
                "render_preview((HDC)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create a preview of the map template onto a\n"
                "   					Windows DC handle\n"
                "   				\n\n"

                ":param arg1: DC Handle\n"
                ":type arg1: :class:`geosoft.gxapi.HDC`\n"
                ":param arg2: left value of the render rect in Windows coordinates (bottom>top)\n"
                ":type arg2: int\n"
                ":param arg3: bottom value\n"
                ":type arg3: int\n"
                ":param arg4: right value\n"
                ":type arg4: int\n"
                ":param arg5: top value\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("render_preview_map_production", &GXMAPTEMPLATE_wrap_render_preview_map_production,
                "render_preview_map_production((HDC)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4, (int_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Render a preview for map sheet production purposes\n\n"

                ":param arg1: DC Handle (pass 0 to just query the Data view pixel location)\n"
                ":type arg1: :class:`geosoft.gxapi.HDC`\n"
                ":param arg2: left value of the render rect in Windows coordinates (bottom>top)\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: bottom value\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: right value\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: top value\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method can also be used to get the data view pixel location\n"
                "   					by passing a null DC handle. This help to plot the view contents\n"
                "   					preview from another location.\n"
                "   				\n\n"
               );

    scope().attr("MAPTEMPLATE_WRITENEW") = (int32_t)0;
    scope().attr("MAPTEMPLATE_EXIST") = (int32_t)1;

}
