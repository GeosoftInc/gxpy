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

    This class is used in the `GXIP` System for the import, export
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
        A null (undefined) instance of `GXIP`
        
        :returns: A null `GXIP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXIP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXIP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Plot Jobs


    @classmethod
    def convert_ubcip2_d_to_grid(cls, file, pg, v_vx, v_vz, x, z, cx, cz, reciprocal):
        """
        Convert a UBC 2D model to a regular grid.

        **Note:**

        Uses `GXTIN` gridding to sample the model.
        By setting the final value, a resistivity grid can be
        created from conductivity data.
        """
        gxapi_cy.WrapIP.convert_ubcip2_d_to_grid(GXContext._get_tls_geo(), file.encode(), pg._wrapper, v_vx._wrapper, v_vz._wrapper, x, z, cx, cz, reciprocal)
        




    def create_default_job(self, ini, type):
        """
        Create a default job from scratch.
        """
        self._wrapper.create_default_job(ini.encode(), type)
        




    def export_ubcip3(self, db, line, chan, error_chan, obs, topo, version):
        """
        Export of `GXIP` data to UBC format.

        **Note:**

        Outputs a ``*.DAT`` file of the survey data for use in the
        UBC 2D inversion program IPINV2D.
        Include error channel output and version-specific formatting.
        """
        self._wrapper.export_ubcip3(db._wrapper, line.encode(), chan.encode(), error_chan.encode(), obs.encode(), topo.encode(), version)
        



    @classmethod
    def export_ubcip_control(cls, control, n_iter, i_rest, chi_factor, obs, cond, mesh, topo, initial, ref_mod, alphas, wts):
        """
        Export a control file for using in the UBC IPINV2D program.

        **Note:**

        UBC Version 3 Control file.
        Outputs a control file for use in the
        UBC 2D `GXIP` inversion program IPINV2D.
        """
        gxapi_cy.WrapIP.export_ubcip_control(GXContext._get_tls_geo(), control.encode(), n_iter, i_rest, chi_factor, obs.encode(), cond.encode(), mesh.encode(), topo.encode(), initial.encode(), ref_mod.encode(), alphas.encode(), wts.encode())
        



    @classmethod
    def export_ubcip_control_v5(cls, control, n_iter, chi_factor, obs, topo, cond_selection, cond, mesh_selection, mesh, initial_selection, initial, reference_selection, ref_cond, alphas_selection, alphas, wts):
        """
        Export a control file for using in the UBC IPINV2D program.

        **Note:**

        UBC Version 5 Control file.
        """
        gxapi_cy.WrapIP.export_ubcip_control_v5(GXContext._get_tls_geo(), control.encode(), n_iter, chi_factor, obs.encode(), topo.encode(), cond_selection, cond.encode(), mesh_selection, mesh.encode(), initial_selection, initial.encode(), reference_selection, ref_cond.encode(), alphas_selection, alphas.encode(), wts.encode())
        




    def export_ubc_res3(self, db, line, voltage_chan, current_chan, error_chan, obs, topo, version):
        """
        Export of `GXIP` Resistivity data to UBC format.

        **Note:**

        Outputs a ``*.DAT`` file of the survey data for use in the
        UBC 2D inversion program DCINV2D.
        Voltage and current channels should be in units such that
        V/I gives volts/amp (or mV/mA).
        """
        self._wrapper.export_ubc_res3(db._wrapper, line.encode(), voltage_chan.encode(), current_chan.encode(), error_chan.encode(), obs.encode(), topo.encode(), version)
        



    @classmethod
    def export_ubc_res_control(cls, control, n_iter, i_rest, chi_factor, obs, mesh, topo, initial, ref_cond, alphas, wts):
        """
        Export a control file for using in the UBC DCINV2D program.

        **Note:**

        UBC Version 3.
        Outputs a control file for use in the
        UBC 2D resistivity inversion program DCINV2D.
        """
        gxapi_cy.WrapIP.export_ubc_res_control(GXContext._get_tls_geo(), control.encode(), n_iter, i_rest, chi_factor, obs.encode(), mesh.encode(), topo.encode(), initial.encode(), ref_cond, alphas.encode(), wts.encode())
        



    @classmethod
    def export_ubc_res_control_v5(cls, control, n_iter, chi_factor, obs, topo, mesh_selection, mesh, initial_selection, initial, reference_selection, ref_cond, alphas_selection, alphas, wts):
        """
        Export a control file for using in the UBC DCINV2D program.

        **Note:**

        UBC Version 5.
        Outputs a control file for use in the
        UBC 2D resistivity inversion program DCINV2D.
        """
        gxapi_cy.WrapIP.export_ubc_res_control_v5(GXContext._get_tls_geo(), control.encode(), n_iter, chi_factor, obs.encode(), topo.encode(), mesh_selection, mesh.encode(), initial_selection, initial.encode(), reference_selection, ref_cond.encode(), alphas_selection, alphas.encode(), wts.encode())
        




    def export_data_to_ubc_3d(self, db, line_lst, locations_only, include_z, chan, error_chan, mask_chan, ip_type, comments, obs):
        """
        Export of `GXIP` data to UBC 3D `GXIP` format.

        **Note:**

        Outputs a ``*.DAT`` file of the survey data for use in the
        UBC `GXIP` 3D inversion programs.
        """
        self._wrapper.export_data_to_ubc_3d(db._wrapper, line_lst._wrapper, locations_only, include_z, chan.encode(), error_chan.encode(), mask_chan.encode(), ip_type, comments.encode(), obs.encode())
        



    @classmethod
    def import_ubc2_dmod(cls, file, type):
        """
        Import a MOD file from the UBC IPINV2D program.

        **Note:**

        Imports the MOD file values to a `GXPG` object.
        The CON/CHG selection is necessary because the import sets
        padding values to dummies based on the type of file.
        """
        ret_val = gxapi_cy.WrapIP.import_ubc2_dmod(GXContext._get_tls_geo(), file.encode(), type)
        return GXPG(ret_val)



    @classmethod
    def import_ubc2_dmsh(cls, file, x, z, v_vx, v_vz):
        """
        Import a MSH file from the UBC IPINV2D program.

        **Note:**

        Imports the MSH file geometry.
        """
        x.value, z.value = gxapi_cy.WrapIP.import_ubc2_dmsh(GXContext._get_tls_geo(), file.encode(), x.value, z.value, v_vx._wrapper, v_vz._wrapper)
        



    @classmethod
    def import_ubc2_d_topo(cls, file, elev0, v_vx, v_vz):
        """
        Import a Topography file from the UBC IPINV2D program.

        **Note:**

        Imports the maximum elevation (top of mesh)
        as well as the topo (X, Z) values.
        """
        elev0.value = gxapi_cy.WrapIP.import_ubc2_d_topo(GXContext._get_tls_geo(), file.encode(), elev0.value, v_vx._wrapper, v_vz._wrapper)
        




    def open_job(self, job, type):
        """
        Open a `GXIP` plotting job
        """
        self._wrapper.open_job(job.encode(), type)
        




    def save_job(self, job, type):
        """
        Save a `GXIP` plotting job
        """
        self._wrapper.save_job(job.encode(), type)
        



    @classmethod
    def trim_ubc2_d_model(cls, pg, trim_xl, trim_xr, trim_z, v_vx, v_vz, x):
        """
        Trim the padding cells from the UBC IPINV2D Model.

        **Note:**

        The cells are removed from the left, right and bottom.
        The returned `GXPG` is the trimmed version.
        The input cell size VVs are also trimmed to match,
        and the origin is updated (still upper left corner).
        """
        ret_val, x.value = gxapi_cy.WrapIP.trim_ubc2_d_model(GXContext._get_tls_geo(), pg._wrapper, trim_xl, trim_xr, trim_z, v_vx._wrapper, v_vz._wrapper, x.value)
        return GXPG(ret_val)




    def write_distant_electrodes(self, db):
        """
        Write distant electrode locations to channels

        **Note:**

        Writes values for ALL lines.
        """
        self._wrapper.write_distant_electrodes(db._wrapper)
        




    def write_distant_electrodes_lst(self, db, lst):
        """
        Write distant electrode locations to channels for a `GXLST` of lines

        **Note:**

        Writes values for lines in the input `GXLST`.
        """
        self._wrapper.write_distant_electrodes_lst(db._wrapper, lst._wrapper)
        




# Miscellaneous



    def average_duplicates_qc(self, db, chan, qc_chan, out):
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
        self._wrapper.average_duplicates_qc(db._wrapper, chan.encode(), qc_chan.encode(), out)
        



    @classmethod
    def create(cls):
        """
        Create `GXIP`.
        """
        ret_val = gxapi_cy.WrapIP.create(GXContext._get_tls_geo())
        return GXIP(ret_val)






    def export_i2_x(self, db, file, line, res_data, p6, p7, p8, p9, p10, p11, p12):
        """
        Export line(s) to an Interpex RESIX I2X format file.

        **Note:**

        Exports a line to an ".I2X" file.
        """
        self._wrapper.export_i2_x(db._wrapper, file.encode(), line.encode(), res_data.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode())
        




    def export_ipdata(self, db, chan, title):
        """
        Exports data in the Geosoft IPDATA format.
        """
        self._wrapper.export_ipdata(db._wrapper, chan.encode(), title.encode())
        




    def export_ipdata_dir(self, db, chan, title, dir):
        """
        Exports data in the Geosoft IPDATA format in the specified directory
        """
        self._wrapper.export_ipdata_dir(db._wrapper, chan.encode(), title.encode(), dir.encode())
        




    def export_ipred(self, db, title, chan, suffix, filter, wts, stn1, stn2, max_n):
        """
        Exports pseudo-section in the Geosoft IPRED format.

        **Note:**

        The Fraser Filter weights apply to each N expansion above,
        and are listed as w1,w2,w3,...   Unspecified values beyond
        the list's end are set to 1.0.
        """
        self._wrapper.export_ipred(db._wrapper, title.encode(), chan.encode(), suffix.encode(), filter, wts.encode(), stn1, stn2, max_n)
        




    def export_ipred_dir(self, db, title, chan, suffix, filter, wts, stn1, stn2, max_n, dir):
        """
        Exports pseudo-section in the Geosoft IPRED format in the specified directory

        **Note:**

        The Fraser Filter weights apply to each N expansion above,
        and are listed as w1,w2,w3,...   Unspecified values beyond
        the list's end are set to 1.0.
        """
        self._wrapper.export_ipred_dir(db._wrapper, title.encode(), chan.encode(), suffix.encode(), filter, wts.encode(), stn1, stn2, max_n, dir.encode())
        




    def export_line_ipdata(self, db, line, chan, title):
        """
        Exports one line of data in the Geosoft IPDATA format.
        """
        self._wrapper.export_line_ipdata(db._wrapper, line.encode(), chan.encode(), title.encode())
        




    def export_sgdf(self, db, file, chan, chan2):
        """
        Exports data to a Scintrex Geophysical Data Format file.
        """
        self._wrapper.export_sgdf(db._wrapper, file.encode(), chan.encode(), chan2.encode())
        




    def get_n_value_lst(self, db, lst):
        """
        Fill a list with unique N values in selected lines.
        """
        self._wrapper.get_n_value_lst(db._wrapper, lst._wrapper)
        




    def get_topo_line(self, db, line, x_min, x_max, x_inc, vv):
        """
        Get topography values for a line.

        **Note:**

        If topography info is available, returns values calculated for
        the input line. If no topography is available, returned values
        will be dummies. Values between actual data are interpolated using
        the Akima spline. Ends are extrapolated using the end data points.
        """
        self._wrapper.get_topo_line(db._wrapper, line.encode(), x_min, x_max, x_inc, vv._wrapper)
        




    def get_chan_domain(self, db, chan):
        """
        Is this channel registered as a Time or Frequency domain channel?
        """
        ret_val = self._wrapper.get_chan_domain(db._wrapper, chan.encode())
        return ret_val



    @classmethod
    def get_chan_label(cls, chan, label, units):
        """
        Get the default label and units for a given channel.
        """
        label.value, units.value = gxapi_cy.WrapIP.get_chan_label(GXContext._get_tls_geo(), chan.encode(), label.value.encode(), units.value.encode())
        




    def get_channel_info(self, db, chan, domain, delay, n_windows, vv):
        """
        Time Windows or Frequency info from a channel.
        """
        domain.value, delay.value, n_windows.value = self._wrapper.get_channel_info(db._wrapper, chan.encode(), domain.value, delay.value, n_windows.value, vv._wrapper)
        




    def set_channel_info(self, db, chan, domain, delay, n_windows, vv):
        """
        Set Time Windows or Frequency info for a channel.
        """
        self._wrapper.set_channel_info(db._wrapper, chan.encode(), domain, delay, n_windows, vv._wrapper)
        




    def import_dump(self, sys, db, dump_file):
        """
        Imports data from an `GXIP` instrument dump file.
        """
        self._wrapper.import_dump(sys, db._wrapper, dump_file.encode())
        




    def import_grid(self, db, grid, chan):
        """
        Imports data from a grid

        **Note:**

        Data is imported to the specified channel.
        The values are interpolated at each row's X and Y
        positions.
        """
        self._wrapper.import_grid(db._wrapper, grid.encode(), chan.encode())
        




    def import_i2_x(self, db, file, line, res_data, p6, p7, p8, p9, p10, p11, p12, p13):
        """
        Imports an Interpex RESIX I2X format file to a line.

        **Note:**

        Imports a single ".I2X" file to a specified line.
        If the line does not exist, it will be created.
        """
        self._wrapper.import_i2_x(db._wrapper, file.encode(), line.encode(), res_data.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode(), p13)
        




    def import_i2_x_ex(self, db, file, line, res_data, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15):
        """
        Same as `import_i2_x`, with Zonge data imported as well.

        **Note:**

        Imports a single ".I2X" file to a specified line.
        If the line does not exist, it will be created.
        """
        self._wrapper.import_i2_x_ex(db._wrapper, file.encode(), line.encode(), res_data.encode(), p6.encode(), p7.encode(), p8.encode(), p9.encode(), p10.encode(), p11.encode(), p12.encode(), p13.encode(), p14.encode(), p15)
        




    def import_instrumentation_gdd(self, db, file):
        """
        Imports an Instrumentation GDD format file.
        """
        self._wrapper.import_instrumentation_gdd(db._wrapper, file.encode())
        




    def import_ipdata(self, db, file, chan):
        """
        Imports data in the Geosoft IPDATA format.
        """
        self._wrapper.import_ipdata(db._wrapper, file.encode(), chan.encode())
        




    def import_ipdata2(self, db, file, chan, chan2):
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
        self._wrapper.import_ipdata2(db._wrapper, file.encode(), chan.encode(), chan2.encode())
        




    def import_ipred(self, db, file, chan):
        """
        Imports data from the Geosoft IPRED format.

        **Note:**

        This import produces a limited `GXIP` data set with no Current "I",
        Voltage "Vp" or Apparent Resistivity "ResApp" values.
        """
        self._wrapper.import_ipred(db._wrapper, file.encode(), chan.encode())
        




    def import_merge_ipred(self, db, file, chan):
        """
        Imports IPRED data to an existing line.

        **Note:**

        Exits with error if the line does not exist.
        Data is merged on basis of Stn and N value.
        """
        self._wrapper.import_merge_ipred(db._wrapper, file.encode(), chan.encode())
        




    def import_sgdf(self, db, file):
        """
        Imports data from a Scintrex Geophysical Data Format file.
        """
        self._wrapper.import_sgdf(db._wrapper, file.encode())
        




    def import_topo_csv(self, db, csv):
        """
        Imports topography data from a CSV line-station file

        **Note:**

        The elevation of each point in the current database
        is interpolated from the input topography values.
        """
        self._wrapper.import_topo_csv(db._wrapper, csv.encode())
        




    def import_topo_grid(self, db, grid):
        """
        Imports topography data from a grid

        **Note:**

        The elevation of each point in the current database
        is interpolated from the input topography grid.
        """
        self._wrapper.import_topo_grid(db._wrapper, grid.encode())
        




    def import_zonge_avg(self, db, file, line, scale, mult):
        """
        Imports a Zonge AVG format file.

        **Note:**

        See `import_zonge_fld`
        """
        self._wrapper.import_zonge_avg(db._wrapper, file.encode(), line, scale, mult)
        




    def import_zonge_fld(self, db, file, scale, mult):
        """
        Imports a Zonge FLD format file.

        **Note:**

        The Zonge Line and Station numbers may not be the X or Y position
        values, and a conversion is required.
        The line direction is taken from the `GXIP` setup values.
        """
        self._wrapper.import_zonge_fld(db._wrapper, file.encode(), scale, mult)
        




    def new_xy_database(self, db, new_db, chan_vv, mask, pr_n_val):
        """
        Create a subset database using a mask channel, "N" value

        **Note:**

        A mask channel can be used to select a subset of the data.
        A single N value can also be selected (Dummy for all).
        """
        self._wrapper.new_xy_database(db._wrapper, new_db._wrapper, chan_vv._wrapper, mask.encode(), pr_n_val)
        




    def pseudo_plot(self, db, ini_file, cur_line, map):
        """
        Create pseudo-sections of a single line using a control file.

        **Note:**

        The control file is created using the IPPLTCON GX. It may then
        be modified by hand as required.
        """
        self._wrapper.pseudo_plot(db._wrapper, ini_file.encode(), cur_line.encode(), map.encode())
        




    def pseudo_plot2(self, db, ini_file, cur_line, tag, map):
        """
        Same as `pseudo_plot`, but specify a tag for grids created.

        **Note:**

        The control file is created using the IPPLTCON GX. It may then
        be modified by hand as required.
        """
        self._wrapper.pseudo_plot2(db._wrapper, ini_file.encode(), cur_line.encode(), tag.encode(), map.encode())
        




    def pseudo_plot2_dir(self, db, ini_file, cur_line, tag, map, dir):
        """
        Same as `pseudo_plot2`, but with directory specified.

        **Note:**

        The control file is created using the IPPLTCON GX. It may then
        be modified by hand as required.
        """
        self._wrapper.pseudo_plot2_dir(db._wrapper, ini_file.encode(), cur_line.encode(), tag.encode(), map.encode(), dir.encode())
        




    def ps_stack(self, db, chan, con_file, map):
        """
        Create a stacked pseudo-section plot using a control file.

        **Note:**

        The control file is created using the IPSTAKCON GX. It may then
        be modified by hand as required.
        """
        self._wrapper.ps_stack(db._wrapper, chan.encode(), con_file.encode(), map.encode())
        




    def ps_stack2(self, db, chan, con_file, type, map):
        """
        As `ps_stack`, but select section spacing option.
        """
        self._wrapper.ps_stack2(db._wrapper, chan.encode(), con_file.encode(), type, map.encode())
        




    def ps_stack2_dir(self, db, chan, con_file, type, map, dir):
        """
        Same as `pseudo_plot2`, but with directory specified.
        """
        self._wrapper.ps_stack2_dir(db._wrapper, chan.encode(), con_file.encode(), type, map.encode(), dir.encode())
        




    def qc_chan_lst(self, db, lst):
        """
        Fill a list with QC channels.

        **Note:**

        Searches for the following QC channels existing in a database:
        QC, QC_RES.
        """
        self._wrapper.qc_chan_lst(db._wrapper, lst._wrapper)
        




    def recalculate(self, db):
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
        would have to call `recalculate`, then recalculate "Topo"
        (since the X and Y values would have changed), then call
        `recalculate_z`, since "Z" values are based on "Topo" values.
        """
        self._wrapper.recalculate(db._wrapper)
        




    def recalculate_ex(self, db, recalculate_xyz):
        """
        Recalculate derived channel values, with option for including/excluding location calculations.

        **Note:**

        See `recalculate`. This version allows you to suppress the recalculation of the
        current X, Y and Z channel values from the station locations.
        """
        self._wrapper.recalculate_ex(db._wrapper, recalculate_xyz)
        




    def recalculate_z(self, db):
        """
        Recalculate Z channel values.

        **Note:**

        The "Z" channel values are calculated as follows:
        If the "Topo" value is defined, then
        Z = Topo - 0.5*N*A, where "N" is the N-spacing, and
        A is the A-spacing. If the Topography is not defined, then
        it is assumed to be equal to 0.

        .. seealso::

            `recalculate`
        """
        self._wrapper.recalculate_z(db._wrapper)
        




    def set_import_line(self, line):
        """
        Set the line name for some imports.

        **Note:**

        For some imports, no line name is derivable from the import itself.
        """
        self._wrapper.set_import_line(line.encode())
        




    def set_import_mode(self, append):
        """
        When importing data to a line, set append/overwrite mode.

        **Note:**

        By default, importing data overwrites existing data.
        Call this function before doing the import in order
        to append imported data to existing data.
        "Short" data channels will be dummied to the existing
        data length before the new data is appended.
        """
        self._wrapper.set_import_mode(append)
        




    def window(self, db, va_chan, chan, windows):
        """
        Window an `GXIP` array channel to produce a normal channel.

        **Note:**

        The array channels cannot be used directly to produce sections.
        `window` allows the user to select one or more of the windows
        and create a new channel. In time domain, if more than one channel
        is selected a weighted sum is performed, according to window widths.
        In frequency domain a simple sum is performed.
        Window List Syntax:
        """
        self._wrapper.window(db._wrapper, va_chan.encode(), chan.encode(), windows.encode())
        



    @classmethod
    def winnow_chan_list(cls, lst):
        """
        Removes obviously non-pseudo-section type channels from list.
        """
        gxapi_cy.WrapIP.winnow_chan_list(GXContext._get_tls_geo(), lst._wrapper)
        



    @classmethod
    def winnow_chan_list2(cls, lst, db):
        """
        Same as `winnow_chan_list`, but removes current X,Y,Z.
        """
        gxapi_cy.WrapIP.winnow_chan_list2(GXContext._get_tls_geo(), lst._wrapper, db._wrapper)
        




    def is_valid_line(self, db, line):
        """
        See if a given database line is registered for the `GXIP` system
        """
        ret_val = self._wrapper.is_valid_line(db._wrapper, line.encode())
        return ret_val




    def line_array_type(self, db, line):
        """
        Return the type of `GXIP` array for the input line. If necessary, first imports the specified line into the `GXIP` object
        """
        ret_val = self._wrapper.line_array_type(db._wrapper, line.encode())
        return ret_val




    def a_spacing(self, db, line):
        """
        Return the A-Spacing for the input line. If necessary, first imports the specified line into the `GXIP` object.
        """
        ret_val = self._wrapper.a_spacing(db._wrapper, line.encode())
        return ret_val




    def pldp_convention(self):
        """
        Return the user's plot point convention for pole-dipole arrays.
        """
        ret_val = self._wrapper.pldp_convention()
        return ret_val




    def get_electrode_locations_and_mask_values(self, db, line, p4, p5, p6, p7, p8):
        """
        Get unique electrodes, along with current mask info.

        **Note:**

        The mask values are determined from the first row where a given electrode is found.
        Values returned for all currently selected lines.
        """
        self._wrapper.get_electrode_locations_and_mask_values(db._wrapper, line.encode(), p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper)
        




    def get_electrode_locations_and_mask_values2(self, db, line, p4, p5, p6, p7, p8, p9):
        """
        Get unique electrodes, along with current mask info.

        **Note:**

        The mask values are determined from the first row where a given electrode is found.
        Values returned for all currently selected lines.
        """
        self._wrapper.get_electrode_locations_and_mask_values2(db._wrapper, line.encode(), p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        




    def set_electrode_mask_values(self, db, line, p4, p5, p6, p7, p8):
        """
        Set unique electrodes, along with current mask info.

        **Note:**

        Mask values are set for all included electrode locations, currently selected lines.
        """
        self._wrapper.set_electrode_mask_values(db._wrapper, line.encode(), p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper)
        




    def set_electrode_mask_values_single_qc_channel(self, db, line, p4, p5, p6, p7, p8):
        """
        Set unique electrodes, along with current mask info.

        **Note:**

        Mask values are set for all included electrode locations, currently selected lines.
        """
        self._wrapper.set_electrode_mask_values_single_qc_channel(db._wrapper, line.encode(), p4, p5, p6._wrapper, p7._wrapper, p8._wrapper)
        



    @classmethod
    def get_qc_channel(cls, db, qc_type, p3):
        """
        Get the QC channel handle, if it exists.

        **Note:**

        For `GXIP`, looks for "QC_IP", then "QC_OffTime", then "QC".
        For Resistivity, looks for "QC_Res", then "QC_OnTime" (case insensitive).
        """
        ret_val, p3.value = gxapi_cy.WrapIP.get_qc_channel(GXContext._get_tls_geo(), db._wrapper, qc_type, p3.value.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer