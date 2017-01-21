#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXUSERMETAPtr GXUSERMETA_wrap_create(int32_t arg1)
{
    GXUSERMETAPtr ret = GXUSERMETA::create((USERMETA_FORMAT)arg1);
    return ret;
}
inline GXUSERMETAPtr GXUSERMETA_wrap_create_s(const gx_string_type& arg1)
{
    GXUSERMETAPtr ret = GXUSERMETA::create_s(arg1);
    return ret;
}
inline void GXUSERMETA_wrap_get_data_creation_date(GXUSERMETAPtr self, float_ref& arg1)
{
    self->get_data_creation_date(arg1);
}
inline void GXUSERMETA_wrap_get_extents2d(GXUSERMETAPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->get_extents2d(arg1, arg2, arg3, arg4);
}
inline void GXUSERMETA_wrap_get_extents3d(GXUSERMETAPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->get_extents3d(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXUSERMETA_wrap_get_ipj(GXUSERMETAPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}
inline void GXUSERMETA_wrap_get_meta_creation_date(GXUSERMETAPtr self, float_ref& arg1)
{
    self->get_meta_creation_date(arg1);
}
inline void GXUSERMETA_wrap_get_xml_format(GXUSERMETAPtr self, int_ref& arg1)
{
    self->get_xml_format((USERMETA_FORMAT&)arg1);
}
inline int32_t GXUSERMETA_wrap_compare(GXUSERMETAPtr self, GXUSERMETAPtr arg1)
{
    int32_t ret = self->compare(arg1);
    return ret;
}
inline void GXUSERMETA_wrap_get_data_creator(GXUSERMETAPtr self, str_ref& arg1)
{
    self->get_data_creator(arg1);
}
inline void GXUSERMETA_wrap_get_format(GXUSERMETAPtr self, str_ref& arg1)
{
    self->get_format(arg1);
}
inline void GXUSERMETA_wrap_get_meta_creator(GXUSERMETAPtr self, str_ref& arg1)
{
    self->get_meta_creator(arg1);
}
inline void GXUSERMETA_wrap_get_project(GXUSERMETAPtr self, str_ref& arg1)
{
    self->get_project(arg1);
}
inline void GXUSERMETA_wrap_get_title(GXUSERMETAPtr self, str_ref& arg1)
{
    self->get_title(arg1);
}
inline void GXUSERMETA_wrap_serial(GXUSERMETAPtr self, bool arg1, const gx_string_type& arg2)
{
    self->serial(arg1, arg2);
}
inline void GXUSERMETA_wrap_set_data_creation_date(GXUSERMETAPtr self, double arg1)
{
    self->set_data_creation_date(arg1);
}
inline void GXUSERMETA_wrap_set_data_creator(GXUSERMETAPtr self, const gx_string_type& arg1)
{
    self->set_data_creator(arg1);
}
inline void GXUSERMETA_wrap_set_extents2d(GXUSERMETAPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->set_extents2d(arg1, arg2, arg3, arg4);
}
inline void GXUSERMETA_wrap_set_extents3d(GXUSERMETAPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->set_extents3d(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXUSERMETA_wrap_set_format(GXUSERMETAPtr self, const gx_string_type& arg1)
{
    self->set_format(arg1);
}
inline void GXUSERMETA_wrap_set_ipj(GXUSERMETAPtr self, GXIPJPtr arg1)
{
    self->set_ipj(arg1);
}
inline void GXUSERMETA_wrap_set_meta_creation_date(GXUSERMETAPtr self, double arg1)
{
    self->set_meta_creation_date(arg1);
}
inline void GXUSERMETA_wrap_set_meta_creator(GXUSERMETAPtr self, const gx_string_type& arg1)
{
    self->set_meta_creator(arg1);
}
inline void GXUSERMETA_wrap_set_project(GXUSERMETAPtr self, const gx_string_type& arg1)
{
    self->set_project(arg1);
}
inline void GXUSERMETA_wrap_set_title(GXUSERMETAPtr self, const gx_string_type& arg1)
{
    self->set_title(arg1);
}
inline void GXUSERMETA_wrap_update_extents2_d(const gx_string_type& arg1, GXIPJPtr arg2, double arg3, double arg4, double arg5, double arg6)
{
    GXUSERMETA::update_extents2_d(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXUSERMETA_wrap_update_file_type(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXUSERMETA::update_file_type(arg1, arg2);
}
inline void GXUSERMETA_wrap_save_file_lineage(const gx_string_type& arg1, bool arg2)
{
    GXUSERMETA::save_file_lineage(arg1, arg2);
}

void gxPythonImportGXUSERMETA()
{

    class_<GXUSERMETA, GXUSERMETAPtr> pyClass("GXUSERMETA",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		The USERMETA class handles user style metadata tied to real\n"
            "   		data.\n"
            "   	\n\n"
            , no_init);

    pyClass.def("null", &GXUSERMETA::null, "null() -> GXUSERMETA\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXUSERMETA`\n\n:returns: A null :class:`geosoft.gxapi.GXUSERMETA`\n:rtype: :class:`geosoft.gxapi.GXUSERMETA`\n").staticmethod("null");
    pyClass.def("is_null", &GXUSERMETA::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXUSERMETA is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXUSERMETA`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXUSERMETA::_internal_handle);
    pyClass.def("create", &GXUSERMETA_wrap_create,
                "create((int)arg1) -> GXUSERMETA:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an empty USERMETA object\n\n"

                ":param arg1: \\ :ref:`USERMETA_FORMAT`\\  Type of Meta to create\n"
                ":type arg1: int\n"
                ":returns: USERMETA Object\n"
                ":rtype: :class:`geosoft.gxapi.GXUSERMETA`\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_s", &GXUSERMETA_wrap_create_s,
                "create_s((str)arg1) -> GXUSERMETA:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a USERMETA from a file\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: USERMETA Object\n"
                ":rtype: :class:`geosoft.gxapi.GXUSERMETA`\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("create_s");
    pyClass.def("get_data_creation_date", &GXUSERMETA_wrap_get_data_creation_date,
                "get_data_creation_date((float_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Data Creation Date\n\n"

                ":param arg1: Date\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_extents2d", &GXUSERMETA_wrap_get_extents2d,
                "get_extents2d((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the 2d Extents\n\n"

                ":param arg1: MinX\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: MinY\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: MaxX\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: MaxY\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_extents3d", &GXUSERMETA_wrap_get_extents3d,
                "get_extents3d((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the 3d Extents\n\n"

                ":param arg1: MinX\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: MinY\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: MinZ\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: MaxX\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: MaxY\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: MaxZ\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_ipj", &GXUSERMETA_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the IPJ\n\n"

                ":param arg1: Date\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_meta_creation_date", &GXUSERMETA_wrap_get_meta_creation_date,
                "get_meta_creation_date((float_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Meta Creation Date\n\n"

                ":param arg1: Date\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_xml_format", &GXUSERMETA_wrap_get_xml_format,
                "get_xml_format((int_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the XML Format\n\n"

                ":param arg1: \\ :ref:`USERMETA_FORMAT`\\ \n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("compare", &GXUSERMETA_wrap_compare,
                "compare((GXUSERMETA)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Compare 2 USERMETA's\n\n"

                ":param arg1: Second UERMETA\n"
                ":type arg1: :class:`geosoft.gxapi.GXUSERMETA`\n"
                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_data_creator", &GXUSERMETA_wrap_get_data_creator,
                "get_data_creator((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Data Creator\n\n"

                ":param arg1: DataCreator returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_format", &GXUSERMETA_wrap_get_format,
                "get_format((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the File Format\n\n"

                ":param arg1: title returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_meta_creator", &GXUSERMETA_wrap_get_meta_creator,
                "get_meta_creator((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Meta Creator\n\n"

                ":param arg1: MetaCreator returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_project", &GXUSERMETA_wrap_get_project,
                "get_project((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the File Project\n\n"

                ":param arg1: title returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_title", &GXUSERMETA_wrap_get_title,
                "get_title((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Title\n\n"

                ":param arg1: title returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("serial", &GXUSERMETA_wrap_serial,
                "serial((bool)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize USERMETA to a BF.\n\n"

                ":param arg1: bool Output Geosoft Metadata?\n"
                ":type arg1: bool\n"
                ":param arg2: File name to save to\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_data_creation_date", &GXUSERMETA_wrap_set_data_creation_date,
                "set_data_creation_date((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Data Creation Date\n\n"

                ":param arg1: Date\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_data_creator", &GXUSERMETA_wrap_set_data_creator,
                "set_data_creator((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Data Creator\n\n"

                ":param arg1: DataCreator\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_extents2d", &GXUSERMETA_wrap_set_extents2d,
                "set_extents2d((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the 2d Extents\n\n"

                ":param arg1: MinX\n"
                ":type arg1: float\n"
                ":param arg2: MinY\n"
                ":type arg2: float\n"
                ":param arg3: MaxX\n"
                ":type arg3: float\n"
                ":param arg4: MaxY\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_extents3d", &GXUSERMETA_wrap_set_extents3d,
                "set_extents3d((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the 3d Extents\n\n"

                ":param arg1: MinX\n"
                ":type arg1: float\n"
                ":param arg2: MinY\n"
                ":type arg2: float\n"
                ":param arg3: MinZ\n"
                ":type arg3: float\n"
                ":param arg4: MaxX\n"
                ":type arg4: float\n"
                ":param arg5: MaxY\n"
                ":type arg5: float\n"
                ":param arg6: MaxZ\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_format", &GXUSERMETA_wrap_set_format,
                "set_format((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the File Format\n\n"

                ":param arg1: Format\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_ipj", &GXUSERMETA_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the IPJ\n\n"

                ":param arg1: Date\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_meta_creation_date", &GXUSERMETA_wrap_set_meta_creation_date,
                "set_meta_creation_date((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Meta Creation Date\n\n"

                ":param arg1: Date\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_meta_creator", &GXUSERMETA_wrap_set_meta_creator,
                "set_meta_creator((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Meta Creator\n\n"

                ":param arg1: MetaCreator\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_project", &GXUSERMETA_wrap_set_project,
                "set_project((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the File Project\n\n"

                ":param arg1: Project\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_title", &GXUSERMETA_wrap_set_title,
                "set_title((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Title\n\n"

                ":param arg1: Title\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("update_extents2_d", &GXUSERMETA_wrap_update_extents2_d,
                "update_extents2_d((str)arg1, (GXIPJ)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Edit an existing XML metadata file by\n"
                "   					changing the extents and projection data\n"
                "   				\n\n"

                ":param arg1: Filename of existing metadata to update\n"
                ":type arg1: str\n"
                ":param arg2: New projection\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: New MinX value\n"
                ":type arg3: float\n"
                ":param arg4: New MinY value\n"
                ":type arg4: float\n"
                ":param arg5: New MaxX value\n"
                ":type arg5: float\n"
                ":param arg6: New MaxY value\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.1\n\n"
               ).staticmethod("update_extents2_d");
    pyClass.def("update_file_type", &GXUSERMETA_wrap_update_file_type,
                "update_file_type((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Edit an existing XML metadata file by\n"
                "   					changing the file type\n"
                "   				\n\n"

                ":param arg1: Filename of existing metadata to update\n"
                ":type arg1: str\n"
                ":param arg2: New file type\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("update_file_type");
    pyClass.def("save_file_lineage", &GXUSERMETA_wrap_save_file_lineage,
                "save_file_lineage((str)arg1, (bool)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add lineage to XML\n\n"

                ":param arg1: Filename of existing metadata to update\n"
                ":type arg1: str\n"
                ":param arg2: bool Output Geosoft Metadata?\n"
                ":type arg2: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"
               ).staticmethod("save_file_lineage");

    scope().attr("USERMETA_FORMAT_DEFAULT") = (int32_t)-1;
    scope().attr("USERMETA_FORMAT_ISO") = (int32_t)0;
    scope().attr("USERMETA_FORMAT_FGDC") = (int32_t)1;

}
