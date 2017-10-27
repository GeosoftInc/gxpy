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
class GXBF:
    """
    GXBF class.

    The `GXBF` class is used to access (or create) Binary files and remove
    (or destroy) files from use. You can also perform a variety of
    additional tasks, such as positioning within files, reading from
    files and writing to files.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapBF(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXBF`
        
        :returns: A null `GXBF`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXBF` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXBF`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def ch_size(self, size):
        """
        Changes the size of a file
        """
        self._wrapper.ch_size(size)
        




    def seek(self, offset, ref):
        """
        Moves file position

        **Note:**

        Terminates if attempt to move past the end of
        a read-only file.
        """
        self._wrapper.seek(offset, ref)
        




    def copy(self, b_fw):
        """
        Copy entire contents of a source `GXBF` to a destination `GXBF`
        """
        self._wrapper.copy(b_fw._wrapper)
        




    def crc(self, size, crc):
        """
        Compute CRC of a file.
        """
        ret_val = self._wrapper.crc(size, crc)
        return ret_val



    @classmethod
    def create(cls, file, status):
        """
        Create `GXBF` object.

        **Note:**

        Run-time specific directory paths may be added the the front of file names
        as follows:
        
        <geosoft>      the main Geosoft installation directory
        <geosoft2>     the secondary Geosoft installation directory
        <geotemp>      the Geosoft temporary file directory
        <windows>      the operating system Windows directory
        <system>       the operating system system directory
        <other>        other environment variables
        
        For example "<geosoft>/user/csv/datum.csv"
        """
        ret_val = gxapi_cy.WrapBF.create(GXContext._get_tls_geo(), file.encode(), status)
        return GXBF(ret_val)



    @classmethod
    def create_sbf(cls, sbf, file, status):
        """
        Create `GXBF` object inside an `GXSBF`.

        **Note:**

        see sbf.gxh
        """
        ret_val = gxapi_cy.WrapBF.create_sbf(GXContext._get_tls_geo(), sbf._wrapper, file.encode(), status)
        return GXBF(ret_val)








    def eof(self):
        """
        Returns 1 if at the end of the file
        """
        ret_val = self._wrapper.eof()
        return ret_val




    def query_write(self):
        """
        Check if you can write to the `GXBF`.
        """
        ret_val = self._wrapper.query_write()
        return ret_val




    def read_binary_string(self, bytes, encoding, data):
        """
        Reads string data from current position in `GXBF`
        """
        data.value = self._wrapper.read_binary_string(bytes, encoding, data.value.encode())
        




    def size(self):
        """
        Returns the file length
        """
        ret_val = self._wrapper.size()
        return ret_val




    def tell(self):
        """
        Returns current position of file pointer in bytes
        """
        ret_val = self._wrapper.tell()
        return ret_val




    def read_int(self, type, data):
        """
        Reads int data from current position in `GXBF`

        **Note:**

        If the data source may be in byte order different from that
        required by the reader, you can add the source byte-order
        to the `GXBF` elelment type.  The byte order will be swapped
        if required.  For example, to write out a real number 3.5
        with Most-Significant_Byte first (Mortorola) convention:
        
        `write_double`(hBF,`BF_BYTEORDER_MSB`+`GS_REAL`,3.5).
        
        If a byte order is not specified, the source is assumed to be
        in the native byte order of the reading/writing computer.
        """
        data.value = self._wrapper.read_int(type, data.value)
        




    def read_double(self, type, data):
        """
        Reads real data from current position in `GXBF`

        **Note:**

        If the data source may be in byte order different from that
        required by the reader, you can add the source byte-order
        to the `GXBF` elelment type.  The byte order will be swapped
        if required.  For example, to write out a real number 3.5
        with Most-Significant_Byte first (Mortorola) convention:
        
        `write_double`(hBF,`BF_BYTEORDER_MSB`+`GS_REAL`,3.5).
        
        If a byte order is not specified, the source is assumed to be
        in the native byte order of the reading/writing computer.
        """
        data.value = self._wrapper.read_double(type, data.value)
        




    def read_vv(self, type, vv):
        """
        Read data to a `GXVV` from current position in `GXBF`

        **Note:**

        If the data source may be in byte order different from that
        required by the reader, you can add the source byte-order
        to the `GXBF` elelment type.  The byte order will be swapped
        if required.  For example, to write out a real number 3.5
        with Most-Significant_Byte first (Mortorola) convention:
        
        `write_double`(hBF,`BF_BYTEORDER_MSB`+`GS_REAL`,3.5).
        
        If a byte order is not specified, the source is assumed to be
        in the native byte order of the reading/writing computer.
        """
        self._wrapper.read_vv(type, vv._wrapper)
        




    def set_destroy_status(self, status):
        """
        Set the flag to delete the file on close
        """
        self._wrapper.set_destroy_status(status)
        




    def write_binary_string(self, encoding, data):
        """
        Write a binary string to a `GXBF`
        """
        self._wrapper.write_binary_string(encoding, data.encode())
        




    def write_data_null(self):
        """
        Writes a null byte (0) to `GXBF`
        """
        self._wrapper.write_data_null()
        




    def write_int(self, type, data):
        """
        Writes int to the `GXBF`

        **Note:**

        See comments on byte order for the Read.. functions if you
        want to enforce a certain byte order.
        
        If a byte order is not specified, the data is written
        in the native byte order of the writing computer.
        """
        self._wrapper.write_int(type, data)
        




    def write_double(self, type, data):
        """
        Writes real to the `GXBF`

        **Note:**

        See comments on byte order for the Read.. functions if you
        want to enforce a certain byte order.
        
        If a byte order is not specified, the data is written
        in the native byte order of the writing computer.
        """
        self._wrapper.write_double(type, data)
        




    def write_vv(self, type, vv):
        """
        Writes `GXVV` to the `GXBF`

        **Note:**

        See comments on byte order for the Read.. functions if you
        want to enforce a certain byte order.
        
        If a byte order is not specified, the data is written
        in the native byte order of the writing computer.
        """
        self._wrapper.write_vv(type, vv._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer