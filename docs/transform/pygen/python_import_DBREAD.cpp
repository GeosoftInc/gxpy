#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXDBREADPtr GXDBREAD_wrap_create(GXDBPtr arg1, GXLSTPtr arg2)
{
    GXDBREADPtr ret = GXDBREAD::create(arg1, arg2);
    return ret;
}
inline GXDBREADPtr GXDBREAD_wrap_create_xy(GXDBPtr arg1, GXLSTPtr arg2)
{
    GXDBREADPtr ret = GXDBREAD::create_xy(arg1, arg2);
    return ret;
}
inline GXDBREADPtr GXDBREAD_wrap_create_xyz(GXDBPtr arg1, GXLSTPtr arg2)
{
    GXDBREADPtr ret = GXDBREAD::create_xyz(arg1, arg2);
    return ret;
}
inline int32_t GXDBREAD_wrap_add_channel(GXDBREADPtr self, int32_t arg1)
{
    int32_t ret = self->add_channel(arg1);
    return ret;
}
inline GXVVPtr GXDBREAD_wrap_get_vv(GXDBREADPtr self, int32_t arg1)
{
    GXVVPtr ret = self->get_vv(arg1);
    return ret;
}
inline GXVAPtr GXDBREAD_wrap_get_va(GXDBREADPtr self, int32_t arg1)
{
    GXVAPtr ret = self->get_va(arg1);
    return ret;
}
inline GXVVPtr GXDBREAD_wrap_get_v_vx(GXDBREADPtr self)
{
    GXVVPtr ret = self->get_v_vx();
    return ret;
}
inline GXVVPtr GXDBREAD_wrap_get_v_vy(GXDBREADPtr self)
{
    GXVVPtr ret = self->get_v_vy();
    return ret;
}
inline GXVVPtr GXDBREAD_wrap_get_v_vz(GXDBREADPtr self)
{
    GXVVPtr ret = self->get_v_vz();
    return ret;
}
inline int32_t GXDBREAD_wrap_get_chan_array_size(GXDBREADPtr self, int32_t arg1)
{
    int32_t ret = self->get_chan_array_size(arg1);
    return ret;
}
inline int32_t GXDBREAD_wrap_get_number_of_blocks_to_process(GXDBREADPtr self)
{
    int32_t ret = self->get_number_of_blocks_to_process();
    return ret;
}
inline int32_t GXDBREAD_wrap_get_next_block(GXDBREADPtr self, int_ref& arg1, int_ref& arg2, int_ref& arg3)
{
    int32_t ret = self->get_next_block(arg1, arg2, arg3);
    return ret;
}

void gxPythonImportGXDBREAD()
{

    class_<GXDBREAD, GXDBREADPtr> pyClass("GXDBREAD",
                                          "\n.. parsed-literal::\n\n"
                                          "   The DBREAD class is used to open and read from databases. Very large lines\n"
                                          "     are split into blocks and served up sequentially to prevent the over-use of virtual memory when channels are read into VVs or VAs.\n"
                                          "     Individual data blocks are limited by default to 1 MB (which is user-alterable). Single lines smaller than the block size\n"
                                          "     are served up whole, one block per line.\n"
                                          "   \n\n"
                                          , no_init);

    pyClass.def("null", &GXDBREAD::null, "null() -> GXDBREAD\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDBREAD`\n\n:returns: A null :class:`geosoft.gxapi.GXDBREAD`\n:rtype: :class:`geosoft.gxapi.GXDBREAD`\n").staticmethod("null");
    pyClass.def("is_null", &GXDBREAD::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDBREAD is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDBREAD`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDBREAD::_internal_handle);
    pyClass.def("create", &GXDBREAD_wrap_create,
                "create((GXDB)arg1, (GXLST)arg2) -> GXDBREAD:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Create a DBREAD object\n"
                "   				 Add channels using the \\ :func:`geosoft.gxapi.GXDBREAD.add_channel`\\ () method.channel.\n"
                "   			 \n\n"

                ":param arg1: Database input\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: list of lines to process NAME = line name, VALUE = line symbol\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: DBREAD object\n"
                ":rtype: :class:`geosoft.gxapi.GXDBREAD`\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_xy", &GXDBREAD_wrap_create_xy,
                "create_xy((GXDB)arg1, (GXLST)arg2) -> GXDBREAD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a DBREAD object for a XY-located data. Add channels using the\n"
                "   		               \\ :func:`geosoft.gxapi.GXDBREAD.add_channel`\\ () method.\n\n"

                ":param arg1: Database input\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: list of lines to process NAME = line name, VALUE = line symbol\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: DBREAD object\n"
                ":rtype: :class:`geosoft.gxapi.GXDBREAD`\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               ).staticmethod("create_xy");
    pyClass.def("create_xyz", &GXDBREAD_wrap_create_xyz,
                "create_xyz((GXDB)arg1, (GXLST)arg2) -> GXDBREAD:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Create a DBREAD object for a XYZ-located data.\n"
                "   				 Add channels using the \\ :func:`geosoft.gxapi.GXDBREAD.add_channel`\\ () method.channel\n\n"

                ":param arg1: Database input\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: list of lines to process NAME = line name, VALUE = line symbol\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: DBREAD object\n"
                ":rtype: :class:`geosoft.gxapi.GXDBREAD`\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               ).staticmethod("create_xyz");
    pyClass.def("add_channel", &GXDBREAD_wrap_add_channel,
                "add_channel((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a data channel to the DBREAD object.\n\n"

                ":param arg1: Channel handle (does not need to be locked, but can be.)\n"
                ":type arg1: int\n"
                ":returns: Channel index. Use for getting the correct VV or VA object.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );
    pyClass.def("get_vv", &GXDBREAD_wrap_get_vv,
                "get_vv((int)arg1) -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the VV handle for a channel.\n\n"

                ":param arg1: Index of channel to access.\n"
                ":type arg1: int\n"
                ":returns: VV handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Call only for single-column (regular) channels. You can call the \\ :func:`geosoft.gxapi.GXDBREAD.get_chan_array_size`\\ \n"
                "   			 function to find the number fo columns in a given channel.\n"
                "   		    The VV is filled anew for each block served up.\n\n"
               );
    pyClass.def("get_va", &GXDBREAD_wrap_get_va,
                "get_va((int)arg1) -> GXVA:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the VA handle for an array channel.\n\n"

                ":param arg1: Index of channel to access.\n"
                ":type arg1: int\n"
                ":returns: VA handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVA`\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Call only for array (multi-column) channels. You can call the \\ :func:`geosoft.gxapi.GXDBREAD.get_chan_array_size`\\ \n"
                "   				 function to find the number fo columns in a given channel, or you can call \\ :func:`geosoft.gxapi.GXVA.col`\\  on the returned VA handle.\n"
                "   				 The VA is filled anew for each block served up.\n"
                "   			 \n\n"
               );
    pyClass.def("get_v_vx", &GXDBREAD_wrap_get_v_vx,
                "get_v_vx() -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the X channel VV handle.\n\n"

                ":returns: VV handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Only available for the CreateXY or CreateXYZ methods.\n"
                "   				 The VV is filled anew for each block served up.\n"
                "   			 \n\n"
               );
    pyClass.def("get_v_vy", &GXDBREAD_wrap_get_v_vy,
                "get_v_vy() -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Y channel VV handle.\n\n"

                ":returns: VV handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Only available for the CreateXY or CreateXYZ methods.\n"
                "   				 The VV is filled anew for each block served up.\n"
                "   			 \n\n"
               );
    pyClass.def("get_v_vz", &GXDBREAD_wrap_get_v_vz,
                "get_v_vz() -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Z channel VV handle.\n\n"

                ":returns: VV handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Only available for the CreateXY or CreateXYZ methods.\n"
                "   				 The VV is filled anew for each block served up.\n"
                "   				 If the Z channel is an array channel, the returned VV is the \"base\" VV of the VA and contains all items sequentially.\n"
                "   			 \n\n"
               );
    pyClass.def("get_chan_array_size", &GXDBREAD_wrap_get_chan_array_size,
                "get_chan_array_size((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of columns of data in a channel.\n\n"

                ":param arg1: Index of channel to access.\n"
                ":type arg1: int\n"
                ":returns: The number of columns (array size) for a channel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Regular channels have one column of data. Array channels have more than one column of data.\n"
                "   				 This function should be called to determine whether to use \\ :func:`geosoft.gxapi.GXDBREAD.get_vv`\\  or \\ :func:`geosoft.gxapi.GXDBREAD.get_va`\\  to access data\n"
                "   				 for a channel.\n"
                "   			 \n\n"
               );
    pyClass.def("get_number_of_blocks_to_process", &GXDBREAD_wrap_get_number_of_blocks_to_process,
                "get_number_of_blocks_to_process() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of blocks to be served up.\n\n"

                ":returns: The number of blocks to process in the selected lines.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				The selected lines are scanned. All lines where the served up data is less than the maximum block size for\n"
                "   				all channels are served as a single block. Any lines where any channel's data exceeds the maximum block size are split up into blocks.\n"
                "   				The value returned can be used as the progress message maximum iteration value.\n"
                "   			 \n\n"
               );
    pyClass.def("get_next_block", &GXDBREAD_wrap_get_next_block,
                "get_next_block((int_ref)arg1, (int_ref)arg2, (int_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the next block of data.\n\n"

                ":param arg1: (returned) The index into the input selected line list of the line whose data is contained in the current block\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: (returned) The block index (0 to NBlocks-1) for the current line of data.\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: (returned) The number of blocks that the current line is split into.\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Returns the current block index, or -1 if at end of file (no new data returned).\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				  The next block of data is read and copied into the channel VV and/or VA objects, accessed using\n"
                "   				  the \\ :func:`geosoft.gxapi.GXDBREAD.get_vv`\\  and \\ :func:`geosoft.gxapi.GXDBREAD.get_va`\\  functions.\n"
                "   			  \n\n"
               );


}
