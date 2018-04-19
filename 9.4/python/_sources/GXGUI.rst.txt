
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
    
    .. autoattribute:: geosoft.gxapi.AOI_RETURN_CANCEL
.. autodata:: geosoft.gxapi.AOI_RETURN_NODEFINE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.AOI_RETURN_NODEFINE
.. autodata:: geosoft.gxapi.AOI_RETURN_DEFINE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.AOI_RETURN_DEFINE


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
    
    .. autoattribute:: geosoft.gxapi.COORDSYS_MODE_ALL
.. autodata:: geosoft.gxapi.COORDSYS_MODE_GCS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.COORDSYS_MODE_GCS
.. autodata:: geosoft.gxapi.COORDSYS_MODE_PCS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.COORDSYS_MODE_PCS
.. autodata:: geosoft.gxapi.COORDSYS_MODE_GCS_PCS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.COORDSYS_MODE_GCS_PCS
.. autodata:: geosoft.gxapi.COORDSYS_MODE_PCS_UNKNOWN
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.COORDSYS_MODE_PCS_UNKNOWN


.. _DAT_TYPE:

DAT_TYPE constants
-----------------------------------------------------------------------

Type of files (grids, images) to support

.. autodata:: geosoft.gxapi.DAT_TYPE_GRID
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DAT_TYPE_GRID
.. autodata:: geosoft.gxapi.DAT_TYPE_IMAGE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DAT_TYPE_IMAGE
.. autodata:: geosoft.gxapi.DAT_TYPE_GRID_AND_IMAGE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.DAT_TYPE_GRID_AND_IMAGE


.. _FILE_FILTER:

FILE_FILTER constants
-----------------------------------------------------------------------

File filters

.. autodata:: geosoft.gxapi.FILE_FILTER_ALL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ALL
.. autodata:: geosoft.gxapi.FILE_FILTER_GDB
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GDB
.. autodata:: geosoft.gxapi.FILE_FILTER_GX
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GX
.. autodata:: geosoft.gxapi.FILE_FILTER_GS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GS
.. autodata:: geosoft.gxapi.FILE_FILTER_INI
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_INI
.. autodata:: geosoft.gxapi.FILE_FILTER_OMN
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_OMN
.. autodata:: geosoft.gxapi.FILE_FILTER_VU
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_VU
.. autodata:: geosoft.gxapi.FILE_FILTER_MAP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_MAP
.. autodata:: geosoft.gxapi.FILE_FILTER_PRJ
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_PRJ
.. autodata:: geosoft.gxapi.FILE_FILTER_CON
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_CON
.. autodata:: geosoft.gxapi.FILE_FILTER_MNU
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_MNU
.. autodata:: geosoft.gxapi.FILE_FILTER_PDF
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_PDF
.. autodata:: geosoft.gxapi.FILE_FILTER_PLT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_PLT
.. autodata:: geosoft.gxapi.FILE_FILTER_GWS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GWS
.. autodata:: geosoft.gxapi.FILE_FILTER_AGG
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_AGG
.. autodata:: geosoft.gxapi.FILE_FILTER_TBL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_TBL
.. autodata:: geosoft.gxapi.FILE_FILTER_ZON
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ZON
.. autodata:: geosoft.gxapi.FILE_FILTER_ITR
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ITR
.. autodata:: geosoft.gxapi.FILE_FILTER_DXF
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_DXF
.. autodata:: geosoft.gxapi.FILE_FILTER_TIF
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_TIF
.. autodata:: geosoft.gxapi.FILE_FILTER_EMF
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_EMF
.. autodata:: geosoft.gxapi.FILE_FILTER_BMP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_BMP
.. autodata:: geosoft.gxapi.FILE_FILTER_LUT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_LUT
.. autodata:: geosoft.gxapi.FILE_FILTER_PNG
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_PNG
.. autodata:: geosoft.gxapi.FILE_FILTER_JPG
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_JPG
.. autodata:: geosoft.gxapi.FILE_FILTER_PCX
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_PCX
.. autodata:: geosoft.gxapi.FILE_FILTER_GIF
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GIF
.. autodata:: geosoft.gxapi.FILE_FILTER_GRD
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GRD
.. autodata:: geosoft.gxapi.FILE_FILTER_ERS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ERS
.. autodata:: geosoft.gxapi.FILE_FILTER_EPS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_EPS
.. autodata:: geosoft.gxapi.FILE_FILTER_SHP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_SHP
.. autodata:: geosoft.gxapi.FILE_FILTER_CGM
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_CGM
.. autodata:: geosoft.gxapi.FILE_FILTER_TAB
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_TAB
.. autodata:: geosoft.gxapi.FILE_FILTER_COMPS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_COMPS
.. autodata:: geosoft.gxapi.FILE_FILTER_CSV
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_CSV
.. autodata:: geosoft.gxapi.FILE_FILTER_GPF
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GPF
.. autodata:: geosoft.gxapi.FILE_FILTER_PLY
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_PLY
.. autodata:: geosoft.gxapi.FILE_FILTER_STM
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_STM
.. autodata:: geosoft.gxapi.FILE_FILTER_TTM
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_TTM
.. autodata:: geosoft.gxapi.FILE_FILTER_XYZ
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_XYZ
.. autodata:: geosoft.gxapi.FILE_FILTER_BAR
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_BAR
.. autodata:: geosoft.gxapi.FILE_FILTER_GEOSOFT_LICENSE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GEOSOFT_LICENSE
.. autodata:: geosoft.gxapi.FILE_FILTER_XML
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_XML
.. autodata:: geosoft.gxapi.FILE_FILTER_GXNET
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GXNET
.. autodata:: geosoft.gxapi.FILE_FILTER_ECW
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ECW
.. autodata:: geosoft.gxapi.FILE_FILTER_J2K
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_J2K
.. autodata:: geosoft.gxapi.FILE_FILTER_JP2
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_JP2
.. autodata:: geosoft.gxapi.FILE_FILTER_SEL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_SEL
.. autodata:: geosoft.gxapi.FILE_FILTER_SVG
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_SVG
.. autodata:: geosoft.gxapi.FILE_FILTER_SVZ
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_SVZ
.. autodata:: geosoft.gxapi.FILE_FILTER_WRP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_WRP
.. autodata:: geosoft.gxapi.FILE_FILTER_MAPPLOT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_MAPPLOT
.. autodata:: geosoft.gxapi.FILE_FILTER_DTM
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_DTM
.. autodata:: geosoft.gxapi.FILE_FILTER_VOXEL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_VOXEL
.. autodata:: geosoft.gxapi.FILE_FILTER_MAPTEMPLATE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_MAPTEMPLATE
.. autodata:: geosoft.gxapi.FILE_FILTER_ACTION
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ACTION
.. autodata:: geosoft.gxapi.FILE_FILTER_DM
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_DM
.. autodata:: geosoft.gxapi.FILE_FILTER_KML
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_KML
.. autodata:: geosoft.gxapi.FILE_FILTER_KMZ
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_KMZ
.. autodata:: geosoft.gxapi.FILE_FILTER_TARGET_PLAN
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_TARGET_PLAN
.. autodata:: geosoft.gxapi.FILE_FILTER_TARGET_SECTION
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_TARGET_SECTION
.. autodata:: geosoft.gxapi.FILE_FILTER_TARGET_STRIPLOG
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_TARGET_STRIPLOG
.. autodata:: geosoft.gxapi.FILE_FILTER_TARGET_3D
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_TARGET_3D
.. autodata:: geosoft.gxapi.FILE_FILTER_ARGIS_LYR
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ARGIS_LYR
.. autodata:: geosoft.gxapi.FILE_FILTER_ARGIS_MXD
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ARGIS_MXD
.. autodata:: geosoft.gxapi.FILE_FILTER_GOCAD_TS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GOCAD_TS
.. autodata:: geosoft.gxapi.FILE_FILTER_LST
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_LST
.. autodata:: geosoft.gxapi.FILE_FILTER_ECS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ECS
.. autodata:: geosoft.gxapi.FILE_FILTER_TARGET_FENCE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_TARGET_FENCE
.. autodata:: geosoft.gxapi.FILE_FILTER_GMS3D
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GMS3D
.. autodata:: geosoft.gxapi.FILE_FILTER_BT2
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_BT2
.. autodata:: geosoft.gxapi.FILE_FILTER_BPR
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_BPR
.. autodata:: geosoft.gxapi.FILE_FILTER_BPR2
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_BPR2
.. autodata:: geosoft.gxapi.FILE_FILTER_XLS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_XLS
.. autodata:: geosoft.gxapi.FILE_FILTER_XLSX
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_XLSX
.. autodata:: geosoft.gxapi.FILE_FILTER_MDB
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_MDB
.. autodata:: geosoft.gxapi.FILE_FILTER_ACCDB
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ACCDB
.. autodata:: geosoft.gxapi.FILE_FILTER_INTERSECTION_TBL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_INTERSECTION_TBL
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_CON
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_CON
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_CHG
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_CHG
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_MSH
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_MSH
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_MSH_DAT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_MSH_DAT
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_TOPO_DAT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_TOPO_DAT
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_TOPO_XYZ
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_TOPO_XYZ
.. autodata:: geosoft.gxapi.FILE_FILTER_XYZ_TEMPLATE_I0
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_XYZ_TEMPLATE_I0
.. autodata:: geosoft.gxapi.FILE_FILTER_PICO_TEMPLATE_I1
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_PICO_TEMPLATE_I1
.. autodata:: geosoft.gxapi.FILE_FILTER_BB_TEMPLATE_I2
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_BB_TEMPLATE_I2
.. autodata:: geosoft.gxapi.FILE_FILTER_ASCII_TEMPLATE_I3
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ASCII_TEMPLATE_I3
.. autodata:: geosoft.gxapi.FILE_FILTER_ODBC_TEMPLATE_I4
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ODBC_TEMPLATE_I4
.. autodata:: geosoft.gxapi.FILE_FILTER_EXP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_EXP
.. autodata:: geosoft.gxapi.FILE_FILTER_SEGY
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_SEGY
.. autodata:: geosoft.gxapi.FILE_FILTER_DAARC500
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_DAARC500
.. autodata:: geosoft.gxapi.FILE_FILTER_TXT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_TXT
.. autodata:: geosoft.gxapi.FILE_FILTER_VOXEL_INVERSION
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_VOXEL_INVERSION
.. autodata:: geosoft.gxapi.FILE_FILTER_GMS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GMS
.. autodata:: geosoft.gxapi.FILE_FILTER_FLT3D
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_FLT3D
.. autodata:: geosoft.gxapi.FILE_FILTER_RESOURCE_PACK
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_RESOURCE_PACK
.. autodata:: geosoft.gxapi.FILE_FILTER_GEOSTRING
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GEOSTRING
.. autodata:: geosoft.gxapi.FILE_FILTER_GEOSURFACE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GEOSURFACE
.. autodata:: geosoft.gxapi.FILE_FILTER_GEOSOFT3DV
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GEOSOFT3DV
.. autodata:: geosoft.gxapi.FILE_FILTER_VECTORVOXEL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_VECTORVOXEL
.. autodata:: geosoft.gxapi.FILE_FILTER_FLT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_FLT
.. autodata:: geosoft.gxapi.FILE_FILTER_XYZ_TEMPLATE_O0
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_XYZ_TEMPLATE_O0
.. autodata:: geosoft.gxapi.FILE_FILTER_GMS2D
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GMS2D
.. autodata:: geosoft.gxapi.FILE_FILTER_IP_DATABASE_TEMPLATE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_IP_DATABASE_TEMPLATE
.. autodata:: geosoft.gxapi.FILE_FILTER_GEOSOFT_RESOURCE_MODULE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GEOSOFT_RESOURCE_MODULE
.. autodata:: geosoft.gxapi.FILE_FILTER_VT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_VT
.. autodata:: geosoft.gxapi.FILE_FILTER_INT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_INT
.. autodata:: geosoft.gxapi.FILE_FILTER_SGT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_SGT
.. autodata:: geosoft.gxapi.FILE_FILTER_IMGVIEW
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_IMGVIEW
.. autodata:: geosoft.gxapi.FILE_FILTER_ZIP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ZIP
.. autodata:: geosoft.gxapi.FILE_FILTER_GPS_TABLE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GPS_TABLE
.. autodata:: geosoft.gxapi.FILE_FILTER_VULCAN_TRIANGULATION
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_VULCAN_TRIANGULATION
.. autodata:: geosoft.gxapi.FILE_FILTER_VULCAN_BLOCK_MODEL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_VULCAN_BLOCK_MODEL
.. autodata:: geosoft.gxapi.FILE_FILTER_PRJVIEW
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_PRJVIEW
.. autodata:: geosoft.gxapi.FILE_FILTER_LEAPFROG_MODEL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_LEAPFROG_MODEL
.. autodata:: geosoft.gxapi.FILE_FILTER_IOGAS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_IOGAS
.. autodata:: geosoft.gxapi.FILE_FILTER_ASEG_ESF
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_ASEG_ESF
.. autodata:: geosoft.gxapi.FILE_FILTER_LACOSTE_DAT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_LACOSTE_DAT
.. autodata:: geosoft.gxapi.FILE_FILTER_VAR
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_VAR
.. autodata:: geosoft.gxapi.FILE_FILTER_P190
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_P190
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_OBS_DAT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_OBS_DAT
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_LOC
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_LOC
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_MOD
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_MOD
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_DEN
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_DEN
.. autodata:: geosoft.gxapi.FILE_FILTER_UBC_SUS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_SUS
.. autodata:: geosoft.gxapi.FILE_FILTER_GOCAD_VOXET
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FILTER_GOCAD_VOXET


.. _FILE_FORM:

FILE_FORM constants
-----------------------------------------------------------------------

File Form Defines

.. autodata:: geosoft.gxapi.FILE_FORM_OPEN
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FORM_OPEN
.. autodata:: geosoft.gxapi.FILE_FORM_SAVE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.FILE_FORM_SAVE


.. _GS_DIRECTORY:

GS_DIRECTORY constants
-----------------------------------------------------------------------

Geosoft predefined directory

.. autodata:: geosoft.gxapi.GS_DIRECTORY_NONE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_NONE
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GEOSOFT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GEOSOFT
.. autodata:: geosoft.gxapi.GS_DIRECTORY_BIN
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_BIN
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GER
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GER
.. autodata:: geosoft.gxapi.GS_DIRECTORY_OMN
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_OMN
.. autodata:: geosoft.gxapi.GS_DIRECTORY_TBL
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_TBL
.. autodata:: geosoft.gxapi.GS_DIRECTORY_FONTS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_FONTS
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GX
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GX
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GS
.. autodata:: geosoft.gxapi.GS_DIRECTORY_APPS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_APPS
.. autodata:: geosoft.gxapi.GS_DIRECTORY_ETC
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_ETC
.. autodata:: geosoft.gxapi.GS_DIRECTORY_HLP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_HLP
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GXDEV
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GXDEV
.. autodata:: geosoft.gxapi.GS_DIRECTORY_COMPONENT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_COMPONENT
.. autodata:: geosoft.gxapi.GS_DIRECTORY_CSV
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_CSV
.. autodata:: geosoft.gxapi.GS_DIRECTORY_LIC
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_LIC
.. autodata:: geosoft.gxapi.GS_DIRECTORY_INI
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_INI
.. autodata:: geosoft.gxapi.GS_DIRECTORY_TEMP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_TEMP
.. autodata:: geosoft.gxapi.GS_DIRECTORY_UETC
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_UETC
.. autodata:: geosoft.gxapi.GS_DIRECTORY_UMAPTEMPLATE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_UMAPTEMPLATE
.. autodata:: geosoft.gxapi.GS_DIRECTORY_COMPONENT_SCRIPTS
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_COMPONENT_SCRIPTS
.. autodata:: geosoft.gxapi.GS_DIRECTORY_COMPONENT_HTML
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_COMPONENT_HTML
.. autodata:: geosoft.gxapi.GS_DIRECTORY_IMG
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_IMG
.. autodata:: geosoft.gxapi.GS_DIRECTORY_BAR
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_BAR
.. autodata:: geosoft.gxapi.GS_DIRECTORY_GXNET
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GXNET
.. autodata:: geosoft.gxapi.GS_DIRECTORY_MAPTEMPLATE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.GS_DIRECTORY_MAPTEMPLATE


