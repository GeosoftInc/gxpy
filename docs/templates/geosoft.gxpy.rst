.. _gxpy:

gxpy modules reference
======================

The :mod:`geosoft.gxpy` modules provide a Python-oriented API that takes advantage of Python to simplify
much of the complexity of the `low-level GX API <geosoft.gxapi.html>`__.

Submodules
----------

The following sub-modules organize functions into logical groups.

.. currentmodule:: geosoft.gxpy

.. autosummary::
   :toctree:

{% for module in modules %}   geosoft.gxpy.{{ module[0] }}
{% endfor %}


See https://github.com/GeosoftInc/gxpy/tree/master/examples for example scripts that use the Python modules.

.. automodule:: geosoft.gxpy
    :members:
    :undoc-members:
    :show-inheritance:
