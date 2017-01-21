#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXCOMPtr GXCOM_wrap_create(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    GXCOMPtr ret = GXCOM::create(arg1, (COM_BAUD)arg2, (COM_DATASIZE)arg3, (COM_PARITY)arg4, (COM_STOPBITS)arg5, (COM_FLOWCONTROL)arg6, arg7);
    return ret;
}
inline GXCOMPtr GXCOM_wrap_create_no_terminate(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    GXCOMPtr ret = GXCOM::create_no_terminate(arg1, (COM_BAUD)arg2, (COM_DATASIZE)arg3, (COM_PARITY)arg4, (COM_STOPBITS)arg5, (COM_FLOWCONTROL)arg6, arg7);
    return ret;
}
inline int32_t GXCOM_wrap_read_line_no_terminate(GXCOMPtr self, str_ref& arg1)
{
    int32_t ret = self->read_line_no_terminate(arg1);
    return ret;
}
inline int32_t GXCOM_wrap_read_chars_no_terminate(GXCOMPtr self, str_ref& arg1)
{
    int32_t ret = self->read_chars_no_terminate(arg1);
    return ret;
}
inline void GXCOM_wrap_read_line(GXCOMPtr self, str_ref& arg1)
{
    self->read_line(arg1);
}
inline int32_t GXCOM_wrap_write_chars_no_terminate(GXCOMPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->write_chars_no_terminate(arg1);
    return ret;
}
inline void GXCOM_wrap_purge_comm(GXCOMPtr self)
{
    self->purge_comm();
}
inline void GXCOM_wrap_read_chars(GXCOMPtr self, str_ref& arg1)
{
    self->read_chars(arg1);
}
inline void GXCOM_wrap_read_em61_lines_wa(GXCOMPtr self, int32_t arg1, GXWAPtr arg2)
{
    self->read_em61_lines_wa(arg1, arg2);
}
inline void GXCOM_wrap_read_file2_wa(GXCOMPtr self, GXWAPtr arg1)
{
    self->read_file2_wa(arg1);
}
inline void GXCOM_wrap_read_lines_wa(GXCOMPtr self, int32_t arg1, GXWAPtr arg2)
{
    self->read_lines_wa(arg1, arg2);
}
inline void GXCOM_wrap_set_time_out(GXCOMPtr self, int32_t arg1)
{
    self->set_time_out(arg1);
}
inline void GXCOM_wrap_write_chars(GXCOMPtr self, const gx_string_type& arg1)
{
    self->write_chars(arg1);
}
inline void GXCOM_wrap_write_line(GXCOMPtr self, const gx_string_type& arg1)
{
    self->write_line(arg1);
}

