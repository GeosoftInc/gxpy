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
class GXCOM(gxapi_cy.WrapCOM):
    """
    GXCOM class.

    This class is used to communicate with external serial devices. It allows the setting of timeouts.
    """

    def __init__(self, handle=0):
        super(GXCOM, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXCOM <geosoft.gxapi.GXCOM>`
        
        :returns: A null `GXCOM <geosoft.gxapi.GXCOM>`
        :rtype:   GXCOM
        """
        return GXCOM()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, port, baud, data_size, parity, stop_bits, flow_control, time_out):
        """
        Create `GXCOM <geosoft.gxapi.GXCOM>` object.
        
        :param port:          Port name to open ("COM1" is example)
        :param baud:          :ref:`COM_BAUD`
        :param data_size:     :ref:`COM_DATASIZE`
        :param parity:        :ref:`COM_PARITY`
        :param stop_bits:     :ref:`COM_STOPBITS`
        :param flow_control:  :ref:`COM_FLOWCONTROL`
        :param time_out:      Timeout in Ms (500)
        :type  port:          str
        :type  baud:          int
        :type  data_size:     int
        :type  parity:        int
        :type  stop_bits:     int
        :type  flow_control:  int
        :type  time_out:      int

        :returns:             `GXCOM <geosoft.gxapi.GXCOM>` Object
        :rtype:               GXCOM

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapCOM._create(GXContext._get_tls_geo(), port.encode(), baud, data_size, parity, stop_bits, flow_control, time_out)
        return GXCOM(ret_val)



    @classmethod
    def create_no_terminate(cls, port, baud, data_size, parity, stop_bits, flow_control, time_out):
        """
        Create `GXCOM <geosoft.gxapi.GXCOM>` object.
        
        :param port:          Port name to open ("COM1" is example)
        :param baud:          :ref:`COM_BAUD`
        :param data_size:     :ref:`COM_DATASIZE`
        :param parity:        :ref:`COM_PARITY`
        :param stop_bits:     :ref:`COM_STOPBITS`
        :param flow_control:  :ref:`COM_FLOWCONTROL`
        :param time_out:      Timeout in Ms (500)
        :type  port:          str
        :type  baud:          int
        :type  data_size:     int
        :type  parity:        int
        :type  stop_bits:     int
        :type  flow_control:  int
        :type  time_out:      int

        :returns:             `GXCOM <geosoft.gxapi.GXCOM>` Object
        :rtype:               GXCOM

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapCOM._create_no_terminate(GXContext._get_tls_geo(), port.encode(), baud, data_size, parity, stop_bits, flow_control, time_out)
        return GXCOM(ret_val)






    def read_line_no_terminate(self, line):
        """
        Reads a Line from the `GXCOM <geosoft.gxapi.GXCOM>`
        
        :param line:  String for line
        :type  line:  str_ref

        :returns:     0 - if successful in reading a line
                      1 - if an error was encountered
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val, line.value = self._read_line_no_terminate(line.value.encode())
        return ret_val




    def read_chars_no_terminate(self, line):
        """
        Reads characters from the `GXCOM <geosoft.gxapi.GXCOM>`, times out and does not terminate
        
        :param line:  String for characters
        :type  line:  str_ref

        :returns:     0 - if successful
                      1 - if time out or error
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val, line.value = self._read_chars_no_terminate(line.value.encode())
        return ret_val




    def read_line(self, line):
        """
        Reads a Line from the `GXCOM <geosoft.gxapi.GXCOM>`
        
        :param line:  String for line
        :type  line:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        line.value = self._read_line(line.value.encode())
        




    def write_chars_no_terminate(self, line):
        """
        Writes characters to the `GXCOM <geosoft.gxapi.GXCOM>`.  Does not terminate upon error
        
        :param line:  Line to write
        :type  line:  str

        :returns:     0 - if successful in writing a string
                      1 - if time out or error was encountered
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._write_chars_no_terminate(line.encode())
        return ret_val




    def purge_comm(self):
        """
        Purges the input and output buffers.
        

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._purge_comm()
        




    def read_chars(self, line):
        """
        Reads characters from the `GXCOM <geosoft.gxapi.GXCOM>`
        
        :param line:  String for characters
        :type  line:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        line.value = self._read_chars(line.value.encode())
        




    def read_em61_lines_wa(self, lines, wa):
        """
        Reads Lines from the `GXCOM <geosoft.gxapi.GXCOM>` to a `GXWA <geosoft.gxapi.GXWA>`: Geonics EM61 only
        
        :param lines:  Number of lines
        :param wa:     Where to put lines
        :type  lines:  int
        :type  wa:     GXWA

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._read_em61_lines_wa(lines, wa)
        




    def read_file2_wa(self, wa):
        """
        Reads entire dataset from the `GXCOM <geosoft.gxapi.GXCOM>` to a `GXWA <geosoft.gxapi.GXWA>`
        
        :param wa:   Where to put lines
        :type  wa:   GXWA

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._read_file2_wa(wa)
        




    def read_lines_wa(self, lines, wa):
        """
        Reads Lines from the `GXCOM <geosoft.gxapi.GXCOM>` to a `GXWA <geosoft.gxapi.GXWA>`
        
        :param lines:  Number of lines
        :param wa:     Where to put lines
        :type  lines:  int
        :type  wa:     GXWA

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._read_lines_wa(lines, wa)
        




    def set_time_out(self, time_out):
        """
        Set the timeout value.
        
        :param time_out:  Timeout in Ms (500)
        :type  time_out:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_time_out(time_out)
        




    def write_chars(self, line):
        """
        Writes characters to the `GXCOM <geosoft.gxapi.GXCOM>`
        
        :param line:  Line to write
        :type  line:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._write_chars(line.encode())
        




    def write_line(self, line):
        """
        Writes a Line to the `GXCOM <geosoft.gxapi.GXCOM>`
        
        :param line:  Line to write
        :type  line:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._write_line(line.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer