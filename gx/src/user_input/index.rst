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

