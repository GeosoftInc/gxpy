Python Examples
===============

Following are simple examples demonstrate minimal functioning Python extensions and stand-alone Python program.

Python GX Extensions
--------------------

Python extensions have a rungx() function.

Hello user extension...

.. literalinclude:: ../examples/om-extensions/hello_world.py

Add a constant to a channel extension...

.. literalinclude:: ../examples/om-extensions/chanadd.py


Stand-Alone Python Programs
---------------------------

Stand-alone Python scripts create a GX context before calling any other API functions.

Hello user program...

.. literalinclude:: ../examples/stand-alone/hello_world.py

Add a constant to a channel program...

.. literalinclude:: ../examples/stand-alone/chanadd.py