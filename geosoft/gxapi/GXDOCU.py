### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDOCU:
    """
    GXDOCU class.

    Class to work with documents
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDOCU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXDOCU`
        
        :returns: A null :class:`geosoft.gxapi.GXDOCU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXDOCU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXDOCU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def copy(self, p2):
        """
        Copy :class:`geosoft.gxapi.GXDOCU`
        """
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls):
        """
        Create a document onject
        """
        ret_val = gxapi_cy.WrapDOCU.create(GXContext._get_tls_geo())
        return GXDOCU(ret_val)



    @classmethod
    def create_s(cls, p1):
        """
        Create from a serialized source
        """
        ret_val = gxapi_cy.WrapDOCU.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXDOCU(ret_val)






    def get_file(self, p2):
        """
        Get the document and place in a file.
        """
        self._wrapper.get_file(p2.encode())
        




    def get_file_meta(self, p2):
        """
        Get the document and place in a file with metadata.

        **Note:**

        If this document is only a URL link, the URL link will
        be resolved and the document downloaded from the appropriate
        server using the protocol specified.
        
        The document has metadata, and the native document does not
        support metadata, the metadata will be placed in an associated
        file "filename.extension.GeosoftMeta"
        """
        self._wrapper.get_file_meta(p2.encode())
        




    def get_meta(self, p2):
        """
        Get the document's meta
        """
        self._wrapper.get_meta(p2._wrapper)
        




    def doc_name(self, p2):
        """
        The document name.
        """
        p2.value = self._wrapper.doc_name(p2.value.encode())
        




    def file_name(self, p2):
        """
        The original document file name.
        """
        p2.value = self._wrapper.file_name(p2.value.encode())
        




    def have_meta(self):
        """
        Do you have metadata?
        """
        ret_val = self._wrapper.have_meta()
        return ret_val




    def is_reference(self):
        """
        Is the document only a reference (a URL) ?
        """
        ret_val = self._wrapper.is_reference()
        return ret_val




    def open(self, p2):
        """
        Open a document in the document viewer

        **Note:**

        On Windows, the default application for the file extension is
        used to open the file.
        """
        self._wrapper.open(p2)
        




    def serial(self, p2):
        """
        Serialize :class:`geosoft.gxapi.GXDOCU`
        """
        self._wrapper.serial(p2._wrapper)
        




    def set_file(self, p2, p3, p4):
        """
        Set the document from a file source.

        **Note:**

        Document types are normally identified by their extension.  If you
        leave the document type blank, the extension of the document file
        will be used as the document type.
        
        To resolve conflicting types, you can define your own unique type
        by entering your own type "extension" string.
        
        The following types are pre-defined (as are any normal Geosoft
        file types):
        
           "htm"       HTML
           "html"      HTML
           "txt"       ASCII text file
           "doc"       Word for Windows document
           "pdf"       Adobe PDF
           "map"       Geosoft map file
           "mmap"      Mapinfo map file (real extension "map")
           "grd"       Geosoft grid file
           "gdb"       Geosoft database
        
        URL Document Links
        
        The document name can be a URL link to the document using one of
        the supported protocols. The following protocols are supported:
        
           http://www.mywebserver.com/MyFile.doc                 - :class:`geosoft.gxapi.GXHTTP`
           dap://my.dap.server.com/dcs?DatasetName?MyFile.doc    - DAP (DAP Document Access)
           ftp://my.ftp.server.com/Dir1/MyFile.doc               - FTP protocol
        
        The full file name will be stored but no data will be stored with
        the :class:`geosoft.gxapi.GXDOCU` class and the document can be retrieved using the sGetFile_DOCU
        method.
        """
        self._wrapper.set_file(p2.encode(), p3.encode(), p4.encode())
        




    def set_file_meta(self, p2, p3, p4):
        """
        Set the document from a file source with metadata.

        **Note:**

        See SetFile_DOCU.
        This function is the same as sSetFile_DOCU, plus insures that a
        :class:`geosoft.gxapi.GXMETA` exists that includes the "Data" class.  If the file has
        associated metadata, either supported natively in the file, or
        through an associated file "filename.extension.GeosoftMeta",
        that metadata will be loaded into the :class:`geosoft.gxapi.GXDOCU` meta, and a Data
        class will be constructed if one does not exist.
        
        Also, the Document type Extension is very important in that it
        specifies the document types that natively have metadata. The
        ones currently supported are:
        
           "map"       Geosoft map file
           "gdb"       Geosoft database
           "grd"       Geosoft grid file
        """
        self._wrapper.set_file_meta(p2.encode(), p3.encode(), p4.encode())
        




    def set_meta(self, p2):
        """
        Set the document's meta
        """
        self._wrapper.set_meta(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer