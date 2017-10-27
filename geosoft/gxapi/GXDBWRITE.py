### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
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
class GXDBWRITE:
    """
    GXDBWRITE class.

    The `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` class is used to open and write to databases. Large blocks of data
    are split into blocks and served up sequentially to prevent the over-use of virtual memory when VVs or VAs are being written to channels.
    Individual data blocks are limited by default to 1 MB (which is user-alterable). Data less than the block size
    are served up whole, one block per line.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDBWRITE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDBWRITE`
        
        :returns: A null `GXDBWRITE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDBWRITE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDBWRITE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Create Methods


    @classmethod
    def create(cls, db):
        """
        Create a `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object
        Add channels using the `add_channel <geosoft.gxapi.GXDBWRITE.add_channel>` method.channel.
        """
        ret_val = gxapi_cy.WrapDBWRITE.create(GXContext._get_tls_geo(), db._wrapper)
        return GXDBWRITE(ret_val)



    @classmethod
    def create_xy(cls, db):
        """
        Create a `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object for a XY-located data. Add channels using the
        `add_channel <geosoft.gxapi.GXDBWRITE.add_channel>` method.
        """
        ret_val = gxapi_cy.WrapDBWRITE.create_xy(GXContext._get_tls_geo(), db._wrapper)
        return GXDBWRITE(ret_val)



    @classmethod
    def create_xyz(cls, db):
        """
        Create a `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object for a XYZ-located data.
        Add channels using the `add_channel <geosoft.gxapi.GXDBWRITE.add_channel>` method.channel
        """
        ret_val = gxapi_cy.WrapDBWRITE.create_xyz(GXContext._get_tls_geo(), db._wrapper)
        return GXDBWRITE(ret_val)






    def add_channel(self, chan):
        """
        Add a data channel to the `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object.
        """
        ret_val = self._wrapper.add_channel(chan)
        return ret_val




# Data Access Methods



    def get_db(self):
        """
        Get the output `GXDB <geosoft.gxapi.GXDB>` handle from the `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object.
        """
        ret_val = self._wrapper.get_db()
        return GXDB(ret_val)




    def get_vv(self, chan):
        """
        Get the `GXVV <geosoft.gxapi.GXVV>` handle for a channel.

        **Note:**

        Call only for single-column (regular) channels. You can call the `get_chan_array_size <geosoft.gxapi.GXDBWRITE.get_chan_array_size>`
        function to find the number fo columns in a given channel. The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        """
        ret_val = self._wrapper.get_vv(chan)
        return GXVV(ret_val)




    def get_va(self, chan):
        """
        Get the `GXVA <geosoft.gxapi.GXVA>` handle for an array channel.

        **Note:**

        Call only for array (multi-column) channels. You can call the `get_chan_array_size <geosoft.gxapi.GXDBWRITE.get_chan_array_size>`
        function to find the number fo columns in a given channel, or you can call `GXVA.col <geosoft.gxapi.GXVA.col>` on the returned `GXVA <geosoft.gxapi.GXVA>` handle.
        The `GXVA <geosoft.gxapi.GXVA>` is filled anew for each block served up.
        """
        ret_val = self._wrapper.get_va(chan)
        return GXVA(ret_val)




    def get_v_vx(self):
        """
        Get the X channel `GXVV <geosoft.gxapi.GXVV>` handle.

        **Note:**

        Only available for the CreateXY or CreateXYZ methods.
        The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        """
        ret_val = self._wrapper.get_v_vx()
        return GXVV(ret_val)




    def get_v_vy(self):
        """
        Get the Y channel `GXVV <geosoft.gxapi.GXVV>` handle.

        **Note:**

        Only available for the CreateXY or CreateXYZ methods.
        The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        """
        ret_val = self._wrapper.get_v_vy()
        return GXVV(ret_val)




    def get_v_vz(self):
        """
        Get the Z channel `GXVV <geosoft.gxapi.GXVV>` handle.

        **Note:**

        Only available for the CreateXY or CreateXYZ methods.
        The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        If the Z channel is an array channel, the returned `GXVV <geosoft.gxapi.GXVV>` is the "base" `GXVV <geosoft.gxapi.GXVV>` of the `GXVA <geosoft.gxapi.GXVA>` and contains all items sequentially.
        """
        ret_val = self._wrapper.get_v_vz()
        return GXVV(ret_val)




    def get_chan_array_size(self, chan):
        """
        Get the number of columns of data in a channel.

        **Note:**

        Regular channels have one column of data. Array channels have more than one column of data.
        This function should be called to determine whether to use `get_vv <geosoft.gxapi.GXDBWRITE.get_vv>` or `get_va <geosoft.gxapi.GXDBWRITE.get_va>` to access data
        for a channel.
        """
        ret_val = self._wrapper.get_chan_array_size(chan)
        return ret_val




# Processing



    def add_block(self, line):
        """
        Add the current block of data.

        **Note:**

        First, set up the data for each channel by copying values into the individual channel VVs and VAs.
        """
        self._wrapper.add_block(line)
        




    def commit(self):
        """
        Commit remaining data to the database.
        """
        self._wrapper.commit()
        




    def test_func(self, ra):
        """
        Temporary test function.

        **Note:**

        Designed to import the "Massive.xyz" file, which has data in the format "X Y Z Data".
        """
        self._wrapper.test_func(ra._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer