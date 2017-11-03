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
class GXSEMPLOT(gxapi_cy.WrapSEMPLOT):
    """
    GXSEMPLOT class.

    Oasis montaj implementation of RTE `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>`
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>`
        
        :returns: A null `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>`
        :rtype:   GXSEMPLOT
        """
        return GXSEMPLOT()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def apply_filter_to_mask(cls, db, filter, mask_ch, mineral_ch, mineral, mode):
        """
        Apply the filter to the mask channel
        
        :param db:          Database handle
        :param filter:      Filter name
        :param mask_ch:     Mask channel name
        :param mineral_ch:  Mineral channel name
        :param mineral:     Mineral to use ("All" or "" for all)
        :param mode:        Mask mode (0: Append, 1: New)
        :type  db:          GXDB
        :type  filter:      str
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  mineral:     str
        :type  mode:        int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The mask channel is updated for the current data to reflect
        the actions of the filter. Those values passing get 1, those
        failing get 0.
        """
        gxapi_cy.WrapSEMPLOT._apply_filter_to_mask(GXContext._get_tls_geo(), db, filter.encode(), mask_ch.encode(), mineral_ch.encode(), mineral.encode(), mode)
        



    @classmethod
    def convert_dummies(cls, db, line):
        """
        Convert dummies to zero values for assay channels.
        
        :param db:    Database handle
        :param line:  Input line to convert
        :type  db:    GXDB
        :type  line:  int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The is operation is controlled by the Preferences
        "Use dummies to indicate no data?" By default, this option is "yes"
        so this function will return with no changes. However, if
        "no", then all ASSAY class channels will have dummy values
        converted to 0.0.
        """
        gxapi_cy.WrapSEMPLOT._convert_dummies(GXContext._get_tls_geo(), db, line)
        



    @classmethod
    def create_groups(cls, db, mask_ch):
        """
        Group data by anomaly or string channel - Interactive.
        
        :param db:       Database handle
        :param mask_ch:  Mask channel
        :type  db:       GXDB
        :type  mask_ch:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._create_groups(GXContext._get_tls_geo(), db, mask_ch.encode())
        



    @classmethod
    def default_groups(cls, db):
        """
        Group data by selected anomalies.
        
        :param db:  Database handle
        :type  db:  GXDB

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._default_groups(GXContext._get_tls_geo(), db)
        



    @classmethod
    def edit_map_plot_parameters(cls, db, mask_ch, mineral_ch, map, view):
        """
        Alter parameters in an XYplot Triplot map.
        
        :param db:          Database handle
        :param mask_ch:     Mask channel (can be "")
        :param mineral_ch:  Mineral channel (can be "" for raw data)
        :param map:         Map handle
        :param view:        Map View
        :type  db:          GXDB
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  map:         GXMAP
        :type  view:        str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The Parameters `GXGUI <geosoft.gxapi.GXGUI>` is loaded based on settings stored in
        the map. The map is then re-plotted, overwriting the old one,
        based on the new settings. Note that the selection of data
        in the current `GXDB <geosoft.gxapi.GXDB>` is used to replot the map.
        """
        gxapi_cy.WrapSEMPLOT._edit_map_plot_parameters(GXContext._get_tls_geo(), db, mask_ch.encode(), mineral_ch.encode(), map, view.encode())
        



    @classmethod
    def edit_plot_components(cls, db, template):
        """
        Set group names and channels to plot in a template.
        
        :param db:        Database handle
        :param template:  Template name
        :type  db:        GXDB
        :type  template:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The "Components" group in the INI file is edited.
        
        Looks first in user\\etc, then in \\etc.
        Looks first for file prefix "semtemplate" then "xyt" or "tri"
        The altered template will be output to the user\\etc directory with
        the file extension "semtemplate".
        """
        gxapi_cy.WrapSEMPLOT._edit_plot_components(GXContext._get_tls_geo(), db, template.encode())
        



    @classmethod
    def edit_plot_parameters(cls, db, template):
        """
        Set TriPlot parameters in a template.
        
        :param db:        Database handle
        :param template:  Template name
        :type  db:        GXDB
        :type  template:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The "Parameters" group in the INI file is edited.
        
        Looks first in user\\etc, then in \\etc.
        Looks first for file prefix "semtemplate" then "xyt" or "tri"
        The altered template will be output to the user\\etc directory with
        the file extension "semtemplate".
        """
        gxapi_cy.WrapSEMPLOT._edit_plot_parameters(GXContext._get_tls_geo(), db, template.encode())
        



    @classmethod
    def export_overlay(cls, overlay, map, mview, group, plot_type, x_stage, x_oxide, y_stage, y_oxide, z_stage, z_oxide, extension):
        """
        Create overlay map and file from a group.
        
        :param overlay:    Overlay file name
        :param map:        Associated map
        :param mview:      View with group
        :param group:      Group name
        :param plot_type:  :ref:`SEMPLOT_PLOT`
        :param x_stage:    XStage
        :param x_oxide:    XOxide
        :param y_stage:    YStage
        :param y_oxide:    YOxide
        :param z_stage:    ZStage
        :param z_oxide:    ZOxide
        :param extension:  :ref:`SEMPLOT_EXT`
        :type  overlay:    str
        :type  map:        str
        :type  mview:      GXMVIEW
        :type  group:      str
        :type  plot_type:  int
        :type  x_stage:    str
        :type  x_oxide:    str
        :type  y_stage:    str
        :type  y_oxide:    str
        :type  z_stage:    str
        :type  z_oxide:    str
        :type  extension:  int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The group is written to a new map, and an overlay file
        is created which points to this map.
        """
        gxapi_cy.WrapSEMPLOT._export_overlay(GXContext._get_tls_geo(), overlay.encode(), map.encode(), mview, group.encode(), plot_type, x_stage.encode(), x_oxide.encode(), y_stage.encode(), y_oxide.encode(), z_stage.encode(), z_oxide.encode(), extension)
        



    @classmethod
    def export_view(cls, db, lst, new_db, view, mask_ch, mineral_ch, mineral):
        """
        Create a "View" database
        
        :param db:          Original raw data database
        :param lst:         List of lines (anomlies) to export
        :param new_db:      Destination database
        :param view:        View to export - One of SEMPLOT_XXX_STAGE
        :param mask_ch:     Mask channel ("" for None)
        :param mineral_ch:  Mineral channel
        :param mineral:     Mineral to export ("" for all)
        :type  db:          GXDB
        :type  lst:         GXLST
        :type  new_db:      GXDB
        :type  view:        int
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  mineral:     str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._export_view(GXContext._get_tls_geo(), db, lst, new_db, view, mask_ch.encode(), mineral_ch.encode(), mineral.encode())
        



    @classmethod
    def export_view2(cls, db, lst, new_db, view, mask_ch, mineral_ch, mineral, export):
        """
        Create a "View" database, with channel selection
        
        :param db:          Original raw data database
        :param lst:         List of lines (anomlies) to export
        :param new_db:      Destination database
        :param view:        View to export - One of SEMPLOT_XXX_STAGE
        :param mask_ch:     Mask channel ("" for None)
        :param mineral_ch:  Mineral channel
        :param mineral:     Mineral to export ("" for all)
        :param export:      :ref:`SEMPLOT_EXPORT` Channel selection
        :type  db:          GXDB
        :type  lst:         GXLST
        :type  new_db:      GXDB
        :type  view:        int
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  mineral:     str
        :type  export:      int

        .. versionadded:: 7.1

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._export_view2(GXContext._get_tls_geo(), db, lst, new_db, view, mask_ch.encode(), mineral_ch.encode(), mineral.encode(), export)
        



    @classmethod
    def filter_lst(cls, lst):
        """
        Fill a `GXLST <geosoft.gxapi.GXLST>` with existing `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>` filters
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` to fill.
        :type  lst:  GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** "Supplied" filters are stored in \\etc, while user-edited and new filters
        are stored in user\\etc. This function finds all files with the extension
        ".semfilter", first in user\\etc, then in \\etc, and adds the file names
        (without the extension) to the `GXLST <geosoft.gxapi.GXLST>`. The name with the extension is stored
        as the value.
        The `GXLST <geosoft.gxapi.GXLST>` is cleared first.
        """
        gxapi_cy.WrapSEMPLOT._filter_lst(GXContext._get_tls_geo(), lst)
        



    @classmethod
    def filter_mineral_pos_data(cls, db, mask_ch, mineral_ch, mineral, pos):
        """
        Filter raw data by position and mineral values
        
        :param db:          Database handle
        :param mask_ch:     Mask channel
        :param mineral_ch:  Mineral channel
        :param mineral:     Mineral (string) - "C", "I" etc.
        :param pos:         Grain position
        :type  db:          GXDB
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  mineral:     str
        :type  pos:         int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The Mask channel will be updated so that those data values
        which "pass" get "1" and those that "fail" get dummy "*"
        NO DATA IS REMOVED.
        Works on all selected lines of data.
        """
        gxapi_cy.WrapSEMPLOT._filter_mineral_pos_data(GXContext._get_tls_geo(), db, mask_ch.encode(), mineral_ch.encode(), mineral.encode(), pos)
        



    @classmethod
    def get_associated_lst(cls, db, group, lst):
        """
        Get the associated channels for this group in a `GXLST <geosoft.gxapi.GXLST>`
        
        :param db:     Database handle
        :param group:  Data Group handle
        :param lst:    `GXLST <geosoft.gxapi.GXLST>` to copy channels into
        :type  db:     GXDB
        :type  group:  int
        :type  lst:    GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._get_associated_lst(GXContext._get_tls_geo(), db, group, lst)
        



    @classmethod
    def get_current_mineral_lst(cls, db, mineral_ch, lst):
        """
        Retrieve `GXLST <geosoft.gxapi.GXLST>` of minerals in selected lines.
        
        :param db:          Database handle
        :param mineral_ch:  Mineral channel name
        :param lst:         `GXLST <geosoft.gxapi.GXLST>` object
        :type  db:          GXDB
        :type  mineral_ch:  str
        :type  lst:         GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** If the mineral channel name is not specified, it returns
        just the "X" (Unknown) item.
        """
        gxapi_cy.WrapSEMPLOT._get_current_mineral_lst(GXContext._get_tls_geo(), db, mineral_ch.encode(), lst)
        



    @classmethod
    def get_current_position_lst(cls, db, lst):
        """
        Retrieve `GXLST <geosoft.gxapi.GXLST>` of positions in selected lines.
        
        :param db:   Database handle
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object
        :type  db:   GXDB
        :type  lst:  GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._get_current_position_lst(GXContext._get_tls_geo(), db, lst)
        



    @classmethod
    def get_full_mineral_lst(cls, lst):
        """
        Retrieve `GXLST <geosoft.gxapi.GXLST>` of all minerals in Semplot_Minerals.csv
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object
        :type  lst:  GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._get_full_mineral_lst(GXContext._get_tls_geo(), lst)
        



    @classmethod
    def get_full_position_lst(cls, lst):
        """
        Retrieve `GXLST <geosoft.gxapi.GXLST>` of all possible mineral positions.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object
        :type  lst:  GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._get_full_position_lst(GXContext._get_tls_geo(), lst)
        



    @classmethod
    def get_grouping_lst(cls, db, lst):
        """
        Get list of items to group symbols by.
        
        :param db:   Database handle
        :param lst:  List to hold items
        :type  db:   GXDB
        :type  lst:  GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The first item is "Anomaly", which gives the line names, The second
        item (if the channel exists in the database) is the Sample Number.
        After this are included all string channels which are NOT oxides or
        elements. (The list can include the mineral).
        Channel symbol is the `GXLST <geosoft.gxapi.GXLST>` value (except for the first item - "Anomaly")
        """
        gxapi_cy.WrapSEMPLOT._get_grouping_lst(GXContext._get_tls_geo(), db, lst)
        



    @classmethod
    def create_ascii_template(cls, name, temp):
        """
        : Generate ASCII import template automatically
        
        :param name:  Data file name
        :param temp:  Template to make
        :type  name:  str
        :type  temp:  str

        :returns:     1 if it succeeds in creating a Template.
                      0 if it fails.
        :rtype:       int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        ret_val = gxapi_cy.WrapSEMPLOT._create_ascii_template(GXContext._get_tls_geo(), name.encode(), temp.encode())
        return ret_val



    @classmethod
    def create_database_template(cls, name, temp):
        """
        Generate database import template automatically
        
        :param name:  Data file name
        :param temp:  Template to make
        :type  name:  str
        :type  temp:  str

        :returns:     1 if it succeeds in creating a Template.
                      0 if it fails.
        :rtype:       int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        ret_val = gxapi_cy.WrapSEMPLOT._create_database_template(GXContext._get_tls_geo(), name.encode(), temp.encode())
        return ret_val



    @classmethod
    def edit_filter(cls, db, filter, mask_ch, mineral_ch, mineral):
        """
        Edit and create filter on channel values
        
        :param db:          Database handle
        :param filter:      Name of filter
        :param mask_ch:     Mask channel name
        :param mineral_ch:  Mineral channel name
        :param mineral:     Mineral to restrict filter to.
        :type  db:          GXDB
        :type  filter:      str
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  mineral:     str

        :returns:           -1 - Cancel - Edits to filter discarded.
                            
                             0 - Normal Return. Edits saved to filter file.
                            
                             1 - Apply filter to current data only
                            
                             2 - Remove filter - If removing filtered data, just
                                 restore the data to the Min/Pos data
                                 otherwise set the mask channel to 1.
                            
                            Re-entry code. If not `iDUMMY <geosoft.gxapi.iDUMMY>`, what to do inside the filter after
                            going back in. Returned on exit, used on next input.
                            
                             0 - Nothing. Don't need to go back into this function again.
                             1 - Edit the filter.
                            
                            Notes            New and edited filters are stored in user\\etc in files with
                             the file extension ".semfilter"
                             If a file for the specified filter does not exist, then a
                             new filter by that name will be created.
        :rtype:             int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        ret_val = gxapi_cy.WrapSEMPLOT._edit_filter(GXContext._get_tls_geo(), db, filter.encode(), mask_ch.encode(), mineral_ch.encode(), mineral.encode())
        return ret_val



    @classmethod
    def get_mineral_channel_name(cls, db, mineral_ch):
        """
        Retrieve the mineral channel name.
        
        :param db:          Database handle
        :param mineral_ch:  Mineral channel name
        :type  db:          GXDB
        :type  mineral_ch:  str_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** First looks at the `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>`.MINERAL_CHANNEL value.
        If not found, returns the first MINERAL class
        channel found. If still not found, returns a
        blank string.
        """
        mineral_ch.value = gxapi_cy.WrapSEMPLOT._get_mineral_channel_name(GXContext._get_tls_geo(), db, mineral_ch.value.encode())
        



    @classmethod
    def import_ascii_wizard(cls, name, temp, anomaly):
        """
        Generate a `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>` ASCII import template.
        
        :param name:     Data file name
        :param temp:     Template to make
        :param anomaly:  Anomaly name (can be "")
        :type  name:     str
        :type  temp:     str
        :type  anomaly:  str_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** If the anomaly name is not included, then
        the input data must have an "Anom_Name" field.
        """
        anomaly.value = gxapi_cy.WrapSEMPLOT._import_ascii_wizard(GXContext._get_tls_geo(), name.encode(), temp.encode(), anomaly.value.encode())
        



    @classmethod
    def import_database_odbc(cls, connection, temp):
        """
        Generate a template file for importing ODBC databases.
        
        :param connection:  Connection string (input and returned)
        :param temp:        Template file (returned)
        :type  connection:  str_ref
        :type  temp:        str_ref

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        connection.value, temp.value = gxapi_cy.WrapSEMPLOT._import_database_odbc(GXContext._get_tls_geo(), connection.value.encode(), temp.value.encode())
        



    @classmethod
    def import_bin(cls, db, data, template, line, flight, date):
        """
        Import blocked binary or archive ASCII data
        
        :param db:        Database
        :param data:      Import data file name
        :param template:  Import template name
        :param line:      Optional Line name (see note 3.)
        :param flight:    Optional Flight number
        :param date:      Optional date
        :type  db:        GXDB
        :type  data:      str
        :type  template:  str
        :type  line:      str
        :type  flight:    int
        :type  date:      float

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** This wrapper is for `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>`, and does not require the import licence.
        
           1. Binary import templates have extension .I2 by convention.  See
              BINARY.I2 for a description of the template format.
              Archive import templates have extension .I3 by convention. See
              ARCHIVE.I3 for a description of the template format.
        
           2. Both the import template and data file must exist.
        
           3. If a line already exists in the database, a new version is created
              unless a line name is passed in.  In this case, the specified name
              is used and the imported channels on the previous line will be
              destroyed.

        .. seealso::

            `GXDU.lab_template <geosoft.gxapi.GXDU.lab_template>` in du.gxh
        """
        gxapi_cy.WrapSEMPLOT._import_bin(GXContext._get_tls_geo(), db, data.encode(), template.encode(), line.encode(), flight, date)
        



    @classmethod
    def import_database_ado(cls, name, temp):
        """
        Generate a template file for importing semplot databases.
        
        :param name:  Data file name
        :param temp:  Template to make
        :type  name:  str
        :type  temp:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._import_database_ado(GXContext._get_tls_geo(), name.encode(), temp.encode())
        



    @classmethod
    def init_group_symbols_used(cls, db):
        """
        Initializes memory of symbols used in plotting.
        
        :param db:  Database handle
        :type  db:  GXDB

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** Maintains a list of the symbols used in plotting. Call before
        Plotting one or more legends - symbols are accumulated.
        `plot_symbol_legend <geosoft.gxapi.GXSEMPLOT.plot_symbol_legend>` uses this information to create a legend.
        """
        gxapi_cy.WrapSEMPLOT._init_group_symbols_used(GXContext._get_tls_geo(), db)
        



    @classmethod
    def template_type(cls, template):
        """
        Create a new XYPlot or TriPlot template.
        
        :param template:  Template name
        :type  template:  str

        :returns:         `SEMPLOT_PLOT_XYPLOT <geosoft.gxapi.SEMPLOT_PLOT_XYPLOT>` or
                          `SEMPLOT_PLOT_TRIPLOT <geosoft.gxapi.SEMPLOT_PLOT_TRIPLOT>`
                          Terminates if error.
        :rtype:           int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        ret_val = gxapi_cy.WrapSEMPLOT._template_type(GXContext._get_tls_geo(), template.encode())
        return ret_val



    @classmethod
    def view_type(cls, map, view):
        """
        Test to see if a view is an XYPlot or Triplot view.
        
        :param map:   Input map object
        :param view:  Input view name
        :type  map:   GXMAP
        :type  view:  str

        :returns:     :ref:`SEMPLOT_PLOT`
        :rtype:       int

        .. versionadded:: 6.4.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** First checks the view name to see if it starts with
        ``"XYplt_"`` or ``"Triplt_"``. Failing that it looks in the
        view `GXREG <geosoft.gxapi.GXREG>` for a value for "Components.Type", which will
        be either "XYPlot" or "TriPlot".
        If the view does not appear to be an XYPlot or a TriPlot view,
        the function returns `SEMPLOT_PLOT_UNKNOWN <geosoft.gxapi.SEMPLOT_PLOT_UNKNOWN>`.
        """
        ret_val = gxapi_cy.WrapSEMPLOT._view_type(GXContext._get_tls_geo(), map, view.encode())
        return ret_val



    @classmethod
    def mineral_id(cls, db, resid, min_ch, res_ch):
        """
        Identify minerals from the oxide channels.
        
        :param db:      Database
        :param resid:   Maximum residual value (in % of the total oxide)
        :param min_ch:  Mineral channel (Locked RW)
        :param res_ch:  Residual channel (Locked RW)
        :type  db:      GXDB
        :type  resid:   float
        :type  min_ch:  int
        :type  res_ch:  int

        .. versionadded:: 6.3

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** Finds the best mineral matching the composition for each
        row of oxide values. Works using linear programming and
        the simplex method to maximize the oxides used to create
        each of the possible output minerals. The mineral leaving the
        least leftover is selected, as long as the residual (measured
        as a percent of the total) is less than or equal to the
        input value.
        """
        gxapi_cy.WrapSEMPLOT._mineral_id(GXContext._get_tls_geo(), db, resid, min_ch, res_ch)
        



    @classmethod
    def new_filter(cls, filter, model):
        """
        Create a new selection filter.
        
        :param filter:  New filter name
        :param model:   Filter to use as a model (can be "")
        :type  filter:  str
        :type  model:   str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** Creates a new, empty filter file in the user\\etc directory
        """
        gxapi_cy.WrapSEMPLOT._new_filter(GXContext._get_tls_geo(), filter.encode(), model.encode())
        



    @classmethod
    def new_template(cls, template, type, model):
        """
        Create a new XYPlot or TriPlot template.
        
        :param template:  New template name
        :param type:      Unknown
        :param model:     Template to use as a model (can be "")
        :type  template:  str
        :type  type:      int
        :type  model:     str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The new template is written to the user\\etc directory, with
        the file extension "semfilter". The template contains a parameter
        identifying it as an XY or Triplot.
        
        Model Template: Looks first in user\\etc, then in \\etc.
        Looks first for file prefix "semtemplate" then "xyt" or "tri"
        
        Because there are so many shared parameters, it is possible to use
        an XYPlot template as a model for a TriPlot, and vica-verca, with
        few complications.  (e.g. needing to define a "Z" component)
        """
        gxapi_cy.WrapSEMPLOT._new_template(GXContext._get_tls_geo(), template.encode(), type, model.encode())
        



    @classmethod
    def overlay_lst(cls, lst, extension, type):
        """
        Fill a list with the available plot overlay names
        
        :param lst:        Input `GXLST <geosoft.gxapi.GXLST>`.
        :param extension:  :ref:`SEMPLOT_EXT`
        :param type:       :ref:`SEMPLOT_PLOT`
        :type  lst:        GXLST
        :type  extension:  int
        :type  type:       int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** Looks first in user\\etc, then in \\etc.
        See :ref:`SEMPLOT_EXT` definitions above for which files to look for.
        """
        gxapi_cy.WrapSEMPLOT._overlay_lst(GXContext._get_tls_geo(), lst, extension, type)
        



    @classmethod
    def plot(cls, db, template, mask_ch, mineral_ch, map, map_mode, plot_symb):
        """
        Plot an XYPlot or TriPlot based on the template.
        
        :param db:          Database handle
        :param template:    Template file name
        :param mask_ch:     Mask channel (can be "")
        :param mineral_ch:  Mineral channel (can be "" for raw data)
        :param map:         Map name
        :param map_mode:    Map open mode; one of MAP_WRITEXXX (see map.gxh)
        :param plot_symb:   Plot symbols (O: No, 1:Yes) ?
        :type  db:          GXDB
        :type  template:    str
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  map:         str
        :type  map_mode:    int
        :type  plot_symb:   int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The "Components" and "Parameters" groups in the INI file
        are used.
        Only values with mask values of 1 are plotted, if the mask
        channel is specified.
        
        Call "`reset_used_channel <geosoft.gxapi.GXSEMPLOT.reset_used_channel>`" prior to this function
        in order to track the values actually plotted.
        
        Call `init_group_symbols_used <geosoft.gxapi.GXSEMPLOT.init_group_symbols_used>` prior to this function
        to reset recording of the symbols used in plotting (for legends etc).
        """
        gxapi_cy.WrapSEMPLOT._plot(GXContext._get_tls_geo(), db, template.encode(), mask_ch.encode(), mineral_ch.encode(), map.encode(), map_mode, plot_symb)
        



    @classmethod
    def plot_symbol_legend(cls, db, mview, x_min, y_min, y_max, symb_size):
        """
        Plot a symbol legend in a view.
        
        :param db:         Database handle
        :param mview:      View to plot into
        :param x_min:      X Minimum
        :param y_min:      Y Minimum
        :param y_max:      Y Maximum
        :param symb_size:  Symbol size
        :type  db:         GXDB
        :type  mview:      GXMVIEW
        :type  x_min:      float
        :type  y_min:      float
        :type  y_max:      float
        :type  symb_size:  float

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** This function depends on `init_group_symbols_used <geosoft.gxapi.GXSEMPLOT.init_group_symbols_used>`
        before the plot for which this legend is created is made.
        The symbols and groups to use in the legend are stored to
        a database blob after the plot is made. These values are
        recovered by this function to make the legend at the
        specified location.
        """
        gxapi_cy.WrapSEMPLOT._plot_symbol_legend(GXContext._get_tls_geo(), db, mview, x_min, y_min, y_max, symb_size)
        



    @classmethod
    def prop_symb(cls, db, map, view, chan, mask_ch, mineral_ch, log, area, base, scale, symb, wt, line_col, fill_col, legend):
        """
        Plot a proportional symbol plot.
        
        :param db:          Database handle
        :param map:         Map to plot to
        :param view:        View to replot
        :param chan:        Channel name
        :param mask_ch:     Mask channel (can be "")
        :param mineral_ch:  Mineral channel (
        :param log:         Linear (0) or logarithmic (1) scaling
        :param area:        Scale by diameter (0) or area (1)
        :param base:        Scale base (log) data units
        :param scale:       Scale factor (log) data units/mm
        :param symb:        Symbol number
        :param wt:          Symbol weight
        :param line_col:    Symbol line color
        :param fill_col:    Symbol fill color
        :param legend:      Plot legend?
        :type  db:          GXDB
        :type  map:         GXMAP
        :type  view:        str
        :type  chan:        str
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  log:         int
        :type  area:        int
        :type  base:        float
        :type  scale:       float
        :type  symb:        int
        :type  wt:          int
        :type  line_col:    int
        :type  fill_col:    int
        :type  legend:      int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** Replots map using proportional symbols
        """
        gxapi_cy.WrapSEMPLOT._prop_symb(GXContext._get_tls_geo(), db, map, view.encode(), chan.encode(), mask_ch.encode(), mineral_ch.encode(), log, area, base, scale, symb, wt, line_col, fill_col, legend)
        



    @classmethod
    def replot(cls, db, mask_ch, mineral_ch, map, view):
        """
        Replot an existing `GXSEMPLOT <geosoft.gxapi.GXSEMPLOT>` plot based on current data.
        
        :param db:          Database handle
        :param mask_ch:     Mask channel (can be "")
        :param mineral_ch:  Mineral channel (can be "" for raw data)
        :param map:         Map handle
        :param view:        Map View containing the plot
        :type  db:          GXDB
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  map:         GXMAP
        :type  view:        str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** Note that the selection of data
        in the current `GXDB <geosoft.gxapi.GXDB>` is used to replot the map.
        
        Call "`reset_used_channel <geosoft.gxapi.GXSEMPLOT.reset_used_channel>`" prior to this function
        in order to track the values actually plotted.
        
        Call `init_group_symbols_used <geosoft.gxapi.GXSEMPLOT.init_group_symbols_used>` prior to this function
        to reset recording of the symbols used in plotting (for legends etc).
        """
        gxapi_cy.WrapSEMPLOT._replot(GXContext._get_tls_geo(), db, mask_ch.encode(), mineral_ch.encode(), map, view.encode())
        



    @classmethod
    def re_plot_symbol_legend(cls, db, mview):
        """
        Replot a symbol legend in a view.
        
        :param db:     Database handle
        :param mview:  View to plot into
        :type  db:     GXDB
        :type  mview:  GXMVIEW

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** Searches the VIEW `GXREG <geosoft.gxapi.GXREG>` for information on a previously
        created legend, and if it finds that info, replots the Legend,
        using the current data, group key etc.
        """
        gxapi_cy.WrapSEMPLOT._re_plot_symbol_legend(GXContext._get_tls_geo(), db, mview)
        



    @classmethod
    def reset_groups(cls, db, mask_ch):
        """
        Re-group data using current settings.
        
        :param db:       Database handle
        :param mask_ch:  Mask channel
        :type  db:       GXDB
        :type  mask_ch:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._reset_groups(GXContext._get_tls_geo(), db, mask_ch.encode())
        



    @classmethod
    def reset_used_channel(cls, db):
        """
        Set the "Plotted" channel to dummies
        
        :param db:  Database handle
        :type  db:  GXDB

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** This function is called before one or a series of plots to initialize
        the "Plotted" channel in all the selected lines to dummy values.
        As the plots are created, those points used in the plot are set to 1,
        so that at the end the database records which values have been plotted.
        This information can then be used to make a symbol legend.
        If the "Plotted" channel does not exist, it is created, associated,
        loaded, and filled with dummies.
        """
        gxapi_cy.WrapSEMPLOT._reset_used_channel(GXContext._get_tls_geo(), db)
        



    @classmethod
    def select_poly(cls, db, mview, mask_ch, mineral_ch, pply, mode):
        """
        Select data from a polygonal area on a map.
        
        :param db:          Database handle
        :param mview:       View Handle
        :param mask_ch:     Mask channel to update
        :param mineral_ch:  Mineral channel
        :param pply:        Polygon to select from, in the view coordinates.
        :param mode:        Mask mode (0: Append, 1: New)
        :type  db:          GXDB
        :type  mview:       GXMVIEW
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  pply:        GXPLY
        :type  mode:        int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._select_poly(GXContext._get_tls_geo(), db, mview, mask_ch.encode(), mineral_ch.encode(), pply, mode)
        



    @classmethod
    def set_channel_order(cls, db, lst):
        """
        Sets preset channel order.
        
        :param db:   Database handle
        :param lst:  Channel names, handles
        :type  db:   GXDB
        :type  lst:  GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** Sets channel order as follows:
        
        Sample_No
        X and Y Locations
        Mineral
        Grain_No
        Position (e.g. center, edge etc.)
        Grain Morph
        Oxides (in the order they appear in Semplot_Oxides.csv)
        Trace Elements (Ordered as in the periodic table)
        Total
        Mask
        IsPlotted (flag set when a value is plotted)
        Other channels
        
        Channel order is set for all "RawData" groups.
        """
        gxapi_cy.WrapSEMPLOT._set_channel_order(GXContext._get_tls_geo(), db, lst)
        



    @classmethod
    def set_channel_units(cls, db):
        """
        Set units for oxides (%) and elements (ppm)
        
        :param db:  Database handle
        :type  db:  GXDB

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** If the channel units are already set, then they are not changed.
        Oxide channels are identified from the Semplot_Oxides.csv file.
        Trace elements are identified from the periodic table of the
        elements, except for "Y", if it is the current Y channel.
        """
        gxapi_cy.WrapSEMPLOT._set_channel_units(GXContext._get_tls_geo(), db)
        



    @classmethod
    def set_itr(cls, db, ch, itr):
        """
        Put `GXITR <geosoft.gxapi.GXITR>` into a channel.
        
        :param db:   Database handle
        :param ch:   Data channel handle
        :type  db:   GXDB
        :type  ch:   int
        :type  itr:  GXITR

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._set_itr(GXContext._get_tls_geo(), db, ch, itr)
        



    @classmethod
    def set_mask(cls, db, mask_ch, mineral_ch, mineral, selected, val):
        """
        Set the mask channel ON or OFF.
        
        :param db:          Database handle
        :param mask_ch:     Mask channel
        :param mineral_ch:  Mineral channel
        :param mineral:     Mineral to use ("All" or "" for all)
        :param selected:    0 for all lines, 1 for selected lines
        :param val:         0 for off, 1 for on.
        :type  db:          GXDB
        :type  mask_ch:     str
        :type  mineral_ch:  str
        :type  mineral:     str
        :type  selected:    int
        :type  val:         int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._set_mask(GXContext._get_tls_geo(), db, mask_ch.encode(), mineral_ch.encode(), mineral.encode(), selected, val)
        



    @classmethod
    def sort_data(cls, db, group, anomaly):
        """
        Sort data by Sample No, Grain and Position
        
        :param db:       Database handle
        :param group:    Data Group handle
        :param anomaly:  Use Anomaly channel as primary sort?
        :type  db:       GXDB
        :type  group:    int
        :type  anomaly:  int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._sort_data(GXContext._get_tls_geo(), db, group, anomaly)
        



    @classmethod
    def template_lst(cls, lst, type):
        """
        Fill a list with the available plot template names
        
        :param lst:   Input `GXLST <geosoft.gxapi.GXLST>`.
        :param type:  :ref:`SEMPLOT_PLOT`
        :type  lst:   GXLST
        :type  type:  int

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** Looks first in user\\etc, then in \\etc.
        Looks first for file prefix "semtemplate" then "xyt" or "tri"
        (New-style templates with the "semtemplate" extentsion have the
        plot type "triplot" or "xyplot" inside them.)
        """
        gxapi_cy.WrapSEMPLOT._template_lst(GXContext._get_tls_geo(), lst, type)
        



    @classmethod
    def tile_windows(cls):
        """
        Tile currently maximimized windows.
        

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_
        """
        gxapi_cy.WrapSEMPLOT._tile_windows(GXContext._get_tls_geo())
        



    @classmethod
    def total_oxides(cls, db, mineral_ch):
        """
        Calculate the total oxides channel.
        
        :param db:          Database handle
        :param mineral_ch:  Mineral channel
        :type  db:          GXDB
        :type  mineral_ch:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Extended Desktop License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_

        **Note:** The mineral channel is needed in order to adjust the total
        with the Fe Corrected Ferric and Ferrous values, and these
        require a mineral for their identification. If none is provided,
        mineral "X" (unknown) is assumed.
        """
        gxapi_cy.WrapSEMPLOT._total_oxides(GXContext._get_tls_geo(), db, mineral_ch.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer