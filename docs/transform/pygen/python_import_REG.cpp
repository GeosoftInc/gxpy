#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXREG_wrap_clear(GXREGPtr self)
{
    self->clear();
}
inline void GXREG_wrap_copy(GXREGPtr self, GXREGPtr arg1)
{
    self->copy(arg1);
}
inline GXREGPtr GXREG_wrap_create(int32_t arg1)
{
    GXREGPtr ret = GXREG::create(arg1);
    return ret;
}
inline GXREGPtr GXREG_wrap_create_s(GXBFPtr arg1)
{
    GXREGPtr ret = GXREG::create_s(arg1);
    return ret;
}
inline void GXREG_wrap_get(GXREGPtr self, const gx_string_type& arg1, str_ref& arg2)
{
    self->get(arg1, arg2);
}
inline void GXREG_wrap_get_int(GXREGPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    self->get_int(arg1, arg2);
}
inline void GXREG_wrap_get_one(GXREGPtr self, int32_t arg1, str_ref& arg2, str_ref& arg3)
{
    self->get_one(arg1, arg2, arg3);
}
inline void GXREG_wrap_get_double(GXREGPtr self, const gx_string_type& arg1, float_ref& arg2)
{
    self->get_double(arg1, arg2);
}
inline int32_t GXREG_wrap_entries(GXREGPtr self)
{
    int32_t ret = self->entries();
    return ret;
}
inline void GXREG_wrap_load_ini(GXREGPtr self, const gx_string_type& arg1)
{
    self->load_ini(arg1);
}
inline void GXREG_wrap_match_string(GXREGPtr self, const gx_string_type& arg1, str_ref& arg2)
{
    self->match_string(arg1, arg2);
}
inline void GXREG_wrap_merge(GXREGPtr self, GXREGPtr arg1, int32_t arg2)
{
    self->merge(arg1, (REG_MERGE)arg2);
}
inline void GXREG_wrap_save_ini(GXREGPtr self, const gx_string_type& arg1)
{
    self->save_ini(arg1);
}
inline void GXREG_wrap_serial(GXREGPtr self, GXBFPtr arg1)
{
    self->serial(arg1);
}
inline void GXREG_wrap_set(GXREGPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->set(arg1, arg2);
}
inline void GXREG_wrap_set_int(GXREGPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->set_int(arg1, arg2);
}
inline void GXREG_wrap_set_double(GXREGPtr self, const gx_string_type& arg1, double arg2)
{
    self->set_double(arg1, arg2);
}

