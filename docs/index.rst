Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
* :ref:`toc`

Introduction
============

Hello World Example
-------------------

.. literalinclude:: ../examples/om-extensions/hello_world.py

.. literalinclude:: ../examples/stand-alone/hello_world.py


The geosoft.gxpy package
------------------------

.. note::
   This package is a work in progress to wrap the generated GX API in an API that can be used to write 
   code in a more pythonic style. For this reason the classes in module do not have the same degree of stability
   between different release versions. That being said, a reasonable effort will be made to maintain API stability 
   unless there is a good enough reason to break it.

:doc:`More... </geosoft.gxpy>`


The GXContext class
-------------------

.. autoclass:: geosoft.gxapi.GXContext
   :members:

.. note::
	There should be a single instance of this class constructed in a global location prior to using any other GX API 
	classes and their methods. By default the module will only function if an installed *Oasis montaj* product is found since
	it loads the dlls that are shipped with *Oasis montaj* for the actual functionality.

	It is possible to redirect the location of dlls used by setting the ``GX_GEOSOFT_BIN_PATH`` environment variable. 
	This can be done either using the normal *Windows* mechanisms (i.e. via ``set`` command line or *Advanced System Settings->Environment Variables*)
	or directly in Python code by using ``os.putenv("GX_GEOSOFT_BIN_PATH", ...)``. If the intention is to use the public standalone API that is shipped with *GX Developer* then this should be set to wherever
	the ``GeosoftFiles`` redistributable folder is copied or installed.
	
Exceptions
----------

.. autoexception:: geosoft.gxapi.GXRuntimeError

.. autoexception:: geosoft.gxapi.GXTerminate

TERMINATE constants
-----------------------------------------------------------------------

::

   Value of :py:exc:GXTerminate indicating cause of termination 

.. autoattribute:: geosoft.gxapi.TERMINATE_EXITED

::

   Normal exit

.. autoattribute:: geosoft.gxapi.TERMINATE_CANCELLED

::

   Opration cancelled

.. autoattribute:: geosoft.gxapi.TERMINATE_USER_ERROR

::

   User error registered


Helper classes to pass immutable values by reference
----------------------------------------------------

Each of the classes below can be used to pass these immutable types by reference to the GX API.
Instances of the objects have a ``value`` property that holds the reference to the immutable.

.. autoclass:: geosoft.gxapi.str_ref()

.. autoclass:: geosoft.gxapi.bool_ref()

.. autoclass:: geosoft.gxapi.int_ref()

.. autoclass:: geosoft.gxapi.float_ref()

Default instances will be intialized with dummy values for ``float_ref`` and ``int_ref``, an empty string
for ``str_ref`` and ``False`` for ``bool_ref``. One can also set the value during intialization or assigning
to the ``value`` property.

Example usage:

.. code-block:: python

   import geosoft.gxapi as gxapi

   ctx = gxapi.GXContext.create("sample", "1.0")
   _3dn = gxapi.GX3DN.create(ctx)

   # the GX3DN get_point_of_view() method requires float_ref class to return values
   distance = gxapi.float_ref() # value property will be initially be gxapi.rDUMMY
   rot1 = gxapi.float_ref(1.01) # value property will be equal to 1.01
   rot2 = gxapi.float_ref(2.0)  # value property will be equal to 2.0
   rot2.value = 4  # value propertyis changed to 4.0

   # the values in the objects will be changed to the current point of view
   _3dn.get_point_of_view(distance, rot1, rot2)

   print(distance.value) # value property will now be 8.0
   print(rot1.value) # value property will now be 0.0
   print(rot2.value) # value property will now be 0.0


Other Classes in the GX API
---------------------------

 

GX3DN class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GX3DN
	:noindex:
	
:ref:`More... <GX3DN>`

 

GX3DV class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GX3DV
	:noindex:
	
:ref:`More... <GX3DV>`

 

GXACQUIRE class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXACQUIRE
	:noindex:
	
:ref:`More... <GXACQUIRE>`

 

GXAGG class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXAGG
	:noindex:
	
:ref:`More... <GXAGG>`

 

GXARCDB class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXARCDB
	:noindex:
	
:ref:`More... <GXARCDB>`

 

GXARCDH class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXARCDH
	:noindex:
	
:ref:`More... <GXARCDH>`

 

GXARCMAP class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXARCMAP
	:noindex:
	
:ref:`More... <GXARCMAP>`

 

GXARCSYS class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXARCSYS
	:noindex:
	
:ref:`More... <GXARCSYS>`

 

GXBF class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXBF
	:noindex:
	
:ref:`More... <GXBF>`

 

GXBIGRID class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXBIGRID
	:noindex:
	
:ref:`More... <GXBIGRID>`

 

GXCHIMERA class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXCHIMERA
	:noindex:
	
:ref:`More... <GXCHIMERA>`

 

GXCOM class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXCOM
	:noindex:
	
:ref:`More... <GXCOM>`

 

GXCSYMB class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXCSYMB
	:noindex:
	
:ref:`More... <GXCSYMB>`

 

GXDAT class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDAT
	:noindex:
	
:ref:`More... <GXDAT>`

 

GXDATALINKD class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDATALINKD
	:noindex:
	
:ref:`More... <GXDATALINKD>`

 

GXDATAMINE class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDATAMINE
	:noindex:
	
:ref:`More... <GXDATAMINE>`

 

GXDB class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDB
	:noindex:
	
:ref:`More... <GXDB>`

 

GXDBREAD class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDBREAD
	:noindex:
	
:ref:`More... <GXDBREAD>`

 

GXDBWRITE class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDBWRITE
	:noindex:
	
:ref:`More... <GXDBWRITE>`

 

GXDGW class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDGW
	:noindex:
	
:ref:`More... <GXDGW>`

 

GXDH class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDH
	:noindex:
	
:ref:`More... <GXDH>`

 

GXDMPPLY class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDMPPLY
	:noindex:
	
:ref:`More... <GXDMPPLY>`

 

GXDOCU class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDOCU
	:noindex:
	
:ref:`More... <GXDOCU>`

 

GXDSEL class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDSEL
	:noindex:
	
:ref:`More... <GXDSEL>`

 

GXDU class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDU
	:noindex:
	
:ref:`More... <GXDU>`

 

GXDXFI class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXDXFI
	:noindex:
	
:ref:`More... <GXDXFI>`

 

GXEDB class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXEDB
	:noindex:
	
:ref:`More... <GXEDB>`

 

GXEDOC class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXEDOC
	:noindex:
	
:ref:`More... <GXEDOC>`

 

GXEMAP class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXEMAP
	:noindex:
	
:ref:`More... <GXEMAP>`

 

GXEMAPTEMPLATE class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXEMAPTEMPLATE
	:noindex:
	
:ref:`More... <GXEMAPTEMPLATE>`

 

GXEUL3 class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXEUL3
	:noindex:
	
:ref:`More... <GXEUL3>`

 

GXEXP class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXEXP
	:noindex:
	
:ref:`More... <GXEXP>`

 

GXEXT class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXEXT
	:noindex:
	
:ref:`More... <GXEXT>`

 

GXFFT class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXFFT
	:noindex:
	
:ref:`More... <GXFFT>`

 

GXFFT2 class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXFFT2
	:noindex:
	
:ref:`More... <GXFFT2>`

 

GXFLT class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXFLT
	:noindex:
	
:ref:`More... <GXFLT>`

 

GXGD class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXGD
	:noindex:
	
:ref:`More... <GXGD>`

 

GXGEOSTRING class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXGEOSTRING
	:noindex:
	
:ref:`More... <GXGEOSTRING>`

 

GXGER class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXGER
	:noindex:
	
:ref:`More... <GXGER>`

 

GXGIS class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXGIS
	:noindex:
	
:ref:`More... <GXGIS>`

 

GXGMSYS class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXGMSYS
	:noindex:
	
:ref:`More... <GXGMSYS>`

 

GXGU class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXGU
	:noindex:
	
:ref:`More... <GXGU>`

 

GXGUI class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXGUI
	:noindex:
	
:ref:`More... <GXGUI>`

 

GXHGD class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXHGD
	:noindex:
	
:ref:`More... <GXHGD>`

 

GXHTTP class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXHTTP
	:noindex:
	
:ref:`More... <GXHTTP>`

 

GXHXYZ class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXHXYZ
	:noindex:
	
:ref:`More... <GXHXYZ>`

 

GXIEXP class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXIEXP
	:noindex:
	
:ref:`More... <GXIEXP>`

 

GXIGRF class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXIGRF
	:noindex:
	
:ref:`More... <GXIGRF>`

 

GXIMG class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXIMG
	:noindex:
	
:ref:`More... <GXIMG>`

 

GXIMU class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXIMU
	:noindex:
	
:ref:`More... <GXIMU>`

 

GXINTERNET class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXINTERNET
	:noindex:
	
:ref:`More... <GXINTERNET>`

 

GXIP class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXIP
	:noindex:
	
:ref:`More... <GXIP>`

 

GXIPGUI class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXIPGUI
	:noindex:
	
:ref:`More... <GXIPGUI>`

 

GXIPJ class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXIPJ
	:noindex:
	
:ref:`More... <GXIPJ>`

 

GXITR class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXITR
	:noindex:
	
:ref:`More... <GXITR>`

 

GXKGRD class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXKGRD
	:noindex:
	
:ref:`More... <GXKGRD>`

 

GXLAYOUT class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXLAYOUT
	:noindex:
	
:ref:`More... <GXLAYOUT>`

 

GXLL2 class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXLL2
	:noindex:
	
:ref:`More... <GXLL2>`

 

GXLMSG class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXLMSG
	:noindex:
	
:ref:`More... <GXLMSG>`

 

GXLPT class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXLPT
	:noindex:
	
:ref:`More... <GXLPT>`

 

GXLST class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXLST
	:noindex:
	
:ref:`More... <GXLST>`

 

GXLTB class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXLTB
	:noindex:
	
:ref:`More... <GXLTB>`

 

GXMAP class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMAP
	:noindex:
	
:ref:`More... <GXMAP>`

 

GXMAPL class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMAPL
	:noindex:
	
:ref:`More... <GXMAPL>`

 

GXMAPTEMPLATE class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMAPTEMPLATE
	:noindex:
	
:ref:`More... <GXMAPTEMPLATE>`

 

GXMATH class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMATH
	:noindex:
	
:ref:`More... <GXMATH>`

 

GXMETA class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMETA
	:noindex:
	
:ref:`More... <GXMETA>`

 

GXMISC class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMISC
	:noindex:
	
:ref:`More... <GXMISC>`

 

GXMSTK class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMSTK
	:noindex:
	
:ref:`More... <GXMSTK>`

 

GXMVG class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMVG
	:noindex:
	
:ref:`More... <GXMVG>`

 

GXMVIEW class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMVIEW
	:noindex:
	
:ref:`More... <GXMVIEW>`

 

GXMVU class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMVU
	:noindex:
	
:ref:`More... <GXMVU>`

 

GXMXD class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXMXD
	:noindex:
	
:ref:`More... <GXMXD>`

 

GXPAT class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXPAT
	:noindex:
	
:ref:`More... <GXPAT>`

 

GXPDF3D class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXPDF3D
	:noindex:
	
:ref:`More... <GXPDF3D>`

 

GXPG class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXPG
	:noindex:
	
:ref:`More... <GXPG>`

 

GXPGEXP class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXPGEXP
	:noindex:
	
:ref:`More... <GXPGEXP>`

 

GXPGU class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXPGU
	:noindex:
	
:ref:`More... <GXPGU>`

 

GXPJ class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXPJ
	:noindex:
	
:ref:`More... <GXPJ>`

 