void gxPythonImportGXCOM()
{

    class_<GXCOM, GXCOMPtr> pyClass("GXCOM",
                                    "\n.. parsed-literal::\n\n"
                                    "   This class is used to communicate with external serial devices. It allows the setting of timeouts.\n\n"
                                    , no_init);

    pyClass.def("null", &GXCOM::null, "null() -> GXCOM\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXCOM`\n\n:returns: A null :class:`geosoft.gxapi.GXCOM`\n:rtype: :class:`geosoft.gxapi.GXCOM`\n").staticmethod("null");
    pyClass.def("is_null", &GXCOM::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXCOM is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXCOM`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXCOM::_internal_handle);
    pyClass.def("create", &GXCOM_wrap_create,
                "create((str)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> GXCOM:\n"

                "\n.. parsed-literal::\n\n"
                "   Create COM object.\n\n"

                ":param arg1: port name to open (\"COM1\" is example)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`COM_BAUD`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`COM_DATASIZE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`COM_PARITY`\\ \n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`COM_STOPBITS`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`COM_FLOWCONTROL`\\ \n"
                ":type arg6: int\n"
                ":param arg7: Timeout in Ms (500)\n"
                ":type arg7: int\n"
                ":returns: COM Object\n"
                ":rtype: :class:`geosoft.gxapi.GXCOM`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_no_terminate", &GXCOM_wrap_create_no_terminate,
                "create_no_terminate((str)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> GXCOM:\n"

                "\n.. parsed-literal::\n\n"
                "   Create COM object.\n\n"

                ":param arg1: port name to open (\"COM1\" is example)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`COM_BAUD`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`COM_DATASIZE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`COM_PARITY`\\ \n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`COM_STOPBITS`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`COM_FLOWCONTROL`\\ \n"
                ":type arg6: int\n"
                ":param arg7: Timeout in Ms (500)\n"
                ":type arg7: int\n"
                ":returns: COM Object\n"
                ":rtype: :class:`geosoft.gxapi.GXCOM`\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("create_no_terminate");
    pyClass.def("read_line_no_terminate", &GXCOM_wrap_read_line_no_terminate,
                "read_line_no_terminate((str_ref)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads a Line from the COM\n\n"

                ":param arg1: string for line\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - if successful in reading a line\n"
                "          1 - if an error was encountered\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("read_chars_no_terminate", &GXCOM_wrap_read_chars_no_terminate,
                "read_chars_no_terminate((str_ref)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads characters from the COM, times out and does not terminate\n\n"

                ":param arg1: string for characters\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 1 - if time out or error\n"
                "          0 - if successful\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("read_line", &GXCOM_wrap_read_line,
                "read_line((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads a Line from the COM\n\n"

                ":param arg1: string for line\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("write_chars_no_terminate", &GXCOM_wrap_write_chars_no_terminate,
                "write_chars_no_terminate((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes characters to the COM.  Does not terminate upon error\n\n"

                ":param arg1: line to write\n"
                ":type arg1: str\n"
                ":returns: 0 - if successful in writing a string\n"
                "          1 - if time out or error was encountered\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("purge_comm", &GXCOM_wrap_purge_comm,
                "purge_comm() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Purges the input and output buffers.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("read_chars", &GXCOM_wrap_read_chars,
                "read_chars((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads characters from the COM\n\n"

                ":param arg1: string for characters\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("read_em61_lines_wa", &GXCOM_wrap_read_em61_lines_wa,
                "read_em61_lines_wa((int)arg1, (GXWA)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads Lines from the COM to a WA: Geonics EM61 only\n\n"

                ":param arg1: number of lines\n"
                ":type arg1: int\n"
                ":param arg2: Where to put lines\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("read_file2_wa", &GXCOM_wrap_read_file2_wa,
                "read_file2_wa((GXWA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads entire dataset from the COM to a WA\n\n"

                ":param arg1: Where to put lines\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("read_lines_wa", &GXCOM_wrap_read_lines_wa,
                "read_lines_wa((int)arg1, (GXWA)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads Lines from the COM to a WA\n\n"

                ":param arg1: number of lines\n"
                ":type arg1: int\n"
                ":param arg2: Where to put lines\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_time_out", &GXCOM_wrap_set_time_out,
                "set_time_out((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the timeout value.\n\n"

                ":param arg1: Timeout in Ms (500)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("write_chars", &GXCOM_wrap_write_chars,
                "write_chars((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes characters to the COM\n\n"

                ":param arg1: line to write\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("write_line", &GXCOM_wrap_write_line,
                "write_line((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes a Line to the COM\n\n"

                ":param arg1: line to write\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );

    scope().attr("COM_BAUD_110") = (int32_t)0;
    scope().attr("COM_BAUD_300") = (int32_t)1;
    scope().attr("COM_BAUD_600") = (int32_t)2;
    scope().attr("COM_BAUD_1200") = (int32_t)3;
    scope().attr("COM_BAUD_2400") = (int32_t)4;
    scope().attr("COM_BAUD_4800") = (int32_t)5;
    scope().attr("COM_BAUD_9600") = (int32_t)6;
    scope().attr("COM_BAUD_14400") = (int32_t)7;
    scope().attr("COM_BAUD_19200") = (int32_t)8;
    scope().attr("COM_BAUD_56000") = (int32_t)9;
    scope().attr("COM_BAUD_57600") = (int32_t)10;
    scope().attr("COM_BAUD_115200") = (int32_t)11;
    scope().attr("COM_BAUD_128000") = (int32_t)12;
    scope().attr("COM_BAUD_256000") = (int32_t)13;
    scope().attr("COM_BAUD_38400") = (int32_t)14;
    scope().attr("COM_DATASIZE_FIVE") = (int32_t)5;
    scope().attr("COM_DATASIZE_SIX") = (int32_t)6;
    scope().attr("COM_DATASIZE_SEVEN") = (int32_t)7;
    scope().attr("COM_DATASIZE_EIGHT") = (int32_t)8;
    scope().attr("COM_FLOWCONTROL_NONE") = (int32_t)0;
    scope().attr("COM_FLOWCONTROL_RTS_CTS") = (int32_t)1;
    scope().attr("COM_FLOWCONTROL_DTR_DSR") = (int32_t)2;
    scope().attr("COM_FLOWCONTROL_XON_XOFF") = (int32_t)3;
    scope().attr("COM_PARITY_EVEN") = (int32_t)0;
    scope().attr("COM_PARITY_NARK") = (int32_t)1;
    scope().attr("COM_PARITY_NONE") = (int32_t)2;
    scope().attr("COM_PARITY_ODD") = (int32_t)3;
    scope().attr("COM_PARITY_SPACE") = (int32_t)4;
    scope().attr("COM_STOPBITS_ONE") = (int32_t)0;
    scope().attr("COM_STOPBITS_ONE5") = (int32_t)1;
    scope().attr("COM_STOPBITS_TWO") = (int32_t)2;

}
