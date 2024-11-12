# Geosoft GX for Python Repository

This is the repository for Seequent's Geosoft GX Developer support for Python development. Refer to the documentation for more information.

[GX Developer documentation](https://geosoftgxdev.atlassian.net/wiki/display/GD/Python+in+GX+Developer)

Tutorials for various subjects are available as Jupyter Notebooks, and are added as subjects are developed.  See the following github page for what is currently available:

https://github.com/GeosoftInc/gxpy/tree/master/examples/jupyter_notebooks/Tutorials
(Select the branch that matches the GX Developer version you are working with.)

If you are new to GX Developer, refer to the [GX Developer tutorial](https://geosoftgxdev.atlassian.net/wiki/spaces/GXD93/pages/103153671/Python+Tutorial+for+Geosoft+GX+Developer)

[Python Packages](https://github.com/GeosoftInc/gxpy/wiki)

Also see the [Geosoft organization on Github](https://github.com/GeosoftInc) for the other programming language specific repos.

Quick Start
-----------

A Python environment is shipped with Oasis Montaj and will be used by default. If you would like to use a different environment installed on your machine, you can configure this in Oasis Montaj from the `Project > Settings > Python...` path in the menu. 
If you choose to use a non-default environment, you will need to manually install the gxpy wheels into that environment
```
envpath\scripts\pip.exe install geosoft
```
See https://pypi.org/project/geosoft/#history to determine for any gxpy version, what python environment version it can be installed into.

The base GX API, which is exposed to Python by the ___geosoft.gxapi___ module, is consistent across versions. This means that earlier versions of ___geosoft.pxpy___ will work with the latest Oasis Montaj. While we recommend that older scripts be updated to conform to the latest version API, should you need support for **multiple** versions of ___geosoft.gxpy___ you can create separate Python environments for each version.

License
-------

Any source code found here are released under the [BSD 2-clause license](https://github.com/GeosoftInc/gxpy/blob/master/LICENSE). Core functionality exposed by the GX API may have additional license implications. For more information consult the [License page in the GX Developer Wiki](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License)
