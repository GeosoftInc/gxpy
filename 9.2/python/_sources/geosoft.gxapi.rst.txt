Geosoft GX API
==============

The complete Geosoft GX API is exposed to python developers through the :doc:`geosoft.gxapi </geosoft.gxapi.classes>`
module.  This includes all low-level classes and function calls that expose almost all Geosoft functionality to
a developer.

The GXContext class
-------------------

Before calling any other API function from a stand-alone script (a script that is not run as an extension from
Geosoft Desktop), a GX Context must be created and held.  This can be done by creating an instance of
coordinate_system=:class:`.gxapi.GXContext` or an instance of coordinate_system=:class:`.gxpy.gx.GXpy` which handles the details of
``GXContext`` for you.  We recommend using coordinate_system=:class:`.gxpy.gx.GXpy` unless you have chosen to work only with the
low-level :py:mod:`gxapi`.

Creating a GX context requires **Geosoft Desktop** installed on the target system, from which the
library dll's are located and loaded. **Geosoft Desktop** can be downloaded from
`Geosoft Downloads <https://my.geosoft.com/downloads>`_.

It is possible to redirect the location of dlls used by setting the
**GX_GEOSOFT_BIN_PATH** environment variable to point to the location of the Geosoft binary files.
Refer to the `GX Developer Guide <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/overview>`_ for more
information.

.. autoclass:: geosoft.gxapi.GXContext
   :members:

_sources/config.rst.txt



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


