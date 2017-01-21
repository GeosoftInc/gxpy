.. _toc:

Table of Contents
=================

.. toctree::
   :maxdepth: 2

   index
{% for gxclass in classes %}{% if not gxclass.name == "GEO" and not gxclass.name == "GEOSOFT" %} 
   GX{{ gxclass.name }}{% endif %}{% endfor %}

   toc
