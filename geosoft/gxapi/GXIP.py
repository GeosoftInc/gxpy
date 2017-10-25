### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXPG import GXPG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIP:
    """
    GXIP class.

    This class is used in the :class:`geosoft.gxapi.GXIP` System for the import, export
    and processing of Induced Polarization data.

    **Note:**

    The following defines are used in GX code but are not
    part of any functions:
    
    `IP_ARRAY`
    `IP_CHANNELS`
    `IP_LINES`
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXIP`
        
        :returns: A null :class:`geosoft.gxapi.GXIP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXIP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXIP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Plot Jobs


    @classmethod
    def convert_ubcip2_d_to_grid(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Convert a UBC 2D model to a regular grid.

        **Note:**

        Uses :class:`geosoft.gxapi.GXTIN` gridding to sample the model.
        By setting the final value, a resistivity grid can be
        created from conductivity data.
        """
        gxapi_cy.WrapIP.convert_ubcip2_d_to_grid(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9)
        




    def create_default_job(self, p2, p3):
        """
        Create a default job from scratch.
        """
        self._wrapper.create_default_job(p2.encode(), p3)
        




    def export_ubcip3(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Export of :class:`geosoft.gxapi.GXIP` data to UBC format.

        **Note:**

        Outputs a ``*.DAT`` file of the survey data for use in the
        UBC 2D inversion program IPINV2D.
        Include error channel output and version-specific formatting.
        """
        self._wrapper.export_ubcip3(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8)
        



    @classmethod
    def export_ubcip_control(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Export a control file for using in the UBC IPINV2D program.

        **Note:**

        UBC Version 3 Control file.
        Outputs a control file for use in the
        UBC 2D :class:`geosoft.gxapi.GXIP` inversion program IPINV2D.
        """
        gxapi_cy.WrapIP.export_ubcip_control(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode())
        



    @classmethod
    def export_ubcip_control_v5(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16):
        """
        Export a control file for using in the UBC IPINV2D program.

        **Note:**

        UBC Version 5 Control file.
        """
        gxapi_cy.WrapIP.export_ubcip_control_v5(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4.encode(), p5.encode(), p6, p7.encode(), p8, p9.encode(), p10, p11.encode(), p12, p13.encode(), p14, p15.encode(), p16.encode())
        




    def export_ubc_res3(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Export of :class:`geosoft.gxapi.GXIP` Resistivity data to UBC format.

        **Note:**

        Outputs a ``*.DAT`` file of the survey data for use in the
        UBC 2D inversion program DCINV2D.
        Voltage and current channels should be in units such that
        V/I gives volts/amp (or mV/mA).
        """
        self._wrapper.export_ubc_res3(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9)
        



    @classmethod
    def export_ubc_res_control(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Export a control file for using in the UBC DCINV2D program.

        **Note:**

        UBC Version 3.
        Outputs a control file for use in the
        UBC 2D resistivity inversion program DCINV2D.
        """
        gxapi_cy.WrapIP.export_ubc_res_control(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9, p10.encode(), p11.encode())
        



    @classmethod
    def export_ubc_res_control_v5(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):
        """
        Export a control file for using in the UBC DCINV2D program.

        **Note:**

        UBC Version 5.
        Outputs a control file for use in the
        UBC 2D resistivity inversion program DCINV2D.
        """
        gxapi_cy.WrapIP.export_ubc_res_control_v5(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4.encode(), p5.encode(), p6, p7.encode(), p8, p9.encode(), p10, p11.encode(), p12, p13.encode(), p14.encode())
        




    def export_data_to_ubc_3d(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Export of :class:`geosoft.gxapi.GXIP` data to UBC 3D :class:`geosoft.gxapi.GXIP` format.

        **Note:**

        Outputs a ``*.DAT`` file of the survey data for use in the
        UBC :class:`geosoft.gxapi.GXIP` 3D inversion programs.
        """
        self._wrapper.export_data_to_ubc_3d(p2._wrapper, p3._wrapper, p4, p5, p6.encode(), p7.encode(), p8.encode(), p9, p10.encode(), p11.encode())
        



    @classmethod
    def import_ubc2_dmod(cls, p1, p2):
        """
        Import a MOD file from the UBC IPINV2D program.

        **Note:**

        Imports the MOD file values to a :class:`geosoft.gxapi.GXPG` object.
        The CON/CHG selection is necessary because the import sets
        padding values to dummies based on the type of file.
        """
        ret_val = gxapi_cy.WrapIP.import_ubc2_dmod(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXPG(ret_val)



    @classmethod
    def import_ubc2_dmsh(cls, p1, p2, p3, p4, p5):
        """
        Import a MSH file from the UBC IPINV2D program.

        **Note:**

        Imports the MSH file geometry.
        """
        p2.value, p3.value = gxapi_cy.WrapIP.import_ubc2_dmsh(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4._wrapper, p5._wrapper)
        



    @classmethod
    def import_ubc2_d_topo(cls, p1, p2, p3, p4):
        """
        Import a Topography file from the UBC IPINV2D program.

        **Note:**

        Imports the maximum elevation (top of mesh)
        as well as the topo (X, Z) values.
        """
        p2.value = gxapi_cy.WrapIP.import_ubc2_d_topo(GXContext._get_tls_geo(), p1.encode(), p2.value, p3._wrapper, p4._wrapper)
        




    def open_job(self, p2, p3):
        """
        Open a :class:`geosoft.gxapi.GXIP` plotting job
        """
        self._wrapper.open_job(p2.encode(), p3)
        




    def save_job(self, p2, p3):
        """
        Save a :class:`geosoft.gxapi.GXIP` plotting job
        """
        self._wrapper.save_job(p2.encode(), p3)
        



    @classmethod
    def trim_ubc2_d_model(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Trim the padding cells from the UBC IPINV2D Model.

        **Note:**

        The cells are removed from the left, right and bottom.
        The returned :class:`geosoft.gxapi.GXPG` is the trimmed version.
        The input cell size VVs are also trimmed to match,
        and the origin is updated (still upper left corner).
        """
        ret_val, p7.value = gxapi_cy.WrapIP.trim_ubc2_d_model(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5._wrapper, p6._wrapper, p7.value)
        return GXPG(ret_val)




    def write_distant_electrodes(self, p2):
        """
        Write distant electrode locations to channels

        **Note:**

        Writes values for ALL lines.
        """
        self._wrapper.write_distant_electrodes(p2._wrapper)
        




    def write_distant_electrodes_lst(self, p2, p3):
        """
        Write distant electrode locations to channels for a :class:`geosoft.gxapi.GXLST` of lines

        **Note:**

        Writes values for lines in the input :class:`geosoft.gxapi.GXLST`.
        """
        self._wrapper.write_distant_electrodes_lst(p2._wrapper, p3._wrapper)
        




# Miscellaneous



    def average_duplicates_qc(self, p2, p3, p4, p5):
        """
        Average duplicate samples in a database.

        **Note:**

        Averages all values with shared station and N values,
        as long as the mask channel is defined at that FID.
        Previous averaged values (IP_DATA_AVG) are overwritten according to the
        overwrite flag.
        If the QC channel is selected, only those rows of data where the QC channel
        value is "1" will be included in the average.
        """
        self._wrapper.average_duplicates_qc(p2._wrapper, p3.encode(), p4.encode(), p5)
        



    @classmethod
    def create(cls):
        """
        Create :class:`geosoft.gxapi.GXIP`.
        """
        ret_val = gxapi_cy.WrapIP.create(GXContext._get_tls_geo())
        return GXIP(ret_val)






    def export_i2_x(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
        """
        Export line(s) to an Interpex RESIX I2X format file.

        **Note:**

        Exports a line to an ".I2X" file.
        """
        self._wrapper.export_i2_x(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode())
        




    def export_ipdata(self, p2, p3, p4):
        """
        Exports data in the Geosoft IPDATA format.
        """
        self._wrapper.export_ipdata(p2._wrapper, p3.encode(), p4.encode())
        




    def export_ipdata_dir(self, p2, p3, p4, p5):
        """
        Exports data in the Geosoft IPDATA format in the specified directory
        """
        self._wrapper.export_ipdata_dir(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def export_ipred(self, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Exports pseudo-section in the Geosoft IPRED format.

        **Note:**

        The Fraser Filter weights apply to each N expansion above,
        and are listed as w1,w2,w3,...   Unspecified values beyond
        the list's end are set to 1.0.
        """
        self._wrapper.export_ipred(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6, p7.encode(), p8, p9, p10)
        




    def export_ipred_dir(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Exports pseudo-section in the Geosoft IPRED format in the specified directory

        **Note:**

        The Fraser Filter weights apply to each N expansion above,
        and are listed as w1,w2,w3,...   Unspecified values beyond
        the list's end are set to 1.0.
        """
        self._wrapper.export_ipred_dir(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6, p7.encode(), p8, p9, p10, p11.encode())
        




    def export_line_ipdata(self, p2, p3, p4, p5):
        """
        Exports one line of data in the Geosoft IPDATA format.
        """
        self._wrapper.export_line_ipdata(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def export_sgdf(self, p2, p3, p4, p5):
        """
        Exports data to a Scintrex Geophysical Data Format file.
        """
        self._wrapper.export_sgdf(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def get_n_value_lst(self, p2, p3):
        """
        Fill a list with unique N values in selected lines.
        """
        self._wrapper.get_n_value_lst(p2._wrapper, p3._wrapper)
        




    def get_topo_line(self, p2, p3, p4, p5, p6, p7):
        """
        Get topography values for a line.

        **Note:**

        If topography info is available, returns values calculated for
        the input line. If no topography is available, returned values
        will be dummies. Values between actual data are interpolated using
        the Akima spline. Ends are extrapolated using the end data points.
        """
        self._wrapper.get_topo_line(p2._wrapper, p3.encode(), p4, p5, p6, p7._wrapper)
        




    def get_chan_domain(self, p2, p3):
        """
        Is this channel registered as a Time or Frequency domain channel?
        """
        ret_val = self._wrapper.get_chan_domain(p2._wrapper, p3.encode())
        return ret_val



    @classmethod
    def get_chan_label(cls, p1, p2, p4):
        """
        Get the default label and units for a given channel.
        """
        p2.value, p4.value = gxapi_cy.WrapIP.get_chan_label(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4.value.encode())
        




    def get_channel_info(self, p2, p3, p4, p5, p6, p7):
        """
        Time Windows or Frequency info from a channel.
        """
        p4.value, p5.value, p6.value = self._wrapper.get_channel_info(p2._wrapper, p3.encode(), p4.value, p5.value, p6.value, p7._wrapper)
        




    def set_channel_info(self, p2, p3, p4, p5, p6, p7):
        """
        Set Time Windows or Frequency info for a channel.
        """
        self._wrapper.set_channel_info(p2._wrapper, p3.encode(), p4, p5, p6, p7._wrapper)
        




    def import_dump(self, p2, p3, p4):
        """
        Imports data from an :class:`geosoft.gxapi.GXIP` instrument dump file.
        """
        self._wrapper.import_dump(p2, p3._wrapper, p4.encode())
        




    def import_grid(self, p2, p3, p4):
        """
        Imports data from a grid

        **Note:**

        Data is imported to the specified channel.
        The values are interpolated at each row's X and Y
        positions.
        """
        self._wrapper.import_grid(p2._wrapper, p3.encode(), p4.encode())
        




    def import_i2_x(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13):
        """
        Imports an Interpex RESIX I2X format file to a line.

        **Note:**

        Imports a single ".I2X" file to a specified line.
        If the line does not exist, it will be created.
        """
        self._wrapper.import_i2_x(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode(), p13)
        




    def import_i2_x_ex(self, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15):
        """
        Same as ImportI2X_IP, with Zonge data imported as well.

        **Note:**

        Imports a single ".I2X" file to a specified line.
        If the line does not exist, it will be created.
        """
        self._wrapper.import_i2_x_ex(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode(), p13.encode(), p14.encode(), p15)
        




    def import_instrumentation_gdd(self, p2, p3):
        """
        Imports an Instrumentation GDD format file.
        """
        self._wrapper.import_instrumentation_gdd(p2._wrapper, p3.encode())
        




    def import_ipdata(self, p2, p3, p4):
        """
        Imports data in the Geosoft IPDATA format.
        """
        self._wrapper.import_ipdata(p2._wrapper, p3.encode(), p4.encode())
        




    def import_ipdata2(self, p2, p3, p4, p5):
        """
        Imports data in the Geosoft IPDATA format - up to two arrays.

        **Note:**

        The second channel may be specified for frequency domain data sets
        with two array channels; e.g. amplitude and phase, or real and
        imaginary parts. If the second channel is specified, and no
        time or frequncy information is specified in the header (using
        the T= or F= fields) then the import is assumed to be frequency
        domain.
        """
        self._wrapper.import_ipdata2(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def import_ipred(self, p2, p3, p4):
        """
        Imports data from the Geosoft IPRED format.

        **Note:**

        This import produces a limited :class:`geosoft.gxapi.GXIP` data set with no Current "I",
        Voltage "Vp" or Apparent Resistivity "ResApp" values.
        """
        self._wrapper.import_ipred(p2._wrapper, p3.encode(), p4.encode())
        




    def import_merge_ipred(self, p2, p3, p4):
        """
        Imports IPRED data to an existing line.

        **Note:**

        Exits with error if the line does not exist.
        Data is merged on basis of Stn and N value.
        """
        self._wrapper.import_merge_ipred(p2._wrapper, p3.encode(), p4.encode())
        




    def import_sgdf(self, p2, p3):
        """
        Imports data from a Scintrex Geophysical Data Format file.
        """
        self._wrapper.import_sgdf(p2._wrapper, p3.encode())
        




    def import_topo_csv(self, p2, p3):
        """
        Imports topography data from a CSV line-station file

        **Note:**

        The elevation of each point in the current database
        is interpolated from the input topography values.
        """
        self._wrapper.import_topo_csv(p2._wrapper, p3.encode())
        




    def import_topo_grid(self, p2, p3):
        """
        Imports topography data from a grid

        **Note:**

        The elevation of each point in the current database
        is interpolated from the input topography grid.
        """
        self._wrapper.import_topo_grid(p2._wrapper, p3.encode())
        




    def import_zonge_avg(self, p2, p3, p4, p5, p6):
        """
        Imports a Zonge AVG format file.

        **Note:**

        See ImportZongeFLD_IP
        """
        self._wrapper.import_zonge_avg(p2._wrapper, p3.encode(), p4, p5, p6)
        




    def import_zonge_fld(self, p2, p3, p4, p5):
        """
        Imports a Zonge FLD format file.

        **Note:**

        The Zonge Line and Station numbers may not be the X or Y position
        values, and a conversion is required.
        The line direction is taken from the :class:`geosoft.gxapi.GXIP` setup values.
        """
        self._wrapper.import_zonge_fld(p2._wrapper, p3.encode(), p4, p5)
        




    def new_xy_database(self, p2, p3, p4, p5, p6):
        """
        Create a subset database using a mask channel, "N" value

        **Note:**

        A mask channel can be used to select a subset of the data.
        A single N value can also be selected (Dummy for all).
        """
        self._wrapper.new_xy_database(p2._wrapper, p3._wrapper, p4._wrapper, p5.encode(), p6)
        




    def pseudo_plot(self, p2, p3, p4, p5):
        """
        Create pseudo-sections of a single line using a control file.

        **Note:**

        The control file is created using the IPPLTCON GX. It may then
        be modified by hand as required.
        """
        self._wrapper.pseudo_plot(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def pseudo_plot2(self, p2, p3, p4, p5, p6):
        """
        Same as PseudoPlot_IP, but specify a tag for grids created.

        **Note:**

        The control file is created using the IPPLTCON GX. It may then
        be modified by hand as required.
        """
        self._wrapper.pseudo_plot2(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode())
        




    def pseudo_plot2_dir(self, p2, p3, p4, p5, p6, p7):
        """
        Same as PseudoPlot2_IP, but with directory specified.

        **Note:**

        The control file is created using the IPPLTCON GX. It may then
        be modified by hand as required.
        """
        self._wrapper.pseudo_plot2_dir(p2._wrapper, p3.encode(), p4.encode(), p5.encode(), p6.encode(), p7.encode())
        




    def ps_stack(self, p2, p3, p4, p5):
        """
        Create a stacked pseudo-section plot using a control file.

        **Note:**

        The control file is created using the IPSTAKCON GX. It may then
        be modified by hand as required.
        """
        self._wrapper.ps_stack(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        




    def ps_stack2(self, p2, p3, p4, p5, p6):
        """
        As PSStack_IP, but select section spacing option.
        """
        self._wrapper.ps_stack2(p2._wrapper, p3.encode(), p4.encode(), p5, p6.encode())
        




    def ps_stack2_dir(self, p2, p3, p4, p5, p6, p7):
        """
        Same as PseudoPlot2_IP, but with directory specified.
        """
        self._wrapper.ps_stack2_dir(p2._wrapper, p3.encode(), p4.encode(), p5, p6.encode(), p7.encode())
        




    def qc_chan_lst(self, p2, p3):
        """
        Fill a list with QC channels.

        **Note:**

        Searches for the following QC channels existing in a database:
        QC, QC_RES.
        """
        self._wrapper.qc_chan_lst(p2._wrapper, p3._wrapper)
        




    def recalculate(self, p2):
        """
        Recalculate derived channel values.

        **Note:**

        This function recalculates "derived" channel values from
        "core" data.
        
            1. Recalculates the "STN" and "N" channels, using the TX1,
               TX2, RX1 and RX2 channels (depending on the system).
            2. Recalculates the apparent resistivity "ResCalc",
               average "IP_Avg" and metal factor "MF" channels
            3. Recalculates the "X" and "Y" channels. One of these will
               be equal to "STN", the other to the internally stored
               line number for the current line.
            4. Recalculate the "Z" channel, based on the current "Topo"
               channel, and the "N" values.
        
        Warning: If you make a change to an electrode location, you
        would have to call Recalculate_IP, then recalculate "Topo"
        (since the X and Y values would have changed), then call
        RecalculateZ_IP, since "Z" values are based on "Topo" values.
        """
        self._wrapper.recalculate(p2._wrapper)
        




    def recalculate_ex(self, p2, p3):
        """
        Recalculate derived channel values, with option for including/excluding location calculations.

        **Note:**

        See Recalculate_IP. This version allows you to suppress the recalculation of the
        current X, Y and Z channel values from the station locations.
        """
        self._wrapper.recalculate_ex(p2._wrapper, p3)
        




    def recalculate_z(self, p2):
        """
        Recalculate Z channel values.

        **Note:**

        The "Z" channel values are calculated as follows:
        If the "Topo" value is defined, then
        Z = Topo - 0.5*N*A, where "N" is the N-spacing, and
        A is the A-spacing. If the Topography is not defined, then
        it is assumed to be equal to 0.
        """
        self._wrapper.recalculate_z(p2._wrapper)
        




    def set_import_line(self, p2):
        """
        Set the line name for some imports.

        **Note:**

        For some imports, no line name is derivable from the import itself.
        """
        self._wrapper.set_import_line(p2.encode())
        




    def set_import_mode(self, p2):
        """
        When importing data to a line, set append/overwrite mode.

        **Note:**

        By default, importing data overwrites existing data.
        Call this function before doing the import in order
        to append imported data to existing data.
        "Short" data channels will be dummied to the existing
        data length before the new data is appended.
        """
        self._wrapper.set_import_mode(p2)
        




    def window(self, p2, p3, p4, p5):
        """
        Window an :class:`geosoft.gxapi.GXIP` array channel to produce a normal channel.

        **Note:**

        The array channels cannot be used directly to produce sections.
        Window_IP allows the user to select one or more of the windows
        and create a new channel. In time domain, if more than one channel
        is selected a weighted sum is performed, according to window widths.
        In frequency domain a simple sum is performed.
        Window List Syntax:
        """
        self._wrapper.window(p2._wrapper, p3.encode(), p4.encode(), p5.encode())
        



    @classmethod
    def winnow_chan_list(cls, p1):
        """
        Removes obviously non-pseudo-section type channels from list.
        """
        gxapi_cy.WrapIP.winnow_chan_list(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def winnow_chan_list2(cls, p1, p2):
        """
        Same as WinnowChanList_IP, but removes current X,Y,Z.
        """
        gxapi_cy.WrapIP.winnow_chan_list2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        




    def is_valid_line(self, p2, p3):
        """
        See if a given database line is registered for the :class:`geosoft.gxapi.GXIP` system
        """
        ret_val = self._wrapper.is_valid_line(p2._wrapper, p3.encode())
        return ret_val




    def line_array_type(self, p2, p3):
        """
        Return the type of :class:`geosoft.gxapi.GXIP` array for the input line. If necessary, first imports the specified line into the :class:`geosoft.gxapi.GXIP` object
        """
        ret_val = self._wrapper.line_array_type(p2._wrapper, p3.encode())
        return ret_val




    def a_spacing(self, p2, p3):
        """
        Return the A-Spacing for the input line. If necessary, first imports the specified line into the :class:`geosoft.gxapi.GXIP` object.
        """
        ret_val = self._wrapper.a_spacing(p2._wrapper, p3.encode())
        return ret_val




    def pldp_convention(self):
        """
        Return the user's plot point convention for pole-dipole arrays.
        """
        ret_val = self._wrapper.pldp_convention()
        return ret_val




    def get_electrode_locations_and_mask_values(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Get unique electrodes, along with current mask info.

        **Note:**

        The mask values are determined from the first row where a given electrode is found.
        Values returned for all currently selected lines.
        """
        self._wrapper.get_electrode_locations_and_mask_values(p2._wrapper, p3.encode(), p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper)
        




    def get_electrode_locations_and_mask_values2(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Get unique electrodes, along with current mask info.

        **Note:**

        The mask values are determined from the first row where a given electrode is found.
        Values returned for all currently selected lines.
        """
        self._wrapper.get_electrode_locations_and_mask_values2(p2._wrapper, p3.encode(), p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        




    def set_electrode_mask_values(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Set unique electrodes, along with current mask info.

        **Note:**

        Mask values are set for all included electrode locations, currently selected lines.
        """
        self._wrapper.set_electrode_mask_values(p2._wrapper, p3.encode(), p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper)
        




    def set_electrode_mask_values_single_qc_channel(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Set unique electrodes, along with current mask info.

        **Note:**

        Mask values are set for all included electrode locations, currently selected lines.
        """
        self._wrapper.set_electrode_mask_values_single_qc_channel(p2._wrapper, p3.encode(), p4, p5, p6._wrapper, p7._wrapper, p8._wrapper)
        



    @classmethod
    def get_qc_channel(cls, p1, p2, p3):
        """
        Get the QC channel handle, if it exists.

        **Note:**

        For :class:`geosoft.gxapi.GXIP`, looks for "QC_IP", then "QC_OffTime", then "QC".
        For Resistivity, looks for "QC_Res", then "QC_OnTime" (case insensitive).
        """
        ret_val, p3.value = gxapi_cy.WrapIP.get_qc_channel(GXContext._get_tls_geo(), p1._wrapper, p2, p3.value.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer