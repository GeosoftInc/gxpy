### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXPG import GXPG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIP(gxapi_cy.WrapIP):
    """
    GXIP class.

    This class is used in the `GXIP <geosoft.gxapi.GXIP>` System for the import, export
    and processing of Induced Polarization data.

    **Note:**

    The following defines are used in GX code but are not
    part of any functions:

    :ref:`IP_ARRAY`
    :ref:`IP_CHANNELS`
    :ref:`IP_LINES`
    """

    def __init__(self, handle=0):
        super(GXIP, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIP <geosoft.gxapi.GXIP>`
        
        :returns: A null `GXIP <geosoft.gxapi.GXIP>`
        :rtype:   GXIP
        """
        return GXIP()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Plot Jobs


    @classmethod
    def convert_ubcip_2d_to_grid(cls, file, pg, vv_x, vv_z, x, z, cx, cz, reciprocal):
        """
        Convert a UBC 2D model to a regular grid.
        
        :param file:        Output grid file name
        :param pg:          Model data
        :param vv_x:        Model cells sizes (input)
        :param vv_z:        Model cells sizes (input)
        :param x:           Top-left corner X
        :param z:           Top-left corner Z
        :param cx:          Output grid cell size in X
        :param cz:          Output grid cell size in Z
        :param reciprocal:  Output reciprocal of values (0:No, 1:Yes) for resistivity?
        :type  file:        str
        :type  pg:          GXPG
        :type  vv_x:        GXVV
        :type  vv_z:        GXVV
        :type  x:           float
        :type  z:           float
        :type  cx:          float
        :type  cz:          float
        :type  reciprocal:  int

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Uses `GXTIN <geosoft.gxapi.GXTIN>` gridding to sample the model.
        By setting the final value, a resistivity grid can be
        created from conductivity data.
        """
        gxapi_cy.WrapIP._convert_ubcip_2d_to_grid(GXContext._get_tls_geo(), file.encode(), pg, vv_x, vv_z, x, z, cx, cz, reciprocal)
        




    def create_default_job(self, ini, type):
        """
        Create a default job from scratch.
        
        :param ini:   File name of the INI file to create (forces correct suffix)
        :param type:  :ref:`IP_PLOT`
        :type  ini:   str
        :type  type:  int

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._create_default_job(ini.encode(), type)
        




    def export_ubcip3(self, db, line, chan, error_chan, obs, topo, version):
        """
        Export of `GXIP <geosoft.gxapi.GXIP>` data to UBC format.
        
        :param db:          `GXDB <geosoft.gxapi.GXDB>` object
        :param line:        Output line name
        :param chan:        Output `GXIP <geosoft.gxapi.GXIP>` channel name
        :param error_chan:  Output error channel name ("" for none)
        :param obs:         Output OBS file name
        :param topo:        Output TOPO file name
        :param version:     Version number (3 or 5)
        :type  db:          GXDB
        :type  line:        str
        :type  chan:        str
        :type  error_chan:  str
        :type  obs:         str
        :type  topo:        str
        :type  version:     float

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Outputs a ``*.DAT`` file of the survey data for use in the
        UBC 2D inversion program IPINV2D.
        Include error channel output and version-specific formatting.
        """
        self._export_ubcip3(db, line.encode(), chan.encode(), error_chan.encode(), obs.encode(), topo.encode(), version)
        



    @classmethod
    def export_ubcip_control(cls, control, n_iter, i_rest, chi_factor, obs, cond, mesh, topo, initial, ref_mod, alphas, wts):
        """
        Export a control file for using in the UBC IPINV2D program.
        
        :param control:     Output control file name
        :param n_iter:      niter
        :param i_rest:      irest
        :param chi_factor:  chifact
        :param obs:         `GXIP <geosoft.gxapi.GXIP>` obs file
        :param cond:        Conductivity file
        :param mesh:        Mesh file
        :param topo:        Topography file
        :param initial:     Initial model file
        :param ref_mod:     Reference model
        :param alphas:      Alphas
        :param wts:         Weights file
        :type  control:     str
        :type  n_iter:      int
        :type  i_rest:      int
        :type  chi_factor:  float
        :type  obs:         str
        :type  cond:        str
        :type  mesh:        str
        :type  topo:        str
        :type  initial:     str
        :type  ref_mod:     str
        :type  alphas:      str
        :type  wts:         str

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** UBC Version 3 Control file.
        Outputs a control file for use in the
        UBC 2D `GXIP <geosoft.gxapi.GXIP>` inversion program IPINV2D.
        """
        gxapi_cy.WrapIP._export_ubcip_control(GXContext._get_tls_geo(), control.encode(), n_iter, i_rest, chi_factor, obs.encode(), cond.encode(), mesh.encode(), topo.encode(), initial.encode(), ref_mod.encode(), alphas.encode(), wts.encode())
        



    @classmethod
    def export_ubcip_control_v5(cls, control, n_iter, chi_factor, obs, topo, cond_selection, cond, mesh_selection, mesh, initial_selection, initial, reference_selection, ref_cond, alphas_selection, alphas, wts):
        """
        Export a control file for using in the UBC IPINV2D program.
        
        :param control:              Output control file name
        :param n_iter:               niter
        :param chi_factor:           chifact
        :param obs:                  RES obs file
        :param topo:                 Topography file (required)
        :param cond_selection:       Conductivity type :ref:`IP_UBC_CONTROL` FILE or VALUE
        :param cond:                 Conductivity file (can be "") or value
        :param mesh_selection:       Mesh type :ref:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT
        :param mesh:                 Mesh file (can be "") or value
        :param initial_selection:    Initial model type :ref:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT
        :param initial:              Initial model file (can be "") or value
        :param reference_selection:  Reference model type :ref:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT
        :param ref_cond:             Reference model file (can be "") or value(
        :param alphas_selection:     Alphas type :ref:`IP_UBC_CONTROL` FILE, VALUE, LENGTH or DEFAULT
        :param alphas:               Alphas  file (can be ""), value or length
        :param wts:                  Weights file
        :type  control:              str
        :type  n_iter:               int
        :type  chi_factor:           float
        :type  obs:                  str
        :type  topo:                 str
        :type  cond_selection:       int
        :type  cond:                 str
        :type  mesh_selection:       int
        :type  mesh:                 str
        :type  initial_selection:    int
        :type  initial:              str
        :type  reference_selection:  int
        :type  ref_cond:             str
        :type  alphas_selection:     int
        :type  alphas:               str
        :type  wts:                  str

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** UBC Version 5 Control file.
        """
        gxapi_cy.WrapIP._export_ubcip_control_v5(GXContext._get_tls_geo(), control.encode(), n_iter, chi_factor, obs.encode(), topo.encode(), cond_selection, cond.encode(), mesh_selection, mesh.encode(), initial_selection, initial.encode(), reference_selection, ref_cond.encode(), alphas_selection, alphas.encode(), wts.encode())
        




    def export_ubc_res3(self, db, line, voltage_chan, current_chan, error_chan, obs, topo, version):
        """
        Export of `GXIP <geosoft.gxapi.GXIP>` Resistivity data to UBC format.
        
        :param db:            `GXDB <geosoft.gxapi.GXDB>` object
        :param line:          Output line name
        :param voltage_chan:  Output voltage channel name
        :param current_chan:  Output current channel name
        :param error_chan:    Output error channel name ("" for none)
        :param obs:           Output OBS file name
        :param topo:          Output TOPO file name
        :param version:       Version number (3 or 5)
        :type  db:            GXDB
        :type  line:          str
        :type  voltage_chan:  str
        :type  current_chan:  str
        :type  error_chan:    str
        :type  obs:           str
        :type  topo:          str
        :type  version:       float

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Outputs a ``*.DAT`` file of the survey data for use in the
        UBC 2D inversion program DCINV2D.
        Voltage and current channels should be in units such that
        V/I gives volts/amp (or mV/mA).
        """
        self._export_ubc_res3(db, line.encode(), voltage_chan.encode(), current_chan.encode(), error_chan.encode(), obs.encode(), topo.encode(), version)
        



    @classmethod
    def export_ubc_res_control(cls, control, n_iter, i_rest, chi_factor, obs, mesh, topo, initial, ref_cond, alphas, wts):
        """
        Export a control file for using in the UBC DCINV2D program.
        
        :param control:     Output control file name
        :param n_iter:      niter
        :param i_rest:      irest
        :param chi_factor:  chifact
        :param obs:         RES obs file
        :param mesh:        Mesh file
        :param topo:        Topography file (required)
        :param initial:     Initial model file (can be "" or "NULL")
        :param ref_cond:    Reference model conductivity
        :param alphas:      Alphas
        :param wts:         Weights file
        :type  control:     str
        :type  n_iter:      int
        :type  i_rest:      int
        :type  chi_factor:  float
        :type  obs:         str
        :type  mesh:        str
        :type  topo:        str
        :type  initial:     str
        :type  ref_cond:    float
        :type  alphas:      str
        :type  wts:         str

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** UBC Version 3.
        Outputs a control file for use in the
        UBC 2D resistivity inversion program DCINV2D.
        """
        gxapi_cy.WrapIP._export_ubc_res_control(GXContext._get_tls_geo(), control.encode(), n_iter, i_rest, chi_factor, obs.encode(), mesh.encode(), topo.encode(), initial.encode(), ref_cond, alphas.encode(), wts.encode())
        



    @classmethod
    def export_ubc_res_control_v5(cls, control, n_iter, chi_factor, obs, topo, mesh_selection, mesh, initial_selection, initial, reference_selection, ref_cond, alphas_selection, alphas, wts):
        """
        Export a control file for using in the UBC DCINV2D program.
        
        :param control:              Output control file name
        :param n_iter:               niter
        :param chi_factor:           chifact
        :param obs:                  RES obs file
        :param topo:                 Topography file (required)
        :param mesh_selection:       Mesh type :ref:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT
        :param mesh:                 Mesh file (can be "") or value
        :param initial_selection:    Initial model type :ref:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT
        :param initial:              Initial model file (can be "") or value
        :param reference_selection:  Reference model type :ref:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT
        :param ref_cond:             Reference model file (can be "") or value(
        :param alphas_selection:     Alphas type :ref:`IP_UBC_CONTROL` FILE, VALUE, LENGTH or DEFAULT
        :param alphas:               Alphas  file (can be ""), value or length
        :param wts:                  Weights file
        :type  control:              str
        :type  n_iter:               int
        :type  chi_factor:           float
        :type  obs:                  str
        :type  topo:                 str
        :type  mesh_selection:       int
        :type  mesh:                 str
        :type  initial_selection:    int
        :type  initial:              str
        :type  reference_selection:  int
        :type  ref_cond:             str
        :type  alphas_selection:     int
        :type  alphas:               str
        :type  wts:                  str

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** UBC Version 5.
        Outputs a control file for use in the
        UBC 2D resistivity inversion program DCINV2D.
        """
        gxapi_cy.WrapIP._export_ubc_res_control_v5(GXContext._get_tls_geo(), control.encode(), n_iter, chi_factor, obs.encode(), topo.encode(), mesh_selection, mesh.encode(), initial_selection, initial.encode(), reference_selection, ref_cond.encode(), alphas_selection, alphas.encode(), wts.encode())
        




    def export_data_to_ubc_3d(self, db, line_lst, locations_only, include_z, chan, error_chan, mask_chan, ip_type, comments, obs):
        """
        Export of `GXIP <geosoft.gxapi.GXIP>` data to UBC 3D `GXIP <geosoft.gxapi.GXIP>` format.
        
        :param db:              `GXDB <geosoft.gxapi.GXDB>` object
        :param line_lst:        Lines to export (Name, Symbol)
        :param locations_only:  Locations only (0: No, 1: Yes)?
        :param include_z:       Include Z values (0: No, 1: Yes)?
        :param chan:            `GXIP <geosoft.gxapi.GXIP>` channel name (can be "" if exporting locations only)
        :param error_chan:      Error channel name (can be "" if exporting locations only)
        :param mask_chan:       Mask channel name (can be "")
        :param ip_type:         IPTYPE (1: Vp, 2: Chargeability)
        :param comments:        Comments (can be "")
        :param obs:             Output OBS file name
        :type  db:              GXDB
        :type  line_lst:        GXLST
        :type  locations_only:  int
        :type  include_z:       int
        :type  chan:            str
        :type  error_chan:      str
        :type  mask_chan:       str
        :type  ip_type:         int
        :type  comments:        str
        :type  obs:             str

        .. versionadded:: 9.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Outputs a ``*.DAT`` file of the survey data for use in the
        UBC `GXIP <geosoft.gxapi.GXIP>` 3D inversion programs.
        """
        self._export_data_to_ubc_3d(db, line_lst, locations_only, include_z, chan.encode(), error_chan.encode(), mask_chan.encode(), ip_type, comments.encode(), obs.encode())
        



    @classmethod
    def import_ubc2_dmod(cls, file, type):
        """
        Import a MOD file from the UBC IPINV2D program.
        
        :param file:  UBC MOD file name to import
        :param type:  0 - CON, 1 - CHG
        :type  file:  str
        :type  type:  int

        :returns:     `GXPG <geosoft.gxapi.GXPG>` Object
        :rtype:       GXPG

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Imports the MOD file values to a `GXPG <geosoft.gxapi.GXPG>` object.
        The CON/CHG selection is necessary because the import sets
        padding values to dummies based on the type of file.
        """
        ret_val = gxapi_cy.WrapIP._import_ubc2_dmod(GXContext._get_tls_geo(), file.encode(), type)
        return GXPG(ret_val)



    @classmethod
    def import_ubc2_dmsh(cls, file, x, z, vv_x, vv_z):
        """
        Import a MSH file from the UBC IPINV2D program.
        
        :param file:  UBC MSH file to import
        :param x:     Returned origin X (top left corner)
        :param z:     Returned origin Z (top left corner)
        :param vv_x:  Cell widths  (left to right) (real)
        :param vv_z:  Cell heights (top down) (real)
        :type  file:  str
        :type  x:     float_ref
        :type  z:     float_ref
        :type  vv_x:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Imports the MSH file geometry.
        """
        x.value, z.value = gxapi_cy.WrapIP._import_ubc2_dmsh(GXContext._get_tls_geo(), file.encode(), x.value, z.value, vv_x, vv_z)
        



    @classmethod
    def import_ubc_2d_topo(cls, file, elev0, vv_x, vv_z):
        """
        Import a Topography file from the UBC IPINV2D program.
        
        :param file:   UBC Topo file to import
        :param elev0:  Returned top of mesh elevation
        :param vv_x:   Topography X values
        :param vv_z:   Topography Z values (elevations)
        :type  file:   str
        :type  elev0:  float_ref
        :type  vv_x:   GXVV
        :type  vv_z:   GXVV

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Imports the maximum elevation (top of mesh)
        as well as the topo (X, Z) values.
        """
        elev0.value = gxapi_cy.WrapIP._import_ubc_2d_topo(GXContext._get_tls_geo(), file.encode(), elev0.value, vv_x, vv_z)
        




    def open_job(self, job, type):
        """
        Open a `GXIP <geosoft.gxapi.GXIP>` plotting job
        
        :param job:   Job file name
        :param type:  Job type :ref:`IP_PLOT`
        :type  job:   str
        :type  type:  int

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._open_job(job.encode(), type)
        




    def save_job(self, job, type):
        """
        Save a `GXIP <geosoft.gxapi.GXIP>` plotting job
        
        :param job:   Job file name
        :param type:  Job type  :ref:`IP_PLOT`
        :type  job:   str
        :type  type:  int

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._save_job(job.encode(), type)
        



    @classmethod
    def trim_ubc_2d_model(cls, pg, trim_xl, trim_xr, trim_z, vv_x, vv_z, x):
        """
        Trim the padding cells from the UBC IPINV2D Model.
        
        :param pg:       Input model (unchanged)
        :param trim_xl:  Cells to remove on left
        :param trim_xr:  Cells to remove on right
        :param trim_z:   Cells to remove on the bottom
        :param vv_x:     Column widths (modified)
        :param vv_z:     Row heights (modified)
        :param x:        Top left corner X (modified)
        :type  pg:       GXPG
        :type  trim_xl:  int
        :type  trim_xr:  int
        :type  trim_z:   int
        :type  vv_x:     GXVV
        :type  vv_z:     GXVV
        :type  x:        float_ref

        :returns:        `GXPG <geosoft.gxapi.GXPG>` Object
        :rtype:          GXPG

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The cells are removed from the left, right and bottom.
        The returned `GXPG <geosoft.gxapi.GXPG>` is the trimmed version.
        The input cell size VVs are also trimmed to match,
        and the origin is updated (still upper left corner).
        """
        ret_val, x.value = gxapi_cy.WrapIP._trim_ubc_2d_model(GXContext._get_tls_geo(), pg, trim_xl, trim_xr, trim_z, vv_x, vv_z, x.value)
        return GXPG(ret_val)




    def write_distant_electrodes(self, db):
        """
        Write distant electrode locations to channels
        
        :param db:  `GXDB <geosoft.gxapi.GXDB>` object
        :type  db:  GXDB

        .. versionadded:: 6.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Writes values for ALL lines.
        """
        self._write_distant_electrodes(db)
        




    def write_distant_electrodes_lst(self, db, lst):
        """
        Write distant electrode locations to channels for a `GXLST <geosoft.gxapi.GXLST>` of lines
        
        :param db:   `GXDB <geosoft.gxapi.GXDB>` object
        :param lst:  Lines to write out
        :type  db:   GXDB
        :type  lst:  GXLST

        .. versionadded:: 6.4.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Writes values for lines in the input `GXLST <geosoft.gxapi.GXLST>`.
        """
        self._write_distant_electrodes_lst(db, lst)
        




# Miscellaneous



    def average_duplicates_qc(self, db, chan, qc_chan, out):
        """
        Average duplicate samples in a database.
        
        :param db:       Database to export from
        :param chan:     Mask or reference channel (required)
        :param qc_chan:  QC channel (can be left blank)
        :param out:      :ref:`IP_DUPLICATE`
        :type  db:       GXDB
        :type  chan:     str
        :type  qc_chan:  str
        :type  out:      int

        .. versionadded:: 7.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Averages all values with shared station and N values,
        as long as the mask channel is defined at that FID.
        Previous averaged values (IP_DATA_AVG) are overwritten according to the
        overwrite flag.
        If the QC channel is selected, only those rows of data where the QC channel
        value is "1" will be included in the average.
        """
        self._average_duplicates_qc(db, chan.encode(), qc_chan.encode(), out)
        



    @classmethod
    def create(cls):
        """
        Create `GXIP <geosoft.gxapi.GXIP>`.
        

        :returns:    `GXIP <geosoft.gxapi.GXIP>` Object
        :rtype:      GXIP

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapIP._create(GXContext._get_tls_geo())
        return GXIP(ret_val)






    def export_i2_x(self, db, file, line, res_data, ip_data, res_model, ip_model, res_synth, ip_synth, res_poly, ip_poly):
        """
        Export line(s) to an Interpex RESIX I2X format file.
        
        :param db:         Database to export from
        :param file:       Name of the file
        :param line:       Name of the line
        :param res_data:   Resistivity (data) channel
        :param ip_data:    `GXIP <geosoft.gxapi.GXIP>` (data) channel (can be "")
        :param res_model:  Image model resistivity channel (can be "")
        :param ip_model:   Image model `GXIP <geosoft.gxapi.GXIP>` channel (can be "")
        :param res_synth:  Image model synthetic resistivity channel (can be "")
        :param ip_synth:   Image model synthetic `GXIP <geosoft.gxapi.GXIP>` channel (can be "")
        :param res_poly:   Resistivity (polygon) channel (can be "")
        :param ip_poly:    `GXIP <geosoft.gxapi.GXIP>` (polygon) channel (can be "")
        :type  db:         GXDB
        :type  file:       str
        :type  line:       str
        :type  res_data:   str
        :type  ip_data:    str
        :type  res_model:  str
        :type  ip_model:   str
        :type  res_synth:  str
        :type  ip_synth:   str
        :type  res_poly:   str
        :type  ip_poly:    str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Exports a line to an ".I2X" file.
        """
        self._export_i2_x(db, file.encode(), line.encode(), res_data.encode(), ip_data.encode(), res_model.encode(), ip_model.encode(), res_synth.encode(), ip_synth.encode(), res_poly.encode(), ip_poly.encode())
        




    def export_ipdata(self, db, chan, title):
        """
        Exports data in the Geosoft IPDATA format.
        
        :param db:     Database to export from
        :param chan:   Channel to export
        :param title:  Title for IPDATA files
        :type  db:     GXDB
        :type  chan:   str
        :type  title:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._export_ipdata(db, chan.encode(), title.encode())
        




    def export_ipdata_dir(self, db, chan, title, dir):
        """
        Exports data in the Geosoft IPDATA format in the specified directory
        
        :param db:     Database to export from
        :param chan:   Channel to export
        :param title:  Title for IPDATA files
        :param dir:    Directory for IPDATA files
        :type  db:     GXDB
        :type  chan:   str
        :type  title:  str
        :type  dir:    str

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._export_ipdata_dir(db, chan.encode(), title.encode(), dir.encode())
        




    def export_ipred(self, db, title, chan, suffix, filter, wts, stn1, stn2, max_n):
        """
        Exports pseudo-section in the Geosoft IPRED format.
        
        :param db:      Database to export from
        :param title:   Title for first line of file
        :param chan:    Channel to process
        :param suffix:  File suffix (type)
        :param filter:  :ref:`IP_FILTER`
        :param wts:     The Fraser Filter weights
        :param stn1:    First Station position (`rDUMMY <geosoft.gxapi.rDUMMY>` for default)
        :param stn2:    Last Station position  (`rDUMMY <geosoft.gxapi.rDUMMY>` for default)
        :param max_n:   Maximum n spacing
        :type  db:      GXDB
        :type  title:   str
        :type  chan:    str
        :type  suffix:  str
        :type  filter:  int
        :type  wts:     str
        :type  stn1:    float
        :type  stn2:    float
        :type  max_n:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The Fraser Filter weights apply to each N expansion above,
        and are listed as w1,w2,w3,...   Unspecified values beyond
        the list's end are set to 1.0.
        """
        self._export_ipred(db, title.encode(), chan.encode(), suffix.encode(), filter, wts.encode(), stn1, stn2, max_n)
        




    def export_ipred_dir(self, db, title, chan, suffix, filter, wts, stn1, stn2, max_n, dir):
        """
        Exports pseudo-section in the Geosoft IPRED format in the specified directory
        
        :param db:      Database to export from
        :param title:   Title for first line of file
        :param chan:    Channel to process
        :param suffix:  File suffix (type)
        :param filter:  :ref:`IP_FILTER`
        :param wts:     The Fraser Filter weights
        :param stn1:    First Station position (`rDUMMY <geosoft.gxapi.rDUMMY>` for default)
        :param stn2:    Last Station position  (`rDUMMY <geosoft.gxapi.rDUMMY>` for default)
        :param max_n:   Maximum n spacing
        :param dir:     Directory to export to
        :type  db:      GXDB
        :type  title:   str
        :type  chan:    str
        :type  suffix:  str
        :type  filter:  int
        :type  wts:     str
        :type  stn1:    float
        :type  stn2:    float
        :type  max_n:   int
        :type  dir:     str

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The Fraser Filter weights apply to each N expansion above,
        and are listed as w1,w2,w3,...   Unspecified values beyond
        the list's end are set to 1.0.
        """
        self._export_ipred_dir(db, title.encode(), chan.encode(), suffix.encode(), filter, wts.encode(), stn1, stn2, max_n, dir.encode())
        




    def export_line_ipdata(self, db, line, chan, title):
        """
        Exports one line of data in the Geosoft IPDATA format.
        
        :param db:     Database to export from
        :param line:   Line to export
        :param chan:   Channel to export
        :param title:  Title for IPDATA files
        :type  db:     GXDB
        :type  line:   str
        :type  chan:   str
        :type  title:  str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._export_line_ipdata(db, line.encode(), chan.encode(), title.encode())
        




    def export_sgdf(self, db, file, chan, chan2):
        """
        Exports data to a Scintrex Geophysical Data Format file.
        
        :param db:     Database to export from
        :param file:   SGDF file to create
        :param chan:   Time Domain channel or Frequency Amplitude Channel
        :param chan2:  Frequency Domain Phase channel (optional)
        :type  db:     GXDB
        :type  file:   str
        :type  chan:   str
        :type  chan2:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._export_sgdf(db, file.encode(), chan.encode(), chan2.encode())
        




    def get_n_value_lst(self, db, lst):
        """
        Fill a list with unique N values in selected lines.
        
        :param db:   Database
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object
        :type  db:   GXDB
        :type  lst:  GXLST

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._get_n_value_lst(db, lst)
        




    def get_topo_line(self, db, line, x_min, x_max, x_inc, vv):
        """
        Get topography values for a line.
        
        :param db:     Database to import data to
        :param line:   Line name
        :param x_min:  Starting "X" (station) value (`rDUMMY <geosoft.gxapi.rDUMMY>` for default)
        :param x_max:  Ending "X" (station) value (`rDUMMY <geosoft.gxapi.rDUMMY>` for default)
        :param x_inc:  "X" increment along the line (`rDUMMY <geosoft.gxapi.rDUMMY>` for default = half "A" separation)
        :param vv:     Returned topography values
        :type  db:     GXDB
        :type  line:   str
        :type  x_min:  float
        :type  x_max:  float
        :type  x_inc:  float
        :type  vv:     GXVV

        .. versionadded:: 6.4.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If topography info is available, returns values calculated for
        the input line. If no topography is available, returned values
        will be dummies. Values between actual data are interpolated using
        the Akima spline. Ends are extrapolated using the end data points.
        """
        self._get_topo_line(db, line.encode(), x_min, x_max, x_inc, vv)
        




    def get_chan_domain(self, db, chan):
        """
        Is this channel registered as a Time or Frequency domain channel?
        
        :param db:    Database
        :param chan:  Channel to check
        :type  db:    GXDB
        :type  chan:  str

        :returns:     :ref:`IP_DOMAIN`
        :rtype:       int

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._get_chan_domain(db, chan.encode())
        return ret_val



    @classmethod
    def get_chan_label(cls, chan, label, units):
        """
        Get the default label and units for a given channel.
        
        :param chan:   Input channel
        :param label:  Returned label
        :param units:  Returned units
        :type  chan:   str
        :type  label:  str_ref
        :type  units:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        label.value, units.value = gxapi_cy.WrapIP._get_chan_label(GXContext._get_tls_geo(), chan.encode(), label.value.encode(), units.value.encode())
        




    def get_channel_info(self, db, chan, domain, delay, n_windows, vv):
        """
        Time Windows or Frequency info from a channel.
        
        :param db:         Database
        :param chan:       Channel to check
        :param domain:     :ref:`IP_DOMAIN`
        :param delay:      Delay or Base Frequency
        :param n_windows:  Number of time windows or frequencies
        :param vv:         Time windows or frequencies
        :type  db:         GXDB
        :type  chan:       str
        :type  domain:     int_ref
        :type  delay:      float_ref
        :type  n_windows:  int_ref
        :type  vv:         GXVV

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        domain.value, delay.value, n_windows.value = self._get_channel_info(db, chan.encode(), domain.value, delay.value, n_windows.value, vv)
        




    def set_channel_info(self, db, chan, domain, delay, n_windows, vv):
        """
        Set Time Windows or Frequency info for a channel.
        
        :param db:         Database
        :param chan:       Channel to check
        :param domain:     :ref:`IP_DOMAIN`
        :param delay:      Delay or Base Frequency
        :param n_windows:  Number of time windows or frequencies
        :param vv:         Time windows or frequencies
        :type  db:         GXDB
        :type  chan:       str
        :type  domain:     int
        :type  delay:      float
        :type  n_windows:  int
        :type  vv:         GXVV

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._set_channel_info(db, chan.encode(), domain, delay, n_windows, vv)
        




    def import_dump(self, ip_sys, db, dump_file):
        """
        Imports data from an `GXIP <geosoft.gxapi.GXIP>` instrument dump file.
        
        :param ip_sys:     :ref:`IP_SYS`
        :param db:         `GXDB <geosoft.gxapi.GXDB>` Handle
        :param dump_file:  Dump file name
        :type  ip_sys:     int
        :type  db:         GXDB
        :type  dump_file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._import_dump(ip_sys, db, dump_file.encode())
        




    def import_grid(self, db, grid, chan):
        """
        Imports data from a grid
        
        :param db:    Database to import data to
        :param grid:  The name of the grid file, with decorations
        :param chan:  The name of the channel to import to
        :type  db:    GXDB
        :type  grid:  str
        :type  chan:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Data is imported to the specified channel.
        The values are interpolated at each row's X and Y
        positions.
        """
        self._import_grid(db, grid.encode(), chan.encode())
        




    def import_i2_x(self, db, file, line, res_data, ip_data, res_model, ip_model, res_synth, ip_synth, res_poly, ip_poly, mode):
        """
        Imports an Interpex RESIX I2X format file to a line.
        
        :param db:         Database to import to
        :param file:       Name of file to import
        :param line:       Line to import to
        :param res_data:   Resistivity (data) channel
        :param ip_data:    `GXIP <geosoft.gxapi.GXIP>` (data) channel (can be "")
        :param res_model:  Image model resistivity channel (can be "")
        :param ip_model:   Image model `GXIP <geosoft.gxapi.GXIP>` channel (can be "")
        :param res_synth:  Image model synthetic resistivity channel (can be "")
        :param ip_synth:   Image model synthetic `GXIP <geosoft.gxapi.GXIP>` channel (can be "")
        :param res_poly:   Resistivity (polygon) channel (can be "")
        :param ip_poly:    `GXIP <geosoft.gxapi.GXIP>` (polygon) channel (can be "")
        :param mode:       :ref:`IP_I2XIMPMODE`
        :type  db:         GXDB
        :type  file:       str
        :type  line:       str
        :type  res_data:   str
        :type  ip_data:    str
        :type  res_model:  str
        :type  ip_model:   str
        :type  res_synth:  str
        :type  ip_synth:   str
        :type  res_poly:   str
        :type  ip_poly:    str
        :type  mode:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Imports a single ".I2X" file to a specified line.
        If the line does not exist, it will be created.
        """
        self._import_i2_x(db, file.encode(), line.encode(), res_data.encode(), ip_data.encode(), res_model.encode(), ip_model.encode(), res_synth.encode(), ip_synth.encode(), res_poly.encode(), ip_poly.encode(), mode)
        




    def import_i2_x_ex(self, db, file, line, res_data, ip_data, res_model, ip_model, res_synth, ip_synth, res_poly, ip_poly, res_zonge, ip_zonge, mode):
        """
        Same as `import_i2_x <geosoft.gxapi.GXIP.import_i2_x>`, with Zonge data imported as well.
        
        :param db:         Database to import to
        :param file:       Name of file to import
        :param line:       Line to import to
        :param res_data:   Resistivity (data) channel
        :param ip_data:    `GXIP <geosoft.gxapi.GXIP>` (data) channel (can be "")
        :param res_model:  Image model resistivity channel (can be "")
        :param ip_model:   Image model `GXIP <geosoft.gxapi.GXIP>` channel (can be "")
        :param res_synth:  Image model synthetic resistivity channel (can be "")
        :param ip_synth:   Image model synthetic `GXIP <geosoft.gxapi.GXIP>` channel (can be "")
        :param res_poly:   Resistivity (polygon) channel (can be "")
        :param ip_poly:    `GXIP <geosoft.gxapi.GXIP>` (polygon) channel (can be "")
        :param res_zonge:  Zonge Resistivity channel (can be "")
        :param ip_zonge:   Zonge `GXIP <geosoft.gxapi.GXIP>` channel (can be "")
        :param mode:       :ref:`IP_I2XIMPMODE`
        :type  db:         GXDB
        :type  file:       str
        :type  line:       str
        :type  res_data:   str
        :type  ip_data:    str
        :type  res_model:  str
        :type  ip_model:   str
        :type  res_synth:  str
        :type  ip_synth:   str
        :type  res_poly:   str
        :type  ip_poly:    str
        :type  res_zonge:  str
        :type  ip_zonge:   str
        :type  mode:       int

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Imports a single ".I2X" file to a specified line.
        If the line does not exist, it will be created.
        """
        self._import_i2_x_ex(db, file.encode(), line.encode(), res_data.encode(), ip_data.encode(), res_model.encode(), ip_model.encode(), res_synth.encode(), ip_synth.encode(), res_poly.encode(), ip_poly.encode(), res_zonge.encode(), ip_zonge.encode(), mode)
        




    def import_instrumentation_gdd(self, db, file):
        """
        Imports an Instrumentation GDD format file.
        
        :param db:    Database to import to
        :param file:  GDD file name
        :type  db:    GXDB
        :type  file:  str

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._import_instrumentation_gdd(db, file.encode())
        




    def import_ipdata(self, db, file, chan):
        """
        Imports data in the Geosoft IPDATA format.
        
        :param db:    Database to import to
        :param file:  IPDATA file name
        :param chan:  Channel to import to
        :type  db:    GXDB
        :type  file:  str
        :type  chan:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._import_ipdata(db, file.encode(), chan.encode())
        




    def import_ipdata2(self, db, file, chan, chan2):
        """
        Imports data in the Geosoft IPDATA format - up to two arrays.
        
        :param db:     Database to import to
        :param file:   IPDATA file name
        :param chan:   Channel to import to (default is "`GXIP <geosoft.gxapi.GXIP>`")
        :param chan2:  (optional) Second channel to import to
        :type  db:     GXDB
        :type  file:   str
        :type  chan:   str
        :type  chan2:  str

        .. versionadded:: 5.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The second channel may be specified for frequency domain data sets
        with two array channels; e.g. amplitude and phase, or real and
        imaginary parts. If the second channel is specified, and no
        time or frequncy information is specified in the header (using
        the T= or F= fields) then the import is assumed to be frequency
        domain.
        """
        self._import_ipdata2(db, file.encode(), chan.encode(), chan2.encode())
        




    def import_ipred(self, db, file, chan):
        """
        Imports data from the Geosoft IPRED format.
        
        :param db:    Database to import to
        :param file:  File to import from
        :param chan:  Channel to import
        :type  db:    GXDB
        :type  file:  str
        :type  chan:  str

        .. versionadded:: 5.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** This import produces a limited `GXIP <geosoft.gxapi.GXIP>` data set with no Current "I",
        Voltage "Vp" or Apparent Resistivity "ResApp" values.
        """
        self._import_ipred(db, file.encode(), chan.encode())
        




    def import_merge_ipred(self, db, file, chan):
        """
        Imports IPRED data to an existing line.
        
        :param db:    Database to import to
        :param file:  File to import from
        :param chan:  Channel to import
        :type  db:    GXDB
        :type  file:  str
        :type  chan:  str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Exits with error if the line does not exist.
        Data is merged on basis of Stn and N value.
        """
        self._import_merge_ipred(db, file.encode(), chan.encode())
        




    def import_sgdf(self, db, file):
        """
        Imports data from a Scintrex Geophysical Data Format file.
        
        :param db:    Database to import to
        :param file:  SGDF file name
        :type  db:    GXDB
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._import_sgdf(db, file.encode())
        




    def import_topo_csv(self, db, csv):
        """
        Imports topography data from a CSV line-station file
        
        :param db:   Database to calculate topography for
        :param csv:  The name of CSV file
        :type  db:   GXDB
        :type  csv:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The elevation of each point in the current database
        is interpolated from the input topography values.
        """
        self._import_topo_csv(db, csv.encode())
        




    def import_topo_grid(self, db, grid):
        """
        Imports topography data from a grid
        
        :param db:    Database to calculate topography for
        :param grid:  The name of the grid file, with decorations
        :type  db:    GXDB
        :type  grid:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The elevation of each point in the current database
        is interpolated from the input topography grid.
        """
        self._import_topo_grid(db, grid.encode())
        




    def import_zonge_avg(self, db, file, line, scale, mult):
        """
        Imports a Zonge AVG format file.
        
        :param db:     Database to import to
        :param file:   FLD file name
        :param line:   Line number (will be scaled if applicable)
        :param scale:  :ref:`IP_STNSCALE`
        :param mult:   Line, station multiplier (for `IP_STNSCALE_VALUE <geosoft.gxapi.IP_STNSCALE_VALUE>`)
        :type  db:     GXDB
        :type  file:   str
        :type  line:   float
        :type  scale:  int
        :type  mult:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** See `import_zonge_fld <geosoft.gxapi.GXIP.import_zonge_fld>`
        """
        self._import_zonge_avg(db, file.encode(), line, scale, mult)
        




    def import_zonge_fld(self, db, file, scale, mult):
        """
        Imports a Zonge FLD format file.
        
        :param db:     Database to import to
        :param file:   FLD file name
        :param scale:  :ref:`IP_STNSCALE`
        :param mult:   Line, station multiplier (for `IP_STNSCALE_VALUE <geosoft.gxapi.IP_STNSCALE_VALUE>`)
        :type  db:     GXDB
        :type  file:   str
        :type  scale:  int
        :type  mult:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The Zonge Line and Station numbers may not be the X or Y position
        values, and a conversion is required.
        The line direction is taken from the `GXIP <geosoft.gxapi.GXIP>` setup values.
        """
        self._import_zonge_fld(db, file.encode(), scale, mult)
        




    def new_xy_database(self, db, new_db, chan_vv, mask, pr_n_val):
        """
        Create a subset database using a mask channel, "N" value
        
        :param db:        `GXDB <geosoft.gxapi.GXDB>` object
        :param new_db:    New `GXDB <geosoft.gxapi.GXDB>` object
        :param chan_vv:   Channel list
        :param mask:      Mask channel
        :param pr_n_val:  "N" Value
        :type  db:        GXDB
        :type  new_db:    GXDB
        :type  chan_vv:   GXVV
        :type  mask:      str
        :type  pr_n_val:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** A mask channel can be used to select a subset of the data.
        A single N value can also be selected (Dummy for all).
        """
        self._new_xy_database(db, new_db, chan_vv, mask.encode(), pr_n_val)
        




    def pseudo_plot(self, db, ini_file, cur_line, map):
        """
        Create pseudo-sections of a single line using a control file.
        
        :param db:        Database
        :param ini_file:  "IPPLOT" INI file name
        :param cur_line:  Current line name
        :param map:       Map name to create
        :type  db:        GXDB
        :type  ini_file:  str
        :type  cur_line:  str
        :type  map:       str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The control file is created using the IPPLTCON GX. It may then
        be modified by hand as required.
        """
        self._pseudo_plot(db, ini_file.encode(), cur_line.encode(), map.encode())
        




    def pseudo_plot2(self, db, ini_file, cur_line, tag, map):
        """
        Same as `pseudo_plot <geosoft.gxapi.GXIP.pseudo_plot>`, but specify a tag for grids created.
        
        :param db:        Database
        :param ini_file:  "IPPLOT" INI file name
        :param cur_line:  Current line name
        :param tag:       Tag for created grids
        :param map:       Map name to create
        :type  db:        GXDB
        :type  ini_file:  str
        :type  cur_line:  str
        :type  tag:       str
        :type  map:       str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The control file is created using the IPPLTCON GX. It may then
        be modified by hand as required.
        """
        self._pseudo_plot2(db, ini_file.encode(), cur_line.encode(), tag.encode(), map.encode())
        




    def pseudo_plot2_dir(self, db, ini_file, cur_line, tag, map, dir):
        """
        Same as `pseudo_plot2 <geosoft.gxapi.GXIP.pseudo_plot2>`, but with directory specified.
        
        :param db:        Database
        :param ini_file:  "IPPLOT" INI file name
        :param cur_line:  Current line name
        :param tag:       Tag for created grids
        :param map:       Map name to create
        :param dir:       Directory to create files
        :type  db:        GXDB
        :type  ini_file:  str
        :type  cur_line:  str
        :type  tag:       str
        :type  map:       str
        :type  dir:       str

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The control file is created using the IPPLTCON GX. It may then
        be modified by hand as required.
        """
        self._pseudo_plot2_dir(db, ini_file.encode(), cur_line.encode(), tag.encode(), map.encode(), dir.encode())
        




    def ps_stack(self, db, chan, con_file, map):
        """
        Create a stacked pseudo-section plot using a control file.
        
        :param db:        `GXDB <geosoft.gxapi.GXDB>` object
        :param chan:      Channel to plot
        :param con_file:  "IPPLOT" INI file name
        :param map:       Map name to create
        :type  db:        GXDB
        :type  chan:      str
        :type  con_file:  str
        :type  map:       str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The control file is created using the IPSTAKCON GX. It may then
        be modified by hand as required.
        """
        self._ps_stack(db, chan.encode(), con_file.encode(), map.encode())
        




    def ps_stack2(self, db, chan, con_file, type, map):
        """
        As `ps_stack <geosoft.gxapi.GXIP.ps_stack>`, but select section spacing option.
        
        :param db:        `GXDB <geosoft.gxapi.GXDB>` object
        :param chan:      Channel to plot
        :param con_file:  "IPPLOT" INI file name
        :param type:      :ref:`IP_STACK_TYPE`
        :param map:       Map name to create
        :type  db:        GXDB
        :type  chan:      str
        :type  con_file:  str
        :type  type:      int
        :type  map:       str

        .. versionadded:: 5.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._ps_stack2(db, chan.encode(), con_file.encode(), type, map.encode())
        




    def ps_stack2_dir(self, db, chan, con_file, type, map, dir):
        """
        Same as `pseudo_plot2 <geosoft.gxapi.GXIP.pseudo_plot2>`, but with directory specified.
        
        :param db:        `GXDB <geosoft.gxapi.GXDB>` object
        :param chan:      Channel to plot
        :param con_file:  "IPPLOT" INI file name
        :param type:      :ref:`IP_STACK_TYPE`
        :param map:       Map name to create
        :param dir:       Directory to create files
        :type  db:        GXDB
        :type  chan:      str
        :type  con_file:  str
        :type  type:      int
        :type  map:       str
        :type  dir:       str

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._ps_stack2_dir(db, chan.encode(), con_file.encode(), type, map.encode(), dir.encode())
        




    def qc_chan_lst(self, db, lst):
        """
        Fill a list with QC channels.
        
        :param db:   Database
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object
        :type  db:   GXDB
        :type  lst:  GXLST

        .. versionadded:: 7.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Searches for the following QC channels existing in a database:
        QC, QC_RES.
        """
        self._qc_chan_lst(db, lst)
        




    def recalculate(self, db):
        """
        Recalculate derived channel values.
        
        :param db:  Database
        :type  db:  GXDB

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** This function recalculates "derived" channel values from
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
        would have to call `recalculate <geosoft.gxapi.GXIP.recalculate>`, then recalculate "Topo"
        (since the X and Y values would have changed), then call
        `recalculate_z <geosoft.gxapi.GXIP.recalculate_z>`, since "Z" values are based on "Topo" values.
        """
        self._recalculate(db)
        




    def recalculate_ex(self, db, recalculate_xyz):
        """
        Recalculate derived channel values, with option for including/excluding location calculations.
        
        :param db:               Database
        :param recalculate_xyz:  Recalculate XYZ locations (TRUE or FALSE)?
        :type  db:               GXDB
        :type  recalculate_xyz:  int

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** See `recalculate <geosoft.gxapi.GXIP.recalculate>`. This version allows you to suppress the recalculation of the
        current X, Y and Z channel values from the station locations.
        """
        self._recalculate_ex(db, recalculate_xyz)
        




    def recalculate_z(self, db):
        """
        Recalculate Z channel values.
        
        :param db:  Database
        :type  db:  GXDB

        .. versionadded:: 5.1.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The "Z" channel values are calculated as follows:
        If the "Topo" value is defined, then
        Z = Topo - 0.5*N*A, where "N" is the N-spacing, and
        A is the A-spacing. If the Topography is not defined, then
        it is assumed to be equal to 0.

        .. seealso::

            `recalculate <geosoft.gxapi.GXIP.recalculate>`
        """
        self._recalculate_z(db)
        




    def set_import_line(self, line):
        """
        Set the line name for some imports.
        
        :param line:  Line name
        :type  line:  str

        .. versionadded:: 9.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** For some imports, no line name is derivable from the import itself.
        """
        self._set_import_line(line.encode())
        




    def set_import_mode(self, append):
        """
        When importing data to a line, set append/overwrite mode.
        
        :param append:  0: Overwrite, 1: Append
        :type  append:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** By default, importing data overwrites existing data.
        Call this function before doing the import in order
        to append imported data to existing data.
        "Short" data channels will be dummied to the existing
        data length before the new data is appended.
        """
        self._set_import_mode(append)
        




    def window(self, db, va_chan, chan, windows):
        """
        Window an `GXIP <geosoft.gxapi.GXIP>` array channel to produce a normal channel.
        
        :param db:       `GXDB <geosoft.gxapi.GXDB>` object
        :param va_chan:  `GXVA <geosoft.gxapi.GXVA>` channel to use
        :param chan:     New channel
        :param windows:  Window list
        :type  db:       GXDB
        :type  va_chan:  str
        :type  chan:     str
        :type  windows:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The array channels cannot be used directly to produce sections.
        `window <geosoft.gxapi.GXIP.window>` allows the user to select one or more of the windows
        and create a new channel. In time domain, if more than one channel
        is selected a weighted sum is performed, according to window widths.
        In frequency domain a simple sum is performed.
        Window List Syntax:
        """
        self._window(db, va_chan.encode(), chan.encode(), windows.encode())
        



    @classmethod
    def winnow_chan_list(cls, lst):
        """
        Removes obviously non-pseudo-section type channels from list.
        
        :param lst:  List of channels
        :type  lst:  GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapIP._winnow_chan_list(GXContext._get_tls_geo(), lst)
        



    @classmethod
    def winnow_chan_list2(cls, lst, db):
        """
        Same as `winnow_chan_list <geosoft.gxapi.GXIP.winnow_chan_list>`, but removes current X,Y,Z.
        
        :param lst:  List of channels
        :param db:   Database
        :type  lst:  GXLST
        :type  db:   GXDB

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapIP._winnow_chan_list2(GXContext._get_tls_geo(), lst, db)
        




    def is_valid_line(self, db, line):
        """
        See if a given database line is registered for the `GXIP <geosoft.gxapi.GXIP>` system
        
        :param db:    Database
        :param line:  Line name
        :type  db:    GXDB
        :type  line:  str

        :returns:     1 if the line is a valid `GXIP <geosoft.gxapi.GXIP>` line, 0 if not
        :rtype:       int

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._is_valid_line(db, line.encode())
        return ret_val




    def line_array_type(self, db, line):
        """
        Return the type of `GXIP <geosoft.gxapi.GXIP>` array for the input line. If necessary, first imports the specified line into the `GXIP <geosoft.gxapi.GXIP>` object
        
        :param db:    Database
        :param line:  Line name
        :type  db:    GXDB
        :type  line:  str

        :returns:     :ref:`IP_ARRAY`
        :rtype:       int

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._line_array_type(db, line.encode())
        return ret_val




    def a_spacing(self, db, line):
        """
        Return the A-Spacing for the input line. If necessary, first imports the specified line into the `GXIP <geosoft.gxapi.GXIP>` object.
        
        :param db:    Database
        :param line:  Line name
        :type  db:    GXDB
        :type  line:  str

        :returns:     The A-Spacing value. If there are multiple A-Spacings, the base or smallest value.
                      				 This value could be `rDUMMY <geosoft.gxapi.rDUMMY>` for some arrays (such as 3D) where no A-Spacing is explicitly defined.
        :rtype:       float

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._a_spacing(db, line.encode())
        return ret_val




    def pldp_convention(self):
        """
        Return the user's plot point convention for pole-dipole arrays.
        

        :returns:    The user's PLDP plot point convention :ref:`IP_PLDP_CONV`
        :rtype:      int

        .. versionadded:: 8.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._pldp_convention()
        return ret_val




    def get_electrode_locations_and_mask_values(self, db, line, tx_rx, v_vx, v_vy, v_vm1, v_vm2):
        """
        Get unique electrodes, along with current mask info.
        
        :param db:     `GXDB <geosoft.gxapi.GXDB>` object
        :param line:   Line name ("" for all selected lines)
        :param tx_rx:  Electrode type. 0:Tx, 1:Rx
        :param v_vx:   X locations
        :param v_vy:   Y locations
        :param v_vm1:  `GXIP <geosoft.gxapi.GXIP>` QC channel values ("QC" or "QC_IP")
        :param v_vm2:  Resistivity QC channel values ("QC_RES")
        :type  db:     GXDB
        :type  line:   str
        :type  tx_rx:  int
        :type  v_vx:   GXVV
        :type  v_vy:   GXVV
        :type  v_vm1:  GXVV
        :type  v_vm2:  GXVV

        .. versionadded:: 9.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The mask values are determined from the first row where a given electrode is found.
        Values returned for all currently selected lines.
        """
        self._get_electrode_locations_and_mask_values(db, line.encode(), tx_rx, v_vx, v_vy, v_vm1, v_vm2)
        




    def get_electrode_locations_and_mask_values2(self, db, line, tx_rx, v_vx, v_vy, v_vm1, v_vm2, v_vlines):
        """
        Get unique electrodes, along with current mask info.
        
        :param db:        `GXDB <geosoft.gxapi.GXDB>` object
        :param line:      Line name ("" for all selected lines)
        :param tx_rx:     Electrode type. 0:Tx, 1:Rx
        :param v_vx:      X locations
        :param v_vy:      Y locations
        :param v_vm1:     `GXIP <geosoft.gxapi.GXIP>` QC channel values ("QC" or "QC_IP")
        :param v_vm2:     Resistivity QC channel values ("QC_RES")
        :param v_vlines:  Line symbol values (`GS_INT <geosoft.gxapi.GS_INT>`)
        :type  db:        GXDB
        :type  line:      str
        :type  tx_rx:     int
        :type  v_vx:      GXVV
        :type  v_vy:      GXVV
        :type  v_vm1:     GXVV
        :type  v_vm2:     GXVV
        :type  v_vlines:  GXVV

        .. versionadded:: 9.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The mask values are determined from the first row where a given electrode is found.
        Values returned for all currently selected lines.
        """
        self._get_electrode_locations_and_mask_values2(db, line.encode(), tx_rx, v_vx, v_vy, v_vm1, v_vm2, v_vlines)
        




    def set_electrode_mask_values(self, db, line, tx_rx, v_vx, v_vy, v_vm1, v_vm2):
        """
        Set unique electrodes, along with current mask info.
        
        :param db:     `GXDB <geosoft.gxapi.GXDB>` object
        :param line:   Line name ("" for all selected lines)
        :param tx_rx:  Electrode type. 0:Tx, 1:Rx
        :param v_vx:   X locations
        :param v_vy:   Y locations
        :param v_vm1:  `GXIP <geosoft.gxapi.GXIP>` QC channel values ("QC" or "QC_IP")
        :param v_vm2:  Resistivity QC channel values ("QC_RES")
        :type  db:     GXDB
        :type  line:   str
        :type  tx_rx:  int
        :type  v_vx:   GXVV
        :type  v_vy:   GXVV
        :type  v_vm1:  GXVV
        :type  v_vm2:  GXVV

        .. versionadded:: 9.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Mask values are set for all included electrode locations, currently selected lines.
        """
        self._set_electrode_mask_values(db, line.encode(), tx_rx, v_vx, v_vy, v_vm1, v_vm2)
        




    def set_electrode_mask_values_single_qc_channel(self, db, line, tx_rx, qc_type, v_vx, v_vy, v_vm):
        """
        Set unique electrodes, along with current mask info.
        
        :param db:       `GXDB <geosoft.gxapi.GXDB>` object
        :param line:     Line name ("" for all selected lines)
        :param tx_rx:    Electrode type. 0:Tx, 1:Rx
        :param qc_type:  QC channel type.  :ref:`IP_QCTYPE`
        :param v_vx:     X locations
        :param v_vy:     Y locations
        :param v_vm:     QC channel values ("QC")
        :type  db:       GXDB
        :type  line:     str
        :type  tx_rx:    int
        :type  qc_type:  int
        :type  v_vx:     GXVV
        :type  v_vy:     GXVV
        :type  v_vm:     GXVV

        .. versionadded:: 9.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Mask values are set for all included electrode locations, currently selected lines.
        """
        self._set_electrode_mask_values_single_qc_channel(db, line.encode(), tx_rx, qc_type, v_vx, v_vy, v_vm)
        



    @classmethod
    def get_qc_channel(cls, db, qc_type, chan):
        """
        Get the QC channel handle, if it exists.
        
        :param db:       `GXDB <geosoft.gxapi.GXDB>` object
        :param qc_type:  QC channel type.  :ref:`IP_QCTYPE`
        :param chan:     String to place name into
        :type  db:       GXDB
        :type  qc_type:  int
        :type  chan:     str_ref

        :returns:        Channel handle,  `NULLSYMB <geosoft.gxapi.NULLSYMB>` if not found
        :rtype:          int

        .. versionadded:: 9.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** For `GXIP <geosoft.gxapi.GXIP>`, looks for "QC_IP", then "QC_OffTime", then "QC".
        For Resistivity, looks for "QC_Res", then "QC_OnTime" (case insensitive).
        """
        ret_val, chan.value = gxapi_cy.WrapIP._get_qc_channel(GXContext._get_tls_geo(), db, qc_type, chan.value.encode())
        return ret_val



    @classmethod
    def locate_contributing_electrodes(cls, db, map, rx1x, rx1y, rx2x, rx2y, tx1x, tx1y, tx2x, tx2y, sym_size):
        """
        Locate on a map electrodes selected in a database row.
        
        :param db:        `GXDB <geosoft.gxapi.GXDB>` object
        :param map:       The current map
        :param rx1x:      Rx1 X channel
        :param rx1y:      Rx1 Y channel
        :param rx2x:      Rx2 X channel
        :param rx2y:      Rx2 Y channel
        :param tx1x:      Tx1 X channel
        :param tx1y:      Tx1 Y channel
        :param tx2x:      Tx2 X channel
        :param tx2y:      Tx2 Y channel
        :param sym_size:  Symbol size (mm)
        :type  db:        GXDB
        :type  map:       str
        :type  rx1x:      str
        :type  rx1y:      str
        :type  rx2x:      str
        :type  rx2y:      str
        :type  tx1x:      str
        :type  tx1y:      str
        :type  tx2x:      str
        :type  tx2y:      str
        :type  sym_size:  float

        .. versionadded:: 9.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Sets up an EXT object in the database that captures row/line change events and plots the
        electrodes for the selected row on an accompanying map.
        The EXT object is removed by running LaunchRemoveContributingElectrodesEXTTool_IPGUI.
        This EXT is not serialized, so it is also removed if the database is closed (since
        this is not the normal behaviour expected from a database).
        """
        gxapi_cy.WrapIP._locate_contributing_electrodes(GXContext._get_tls_geo(), db, map.encode(), rx1x.encode(), rx1y.encode(), rx2x.encode(), rx2y.encode(), tx1x.encode(), tx1y.encode(), tx2x.encode(), tx2y.encode(), sym_size)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer