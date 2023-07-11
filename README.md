# Geosoft GX for Python Repository

This is the repository for Seequent's Geosoft GX Developer support for Python development. Refer to the documentation for more information.

[GX Developer documentation](https://geosoftgxdev.atlassian.net/wiki/display/GD/Python+in+GX+Developer)

From release 9.6, tutorials for various subjects are available as Jupyter Notebooks, and are added as subjects are developed.  See the following github page for what is currently available:

https://github.com/GeosoftInc/gxpy/tree/master/examples/jupyter_notebooks/Tutorials
(Select the branch that matches the GX Developer version you are working with.)

If you are new to GX Developer, refer to the [GX Developer tutorial](https://geosoftgxdev.atlassian.net/wiki/spaces/GXD93/pages/103153671/Python+Tutorial+for+Geosoft+GX+Developer) that is documented as part of the 9.3 release.

[Python Packages](https://github.com/GeosoftInc/gxpy/wiki)

Also see the [Geosoft organization on Github](https://github.com/GeosoftInc) for the other programming language specific repos.

Quick Start
-----------

### Configuration ###

See [Python Configuration Menu](https://github.com/GeosoftInc/gxpy/wiki/Python-menu-for-Geosoft-Desktop) to install a Python menu that simplifies Python configuration for an Oasis montaj installation.

To update an existing Python installation, load the Python menu from your User Menus and select Python > Configure Python... > update geosoft package.

If you encounter problems due to a non-standard installation you can also update Python manually (see below).  

### Manual Configuration ###

Uninstall Geosoft from Python, then install version 2023.1 as follows (you must have the Geosoft Desktop 2023.1 platform installed).

```
pip uninstall geosoft
pip install geosoft
```

Or, alternately:

```
pip install geosoft --upgrade
```

### Version Compatibility ###
The base GX API, which is exposed to Python by the ___geosoft.gxapi___ module, is consistent across versions. This means that earlier versions of ___geosoft.pxpy___ will work with Geosoft Desktop 2023.1. While we recommend that older scripts be updated to conform to the 2023.1 API, should you need support for multiple versions of ___geosoft.gxpy___ you can create separate Anaconda Python environments for each version. For example, you might create an environment ___'py35_gx91'___ for Python 3.5 and the GX API version 9.1, ___'py36_gx92'___ for Python 3.6 and GX Developer 9.2 and 'py36_gx96' for GX Developer 9.6. If you do not depend on earlier versions of the GX Developer Python API it is best to use only the most recently released API.

Vesion 2023.1 supports Python 3.7, 3.8, 3.9 and 3.10. If you need Python 3.4 support, install geosoft version 9.2.1, which will work with both Geosoft Desktop versions 9.2 and 9.5, but will not contain any methods and classes introduced since version 9.2. If you need Python 3.5 support, install geosoft version 9.5, which will work with both Geosoft Desktop and redistributable versions 9.5 and 9.6, but will not contain any methods and classes introduced since version 9.6.

License
-------

Any source code found here are released under the [BSD 2-clause license](https://github.com/GeosoftInc/gxpy/blob/master/LICENSE). Core functionality exposed by the GX API may have additional license implications. For more information consult the [License page in the GX Developer Wiki](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License)
