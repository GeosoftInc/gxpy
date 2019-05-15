### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXDB import GXDB
from .GXVA import GXVA
from .GXVV import GXVV


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDBWRITE(gxapi_cy.WrapDBWRITE):
    """
    GXDBWRITE class.

    The `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` class is used to open and write to databases. Large blocks of data
    are split into blocks and served up sequentially to prevent the over-use of virtual memory when VVs or VAs are being written to channels.
    Individual data blocks are limited by default to 1 MB (which is user-alterable). Data less than the block size
    are served up whole, one block per line.
    """

    def __init__(self, handle=0):
        super(GXDBWRITE, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDBWRITE <geosoft.gxapi.GXDBWRITE>`
        
        :returns: A null `GXDBWRITE <geosoft.gxapi.GXDBWRITE>`
        :rtype:   GXDBWRITE
        """
        return GXDBWRITE()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Create Methods


    @classmethod
    def create(cls, db):
        """
        Create a `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object
        Add channels using the `add_channel <geosoft.gxapi.GXDBWRITE.add_channel>` method.channel.
        
        :param db:  Database input
        :type  db:  GXDB

        :returns:    `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object
        :rtype:      GXDBWRITE

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapDBWRITE._create(GXContext._get_tls_geo(), db)
        return GXDBWRITE(ret_val)



    @classmethod
    def create_xy(cls, db):
        """
        Create a `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object for a XY-located data. Add channels using the
        `add_channel <geosoft.gxapi.GXDBWRITE.add_channel>` method.
        
        :param db:  Database input
        :type  db:  GXDB

        :returns:    `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object
        :rtype:      GXDBWRITE

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapDBWRITE._create_xy(GXContext._get_tls_geo(), db)
        return GXDBWRITE(ret_val)



    @classmethod
    def create_xyz(cls, db):
        """
        Create a `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object for a XYZ-located data.
        Add channels using the `add_channel <geosoft.gxapi.GXDBWRITE.add_channel>` method.channel
        
        :param db:  Database input
        :type  db:  GXDB

        :returns:    `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object
        :rtype:      GXDBWRITE

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapDBWRITE._create_xyz(GXContext._get_tls_geo(), db)
        return GXDBWRITE(ret_val)






    def add_channel(self, chan):
        """
        Add a data channel to the `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object.
        
        :param chan:     Channel handle (does not need to be locked, but can be.)
        :type  chan:     int

        :returns:        Channel index. Use for getting the correct `GXVV <geosoft.gxapi.GXVV>` or `GXVA <geosoft.gxapi.GXVA>` object.
        :rtype:          int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._add_channel(chan)
        return ret_val




# Data Access Methods



    def get_db(self):
        """
        Get the output `GXDB <geosoft.gxapi.GXDB>` handle from the `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object.
        

        :returns:        `GXDB <geosoft.gxapi.GXDB>` handle
        :rtype:          GXDB

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_db()
        return GXDB(ret_val)




    def get_vv(self, chan):
        """
        Get the `GXVV <geosoft.gxapi.GXVV>` handle for a channel.
        
        :param chan:     Index of channel to access.
        :type  chan:     int

        :returns:        `GXVV <geosoft.gxapi.GXVV>` handle
        :rtype:          GXVV

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Call only for single-column (regular) channels. You can call the `get_chan_array_size <geosoft.gxapi.GXDBWRITE.get_chan_array_size>`
        function to find the number fo columns in a given channel. The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        """
        ret_val = self._get_vv(chan)
        return GXVV(ret_val)




    def get_va(self, chan):
        """
        Get the `GXVA <geosoft.gxapi.GXVA>` handle for an array channel.
        
        :param chan:     Index of channel to access.
        :type  chan:     int

        :returns:        `GXVA <geosoft.gxapi.GXVA>` handle
        :rtype:          GXVA

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Call only for array (multi-column) channels. You can call the `get_chan_array_size <geosoft.gxapi.GXDBWRITE.get_chan_array_size>`
        function to find the number fo columns in a given channel, or you can call `GXVA.col <geosoft.gxapi.GXVA.col>` on the returned `GXVA <geosoft.gxapi.GXVA>` handle.
        The `GXVA <geosoft.gxapi.GXVA>` is filled anew for each block served up.
        """
        ret_val = self._get_va(chan)
        return GXVA(ret_val)




    def get_v_vx(self):
        """
        Get the X channel `GXVV <geosoft.gxapi.GXVV>` handle.
        

        :returns:        `GXVV <geosoft.gxapi.GXVV>` handle
        :rtype:          GXVV

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Only available for the CreateXY or CreateXYZ methods.
        The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        """
        ret_val = self._get_v_vx()
        return GXVV(ret_val)




    def get_v_vy(self):
        """
        Get the Y channel `GXVV <geosoft.gxapi.GXVV>` handle.
        

        :returns:        `GXVV <geosoft.gxapi.GXVV>` handle
        :rtype:          GXVV

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Only available for the CreateXY or CreateXYZ methods.
        The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        """
        ret_val = self._get_v_vy()
        return GXVV(ret_val)




    def get_v_vz(self):
        """
        Get the Z channel `GXVV <geosoft.gxapi.GXVV>` handle.
        

        :returns:        `GXVV <geosoft.gxapi.GXVV>` handle
        :rtype:          GXVV

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Only available for the CreateXY or CreateXYZ methods.
        The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        If the Z channel is an array channel, the returned `GXVV <geosoft.gxapi.GXVV>` is the "base" `GXVV <geosoft.gxapi.GXVV>` of the `GXVA <geosoft.gxapi.GXVA>` and contains all items sequentially.
        """
        ret_val = self._get_v_vz()
        return GXVV(ret_val)




    def get_chan_array_size(self, chan):
        """
        Get the number of columns of data in a channel.
        
        :param chan:     Index of channel to access.
        :type  chan:     int

        :returns:        The number of columns (array size) for a channel
        :rtype:          int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Regular channels have one column of data. Array channels have more than one column of data.
        This function should be called to determine whether to use `get_vv <geosoft.gxapi.GXDBWRITE.get_vv>` or `get_va <geosoft.gxapi.GXDBWRITE.get_va>` to access data
        for a channel.
        """
        ret_val = self._get_chan_array_size(chan)
        return ret_val




# Processing



    def add_block(self, line):
        """
        Add the current block of data.
        
        :param line:     Line
        :type  line:     int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** First, set up the data for each channel by copying values into the individual channel VVs and VAs.
        """
        self._add_block(line)
        




    def commit(self):
        """
        Commit remaining data to the database.
        

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._commit()
        




    def test_func(self, ra):
        """
        Temporary test function.
        
        :param ra:       `GXRA <geosoft.gxapi.GXRA>` handle to text file to import.
        :type  ra:       GXRA

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Designed to import the "Massive.xyz" file, which has data in the format "X Y Z Data".
        """
        self._test_func(ra)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer