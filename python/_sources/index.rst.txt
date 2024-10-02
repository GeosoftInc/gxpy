
Introduction
============

This is the Python API reference documentation for the Geosoft GX API (and gxpy), which is part of Geosoft GX Developer.
The complete GX Developer programming guide can be found in a separate on-line document:
`GX Developer Guide <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/overview>`__.
The GX Developer Guide has a version for each released version of GX Developer. Refer to the
documentation version that matches the API version noted at the top of this page.

The GX API has two parts:

    1.  The *Geosoft GX API* provides the full low-level library of functions available to all languages,
        including Python.  The *Geosoft GX API* is exposed to python developers through the
        :ref:`geosoft.gxapi modules <geosoft.gxapi.classes>`.

    2.  The *Geosoft gxpy API* is a set of :ref:`Python modules <gxpy>` that provide a
        Pythonic abstraction of key parts of the underlying *Geosoft GX API*.  This hides much of the
        complexity of the low-level *Geosoft GX API*, while providing low-level access where necessary.
        The coding of the *Geosoft gxpy API* Python modules also provides an invaluable reference for
        how to work with the low-level libraries.  The Python source code for the *Geosoft GX API* can
        be found on `github <https://github.com/GeosoftInc/gxpy>`_.

Reference
=========

.. toctree::
   :maxdepth: 1

   geosoft.gxapi.classes
   geosoft.gxpy
   Example scripts... </helloworld>

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
* :ref:`toc`
