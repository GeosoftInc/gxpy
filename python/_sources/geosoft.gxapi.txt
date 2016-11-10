Geosoft GX API
==============

The Geosoft GX API is exposed to python developers through the :code:`geosoft.gxapi` module.  The API includes the full set of
low-level function calls that expose almost all Geosoft functionality to developer.

GX API Reference
----------------

   :doc:`GX API Class/Library Reference... </geosoft.gxapi.classes>`

The GXContext class
-------------------

.. autoclass:: geosoft.gxapi.GXContext
   :members:

.. note::
	There should be a single instance of this class constructed in a global location prior to using any other GX API
	classes and their methods. By default the module will only function if an installed *Oasis montaj* product is found since
	it loads the dlls that are shipped with *Oasis montaj* for the actual functionality.

	It is possible to redirect the location of dlls used by setting the :code:`GX_GEOSOFT_BIN_PATH` environment variable.
	This can be done either using the normal *Windows* mechanisms (i.e. via :code:`set` command line or *Advanced System Settings->Environment Variables*)
	or directly in Python code by using :code:`os.putenv("GX_GEOSOFT_BIN_PATH", ...)`. If your intention is to use the
	public standalone API that is shipped with *GX Developer* then this should be set to wherever
	the :code:`GeosoftFiles` redistributable folder is copied or installed.

	The UI console functions are inteded for extension scripts or scripts running in Oasis montaj or other UI applications
	and are launched with :func:`geosoft.gxapi.GXSYS.run_gx`. The GX execution engine will detect if it is not running
	in a console and create a console for that can be shown or hidden by default with a setting. 


Helper classes to pass immutable values by reference
----------------------------------------------------

Each of the classes below can be used to pass these immutable types by reference to the GX API.
Instances of the objects have a :code`value` property that holds the reference to the immutable.

.. autoclass:: geosoft.gxapi.str_ref()

.. autoclass:: geosoft.gxapi.bool_ref()

.. autoclass:: geosoft.gxapi.int_ref()

.. autoclass:: geosoft.gxapi.float_ref()

Default instances will be intialized with dummy values for :code:`float_ref` and :code:`int_ref`, an empty string
for :code:`str_ref` and :code:`False` for :code:`bool_ref`. One can also set the value during intialization or assigning
to the :code:`value` property.

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

Exceptions
----------

.. autoexception:: geosoft.gxapi.GXCancel

.. autoexception:: geosoft.gxapi.GXExit

.. autoexception:: geosoft.gxapi.GXAPIError

.. autoexception:: geosoft.gxapi.GXError


