### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXDB import GXDB
from .GXMAP import GXMAP
from .GXREG import GXREG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDH(gxapi_cy.WrapDH):
    """
    GXDH class.

    This class is used for importing and interacting with Drill Hole
    data files. For detailed information on Drill Hole data,
    see the documentation for Wholeplot.

    **Note:**

    The `GXDH <geosoft.gxapi.GXDH>` class has some defines not used by any functions.
        `DH_DEFINE_PLAN <geosoft.gxapi.DH_DEFINE_PLAN>`
        :ref:`DH_DEFINE_SECT`
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDH <geosoft.gxapi.GXDH>`
        
        :returns: A null `GXDH <geosoft.gxapi.GXDH>`
        :rtype:   GXDH
        """
        return GXDH()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# ArcGIS Target Functions


    @classmethod
    def is_esri(cls):
        """
        Running inside ArcGIS?
        

        :returns:    0 - if No
                  1 - if Yes
        :rtype:      int

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapDH._is_esri(GXContext._get_tls_geo())
        return ret_val




# Data processing/conversion methods



    def creat_chan_lst(self, lst):
        """
        Fills a `GXLST <geosoft.gxapi.GXLST>` with available string and numeric channel code values.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` to fill with channel code values.
        :type  lst:  GXLST

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._creat_chan_lst(lst)
        




    def depth_data_lst(self, lst):
        """
        Fills a `GXLST <geosoft.gxapi.GXLST>` with available channel code values from Depth databases.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` to fill with channel code values.
        :type  lst:  GXLST

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._depth_data_lst(lst)
        




    def from_to_data_lst(self, assay, lst):
        """
        Fills a `GXLST <geosoft.gxapi.GXLST>` with available string and numeric channel code values from From-To databases.
        
        :param assay:  Assay dataset ("" for all)
        :param lst:    `GXLST <geosoft.gxapi.GXLST>` to fill with channel code values.
        :type  assay:  str
        :type  lst:    GXLST

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._from_to_data_lst(assay.encode(), lst)
        




    def get_geology_contacts(self, lst, chan_code, geology, surface, gap, vv_x, vv_y, vv_z):
        """
        Return XYZ locations of top or bottom geological surfaces
        
        :param lst:        `GXLST <geosoft.gxapi.GXLST>` of holes to check
        :param chan_code:  Channel code
        :param geology:    Geology item
        :param surface:    :ref:`DH_SURFACE` Surface selection (top or bottom)
        :param gap:        Max gap to skip when compositing (`GS_R8DM <geosoft.gxapi.GS_R8DM>` for none)
        :param vv_x:       X locations of the contact
        :param vv_y:       Y locations of the contact
        :param vv_z:       Z locations of the contact
        :type  lst:        GXLST
        :type  chan_code:  str
        :type  geology:    str
        :type  surface:    int
        :type  gap:        float
        :type  vv_x:       GXVV
        :type  vv_y:       GXVV
        :type  vv_z:       GXVV

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** For the input `GXLST <geosoft.gxapi.GXLST>` of holes, returns XYZ location of top or bottom
        contact with the input geology. Those selected holes which do NOT
        have contacts, return `rDUMMY <geosoft.gxapi.rDUMMY>` for the corresponding locations.
        """
        self._get_geology_contacts(lst, chan_code.encode(), geology.encode(), surface, gap, vv_x, vv_y, vv_z)
        




    def get_oriented_core_dip_dir(self, lst, alpha, beta, top_ref, dip, dip_dir):
        """
        Converted alpha/beta values in oriented cores to dip/dip direction.
        
        :param lst:      List of holes to process (e.g. from `hole_lst <geosoft.gxapi.GXDH.hole_lst>`)
        :param alpha:    Channel code for input alpha data
        :param beta:     Channel code for input beta data
        :param top_ref:  1: Top of core reference 0: Bottom of core reference
        :param dip:      Channel name for output dip data
        :param dip_dir:  Channel name for output dip direction
        :type  lst:      GXLST
        :type  alpha:    str
        :type  beta:     str
        :type  top_ref:  int
        :type  dip:      str
        :type  dip_dir:  str

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The input data are the oriented core alpha and beta values, using either
        top or bottom reference. The values for each hole in the `GXLST <geosoft.gxapi.GXLST>` are converted
        to "absolute" dip and dip-direction values, using the resurveyed hole
        orientations at each depth.
        The alpha and beta data must be from the same database, and the output
        dip and dip/dir channels are written to the same database.
        """
        self._get_oriented_core_dip_dir(lst, alpha.encode(), beta.encode(), top_ref, dip.encode(), dip_dir.encode())
        




    def get_unique_channel_items(self, chan_code, selected_holes, vv):
        """
        Return a `GXVV <geosoft.gxapi.GXVV>` with unique items in a channel.
        
        :param chan_code:       Channel code
        :param selected_holes:  Selected holes (1), All holes (0)
        :param vv:              `GXVV <geosoft.gxapi.GXVV>` filled with items (converted to this `GXVV <geosoft.gxapi.GXVV>` type)
        :type  chan_code:       str
        :type  selected_holes:  int
        :type  vv:              GXVV

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Finds and sorts all the unique non-dummy items for the selected channel.
        """
        self._get_unique_channel_items(chan_code.encode(), selected_holes, vv)
        




    def get_unique_channel_items_from_collar(self, chan_name, selected_holes, vv):
        """
        Return a `GXVV <geosoft.gxapi.GXVV>` with unique items in a channel.
        
        :param chan_name:       Channel
        :param selected_holes:  Selected holes (1), All holes (0)
        :param vv:              `GXVV <geosoft.gxapi.GXVV>` filled with items (converted to this `GXVV <geosoft.gxapi.GXVV>` type)
        :type  chan_name:       str
        :type  selected_holes:  int
        :type  vv:              GXVV

        .. versionadded:: 7.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Finds and sorts all the unique non-dummy items for the selected channel.
        """
        self._get_unique_channel_items_from_collar(chan_name.encode(), selected_holes, vv)
        




    def chan_type(self, chan_code):
        """
        Return the data type for a channel code.
        
        :param chan_code:  Channel code
        :type  chan_code:  str

        :returns:          Channel data type
        :rtype:            int

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Finds and sorts all the unique non-dummy items for the selected channel.
        """
        ret_val = self._chan_type(chan_code.encode())
        return ret_val




    def find_hole_intersection(self, hole, img, x, y, z):
        """
        Return XYZ locations of the intersection of a hole with a DEM grid.
        
        :param hole:  Hole index
        :param img:   DEM Grid
        :param x:     Returned X location
        :param y:     Returned Y location
        :param z:     Returned Z location
        :type  hole:  int
        :type  img:   GXIMG
        :type  x:     float_ref
        :type  y:     float_ref
        :type  z:     float_ref

        :returns:     1 if intersection found
                      0 if no intersection found
        :rtype:       int

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Input the hole index and an `GXIMG <geosoft.gxapi.GXIMG>` object. Returns XYZ location
        of the hole intersection with the DEM. Interpolation inside the DEM
        uses the native `GXIMG <geosoft.gxapi.GXIMG>` interp method. If no intersection is found the
        returned XYZ locations are `rDUMMY <geosoft.gxapi.rDUMMY>`.
        """
        ret_val, x.value, y.value, z.value = self._find_hole_intersection(hole, img, x.value, y.value, z.value)
        return ret_val




    def get_chan_code_info(self, chan_code, assay_db_index, chan):
        """
        Return the assay database index and channel name from a channel code string.
        
        :param chan_code:       Input channel code "[Assay] channel"
        :param assay_db_index:  Returned assay database index
        :param chan:            Channel name
        :type  chan_code:       str
        :type  assay_db_index:  int_ref
        :type  chan:            str_ref

        .. versionadded:: 7.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The input channel code is in the form "[Assay] channel"
        """
        assay_db_index.value, chan.value = self._get_chan_code_info(chan_code.encode(), assay_db_index.value, chan.value.encode())
        




    def grid_intersection(self, xi, yi, zi, dip, az, grid, xo, yo, zo):
        """
        Algorithm to determine the intersection of a straight hole with a surface (DEM) grid.
        
        :param xi:    Input location on hole X
        :param yi:    Input location on hole Y
        :param zi:    Input location on hole Z
        :param dip:   Dip (positive up) in degrees
        :param az:    Azimuth in degrees
        :param grid:  DEM grid
        :param xo:    Returned intersection point X
        :param yo:    Returned intersection point Y
        :param zo:    Returned intersection point Z
        :type  xi:    float
        :type  yi:    float
        :type  zi:    float
        :type  dip:   float
        :type  az:    float
        :type  grid:  str
        :type  xo:    float_ref
        :type  yo:    float_ref
        :type  zo:    float_ref

        :returns:     1 if an intersection is found, 0 if not.
        :rtype:       int

        .. versionadded:: 7.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Given a point on the hole and the straight hole dip and azimuth,
        ocate (an) intersection point with the input DEM grid.
        """
        ret_val, xo.value, yo.value, zo.value = self._grid_intersection(xi, yi, zi, dip, az, grid.encode(), xo.value, yo.value, zo.value)
        return ret_val




    def litho_grid_3d(self, chan_code, tpat, vox, cell_size, gap, non_contact_radius, gridding_type, reg, retain_grid_files):
        """
        Create a lithology voxel grid with lith codes mapped to single values.
        
        :param chan_code:           Lithology channel code
        :param tpat:                Codes, colors etc.
        :param vox:                 Name of `GXVOX <geosoft.gxapi.GXVOX>` Persistent Storage file
        :param cell_size:           Cell Size (`GS_R8DM <geosoft.gxapi.GS_R8DM>` for automatic calculation)
        :param gap:                 Max gap to skip when compositing (`GS_R8DM <geosoft.gxapi.GS_R8DM>` for none)
        :param non_contact_radius:  Non-contact radius.
        :param gridding_type:       Gridding type (0: Rangrid, 1: TinGrid)
        :param reg:                 Rangrid control `GXREG <geosoft.gxapi.GXREG>` (see `GXRGRD <geosoft.gxapi.GXRGRD>` class for parameters)
        :param retain_grid_files:   Retain top/bottom grids?
        :type  chan_code:           str
        :type  tpat:                GXTPAT
        :type  vox:                 str
        :type  cell_size:           float
        :type  gap:                 float
        :type  non_contact_radius:  float
        :type  gridding_type:       int
        :type  reg:                 GXREG
        :type  retain_grid_files:   int

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Values in the input channel are assigned the index of the corresponding
        item found in the input `GXTPAT <geosoft.gxapi.GXTPAT>`.
        The compositing gap refers to the size of gaps in the data (either
        a blank lithology or missing from-to interval) which will be ignored
        when compositing lithologies into contiguous from-to intervals.
        The non-contact radius is used to dummy out the level grids around holes
        where the gridded lithology is not found. If not specified (dummy) then
        half the distance to the nearest contacting hole is used.
        """
        self._litho_grid_3d(chan_code.encode(), tpat, vox.encode(), cell_size, gap, non_contact_radius, gridding_type, reg, retain_grid_files)
        




    def numeric_chan_lst(self, lst):
        """
        Fills a `GXLST <geosoft.gxapi.GXLST>` with available numeric channel code values.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` to fill with channel code values.
        :type  lst:  GXLST

        .. versionadded:: 7.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._numeric_chan_lst(lst)
        




    def numeric_from_to_data_lst(self, assay, lst):
        """
        Fills a `GXLST <geosoft.gxapi.GXLST>` with available numeric channel code values from From-To databases..
        
        :param assay:  Assay dataset ("" for all)
        :param lst:    `GXLST <geosoft.gxapi.GXLST>` to fill with channel code values.
        :type  assay:  str
        :type  lst:    GXLST

        .. versionadded:: 7.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._numeric_from_to_data_lst(assay.encode(), lst)
        




    def punch_grid_holes(self, img, vv_x, vv_y, vv_z, blank_dist):
        """
        Dummy out locations in a grid around non-contact holes.
        
        :param img:         DEM grid
        :param vv_x:        X locations of the contacts
        :param vv_y:        Y locations of the contacts
        :param vv_z:        Z locations of the contacts
        :param blank_dist:  Blanking distance
        :type  img:         GXIMG
        :type  vv_x:        GXVV
        :type  vv_y:        GXVV
        :type  vv_z:        GXVV
        :type  blank_dist:  float

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Grid is dummied out to the blanking distance around holes where
        the input Z value is dummy. If a contacting hole is closer then
        twice the blanking distance, the blanking distance is reduced
        accordingly. Distances are measured horizontally (e.g. Z is ignored).
        If the blanking distance is zero or dummy, the distance is
        automatically set to half the distance to the closest hole intersection.
        """
        self._punch_grid_holes(img, vv_x, vv_y, vv_z, blank_dist)
        




    def string_chan_lst(self, lst):
        """
        Fills a `GXLST <geosoft.gxapi.GXLST>` with available string channel code values.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` to fill with channel code values.
        :type  lst:  GXLST

        .. versionadded:: 7.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Channel codes are in the format "[Assay] Au", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Au" channel in the "Tutorial_Assay.gdb" database.
        """
        self._string_chan_lst(lst)
        




    def string_from_to_data_lst(self, assay, lst):
        """
        Fills a `GXLST <geosoft.gxapi.GXLST>` with available string-type channel code values from From-To databases.
        
        :param assay:  Assay dataset ("" for all)
        :param lst:    `GXLST <geosoft.gxapi.GXLST>` to fill with channel code values.
        :type  assay:  str
        :type  lst:    GXLST

        .. versionadded:: 7.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Channel codes are in the format "[Geology] Lithology", where the name in
        the square brackets is descriptive part of the project database
        containing the given channel name. The above code might refer to
        the "Lithology" channel in the "Tutorial_Geology.gdb" database.
        """
        self._string_from_to_data_lst(assay.encode(), lst)
        




# Miscellaneous



    def h_assay_db(self, assay):
        """
        Database for an assay data set.
        
        :param assay:  Assay dataset number
        :type  assay:  int

        :returns:      x - `GXDB <geosoft.gxapi.GXDB>`
                       `DB_NULL <geosoft.gxapi.DB_NULL>` if no assay data (no error registered)
        :rtype:        GXDB

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Works for both single and multiple `GXDB <geosoft.gxapi.GXDB>` Wholeplots.
        """
        ret_val = self._h_assay_db(assay)
        return GXDB(ret_val)




    def h_assay_symb(self, assay, hole):
        """
        Line/Group symbol for a specific assay data set hole.
        
        :param assay:  Assay dataset number
        :param hole:   Hole index number
        :type  assay:  int
        :type  hole:   int

        :returns:      x - DB_SYMB
                       `NULLSYMB <geosoft.gxapi.NULLSYMB>` if no survey data for this hole (no error registered)
        :rtype:        int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Works for both single and multiple `GXDB <geosoft.gxapi.GXDB>` Wholeplots.
        """
        ret_val = self._h_assay_symb(assay, hole)
        return ret_val




    def h_collar_db(self):
        """
        Database for the collar table.
        

        :returns:    x - `GXDB <geosoft.gxapi.GXDB>`
                    `DB_NULL <geosoft.gxapi.DB_NULL>` if no collar table (no error registered)
        :rtype:      GXDB

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Works for both single and multiple `GXDB <geosoft.gxapi.GXDB>` Wholeplots.
        """
        ret_val = self._h_collar_db()
        return GXDB(ret_val)




    def h_collar_symb(self):
        """
        Line/Group symbol for the collar table.
        

        :returns:    x - DB_SYMB
                    `NULLSYMB <geosoft.gxapi.NULLSYMB>` if no collar table (no error registered)
        :rtype:      int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Works for both single and multiple `GXDB <geosoft.gxapi.GXDB>` Wholeplots.
        """
        ret_val = self._h_collar_symb()
        return ret_val




    def h_dip_az_survey_db(self):
        """
        Database for the Dip-Azimuth survey data
        

        :returns:    x - `GXDB <geosoft.gxapi.GXDB>`
                    `DB_NULL <geosoft.gxapi.DB_NULL>` if no dip-azimuth survey data (no error registered)
        :rtype:      GXDB

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Works for both single and multiple `GXDB <geosoft.gxapi.GXDB>` Wholeplots.
        """
        ret_val = self._h_dip_az_survey_db()
        return GXDB(ret_val)




    def h_dip_az_survey_symb(self, hole):
        """
        Line/Group symbol for a specific hole Dip-Azimuth survey.
        
        :param hole:  Hole index number
        :type  hole:  int

        :returns:     x - DB_SYMB
                      `NULLSYMB <geosoft.gxapi.NULLSYMB>` if no Dip-Azimuth survey data for this hole (no error registered)
        :rtype:       int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Works for both single and multiple `GXDB <geosoft.gxapi.GXDB>` Wholeplots.
        """
        ret_val = self._h_dip_az_survey_symb(hole)
        return ret_val




    def h_en_survey_db(self):
        """
        Database for the East-North survey data
        

        :returns:    x - `GXDB <geosoft.gxapi.GXDB>`
                    `DB_NULL <geosoft.gxapi.DB_NULL>` if no East-North survey data (no error registered)
        :rtype:      GXDB

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Works for both single and multiple `GXDB <geosoft.gxapi.GXDB>` Wholeplots.
        """
        ret_val = self._h_en_survey_db()
        return GXDB(ret_val)




    def h_en_survey_symb(self, hole):
        """
        Line/Group symbol for a specific hole East-North survey.
        
        :param hole:  Hole index number
        :type  hole:  int

        :returns:     x - DB_SYMB
                      `NULLSYMB <geosoft.gxapi.NULLSYMB>` if no EN survey data for this hole (no error registered)
        :rtype:       int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Works for both single and multiple `GXDB <geosoft.gxapi.GXDB>` Wholeplots.
        """
        ret_val = self._h_en_survey_symb(hole)
        return ret_val




    def add_survey_table(self, hole):
        """
        Add a survey table for a new hole.
        
        :param hole:  Hole index
        :type  hole:  int

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The information is created from the collar table info.
        If the survey info already exists, does nothing.
        """
        self._add_survey_table(hole)
        




    def assay_hole_lst(self, assay_db, lst):
        """
        Populate an `GXLST <geosoft.gxapi.GXLST>` with holes in an assay database
        
        :param assay_db:  Index of the assay database
        :param lst:       `GXLST <geosoft.gxapi.GXLST>` handle
        :type  assay_db:  int
        :type  lst:       GXLST

        .. versionadded:: 6.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._assay_hole_lst(assay_db, lst)
        




    def assay_lst(self, lst):
        """
        Return the `GXLST <geosoft.gxapi.GXLST>` of from-to and point assay datasets
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` to be populated
        :type  lst:  GXLST

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Assay dataset name is given as `LST_ITEM_NAME <geosoft.gxapi.LST_ITEM_NAME>`
        Assay dataset number is given as `LST_ITEM_VALUE <geosoft.gxapi.LST_ITEM_VALUE>`
        Returns an empty `GXLST <geosoft.gxapi.GXLST>` if no datasets.
        """
        self._assay_lst(lst)
        



    @classmethod
    def auto_select_holes(cls, flag):
        """
        Use automatic hole selection based on slice.
        
        :param flag:  Turn on (TRUE) or off (FALSE)
        :type  flag:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapDH._auto_select_holes(GXContext._get_tls_geo(), flag)
        




    def clean(self):
        """
        Delete extraneous holes from project databases.
        

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Removes from Project databases any lines not connected to
        a line found in the collar table list.
        If all the database lines would be removed, the database is
        simply deleted.
        """
        self._clean()
        




    def composite_db(self, mast_db, comp_db, hol_sel, int_sel, fix_int, lith_ch, int_file, wt_ch, rej1_val, rej2_val, rej3_val, rej3_op, rej3_ch):
        """
        Make a composite database
        
        :param mast_db:   Input assay `GXDB <geosoft.gxapi.GXDB>` object
        :param comp_db:   Output composite `GXDB <geosoft.gxapi.GXDB>` object
        :param hol_sel:   :ref:`DH_COMPSTDB_HOLSEL`
        :param int_sel:   :ref:`DH_COMPSTDB_INTSEL`
        :param fix_int:   Fixed interval length
        :param lith_ch:   Name of lithology cannel
        :param int_file:  Name of interval file
        :param wt_ch:     Name of Weight channel
        :param rej1_val:  dRej1Val for intervals short than, (`GS_R8DM <geosoft.gxapi.GS_R8DM>` for no action)
        :param rej2_val:  dRej2Val for intervals gap greater than, (`GS_R8DM <geosoft.gxapi.GS_R8DM>` for no action)
        :param rej3_val:  dRej3Val for Rej3Ch with Rej3Op, (`GS_R8DM <geosoft.gxapi.GS_R8DM>` for no action)
        :param rej3_op:   dRej3Op: 0: >, 1: >=, 2: <, 3: <=
        :param rej3_ch:   Name of Rej3Ch channel
        :type  mast_db:   GXDB
        :type  comp_db:   GXDB
        :type  hol_sel:   int
        :type  int_sel:   int
        :type  fix_int:   float
        :type  lith_ch:   str
        :type  int_file:  str
        :type  wt_ch:     str
        :type  rej1_val:  float
        :type  rej2_val:  float
        :type  rej3_val:  float
        :type  rej3_op:   int
        :type  rej3_ch:   str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._composite_db(mast_db, comp_db, hol_sel, int_sel, fix_int, lith_ch.encode(), int_file.encode(), wt_ch.encode(), rej1_val, rej2_val, rej3_val, rej3_op, rej3_ch.encode())
        




    def compute_hole_xyz(self, hole):
        """
        Computes XYZ for survey and assay data for a single hole.
        
        :param hole:  Hole index
        :type  hole:  int

        .. versionadded:: 7.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._compute_hole_xyz(hole)
        




    def compute_sel_extent(self, e_min, e_max, n_min, n_max, z_min, z_max):
        """
        Computes the extents for selected holes.
        
        :param e_min:  East Min
        :param e_max:  East Max
        :param n_min:  North Min
        :param n_max:  North Max
        :param z_min:  Elev Min
        :param z_max:  Elev Max
        :type  e_min:  float_ref
        :type  e_max:  float_ref
        :type  n_min:  float_ref
        :type  n_max:  float_ref
        :type  z_min:  float_ref
        :type  z_max:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        e_min.value, e_max.value, n_min.value, n_max.value, z_min.value, z_max.value = self._compute_sel_extent(e_min.value, e_max.value, n_min.value, n_max.value, z_min.value, z_max.value)
        




    def compute_xyz(self):
        """
        Computes XYZ for survey and assay data.
        

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._compute_xyz()
        



    @classmethod
    def convert_old_line_names(cls, db, lst):
        """
        Convert old "DD001.Assay" type lines to "DD001"
        
        :param db:   `GXDH <geosoft.gxapi.GXDH>` object
        :param lst:  Names to convert (call `GXDB.symb_lst <geosoft.gxapi.GXDB.symb_lst>`).
        :type  db:   GXDB
        :type  lst:  GXLST

        .. versionadded:: 6.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The input `GXLST <geosoft.gxapi.GXLST>` must be filled using a function like `GXDB.symb_lst <geosoft.gxapi.GXDB.symb_lst>`, which
        puts the name and symbol into the `GXLST <geosoft.gxapi.GXLST>` items.
        Any names with a period are truncated at the period, and
        the line name in the database is changed to the new name
        (just the hole name).
        The `GXLST <geosoft.gxapi.GXLST>` is modified to have the new names.
        A value is put into the `GXDB <geosoft.gxapi.GXDB>` `GXREG <geosoft.gxapi.GXREG>` "DH_CONVERTED_NAMES" parameter so
        this process is done only once on a database.

        DO NOT use on old-style single-database Wholeplot projects.
        """
        gxapi_cy.WrapDH._convert_old_line_names(GXContext._get_tls_geo(), db, lst)
        



    @classmethod
    def create(cls, db):
        """
        Create `GXDH <geosoft.gxapi.GXDH>`.
        
        :param db:  Name of current database
        :type  db:  str

        :returns:    `GXDH <geosoft.gxapi.GXDH>` Object
        :rtype:      GXDH

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapDH._create(GXContext._get_tls_geo(), db.encode())
        return GXDH(ret_val)




    def create_default_job(self, ini, type):
        """
        Create a default job from scratch.
        
        :param ini:   File name of the INI file to create (forces correct suffix)
        :param type:  :ref:`DH_PLOT`
        :type  ini:   str
        :type  type:  int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._create_default_job(ini.encode(), type)
        



    @classmethod
    def create_external(cls, db):
        """
        Create a `GXDH <geosoft.gxapi.GXDH>` from an external process (no montaj running).
        
        :param db:  Name of example project database
        :type  db:  str

        :returns:    `GXDH <geosoft.gxapi.GXDH>` Object
        :rtype:      GXDH

        .. versionadded:: 5.1.6

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The regular `create <geosoft.gxapi.GXDH.create>` assumes a workspace is open and creates
        the project from the databases which are currently loaded.
        This function instead creates the project from all projects
        in the input databases's directory.
        """
        ret_val = gxapi_cy.WrapDH._create_external(GXContext._get_tls_geo(), db.encode())
        return GXDH(ret_val)



    @classmethod
    def current(cls):
        """
        Creates a drill project from current environment.
        

        :returns:    `GXDH <geosoft.gxapi.GXDH>` Object
        :rtype:      GXDH

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If no `GXDH <geosoft.gxapi.GXDH>` database is open the Open `GXDH <geosoft.gxapi.GXDH>` Project `GXGUI <geosoft.gxapi.GXGUI>` will be displayed which may be
        cancelled by the user in which case the GX will terminate with cancel.
        """
        ret_val = gxapi_cy.WrapDH._current(GXContext._get_tls_geo())
        return GXDH(ret_val)



    @classmethod
    def datamine_to_csv(cls, file, proj):
        """
        Convert a Datamine drillhole file to CSV files ready for import.
        
        :param file:  Datamine database file to import (``*.dm``)
        :param proj:  Drillhole project name
        :type  file:  str
        :type  proj:  str

        .. versionadded:: 6.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Creates three CSV files and the accompanying template files
        ready for batch ASCII import into a drill project.

             Project_Collar.csv, .i3
             Project_Survey.csv, .i3
             Project_Assay.csv,  .i3
        """
        gxapi_cy.WrapDH._datamine_to_csv(GXContext._get_tls_geo(), file.encode(), proj.encode())
        




    def delete_holes(self, lst):
        """
        Delete a list of holes from the project.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` of holes to delete
        :type  lst:  GXLST

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Removes all lines in the input `GXLST <geosoft.gxapi.GXLST>` from `GXDH <geosoft.gxapi.GXDH>` project databases.
        If all the database lines would be removed, the database is
        simply deleted.
        """
        self._delete_holes(lst)
        






    def export_file(self, file, type):
        """
        Exports a Drill Hole database to an external file.
        
        :param file:  File name
        :param type:  :ref:`DH_EXP`
        :type  file:  str
        :type  type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._export_file(file.encode(), type)
        




    def export_geodatabase_lst(self, lst, file, pre, feat_class, overwrite):
        """
        Exports whole or part of a Drill Hole database to an ArcGIS Geodatabase as feature class(es).
        
        :param lst:         Hole Names in the Name and Value parts of the `GXLST <geosoft.gxapi.GXLST>`
        :param file:        File name (.pdb folder for File Geodatabase or .sde connector for SDE)
        :param pre:         String to prefix dataset names with
        :param feat_class:  Feature class name to export (pass empty for all or name of table, will contain the name of the output dataset for if a rename occurs)
        :param overwrite:   Overwrite existing feature classes? ``False`` will create copies.
        :type  lst:         GXLST
        :type  file:        str
        :type  pre:         str
        :type  feat_class:  str_ref
        :type  overwrite:   int

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** A table with metadata about the created feature classes will be written to the Geodatabase. This table will have the same
        name with the postfix "_Metadata" attached
        """
        feat_class.value = self._export_geodatabase_lst(lst, file.encode(), pre.encode(), feat_class.value.encode(), overwrite)
        




    def export_las(self, assay_db, hole, interval, file):
        """
        Exports a Drill Hole database to a LAS v2 file.
        
        :param assay_db:  Assay database index
        :param hole:      Hole index
        :param interval:  Interval for output
        :param file:      File name
        :type  assay_db:  int
        :type  hole:      int
        :type  interval:  float
        :type  file:      str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._export_las(assay_db, hole, interval, file.encode())
        




    def export_lst(self, lst, file, type):
        """
        Exports a `GXLST <geosoft.gxapi.GXLST>` of holes in a Drill Hole database to an external file.
        
        :param lst:   Hole Names in the Name and Value parts of the `GXLST <geosoft.gxapi.GXLST>`
        :param file:  File name
        :param type:  :ref:`DH_EXP`
        :type  lst:   GXLST
        :type  file:  str
        :type  type:  int

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Use functions like `GXDB.selected_line_lst <geosoft.gxapi.GXDB.selected_line_lst>` to construct the `GXLST <geosoft.gxapi.GXLST>`
        """
        self._export_lst(lst, file.encode(), type)
        




    def flush_select(self):
        """
        Flush all selections to database selection engine.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._flush_select()
        




    def get_databases_vv(self, gvv):
        """
        Get the names of the project databases in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param gvv:  `GXVV <geosoft.gxapi.GXVV>` of type -`STR_FILE <geosoft.gxapi.STR_FILE>`
        :type  gvv:  GXVV

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._get_databases_vv(gvv)
        




    def get_databases_sorted_vv(self, gvv):
        """
        Get the names of the project databases in a `GXVV <geosoft.gxapi.GXVV>`, same as `get_databases_vv <geosoft.gxapi.GXDH.get_databases_vv>` but the list is sorted alphabetically.
        
        :param gvv:  `GXVV <geosoft.gxapi.GXVV>` of type -`STR_FILE <geosoft.gxapi.STR_FILE>`
        :type  gvv:  GXVV

        .. versionadded:: 8.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._get_databases_sorted_vv(gvv)
        




    def get_data_type(self, db, type):
        """
        Get the type of data in a Wholeplot database.
        
        :param db:    `GXDB <geosoft.gxapi.GXDB>` Handle
        :param type:  :ref:`DH_DATA`
        :type  db:    GXDB
        :type  type:  int_ref

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Returns `DH_DATA_UNKNOWN <geosoft.gxapi.DH_DATA_UNKNOWN>` if it can't determine the type.
        """
        type.value = self._get_data_type(db, type.value)
        




    def get_default_section(self, az, x1, x2, l, w):
        """
        Computes default section azimuths, extents for selected holes.
        
        :param az:  Azimuth of section (returned)
        :param x1:  Corner X (Easting) of section (returned)
        :param x2:  Corner Y (Northing) of section (returned)
        :param l:   Section length (returned)
        :param w:   Section width (returned)
        :type  az:  float_ref
        :type  x1:  float_ref
        :type  x2:  float_ref
        :type  l:   float_ref
        :type  w:   float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        az.value, x1.value, x2.value, l.value, w.value = self._get_default_section(az.value, x1.value, x2.value, l.value, w.value)
        




    def get_hole_group(self, hole, assay):
        """
        Get the Group symbol for this hole/table combination.
        
        :param hole:   Hole index
        :param assay:  Table Name
        :type  hole:   int
        :type  assay:  str

        :returns:      Hole Symbol
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._get_hole_group(hole, assay.encode())
        return ret_val




    def get_hole_survey(self, hole, vv_x, vv_y, vv_z, vv_d):
        """
        Get the Survey information of a Hole.
        
        :param hole:  Hole index
        :param vv_x:  X
        :param vv_y:  Y
        :param vv_z:  Z
        :param vv_d:  Depth
        :type  hole:  int
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV
        :type  vv_d:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._get_hole_survey(hole, vv_x, vv_y, vv_z, vv_d)
        




    def get_hole_survey_ex(self, hole, vv_x, vv_y, vv_z, vv_d, thin):
        """
        Get the Survey information of a Hole.
        
        :param hole:  Hole index
        :param vv_x:  X
        :param vv_y:  Y
        :param vv_z:  Z
        :param vv_d:  Depth
        :param thin:  Thin nearly co-linear segments?
        :type  hole:  int
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV
        :type  vv_d:  GXVV
        :type  thin:  bool

        .. versionadded:: 9.5

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._get_hole_survey_ex(hole, vv_x, vv_y, vv_z, vv_d, thin)
        




    def get_hole_survey_from_to(self, db, line, vv_x, vv_y, vv_z, vv_d, vv_l, thin):
        """
        Get the Survey information of a Hole using From/To database.
        
        :param db:    From/To Database
        :param line:  Line handle for hole
        :param vv_x:  X
        :param vv_y:  Y
        :param vv_z:  Z
        :param vv_d:  Depth
        :param vv_l:  From To Segment lengths
        :param thin:  Thin nearly co-linear segments?
        :type  db:    GXDB
        :type  line:  int
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV
        :type  vv_d:  GXVV
        :type  vv_l:  GXVV
        :type  thin:  bool

        .. versionadded:: 9.5

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._get_hole_survey_from_to(db, line, vv_x, vv_y, vv_z, vv_d, vv_l, thin)
        




    def get_ipj(self, ipj):
        """
        Get the project `GXIPJ <geosoft.gxapi.GXIPJ>`.
        
        :param ipj:  `GXIPJ <geosoft.gxapi.GXIPJ>` Handle
        :type  ipj:  GXIPJ

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The projection for the project is the projection stored
        in the DH_EAST channel in the collar table.
        """
        self._get_ipj(ipj)
        




    def get_map_names_vv(self, vv):
        """
        Get plotted map names.
        
        :param vv:  Returned map names (string type `GXVV <geosoft.gxapi.GXVV>`)
        :type  vv:  GXVV

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** This will return the currently plotted map name(s)
        in a `GXVV <geosoft.gxapi.GXVV>`. This should only be called after a call
        to `wholeplot <geosoft.gxapi.GXDH.wholeplot>`. The `GXVV <geosoft.gxapi.GXVV>` size is set to the number
        of maps created.
        """
        self._get_map_names_vv(vv)
        




    def get_map(self, index):
        """
        Get a plotting map
        
        :param index:  Map Index
        :type  index:  int

        :returns:      `GXMAP <geosoft.gxapi.GXMAP>` Object
        :rtype:        GXMAP

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._get_map(index)
        return GXMAP(ret_val)




    def get_num_maps(self):
        """
        Get the number plotting maps
        

        :returns:    Number of plotting maps
        :rtype:      int

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._get_num_maps()
        return ret_val




    def get_reg(self):
        """
        Get the `GXREG <geosoft.gxapi.GXREG>` Object used in this project.
        

        :returns:    `GXREG <geosoft.gxapi.GXREG>` Object
        :rtype:      GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._get_reg()
        return GXREG(ret_val)




    def get_selected_holes_vv(self, vv):
        """
        Populate a `GXVV <geosoft.gxapi.GXVV>` with the indices of all selected holes
        
        :param vv:  Returned hole indices (must be type INT)
        :type  vv:  GXVV

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._get_selected_holes_vv(vv)
        



    @classmethod
    def get_table_default_chan_lst(cls, lst, type):
        """
        Return list of default channels by collar/assay/survey table type.
        
        :param lst:   `GXLST <geosoft.gxapi.GXLST>` handle
        :param type:  :ref:`DH_DATA`
        :type  lst:   GXLST
        :type  type:  int

        .. versionadded:: 7.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Fills a `GXLST <geosoft.gxapi.GXLST>` with the default channel names created according to
        type (Collar, Survey, Assay). Value is in the `LST_ITEM_NAME <geosoft.gxapi.LST_ITEM_NAME>` part.
        """
        gxapi_cy.WrapDH._get_table_default_chan_lst(GXContext._get_tls_geo(), lst, type)
        




    def hole_lst(self, lst):
        """
        Populate an `GXLST <geosoft.gxapi.GXLST>` with the list of the selected holes
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` handle
        :type  lst:  GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._hole_lst(lst)
        




    def hole_lst2(self, lst):
        """
        Populate an `GXLST <geosoft.gxapi.GXLST>` with the list of all the holes
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` handle
        :type  lst:  GXLST

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._hole_lst2(lst)
        




    def add_hole(self, hole):
        """
        Add a hole and return it's index.
        
        :param hole:  Name of hole
        :type  hole:  str

        :returns:     x  - Hole index
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._add_hole(hole.encode())
        return ret_val




    def clean_will_delete_db(self):
        """
        See if "cleaning" will delete project databases.
        

        :returns:    1 if calling `clean <geosoft.gxapi.GXDH.clean>` will remove all "lines" from
                        one of the `GXDH <geosoft.gxapi.GXDH>` project databases.
        :rtype:      int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._clean_will_delete_db()
        return ret_val




    def compositing_tool_gui(self, map, x, y1, y2):
        """
        Annotate a strip log map using the compositing tool.
        
        :param map:  Current strip log map
        :param x:    X location on map of selected strip
        :param y1:   Y End of hole interval in view coords
        :param y2:   Y Other end of hole interval in view coords
        :type  map:  GXMAP
        :type  x:    float
        :type  y1:   float
        :type  y2:   float

        :returns:    :ref:`DH_COMP_CHOICE`
        :rtype:      int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If any of the input X or Y values are dummies the tool uses default values.
        """
        ret_val = self._compositing_tool_gui(map, x, y1, y2)
        return ret_val



    @classmethod
    def create_collar_table(cls, project, chan, db):
        """
        Create a collar table `GXDB <geosoft.gxapi.GXDB>` with channels set up.
        
        :param project:  Project name
        :param chan:     Number of channels
        :param db:       Collar table name (returned)
        :type  project:  str
        :type  chan:     int
        :type  db:       str_ref

        .. versionadded:: 5.1.6

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The database name will be of the form

        "d:\\directory\\Project_Collar.gdb"
        """
        db.value = gxapi_cy.WrapDH._create_collar_table(GXContext._get_tls_geo(), project.encode(), chan, db.value.encode())
        



    @classmethod
    def create_collar_table_dir(cls, project, dir, chan, db):
        """
        Create a collar table in the specified directory.
        
        :param project:  Project name
        :param dir:      Directory to create project in
        :param chan:     Number of channels
        :param db:       Collar table name (returned)
        :type  project:  str
        :type  dir:      str
        :type  chan:     int
        :type  db:       str_ref

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The database name will be of the form

        "d:\\directory\\Project_Collar.gdb"
        """
        db.value = gxapi_cy.WrapDH._create_collar_table_dir(GXContext._get_tls_geo(), project.encode(), dir.encode(), chan, db.value.encode())
        




    def delete_will_delete_db(self, lst):
        """
        See if deleting holes will delete project databases.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` of holes to delete
        :type  lst:  GXLST

        :returns:    1 if deleting the `GXLST <geosoft.gxapi.GXLST>` of holes will remove all "lines" from
                     one of the `GXDH <geosoft.gxapi.GXDH>` project databases.
        :rtype:      int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._delete_will_delete_db(lst)
        return ret_val




    def find_hole(self, hole):
        """
        Find a hole and return it's index.
        
        :param hole:  Name of hole
        :type  hole:  str

        :returns:     x  - Hole index
                      -1 - Not found
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._find_hole(hole.encode())
        return ret_val




    def get_collar_table_db(self, db):
        """
        Get the name of the database containing the collar table.
        
        :param db:  Returned file name
        :type  db:  str_ref

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        db.value = self._get_collar_table_db(db.value.encode())
        




    def get_info(self, hole, name, data):
        """
        Get Collar Information.
        
        :param hole:  Hole index
        :param name:  Name of information
        :param data:  Buffer to place information
        :type  hole:  int
        :type  name:  str
        :type  data:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the DH_ELEV channel is requested it will also
        search for the DH_RL channel, which is the new
        name for the collar elevation.
        """
        data.value = self._get_info(hole, name.encode(), data.value.encode())
        




    def get_project_name(self, project):
        """
        Get the Wholeplot project name.
        
        :param project:  Returned string
        :type  project:  str_ref

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        project.value = self._get_project_name(project.value.encode())
        



    @classmethod
    def get_section_id(cls, azimuth, east, north, id):
        """
        Create a section ID based on its location
        
        :param azimuth:  Section Azimuth
        :param east:     Section Easting
        :param north:    Section Northing
        :param id:       Section ID
        :type  azimuth:  float
        :type  east:     float
        :type  north:    float
        :type  id:       str_ref

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        id.value = gxapi_cy.WrapDH._get_section_id(GXContext._get_tls_geo(), azimuth, east, north, id.value.encode())
        



    @classmethod
    def get_template_blob(cls, db, template, imp_type):
        """
        Retrieve the import template from the database.
        
        :param db:        `GXDB <geosoft.gxapi.GXDB>` Handle
        :param template:  Name of template file to extract to.
        :param imp_type:  The stored import template type :ref:`DH_DATA`
        :type  db:        GXDB
        :type  template:  str
        :type  imp_type:  int_ref

        :returns:         0: No template stored in the database
                          1: Template retrieved and written to a file.
        :rtype:           int

        .. versionadded:: 6.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The template can be retrieved in order to refresh the
        database with a call to the DHIMPORT.GX.

        The import types correspond to the DHIMPORT.IMPTYPE variable:
        0: ASCII, 1: Database/XLS, 2: ODBC

        If no template blob exists, templ
        """
        ret_val, imp_type.value = gxapi_cy.WrapDH._get_template_blob(GXContext._get_tls_geo(), db, template.encode(), imp_type.value)
        return ret_val



    @classmethod
    def get_template_info(cls, template, data_type, file, table):
        """
        Retrieve the file, `GXDH <geosoft.gxapi.GXDH>` Table name and type from an import template.
        
        :param template:   Template name
        :param data_type:  :ref:`DH_DATA`
        :param file:       File name (blank for ODBC, or undefined).
        :param table:      Table name (blank for `DH_DATA_UNKNOWN <geosoft.gxapi.DH_DATA_UNKNOWN>`, or undefined).
        :type  template:   str
        :type  data_type:  int_ref
        :type  file:       str_ref
        :type  table:      str_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** As of version 6.0, the import templates (``*.i3, *.i4``) produced
        by the Wholeplot import wizards contain the following lines:

         FILE assay.txt  (except for ODBC)
         DRILLTYPE 3
         DRILLTABLE Assay

        The FILE is normally the input file name, except for ODBC, where it
        is not defined.
        The DRILLTYPE is one of DH_DATA_XXX, and the DRILLTABLE
        is the name of the Wholeplot database table; e.g. Project_Assay.gdb
        in the above case. The DRILLTABLE is only included in the template
        for `DH_DATA_FROMTO <geosoft.gxapi.DH_DATA_FROMTO>` and `DH_DATA_POINT <geosoft.gxapi.DH_DATA_POINT>`, but this function will
        return the appropriate table names (e.g. Collar, Survey, ENSurvey)
        for the other types.
        If the DRILLTYPE is NOT found in the template, a value of
        `DH_DATA_UNKNOWN <geosoft.gxapi.DH_DATA_UNKNOWN>` is returned for the data type; likely an indication that this
        is not a new-style template produced by Wholeplot.
        """
        data_type.value, file.value, table.value = gxapi_cy.WrapDH._get_template_info(GXContext._get_tls_geo(), template.encode(), data_type.value, file.value.encode(), table.value.encode())
        



    @classmethod
    def get_template_info_ex(cls, template, data_type, file, table, lst):
        """
        Retrieve the file, `GXDH <geosoft.gxapi.GXDH>` Table name, type and channel list from an import template.
        
        :param template:   Template name
        :param data_type:  :ref:`DH_DATA`
        :param file:       File name (blank for ODBC, or undefined).
        :param table:      Table name (blank for `DH_DATA_UNKNOWN <geosoft.gxapi.DH_DATA_UNKNOWN>`, or undefined).
        :param lst:        Channel list (returned)
        :type  template:   str
        :type  data_type:  int_ref
        :type  file:       str_ref
        :type  table:      str_ref
        :type  lst:        GXLST

        .. versionadded:: 7.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** As of version 6.0, the import templates (``*.i3, *.i4``) produced
        by the Wholeplot import wizards contain the following lines:

         FILE assay.txt  (except for ODBC)
         DRILLTYPE 3
         DRILLTABLE Assay

        The FILE is normally the input file name, except for ODBC, where it
        is not defined.
        The DRILLTYPE is one of DH_DATA_XXX, and the DRILLTABLE
        is the name of the Wholeplot database table; e.g. Project_Assay.gdb
        in the above case. The DRILLTABLE is only included in the template
        for `DH_DATA_FROMTO <geosoft.gxapi.DH_DATA_FROMTO>` and `DH_DATA_POINT <geosoft.gxapi.DH_DATA_POINT>`, but this function will
        return the appropriate table names (e.g. Collar, Survey, ENSurvey)
        for the other types.
        If the DRILLTYPE is NOT found in the template, a value of
        `DH_DATA_UNKNOWN <geosoft.gxapi.DH_DATA_UNKNOWN>` is returned for the data type; likely an indication that this
        is not a new-style template produced by Wholeplot.
        This version also returns a list of the channels in the template checks can be made to
        see if the import will exceed the database channel limit.
        """
        data_type.value, file.value, table.value = gxapi_cy.WrapDH._get_template_info_ex(GXContext._get_tls_geo(), template.encode(), data_type.value, file.value.encode(), table.value.encode(), lst)
        




    def get_units(self, units, conv_factor):
        """
        Get the positional units and conversion factor to m.
        
        :param units:        Units (i.e. "m")
        :param conv_factor:  Conversion (units/m)
        :type  units:        str_ref
        :type  conv_factor:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        units.value, conv_factor.value = self._get_units(units.value.encode(), conv_factor.value)
        



    @classmethod
    def have_current(cls):
        """
        Returns ``True`` if a drill project is loaded
        
        :rtype:      bool

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapDH._have_current(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def have_current2(cls, db):
        """
        Returns ``True`` if a drill project is loaded, and the collar database if it is loaded.
        
        :param db:  Collar table name (returned)
        :type  db:  str_ref
        :rtype:      bool

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val, db.value = gxapi_cy.WrapDH._have_current2(GXContext._get_tls_geo(), db.value.encode())
        return ret_val




    def holes(self):
        """
        Return number of holes.
        

        :returns:    x  - Number of holes
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._holes()
        return ret_val



    @classmethod
    def hole_select_from_list_gui(cls, lst, sel_lst):
        """
        Select/Deselect holes using the two-panel selection tool.
        
        :param lst:      All holes
        :param sel_lst:  Selected holes
        :type  lst:      GXLST
        :type  sel_lst:  GXLST

        :returns:        0  - Ok
                         -1 - User Cancelled
        :rtype:          int

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapDH._hole_select_from_list_gui(GXContext._get_tls_geo(), lst, sel_lst)
        return ret_val




    def hole_selection_tool_gui(self):
        """
        Select/Deselect holes using plan map tool.
        

        :returns:    0  - Ok
                    -1 - User Cancelled
        :rtype:      int

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._hole_selection_tool_gui()
        return ret_val




    def modify3d_gui(self, ini, page):
        """
        Modify parameters for a 3D plot.
        
        :param ini:   Job Name   (``*.in3``)
        :param page:  Page to open `GXGUI <geosoft.gxapi.GXGUI>` on
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val, page.value = self._modify3d_gui(ini.encode(), page.value)
        return ret_val




    def edit_classification_table_file_gui(self, chan, class_file, fill_patterns, colors_only):
        """
        Edit a symbol color/pattern CSV file
        
        :param chan:           Channel
        :param class_file:     CSV filename (in/out can be blank)
        :param fill_patterns:  0 - Collar Symbols
                               -1 - Rock Patterns
        :param colors_only:    0 - Symbols/patterns (2D)
                               -1 - Colors only (3D)
        :type  chan:           str
        :type  class_file:     str_ref
        :type  fill_patterns:  int
        :type  colors_only:    int

        :returns:              0 - Ok
                               -1 - User Cancelled
        :rtype:                int

        .. versionadded:: 9.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val, class_file.value = self._edit_classification_table_file_gui(chan.encode(), class_file.value.encode(), fill_patterns, colors_only)
        return ret_val




    def modify_crooked_section_holes_gui(self, ini, page):
        """
        Modify parameters to replot holes and hole data to an existing crooked section map.
        
        :param ini:   Job Name (``*.ins``)
        :param page:  Tab page ID.
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 7.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Will plot to an empty crooked section.
        """
        ret_val, page.value = self._modify_crooked_section_holes_gui(ini.encode(), page.value)
        return ret_val




    def modify_fence_gui(self, ini, page):
        """
        Modify parameters for a section plot.
        
        :param ini:   Job Name (``*.ins``)
        :param page:  :ref:`DH_SECT_PAGE`
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      1 - Interactively define a fence.
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The fence section function.
        """
        ret_val, page.value = self._modify_fence_gui(ini.encode(), page.value)
        return ret_val




    def modify_hole_traces_3d_gui(self, ini, page):
        """
        Modify parameters for a hole traces plot to an existing 3D view.
        
        :param ini:   Job Name
        :param page:  Page to open `GXGUI <geosoft.gxapi.GXGUI>` on
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val, page.value = self._modify_hole_traces_3d_gui(ini.encode(), page.value)
        return ret_val




    def modify_hole_traces_gui(self, ini, page):
        """
        Modify parameters for a hole traces plot to a current map.
        
        :param ini:   Job Name
        :param page:  Page to open `GXGUI <geosoft.gxapi.GXGUI>` on
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val, page.value = self._modify_hole_traces_gui(ini.encode(), page.value)
        return ret_val




    def modify_hole_traces_gui2(self, ini, plot_type, page):
        """
        Modify parameters for a hole traces plot to a current plan or section view.
        
        :param ini:        Job Name
        :param plot_type:  :ref:`DH_PLOT` One of `DH_PLOT_PLAN <geosoft.gxapi.DH_PLOT_PLAN>` or `DH_PLOT_SECTION <geosoft.gxapi.DH_PLOT_SECTION>`
        :param page:       Page to open `GXGUI <geosoft.gxapi.GXGUI>` on
        :type  ini:        str
        :type  plot_type:  int
        :type  page:       int_ref

        :returns:          0 - Ok
                           -1 - User Cancelled
        :rtype:            int

        .. versionadded:: 8.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Currently supports `DH_PLOT_PLAN <geosoft.gxapi.DH_PLOT_PLAN>` and `DH_PLOT_SECTION <geosoft.gxapi.DH_PLOT_SECTION>`
        """
        ret_val, page.value = self._modify_hole_traces_gui2(ini.encode(), plot_type, page.value)
        return ret_val




    def modify_plan_gui(self, ini, page):
        """
        Modify parameters for a plan plot.
        
        :param ini:   Job Name (``*.inp``)
        :param page:  :ref:`DH_SECT_PAGE`
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val, page.value = self._modify_plan_gui(ini.encode(), page.value)
        return ret_val




    def modify_plan_holes_gui(self, ini, page):
        """
        Modify parameters to replot holes and hole data to an existing plan map.
        
        :param ini:   Job Name (``*.ins``)
        :param page:  Tab Page ID
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Modifies only hole trace, hole data, topo, voxel slice data.
        """
        ret_val, page.value = self._modify_plan_holes_gui(ini.encode(), page.value)
        return ret_val



    @classmethod
    def modify_rock_codes_gui(cls, file):
        """
        Modify/create a rock codes file.
        
        :param file:  File name
        :type  file:  str

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapDH._modify_rock_codes_gui(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def modify_rock_codes_gui2(cls, db, file):
        """
        Modify/create a rock codes file, channel population option.
        
        :param db:    Database
        :param file:  File name
        :type  db:    GXDB
        :type  file:  str

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Same as above, but passes the current database so that
        the "Populate from channel" button can be used to
        automatically populate the rock code list. The database
        should be a Wholeplot database.
        """
        ret_val = gxapi_cy.WrapDH._modify_rock_codes_gui2(GXContext._get_tls_geo(), db, file.encode())
        return ret_val




    def modify_section_gui(self, ini, page):
        """
        Modify parameters for a section plot.
        
        :param ini:   Job Name (``*.ins``)
        :param page:  :ref:`DH_SECT_PAGE`
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      1 - Interactively define a NS section
                      2 - Interactively define an EW section
                      3 - Interactively define an angled section
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The stacked section function uses the same control file
        format, but the plotting of profiles and plan views is
        disabled, and if multiple sections are requested, they
        are plotted in a stack on the left side of the same map,
        not to individual maps.
        """
        ret_val, page.value = self._modify_section_gui(ini.encode(), page.value)
        return ret_val




    def modify_section_holes_gui(self, ini, page):
        """
        Modify parameters to replot holes and hole data to an existing section map.
        
        :param ini:   Job Name (``*.ins``)
        :param page:  Tab page ID.
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Works for both regular and stacked sections.
        Modifies only hole trace, hole data, topo, voxel slice data.
        """
        ret_val, page.value = self._modify_section_holes_gui(ini.encode(), page.value)
        return ret_val




    def modify_stacked_section_gui(self, ini, page):
        """
        Modify parameters for a section plot.
        
        :param ini:   Job Name (``*.ins``)
        :param page:  :ref:`DH_SECT_PAGE`
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      1 - Interactively define a NS section
                      2 - Interactively define an EW section
                      3 - Interactively define an angled section
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The stacked section function uses the same control file
        format, but the plotting of profiles and plan views is
        disabled, and if multiple sections are requested, they
        are plotted in a stack on the left side of the same map,
        not to individual maps.
        """
        ret_val, page.value = self._modify_stacked_section_gui(ini.encode(), page.value)
        return ret_val




    def modify_strip_log_gui(self, ini, page):
        """
        Modify parameters for a strip log plot.
        
        :param ini:   Job Name   (``*.inl``)
        :param page:  :ref:`DH_SECT_PAGE`
        :type  ini:   str
        :type  page:  int_ref

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val, page.value = self._modify_strip_log_gui(ini.encode(), page.value)
        return ret_val



    @classmethod
    def modify_structure_codes_gui(cls, file):
        """
        Modify/create a structure codes file.
        
        :param file:  File name
        :type  file:  str

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapDH._modify_structure_codes_gui(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def modify_structure_codes_gui2(cls, db, file):
        """
        Modify/create a structure codes file, channel population option.
        
        :param db:    Database
        :param file:  File name
        :type  db:    GXDB
        :type  file:  str

        :returns:     0 - Ok
                      -1 - User Cancelled
        :rtype:       int

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Same as above, but passes the current database so that
        the "Populate from channel" button can be used to
        automatically populate the structure code list. The database
        should be a Wholeplot database.
        """
        ret_val = gxapi_cy.WrapDH._modify_structure_codes_gui2(GXContext._get_tls_geo(), db, file.encode())
        return ret_val



    @classmethod
    def import2(cls, project, db, line, hole, table, type, log):
        """
        Imports data into a Drill Hole Database (obsolete).
        
        :param project:  Drill project name
        :param db:       `GXDB <geosoft.gxapi.GXDB>` Handle
        :param line:     Line
        :param hole:     Hole channel
        :param table:    Table
        :param type:     :ref:`DH_DATA`
        :param log:      Log file name
        :type  project:  str
        :type  db:       GXDB
        :type  line:     int
        :type  hole:     int
        :type  table:    str
        :type  type:     int
        :type  log:      str

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapDH._import2(GXContext._get_tls_geo(), project.encode(), db, line, hole, table.encode(), type, log.encode())
        




    def import_las(self, assay, file, interval, interp, wa):
        """
        Imports LAS Data into a `GXDH <geosoft.gxapi.GXDH>` database
        
        :param assay:     Assay database to use
        :param file:      LAS file name
        :param interval:  Averaging/desampling interval (cm)
        :param interp:    Interpolation method
        :param wa:        Log file handle
        :type  assay:     str
        :type  file:      str
        :type  interval:  float
        :type  interp:    int
        :type  wa:        GXWA

        .. versionadded:: 6.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The argument for the assay database is the file name
        without the project name and underscore, e.g. for
        "Project_Assay.gdb" use "Assay"
        """
        self._import_las(assay.encode(), file.encode(), interval, interp, wa)
        




    def num_assays(self):
        """
        Number of assay datasets.
        

        :returns:    The number of assay datasets.
        :rtype:      int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Works for both single and multiple `GXDB <geosoft.gxapi.GXDB>` Wholeplots.
        """
        ret_val = self._num_assays()
        return ret_val




    def num_selected_holes(self):
        """
        Returns number of selected holes.
        

        :returns:    The number of selected holes
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = self._num_selected_holes()
        return ret_val




    def qa_dip_az_curvature_lst(self, lst, tolerance, wa):
        """
        Do QA/QC Curvature checking on Dip Azimuth data for holes in a `GXLST <geosoft.gxapi.GXLST>`.
        
        :param lst:        `GXLST <geosoft.gxapi.GXLST>` of holes (name, index)
        :param tolerance:  Dip/Azimuth curvature tolerance (degree per meter)
        :param wa:         `GXWA <geosoft.gxapi.GXWA>` Handle to write to
        :type  lst:        GXLST
        :type  tolerance:  float
        :type  wa:         GXWA

        :returns:          The number of holes found and checked.
        :rtype:            int

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Checks all holes with Dip-Azimuth survey data
        """
        ret_val = self._qa_dip_az_curvature_lst(lst, tolerance, wa)
        return ret_val




    def qa_dip_az_survey_lst(self, lst, wa):
        """
        Do QA/QC on Dip/Az Survey data for holes in a `GXLST <geosoft.gxapi.GXLST>`.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` of holes (Name, Index)
        :param wa:   `GXWA <geosoft.gxapi.GXWA>` Handle to write to
        :type  lst:  GXLST
        :type  wa:   GXWA

        :returns:    The number of holes found and checked.
        :rtype:      int

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Error if no Dip-Azimuth survey database, or if
        a requested hole does not exist in the drill project.
        """
        ret_val = self._qa_dip_az_survey_lst(lst, wa)
        return ret_val




    def qa_east_north_curvature_lst(self, lst, tolerance, wa):
        """
        Do QA/QC Curvature checking on Dip Azimuth data for holes in a `GXLST <geosoft.gxapi.GXLST>`.
        
        :param lst:        `GXLST <geosoft.gxapi.GXLST>` of holes (name, index)
        :param tolerance:  Dip/Azimuth curvature tolerance (degree per meter)
        :param wa:         `GXWA <geosoft.gxapi.GXWA>` Handle
        :type  lst:        GXLST
        :type  tolerance:  float
        :type  wa:         GXWA

        :returns:          The number of holes found and checked.
        :rtype:            int

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Checks all holes with East-North survey data
        """
        ret_val = self._qa_east_north_curvature_lst(lst, tolerance, wa)
        return ret_val




    def qa_east_north_survey_lst(self, lst, wa):
        """
        Do QA/QC on East/North Survey data for holes in a `GXLST <geosoft.gxapi.GXLST>`.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` of holes (Name, Index)
        :param wa:   `GXWA <geosoft.gxapi.GXWA>` Handle to write to
        :type  lst:  GXLST
        :type  wa:   GXWA

        :returns:    The number of holes found and checked.
        :rtype:      int

        .. versionadded:: 7.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Error if no East-North survey database, or if
        a requested hole does not exist in the drill project.
        """
        ret_val = self._qa_east_north_survey_lst(lst, wa)
        return ret_val




    def slice_selection_tool_gui(self, aoix1, aoiy1, aoix2, aoiy2, aoix3, aoiy3, aoix4, aoiy4, x1, y1, x2, y2):
        """
        Select a slice with the holes in context. An optional 4 point area of interest (AOI) can be added to be represented in the UI too.
        
        :param aoix1:  1st Corner of AOI - X
        :param aoiy1:  1st Corner of AOI - Y
        :param aoix2:  2nd Corner of AOI - X
        :param aoiy2:  2nd Corner of AOI - Y
        :param aoix3:  3rd Corner of AOI - X
        :param aoiy3:  3rd Corner of AOI - Y
        :param aoix4:  4th Corner of AOI - X
        :param aoiy4:  4th Corner of AOI - Y
        :param x1:     Returned slice 1st point - X
        :param y1:     Returned slice 1st point - Y
        :param x2:     Returned slice 2nd point - X
        :param y2:     Returned slice 2nd point - Y
        :type  aoix1:  float
        :type  aoiy1:  float
        :type  aoix2:  float
        :type  aoiy2:  float
        :type  aoix3:  float
        :type  aoiy3:  float
        :type  aoix4:  float
        :type  aoiy4:  float
        :type  x1:     float_ref
        :type  y1:     float_ref
        :type  x2:     float_ref
        :type  y2:     float_ref

        :returns:      0  - Ok
                       -1 - User Cancelled
        :rtype:        int

        .. versionadded:: 7.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val, x1.value, y1.value, x2.value, y2.value = self._slice_selection_tool_gui(aoix1, aoiy1, aoix2, aoiy2, aoix3, aoiy3, aoix4, aoiy4, x1.value, y1.value, x2.value, y2.value)
        return ret_val




    def update_survey_from_collar(self, hole):
        """
        Update the Survey table from the collar info.
        
        :param hole:  Hole index
        :type  hole:  int

        :returns:     0 - No change; there is no survey table, the table was empty, or values were same as collar
                      1 - Survey table updated; values changed and there is just one row.
                      2 - Survey table unchanged; there was more than one row in the table, and values were different
        :rtype:       int

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Call when the collar values are edited to update the survey table
        values. If the survey contains more than one row, then no changes
        are applied, and no warning or error is registered.
        """
        ret_val = self._update_survey_from_collar(hole)
        return ret_val




    def load_data_parameters_ini(self, db, dir):
        """
        Load data parameters from INI files..
        
        :param db:   Source database
        :param dir:  Directory to store INI files
        :type  db:   GXDB
        :type  dir:  str

        .. versionadded:: 6.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Wholeplot data graphing parameters for each channel are stored
        in the channel `GXREG <geosoft.gxapi.GXREG>`. This function lets a user transfer pre-defined
        settings to individual INI files (eg. cu.ini).
        """
        self._load_data_parameters_ini(db, dir.encode())
        




    def load_plot_parameters(self, ini, type):
        """
        Load parameters from a Job into the Drill object.
        
        :param ini:   The job file file to read
        :param type:  :ref:`DH_PLOT`
        :type  ini:   str
        :type  type:  int

        .. versionadded:: 6.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._load_plot_parameters(ini.encode(), type)
        




    def load_select(self, file):
        """
        Load selections to from a file.
        
        :param file:  File Name
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._load_select(file.encode())
        




    def mask_ply(self, pply, ipj, tol, mask, select, append):
        """
        Set mask channel based on view selection polygon.
        
        :param pply:    Masking polygon
        :param ipj:     Projection from data to polygon coordinates
        :param tol:     Slice thickness - `rDUMMY <geosoft.gxapi.rDUMMY>` for no limiting thickness
        :param mask:    Name of mask channel
        :param select:  :ref:`DH_HOLES`
        :param append:  :ref:`DH_MASK`
        :type  pply:    GXPLY
        :type  ipj:     GXIPJ
        :type  tol:     float
        :type  mask:    str
        :type  select:  int
        :type  append:  int

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Data values inside the polygon area, and within the slice thickness
        have their mask channel values set to 1.
        If the specified mask channel does not exist, it is created.
        `DH_MASK_NEW <geosoft.gxapi.DH_MASK_NEW>` --- Mask is created new for each selected hole
        `DH_MASK_APPEND <geosoft.gxapi.DH_MASK_APPEND>` --- Current selection is added to previous.
        """
        self._mask_ply(pply, ipj, tol, mask.encode(), select, append)
        



    @classmethod
    def open(cls, db):
        """
        Open `GXDH <geosoft.gxapi.GXDH>` from collar database and load all associated databases.
        
        :param db:  Name of collar database
        :type  db:  str

        :returns:    `GXDH <geosoft.gxapi.GXDH>` Object
        :rtype:      GXDH

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapDH._open(GXContext._get_tls_geo(), db.encode())
        return GXDH(ret_val)




    def open_job(self, job, type):
        """
        Open a `GXDH <geosoft.gxapi.GXDH>` plotting job
        
        :param job:   Job file name
        :param type:  :ref:`DH_PLOT`
        :type  job:   str
        :type  type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._open_job(job.encode(), type)
        




    def plot_hole_traces(self, map, job):
        """
        Plot hole traces to a regular (plan) map.
        
        :param map:  Map handle
        :param job:  Parameter file (INI) name
        :type  map:  GXMAP
        :type  job:  str

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Both the hole traces and data can be plotted.
        The DHPLANHOLES GX uses the default plan map parameter file
        "_plan.inp".
        """
        self._plot_hole_traces(map, job.encode())
        




    def plot_hole_traces_3d(self, mview, job):
        """
        Plot hole traces to an existing 3D map view.
        
        :param mview:  Existing 3D map view
        :param job:    Parameter file (INI) name (normally ``*.in3``)
        :type  mview:  GXMVIEW
        :type  job:    str

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Both the hole traces and data can be plotted.
        The DH3DHOLES GX uses the default 3D map parameter file
        "_3D.in3".
        """
        self._plot_hole_traces_3d(mview, job.encode())
        




    def plot_symbols_3d(self, mview, job):
        """
        Plot 3D symbols to an existing 3D map view.
        
        :param mview:  Existing 3D map view
        :param job:    Parameter file (INI) name (normally ``*.in3``)
        :type  mview:  GXMVIEW
        :type  job:    str

        .. versionadded:: 9.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._plot_symbols_3d(mview, job.encode())
        




    def qa_collar(self, wa):
        """
        Do QA/QC on Hole Collar data.
        
        :param wa:  `GXWA <geosoft.gxapi.GXWA>` Handle
        :type  wa:  GXWA

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._qa_collar(wa)
        




    def qa_collar_lst(self, lst, wa):
        """
        Do QA/QC on Hole Collar data - `GXLST <geosoft.gxapi.GXLST>` of holes.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` of holes (Name, Index)
        :param wa:   `GXWA <geosoft.gxapi.GXWA>` Handle
        :type  lst:  GXLST
        :type  wa:   GXWA

        .. versionadded:: 7.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._qa_collar_lst(lst, wa)
        




    def qa_dip_az_curvature(self, wa, tolerance):
        """
        Do QA/QC Curvature checking on Dip Azimuth data.
        
        :param wa:         `GXWA <geosoft.gxapi.GXWA>` Handle
        :param tolerance:  Dip/Azimuth curvature tolerance (degree per meter)
        :type  wa:         GXWA
        :type  tolerance:  float

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Checks all holes with Dip-Azimuth survey data
        """
        self._qa_dip_az_curvature(wa, tolerance)
        




    def qa_dip_az_curvature2(self, wa, tolerance, hole):
        """
        Do QA/QC Curvature checking on Dip Azimuth data for a single hole.
        
        :param wa:         `GXWA <geosoft.gxapi.GXWA>` Handle
        :param tolerance:  Dip/Azimuth curvature tolerance (degree per meter)
        :param hole:       Hole name
        :type  wa:         GXWA
        :type  tolerance:  float
        :type  hole:       str

        .. versionadded:: 6.4.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Checks single hole with Dip-Azimuth survey data
        """
        self._qa_dip_az_curvature2(wa, tolerance, hole.encode())
        




    def qa_dip_az_survey(self, db, wa, line, hole):
        """
        Do QA/QC on Dip/Az Survey data.
        
        :param db:    `GXDB <geosoft.gxapi.GXDB>` Handle
        :param wa:    `GXWA <geosoft.gxapi.GXWA>` Handle
        :param line:  Line
        :param hole:  Current hole Name
        :type  db:    GXDB
        :type  wa:    GXWA
        :type  line:  int
        :type  hole:  str

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Error if no Dip-Azimuth survey database, or if
        the requested line does not exist in the database.
        """
        self._qa_dip_az_survey(db, wa, line, hole.encode())
        




    def qa_east_north_curvature(self, wa, tolerance):
        """
        Do QA/QC Curvature checking on Dip Azimuth data.
        
        :param wa:         `GXWA <geosoft.gxapi.GXWA>` Handle
        :param tolerance:  Dip/Azimuth curvature tolerance (degree per meter)
        :type  wa:         GXWA
        :type  tolerance:  float

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Checks all holes with East-North survey data
        """
        self._qa_east_north_curvature(wa, tolerance)
        




    def qa_east_north_curvature2(self, wa, tolerance, hole):
        """
        Do QA/QC Curvature checking on Dip Azimuth data for a single hole.
        
        :param wa:         `GXWA <geosoft.gxapi.GXWA>` Handle
        :param tolerance:  Dip/Azimuth curvature tolerance (degree per meter)
        :param hole:       Hole name
        :type  wa:         GXWA
        :type  tolerance:  float
        :type  hole:       str

        .. versionadded:: 6.4.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Checks single holes with East-North survey data
        """
        self._qa_east_north_curvature2(wa, tolerance, hole.encode())
        




    def qa_east_north_survey(self, db, wa, line, hole):
        """
        Do QA/QC on East/North Survey data.
        
        :param db:    `GXDB <geosoft.gxapi.GXDB>` Handle
        :param wa:    `GXWA <geosoft.gxapi.GXWA>` Handle
        :param line:  Line
        :param hole:  Current hole Name
        :type  db:    GXDB
        :type  wa:    GXWA
        :type  line:  int
        :type  hole:  str

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Error if no East-North survey database, or if
        the requested line does not exist in the database.
        """
        self._qa_east_north_survey(db, wa, line, hole.encode())
        




    def qa_from_to_data(self, db, wa, line, hole):
        """
        Do QA/QC on From/To data.
        
        :param db:    `GXDB <geosoft.gxapi.GXDB>` Handle
        :param wa:    `GXWA <geosoft.gxapi.GXWA>` Handle
        :param line:  Line
        :param hole:  Current hole Name
        :type  db:    GXDB
        :type  wa:    GXWA
        :type  line:  int
        :type  hole:  str

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._qa_from_to_data(db, wa, line, hole.encode())
        




    def qa_point_data(self, db, wa, line, hole):
        """
        Do QA/QC on Point data.
        
        :param db:    `GXDB <geosoft.gxapi.GXDB>` Handle
        :param wa:    `GXWA <geosoft.gxapi.GXWA>` Handle
        :param line:  Line
        :param hole:  Current hole Name
        :type  db:    GXDB
        :type  wa:    GXWA
        :type  line:  int
        :type  hole:  str

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._qa_point_data(db, wa, line, hole.encode())
        




    def qa_write_unregistered_holes(self, db, wa):
        """
        Write out unregistered holes in a database.
        
        :param db:  `GXDB <geosoft.gxapi.GXDB>` Handle (not the collar table)
        :param wa:  `GXWA <geosoft.gxapi.GXWA>` Handle
        :type  db:  GXDB
        :type  wa:  GXWA

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Looks at each line in a database and sees if it is listed in
        the collar tables' hole list.
        """
        self._qa_write_unregistered_holes(db, wa)
        




    def replot_holes(self, job, plot_type):
        """
        Replot holes on an existing drill map.
        
        :param job:        Parameter (INI) name
        :param plot_type:  :ref:`DH_PLOT`
        :type  job:        str
        :type  plot_type:  int

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The parameter file must correspond to the plot Type.
        The hDH->hMAP value must be set first, using `set_map <geosoft.gxapi.GXDH.set_map>`.
        Overwrites existing hole and hole data groups.
        Replots the legend if the legend is enabled.
        This should only be used on a slightly modified version of the
        INI file used to create the existing map, or things may not
        work out (e.g. bad locations etc).
        """
        self._replot_holes(job.encode(), plot_type)
        




    def plot_holes_on_section(self, job, plot_type, view):
        """
        Plot the currently selected holes on an existing section view.
        
        :param job:        Parameter (INI) name
        :param plot_type:  :ref:`DH_PLOT` Section plot type (`DH_PLOT_SECTION <geosoft.gxapi.DH_PLOT_SECTION>` or `DH_PLOT_SECTION_CROOKED <geosoft.gxapi.DH_PLOT_SECTION_CROOKED>`
        :param view:       View name
        :type  job:        str
        :type  plot_type:  int
        :type  view:       str

        .. versionadded:: 8.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Plot the currently selected holes to a section view.
        """
        self._plot_holes_on_section(job.encode(), plot_type, view.encode())
        




    def re_survey_east_north(self, hole, vv_x, vv_y, vv_z, vv_d, east, north, elev, top, bot):
        """
        Resurvey an East-North-RL survey.
        
        :param hole:   Hole ID (for error messages)
        :param vv_x:   Input East
        :param vv_y:   Input North
        :param vv_z:   Input RL
        :param vv_d:   Returned depths down the hole
        :param east:   Input collar East
        :param north:  Input collar North
        :param elev:   Input collar RL
        :param top:    Input top of hole depth
        :param bot:    Returned bottom depth
        :type  hole:   str
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV
        :type  vv_z:   GXVV
        :type  vv_d:   GXVV
        :type  east:   float
        :type  north:  float
        :type  elev:   float
        :type  top:    float
        :type  bot:    float_ref

        .. versionadded:: 5.1.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Re-interpolates in X, Y and Z to proper depth interval
        and returns depths for each point
        """
        bot.value = self._re_survey_east_north(hole.encode(), vv_x, vv_y, vv_z, vv_d, east, north, elev, top, bot.value)
        




    def re_survey_pol_fit(self, hole, vv_dip, vv_az, vv_depth, east, north, elev, top, bot, inc, dip_conv, order, vv_x, vv_y, vv_z, vv_d):
        """
        Use the polynomial fit resurveying method.
        
        :param hole:      Hole ID (used for error messages)
        :param vv_dip:    Dip
        :param vv_az:     Azimuth
        :param vv_depth:  Depth
        :param east:      Collar X (easting) (depth = 0)
        :param north:     Collar Y (northing)(depth = 0)
        :param elev:      Collar Z (elevation) (depth = 0)
        :param top:       Minimum hole depth to start output values
        :param bot:       Maximum hole depth for output values
        :param inc:       Increment for output values
        :param dip_conv:  :ref:`DIP_CONVENTION`
        :param order:     Polynomial order
        :param vv_x:      X (Easting) - Output
        :param vv_y:      Y (Northin) - Output
        :param vv_z:      Z (Elevation) - Output
        :param vv_d:      Depths - Output
        :type  hole:      str
        :type  vv_dip:    GXVV
        :type  vv_az:     GXVV
        :type  vv_depth:  GXVV
        :type  east:      float
        :type  north:     float
        :type  elev:      float
        :type  top:       float
        :type  bot:       float
        :type  inc:       float
        :type  dip_conv:  int
        :type  order:     int
        :type  vv_x:      GXVV
        :type  vv_y:      GXVV
        :type  vv_z:      GXVV
        :type  vv_d:      GXVV

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Uses the polynomial fit method to calculate (X, Y, Z)
        locations down the hole from azimuth, dip, depth values.
        The collar is assumed to be at zero depth, and depth is the
        measure distance down the hole (even if it's horizontal).
        A negative dip convention means vertical down is -90 degrees.
        The polynomial order must be in the range 1-20, with 5 being adequate
        for most smoothly curving holes. The order is reduced to no more than
        the number of input points.
        """
        self._re_survey_pol_fit(hole.encode(), vv_dip, vv_az, vv_depth, east, north, elev, top, bot, inc, dip_conv, order, vv_x, vv_y, vv_z, vv_d)
        




    def re_survey_rad_curve(self, hole, vv_dip, vv_az, vv_depth, east, north, elev, top, bot, inc, dip_conv, vv_x, vv_y, vv_z, vv_d):
        """
        Use radius of curvature resurveying method.
        
        :param hole:      Hole ID (used for error messages)
        :param vv_dip:    Dip
        :param vv_az:     Azimuth
        :param vv_depth:  Depth
        :param east:      Collar X (easting) (depth = 0)
        :param north:     Collar Y (northing)(depth = 0)
        :param elev:      Collar Z (elevation) (depth = 0)
        :param top:       Minimum hole depth to start output values
        :param bot:       Maximum hole depth for output values
        :param inc:       Increment for output values
        :param dip_conv:  :ref:`DIP_CONVENTION`
        :param vv_x:      X (Easting) - Output
        :param vv_y:      Y (Northin) - Output
        :param vv_z:      Z (Elevation) - Output
        :param vv_d:      Depths - Output
        :type  hole:      str
        :type  vv_dip:    GXVV
        :type  vv_az:     GXVV
        :type  vv_depth:  GXVV
        :type  east:      float
        :type  north:     float
        :type  elev:      float
        :type  top:       float
        :type  bot:       float
        :type  inc:       float
        :type  dip_conv:  int
        :type  vv_x:      GXVV
        :type  vv_y:      GXVV
        :type  vv_z:      GXVV
        :type  vv_d:      GXVV

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Uses the Radius of curvature method to calculate (X, Y, Z)
        locations down the hole from azimuth, dip, depth values.
        The collar is assumed to be at zero depth, and depth is the
        measure distance down the hole (even if it's horizontal).
        A negative dip convention means vertical down is -90 degrees.
        """
        self._re_survey_rad_curve(hole.encode(), vv_dip, vv_az, vv_depth, east, north, elev, top, bot, inc, dip_conv, vv_x, vv_y, vv_z, vv_d)
        




    def re_survey_straight(self, hole, dip, az, east, north, elev, top, bot, inc, dip_conv, vv_x, vv_y, vv_z, vv_d):
        """
        Resurvey a straight hole.
        
        :param hole:      Hole ID (used for error messages)
        :param dip:       Collar Dip
        :param az:        Collar Azimuth
        :param east:      Collar X (easting) (depth = 0)
        :param north:     Collar Y (northing)(depth = 0)
        :param elev:      Collar Z (elevation) (depth = 0)
        :param top:       Minimum hole depth to start output values
        :param bot:       Maximum hole depth for output values
        :param inc:       Increment for output values
        :param dip_conv:  :ref:`DIP_CONVENTION`
        :param vv_x:      X (Easting) - Output
        :param vv_y:      Y (Northin) - Output
        :param vv_z:      Z (Elevation) - Output
        :param vv_d:      Depths - Output
        :type  hole:      str
        :type  dip:       float
        :type  az:        float
        :type  east:      float
        :type  north:     float
        :type  elev:      float
        :type  top:       float
        :type  bot:       float
        :type  inc:       float
        :type  dip_conv:  int
        :type  vv_x:      GXVV
        :type  vv_y:      GXVV
        :type  vv_z:      GXVV
        :type  vv_d:      GXVV

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Assumes a straight hole to calculate (X, Y, Z)
        locations down the hole from azimuth, dip, depth values.
        The collar is assumed to be at zero depth, and depth is the
        measure distance down the hole (even if it's horizontal).
        A negative dip convention means vertical down is -90 degrees.
        """
        self._re_survey_straight(hole.encode(), dip, az, east, north, elev, top, bot, inc, dip_conv, vv_x, vv_y, vv_z, vv_d)
        




    def re_survey_straight_seg(self, hole, vv_dip, vv_az, vv_depth, east, north, elev, top, bot, inc, dip_conv, vv_x, vv_y, vv_z, vv_d):
        """
        Resurvey a hole with straight segments between locations.
        
        :param hole:      Hole ID (used for error messages)
        :param vv_dip:    Dip
        :param vv_az:     Azimuth
        :param vv_depth:  Depth
        :param east:      Collar X (easting) (depth = 0)
        :param north:     Collar Y (northing)(depth = 0)
        :param elev:      Collar Z (elevation) (depth = 0)
        :param top:       Minimum hole depth to start output values
        :param bot:       Maximum hole depth for output values
        :param inc:       Increment for output values
        :param dip_conv:  :ref:`DIP_CONVENTION`
        :param vv_x:      X (Easting) - Output
        :param vv_y:      Y (Northin) - Output
        :param vv_z:      Z (Elevation) - Output
        :param vv_d:      Depths - Output
        :type  hole:      str
        :type  vv_dip:    GXVV
        :type  vv_az:     GXVV
        :type  vv_depth:  GXVV
        :type  east:      float
        :type  north:     float
        :type  elev:      float
        :type  top:       float
        :type  bot:       float
        :type  inc:       float
        :type  dip_conv:  int
        :type  vv_x:      GXVV
        :type  vv_y:      GXVV
        :type  vv_z:      GXVV
        :type  vv_d:      GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Calculate (X, Y, Z) locations down the hole from azimuth, dip,
        depth values, assuming each segment is straight, and the hole
        bends at each successive azimuth, dip, depth value.
        The collar is assumed to be at zero depth, and depth is the
        measure distance down the hole (even if it's horizontal).
        A negative dip convention means vertical down is -90 degrees.
        """
        self._re_survey_straight_seg(hole.encode(), vv_dip, vv_az, vv_depth, east, north, elev, top, bot, inc, dip_conv, vv_x, vv_y, vv_z, vv_d)
        




    def save_data_parameters_ini(self, db, dir):
        """
        Save data parameters to INI files..
        
        :param db:   Source database
        :param dir:  Directory to store INI files
        :type  db:   GXDB
        :type  dir:  str

        .. versionadded:: 6.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Wholeplot data graphing parameters for each channel are stored
        in the channel `GXREG <geosoft.gxapi.GXREG>`. This function lets a user transfer pre-defined
        settings to individual INI files (eg. cu.ini).
        As of v6.3, the `GXDH <geosoft.gxapi.GXDH>` object is NOT required for this function, and
        is, in fact, ignored.
        """
        self._save_data_parameters_ini(db, dir.encode())
        




    def save_job(self, job, type):
        """
        Save a `GXDH <geosoft.gxapi.GXDH>` plotting job
        
        :param job:   Job file name
        :param type:  :ref:`DH_PLOT`
        :type  job:   str
        :type  type:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._save_job(job.encode(), type)
        




    def save_select(self, file):
        """
        Saves current selections to a file.
        
        :param file:  File Name
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._save_select(file.encode())
        




    def section_window_size_mm(self, xmm, ymm):
        """
        Deterine the size, in mm, of the section window
        
        :param xmm:  X size in mm.
        :param ymm:  Y size in mm.
        :type  xmm:  float_ref
        :type  ymm:  float_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Given the current selection of windows (e.g. legend, plan),
        paper size and orientation, return the size in mm of the
        window used for plotting the section.
        """
        xmm.value, ymm.value = self._section_window_size_mm(xmm.value, ymm.value)
        




    def select_all_holes(self):
        """
        Select all the holes in a Drill hole project.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._select_all_holes()
        




    def select_holes(self, gvv, sel):
        """
        Select holes by hole indices.
        
        :param gvv:  INT `GXVV <geosoft.gxapi.GXVV>` with hole indices.
        :param sel:  0 - deselect, 1 - select
        :type  gvv:  GXVV
        :type  sel:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Indices less than 0 are skipped. This lets you use this function
        after a call to `GXLST.find_items <geosoft.gxapi.GXLST.find_items>`, which returns -1 for indices not located.
        """
        self._select_holes(gvv, sel)
        




    def select_name(self, mask, sel, mode):
        """
        Select holes using a name mask.
        
        :param mask:  Mask
        :param sel:   0 - deselect, 1 - select
        :param mode:  0 - overwrite, 1 - append
        :type  mask:  str
        :type  sel:   int
        :type  mode:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Overwrite mode - all selections tested and selected or not selected
        Append mode    - only holes matching the mask are selected or not selected.
        """
        self._select_name(mask.encode(), sel, mode)
        




    def select_ply(self, pply):
        """
        Select all holes in `GXPLY <geosoft.gxapi.GXPLY>` (Polygon) object.
        
        :param pply:  Polygon object
        :type  pply:  GXPLY

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** This function operates the same as the `select_ply2 <geosoft.gxapi.GXDH.select_ply2>` method 
        with parameters ``(1, 0, 0)``
        """
        self._select_ply(pply)
        




    def select_ply2(self, pply, select, inside, new):
        """
        Select holes in `GXPLY <geosoft.gxapi.GXPLY>` (Polygon) object with options.
        
        :param pply:    Polygon object
        :param select:  Select (0) or Deselect (1)
        :param inside:  Region (0: inside, 1: outside)
        :param new:     Mode (0: Append, 1: New)
        :type  pply:    GXPLY
        :type  select:  int
        :type  inside:  int
        :type  new:     int

        .. versionadded:: 6.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The various selection options give the following results:

        New/Select/inside: Unselect all holes, then
                           select all holes inside the polygon.
        New/Select/outside: Unselect all holes, then
                           select all holes outside the polygon.
        New/Deselect/inside: Select all holes, then
                           deselect all holes inside the polygon.
        New/Deselect/outside: Select all holes, then
                           deselect all holes outside the polygon.

        Append/Select/inside: Select all holes inside the polygon.
                              Leave selections outside as is.
        Append/Select/outside: Select all holes outside the polygon.
                              Leave selections inside as is.
        Append/Deselect/inside: Deselect all holes inside the polygon
                              Leave selections outside as is.
        Append/Deselect/outside: Deselect all holes outside the polygon.
                              Leave selections inside as is.
        """
        self._select_ply2(pply, select, inside, new)
        




    def set_crooked_section_ipj(self, ipj):
        """
        Pass the Crooked projection required for plotting to a crooked section.
        
        :param ipj:  Crooked Section `GXIPJ <geosoft.gxapi.GXIPJ>`
        :type  ipj:  GXIPJ

        .. versionadded:: 7.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** This might be extracted from an existing crooked section view, or created from a database line.
        """
        self._set_crooked_section_ipj(ipj)
        




    def set_current_view_name(self, cur_view):
        """
        Set the current map view name.
        
        :param cur_view:  View name
        :type  cur_view:  str

        .. versionadded:: 7.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Can be used to specify the name of the view to plot into.
        """
        self._set_current_view_name(cur_view.encode())
        




    def set_info(self, hole, name, data):
        """
        Set Collar Information.
        
        :param hole:  Hole index
        :param name:  Name of information
        :param data:  Information
        :type  hole:  int
        :type  name:  str
        :type  data:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** If the DH_ELEV channel is requested it will also
        search for the DH_RL channel, which is the new
        name for the collar elevation.
        """
        self._set_info(hole, name.encode(), data.encode())
        




    def set_ipj(self, ipj):
        """
        Set the project `GXIPJ <geosoft.gxapi.GXIPJ>`.
        
        :param ipj:  `GXIPJ <geosoft.gxapi.GXIPJ>` Handle
        :type  ipj:  GXIPJ

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The projection for the project is the projection stored
        in the DH_EAST channel in the collar table. This
        function sets the projection of the (DH_EAST, DH_NORTH)
        channel pairs in each of the project databases to the
        input `GXIPJ <geosoft.gxapi.GXIPJ>`.
        The input `GXIPJ <geosoft.gxapi.GXIPJ>` cannot be a geographic coordinate system
        or this call will fail with an error message.
        """
        self._set_ipj(ipj)
        




    def set_map(self, map):
        """
        Store the current `GXMAP <geosoft.gxapi.GXMAP>` to the `GXDH <geosoft.gxapi.GXDH>` object.
        
        :param map:  `GXIPJ <geosoft.gxapi.GXIPJ>` Handle
        :type  map:  GXMAP

        .. versionadded:: 7.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Use this before calling the ReplotHoles functions,
        so that, instead of creating a new map, the plotting
        functions use the existing one.
        """
        self._set_map(map)
        




    def set_new_ipj(self, db):
        """
        Set a new project database projection to collar table projection.
        
        :param db:  Project database name
        :type  db:  str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** Gets the `GXIPJ <geosoft.gxapi.GXIPJ>` of the collar table current x channel and copies it
        into the named database (as long as it is in the project!)
        """
        self._set_new_ipj(db.encode())
        




    def set_selected_holes_vv(self, vv, append):
        """
        Set hole selection using hole indices.
        
        :param vv:      Input hole indices (must be type INT)
        :param append:  0 - overwrite, 1 - append
        :type  vv:      GXVV
        :type  append:  int

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._set_selected_holes_vv(vv, append)
        



    @classmethod
    def set_template_blob(cls, db, template, imp_type):
        """
        Store the import template to the database.
        
        :param db:        `GXDB <geosoft.gxapi.GXDB>` Handle
        :param template:  Import template name
        :param imp_type:  :ref:`DH_DATA`
        :type  db:        GXDB
        :type  template:  str
        :type  imp_type:  int

        .. versionadded:: 6.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The template can later be retrieved in order to refresh the
        database with a call to the DHIMPORT.GX.

        The import types correspond to the DHIMPORT.IMPTYPE variable:
        0: ASCII, 1: Database/XLS, 2: ODBC
        """
        gxapi_cy.WrapDH._set_template_blob(GXContext._get_tls_geo(), db, template.encode(), imp_type)
        




    def significant_intersections_db(self, mast_db, comp_db, hol_sel, assay_ch, cut_off_grade, clip_grade, min_composite_thickness, min_composite_grade, max_internal_dilution_length, min_internal_dilution_grade, grade_for_missing_assays):
        """
        Make a report of Significant Intersections
        
        :param mast_db:                       Input assay `GXDB <geosoft.gxapi.GXDB>` object
        :param comp_db:                       Output composite `GXDB <geosoft.gxapi.GXDB>` object
        :param hol_sel:                       :ref:`DH_COMPSTDB_HOLSEL`
        :param assay_ch:                      The primary assay channel.
        :param cut_off_grade:                 Minimum Cut off grade for Primary Assay
        :param clip_grade:                    Maximum Cut off grade for Primary Assay
        :param min_composite_thickness:       Minimum Composite Length
        :param min_composite_grade:           Minimum Composite thickness
        :param max_internal_dilution_length:  Maximum Internal Dilution
        :param min_internal_dilution_grade:   Minimum diluted grade
        :param grade_for_missing_assays:      Grade for Missing Assays
        :type  mast_db:                       GXDB
        :type  comp_db:                       GXDB
        :type  hol_sel:                       int
        :type  assay_ch:                      str
        :type  cut_off_grade:                 float
        :type  clip_grade:                    float
        :type  min_composite_thickness:       float
        :type  min_composite_grade:           float
        :type  max_internal_dilution_length:  float
        :type  min_internal_dilution_grade:   float
        :type  grade_for_missing_assays:      float

        .. versionadded:: 7.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._significant_intersections_db(mast_db, comp_db, hol_sel, assay_ch.encode(), cut_off_grade, clip_grade, min_composite_thickness, min_composite_grade, max_internal_dilution_length, min_internal_dilution_grade, grade_for_missing_assays)
        




    def test_import_las(self, assay, file, interval, wa, warn):
        """
        Tests import of LAS Data for problems.
        
        :param assay:     Assay table name
        :param file:      LAS file name
        :param interval:  Averaging/desampling interval
        :param wa:        Log file handle
        :param warn:      1 returned if problems found
        :type  assay:     str
        :type  file:      str
        :type  interval:  float
        :type  wa:        GXWA
        :type  warn:      int_ref

        .. versionadded:: 6.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** See `import_las <geosoft.gxapi.GXDH.import_las>`.
        Determines if the import of the LAS data will result in data
        being overwritten, interpolated or resampled. Warnings are written to a log
        file, as in sImportLAS_DH. Warnings are not registered in cases
        where data is merely extended at the start or the end with dummies
        to match a different interval down the hole.
        """
        warn.value = self._test_import_las(assay.encode(), file.encode(), interval, wa, warn.value)
        




    def un_select_all_holes(self):
        """
        Unselect all the holes in a Drill hole project.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._un_select_all_holes()
        




    def un_selected_hole_lst(self, lst):
        """
        Populate an `GXLST <geosoft.gxapi.GXLST>` with the list of the unselected holes
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` handle
        :type  lst:  GXLST

        .. versionadded:: 6.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._un_selected_hole_lst(lst)
        




    def update_collar_table(self):
        """
        Update all collar table information.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._update_collar_table()
        




    def update_hole_extent(self, hole):
        """
        Update extents for one hole.
        
        :param hole:  Hole index
        :type  hole:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._update_hole_extent(hole)
        




    def wholeplot(self, job, plot_type):
        """
        Run a Wholeplot plot job.
        
        :param job:        Parameter (INI) name
        :param plot_type:  :ref:`DH_PLOT`
        :type  job:        str
        :type  plot_type:  int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_

        **Note:** The parameter file must correspond to the plot Type. The INI file
        contains settings for all of the non-database data related
        parameters (e.g. Map template, scale, boundaries,
        section definitions, hole trace parameters etc...)
        """
        self._wholeplot(job.encode(), plot_type)
        




    def surface_intersections(self, output_db, input_geosurface_or_grid, hole_selection):
        """
        Determine intersections of drillholes with a surface.
        
        :param output_db:                 Output `GXDB <geosoft.gxapi.GXDB>` Handle
        :param input_geosurface_or_grid:  Input surface file
        :param hole_selection:            Selected holes (1), All holes (0)
        :type  output_db:                 GXDB
        :type  input_geosurface_or_grid:  str
        :type  hole_selection:            int

        .. versionadded:: 8.3

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        self._surface_intersections(output_db, input_geosurface_or_grid.encode(), hole_selection)
        



    @classmethod
    def get_mx_deposit_rights_info(cls, has_rights, base_url, api_version_prefix, api_key, user_key, database_id):
        """
        Get MX Deposit Service API information via Geosoft ID rights.
        
        :param has_rights:          Does Geosoft ID have rights to access MX Deposit?
        :param base_url:            Base URL
        :param api_version_prefix:  API Version Prefix
        :param api_key:             API Key
        :param user_key:            User Key
        :param database_id:         Database ID
        :type  has_rights:          bool_ref
        :type  base_url:            str_ref
        :type  api_version_prefix:  str_ref
        :type  api_key:             str_ref
        :type  user_key:            str_ref
        :type  database_id:         str_ref

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        has_rights.value, base_url.value, api_version_prefix.value, api_key.value, user_key.value, database_id.value = gxapi_cy.WrapDH._get_mx_deposit_rights_info(GXContext._get_tls_geo(), has_rights.value, base_url.value.encode(), api_version_prefix.value.encode(), api_key.value.encode(), user_key.value.encode(), database_id.value.encode())
        



    @classmethod
    def navigate_to_mx_deposit(cls, select_type, select_id):
        """
        Navigate to MX Deposit portal
        
        :param select_type:  Selection Type
        :param select_id:    Selection ID
        :type  select_type:  str
        :type  select_id:    str

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapDH._navigate_to_mx_deposit(GXContext._get_tls_geo(), select_type.encode(), select_id.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer