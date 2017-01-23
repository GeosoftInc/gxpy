#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXBF_wrap_ch_size(GXBFPtr self, int32_t arg1)
{
    self->ch_size(arg1);
}
inline void GXBF_wrap_seek(GXBFPtr self, int32_t arg1, int32_t arg2)
{
    self->seek(arg1, (BF_SEEK)arg2);
}
inline void GXBF_wrap_copy(GXBFPtr self, GXBFPtr arg1)
{
    self->copy(arg1);
}
inline int32_t GXBF_wrap_crc(GXBFPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->crc(arg1, arg2);
    return ret;
}
inline GXBFPtr GXBF_wrap_create(const gx_string_type& arg1, int32_t arg2)
{
    GXBFPtr ret = GXBF::create(arg1, (BF_OPEN_MODE)arg2);
    return ret;
}
inline GXBFPtr GXBF_wrap_create_sbf(GXSBFPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXBFPtr ret = GXBF::create_sbf(arg1, arg2, (BF_OPEN_MODE)arg3);
    return ret;
}
inline int32_t GXBF_wrap_eof(GXBFPtr self)
{
    int32_t ret = self->eof();
    return ret;
}
inline int32_t GXBF_wrap_query_write(GXBFPtr self)
{
    int32_t ret = self->query_write();
    return ret;
}
inline void GXBF_wrap_read_binary_string(GXBFPtr self, int32_t arg1, int32_t arg2, str_ref& arg3)
{
    self->read_binary_string(arg1, (BF_ENCODE)arg2, arg3);
}
inline int32_t GXBF_wrap_size(GXBFPtr self)
{
    int32_t ret = self->size();
    return ret;
}
inline int32_t GXBF_wrap_tell(GXBFPtr self)
{
    int32_t ret = self->tell();
    return ret;
}
inline void GXBF_wrap_read_int(GXBFPtr self, int32_t arg1, int_ref& arg2)
{
    self->read_int(arg1, arg2);
}
inline void GXBF_wrap_read_double(GXBFPtr self, int32_t arg1, float_ref& arg2)
{
    self->read_double(arg1, arg2);
}
inline void GXBF_wrap_read_vv(GXBFPtr self, int32_t arg1, GXVVPtr arg2)
{
    self->read_vv(arg1, arg2);
}
inline void GXBF_wrap_set_destroy_status(GXBFPtr self, int32_t arg1)
{
    self->set_destroy_status((BF_CLOSE)arg1);
}
inline void GXBF_wrap_write_binary_string(GXBFPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->write_binary_string((BF_ENCODE)arg1, arg2);
}
inline void GXBF_wrap_write_data_null(GXBFPtr self)
{
    self->write_data_null();
}
inline void GXBF_wrap_write_int(GXBFPtr self, int32_t arg1, int32_t arg2)
{
    self->write_int(arg1, arg2);
}
inline void GXBF_wrap_write_double(GXBFPtr self, int32_t arg1, double arg2)
{
    self->write_double(arg1, arg2);
}
inline void GXBF_wrap_write_vv(GXBFPtr self, int32_t arg1, GXVVPtr arg2)
{
    self->write_vv(arg1, arg2);
}

void gxPythonImportGXBF()
{

    class_<GXBF, GXBFPtr> pyClass("GXBF",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		The BF class is used to access (or create) Binary files and remove\n"
                                  "   		(or destroy) files from use. You can also perform a variety of\n"
                                  "   		additional tasks, such as positioning within files, reading from\n"
                                  "   		files and writing to files.\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXBF::null, "null() -> GXBF\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXBF`\n\n:returns: A null :class:`geosoft.gxapi.GXBF`\n:rtype: :class:`geosoft.gxapi.GXBF`\n").staticmethod("null");
    pyClass.def("is_null", &GXBF::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXBF is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXBF`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXBF::_internal_handle);
    pyClass.def("ch_size", &GXBF_wrap_ch_size,
                "ch_size((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Changes the size of a file\n\n"

                ":param arg1: new length in bytes\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("seek", &GXBF_wrap_seek,
                "seek((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Moves file position\n\n"

                ":param arg1: number of bytes from reference point\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`BF_SEEK`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Terminates if attempt to move past the end of\n"
                "   					a read-only file.\n"
                "   				\n\n"
               );
    pyClass.def("copy", &GXBF_wrap_copy,
                "copy((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy entire contents of a source BF to a destination BF\n\n"

                ":param arg1: Destination BF\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("crc", &GXBF_wrap_crc,
                "crc((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute CRC of a file.\n\n"

                ":param arg1: number of bytes to CRC\n"
                ":type arg1: int\n"
                ":param arg2: CRC start (use \\ :ref:`CRC_INIT_VALUE`\\  for new)\n"
                ":type arg2: int\n"
                ":returns: CRC Value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXBF_wrap_create,
                "create((str)arg1, (int)arg2) -> GXBF:\n"

                "\n.. parsed-literal::\n\n"
                "   Create BF object.\n\n"

                ":param arg1: file name to open (\"\" is a temporary file)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`BF_OPEN_MODE`\\ \n"
                ":type arg2: int\n"
                ":returns: BF Object\n"
                ":rtype: :class:`geosoft.gxapi.GXBF`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Run-time specific directory paths may be added the the front of file names\n"
                "   					as follows:\n"
                "   \n"
                "   					<geosoft>      the main Geosoft installation directory\n"
                "   					<geosoft2>     the secondary Geosoft installation directory\n"
                "   					<geotemp>      the Geosoft temporary file directory\n"
                "   					<windows>      the operating system Windows directory\n"
                "   					<system>       the operating system system directory\n"
                "   					<other>        other environment variables\n"
                "   \n"
                "   					For example \"<geosoft>/user/csv/datum.csv\"\n"
                "   				\n\n"
               ).staticmethod("create");
    pyClass.def("create_sbf", &GXBF_wrap_create_sbf,
                "create_sbf((GXSBF)arg1, (str)arg2, (int)arg3) -> GXBF:\n"

                "\n.. parsed-literal::\n\n"
                "   Create BF object inside an SBF.\n\n"

                ":param arg1: Storage\n"
                ":type arg1: :class:`geosoft.gxapi.GXSBF`\n"
                ":param arg2: file name to open (\"\" is a temporary file)\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`BF_OPEN_MODE`\\ \n"
                ":type arg3: int\n"
                ":returns: BF Object\n"
                ":rtype: :class:`geosoft.gxapi.GXBF`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   see sbf.gxh\n\n"
               ).staticmethod("create_sbf");
    pyClass.def("eof", &GXBF_wrap_eof,
                "eof() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns 1 if at the end of the file\n\n"

                ":returns: 1 if at the end of the file,\n"
                "          						0 if not at the end of the file\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("query_write", &GXBF_wrap_query_write,
                "query_write() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check if you can write to the BF.\n\n"

                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("read_binary_string", &GXBF_wrap_read_binary_string,
                "read_binary_string((int)arg1, (int)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads string data from current position in BF\n\n"

                ":param arg1: Number of bytes to read\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`BF_ENCODE`\\ \n"
                ":type arg2: int\n"
                ":param arg3: data\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("size", &GXBF_wrap_size,
                "size() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the file length\n\n"

                ":returns: File size in bytes.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("tell", &GXBF_wrap_tell,
                "tell() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns current position of file pointer in bytes\n\n"

                ":returns: Current file pointer location\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("read_int", &GXBF_wrap_read_int,
                "read_int((int)arg1, (int_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads int data from current position in BF\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\  and \\ :ref:`BF_BYTEORDER`\\ \n"
                ":type arg1: int\n"
                ":param arg2: data\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the data source may be in byte order different from that\n"
                "   					required by the reader, you can add the source byte-order\n"
                "   					to the BF elelment type.  The byte order will be swapped\n"
                "   					if required.  For example, to write out a real number 3.5\n"
                "   					with Most-Significant_Byte first (Mortorola) convention:\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXBF.write_double`\\ (hBF,BF_BYTEORDER_MSB+GS_REAL,3.5).\n"
                "   \n"
                "   					If a byte order is not specified, the source is assumed to be\n"
                "   					in the native byte order of the reading/writing computer.\n"
                "   				\n\n"
               );
    pyClass.def("read_double", &GXBF_wrap_read_double,
                "read_double((int)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads real data from current position in BF\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\  and \\ :ref:`BF_BYTEORDER`\\ \n"
                ":type arg1: int\n"
                ":param arg2: data\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the data source may be in byte order different from that\n"
                "   					required by the reader, you can add the source byte-order\n"
                "   					to the BF elelment type.  The byte order will be swapped\n"
                "   					if required.  For example, to write out a real number 3.5\n"
                "   					with Most-Significant_Byte first (Mortorola) convention:\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXBF.write_double`\\ (hBF,BF_BYTEORDER_MSB+GS_REAL,3.5).\n"
                "   \n"
                "   					If a byte order is not specified, the source is assumed to be\n"
                "   					in the native byte order of the reading/writing computer.\n"
                "   				\n\n"
               );
    pyClass.def("read_vv", &GXBF_wrap_read_vv,
                "read_vv((int)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read data to a VV from current position in BF\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\  and \\ :ref:`BF_BYTEORDER`\\ \n"
                ":type arg1: int\n"
                ":param arg2: VV data to read, VV length is read\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the data source may be in byte order different from that\n"
                "   					required by the reader, you can add the source byte-order\n"
                "   					to the BF elelment type.  The byte order will be swapped\n"
                "   					if required.  For example, to write out a real number 3.5\n"
                "   					with Most-Significant_Byte first (Mortorola) convention:\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXBF.write_double`\\ (hBF,BF_BYTEORDER_MSB+GS_REAL,3.5).\n"
                "   \n"
                "   					If a byte order is not specified, the source is assumed to be\n"
                "   					in the native byte order of the reading/writing computer.\n"
                "   				\n\n"
               );
    pyClass.def("set_destroy_status", &GXBF_wrap_set_destroy_status,
                "set_destroy_status((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the flag to delete the file on close\n\n"

                ":param arg1: \\ :ref:`BF_CLOSE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("write_binary_string", &GXBF_wrap_write_binary_string,
                "write_binary_string((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a binary string to a BF\n\n"

                ":param arg1: \\ :ref:`BF_ENCODE`\\ \n"
                ":type arg1: int\n"
                ":param arg2: string to write out\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("write_data_null", &GXBF_wrap_write_data_null,
                "write_data_null() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes a null byte (0) to BF\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("write_int", &GXBF_wrap_write_int,
                "write_int((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes int to the BF\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\  and \\ :ref:`BF_BYTEORDER`\\ \n"
                ":type arg1: int\n"
                ":param arg2: data\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See comments on byte order for the Read.. functions if you\n"
                "   					want to enforce a certain byte order.\n"
                "   \n"
                "   					If a byte order is not specified, the data is written\n"
                "   					in the native byte order of the writing computer.\n"
                "   				\n\n"
               );
    pyClass.def("write_double", &GXBF_wrap_write_double,
                "write_double((int)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes real to the BF\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\  and \\ :ref:`BF_BYTEORDER`\\ \n"
                ":type arg1: int\n"
                ":param arg2: data\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See comments on byte order for the Read.. functions if you\n"
                "   					want to enforce a certain byte order.\n"
                "   \n"
                "   					If a byte order is not specified, the data is written\n"
                "   					in the native byte order of the writing computer.\n"
                "   				\n\n"
               );
    pyClass.def("write_vv", &GXBF_wrap_write_vv,
                "write_vv((int)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes VV to the BF\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\  and \\ :ref:`BF_BYTEORDER`\\ \n"
                ":type arg1: int\n"
                ":param arg2: data\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See comments on byte order for the Read.. functions if you\n"
                "   					want to enforce a certain byte order.\n"
                "   \n"
                "   					If a byte order is not specified, the data is written\n"
                "   					in the native byte order of the writing computer.\n"
                "   				\n\n"
               );

    scope().attr("BF_BYTEORDER_LSB") = (int32_t)256;
    scope().attr("BF_BYTEORDER_MSB") = (int32_t)512;
    scope().attr("BF_KEEP") = (int32_t)0;
    scope().attr("BF_DELETE") = (int32_t)1;
    scope().attr("BF_ENCODE_ANSI") = (int32_t)0;
    scope().attr("BF_ENCODE_UTF8") = (int32_t)1;
    scope().attr("BF_READ") = (int32_t)0;
    scope().attr("BF_READWRITE_NEW") = (int32_t)1;
    scope().attr("BF_READWRITE_OLD") = (int32_t)2;
    scope().attr("BF_READWRITE_APP") = (int32_t)4;
    scope().attr("BF_SEEK_START") = (int32_t)0;
    scope().attr("BF_SEEK_CURRENT") = (int32_t)1;
    scope().attr("BF_SEEK_EOF") = (int32_t)2;

}
