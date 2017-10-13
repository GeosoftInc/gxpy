
.. _GXGUI:

 
GXGUI class
==================================

.. autoclass:: geosoft.gxapi.GXGUI
   :members:

.. _AOI_RETURN_STATE:

AOI_RETURN_STATE constants
-----------------------------------------------------------------------

::

   AOI query return state 

.. autoattribute:: geosoft.gxapi.AOI_RETURN_CANCEL

::

   User canceled 

.. autoattribute:: geosoft.gxapi.AOI_RETURN_NODEFINE

::

   User chose to continue with no AOI defined or available 

.. autoattribute:: geosoft.gxapi.AOI_RETURN_DEFINE

::

   User chose to continue and defined valid AOI parameters 

.. _COORDSYS_MODE:

COORDSYS_MODE constants
-----------------------------------------------------------------------

::

   Coordinate system wizard IPJ types allowed on return.
   The wizard present three types of projections for selection
   by the user, Geographic (GCS), Projected (PCS), and Unknown.
   (Unknown requires only that the units be defined.)
   The Editable flag must be Yes for this option to take affect,
   and is overridden internally if the user's license does not
   allow modification of projections (e.g. the OM Viewer). 

.. autoattribute:: geosoft.gxapi.COORDSYS_MODE_ALL

::

   Allow Geographic (GCS), Projected (PCS), and Unknown 

.. autoattribute:: geosoft.gxapi.COORDSYS_MODE_GCS

::

   Allow only Geographic (GCS) 

.. autoattribute:: geosoft.gxapi.COORDSYS_MODE_PCS

::

   Allow only Projected (PCS) 

.. autoattribute:: geosoft.gxapi.COORDSYS_MODE_GCS_PCS

::

   Allow only Geographic (GCS) and Projected (PCS) 

.. autoattribute:: geosoft.gxapi.COORDSYS_MODE_PCS_UNKNOWN

::

   Allow only Projected (PCS), or Unknown 

.. _DAT_TYPE:

DAT_TYPE constants
-----------------------------------------------------------------------

::

   Type of files (grids, images) to support 

.. autoattribute:: geosoft.gxapi.DAT_TYPE_GRID

::

   Display only grid formats 

.. autoattribute:: geosoft.gxapi.DAT_TYPE_IMAGE

::

   Display only image formats 

.. autoattribute:: geosoft.gxapi.DAT_TYPE_GRID_AND_IMAGE

::

   Displays both grids and image formats 

.. _FILE_FILTER:

FILE_FILTER constants
-----------------------------------------------------------------------

::

   File filters 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ALL

::

   All files              \ `*`\ .\ `*`\                   ANYWHERE 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GDB

::

   Geosoft Database       \ `*`\ .gdb                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GX

::

   Geosoft Executable     \ `*`\ .gx                 GEOSOFT 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GS

::

   Geosoft Script         \ `*`\ .gs                 BOTH 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_INI

::

   Parameter files        \ `*`\ .ini                GEOSOFT 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_OMN

::

   Oasis Menu files       \ `*`\ .omn                GEOSOFT 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_VU

::

   Oasis View files       \ `*`\ .vu                 LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_MAP

::

   Oasis Map files        \ `*`\ .map                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_PRJ

::

   Projection file        \ `*`\ .prj                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_CON

::

   Configuration file     \ `*`\ .con                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_MNU

::

   Sushi MNU files        \ `*`\ .mnu                GEOSOFT 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_PDF

::

   PDF files              \ `*`\ .pdf                GEOSOFT 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_PLT

::

   Geosoft PLT files      \ `*`\ .plt                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GWS

::

   Geosoft workspace      \ `*`\ .gws                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_AGG

::

   Aggregate              \ `*`\ .agg                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_TBL

::

   Color table            \ `*`\ .tbl                GEOSOFT 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ZON

::

   Zone                   \ `*`\ .zon                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ITR

::

   Image transform        \ `*`\ .itr                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_DXF

::

   AutoCAD DXF files      \ `*`\ .dxf                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_TIF

::

   TIFF files             \ `*`\ .tif                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_EMF

::

   Enhanced Metafies      \ `*`\ .emf                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_BMP

::

   Bitmap files           \ `*`\ .bmp                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_LUT

::

   ER Mapper LUT          \ `*`\ .lut                GEOSOFT 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_PNG

::

   PNG files              \ `*`\ .png                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_JPG

::

   JPG files              \ `*`\ .jpg                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_PCX

::

   PCX files              \ `*`\ .pcx                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GIF

::

   GIF files              \ `*`\ .gif                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GRD

::

   GRD files              \ `*`\ .grd                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ERS

::

   ERS files              \ `*`\ .ers                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_EPS

::

   EPS files              \ `*`\ .eps                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_SHP

::

   ArcView Shape files    \ `*`\ .shp                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_CGM

::

   CGM files              \ `*`\ .cgm                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_TAB

::

   MapInfo Tab files      \ `*`\ .tab                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_COMPS

::

   Software Components    Components           LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_CSV

::

   MapInfo Tab files      \ `*`\ .tab                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GPF

::

   Geosoft Project        \ `*`\ .gpf                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_PLY

::

   Geosoft Polygons       \ `*`\ .ply                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_STM

::

   Scatter templates      \ `*`\ .stm                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_TTM

::

   Triplot templates      \ `*`\ .ttm                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_XYZ

::

   Geosoft XYZ files      \ `*`\ .xyz                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_BAR

::

   Geosoft Bar file       \ `*`\ .geobar             LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GEOSOFT_LICENSE

::

   Geosoft License files   \ `*`\ .geosoft_license   LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_XML

::

   XML files              \ `*`\ .xml                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GXNET

::

   GX.NET files           \ `*`\ .dll                GEOSOFT 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ECW

::

   ECW files              \ `*`\ .ecw                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_J2K

::

   J2K JPEG 2000 files    \ `*`\ .j2k                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_JP2

::

   JP2 JPEG 2000 files    \ `*`\ .jp2                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_SEL

::

   acQuire parameters     \ `*`\ .sel                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_SVG

::

   SVG file               \ `*`\ .svg                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_SVZ

::

   SVG Compressed file    \ `*`\ .svz                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_WRP

::

   Warp file              \ `*`\ .wrp                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_MAPPLOT

::

   MAPPLOT file           \ `*`\ .con                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_DTM

::

   Surpac DTM files       \ `*`\ .dtm                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_VOXEL

::

   Geosoft Voxel          \ `*`\ .geosoft_voxel      LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_MAPTEMPLATE

::

   Map Template file      \ `*`\ .geosoft_maptemplate      LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ACTION

::

   Action Scripts         \ `*`\ .action             LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_DM

::

   Datamine files         \ `*`\ .dm                 LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_KML

::

   Google Earth KML       \ `*`\ .kml                LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_KMZ

::

   Google Earth Compressed KML  \ `*`\ .kmz          LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_TARGET_PLAN

::

   Target parameter ini file for plans      \ `*`\ .inp    LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_TARGET_SECTION

::

   Target parameter ini file for sections   \ `*`\ .ins    LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_TARGET_STRIPLOG

::

   Target parameter ini file for strip logs \ `*`\ .inl    LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_TARGET_3D

::

   Target parameter ini file for 3D plots   \ `*`\ .in3    LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ARGIS_LYR

::

   ArcGIS Layer files			 \ `*`\ .lyr    LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ARGIS_MXD

::

   ArcGIS Map Document files	 \ `*`\ .mxd    LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GOCAD_TS

::

   GOCAD TSurf files			 \ `*`\ .ts     LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_LST

::

   Geosoft list of items: names, values  \ `*`\ .lst     LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ECS

::

   GM-SYS external coordinate system     \ `*`\ .ecs     LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_TARGET_FENCE

::

   Target parameter ini file for fence sections   \ `*`\ .ins    LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GMS3D

::

   GM-SYS 3D model   \ `*`\ .geosoft_gmsys3d    LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_BT2

::

   GEMCOM BT2 \ `*`\ .bt2 LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_BPR

::

   GEMCOM BPR \ `*`\ .bpr LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_BPR2

::

   GEMCOM BPR2 \ `*`\ .bpr2 LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_XLS

::

   Excel 97-2003 workbook		\ `*`\ .xls					LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_XLSX

::

   Excel 2007 workbook 			\ `*`\ .xlsx				LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_MDB

::

   Access 97-2003  				\ `*`\ .mdb 				LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ACCDB

::

   Access 2007 					\ `*`\ .accdb 				LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_INTERSECTION_TBL

::

   Levelling intersection		\ `*`\ .tbl					LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_CON

::

   UBC DCIP2D Conductivity model files \ `*`\ .con		LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_CHG

::

   UBC DCIP2D Chargeability model files \ `*`\ .chg	LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_MSH

::

   UBC DCIP2D Mesh files		\ `*`\ .msh					LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_MSH_DAT

::

   UBC DCIP2D Mesh files		\ `*`\ .dat					LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_TOPO_DAT

::

   UBC DCIP2D Topo files		\ `*`\ .dat					LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_TOPO_XYZ

::

   UBC DCIP2D Topo files		\ `*`\ .xyz					LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_XYZ_TEMPLATE_I0

::

   XYZ Import Templates		      \ `*`\ .i0				LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_PICO_TEMPLATE_I1

::

   Picodas Import Templates      \ `*`\ .i1				LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_BB_TEMPLATE_I2

::

   Block Binary Import Templates \ `*`\ .i2				LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ASCII_TEMPLATE_I3

::

   ASCII Import Templates		   \ `*`\ .i3				LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ODBC_TEMPLATE_I4

::

   ODBC Import Templates		   \ `*`\ .i4				LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_EXP

::

   Math expression files		   \ `*`\ .exp  			LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_SEGY

::

   SEG-Y files							\ `*`\ .sgy  			LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_DAARC500

::

   DAARC500 files						xYYMMDD 		   LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_TXT

::

   Text files							\ `*`\ .txt  			LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_VOXEL_INVERSION

::

   Voxi									\ `*`\ .geosoft_voxi	LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GMS

::

   GM-SYS Profile model file		\ `*`\ .gms	LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_FLT3D

::

   Geosoft 3D filter files			\ `*`\ .flt3d			LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_RESOURCE_PACK

::

   Geosoft Resource Update Packages \ `*`\ .geosoft_resource_pack LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GEOSTRING

::

   Geostring files \ `*`\ .geosoft_string LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GEOSURFACE

::

   Geosurface files \ `*`\ .geosoft_surface LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GEOSOFT3DV

::

   Geosoft 3DV \ `*`\ .geosoft_3dv LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_VECTORVOXEL

::

   Geosoft Vector Voxel \ `*`\ .geosoft_vectorvoxel LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_FLT

::

   Geosoft Filters \ `*`\ .flt LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_XYZ_TEMPLATE_O0

::

   XYZ Export Templates \ `*`\ .o0 LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GMS2D

::

   GM-SYS Profile model    \ `*`\ .geosoft_gmsys2d   LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_IP_DATABASE_TEMPLATE

::

   IP Database Template \ `*`\ .geosoft_ipdatabasetemplate LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GEOSOFT_RESOURCE_MODULE

::

   Geosoft Resource Module \ `*`\ .geosoft_resources  LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_VT

::

   Shell VT files     \ `*`\ .vt        LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_INT

::

   Shell INT files     \ `*`\ .int      LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_SGT

::

   Shell SGT files     \ `*`\ .sgt      LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_IMGVIEW

::

   Image Viewer files  \ `*`\ .imgview  LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ZIP

::

   Zip files  \ `*`\ .zip  LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GPS_TABLE

::

   GPS Table \ `*`\ .tbl GEOSOFT 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_VULCAN_TRIANGULATION

::

   Maptek Vulcan trianguilation file   \ `*`\ .tbl     LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_VULCAN_BLOCK_MODEL

::

   Maptek Vulcan block model file       \ `*`\ .bmf                        LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_PRJVIEW

::

   Layout files  \ `*`\ .prjview  LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_LEAPFROG_MODEL

::

   Leapfrog model files  \ `*`\ .lfm  LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_IOGAS

::

   Reflex ioGAS files  \ `*`\ .gas  LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_ASEG_ESF

::

   ASEG ESF file  \ `*`\ .esf  LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_LACOSTE_DAT

::

   Micro-g LaCoste MGS-6 gravity files  \ `*`\ .DAT  LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_VAR

::

   Geosoft variogram file  \ `*`\ .var  LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_P190

::

   UKOOA data exchange file  \ `*`\ .p190  LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_OBS_DAT

::

   UBC observation files \ `*`\ .dat		LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_LOC

::

   UBC location files \ `*`\ .loc		LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_MOD

::

   UBC model files \ `*`\ .mod		LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_DEN

::

   UBC density model files \ `*`\ .den		LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_UBC_SUS

::

   UBC susceptibility model files \ `*`\ .sus		LOCAL 

.. autoattribute:: geosoft.gxapi.FILE_FILTER_GOCAD_VOXET

::

   GOCAD voxet files \ `*`\ .vo		LOCAL 

.. _FILE_FORM:

FILE_FORM constants
-----------------------------------------------------------------------

::

   File Form Defines 

.. autoattribute:: geosoft.gxapi.FILE_FORM_OPEN

::

   Open a file 

.. autoattribute:: geosoft.gxapi.FILE_FORM_SAVE

::

   Save a file 

.. _GS_DIRECTORY:

GS_DIRECTORY constants
-----------------------------------------------------------------------

::

   Geosoft predefined directory 

.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_NONE


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GEOSOFT


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_BIN


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GER


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_OMN


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_TBL


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_FONTS


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GX


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GS


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_APPS


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_ETC


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_HLP


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GXDEV


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_COMPONENT


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_CSV


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_LIC


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_INI


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_TEMP


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_UETC


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_UMAPTEMPLATE


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_COMPONENT_SCRIPTS


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_COMPONENT_HTML


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_IMG


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_BAR


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_GXNET


.. autoattribute:: geosoft.gxapi.GS_DIRECTORY_MAPTEMPLATE


.. _IMPCH_TYPE:

IMPCH_TYPE constants
-----------------------------------------------------------------------

::

   Import Chem defines 

.. autoattribute:: geosoft.gxapi.IMPCH_TYPE_DATA


.. autoattribute:: geosoft.gxapi.IMPCH_TYPE_ASSAY


.. _WINDOW_STATE:

WINDOW_STATE constants
-----------------------------------------------------------------------

::

   Window State Options 

.. autoattribute:: geosoft.gxapi.WINDOW_RESTORE


.. autoattribute:: geosoft.gxapi.WINDOW_MINIMIZE


.. autoattribute:: geosoft.gxapi.WINDOW_MAXIMIZE


.. _XTOOL_ALIGN:

XTOOL_ALIGN constants
-----------------------------------------------------------------------

::

   XTool docking alignment flags 

.. autoattribute:: geosoft.gxapi.XTOOL_ALIGN_LEFT


.. autoattribute:: geosoft.gxapi.XTOOL_ALIGN_TOP


.. autoattribute:: geosoft.gxapi.XTOOL_ALIGN_RIGHT


.. autoattribute:: geosoft.gxapi.XTOOL_ALIGN_BOTTOM


.. autoattribute:: geosoft.gxapi.XTOOL_ALIGN_ANY


.. _XTOOL_DOCK:

XTOOL_DOCK constants
-----------------------------------------------------------------------

::

   XTool default docking state 

.. autoattribute:: geosoft.gxapi.XTOOL_DOCK_TOP


.. autoattribute:: geosoft.gxapi.XTOOL_DOCK_LEFT


.. autoattribute:: geosoft.gxapi.XTOOL_DOCK_RIGHT


.. autoattribute:: geosoft.gxapi.XTOOL_DOCK_BOTTOM


.. autoattribute:: geosoft.gxapi.XTOOL_DOCK_FLOAT


	