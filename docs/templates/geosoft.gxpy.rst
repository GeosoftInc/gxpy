geosoft.gxpy module reference
=============================

The :code:`geosoft.gxpy` modules provide a Python-oriented API that takes advantage of Python to simplify
much of the complexity of the `low-level GX API <geosoft.gxapi.html>`__.

Submodules
----------

The following sub-modules organize functions into logical groups.

    ======================================= =========================================================================================================================
{% for module in modules %}    :mod:`geosoft.gxpy.{{ module[0] }}`{{ module[1]|indent(20 - module[0]|length, True) }}
{% endfor %}
    ======================================= =========================================================================================================================

See https://github.com/GeosoftInc/gxpy/tree/master/examples for example scripts that use the Python modules.

.. automodule:: geosoft.gxpy
    :members:
    :undoc-members:
    :show-inheritance:
