geosoft.gxpy module reference
=============================

The :code:`geosoft.gxpy` modules provide a Python-oriented API that takes advantage of Python to simplify
much of the complexity of the `low-level GX API <geosoft.gxapi.html>`__.

The following sub-modules organize functions into logical groups.

Submodules
----------

.. toctree::

{% for module in modules %}    geosoft.gxpy.{{ module }}
{% endfor %}

.. automodule:: geosoft.gxpy
    :members:
    :undoc-members:
    :show-inheritance:
