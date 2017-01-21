#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXLL2Ptr GXLL2_wrap_create(double arg1, double arg2, double arg3, double arg4, int32_t arg5, int32_t arg6, GXIPJPtr arg7, GXIPJPtr arg8)
{
    GXLL2Ptr ret = GXLL2::create(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
    return ret;
}
inline void GXLL2_wrap_save(GXLL2Ptr self, const gx_string_type& arg1)
{
    self->save(arg1);
}
inline void GXLL2_wrap_set_row(GXLL2Ptr self, int32_t arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->set_row(arg1, arg2, arg3);
}

void gxPythonImportGXLL2()
{

    class_<GXLL2, GXLL2Ptr> pyClass("GXLL2",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		local datum lookup creator\n"
                                    "   		ll2 methods are used to create LL2 objects.  LL2 objects contain\n"
                                    "   		latitude, longitude correction lookup tables to convert between datums.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXLL2::null, "null() -> GXLL2\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXLL2`\n\n:returns: A null :class:`geosoft.gxapi.GXLL2`\n:rtype: :class:`geosoft.gxapi.GXLL2`\n").staticmethod("null");
    pyClass.def("is_null", &GXLL2::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXLL2 is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXLL2`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXLL2::_internal_handle);
    pyClass.def("create", &GXLL2_wrap_create,
                "create((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5, (int)arg6, (GXIPJ)arg7, (GXIPJ)arg8) -> GXLL2:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an empty LL2 table to be filled\n\n"

                ":param arg1: longitude origin\n"
                ":type arg1: float\n"
                ":param arg2: latitude origin\n"
                ":type arg2: float\n"
                ":param arg3: longitude increment\n"
                ":type arg3: float\n"
                ":param arg4: latitude increment\n"
                ":type arg4: float\n"
                ":param arg5: # longitudes\n"
                ":type arg5: int\n"
                ":param arg6: # latitudes\n"
                ":type arg6: int\n"
                ":param arg7: input projection\n"
                ":type arg7: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg8: output projection\n"
                ":type arg8: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: LL2 Object\n"
                ":rtype: :class:`geosoft.gxapi.GXLL2`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXLL2.destroy`\\ , \\ :func:`geosoft.gxapi.GXLL2.set_row`\\ , \\ :func:`geosoft.gxapi.GXLL2.save`\\ \n\n"
               ).staticmethod("create");
    pyClass.def("save", &GXLL2_wrap_save,
                "save((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save an LL2 to a named resource\n\n"

                ":param arg1: named resource\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The named resource is the name of the datum transform define\n"
                "   					inside square brackets in the datum transform name in the\n"
                "   					datumtrf table.\n"
                "   				\n\n"
               );
    pyClass.def("set_row", &GXLL2_wrap_set_row,
                "set_row((int)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Define a row of the LL2\n\n"

                ":param arg1: the row to set\n"
                ":type arg1: int\n"
                ":param arg2: longitude corrections\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: latitude corrections\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The correction data is in degrees, added to the input\n"
                "   					datum to product output datum results.\n"
                "   \n"
                "   					The VV lengths must be equal to #longitudes defined\n"
                "   					by \\ :func:`geosoft.gxapi.GXLL2.create`\\ .\n"
                "   				\n\n"
               );


}