GXPLY class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXPLY
	:noindex:
	
:ref:`More... <GXPLY>`

 

GXPRAGA3 class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXPRAGA3
	:noindex:
	
:ref:`More... <GXPRAGA3>`

 

GXPROJ class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXPROJ
	:noindex:
	
:ref:`More... <GXPROJ>`

 

GXRA class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXRA
	:noindex:
	
:ref:`More... <GXRA>`

 

GXREG class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXREG
	:noindex:
	
:ref:`More... <GXREG>`

 

GXRGRD class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXRGRD
	:noindex:
	
:ref:`More... <GXRGRD>`

 

GXSBF class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXSBF
	:noindex:
	
:ref:`More... <GXSBF>`

 

GXSEMPLOT class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXSEMPLOT
	:noindex:
	
:ref:`More... <GXSEMPLOT>`

 

GXSHP class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXSHP
	:noindex:
	
:ref:`More... <GXSHP>`

 

GXSQLSRV class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXSQLSRV
	:noindex:
	
:ref:`More... <GXSQLSRV>`

 

GXST class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXST
	:noindex:
	
:ref:`More... <GXST>`

 

GXST2 class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXST2
	:noindex:
	
:ref:`More... <GXST2>`

 

GXSTK class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXSTK
	:noindex:
	
:ref:`More... <GXSTK>`

 

GXSTR class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXSTR
	:noindex:
	
:ref:`More... <GXSTR>`

 

GXSTRINGS class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXSTRINGS
	:noindex:
	
:ref:`More... <GXSTRINGS>`

 

GXSURFACE class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXSURFACE
	:noindex:
	
:ref:`More... <GXSURFACE>`

 

GXSURFACEITEM class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXSURFACEITEM
	:noindex:
	
:ref:`More... <GXSURFACEITEM>`

 

GXSYS class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXSYS
	:noindex:
	
:ref:`More... <GXSYS>`

 

GXTB class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXTB
	:noindex:
	
:ref:`More... <GXTB>`

 

GXTC class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXTC
	:noindex:
	
:ref:`More... <GXTC>`

 

GXTEST class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXTEST
	:noindex:
	
:ref:`More... <GXTEST>`

 

GXTIN class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXTIN
	:noindex:
	
:ref:`More... <GXTIN>`

 

GXTPAT class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXTPAT
	:noindex:
	
:ref:`More... <GXTPAT>`

 

GXTR class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXTR
	:noindex:
	
:ref:`More... <GXTR>`

 

GXTRND class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXTRND
	:noindex:
	
:ref:`More... <GXTRND>`

 

GXUNC class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXUNC
	:noindex:
	
:ref:`More... <GXUNC>`

 

GXUSERMETA class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXUSERMETA
	:noindex:
	
:ref:`More... <GXUSERMETA>`

 

GXVA class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXVA
	:noindex:
	
:ref:`More... <GXVA>`

 

GXVAU class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXVAU
	:noindex:
	
:ref:`More... <GXVAU>`

 

GXVM class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXVM
	:noindex:
	
:ref:`More... <GXVM>`

 

GXVOX class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXVOX
	:noindex:
	
:ref:`More... <GXVOX>`

 

GXVOXD class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXVOXD
	:noindex:
	
:ref:`More... <GXVOXD>`

 

GXVOXE class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXVOXE
	:noindex:
	
:ref:`More... <GXVOXE>`

 

GXVULCAN class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXVULCAN
	:noindex:
	
:ref:`More... <GXVULCAN>`

 

GXVV class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXVV
	:noindex:
	
:ref:`More... <GXVV>`

 

GXVVEXP class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXVVEXP
	:noindex:
	
:ref:`More... <GXVVEXP>`

 

GXVVU class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXVVU
	:noindex:
	
:ref:`More... <GXVVU>`

 

GXWA class 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: geosoft.gxapi.GXWA
	:noindex:
	
:ref:`More... <GXWA>`

   

Global Constants
================

.. include:: GXGEOSOFT.rst

