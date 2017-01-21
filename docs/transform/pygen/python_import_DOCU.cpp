#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXDOCU_wrap_copy(GXDOCUPtr self, GXDOCUPtr arg1)
{
    self->copy(arg1);
}
inline GXDOCUPtr GXDOCU_wrap_create()
{
    GXDOCUPtr ret = GXDOCU::create();
    return ret;
}
inline GXDOCUPtr GXDOCU_wrap_create_s(GXBFPtr arg1)
{
    GXDOCUPtr ret = GXDOCU::create_s(arg1);
    return ret;
}
inline void GXDOCU_wrap_get_file(GXDOCUPtr self, const gx_string_type& arg1)
{
    self->get_file(arg1);
}
inline void GXDOCU_wrap_get_file_meta(GXDOCUPtr self, const gx_string_type& arg1)
{
    self->get_file_meta(arg1);
}
inline void GXDOCU_wrap_get_meta(GXDOCUPtr self, GXMETAPtr arg1)
{
    self->get_meta(arg1);
}
inline void GXDOCU_wrap_doc_name(GXDOCUPtr self, str_ref& arg1)
{
    self->doc_name(arg1);
}
inline void GXDOCU_wrap_file_name(GXDOCUPtr self, str_ref& arg1)
{
    self->file_name(arg1);
}
inline bool GXDOCU_wrap_have_meta(GXDOCUPtr self)
{
    bool ret = self->have_meta();
    return ret;
}
inline int32_t GXDOCU_wrap_is_reference(GXDOCUPtr self)
{
    int32_t ret = self->is_reference();
    return ret;
}
inline void GXDOCU_wrap_open(GXDOCUPtr self, int32_t arg1)
{
    self->open((DOCU_OPEN)arg1);
}
inline void GXDOCU_wrap_serial(GXDOCUPtr self, GXBFPtr arg1)
{
    self->serial(arg1);
}
inline void GXDOCU_wrap_set_file(GXDOCUPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->set_file(arg1, arg2, arg3);
}
inline void GXDOCU_wrap_set_file_meta(GXDOCUPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->set_file_meta(arg1, arg2, arg3);
}
inline void GXDOCU_wrap_set_meta(GXDOCUPtr self, GXMETAPtr arg1)
{
    self->set_meta(arg1);
}