void gxPythonImportGXREG()
{

    class_<GXREG, GXREGPtr> pyClass("GXREG",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The REG class is used for storing and retrieving named\n"
                                    "   		variables. Many classes contain REG objects for storing\n"
                                    "   		information particular to the class.  The META class supersedes\n"
                                    "   		the REG class and is gradually replacing the use of the\n"
                                    "   		REG class in newer applications.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXREG::null, "null() -> GXREG\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXREG`\n\n:returns: A null :class:`geosoft.gxapi.GXREG`\n:rtype: :class:`geosoft.gxapi.GXREG`\n").staticmethod("null");
    pyClass.def("is_null", &GXREG::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXREG is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXREG`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXREG::_internal_handle);
    pyClass.def("clear", &GXREG_wrap_clear,
                "clear() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clears all the parameters in a REG object\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("copy", &GXREG_wrap_copy,
                "copy((GXREG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy\n\n"

                ":param arg1: source\n"
                ":type arg1: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXREG_wrap_create,
                "create((int)arg1) -> GXREG:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to a REG object\n\n"

                ":param arg1: maximum size of \"parameter=setting\" string.\n"
                ":type arg1: int\n"
                ":returns: REG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXREG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_s", &GXREG_wrap_create_s,
                "create_s((GXBF)arg1) -> GXREG:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to a REG object from a BF\n\n"

                ":param arg1: BF handle for file containing serialized REG\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: REG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXREG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_s");
    pyClass.def("get", &GXREG_wrap_get,
                "get((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets a string for a specified parameter in the REG object\n\n"

                ":param arg1: Name of the parameter\n"
                ":type arg1: str\n"
                ":param arg2: String to get\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_int", &GXREG_wrap_get_int,
                "get_int((str)arg1, (int_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets an int for a specified parameter in the REG object\n\n"

                ":param arg1: Name of the parameter\n"
                ":type arg1: str\n"
                ":param arg2: Int to get\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If parameter is not present in REG, iDUMMY is returned.\n\n"
               );
    pyClass.def("get_one", &GXREG_wrap_get_one,
                "get_one((int)arg1, (str_ref)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets n-th entry of the REG object\n\n"

                ":param arg1: sequential number of REG entry\n"
                ":type arg1: int\n"
                ":param arg2: String to put parameter name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: String to put data into.\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("get_double", &GXREG_wrap_get_double,
                "get_double((str)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets an real for a specified parameter in the REG object\n\n"

                ":param arg1: Name of the parameter\n"
                ":type arg1: str\n"
                ":param arg2: Real to get\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If parameter is not present in REG, rDUMMY is returned.\n\n"
               );
    pyClass.def("entries", &GXREG_wrap_entries,
                "entries() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of parms in a REG object\n\n"

                ":returns: Number of parms in a REG object.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("load_ini", &GXREG_wrap_load_ini,
                "load_ini((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a registry from an INI file.\n\n"

                ":param arg1: INI file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Items are loaded into the REG in the format \"GROUP.ITEM\".\n\n"
               );
    pyClass.def("match_string", &GXREG_wrap_match_string,
                "match_string((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replace a string with reg settings.\n\n"

                ":param arg1: String to Replace\n"
                ":type arg1: str\n"
                ":param arg2: Output Buffer\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("merge", &GXREG_wrap_merge,
                "merge((GXREG)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Merge\n\n"

                ":param arg1: source\n"
                ":type arg1: :class:`geosoft.gxapi.GXREG`\n"
                ":param arg2: \\ :ref:`REG_MERGE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("save_ini", &GXREG_wrap_save_ini,
                "save_ini((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save a REG to an INI file.\n\n"

                ":param arg1: INI file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Only REG parameters in the form \"GROUP.ITEM\" are\n"
                "   					dumped to the INI file, because they match the INI format\n"
                "   					which groups items under [GROUP] headings.\n"
                "   					Single-word items (without a separating period) are skipped.\n"
                "   				\n\n"
               );
    pyClass.def("serial", &GXREG_wrap_serial,
                "serial((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize a REG object into a file.\n\n"

                ":param arg1: BF to serialize REG into\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set", &GXREG_wrap_set,
                "set((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets a string parameter in the REG object\n\n"

                ":param arg1: Name of the parameter\n"
                ":type arg1: str\n"
                ":param arg2: String to set it to An empty string sets the setting to an empty string, but does NOT remove the parameter from the REG.\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To remove a parameter completely, use one of the\n"
                "   					following:\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXREG.set_int`\\ (Reg, sParam, iDUMMY);\n"
                "   					or\n"
                "   					\\ :func:`geosoft.gxapi.GXREG.set_double`\\ (Reg, sParam, rDUMMY);\n"
                "   				\n\n"
               );
    pyClass.def("set_int", &GXREG_wrap_set_int,
                "set_int((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets an int for a specified parameter in the REG object\n\n"

                ":param arg1: Name of the parameter\n"
                ":type arg1: str\n"
                ":param arg2: Int to set, iDUMMY to remove the parameter\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_double", &GXREG_wrap_set_double,
                "set_double((str)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets an real for a specified parameter in the REG object\n\n"

                ":param arg1: Name of the parameter\n"
                ":type arg1: str\n"
                ":param arg2: Real to set, rDUMMY to remove the parameter\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );

    scope().attr("REG_MERGE_REPLACE") = (int32_t)0;
    scope().attr("REG_MERGE_ADD") = (int32_t)1;

}