.. _IMPCH_TYPE:

IMPCH_TYPE constants
-----------------------------------------------------------------------

Import Chem defines

.. autodata:: geosoft.gxapi.IMPCH_TYPE_DATA
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.IMPCH_TYPE_DATA
.. autodata:: geosoft.gxapi.IMPCH_TYPE_ASSAY
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.IMPCH_TYPE_ASSAY


.. _WINDOW_STATE:

WINDOW_STATE constants
-----------------------------------------------------------------------

Window State Options

.. autodata:: geosoft.gxapi.WINDOW_RESTORE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.WINDOW_RESTORE
.. autodata:: geosoft.gxapi.WINDOW_MINIMIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.WINDOW_MINIMIZE
.. autodata:: geosoft.gxapi.WINDOW_MAXIMIZE
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.WINDOW_MAXIMIZE


.. _XTOOL_ALIGN:

XTOOL_ALIGN constants
-----------------------------------------------------------------------

XTool docking alignment flags

.. autodata:: geosoft.gxapi.XTOOL_ALIGN_LEFT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.XTOOL_ALIGN_LEFT
.. autodata:: geosoft.gxapi.XTOOL_ALIGN_TOP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.XTOOL_ALIGN_TOP
.. autodata:: geosoft.gxapi.XTOOL_ALIGN_RIGHT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.XTOOL_ALIGN_RIGHT
.. autodata:: geosoft.gxapi.XTOOL_ALIGN_BOTTOM
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.XTOOL_ALIGN_BOTTOM
.. autodata:: geosoft.gxapi.XTOOL_ALIGN_ANY
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.XTOOL_ALIGN_ANY


.. _XTOOL_DOCK:

XTOOL_DOCK constants
-----------------------------------------------------------------------

XTool default docking state

.. autodata:: geosoft.gxapi.XTOOL_DOCK_TOP
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.XTOOL_DOCK_TOP
.. autodata:: geosoft.gxapi.XTOOL_DOCK_LEFT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.XTOOL_DOCK_LEFT
.. autodata:: geosoft.gxapi.XTOOL_DOCK_RIGHT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.XTOOL_DOCK_RIGHT
.. autodata:: geosoft.gxapi.XTOOL_DOCK_BOTTOM
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.XTOOL_DOCK_BOTTOM
.. autodata:: geosoft.gxapi.XTOOL_DOCK_FLOAT
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.XTOOL_DOCK_FLOAT

	