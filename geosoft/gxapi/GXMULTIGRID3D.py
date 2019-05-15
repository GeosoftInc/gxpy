### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXGRID3D import GXGRID3D
from .GXPG import GXPG


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMULTIGRID3D(gxapi_cy.WrapMULTIGRID3D):
    """
    GXMULTIGRID3D class.

    High Performance 3D Grid.
    """

    def __init__(self, handle=0):
        super(GXMULTIGRID3D, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>`
        
        :returns: A null `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>`
        :rtype:   GXMULTIGRID3D
        """
        return GXMULTIGRID3D()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def open(cls, name):
        """
        Opens an existing Multivoxset
        
        :param name:  File Name
        :type  name:  str

        :returns:     `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` handle, terminates if creation fails
        :rtype:       GXMULTIGRID3D

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMULTIGRID3D._open(GXContext._get_tls_geo(), name.encode())
        return GXMULTIGRID3D(ret_val)



    @classmethod
    def modify(cls, name):
        """
        Opens an existing Multivoxset with an plan to modify it
        
        :param name:  File Name
        :type  name:  str

        :returns:     `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` handle, terminates if creation fails
        :rtype:       GXMULTIGRID3D

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMULTIGRID3D._modify(GXContext._get_tls_geo(), name.encode())
        return GXMULTIGRID3D(ret_val)



    @classmethod
    def create(cls, name, size_x, size_y, size_z):
        """
        Creates a new Multivoxset
        
        :param name:    File Name
        :param size_x:  Size in X.
        :param size_y:  Size in Y.
        :param size_z:  Size in Z.
        :type  name:    str
        :type  size_x:  int
        :type  size_y:  int
        :type  size_z:  int

        :returns:       `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` handle, terminates if creation fails
        :rtype:         GXMULTIGRID3D

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMULTIGRID3D._create(GXContext._get_tls_geo(), name.encode(), size_x, size_y, size_z)
        return GXMULTIGRID3D(ret_val)




    def duplicate(self, name):
        """
        Creates an MULTIGRID3D with identical geometry to the input
        
        :param name:         File Name
        :type  name:         str

        :returns:            `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` handle, terminates if creation fails
        :rtype:              GXMULTIGRID3D

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._duplicate(name.encode())
        return GXMULTIGRID3D(ret_val)




    def get_default(self):
        """
        Get the default voxset
        

        :returns:            `GXGRID3D <geosoft.gxapi.GXGRID3D>` handle, terminates if creation fails
        :rtype:              GXGRID3D

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_default()
        return GXGRID3D(ret_val)




    def create_default(self, type):
        """
        Get the default voxset
        
        :param type:         :ref:`GRID3D_TYPE`
        :type  type:         int

        :returns:            `GXGRID3D <geosoft.gxapi.GXGRID3D>` handle, terminates if creation fails
        :rtype:              GXGRID3D

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._create_default(type)
        return GXGRID3D(ret_val)




    def is_uniform_cell_size_x(self):
        """
        Is the cell uniform in the X direction
        
        :rtype:              bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_uniform_cell_size_x()
        return ret_val




    def is_uniform_cell_size_y(self):
        """
        Is the cell uniform in the Y direction
        
        :rtype:              bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_uniform_cell_size_y()
        return ret_val




    def is_uniform_cell_size_z(self):
        """
        Is the cell uniform in the Z direction
        
        :rtype:              bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._is_uniform_cell_size_z()
        return ret_val




    def get_size_x(self):
        """
        Get the number of cells in the X direction
        
        :rtype:              int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_size_x()
        return ret_val




    def get_size_y(self):
        """
        Get the number of cells in the X direction
        
        :rtype:              int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_size_y()
        return ret_val




    def get_size_z(self):
        """
        Get the number of cells in the X direction
        
        :rtype:              int

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_size_z()
        return ret_val




    def get_cell_sizes_x(self, vv):
        """
        Get the cell sizes in the X direction
        
        :param vv:           X `GXVV <geosoft.gxapi.GXVV>`
        :type  vv:           GXVV

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_cell_sizes_x(vv)
        




    def get_cell_sizes_y(self, vv):
        """
        Get the cell sizes in the Y direction
        
        :param vv:           Y `GXVV <geosoft.gxapi.GXVV>`
        :type  vv:           GXVV

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_cell_sizes_y(vv)
        




    def get_cell_sizes_z(self, vv):
        """
        Get the cell sizes in the Z direction
        
        :param vv:           Z `GXVV <geosoft.gxapi.GXVV>`
        :type  vv:           GXVV

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_cell_sizes_z(vv)
        




    def set_cell_sizes_x(self, vv):
        """
        Set the cell sizes in the X direction
        
        :param vv:           X `GXVV <geosoft.gxapi.GXVV>`
        :type  vv:           GXVV

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_cell_sizes_x(vv)
        




    def set_cell_sizes_y(self, vv):
        """
        Set the cell sizes in the Y direction
        
        :param vv:           Y `GXVV <geosoft.gxapi.GXVV>`
        :type  vv:           GXVV

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_cell_sizes_y(vv)
        




    def set_cell_sizes_z(self, vv):
        """
        Set the cell sizes in the Z direction
        
        :param vv:           Z `GXVV <geosoft.gxapi.GXVV>`
        :type  vv:           GXVV

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_cell_sizes_z(vv)
        




    def get_uniform_cell_size_x(self):
        """
        Get the uniform cell size in the X direction
        
        :rtype:              float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_uniform_cell_size_x()
        return ret_val




    def get_uniform_cell_size_y(self):
        """
        Get the uniform cell size in the Y direction
        
        :rtype:              float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_uniform_cell_size_y()
        return ret_val




    def get_uniform_cell_size_z(self):
        """
        Get the uniform cell size in the Z direction
        
        :rtype:              float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_uniform_cell_size_z()
        return ret_val




    def set_uniform_cell_size_x(self, cellsize):
        """
        Set the uniform cell size in the X direction
        
        :param cellsize:     cell size
        :type  cellsize:     float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_uniform_cell_size_x(cellsize)
        




    def set_uniform_cell_size_y(self, cellsize):
        """
        Get the uniform cell size in the Y direction
        
        :param cellsize:     cell size
        :type  cellsize:     float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_uniform_cell_size_y(cellsize)
        




    def set_uniform_cell_size_z(self, cellsize):
        """
        Get the uniform cell size in the Z direction
        
        :param cellsize:     cell size
        :type  cellsize:     float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_uniform_cell_size_z(cellsize)
        




    def get_origin(self, origin_x, origin_y, origin_z):
        """
        Get the origin
        
        :param origin_x:     x
        :param origin_y:     y
        :param origin_z:     z
        :type  origin_x:     float_ref
        :type  origin_y:     float_ref
        :type  origin_z:     float_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        origin_x.value, origin_y.value, origin_z.value = self._get_origin(origin_x.value, origin_y.value, origin_z.value)
        




    def set_origin(self, origin_x, origin_y, origin_z):
        """
        Set the origin
        
        :param origin_x:     x
        :param origin_y:     y
        :param origin_z:     z
        :type  origin_x:     float
        :type  origin_y:     float
        :type  origin_z:     float

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_origin(origin_x, origin_y, origin_z)
        




    def get_bounding_box(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the bounding box
        
        :param min_x:        minx
        :param min_y:        miny
        :param min_z:        minz
        :param max_x:        maxx
        :param max_y:        maxy
        :param max_z:        maxz
        :type  min_x:        float_ref
        :type  min_y:        float_ref
        :type  min_z:        float_ref
        :type  max_x:        float_ref
        :type  max_y:        float_ref
        :type  max_z:        float_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._get_bounding_box(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_volume_vectors(self, origin_x, origin_y, origin_z, X_vector_x, X_vector_y, X_vector_z, Y_vector_x, Y_vector_y, Y_vector_z, Z_vector_x, Z_vector_y, Z_vector_z):
        """
        Get the direction of the volume
        
        :param origin_x:     origin_x
        :param origin_y:     origin_y
        :param origin_z:     origin_z
        :param X_vector_x:   X Vector x
        :param X_vector_y:   X Vector y
        :param X_vector_z:   X Vector z
        :param Y_vector_x:   Y Vector x
        :param Y_vector_y:   Y Vector y
        :param Y_vector_z:   Y Vector z
        :param Z_vector_x:   Z Vector x
        :param Z_vector_y:   Z Vector y
        :param Z_vector_z:   Z Vector z
        :type  origin_x:     float_ref
        :type  origin_y:     float_ref
        :type  origin_z:     float_ref
        :type  X_vector_x:   float_ref
        :type  X_vector_y:   float_ref
        :type  X_vector_z:   float_ref
        :type  Y_vector_x:   float_ref
        :type  Y_vector_y:   float_ref
        :type  Y_vector_z:   float_ref
        :type  Z_vector_x:   float_ref
        :type  Z_vector_y:   float_ref
        :type  Z_vector_z:   float_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        origin_x.value, origin_y.value, origin_z.value, X_vector_x.value, X_vector_y.value, X_vector_z.value, Y_vector_x.value, Y_vector_y.value, Y_vector_z.value, Z_vector_x.value, Z_vector_y.value, Z_vector_z.value = self._get_volume_vectors(origin_x.value, origin_y.value, origin_z.value, X_vector_x.value, X_vector_y.value, X_vector_z.value, Y_vector_x.value, Y_vector_y.value, Y_vector_z.value, Z_vector_x.value, Z_vector_y.value, Z_vector_z.value)
        




    def get_oriented_data_extents(self, oriented_origin_x, oriented_origin_y, oriented_origin_z, X_vector_x, X_vector_y, X_vector_z, Y_vector_x, Y_vector_y, Y_vector_z, Z_vector_x, Z_vector_y, Z_vector_z, p1_x, p1_y, p1_z, p2_x, p2_y, p2_z):
        """
        Get the data extents based on an orientation
        
        :param oriented_origin_x:  oriented_origin_x
        :param oriented_origin_y:  oriented_origin_y
        :param oriented_origin_z:  oriented_origin_z
        :param X_vector_x:         X Vector x
        :param X_vector_y:         X Vector y
        :param X_vector_z:         X Vector z
        :param Y_vector_x:         Y Vector x
        :param Y_vector_y:         Y Vector y
        :param Y_vector_z:         Y Vector z
        :param Z_vector_x:         Z Vector x
        :param Z_vector_y:         Z Vector y
        :param Z_vector_z:         Z Vector z
        :param p1_x:               Point1 x
        :param p1_y:               Point1 y
        :param p1_z:               Point1 z
        :param p2_x:               Point2 x
        :param p2_y:               Point2 y
        :param p2_z:               Point2 z
        :type  oriented_origin_x:  float
        :type  oriented_origin_y:  float
        :type  oriented_origin_z:  float
        :type  X_vector_x:         float
        :type  X_vector_y:         float
        :type  X_vector_z:         float
        :type  Y_vector_x:         float
        :type  Y_vector_y:         float
        :type  Y_vector_z:         float
        :type  Z_vector_x:         float
        :type  Z_vector_y:         float
        :type  Z_vector_z:         float
        :type  p1_x:               float_ref
        :type  p1_y:               float_ref
        :type  p1_z:               float_ref
        :type  p2_x:               float_ref
        :type  p2_y:               float_ref
        :type  p2_z:               float_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        p1_x.value, p1_y.value, p1_z.value, p2_x.value, p2_y.value, p2_z.value = self._get_oriented_data_extents(oriented_origin_x, oriented_origin_y, oriented_origin_z, X_vector_x, X_vector_y, X_vector_z, Y_vector_x, Y_vector_y, Y_vector_z, Z_vector_x, Z_vector_y, Z_vector_z, p1_x.value, p1_y.value, p1_z.value, p2_x.value, p2_y.value, p2_z.value)
        




    def get_section_cell_sizes(self, azimuth, scale, origin_x, origin_y, origin_z, cell_size_x, cell_size_y):
        """
        Get the cell sizes of a section
        
        :param azimuth:      azimuth
        :param scale:        scale
        :param origin_x:     x origin
        :param origin_y:     y origin
        :param origin_z:     z origin
        :param cell_size_x:  cell size in x
        :param cell_size_y:  cell size in y
        :type  azimuth:      float
        :type  scale:        float
        :type  origin_x:     float
        :type  origin_y:     float
        :type  origin_z:     float
        :type  cell_size_x:  float_ref
        :type  cell_size_y:  float_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        cell_size_x.value, cell_size_y.value = self._get_section_cell_sizes(azimuth, scale, origin_x, origin_y, origin_z, cell_size_x.value, cell_size_y.value)
        




    def get_vector_orientation(self, inc, dec, cell_size_y):
        """
        Get the vector voxel orientation
        
        :param inc:          inclination
        :param dec:          declination
        :param cell_size_y:  rotated
        :type  inc:          float_ref
        :type  dec:          float_ref
        :type  cell_size_y:  int_ref

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        inc.value, dec.value, cell_size_y.value = self._get_vector_orientation(inc.value, dec.value, cell_size_y.value)
        




    def fill(self, output_file, method, fill_value):
        """
        Fill a grid3d.
        
        :param output_file:  Name of the output grid3d
        :param method:       :ref:`PGU_INTERP_ORDER`
        :param fill_value:   Fill Value
        :type  output_file:  str
        :type  method:       int
        :type  fill_value:   float

        .. versionadded:: 9.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._fill(output_file.encode(), method, fill_value)
        




    def get_ipj(self, ipj):
        """
        Get the projection of the multigrid3d.
        
        :param ipj:          `GXIPJ <geosoft.gxapi.GXIPJ>` object
        :type  ipj:          GXIPJ

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_ipj(ipj)
        




    def set_ipj(self, ipj):
        """
        Set the projection of the multigrid3d.
        
        :param ipj:          `GXIPJ <geosoft.gxapi.GXIPJ>` object
        :type  ipj:          GXIPJ

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_ipj(ipj)
        




    def export_to_xyz(self, xyz, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to an XYZ File
        
        :param xyz:          File Name
        :param dir:          :ref:`DIRECTION3D`
        :param rev_x:        Reverse X?
        :param rev_y:        Reverse Y?
        :param rev_z:        Reverse Z?
        :param dummies:      Write Dummies?
        :type  xyz:          str
        :type  dir:          int
        :type  rev_x:        bool
        :type  rev_y:        bool
        :type  rev_z:        bool
        :type  dummies:      bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_to_xyz(xyz.encode(), dir, rev_x, rev_y, rev_z, dummies)
        




    def export_to_binary(self, binary_file, dir, rev_x, rev_y, rev_z, swap, output_type):
        """
        Export contents of `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to a Binary File.
        
        :param binary_file:  Binary file to write to
        :param dir:          :ref:`DIRECTION3D`
        :param rev_x:        Reverse X?
        :param rev_y:        Reverse Y?
        :param rev_z:        Reverse Z?
        :param swap:         Swap Bytes?
        :param output_type:  Output Type (Geosoft Type)
        :type  binary_file:  str
        :type  dir:          int
        :type  rev_x:        bool
        :type  rev_y:        bool
        :type  rev_z:        bool
        :type  swap:         bool
        :type  output_type:  int

        .. versionadded:: 9.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._export_to_binary(binary_file.encode(), dir, rev_x, rev_y, rev_z, swap, output_type)
        




    def export_to_xml(self, xml_file):
        """
        Export a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to XML
        
        :param xml_file:     XML file
        :type  xml_file:     str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_to_xml(xml_file.encode())
        




    def export_to_wa(self, wa, dir, rev_x, rev_y, rev_z, dummy):
        """
        Export To GDB
        
        :param wa:           `GXWA <geosoft.gxapi.GXWA>` File
        :param dir:          :ref:`DIRECTION3D`
        :param rev_x:        Reverse X?
        :param rev_y:        Reverse Y?
        :param rev_z:        Reverse Z?
        :param dummy:        The Dummy string to write
        :type  wa:           GXWA
        :type  dir:          int
        :type  rev_x:        bool
        :type  rev_y:        bool
        :type  rev_z:        bool
        :type  dummy:        str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_to_wa(wa, dir, rev_x, rev_y, rev_z, dummy.encode())
        




    def export_to_gdb(self, db, chan, dir, rev_x, rev_y, rev_z, dummies):
        """
        Export To GDB
        
        :param db:           Database
        :param chan:         Channel Name
        :param dir:          :ref:`DIRECTION3D`
        :param rev_x:        Reverse X?
        :param rev_y:        Reverse Y?
        :param rev_z:        Reverse Z?
        :param dummies:      Write Dummies?
        :type  db:           GXDB
        :type  chan:         str
        :type  dir:          int
        :type  rev_x:        bool
        :type  rev_y:        bool
        :type  rev_z:        bool
        :type  dummies:      bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_to_gdb(db, chan.encode(), dir, rev_x, rev_y, rev_z, dummies)
        




    def export_to_pg(self):
        """
        Export a MULTIGRID3D To a PG
        

        :returns:            `GXPG <geosoft.gxapi.GXPG>` Object
        :rtype:              GXPG

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._export_to_pg()
        return GXPG(ret_val)




    def get_data_extents(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the voxel size that has non-dummy data.
        
        :param min_x:        Index of minimum valid data in X.
        :param min_y:        Index of minimum valid data in Y.
        :param min_z:        Index of minimum valid data in Z.
        :param max_x:        Index of maximum valid data in X.
        :param max_y:        Index of maximum valid data in Y.
        :param max_z:        Index of maximum valid data in Z.
        :type  min_x:        int_ref
        :type  min_y:        int_ref
        :type  min_z:        int_ref
        :type  max_x:        int_ref
        :type  max_y:        int_ref
        :type  max_z:        int_ref

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Find the non-dummy volume of a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` object. If the voxel is all dummies,
        returns `iMAX <geosoft.gxapi.iMAX>` for the minima, and `iMIN <geosoft.gxapi.iMIN>` for the maxima.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._get_data_extents(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        




    def get_data_ground_extents(self, min_x, min_y, min_z, max_x, max_y, max_z):
        """
        Get the voxel size in ground units that has non-dummy data.
        
        :param min_x:        Ground location of minimum valid data in X.
        :param min_y:        Ground location of minimum valid data in Y.
        :param min_z:        Ground location of minimum valid data in Z.
        :param max_x:        Ground location of maximum valid data in X.
        :param max_y:        Ground location of maximum valid data in Y.
        :param max_z:        Ground location of maximum valid data in Z.
        :type  min_x:        float_ref
        :type  min_y:        float_ref
        :type  min_z:        float_ref
        :type  max_x:        float_ref
        :type  max_y:        float_ref
        :type  max_z:        float_ref

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Find the non-dummy volume of a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` object. If the voxel is all dummies,
        returns `iMAX <geosoft.gxapi.iMAX>` for the minima, and `iMIN <geosoft.gxapi.iMIN>` for the maxima.
        """
        min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value = self._get_data_ground_extents(min_x.value, min_y.value, min_z.value, max_x.value, max_y.value, max_z.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer