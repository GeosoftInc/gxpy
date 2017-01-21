#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXSBFPtr GXSBF_wrap_create(GXSBFPtr self, const gx_string_type& arg1, int32_t arg2)
{
    GXSBFPtr ret = self->create(arg1, (SBF_OPEN)arg2);
    return ret;
}
inline void GXSBF_wrap_create_obj_list(GXSBFPtr self, GXLSTPtr arg1, int32_t arg2)
{
    self->create_obj_list(arg1, (SBF_TYPE)arg2);
}
inline void GXSBF_wrap_del_dir(GXSBFPtr self, const gx_string_type& arg1)
{
    self->del_dir(arg1);
}
inline void GXSBF_wrap_del_file(GXSBFPtr self, const gx_string_type& arg1)
{
    self->del_file(arg1);
}
inline GXSBFPtr GXSBF_wrap_h_get_db(GXDBPtr arg1)
{
    GXSBFPtr ret = GXSBF::h_get_db(arg1);
    return ret;
}
inline GXSBFPtr GXSBF_wrap_h_get_map(GXMAPPtr arg1)
{
    GXSBFPtr ret = GXSBF::h_get_map(arg1);
    return ret;
}
inline GXSBFPtr GXSBF_wrap_h_get_sys()
{
    GXSBFPtr ret = GXSBF::h_get_sys();
    return ret;
}
inline int32_t GXSBF_wrap_exist_dir(GXSBFPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->exist_dir(arg1);
    return ret;
}
inline int32_t GXSBF_wrap_exist_file(GXSBFPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->exist_file(arg1);
    return ret;
}
inline void GXSBF_wrap_save_log(GXSBFPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4)
{
    self->save_log(arg1, arg2, arg3, arg4);
}

void gxPythonImportGXSBF()
{

    class_<GXSBF, GXSBFPtr> pyClass("GXSBF",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The SBF class provides a means of storing data in a\n"
                                    "   		file-type directory structure within a workspace, database\n"
                                    "   		or map. Each of these three objects contains its own SBF object,\n"
                                    "   		which may be accessed using the \\ :func:`geosoft.gxapi.GXSBF.h_get_sys`\\ , \\ :func:`geosoft.gxapi.GXSBF.h_get_db`\\  and\n"
                                    "   		\\ :func:`geosoft.gxapi.GXSBF.h_get_map`\\  functions. To access data in a file, or create a\n"
                                    "   		new file in the SBF object, call the CreatSBF_BF function (see BF),\n"
                                    "   		which will return a BF object to use.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXSBF::null, "null() -> GXSBF\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXSBF`\n\n:returns: A null :class:`geosoft.gxapi.GXSBF`\n:rtype: :class:`geosoft.gxapi.GXSBF`\n").staticmethod("null");
    pyClass.def("is_null", &GXSBF::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXSBF is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXSBF`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXSBF::_internal_handle);
    pyClass.def("create", &GXSBF_wrap_create,
                "create((str)arg1, (int)arg2) -> GXSBF:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a child SBF object inside an SBF.\n\n"

                ":param arg1: directory name to open / create\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`SBF_OPEN`\\ \n"
                ":type arg2: int\n"
                ":returns: SBF object, terminates if fails.\n"
                ":rtype: :class:`geosoft.gxapi.GXSBF`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create_obj_list", &GXSBF_wrap_create_obj_list,
                "create_obj_list((GXLST)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills an LST with embedded storage names of an SBF.\n\n"

                ":param arg1: LST handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`SBF_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Function will populate an LST object with embedded files (SBF_TYPE_FILES),\n"
                "   					directories (SBF_TYPE_DIRS), or both (pass SBF_TYPE_BOTH) in an SBF.\n"
                "   					Along with the Name of the file or directory, a constant \"dir\" or \"file\" string is written\n"
                "   					to the LST also.\n"
                "   				\n\n"
               );
    pyClass.def("del_dir", &GXSBF_wrap_del_dir,
                "del_dir((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a directory (storage) from this storage.\n\n"

                ":param arg1: Dir/Storage Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("del_file", &GXSBF_wrap_del_file,
                "del_file((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a file from this storage.\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("h_get_db", &GXSBF_wrap_h_get_db,
                "h_get_db((GXDB)arg1) -> GXSBF:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the embedded file storage from a database.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: SBF Object\n"
                ":rtype: :class:`geosoft.gxapi.GXSBF`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("h_get_db");
    pyClass.def("h_get_map", &GXSBF_wrap_h_get_map,
                "h_get_map((GXMAP)arg1) -> GXSBF:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the embedded file storage from a map.\n\n"

                ":param arg1: MAP object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":returns: SBF Object\n"
                ":rtype: :class:`geosoft.gxapi.GXSBF`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("h_get_map");
    pyClass.def("h_get_sys", &GXSBF_wrap_h_get_sys,
                "h_get_sys() -> GXSBF:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the main embedded file storage (in workspace).\n\n"

                ":returns: SBF Object\n"
                ":rtype: :class:`geosoft.gxapi.GXSBF`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("h_get_sys");
    pyClass.def("exist_dir", &GXSBF_wrap_exist_dir,
                "exist_dir((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check to see if a directory (storage) exists inside this storage.\n\n"

                ":param arg1: Dir/Storage Name\n"
                ":type arg1: str\n"
                ":returns: 0 - Does not exist\n"
                "          						1 - Exists\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("exist_file", &GXSBF_wrap_exist_file,
                "exist_file((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check to see if a file exists inside this storage.\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: 0 - Does not exist\n"
                "          						1 - Exists\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("save_log", &GXSBF_wrap_save_log,
                "save_log((str)arg1, (str)arg2, (str)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save an embedded file to an ASCII file.\n\n"

                ":param arg1: Directory name in the Parent SBF\n"
                ":type arg1: str\n"
                ":param arg2: File name in the directory\n"
                ":type arg2: str\n"
                ":param arg3: File to save as (as an ASCII file)\n"
                ":type arg3: str\n"
                ":param arg4: Append Mode: 0 - New file, 1 - Append file\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );

    scope().attr("SBF_READ") = (int32_t)0;
    scope().attr("SBF_READWRITE_NEW") = (int32_t)1;
    scope().attr("SBF_READWRITE_OLD") = (int32_t)2;
    scope().attr("SBF_TYPE_DIRS") = (int32_t)1;
    scope().attr("SBF_TYPE_FILES") = (int32_t)2;
    scope().attr("SBF_TYPE_BOTH") = (int32_t)3;

}
