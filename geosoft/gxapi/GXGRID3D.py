### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXGRID3D(gxapi_cy.WrapGRID3D):
    """
    GXGRID3D class.

    High Performance 3D Grid.
    """

    def __init__(self, handle=0):
        super(GXGRID3D, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGRID3D <geosoft.gxapi.GXGRID3D>`
        
        :returns: A null `GXGRID3D <geosoft.gxapi.GXGRID3D>`
        :rtype:   GXGRID3D
        """
        return GXGRID3D()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def get_type(self):
        """
        Get the type of this GRID3D
        
        :rtype:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_type()
        return ret_val




    def is_thematic(self):
        """
        Does this grid3d contain thematic data
        
        :rtype:         bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_thematic()
        return ret_val




    def is_double(self):
        """
        Does this grid3d contain floating point data
        
        :rtype:         bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_double()
        return ret_val




    def is_vector(self):
        """
        Does this grid3d contain vector data
        
        :rtype:         bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_vector()
        return ret_val




    def get_tpat(self, ipj):
        """
        Get the TPAT from the thematic grid3d.
        
        :param ipj:     `GXTPAT <geosoft.gxapi.GXTPAT>` object
        :type  ipj:     GXTPAT

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_tpat(ipj)
        




    def set_tpat(self, ipj):
        """
        Set the TPAT of a thematic grid3d.
        
        :param ipj:     `GXTPAT <geosoft.gxapi.GXTPAT>` object
        :type  ipj:     GXTPAT

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_tpat(ipj)
        




    def get_double_stats(self, num_valid, num_dummies, min, max, mean, stddev):
        """
        Get Double statistics.
        
        :param num_valid:    Number of valid values
        :param num_dummies:  Number of invalid values
        :param min:          Min value
        :param max:          Maximum value
        :param mean:         Mean value
        :param stddev:       Standard Deviation
        :type  num_valid:    int_ref
        :type  num_dummies:  int_ref
        :type  min:          float_ref
        :type  max:          float_ref
        :type  mean:         float_ref
        :type  stddev:       float_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        num_valid.value, num_dummies.value, min.value, max.value, mean.value, stddev.value = self._get_double_stats(num_valid.value, num_dummies.value, min.value, max.value, mean.value, stddev.value)
        




    def get_thematic_stats(self, num_valid, num_dummies, min, max, mean, stddev):
        """
        Get Thematic Data statistics.
        
        :param num_valid:    Number of valid values
        :param num_dummies:  Number of invalid values
        :param min:          Min value
        :param max:          Maximum value
        :param mean:         Mean value
        :param stddev:       Standard Deviation
        :type  num_valid:    int_ref
        :type  num_dummies:  int_ref
        :type  min:          int_ref
        :type  max:          int_ref
        :type  mean:         int_ref
        :type  stddev:       int_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        num_valid.value, num_dummies.value, min.value, max.value, mean.value, stddev.value = self._get_thematic_stats(num_valid.value, num_dummies.value, min.value, max.value, mean.value, stddev.value)
        




    def get_vector_stats(self, num_valid, num_dummies, min_x, min_y, min_z, max_x, max_y, max_z, mean_x, mean_y, mean_z, stddev_x, stddev_y, stddev_z):
        """
        Get Vector Data statistics.
        
        :param num_valid:    Number of valid values
        :param num_dummies:  Number of invalid values
        :param min_x:        Min X value
        :param min_y:        Min Y value
        :param min_z:        Min Z value
        :param max_x:        Maximum X value
        :param max_y:        Maximum Y value
        :param max_z:        Maximum Z value
        :param mean_x:       Mean X value
        :param mean_y:       Mean Y value
        :param mean_z:       Mean Z value
        :param stddev_x:     Standard X Deviation
        :param stddev_y:     Standard Y Deviation
        :param stddev_z:     Standard Z Deviation
        :type  num_valid:    int_ref
        :type  num_dummies:  int_ref
        :type  min_x:        float_ref
        :type  min_y:        float_ref
        :type  min_z:        float_ref
        :type  max_x:        float_ref
        :type  max_y:        float_ref
        :type  max_z:        float_ref
        :type  mean_x:       float_ref
        :type  mean_y:       float_ref
        :type  mean_z:       float_ref
        :type  stddev_x:     float_ref
        :type  stddev_y:     float_ref
        :type  stddev_z:     float_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        num_valid.value, num_dummies.value, min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value, mean_x.value, mean_y.value, mean_z.value, stddev_x.value, stddev_y.value, stddev_z.value = self._get_vector_stats(num_valid.value, num_dummies.value, min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value, mean_x.value, mean_y.value, mean_z.value, stddev_x.value, stddev_y.value, stddev_z.value)
        




    def fill_double(self, value):
        """
        Fill the grid3d with a single double value.
        
        :param value:   Fill Value
        :type  value:   float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._fill_double(value)
        




    def fill_thematic(self, value):
        """
        Fill the grid3d with a single thematic value.
        
        :param value:   Fill Value
        :type  value:   int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._fill_thematic(value)
        




    def fill_vector(self, value_x, value_y, value_z):
        """
        Fill the grid3d with a single vector value.
        
        :param value_x:  Fill Value X
        :param value_y:  Fill Value Y
        :param value_z:  Fill Value Z
        :type  value_x:  float
        :type  value_y:  float
        :type  value_z:  float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._fill_vector(value_x, value_y, value_z)
        




    def get_elements_in_block_x(self):
        """
        Get the number of cells in the block in the X direction
        
        :rtype:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_elements_in_block_x()
        return ret_val




    def get_elements_in_block_y(self):
        """
        Get the number of cells in the block in the Y direction
        
        :rtype:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_elements_in_block_y()
        return ret_val




    def get_elements_in_block_z(self):
        """
        Get the number of cells in the block in the Z direction
        
        :rtype:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_elements_in_block_z()
        return ret_val




    def read_x(self, x, y, z, VV):
        """
        Read data from a GRID3D in the x direction (MOST EFFICIENT)
        
        :param x:       X location
        :param y:       Y location
        :param z:       Z location
        :param VV:      VV Containing Data
        :type  x:       int
        :type  y:       int
        :type  z:       int
        :type  VV:      GXVV
        :rtype:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._read_x(x, y, z, VV)
        return ret_val




    def write_x(self, x, y, z, VV):
        """
        Write data to a GRID3D in the X direction (MOST EFFICIENT)
        
        :param x:       X location
        :param y:       Y location
        :param z:       Z location
        :param VV:      VV Containing Data
        :type  x:       int
        :type  y:       int
        :type  z:       int
        :type  VV:      GXVV
        :rtype:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._write_x(x, y, z, VV)
        return ret_val




    def read_y(self, x, y, z, VV):
        """
        Read data from a GRID3D in the Y direction
        
        :param x:       X location
        :param y:       Y location
        :param z:       Z location
        :param VV:      VV Containing Data
        :type  x:       int
        :type  y:       int
        :type  z:       int
        :type  VV:      GXVV
        :rtype:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._read_y(x, y, z, VV)
        return ret_val




    def write_y(self, x, y, z, VV):
        """
        Write data to a GRID3D in the Y direction
        
        :param x:       X location
        :param y:       Y location
        :param z:       Z location
        :param VV:      VV Containing Data
        :type  x:       int
        :type  y:       int
        :type  z:       int
        :type  VV:      GXVV
        :rtype:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._write_y(x, y, z, VV)
        return ret_val




    def read_z(self, x, y, z, VV):
        """
        Read data from a GRID3D in the Z direction
        
        :param x:       X location
        :param y:       Y location
        :param z:       Z location
        :param VV:      VV Containing Data
        :type  x:       int
        :type  y:       int
        :type  z:       int
        :type  VV:      GXVV
        :rtype:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._read_z(x, y, z, VV)
        return ret_val




    def write_z(self, x, y, z, VV):
        """
        Write data to a GRID3D in the Z direction
        
        :param x:       X location
        :param y:       Y location
        :param z:       Z location
        :param VV:      VV Containing Data
        :type  x:       int
        :type  y:       int
        :type  z:       int
        :type  VV:      GXVV
        :rtype:         int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._write_z(x, y, z, VV)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer