#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXRAPtr GXRA_wrap_create(const gx_string_type& arg1)
{
    GXRAPtr ret = GXRA::create(arg1);
    return ret;
}
inline GXRAPtr GXRA_wrap_create_sbf(GXSBFPtr arg1, const gx_string_type& arg2)
{
    GXRAPtr ret = GXRA::create_sbf(arg1, arg2);
    return ret;
}
inline int32_t GXRA_wrap_gets(GXRAPtr self, str_ref& arg1)
{
    int32_t ret = self->gets(arg1);
    return ret;
}
inline int32_t GXRA_wrap_len(GXRAPtr self)
{
    int32_t ret = self->len();
    return ret;
}
inline int32_t GXRA_wrap_line(GXRAPtr self)
{
    int32_t ret = self->line();
    return ret;
}
inline int32_t GXRA_wrap_seek(GXRAPtr self, int32_t arg1)
{
    int32_t ret = self->seek(arg1);
    return ret;
}

void gxPythonImportGXRA()
{

    class_<GXRA, GXRAPtr> pyClass("GXRA",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		The RA class is used to access ASCII files sequentially or\n"
                                  "   		by line number. The files are opened in read-only mode, so no\n"
                                  "   		write operations are defined\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXRA::null, "null() -> GXRA\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXRA`\n\n:returns: A null :class:`geosoft.gxapi.GXRA`\n:rtype: :class:`geosoft.gxapi.GXRA`\n").staticmethod("null");
    pyClass.def("is_null", &GXRA::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXRA is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXRA`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXRA::_internal_handle);
    pyClass.def("create", &GXRA_wrap_create,
                "create((str)arg1) -> GXRA:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates RA\n\n"

                ":param arg1: name of the file\n"
                ":type arg1: str\n"
                ":returns: RA Object\n"
                ":rtype: :class:`geosoft.gxapi.GXRA`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_sbf", &GXRA_wrap_create_sbf,
                "create_sbf((GXSBF)arg1, (str)arg2) -> GXRA:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates RA on an SBF\n\n"

                ":param arg1: Storage\n"
                ":type arg1: :class:`geosoft.gxapi.GXSBF`\n"
                ":param arg2: name of the file\n"
                ":type arg2: str\n"
                ":returns: RA Object\n"
                ":rtype: :class:`geosoft.gxapi.GXRA`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method allows you to open an RA in a structured file\n"
                "   					storage (an SBF).  SBFs can be created inside other data\n"
                "   					containers, such as workspaces, maps, images and databases.\n"
                "   					This lets you store application specific information together\n"
                "   					with the data to which it applies.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   sbf.gxh\n\n"
               ).staticmethod("create_sbf");
    pyClass.def("gets", &GXRA_wrap_gets,
                "gets((str_ref)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get next full line from RA\n\n"

                ":param arg1: buffer in which to place string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - Ok\n"
                "          						1 - End of file\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("len", &GXRA_wrap_len,
                "len() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the total number of lines in RA\n\n"

                ":returns: # of lines in the RA.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("line", &GXRA_wrap_line,
                "line() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns current line #, 0 is the first\n\n"

                ":returns: The current read line location.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This will be the next line read.\n\n"
               );
    pyClass.def("seek", &GXRA_wrap_seek,
                "seek((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Position next read to specified line #\n\n"

                ":param arg1: line #, 0 is the first.\n"
                ":type arg1: int\n"
                ":returns: 0 if seeked line is within the range of lines,\n"
                "          						1 if outside range, line pointer will not be moved.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );


}
