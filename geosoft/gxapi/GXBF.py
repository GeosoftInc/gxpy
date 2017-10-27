### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
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

    The `GXBF <geosoft.gxapi.GXBF>` class is used to access (or create) Binary files and remove
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
        
        :param size:  New length in bytes
        :type  size:  int

        .. versionadded:: 5.0
        """
        self._wrapper.ch_size(size)
        




    def seek(self, offset, ref):
        """
        Moves file position
        
        :param offset:  Number of bytes from reference point
        :param ref:     `BF_SEEK`
        :type  offset:  int
        :type  ref:     int

        .. versionadded:: 5.0

        **Note:**

        Terminates if attempt to move past the end of
        a read-only file.
        """
        self._wrapper.seek(offset, ref)
        




    def copy(self, b_fw):
        """
        Copy entire contents of a source `GXBF <geosoft.gxapi.GXBF>` to a destination `GXBF <geosoft.gxapi.GXBF>`
        
        :param b_fw:  Destination `GXBF <geosoft.gxapi.GXBF>`
        :type  b_fw:  GXBF

        .. versionadded:: 5.0
        """
        self._wrapper.copy(b_fw._wrapper)
        




    def crc(self, size, crc):
        """
        Compute CRC of a file.
        
        :param size:  Number of bytes to CRC
        :param crc:   CRC start (use `CRC_INIT_VALUE <geosoft.gxapi.CRC_INIT_VALUE>` for new)
        :type  size:  int
        :type  crc:   int

        :returns:     CRC Value
        :rtype:       int

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.crc(size, crc)
        return ret_val



    @classmethod
    def create(cls, file, status):
        """
        Create `GXBF <geosoft.gxapi.GXBF>` object.
        
        :param file:    File name to open ("" is a temporary file)
        :param status:  `BF_OPEN_MODE`
        :type  file:    str
        :type  status:  int

        :returns:       `GXBF <geosoft.gxapi.GXBF>` Object
        :rtype:         GXBF

        .. versionadded:: 5.0

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
        Create `GXBF <geosoft.gxapi.GXBF>` object inside an `GXSBF <geosoft.gxapi.GXSBF>`.
        
        :param sbf:     Storage
        :param file:    File name to open ("" is a temporary file)
        :param status:  `BF_OPEN_MODE`
        :type  sbf:     GXSBF
        :type  file:    str
        :type  status:  int

        :returns:       `GXBF <geosoft.gxapi.GXBF>` Object
        :rtype:         GXBF

        .. versionadded:: 5.0

        **Note:**

        see sbf.gxh
        """
        ret_val = gxapi_cy.WrapBF.create_sbf(GXContext._get_tls_geo(), sbf._wrapper, file.encode(), status)
        return GXBF(ret_val)








    def eof(self):
        """
        Returns 1 if at the end of the file
        

        :returns:    1 if at the end of the file,
                    0 if not at the end of the file
        :rtype:      int

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.eof()
        return ret_val




    def query_write(self):
        """
        Check if you can write to the `GXBF <geosoft.gxapi.GXBF>`.
        

        :returns:    0 - No
                    1 - Yes
        :rtype:      int

        .. versionadded:: 5.1.1
        """
        ret_val = self._wrapper.query_write()
        return ret_val




    def read_binary_string(self, bytes, encoding, data):
        """
        Reads string data from current position in `GXBF <geosoft.gxapi.GXBF>`
        
        :param bytes:     Number of bytes to read
        :param encoding:  `BF_ENCODE`
        :param data:      Data
        :type  bytes:     int
        :type  encoding:  int
        :type  data:      str_ref

        .. versionadded:: 6.3
        """
        data.value = self._wrapper.read_binary_string(bytes, encoding, data.value.encode())
        




    def size(self):
        """
        Returns the file length
        

        :returns:    File size in bytes.
        :rtype:      int

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.size()
        return ret_val




    def tell(self):
        """
        Returns current position of file pointer in bytes
        

        :returns:    Current file pointer location
        :rtype:      int

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.tell()
        return ret_val




    def read_int(self, type, data):
        """
        Reads int data from current position in `GXBF <geosoft.gxapi.GXBF>`
        
        :param type:  `GS_TYPES` and `BF_BYTEORDER`
        :param data:  Data
        :type  type:  int
        :type  data:  int_ref

        .. versionadded:: 5.0

        **Note:**

        If the data source may be in byte order different from that
        required by the reader, you can add the source byte-order
        to the `GXBF <geosoft.gxapi.GXBF>` elelment type.  The byte order will be swapped
        if required.  For example, to write out a real number 3.5
        with Most-Significant_Byte first (Mortorola) convention:
        
        `write_double <geosoft.gxapi.GXBF.write_double>`(hBF,`BF_BYTEORDER_MSB <geosoft.gxapi.BF_BYTEORDER_MSB>`+`GS_REAL <geosoft.gxapi.GS_REAL>`,3.5).
        
        If a byte order is not specified, the source is assumed to be
        in the native byte order of the reading/writing computer.
        """
        data.value = self._wrapper.read_int(type, data.value)
        




    def read_double(self, type, data):
        """
        Reads real data from current position in `GXBF <geosoft.gxapi.GXBF>`
        
        :param type:  `GS_TYPES` and `BF_BYTEORDER`
        :param data:  Data
        :type  type:  int
        :type  data:  float_ref

        .. versionadded:: 5.0

        **Note:**

        If the data source may be in byte order different from that
        required by the reader, you can add the source byte-order
        to the `GXBF <geosoft.gxapi.GXBF>` elelment type.  The byte order will be swapped
        if required.  For example, to write out a real number 3.5
        with Most-Significant_Byte first (Mortorola) convention:
        
        `write_double <geosoft.gxapi.GXBF.write_double>`(hBF,`BF_BYTEORDER_MSB <geosoft.gxapi.BF_BYTEORDER_MSB>`+`GS_REAL <geosoft.gxapi.GS_REAL>`,3.5).
        
        If a byte order is not specified, the source is assumed to be
        in the native byte order of the reading/writing computer.
        """
        data.value = self._wrapper.read_double(type, data.value)
        




    def read_vv(self, type, vv):
        """
        Read data to a `GXVV <geosoft.gxapi.GXVV>` from current position in `GXBF <geosoft.gxapi.GXBF>`
        
        :param type:  `GS_TYPES` and `BF_BYTEORDER`
        :param vv:    `GXVV <geosoft.gxapi.GXVV>` data to read, `GXVV <geosoft.gxapi.GXVV>` length is read
        :type  type:  int
        :type  vv:    GXVV

        .. versionadded:: 5.0

        **Note:**

        If the data source may be in byte order different from that
        required by the reader, you can add the source byte-order
        to the `GXBF <geosoft.gxapi.GXBF>` elelment type.  The byte order will be swapped
        if required.  For example, to write out a real number 3.5
        with Most-Significant_Byte first (Mortorola) convention:
        
        `write_double <geosoft.gxapi.GXBF.write_double>`(hBF,`BF_BYTEORDER_MSB <geosoft.gxapi.BF_BYTEORDER_MSB>`+`GS_REAL <geosoft.gxapi.GS_REAL>`,3.5).
        
        If a byte order is not specified, the source is assumed to be
        in the native byte order of the reading/writing computer.
        """
        self._wrapper.read_vv(type, vv._wrapper)
        




    def set_destroy_status(self, status):
        """
        Set the flag to delete the file on close
        
        :param status:  `BF_CLOSE`
        :type  status:  int

        .. versionadded:: 6.0
        """
        self._wrapper.set_destroy_status(status)
        




    def write_binary_string(self, encoding, data):
        """
        Write a binary string to a `GXBF <geosoft.gxapi.GXBF>`
        
        :param encoding:  `BF_ENCODE`
        :param data:      String to write out
        :type  encoding:  int
        :type  data:      str

        .. versionadded:: 6.3
        """
        self._wrapper.write_binary_string(encoding, data.encode())
        




    def write_data_null(self):
        """
        Writes a null byte (0) to `GXBF <geosoft.gxapi.GXBF>`
        

        .. versionadded:: 5.0
        """
        self._wrapper.write_data_null()
        




    def write_int(self, type, data):
        """
        Writes int to the `GXBF <geosoft.gxapi.GXBF>`
        
        :param type:  `GS_TYPES` and `BF_BYTEORDER`
        :param data:  Data
        :type  type:  int
        :type  data:  int

        .. versionadded:: 5.0

        **Note:**

        See comments on byte order for the Read.. functions if you
        want to enforce a certain byte order.
        
        If a byte order is not specified, the data is written
        in the native byte order of the writing computer.
        """
        self._wrapper.write_int(type, data)
        




    def write_double(self, type, data):
        """
        Writes real to the `GXBF <geosoft.gxapi.GXBF>`
        
        :param type:  `GS_TYPES` and `BF_BYTEORDER`
        :param data:  Data
        :type  type:  int
        :type  data:  float

        .. versionadded:: 5.0

        **Note:**

        See comments on byte order for the Read.. functions if you
        want to enforce a certain byte order.
        
        If a byte order is not specified, the data is written
        in the native byte order of the writing computer.
        """
        self._wrapper.write_double(type, data)
        




    def write_vv(self, type, vv):
        """
        Writes `GXVV <geosoft.gxapi.GXVV>` to the `GXBF <geosoft.gxapi.GXBF>`
        
        :param type:  `GS_TYPES` and `BF_BYTEORDER`
        :param vv:    Data
        :type  type:  int
        :type  vv:    GXVV

        .. versionadded:: 5.0

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