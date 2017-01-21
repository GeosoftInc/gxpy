#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXDBWRITEPtr GXDBWRITE_wrap_create(GXDBPtr arg1)
{
    GXDBWRITEPtr ret = GXDBWRITE::create(arg1);
    return ret;
}
inline GXDBWRITEPtr GXDBWRITE_wrap_create_xy(GXDBPtr arg1)
{
    GXDBWRITEPtr ret = GXDBWRITE::create_xy(arg1);
    return ret;
}
inline GXDBWRITEPtr GXDBWRITE_wrap_create_xyz(GXDBPtr arg1)
{
    GXDBWRITEPtr ret = GXDBWRITE::create_xyz(arg1);
    return ret;
}
inline int32_t GXDBWRITE_wrap_add_channel(GXDBWRITEPtr self, int32_t arg1)
{
    int32_t ret = self->add_channel(arg1);
    return ret;
}
inline GXDBPtr GXDBWRITE_wrap_get_db(GXDBWRITEPtr self)
{
    GXDBPtr ret = self->get_db();
    return ret;
}
inline GXVVPtr GXDBWRITE_wrap_get_vv(GXDBWRITEPtr self, int32_t arg1)
{
    GXVVPtr ret = self->get_vv(arg1);
    return ret;
}
inline GXVAPtr GXDBWRITE_wrap_get_va(GXDBWRITEPtr self, int32_t arg1)
{
    GXVAPtr ret = self->get_va(arg1);
    return ret;
}
inline GXVVPtr GXDBWRITE_wrap_get_v_vx(GXDBWRITEPtr self)
{
    GXVVPtr ret = self->get_v_vx();
    return ret;
}
inline GXVVPtr GXDBWRITE_wrap_get_v_vy(GXDBWRITEPtr self)
{
    GXVVPtr ret = self->get_v_vy();
    return ret;
}
inline GXVVPtr GXDBWRITE_wrap_get_v_vz(GXDBWRITEPtr self)
{
    GXVVPtr ret = self->get_v_vz();
    return ret;
}
inline int32_t GXDBWRITE_wrap_get_chan_array_size(GXDBWRITEPtr self, int32_t arg1)
{
    int32_t ret = self->get_chan_array_size(arg1);
    return ret;
}
inline void GXDBWRITE_wrap_add_block(GXDBWRITEPtr self, int32_t arg1)
{
    self->add_block(arg1);
}
inline void GXDBWRITE_wrap_commit(GXDBWRITEPtr self)
{
    self->commit();
}
inline void GXDBWRITE_wrap_test_func(GXDBWRITEPtr self, GXRAPtr arg1)
{
    self->test_func(arg1);
}

void gxPythonImportGXDBWRITE()
{

    class_<GXDBWRITE, GXDBWRITEPtr> pyClass("GXDBWRITE",
                                            "\n.. parsed-literal::\n\n"
                                            "   The DBWRITE class is used to open and write to databases. Large blocks of data\n"
                                            "     are split into blocks and served up sequentially to prevent the over-use of virtual memory when VVs or VAs are being written to channels.\n"
                                            "     Individual data blocks are limited by default to 1 MB (which is user-alterable). Data less than the block size\n"
                                            "     are served up whole, one block per line.\n"
                                            "   \n\n"
                                            , no_init);

    pyClass.def("null", &GXDBWRITE::null, "null() -> GXDBWRITE\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDBWRITE`\n\n:returns: A null :class:`geosoft.gxapi.GXDBWRITE`\n:rtype: :class:`geosoft.gxapi.GXDBWRITE`\n").staticmethod("null");
    pyClass.def("is_null", &GXDBWRITE::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDBWRITE is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDBWRITE`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDBWRITE::_internal_handle);
    pyClass.def("create", &GXDBWRITE_wrap_create,
                "create((GXDB)arg1) -> GXDBWRITE:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Create a DBWRITE object\n"
                "   				 Add channels using the \\ :func:`geosoft.gxapi.GXDBWRITE.add_channel`\\ () method.channel.\n"
                "   			 \n\n"

                ":param arg1: Database input\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: DBWRITE object\n"
                ":rtype: :class:`geosoft.gxapi.GXDBWRITE`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_xy", &GXDBWRITE_wrap_create_xy,
                "create_xy((GXDB)arg1) -> GXDBWRITE:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a DBWRITE object for a XY-located data. Add channels using the\n"
                "   		               \\ :func:`geosoft.gxapi.GXDBWRITE.add_channel`\\ () method.\n\n"

                ":param arg1: Database input\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: DBWRITE object\n"
                ":rtype: :class:`geosoft.gxapi.GXDBWRITE`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("create_xy");
    pyClass.def("create_xyz", &GXDBWRITE_wrap_create_xyz,
                "create_xyz((GXDB)arg1) -> GXDBWRITE:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Create a DBWRITE object for a XYZ-located data.\n"
                "   				 Add channels using the \\ :func:`geosoft.gxapi.GXDBWRITE.add_channel`\\ () method.channel\n\n"

                ":param arg1: Database input\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: DBWRITE object\n"
                ":rtype: :class:`geosoft.gxapi.GXDBWRITE`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("create_xyz");
    pyClass.def("add_channel", &GXDBWRITE_wrap_add_channel,
                "add_channel((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a data channel to the DBWRITE object.\n\n"

                ":param arg1: Channel handle (does not need to be locked, but can be.)\n"
                ":type arg1: int\n"
                ":returns: Channel index. Use for getting the correct VV or VA object.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("get_db", &GXDBWRITE_wrap_get_db,
                "get_db() -> GXDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the output DB handle from the DBWRITE object.\n\n"

                ":returns: DB handle\n"
                ":rtype: :class:`geosoft.gxapi.GXDB`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("get_vv", &GXDBWRITE_wrap_get_vv,
                "get_vv((int)arg1) -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the VV handle for a channel.\n\n"

                ":param arg1: Index of channel to access.\n"
                ":type arg1: int\n"
                ":returns: VV handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Call only for single-column (regular) channels. You can call the \\ :func:`geosoft.gxapi.GXDBWRITE.get_chan_array_size`\\ \n"
                "   			 function to find the number fo columns in a given channel.\n"
                "   		    The VV is filled anew for each block served up.\n\n"
               );
    pyClass.def("get_va", &GXDBWRITE_wrap_get_va,
                "get_va((int)arg1) -> GXVA:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the VA handle for an array channel.\n\n"

                ":param arg1: Index of channel to access.\n"
                ":type arg1: int\n"
                ":returns: VA handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVA`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Call only for array (multi-column) channels. You can call the \\ :func:`geosoft.gxapi.GXDBWRITE.get_chan_array_size`\\ \n"
                "   				 function to find the number fo columns in a given channel, or you can call \\ :func:`geosoft.gxapi.GXVA.col`\\  on the returned VA handle.\n"
                "   				 The VA is filled anew for each block served up.\n"
                "   			 \n\n"
               );
    pyClass.def("get_v_vx", &GXDBWRITE_wrap_get_v_vx,
                "get_v_vx() -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the X channel VV handle.\n\n"

                ":returns: VV handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Only available for the CreateXY or CreateXYZ methods.\n"
                "   				 The VV is filled anew for each block served up.\n"
                "   			 \n\n"
               );
    pyClass.def("get_v_vy", &GXDBWRITE_wrap_get_v_vy,
                "get_v_vy() -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Y channel VV handle.\n\n"

                ":returns: VV handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Only available for the CreateXY or CreateXYZ methods.\n"
                "   				 The VV is filled anew for each block served up.\n"
                "   			 \n\n"
               );
    pyClass.def("get_v_vz", &GXDBWRITE_wrap_get_v_vz,
                "get_v_vz() -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Z channel VV handle.\n\n"

                ":returns: VV handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Only available for the CreateXY or CreateXYZ methods.\n"
                "   				 The VV is filled anew for each block served up.\n"
                "   				 If the Z channel is an array channel, the returned VV is the \"base\" VV of the VA and contains all items sequentially.\n"
                "   			 \n\n"
               );
    pyClass.def("get_chan_array_size", &GXDBWRITE_wrap_get_chan_array_size,
                "get_chan_array_size((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of columns of data in a channel.\n\n"

                ":param arg1: Index of channel to access.\n"
                ":type arg1: int\n"
                ":returns: The number of columns (array size) for a channel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Regular channels have one column of data. Array channels have more than one column of data.\n"
                "   				 This function should be called to determine whether to use \\ :func:`geosoft.gxapi.GXDBWRITE.get_vv`\\  or \\ :func:`geosoft.gxapi.GXDBWRITE.get_va`\\  to access data\n"
                "   				 for a channel.\n"
                "   			 \n\n"
               );
    pyClass.def("add_block", &GXDBWRITE_wrap_add_block,
                "add_block((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add the current block of data.\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":returns: nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				  First, set up the data for each channel by copying values into the individual channel VVs and VAs.\n"
                "   			  \n\n"
               );
    pyClass.def("commit", &GXDBWRITE_wrap_commit,
                "commit() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Commit remaining data to the database.\n\n"

                ":returns: nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   			  \n\n"
               );
    pyClass.def("test_func", &GXDBWRITE_wrap_test_func,
                "test_func((GXRA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Temporary test function.\n\n"

                ":param arg1: RA handle to text file to import.\n"
                ":type arg1: :class:`geosoft.gxapi.GXRA`\n"
                ":returns: nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				  Designed to import the \"Massive.xyz\" file, which has data in the format \"X Y Z Data\".				  \n"
                "   			  \n\n"
               );


}