void gxPythonImportGXDOCU()
{

    class_<GXDOCU, GXDOCUPtr> pyClass("GXDOCU",
                                      "\n.. parsed-literal::\n\n"
                                      "   Class to work with documents\n\n"
                                      , no_init);

    pyClass.def("null", &GXDOCU::null, "null() -> GXDOCU\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDOCU`\n\n:returns: A null :class:`geosoft.gxapi.GXDOCU`\n:rtype: :class:`geosoft.gxapi.GXDOCU`\n").staticmethod("null");
    pyClass.def("is_null", &GXDOCU::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDOCU is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDOCU`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDOCU::_internal_handle);
    pyClass.def("copy", &GXDOCU_wrap_copy,
                "copy((GXDOCU)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy DOCU\n\n"

                ":param arg1: source DOCU\n"
                ":type arg1: :class:`geosoft.gxapi.GXDOCU`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("create", &GXDOCU_wrap_create,
                "create() -> GXDOCU:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a document onject\n\n"

                ":returns: DOCU Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDOCU`\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               ).staticmethod("create");
    pyClass.def("create_s", &GXDOCU_wrap_create_s,
                "create_s((GXBF)arg1) -> GXDOCU:\n"

                "\n.. parsed-literal::\n\n"
                "   Create from a serialized source\n\n"

                ":param arg1: BF from which to read DOCU\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: DOCU Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDOCU`\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               ).staticmethod("create_s");
    pyClass.def("get_file", &GXDOCU_wrap_get_file,
                "get_file((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the document and place in a file.\n\n"

                ":param arg1: file to which to write document\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("get_file_meta", &GXDOCU_wrap_get_file_meta,
                "get_file_meta((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the document and place in a file with metadata.\n\n"

                ":param arg1: file to which to write document\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If this document is only a URL link, the URL link will\n"
                "   be resolved and the document downloaded from the appropriate\n"
                "   server using the protocol specified.\n"
                "   \n"
                "   The document has metadata, and the native document does not\n"
                "   support metadata, the metadata will be placed in an associated\n"
                "   file \"filename.extension.GeosoftMeta\"\n\n"
               );
    pyClass.def("get_meta", &GXDOCU_wrap_get_meta,
                "get_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the document's meta\n\n"

                ":param arg1: META object to fill in with the document's meta\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("doc_name", &GXDOCU_wrap_doc_name,
                "doc_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   The document name.\n\n"

                ":param arg1: buffer to fill with document name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("file_name", &GXDOCU_wrap_file_name,
                "file_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   The original document file name.\n\n"

                ":param arg1: buffer to fill with document file name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("have_meta", &GXDOCU_wrap_have_meta,
                "have_meta() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Do you have meta data?\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("is_reference", &GXDOCU_wrap_is_reference,
                "is_reference() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is the document only a reference (a URL) ?\n\n"

                ":returns: 1 - Yes, 0 - No\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("open", &GXDOCU_wrap_open,
                "open((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Open a document in the document viewer\n\n"

                ":param arg1: \\ :ref:`DOCU_OPEN`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   On Windows, the default application for the file extension is\n"
                "   used to open the file.\n\n"
               );
    pyClass.def("serial", &GXDOCU_wrap_serial,
                "serial((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize DOCU\n\n"

                ":param arg1: BF in which to write object\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("set_file", &GXDOCU_wrap_set_file,
                "set_file((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the document from a file source.\n\n"

                ":param arg1: document type\n"
                ":type arg1: str\n"
                ":param arg2: document name, if \"\" file name will be used\n"
                ":type arg2: str\n"
                ":param arg3: document file, must exist\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Document types are normally identified by their extension.  If you\n"
                "   leave the document type blank, the extension of the document file\n"
                "   will be used as the document type.\n"
                "   \n"
                "   To resolve conflicting types, you can define your own unique type\n"
                "   by entering your own type \"extension\" string.\n"
                "   \n"
                "   The following types are pre-defined (as are any normal Geosoft\n"
                "   file types):\n"
                "   \n"
                "      \"htm\"       HTML\n"
                "      \"html\"      HTML\n"
                "      \"txt\"       ASCII text file\n"
                "      \"doc\"       Word for Windows document\n"
                "      \"pdf\"       Adobe PDF\n"
                "      \"map\"       Geosoft map file\n"
                "      \"mmap\"      Mapinfo map file (real extension \"map\")\n"
                "      \"grd\"       Geosoft grid file\n"
                "      \"gdb\"       Geosoft database\n"
                "   \n"
                "   URL Document Links\n"
                "   \n"
                "   The document name can be a URL link to the document using one of\n"
                "   the supported protocols. The following protocols are supported:\n"
                "   \n"
                "      http://www.mywebserver.com/MyFile.doc                 - HTTP\n"
                "      dap://my.dap.server.com/dcs?DatasetName?MyFile.doc    - DAP (DAP Document Access)\n"
                "      ftp://my.ftp.server.com/Dir1/MyFile.doc               - FTP protocol\n"
                "   \n"
                "   The full file name will be stored but no data will be stored with\n"
                "   the DOCU class and the document can be retrieved using the sGetFile_DOCU\n"
                "   method.\n\n"
               );
    pyClass.def("set_file_meta", &GXDOCU_wrap_set_file_meta,
                "set_file_meta((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the document from a file source with metadata.\n\n"

                ":param arg1: document type extension\n"
                ":type arg1: str\n"
                ":param arg2: document name, if NULL use file name\n"
                ":type arg2: str\n"
                ":param arg3: document file or URL\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXDOCU.set_file`\\ .\n"
                "   This function is the same as sSetFile_DOCU, plus insures that a\n"
                "   META exists that includes the \"Data\" class.  If the file has\n"
                "   associated metadata, either supported natively in the file, or\n"
                "   through an associated file \"filename.extension.GeosoftMeta\",\n"
                "   that metadata will be loaded into the DOCU meta, and a Data\n"
                "   class will be constructed if one does not exist.\n"
                "   \n"
                "   Also, the Document type Extension is very important in that it\n"
                "   specifies the document types that natively have metadata. The\n"
                "   ones currently supported are:\n"
                "   \n"
                "      \"map\"       Geosoft map file\n"
                "      \"gdb\"       Geosoft database\n"
                "      \"grd\"       Geosoft grid file\n\n"
               );
    pyClass.def("set_meta", &GXDOCU_wrap_set_meta,
                "set_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the document's meta\n\n"

                ":param arg1: META to add to the document's meta\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );

    scope().attr("DOCU_OPEN_VIEW") = (int32_t)0;
    scope().attr("DOCU_OPEN_EDIT") = (int32_t)1;

}
