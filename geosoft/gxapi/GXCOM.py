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
class GXCOM:
    """
    GXCOM class.

    This class is used to communicate with external serial devices. It allows the setting of timeouts.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapCOM(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXCOM`
        
        :returns: A null `GXCOM`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXCOM` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXCOM`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, port, baud, data_size, parity, stop_bits, flow_control, time_out):
        """
        Create `GXCOM <geosoft.gxapi.GXCOM>` object.
        """
        ret_val = gxapi_cy.WrapCOM.create(GXContext._get_tls_geo(), port.encode(), baud, data_size, parity, stop_bits, flow_control, time_out)
        return GXCOM(ret_val)



    @classmethod
    def create_no_terminate(cls, port, baud, data_size, parity, stop_bits, flow_control, time_out):
        """
        Create `GXCOM <geosoft.gxapi.GXCOM>` object.
        """
        ret_val = gxapi_cy.WrapCOM.create_no_terminate(GXContext._get_tls_geo(), port.encode(), baud, data_size, parity, stop_bits, flow_control, time_out)
        return GXCOM(ret_val)






    def read_line_no_terminate(self, line):
        """
        Reads a Line from the `GXCOM <geosoft.gxapi.GXCOM>`
        """
        ret_val, line.value = self._wrapper.read_line_no_terminate(line.value.encode())
        return ret_val




    def read_chars_no_terminate(self, line):
        """
        Reads characters from the `GXCOM <geosoft.gxapi.GXCOM>`, times out and does not terminate
        """
        ret_val, line.value = self._wrapper.read_chars_no_terminate(line.value.encode())
        return ret_val




    def read_line(self, line):
        """
        Reads a Line from the `GXCOM <geosoft.gxapi.GXCOM>`
        """
        line.value = self._wrapper.read_line(line.value.encode())
        




    def write_chars_no_terminate(self, line):
        """
        Writes characters to the `GXCOM <geosoft.gxapi.GXCOM>`.  Does not terminate upon error
        """
        ret_val = self._wrapper.write_chars_no_terminate(line.encode())
        return ret_val




    def purge_comm(self):
        """
        Purges the input and output buffers.
        """
        self._wrapper.purge_comm()
        




    def read_chars(self, line):
        """
        Reads characters from the `GXCOM <geosoft.gxapi.GXCOM>`
        """
        line.value = self._wrapper.read_chars(line.value.encode())
        




    def read_em61_lines_wa(self, lines, wa):
        """
        Reads Lines from the `GXCOM <geosoft.gxapi.GXCOM>` to a `GXWA <geosoft.gxapi.GXWA>`: Geonics EM61 only
        """
        self._wrapper.read_em61_lines_wa(lines, wa._wrapper)
        




    def read_file2_wa(self, wa):
        """
        Reads entire dataset from the `GXCOM <geosoft.gxapi.GXCOM>` to a `GXWA <geosoft.gxapi.GXWA>`
        """
        self._wrapper.read_file2_wa(wa._wrapper)
        




    def read_lines_wa(self, lines, wa):
        """
        Reads Lines from the `GXCOM <geosoft.gxapi.GXCOM>` to a `GXWA <geosoft.gxapi.GXWA>`
        """
        self._wrapper.read_lines_wa(lines, wa._wrapper)
        




    def set_time_out(self, time_out):
        """
        Set the timeout value.
        """
        self._wrapper.set_time_out(time_out)
        




    def write_chars(self, line):
        """
        Writes characters to the `GXCOM <geosoft.gxapi.GXCOM>`
        """
        self._wrapper.write_chars(line.encode())
        




    def write_line(self, line):
        """
        Writes a Line to the `GXCOM <geosoft.gxapi.GXCOM>`
        """
        self._wrapper.write_line(line.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer