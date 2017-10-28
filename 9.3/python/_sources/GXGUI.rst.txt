
.. _GXGUI:

 
GXGUI class
==================================

.. autoclass:: geosoft.gxapi.GXGUI
   :members:


.. _AOI_RETURN_STATE:

AOI_RETURN_STATE constants
-----------------------------------------------------------------------

AOI query return state

.. autodata:: geosoft.gxapi.AOI_RETURN_CANCEL
    :annotation:
.. autodata:: geosoft.gxapi.AOI_RETURN_NODEFINE
    :annotation:
.. autodata:: geosoft.gxapi.AOI_RETURN_DEFINE
    :annotation:


.. _COORDSYS_MODE:

COORDSYS_MODE constants
-----------------------------------------------------------------------

Coordinate system wizard `GXIPJ <geosoft.gxapi.GXIPJ>` types allowed on return.
The wizard present three types of projections for selection
by the user, Geographic (GCS), Projected (PCS), and Unknown.
(Unknown requires only that the units be defined.)
The Editable flag must be Yes for this option to take affect,
and is overridden internally if the user's license does not
allow modification of projections (e.g. the OM Viewer).

.. autodata:: geosoft.gxapi.COORDSYS_MODE_ALL
    :annotation:
.. autodata:: geosoft.gxapi.COORDSYS_MODE_GCS
    :annotation:
.. autodata:: geosoft.gxapi.COORDSYS_MODE_PCS
    :annotation:
.. autodata:: geosoft.gxapi.COORDSYS_MODE_GCS_PCS
    :annotation:
.. autodata:: geosoft.gxapi.COORDSYS_MODE_PCS_UNKNOWN
    :annotation:


.. _DAT_TYPE:

DAT_TYPE constants
-----------------------------------------------------------------------

Type of files (grids, images) to support

.. autodata:: geosoft.gxapi.DAT_TYPE_GRID
    :annotation:
.. autodata:: geosoft.gxapi.DAT_TYPE_IMAGE
    :annotation:
.. autodata:: geosoft.gxapi.DAT_TYPE_GRID_AND_IMAGE
    :annotation:


.. _FILE_FILTER:

FILE_FILTER constants
-----------------------------------------------------------------------

File filters

.. autodata:: geosoft.gxapi.FILE_FILTER_ALL
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GDB
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GX
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_INI
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_OMN
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_VU
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_MAP
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_PRJ
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_CON
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_MNU
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_PDF
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_PLT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GWS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_AGG
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_TBL
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ZON
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ITR
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_DXF
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_TIF
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_EMF
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_BMP
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_LUT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_PNG
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_JPG
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_PCX
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GIF
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GRD
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ERS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_EPS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_SHP
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_CGM
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_TAB
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_COMPS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_CSV
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GPF
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_PLY
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_STM
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_TTM
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_XYZ
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_BAR
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GEOSOFT_LICENSE
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_XML
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GXNET
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ECW
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_J2K
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_JP2
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_SEL
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_SVG
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_SVZ
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_WRP
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_MAPPLOT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_DTM
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_VOXEL
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_MAPTEMPLATE
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ACTION
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_DM
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_KML
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_KMZ
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_TARGET_PLAN
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_TARGET_SECTION
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_TARGET_STRIPLOG
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_TARGET_3D
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ARGIS_LYR
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ARGIS_MXD
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GOCAD_TS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_LST
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ECS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_TARGET_FENCE
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GMS3D
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_BT2
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_BPR
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_BPR2
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_XLS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_XLSX
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_MDB
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ACCDB
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_INTERSECTION_TBL
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_CON
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_CHG
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_MSH
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_MSH_DAT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_TOPO_DAT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_TOPO_XYZ
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_XYZ_TEMPLATE_I0
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_PICO_TEMPLATE_I1
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_BB_TEMPLATE_I2
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ASCII_TEMPLATE_I3
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ODBC_TEMPLATE_I4
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_EXP
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_SEGY
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_DAARC500
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_TXT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_VOXEL_INVERSION
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GMS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_FLT3D
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_RESOURCE_PACK
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GEOSTRING
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GEOSURFACE
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GEOSOFT3DV
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_VECTORVOXEL
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_FLT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_XYZ_TEMPLATE_O0
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GMS2D
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_IP_DATABASE_TEMPLATE
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GEOSOFT_RESOURCE_MODULE
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_VT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_INT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_SGT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_IMGVIEW
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ZIP
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GPS_TABLE
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_VULCAN_TRIANGULATION
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_VULCAN_BLOCK_MODEL
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_PRJVIEW
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_LEAPFROG_MODEL
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_IOGAS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_ASEG_ESF
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_LACOSTE_DAT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_VAR
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_P190
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_OBS_DAT
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_LOC
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_MOD
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_DEN
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_SUS
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FILTER_GOCAD_VOXET
    :annotation:


.. _FILE_FORM:

FILE_FORM constants
-----------------------------------------------------------------------

File Form Defines

.. autodata:: geosoft.gxapi.FILE_FORM_OPEN
    :annotation:
.. autodata:: geosoft.gxapi.FILE_FORM_SAVE
    :annotation:


.. _GS_DIRECTORY:

GS_DIRECTORY constants
-----------------------------------------------------------------------

Geosoft predefined directory

.. autodata:: geosoft.gxapi.GS_DIRECTORY_NONE
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GEOSOFT
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_BIN
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GER
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_OMN
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_TBL
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_FONTS
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GX
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GS
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_APPS
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_ETC
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_HLP
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GXDEV
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_COMPONENT
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_CSV
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_LIC
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_INI
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_TEMP
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_UETC
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_UMAPTEMPLATE
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_COMPONENT_SCRIPTS
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_COMPONENT_HTML
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_IMG
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_BAR
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GXNET
    :annotation:
.. autodata:: geosoft.gxapi.GS_DIRECTORY_MAPTEMPLATE
    :annotation:


.. _IMPCH_TYPE:

IMPCH_TYPE constants
-----------------------------------------------------------------------

Import Chem defines

.. autodata:: geosoft.gxapi.IMPCH_TYPE_DATA
    :annotation:
.. autodata:: geosoft.gxapi.IMPCH_TYPE_ASSAY
    :annotation:


.. _WINDOW_STATE:

WINDOW_STATE constants
-----------------------------------------------------------------------

Window State Options

.. autodata:: geosoft.gxapi.WINDOW_RESTORE
    :annotation:
.. autodata:: geosoft.gxapi.WINDOW_MINIMIZE
    :annotation:
.. autodata:: geosoft.gxapi.WINDOW_MAXIMIZE
    :annotation:


.. _XTOOL_ALIGN:

XTOOL_ALIGN constants
-----------------------------------------------------------------------

XTool docking alignment flags

.. autodata:: geosoft.gxapi.XTOOL_ALIGN_LEFT
    :annotation:
.. autodata:: geosoft.gxapi.XTOOL_ALIGN_TOP
    :annotation:
.. autodata:: geosoft.gxapi.XTOOL_ALIGN_RIGHT
    :annotation:
.. autodata:: geosoft.gxapi.XTOOL_ALIGN_BOTTOM
    :annotation:
.. autodata:: geosoft.gxapi.XTOOL_ALIGN_ANY
    :annotation:


.. _XTOOL_DOCK:

XTOOL_DOCK constants
-----------------------------------------------------------------------

XTool default docking state

.. autodata:: geosoft.gxapi.XTOOL_DOCK_TOP
    :annotation:
.. autodata:: geosoft.gxapi.XTOOL_DOCK_LEFT
    :annotation:
.. autodata:: geosoft.gxapi.XTOOL_DOCK_RIGHT
    :annotation:
.. autodata:: geosoft.gxapi.XTOOL_DOCK_BOTTOM
    :annotation:
.. autodata:: geosoft.gxapi.XTOOL_DOCK_FLOAT
    :annotation:

	