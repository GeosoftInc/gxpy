#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes

class GXGEOSOFT {};



void gxPythonImportGXGEOSOFT()
{

    scope().attr("CRC_INIT_VALUE") = (uint32_t)4294967295;
    scope().attr("DATE_FORMAT_YYYYMMDD") = (int32_t)1;
    scope().attr("DATE_FORMAT_DDMMYYYY") = (int32_t)2;
    scope().attr("DATE_FORMAT_MMDDYYYY") = (int32_t)3;
    scope().attr("iDUMMY") = (int32_t)-2147483647;
    scope().attr("rDUMMY") = (double)-1.0E32;
    scope().attr("GS_S1MX") = (int8_t)127;
    scope().attr("GS_S1MN") = (int8_t)-126;
    scope().attr("GS_S1DM") = (int8_t)-127;
    scope().attr("GS_U1MX") = (uint8_t)254U;
    scope().attr("GS_U1MN") = (uint8_t)0U;
    scope().attr("GS_U1DM") = (uint8_t)255U;
    scope().attr("GS_S2MX") = (int16_t)32767;
    scope().attr("GS_S2MN") = (int16_t)-32766;
    scope().attr("GS_S2DM") = (int16_t)-32767;
    scope().attr("GS_U2MX") = (uint32_t)65534U;
    scope().attr("GS_U2MN") = (uint32_t)0U;
    scope().attr("GS_U2DM") = (uint32_t)65535U;
    scope().attr("GS_S4MX") = (int32_t)2147483647L;
    scope().attr("GS_S4MN") = (int32_t)-2147483646L;
    scope().attr("GS_S4DM") = (int32_t)-2147483647L;
    scope().attr("GS_U4MX") = (uint32_t)0xFFFFFFFE;
    scope().attr("GS_U4MN") = (uint32_t)0x00000000;
    scope().attr("GS_U4DM") = (uint32_t)0xFFFFFFFF;
    scope().attr("GS_S8MX") = (int64_t)0x7FFFFFFFFFFFFFFF;
    scope().attr("GS_S8MN") = (int64_t)0x8000000000000001;
    scope().attr("GS_S8DM") = (int64_t)0x8000000000000000;
    scope().attr("GS_U8MX") = (uint64_t)0xFFFFFFFFFFFFFFFE;
    scope().attr("GS_U8MN") = (uint64_t)0x0000000000000000;
    scope().attr("GS_U8DM") = (uint64_t)0xFFFFFFFFFFFFFFFF;
    scope().attr("GS_R4MX") = (float)1.0E32f;
    scope().attr("GS_R4MN") = (float)-0.9E32f;
    scope().attr("GS_R4DM") = (float)-1.0E32f;
    scope().attr("GS_R8MX") = (double)1.0E32;
    scope().attr("GS_R8MN") = (double)-0.9E+32;
    scope().attr("GS_R8DM") = (double)-1.0E+32;
    scope().attr("GS_R4EPSILON") = (float)1.0E-32f;
    scope().attr("GS_R8EPSILON") = (double)1.0E-32;
    scope().attr("iMIN") = (int32_t)-2147483646;
    scope().attr("iMAX") = (int32_t)2147483647;
    scope().attr("rMIN") = (double)-0.9E32;
    scope().attr("rMAX") = (double)1.0E32;
    scope().attr("STR_DEFAULT") = (int32_t)128;
    scope().attr("STR_DEFAULT_SHORT") = (int32_t)64;
    scope().attr("STR_DEFAULT_LONG") = (int32_t)1024;
    scope().attr("STR_ERROR") = (int32_t)2048;
    scope().attr("STR_VERY_LONG") = (int32_t)16384;
    scope().attr("STR_VIEW") = (int32_t)2080;
    scope().attr("STR_GROUP") = (int32_t)1040;
    scope().attr("STR_VIEW_GROUP") = (int32_t)2080;
    scope().attr("STR_FILE") = (int32_t)1040;
    scope().attr("STR_MULTI_FILE") = (int32_t)16384;
    scope().attr("STR_DB_SYMBOL") = (int32_t)64;
    scope().attr("STR_GXF") = (int32_t)160;
    scope().attr("STR_MAX_PATH") = (int32_t)1040;
    scope().attr("STR_MULTI_PATH") = (int32_t)16384;
    scope().attr("GS_MAX_PATH") = (int32_t)1040;
    scope().attr("GS_MULTI_PATH") = (int32_t)16384;
    scope().attr("GS_INT") = (int32_t)0;
    scope().attr("GS_REAL") = (int32_t)1;
    scope().attr("FORMAT_DECIMAL") = (int32_t)0;
    scope().attr("FORMAT_SIG_DIG") = (int32_t)5;
    scope().attr("FORMAT_EXP") = (int32_t)1;
    scope().attr("FORMAT_TIME_COLON") = (int32_t)2;
    scope().attr("FORMAT_TIME_HMS") = (int32_t)8;
    scope().attr("FORMAT_TIME_HHMMSS") = (int32_t)9;
    scope().attr("FORMAT_DATE_YYYYMMDD") = (int32_t)3;
    scope().attr("FORMAT_DATE_DDMMYYYY") = (int32_t)6;
    scope().attr("FORMAT_DATE_MMDDYYYY") = (int32_t)7;
    scope().attr("FORMAT_GEOGRAPHIC") = (int32_t)4;
    scope().attr("FORMAT_GEOGRAPHIC_1") = (int32_t)10;
    scope().attr("FORMAT_GEOGRAPHIC_2") = (int32_t)11;
    scope().attr("FORMAT_GEOGRAPHIC_3") = (int32_t)12;
    scope().attr("GS_BYTE") = (int32_t)0;
    scope().attr("GS_USHORT") = (int32_t)1;
    scope().attr("GS_SHORT") = (int32_t)2;
    scope().attr("GS_LONG") = (int32_t)3;
    scope().attr("GS_FLOAT") = (int32_t)4;
    scope().attr("GS_DOUBLE") = (int32_t)5;
    scope().attr("GS_UBYTE") = (int32_t)6;
    scope().attr("GS_ULONG") = (int32_t)7;
    scope().attr("GS_LONG64") = (int32_t)8;
    scope().attr("GS_ULONG64") = (int32_t)9;
    scope().attr("GS_FLOAT3D") = (int32_t)10;
    scope().attr("GS_MAXTYPE") = (int32_t)10;
    scope().attr("GS_TYPE_DEFAULT") = (int32_t)-32767;
    scope().attr("SYS_CRYPT_LICENSE_KEY") = "{***LICENSE_KEY***}";
    scope().attr("SYS_CRYPT_COMPUTER_ID") = "{***COMPUTER_ID***}";
    scope().attr("SYS_CRYPT_GLOBAL_ID") = "{***GLOBAL_COMPUTER_ID***}";
    scope().attr("TIME_FORMAT_COLON") = (int32_t)1;
    scope().attr("TIME_FORMAT_HMS") = (int32_t)2;

}
