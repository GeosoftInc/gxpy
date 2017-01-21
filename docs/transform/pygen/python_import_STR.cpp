#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline int32_t GXSTR_wrap_scan_i(const gx_string_type& arg1)
{
    int32_t ret = GXSTR::scan_i(arg1);
    return ret;
}
inline double GXSTR_wrap_scan_date(const gx_string_type& arg1, int32_t arg2)
{
    double ret = GXSTR::scan_date(arg1, (DATE_FORMAT)arg2);
    return ret;
}
inline double GXSTR_wrap_scan_form(const gx_string_type& arg1, int32_t arg2)
{
    double ret = GXSTR::scan_form(arg1, (GS_FORMATS)arg2);
    return ret;
}
inline double GXSTR_wrap_scan_r(const gx_string_type& arg1)
{
    double ret = GXSTR::scan_r(arg1);
    return ret;
}
inline double GXSTR_wrap_scan_time(const gx_string_type& arg1, int32_t arg2)
{
    double ret = GXSTR::scan_time(arg1, (TIME_FORMAT)arg2);
    return ret;
}
inline void GXSTR_wrap_file_combine_parts(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, str_ref& arg6)
{
    GXSTR::file_combine_parts(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXSTR_wrap_file_ext(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3, int32_t arg4)
{
    GXSTR::file_ext(arg1, arg2, arg3, (FILE_EXT)arg4);
}
inline void GXSTR_wrap_file_name_part(const gx_string_type& arg1, str_ref& arg2, int32_t arg3)
{
    GXSTR::file_name_part(arg1, arg2, (STR_FILE_PART)arg3);
}
inline void GXSTR_wrap_get_m_file(const gx_string_type& arg1, str_ref& arg2, int32_t arg3)
{
    GXSTR::get_m_file(arg1, arg2, arg3);
}
inline void GXSTR_wrap_remove_qualifiers(const gx_string_type& arg1, str_ref& arg2)
{
    GXSTR::remove_qualifiers(arg1, arg2);
}
inline void GXSTR_wrap_format_crc(int32_t arg1, str_ref& arg2, int32_t arg3)
{
    GXSTR::format_crc(arg1, arg2, arg3);
}
inline void GXSTR_wrap_format_date(double arg1, str_ref& arg2, int32_t arg3, int32_t arg4)
{
    GXSTR::format_date(arg1, arg2, arg3, (DATE_FORMAT)arg4);
}
inline void GXSTR_wrap_format_i(int32_t arg1, str_ref& arg2, int32_t arg3)
{
    GXSTR::format_i(arg1, arg2, arg3);
}
inline void GXSTR_wrap_format_r(double arg1, str_ref& arg2, int32_t arg3, int32_t arg4)
{
    GXSTR::format_r(arg1, arg2, arg3, arg4);
}
inline void GXSTR_wrap_format_r2(double arg1, str_ref& arg2, int32_t arg3, int32_t arg4)
{
    GXSTR::format_r2(arg1, arg2, arg3, arg4);
}
inline void GXSTR_wrap_format_double(double arg1, str_ref& arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXSTR::format_double(arg1, arg2, (GS_FORMATS)arg3, arg4, arg5);
}
inline void GXSTR_wrap_format_time(double arg1, str_ref& arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXSTR::format_time(arg1, arg2, arg3, arg4, (TIME_FORMAT)arg5);
}
inline void GXSTR_wrap_escape(str_ref& arg1, int32_t arg2)
{
    GXSTR::escape(arg1, (STR_ESCAPE)arg2);
}
inline int32_t GXSTR_wrap_get_char(const gx_string_type& arg1)
{
    int32_t ret = GXSTR::get_char(arg1);
    return ret;
}
inline int32_t GXSTR_wrap_char_n(const gx_string_type& arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = GXSTR::char_n(arg1, arg2, arg3);
    return ret;
}
inline void GXSTR_wrap_justify(const gx_string_type& arg1, str_ref& arg2, int32_t arg3, int32_t arg4)
{
    GXSTR::justify(arg1, arg2, arg3, (STR_JUSTIFY)arg4);
}
inline void GXSTR_wrap_replacei_match_string(str_ref& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXSTR::replacei_match_string(arg1, arg2, arg3);
}
inline void GXSTR_wrap_replace_match_string(str_ref& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXSTR::replace_match_string(arg1, arg2, arg3);
}
inline void GXSTR_wrap_set_char_n(str_ref& arg1, int32_t arg2, int32_t arg3)
{
    GXSTR::set_char_n(arg1, arg2, arg3);
}
inline void GXSTR_wrap_split_string(str_ref& arg1, const gx_string_type& arg2, str_ref& arg3)
{
    GXSTR::split_string(arg1, arg2, arg3);
}
inline void GXSTR_wrap_strcat(str_ref& arg1, const gx_string_type& arg2)
{
    GXSTR::strcat(arg1, arg2);
}
inline int32_t GXSTR_wrap_strcmp(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    int32_t ret = GXSTR::strcmp(arg1, arg2, (STR_CASE)arg3);
    return ret;
}
inline void GXSTR_wrap_strcpy(str_ref& arg1, const gx_string_type& arg2)
{
    GXSTR::strcpy(arg1, arg2);
}
inline int32_t GXSTR_wrap_stri_mask(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSTR::stri_mask(arg1, arg2);
    return ret;
}
inline void GXSTR_wrap_strins(str_ref& arg1, int32_t arg2, const gx_string_type& arg3)
{
    GXSTR::strins(arg1, arg2, arg3);
}
inline int32_t GXSTR_wrap_strlen(const gx_string_type& arg1)
{
    int32_t ret = GXSTR::strlen(arg1);
    return ret;
}
inline int32_t GXSTR_wrap_str_mask(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSTR::str_mask(arg1, arg2);
    return ret;
}
inline int32_t GXSTR_wrap_str_min(str_ref& arg1)
{
    int32_t ret = GXSTR::str_min(arg1);
    return ret;
}
inline int32_t GXSTR_wrap_str_min2(const gx_string_type& arg1)
{
    int32_t ret = GXSTR::str_min2(arg1);
    return ret;
}
inline int32_t GXSTR_wrap_strncmp(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4)
{
    int32_t ret = GXSTR::strncmp(arg1, arg2, arg3, (STR_CASE)arg4);
    return ret;
}
inline int32_t GXSTR_wrap_str_str(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    int32_t ret = GXSTR::str_str(arg1, arg2, (STR_CASE)arg3);
    return ret;
}
inline void GXSTR_wrap_substr(str_ref& arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4)
{
    GXSTR::substr(arg1, arg2, arg3, arg4);
}
inline void GXSTR_wrap_to_lower(str_ref& arg1)
{
    GXSTR::to_lower(arg1);
}
inline void GXSTR_wrap_to_upper(str_ref& arg1)
{
    GXSTR::to_upper(arg1);
}
inline void GXSTR_wrap_xyz_line(const gx_string_type& arg1, str_ref& arg2)
{
    GXSTR::xyz_line(arg1, arg2);
}
inline void GXSTR_wrap_make_alpha(str_ref& arg1)
{
    GXSTR::make_alpha(arg1);
}
inline void GXSTR_wrap_printf(str_ref& arg1, const gx_string_type& arg2)
{
    GXSTR::printf(arg1, arg2);
}
inline void GXSTR_wrap_replace_char(str_ref& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXSTR::replace_char(arg1, arg2, arg3);
}
inline void GXSTR_wrap_replace_char2(str_ref& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXSTR::replace_char2(arg1, arg2, arg3);
}
inline void GXSTR_wrap_replace_multi_char(str_ref& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXSTR::replace_multi_char(arg1, arg2, arg3);
}
inline void GXSTR_wrap_replace_non_ascii(str_ref& arg1, const gx_string_type& arg2)
{
    GXSTR::replace_non_ascii(arg1, arg2);
}
inline void GXSTR_wrap_set_char(str_ref& arg1, int32_t arg2)
{
    GXSTR::set_char(arg1, arg2);
}
inline void GXSTR_wrap_trim_quotes(str_ref& arg1)
{
    GXSTR::trim_quotes(arg1);
}
inline void GXSTR_wrap_trim_space(str_ref& arg1, int32_t arg2)
{
    GXSTR::trim_space(arg1, (STR_TRIM)arg2);
}
inline void GXSTR_wrap_un_quote(str_ref& arg1)
{
    GXSTR::un_quote(arg1);
}
inline void GXSTR_wrap_gen_group_name(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, str_ref& arg4)
{
    GXSTR::gen_group_name(arg1, arg2, arg3, arg4);
}
inline int32_t GXSTR_wrap_count_tokens(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSTR::count_tokens(arg1, arg2);
    return ret;
}
inline void GXSTR_wrap_get_token(str_ref& arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXSTR::get_token(arg1, arg2, arg3);
}
inline int32_t GXSTR_wrap_tokenize(str_ref& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    int32_t ret = GXSTR::tokenize(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXSTR_wrap_tokens(str_ref& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSTR::tokens(arg1, arg2);
    return ret;
}
inline int32_t GXSTR_wrap_tokens2(str_ref& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    int32_t ret = GXSTR::tokens2(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline void GXSTR_wrap_parse_list(const gx_string_type& arg1, GXVVPtr arg2)
{
    GXSTR::parse_list(arg1, arg2);
}

void gxPythonImportGXSTR()
{

    class_<GXSTR, boost::noncopyable> pyClass("GXSTR",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		This library is not a class. Use the STR library functions\n"
            "   		to work with and manipulate string variables. Since the\n"
            "   		GX Programming Language does not provide string literal\n"
            "   		tokens, you must use these functions for any string operations\n"
            "   		you want to perform.\n"
            "   	\n\n"
            , no_init);


    pyClass.def("scan_i", &GXSTR_wrap_scan_i,
                "scan_i((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a string to a GX int.\n\n"

                ":param arg1: String to convert to an integer\n"
                ":type arg1: str\n"
                ":returns: Resulting Integer, iDUMMY is bad integer\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("scan_i");
    pyClass.def("scan_date", &GXSTR_wrap_scan_date,
                "scan_date((str)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a date string to a GX real.\n\n"

                ":param arg1: Date string\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DATE_FORMAT`\\ \n"
                ":type arg2: int\n"
                ":returns: Resulting Real, rDUMMY if conversion fails.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   OLD usage, use ScanForm_STR instead.\n\n"
               ).staticmethod("scan_date");
    pyClass.def("scan_form", &GXSTR_wrap_scan_form,
                "scan_form((str)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a formated string to a real.\n\n"

                ":param arg1: Date string\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`GS_FORMATS`\\ \n"
                ":type arg2: int\n"
                ":returns: Resulting Real, rDUMMY if conversion fails.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("scan_form");
    pyClass.def("scan_r", &GXSTR_wrap_scan_r,
                "scan_r((str)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a string to a GX real.\n\n"

                ":param arg1: String to convert to a real\n"
                ":type arg1: str\n"
                ":returns: Resulting Real, rDUMMY if bad string.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("scan_r");
    pyClass.def("scan_time", &GXSTR_wrap_scan_time,
                "scan_time((str)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a time string to a GX real.\n\n"

                ":param arg1: Date string\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`TIME_FORMAT`\\ \n"
                ":type arg2: int\n"
                ":returns: Resulting Real, rDUMMY if conversion fails.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   OLD usage, use ScanForm_STR instead.\n\n"
               ).staticmethod("scan_time");
    pyClass.def("file_combine_parts", &GXSTR_wrap_file_combine_parts,
                "file_combine_parts((str)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Combine file parts to build a file name.\n\n"

                ":param arg1: drive\n"
                ":type arg1: str\n"
                ":param arg2: directory\n"
                ":type arg2: str\n"
                ":param arg3: name\n"
                ":type arg3: str\n"
                ":param arg4: extension\n"
                ":type arg4: str\n"
                ":param arg5: qualifiers\n"
                ":type arg5: str\n"
                ":param arg6: destination string, can be same as input\n"
                ":type arg6: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("file_combine_parts");
    pyClass.def("file_ext", &GXSTR_wrap_file_ext,
                "file_ext((str)arg1, (str)arg2, (str_ref)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a file extension onto a file name string.\n\n"

                ":param arg1: file name to extend\n"
                ":type arg1: str\n"
                ":param arg2: extension if \"\", extenstion and '.' are stripped.\n"
                ":type arg2: str\n"
                ":param arg3: extended file name (can be same as input)\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: \\ :ref:`FILE_EXT`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("file_ext");
    pyClass.def("file_name_part", &GXSTR_wrap_file_name_part,
                "file_name_part((str)arg1, (str_ref)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get part of a file name.\n\n"

                ":param arg1: file name\n"
                ":type arg1: str\n"
                ":param arg2: destination string, can be same as input\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: \\ :ref:`STR_FILE_PART`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("file_name_part");
    pyClass.def("get_m_file", &GXSTR_wrap_get_m_file,
                "get_m_file((str)arg1, (str_ref)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the indexed filepath from a multiple filepath string\n\n"

                ":param arg1: input multifile string\n"
                ":type arg1: str\n"
                ":param arg2: output filepath string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: index of file\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The multifile string must use '\\ `|`\\ ' as a delimiter.\n"
                "   					Do not pass a string after calling \\ :func:`geosoft.gxapi.GXSTR.tokenize`\\ .\n"
                "   				\n\n"
               ).staticmethod("get_m_file");
    pyClass.def("remove_qualifiers", &GXSTR_wrap_remove_qualifiers,
                "remove_qualifiers((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove file qualifiers from a file name\n\n"

                ":param arg1: input file name\n"
                ":type arg1: str\n"
                ":param arg2: output file name (can be same as input)\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.1\n\n"
               ).staticmethod("remove_qualifiers");
    pyClass.def("format_crc", &GXSTR_wrap_format_crc,
                "format_crc((int)arg1, (str_ref)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a GX CRC value to a string.\n\n"

                ":param arg1: CRC value to format\n"
                ":type arg1: int\n"
                ":param arg2: Resulting string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Width of the field\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("format_crc");
    pyClass.def("format_date", &GXSTR_wrap_format_date,
                "format_date((float)arg1, (str_ref)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a GX real to a date string.\n\n"

                ":param arg1: date value in decimal years to format\n"
                ":type arg1: float\n"
                ":param arg2: Resulting string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Width of the field\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`DATE_FORMAT`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("format_date");
    pyClass.def("format_i", &GXSTR_wrap_format_i,
                "format_i((int)arg1, (str_ref)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a GX int to a string.\n\n"

                ":param arg1: value to format\n"
                ":type arg1: int\n"
                ":param arg2: Resulting string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Width of the field\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("format_i");
    pyClass.def("format_r", &GXSTR_wrap_format_r,
                "format_r((float)arg1, (str_ref)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a GX real to a string with significant digits.\n\n"

                ":param arg1: value to format\n"
                ":type arg1: float\n"
                ":param arg2: Resulting string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Width of the field\n"
                ":type arg3: int\n"
                ":param arg4: Significant digits\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("format_r");
    pyClass.def("format_r2", &GXSTR_wrap_format_r2,
                "format_r2((float)arg1, (str_ref)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a GX real to a string with given decimals.\n\n"

                ":param arg1: value to format\n"
                ":type arg1: float\n"
                ":param arg2: Resulting string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Width of the field\n"
                ":type arg3: int\n"
                ":param arg4: Decimals\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("format_r2");
    pyClass.def("format_double", &GXSTR_wrap_format_double,
                "format_double((float)arg1, (str_ref)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a GX real to a string.\n\n"

                ":param arg1: value to format\n"
                ":type arg1: float\n"
                ":param arg2: Resulting string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: \\ :ref:`GS_FORMATS`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Width of the field\n"
                ":type arg4: int\n"
                ":param arg5: Significant digits/decimals\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("format_double");
    pyClass.def("format_time", &GXSTR_wrap_format_time,
                "format_time((float)arg1, (str_ref)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a GX real to a time string.\n\n"

                ":param arg1: time value in decimal hours to format\n"
                ":type arg1: float\n"
                ":param arg2: Resulting string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Width of the field\n"
                ":type arg3: int\n"
                ":param arg4: Decimals to format with\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`TIME_FORMAT`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("format_time");
    pyClass.def("escape", &GXSTR_wrap_escape,
                "escape((str_ref)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert/replace escape sequences in strings.\n\n"

                ":param arg1: string to modify\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: \\ :ref:`STR_ESCAPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Escape characters:\n"
                "   \n"
                "   					\\a      bell\n"
                "   					\\b      backspace\n"
                "   					\\f      formfeed\n"
                "   					\\n      new line\n"
                "   					\\r      carriage return\n"
                "   					\\t      tab\n"
                "   					\\v      vertical tab\n"
                "   					\\\"      quote character\n"
                "   					\\x      take 'x' literally\n"
                "   					\\\\      backslash\n"
                "   					\\ooo    octal up to 3 characters\n"
                "   					\\xhh    hex up to 2 characters\n"
                "   \n"
                "   					A common use of this function is to convert double-quote characters in\n"
                "   					a user unput string to \\\" so the string can be placed in a tokenized\n"
                "   					string.\n"
                "   				\n\n"
               ).staticmethod("escape");
    pyClass.def("get_char", &GXSTR_wrap_get_char,
                "get_char((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the ASCII value of a character.\n\n"

                ":param arg1: string to return ascii value of first character\n"
                ":type arg1: str\n"
                ":returns: ASCII value of first character in string.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_char");
    pyClass.def("char_n", &GXSTR_wrap_char_n,
                "char_n((str)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the ASCII value of the n'th character.\n\n"

                ":param arg1: string\n"
                ":type arg1: str\n"
                ":param arg2: character to get\n"
                ":type arg2: int\n"
                ":param arg3: maximum string length (unused)\n"
                ":type arg3: int\n"
                ":returns: ASCII value of n'th character in string.\n"
                "          						The first character is 0.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("char_n");
    pyClass.def("justify", &GXSTR_wrap_justify,
                "justify((str)arg1, (str_ref)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Justify a string\n\n"

                ":param arg1: string to justify\n"
                ":type arg1: str\n"
                ":param arg2: result string, can be same as input\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: justification width\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`STR_JUSTIFY`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the string is too big to fit in the number of display characters,\n"
                "   					the output string will be \"\\ `*`\\ \\ `*`\\ \" justified as specified.\n"
                "   				\n\n"
               ).staticmethod("justify");
    pyClass.def("replacei_match_string", &GXSTR_wrap_replacei_match_string,
                "replacei_match_string((str_ref)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replaces all occurances of match string by replacement string with case insensitive.\n\n"

                ":param arg1: Destination String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: match string to replace\n"
                ":type arg2: str\n"
                ":param arg3: replacement string\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the replacement string is \"\" (NULL character)\n"
                "   					then the string to replace is removed from the\n"
                "   					input string, and the string is shortened.\n"
                "   				\n\n"
               ).staticmethod("replacei_match_string");
    pyClass.def("replace_match_string", &GXSTR_wrap_replace_match_string,
                "replace_match_string((str_ref)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replaces all occurances of match string by replacement string with case sensitive.\n\n"

                ":param arg1: Destination String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: match string to replace\n"
                ":type arg2: str\n"
                ":param arg3: replacement string\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the replacement string is \"\" (NULL character)\n"
                "   					then the string to replace is removed from the\n"
                "   					input string, and the string is shortened.\n"
                "   				\n\n"
               ).staticmethod("replace_match_string");
    pyClass.def("set_char_n", &GXSTR_wrap_set_char_n,
                "set_char_n((str_ref)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the n'th character of a string using an ASCII value\n\n"

                ":param arg1: string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: character to set\n"
                ":type arg2: int\n"
                ":param arg3: ASCII value\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"
               ).staticmethod("set_char_n");
    pyClass.def("split_string", &GXSTR_wrap_split_string,
                "split_string((str_ref)arg1, (str)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Splits a string in two on a character.\n\n"

                ":param arg1: original string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: split character (first character of string)\n"
                ":type arg2: str\n"
                ":param arg3: split string past split character.\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The original string is modified by terminating it\n"
                "   					at the character split.\n"
                "   \n"
                "   					The part of the string past the character split is\n"
                "   					copied to the split string.\n"
                "   \n"
                "   					Split characters in quoted strings are ignored.\n"
                "   \n"
                "   					This function is mainly intended to separate comments\n"
                "   					from control file strings.\n"
                "   				\n\n"
               ).staticmethod("split_string");
    pyClass.def("strcat", &GXSTR_wrap_strcat,
                "strcat((str_ref)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method contatinates a string.\n\n"

                ":param arg1: Destination String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: String to add\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("strcat");
    pyClass.def("strcmp", &GXSTR_wrap_strcmp,
                "strcmp((str)arg1, (str)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method compares two strings and returns these values\n\n"

                ":param arg1: string A\n"
                ":type arg1: str\n"
                ":param arg2: string B\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`STR_CASE`\\ \n"
                ":type arg3: int\n"
                ":returns: A  <  B           -1\n"
                "          						A ==  B            0\n"
                "          						A  >  B            1\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("strcmp");
    pyClass.def("strcpy", &GXSTR_wrap_strcpy,
                "strcpy((str_ref)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method copies a string into another string.\n\n"

                ":param arg1: destination string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: origin string\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("strcpy");
    pyClass.def("stri_mask", &GXSTR_wrap_stri_mask,
                "stri_mask((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Case insensitive comparison of two strings.\n\n"

                ":param arg1: mask\n"
                ":type arg1: str\n"
                ":param arg2: string to test\n"
                ":type arg2: str\n"
                ":returns: 0 if string does not match mask.\n"
                "          						1 if string matches mask.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Mask characters '\\ `*`\\ ' - matches any one or more up to\n"
                "   					next character\n"
                "   					'?' - matches one character\n"
                "   \n"
                "   					Test is case insensitive\n"
                "   				\n\n"
               ).staticmethod("stri_mask");
    pyClass.def("strins", &GXSTR_wrap_strins,
                "strins((str_ref)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method inserts a string at a specified position.\n\n"

                ":param arg1: Destination String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Insert Position\n"
                ":type arg2: int\n"
                ":param arg3: String to add\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the specified position does not fall within the current string\n"
                "   					the source string will simply be Concatenated.\n"
                "   				\n\n"
               ).staticmethod("strins");
    pyClass.def("strlen", &GXSTR_wrap_strlen,
                "strlen((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the length of a string.\n\n"

                ":param arg1: string to find the length of\n"
                ":type arg1: str\n"
                ":returns: String length.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("strlen");
    pyClass.def("str_mask", &GXSTR_wrap_str_mask,
                "str_mask((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Case sensitive comparison of two strings.\n\n"

                ":param arg1: mask\n"
                ":type arg1: str\n"
                ":param arg2: string to test\n"
                ":type arg2: str\n"
                ":returns: 0 if string does not match mask.\n"
                "          						1 if string matches mask.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Mask characters '\\ `*`\\ ' - matches any one or more up to\n"
                "   					next character\n"
                "   					'?' - matches one character\n"
                "   \n"
                "   					Test is case sensitive\n"
                "   				\n\n"
               ).staticmethod("str_mask");
    pyClass.def("str_min", &GXSTR_wrap_str_min,
                "str_min((str_ref)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove spaces and tabs and return length\n\n"

                ":param arg1: string to find the min length of\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: String length.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					String may be modified. This function should not be\n"
                "   					used to determine if a file name string is defined, because\n"
                "   					a valid file name can contain spaces, and once \"tested\" the\n"
                "   					name will be altered. Instead, use \\ :func:`geosoft.gxapi.GXSTR.str_min2`\\ , or use\n"
                "   					\\ :func:`geosoft.gxapi.GXSYS.file_exist`\\  to see if the file actually exists.\n"
                "   				\n\n"
               ).staticmethod("str_min");
    pyClass.def("str_min2", &GXSTR_wrap_str_min2,
                "str_min2((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Length less spaces and tabs, string unchanged.\n\n"

                ":param arg1: string to find the min length of\n"
                ":type arg1: str\n"
                ":returns: String length.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("str_min2");
    pyClass.def("strncmp", &GXSTR_wrap_strncmp,
                "strncmp((str)arg1, (str)arg2, (int)arg3, (int)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Compares two strings to a given number of characters.\n\n"

                ":param arg1: string A\n"
                ":type arg1: str\n"
                ":param arg2: string B\n"
                ":type arg2: str\n"
                ":param arg3: number of characters to compare\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`STR_CASE`\\ \n"
                ":type arg4: int\n"
                ":returns: A  <  B           -1\n"
                "          						A ==  B            0\n"
                "          						A  >  B            1\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"
               ).staticmethod("strncmp");
    pyClass.def("str_str", &GXSTR_wrap_str_str,
                "str_str((str)arg1, (str)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Scan a string for the occurrence of a given substring.\n\n"

                ":param arg1: string to scan\n"
                ":type arg1: str\n"
                ":param arg2: string to look for\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`STR_CASE`\\ \n"
                ":type arg3: int\n"
                ":returns: -1 if the substring does not occur in the string\n"
                "          						Index of first matching location if found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               ).staticmethod("str_str");
    pyClass.def("substr", &GXSTR_wrap_substr,
                "substr((str_ref)arg1, (str)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extract part of a string.\n\n"

                ":param arg1: destination string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: origin string\n"
                ":type arg2: str\n"
                ":param arg3: start location\n"
                ":type arg3: int\n"
                ":param arg4: number of characters\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The destination string length will be less than the\n"
                "   					requested length if the substring is not fully enclosed\n"
                "   					in the origin string.\n"
                "   				\n\n"
               ).staticmethod("substr");
    pyClass.def("to_lower", &GXSTR_wrap_to_lower,
                "to_lower((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a string to lower case.\n\n"

                ":param arg1: String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("to_lower");
    pyClass.def("to_upper", &GXSTR_wrap_to_upper,
                "to_upper((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a string to upper case.\n\n"

                ":param arg1: String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("to_upper");
    pyClass.def("xyz_line", &GXSTR_wrap_xyz_line,
                "xyz_line((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make a valid XYZ line name from a valid DB line name.\n\n"

                ":param arg1: line name to convert\n"
                ":type arg1: str\n"
                ":param arg2: buffer to hold new line name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("xyz_line");
    pyClass.def("make_alpha", &GXSTR_wrap_make_alpha,
                "make_alpha((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Turns all non alpha-numeric characters into an _.\n\n"

                ":param arg1: String to trim\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   THE STRING IS MODIFIED.\n\n"
               ).staticmethod("make_alpha");
    pyClass.def("printf", &GXSTR_wrap_printf,
                "printf((str_ref)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Variable Argument PrintF function\n\n"

                ":param arg1: destination string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: pattern string\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               ).staticmethod("printf");
    pyClass.def("replace_char", &GXSTR_wrap_replace_char,
                "replace_char((str_ref)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replaces characters in a string.\n\n"

                ":param arg1: string to modify\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: character to replace (first character only)\n"
                ":type arg2: str\n"
                ":param arg3: replacement character (first character only)\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the input replacement character is \"\", then the\n"
                "   					string will be truncated at the first character to replace.\n"
                "   				\n\n"
               ).staticmethod("replace_char");
    pyClass.def("replace_char2", &GXSTR_wrap_replace_char2,
                "replace_char2((str_ref)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replaces characters in a string, supports simple removal.\n\n"

                ":param arg1: string to modify\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: character to replace (first character only)\n"
                ":type arg2: str\n"
                ":param arg3: replacement character (first character only)\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the replacement character is \"\" (NULL character)\n"
                "   					then the character to replace is removed from the\n"
                "   					input string, and the string is shortened.\n"
                "   				\n\n"
               ).staticmethod("replace_char2");
    pyClass.def("replace_multi_char", &GXSTR_wrap_replace_multi_char,
                "replace_multi_char((str_ref)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replaces multiple characters in a string.\n\n"

                ":param arg1: string to modify\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: characters to replace\n"
                ":type arg2: str\n"
                ":param arg3: replacement characters\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The number of characters to replace must equal\n"
                "   					the number of replacement characters.\n"
                "   				\n\n"
               ).staticmethod("replace_multi_char");
    pyClass.def("replace_non_ascii", &GXSTR_wrap_replace_non_ascii,
                "replace_non_ascii((str_ref)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replace non-ASCII characters in a string.\n\n"

                ":param arg1: string to modify\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: replacement character\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All characthers > 127 will be replaced by the first character\n"
                "   					of the replacement string.\n"
                "   				\n\n"
               ).staticmethod("replace_non_ascii");
    pyClass.def("set_char", &GXSTR_wrap_set_char,
                "set_char((str_ref)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a string's first character using an ASCII value of a character.\n\n"

                ":param arg1: string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: ASCII value\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"
               ).staticmethod("set_char");
    pyClass.def("trim_quotes", &GXSTR_wrap_trim_quotes,
                "trim_quotes((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove double quotes.\n\n"

                ":param arg1: String to trim\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					THE STRING IS MODIFIED.\n"
                "   					This method goes through the string and removes all spaces in a\n"
                "   					string except those enclosed in quotes. It then removes\n"
                "   					any quotes. It is usfull for trimming unwanted spaces from\n"
                "   					an input string but allows the user to use quotes as well.\n"
                "   					If a quote follows a backslash, the quote is retained and\n"
                "   					the backslash is deleted. These quotes are NOT treated as\n"
                "   					delimiters.\n"
                "   				\n\n"
               ).staticmethod("trim_quotes");
    pyClass.def("trim_space", &GXSTR_wrap_trim_space,
                "trim_space((str_ref)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove leading and/or trailing whitespace.\n\n"

                ":param arg1: String to trim\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: \\ :ref:`STR_TRIM`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					THE STRING IS MODIFIED.\n"
                "   					Whitespace characters are defined as space, tab, carriage return,\n"
                "   					new line, vertical tab or formfeed (0x09 to 0x0D, 0x20)\n"
                "   				\n\n"
               ).staticmethod("trim_space");
    pyClass.def("un_quote", &GXSTR_wrap_un_quote,
                "un_quote((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove double quotes from string\n\n"

                ":param arg1: String to unquote\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					THE STRING IS MODIFIED.\n"
                "   					The pointers will be advanced past a first character\n"
                "   					quote and a last character quote will be set to .\\0'.\n"
                "   					Both first and last characters must be quotes for the\n"
                "   					triming to take place.\n"
                "   				\n\n"
               ).staticmethod("un_quote");
    pyClass.def("gen_group_name", &GXSTR_wrap_gen_group_name,
                "gen_group_name((str)arg1, (str)arg2, (str)arg3, (str_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Generate a group name string\n"
                "   					from type string, database and channel(optional) strings..\n"
                "   				\n\n"

                ":param arg1: input type string (static part)\n"
                ":type arg1: str\n"
                ":param arg2: input db string\n"
                ":type arg2: str\n"
                ":param arg3: input ch string (could be 0 length)\n"
                ":type arg3: str\n"
                ":param arg4: output group name string\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The output group name string is formed in the way of typestr_dbstr_chstr.\n"
                "   					If the database/channel strings is too long to fit the output string\n"
                "   					(max total length of 1040, including the NULL ending), then\n"
                "   					the typestr will always be kept the full length to be the first part,\n"
                "   					while the dbstr and/or chstr will be shortened to be the\n"
                "   					second and/or third part of the output string.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   GenNewGroupName_MVIEW\n\n"
               ).staticmethod("gen_group_name");
    pyClass.def("count_tokens", &GXSTR_wrap_count_tokens,
                "count_tokens((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Counts number of tokens.\n\n"

                ":param arg1: string to tokenize\n"
                ":type arg1: str\n"
                ":param arg2: delimiter characters\n"
                ":type arg2: str\n"
                ":returns: Number of tokens in the string.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Delimiters are \"soft\" in that one or more delimiters\n"
                "   					is considered a single delimiter, and preceding and\n"
                "   					trailing delimiters are ignored.\n"
                "   \n"
                "   					DO NOT use this function except in GXC code. The corresponding\n"
                "   					\\ :func:`geosoft.gxapi.GXSTR.get_token`\\  function will not operate correctly in GX.Net code.\n"
                "   				\n\n"
               ).staticmethod("count_tokens");
    pyClass.def("get_token", &GXSTR_wrap_get_token,
                "get_token((str_ref)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a token from a tokenized string.\n\n"

                ":param arg1: destination string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: tokenized string\n"
                ":type arg2: str\n"
                ":param arg3: token number wanted  (0 is the first!)\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Call \\ :func:`geosoft.gxapi.GXSTR.tokens`\\   to prepare the tokenized\n"
                "   					string.\n"
                "   					You MUST NOT get tokens beyond number of tokens returned\n"
                "   					by \\ :func:`geosoft.gxapi.GXSTR.tokens`\\  or \\ :func:`geosoft.gxapi.GXSTR.tokens2`\\ .\n"
                "   					The first token has index 0.\n"
                "   \n"
                "   					DO NOT use this function except in GXC code.\n"
                "   					\\ :func:`geosoft.gxapi.GXSTR.get_token`\\  function will not operate correctly in GX.Net code.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSTR.tokens`\\ , GetToken_STR\n\n"
               ).staticmethod("get_token");
    pyClass.def("tokenize", &GXSTR_wrap_tokenize,
                "tokenize((str_ref)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Tokenize a string based on any characters.\n\n"

                ":param arg1: str - String containing token(s)\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: szSoft - Soft delimiters (spaces/tabs)\n"
                ":type arg2: str\n"
                ":param arg3: szHard - Hard delimiters (commas)\n"
                ":type arg3: str\n"
                ":param arg4: szEsc  - Escape delimiters (back-slash)\n"
                ":type arg4: str\n"
                ":param arg5: szQuote- Quote delimiters  (quote characters)\n"
                ":type arg5: str\n"
                ":returns: number of tokens\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This uses a finite state machine to tokenize on these\n"
                "   					rules:\n"
                "   \n"
                "   					1. Any one character following an escape delimiter is\n"
                "   					treated as a normal character.\n"
                "   \n"
                "   					2. Any characters inside a quote string are treated as\n"
                "   					normal characters.\n"
                "   \n"
                "   					3. Any number of Soft delimiters in sequence without a\n"
                "   					hard delimiter are treated as one hard delimited.\n"
                "   \n"
                "   					4. Any number of soft delimiters can preceed or follow\n"
                "   					a hard delimiter and are ignored.\n"
                "   \n"
                "   \n"
                "   					EXAMPLE\n"
                "   \n"
                "   					Soft = [ ]   Hard = [,]   Escape = [\\]    Quote = [\"]\n"
                "   \n"
                "   					[this is a , , the \"test,\" of   ,  \\,\\\" my delimite  fi,]\n"
                "   \n"
                "   					Results in:\n"
                "   \n"
                "   					[this] [is] [a] [] [the] [\"test,\"] [of] [\\,\\\"] [my] [delimite] [fi] []\n"
                "   \n"
                "   \n"
                "   					NOT use this function except in GXC code. The corresponding\n"
                "   					etToken_STR function will not operate correctly in GX.Net code.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   GetToken_STR\n\n"
               ).staticmethod("tokenize");
    pyClass.def("tokens", &GXSTR_wrap_tokens,
                "tokens((str_ref)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Tokenize a string\n\n"

                ":param arg1: string to tokenize\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: delimiter characters\n"
                ":type arg2: str\n"
                ":returns: number of tokens, maximum is 2048\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Delimiters in the string are reduced to a single NULL.\n"
                "   					Delimiters withing double quoted strings are ignored.\n"
                "   					Use GetToken_STR to extract tokens.\n"
                "   \n"
                "   					DO NOT use this function except in GXC code. The corresponding\n"
                "   					\\ :func:`geosoft.gxapi.GXSTR.get_token`\\  function will not operate correctly in GX.Net code.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSTR.tokens2`\\ , GetToken_STR\n\n"
               ).staticmethod("tokens");
    pyClass.def("tokens2", &GXSTR_wrap_tokens2,
                "tokens2((str_ref)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   General tokenize a string\n\n"

                ":param arg1: string to tokenize\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: szSoft - Soft delimiters (spaces/tabs)\n"
                ":type arg2: str\n"
                ":param arg3: szHard - Hard delimiters (commas)\n"
                ":type arg3: str\n"
                ":param arg4: szEsc  - Escape delimiters (back-slash)\n"
                ":type arg4: str\n"
                ":param arg5: szQuote- Quote delimiters  (quote characters)\n"
                ":type arg5: str\n"
                ":returns: Number of Tokens\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function is for old GX compatibility only.\n"
                "   					See \\ :func:`geosoft.gxapi.GXSTR.tokenize`\\ .\n"
                "   \n"
                "   					DO NOT use this function except in GXC code. The corresponding\n"
                "   					\\ :func:`geosoft.gxapi.GXSTR.get_token`\\  function will not operate correctly in GX.Net code.\n"
                "   				\n\n"
               ).staticmethod("tokens2");
    pyClass.def("parse_list", &GXSTR_wrap_parse_list,
                "parse_list((str)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Parse a tokenized list to get a selection list.\n\n"

                ":param arg1: String to be parsed\n"
                ":type arg1: str\n"
                ":param arg2: Selection Buffer to fill\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Given a list such as \"1,3,4,6-9,12\", it fills the\n"
                "   					input buffer with 1 if the number is selected,\n"
                "   					0 if not. The items are delimited with spaces\n"
                "   					or commas, and ranges are acceptable, either using\n"
                "   					a \"-\" or \":\", e.g.  3-6 and 3:6 both mean 3,4,5, and 6.\n"
                "   					Only values from 0 to one less than the buffer length\n"
                "   					are used.  Out-of-range values are ignored.\n"
                "   				\n\n"
               ).staticmethod("parse_list");

    scope().attr("FILE_EXT_ADD_IF_NONE") = (int32_t)0;
    scope().attr("FILE_EXT_FORCE") = (int32_t)1;
    scope().attr("STR_CASE_TOLERANT") = (int32_t)0;
    scope().attr("STR_CASE_SENSITIVE") = (int32_t)1;
    scope().attr("ESCAPE_CONVERT") = (int32_t)0;
    scope().attr("ESCAPE_REPLACE") = (int32_t)1;
    scope().attr("STR_FILE_PART_NAME") = (int32_t)0;
    scope().attr("STR_FILE_PART_EXTENSION") = (int32_t)1;
    scope().attr("STR_FILE_PART_DIRECTORY") = (int32_t)2;
    scope().attr("STR_FILE_PART_VOLUME") = (int32_t)3;
    scope().attr("STR_FILE_PART_QUALIFIERS") = (int32_t)4;
    scope().attr("STR_FILE_PART_NAME_EXTENSION") = (int32_t)5;
    scope().attr("STR_FILE_PART_FULLPATH_NO_QUALIFIERS") = (int32_t)6;
    scope().attr("STR_JUSTIFY_LEFT") = (int32_t)0;
    scope().attr("STR_JUSTIFY_CENTER") = (int32_t)1;
    scope().attr("STR_JUSTIFY_RIGHT") = (int32_t)2;
    scope().attr("STR_TRIMRIGHT") = (int32_t)1;
    scope().attr("STR_TRIMLEFT") = (int32_t)2;
    scope().attr("STR_TRIMBOTH") = (int32_t)3;

}
