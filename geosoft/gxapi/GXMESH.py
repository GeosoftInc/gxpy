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
class GXMESH(gxapi_cy.WrapMESH):
    """
    GXMESH class.

    High Performance Surface API.
    """

    def __init__(self, handle=0):
        super(GXMESH, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMESH <geosoft.gxapi.GXMESH>`
        
        :returns: A null `GXMESH <geosoft.gxapi.GXMESH>`
        :rtype:   GXMESH
        """
        return GXMESH()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, name):
        """
        Creates a new Mesh
        
        :param name:  Mesh Name
        :type  name:  str

        :returns:     `GXMESH <geosoft.gxapi.GXMESH>` handle, terminates if creation fails
        :rtype:       GXMESH

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMESH._create(GXContext._get_tls_geo(), name.encode())
        return GXMESH(ret_val)



    @classmethod
    def open(cls, fileName, lstMeshNames):
        """
        Opens an existing Mesh
        
        :param fileName:      File Name
        :param lstMeshNames:  `GXLST <geosoft.gxapi.GXLST>` to fill with Mesh Names
        :type  fileName:      str
        :type  lstMeshNames:  GXLST

        :returns:             `GXMESH <geosoft.gxapi.GXMESH>` handle, terminates if creation fails
        :rtype:               GXMESH

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMESH._open(GXContext._get_tls_geo(), fileName.encode(), lstMeshNames)
        return GXMESH(ret_val)




    def insert_patch(self, mesh_name):
        """
        Inserts a new surface patch to the mesh specified by a unique ID
        
        :param mesh_name:  Mesh Name
        :type  mesh_name:  str

        :returns:          Patch ID of the inserted patch
        :rtype:            int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._insert_patch(mesh_name.encode())
        return ret_val




    def delete_patch(self, mesh_name, patch_id):
        """
        Deletes a patch specified by Patch ID from a mesh
        
        :param mesh_name:  Mesh Name
        :param patch_id:   Patch ID
        :type  mesh_name:  str
        :type  patch_id:   int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._delete_patch(mesh_name.encode(), patch_id)
        




    def patch_exists(self, mesh_name, patch_id):
        """
        Checks if a patch specified by a patch ID exists in a mesh
        
        :param mesh_name:  Mesh Name
        :param patch_id:   Patch ID
        :type  mesh_name:  str
        :type  patch_id:   int

        :returns:          TRUE if patch exists
        :rtype:            bool

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._patch_exists(mesh_name.encode(), patch_id)
        return ret_val




    def num_patches(self, mesh_name):
        """
        Returns the number of patches added to the mesh
        
        :param mesh_name:  Mesh Name
        :type  mesh_name:  str

        :returns:          The number of patches added to the mesh
        :rtype:            int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_patches(mesh_name.encode())
        return ret_val




    def add_vertex(self, mesh_name, patch_id, x, y, z):
        """
        Adds a vertex to a patch in a mesh
        
        :param mesh_name:  Mesh Name
        :param patch_id:   Patch ID
        :param x:          x coordinate of the vertex
        :param y:          y coordinate of the vertex
        :param z:          z coordinate of the vertex
        :type  mesh_name:  str
        :type  patch_id:   int
        :type  x:          float
        :type  y:          float
        :type  z:          float

        :returns:          Returns the vertex index of the added vertex
        :rtype:            int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._add_vertex(mesh_name.encode(), patch_id, x, y, z)
        return ret_val




    def num_vertices(self, mesh_name, patch_id):
        """
        Number of vertices in a patch in mesh
        
        :param mesh_name:  Mesh Name
        :param patch_id:   Patch ID
        :type  mesh_name:  str
        :type  patch_id:   int

        :returns:          Returns the number of vertices in a patch
        :rtype:            int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_vertices(mesh_name.encode(), patch_id)
        return ret_val




    def add_face(self, mesh_name, patch_id, v0, v1, v2):
        """
        Adds a face to a patch in a mesh
        
        :param mesh_name:  Mesh Name
        :param patch_id:   Patch ID
        :param v0:         Vertex index 0 for the face
        :param v1:         Vertex index 1 for the face
        :param v2:         Vertex index 2 for the face
        :type  mesh_name:  str
        :type  patch_id:   int
        :type  v0:         int
        :type  v1:         int
        :type  v2:         int

        :returns:          Returns the face index of the added face
        :rtype:            int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._add_face(mesh_name.encode(), patch_id, v0, v1, v2)
        return ret_val




    def num_faces(self, mesh_name, patch_id):
        """
        Number of faces in a patch in mesh
        
        :param mesh_name:  Mesh Name
        :param patch_id:   Patch ID
        :type  mesh_name:  str
        :type  patch_id:   int

        :returns:          Returns the number of faces in a patch
        :rtype:            int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_faces(mesh_name.encode(), patch_id)
        return ret_val




    def get_vertex_point(self, mesh_name, patch_id, vertex_index, x_coordinate, y_coordinate, z_coordinate):
        """
        Number of faces in a patch in mesh
        
        :param mesh_name:     Mesh Name
        :param patch_id:      Patch ID
        :param vertex_index:  Vertex Index
        :param x_coordinate:  X coordinate
        :param y_coordinate:  Y coordinate
        :param z_coordinate:  Z coordinate
        :type  mesh_name:     str
        :type  patch_id:      int
        :type  vertex_index:  int
        :type  x_coordinate:  float_ref
        :type  y_coordinate:  float_ref
        :type  z_coordinate:  float_ref

        :returns:             Returns the number of faces in a patch
        :rtype:               int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, x_coordinate.value, y_coordinate.value, z_coordinate.value = self._get_vertex_point(mesh_name.encode(), patch_id, vertex_index, x_coordinate.value, y_coordinate.value, z_coordinate.value)
        return ret_val




    def get_vertices(self, mesh_name, patch_id, vert_v_vx, vert_v_vy, vert_v_vz):
        """
        Returns all the vertices in a patch
        
        :param mesh_name:  Mesh Name
        :param patch_id:   Patch ID
        :param vert_v_vx:  Vertices X
        :param vert_v_vy:  Vertices Y
        :param vert_v_vz:  Vertices Z
        :type  mesh_name:  str
        :type  patch_id:   int
        :type  vert_v_vx:  GXVV
        :type  vert_v_vy:  GXVV
        :type  vert_v_vz:  GXVV

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_vertices(mesh_name.encode(), patch_id, vert_v_vx, vert_v_vy, vert_v_vz)
        




    def get_faces(self, mesh_name, patch_id, face_v_1, face_v_2, face_v_3):
        """
        Returns all the faces comprising of vertex indices in a patch
        
        :param mesh_name:  Mesh Name
        :param patch_id:   Patch ID
        :param face_v_1:   Face vertex 1
        :param face_v_2:   Face vertex 2
        :param face_v_3:   Face vertex 3
        :type  mesh_name:  str
        :type  patch_id:   int
        :type  face_v_1:   GXVV
        :type  face_v_2:   GXVV
        :type  face_v_3:   GXVV

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_faces(mesh_name.encode(), patch_id, face_v_1, face_v_2, face_v_3)
        




    def insert_attributes(self, mesh_name, attribute_name, data_type, attribute_type):
        """
        Inserts an attribute set to a mesh
        
        :param mesh_name:       Mesh Name
        :param attribute_name:  Attribute Name
        :param data_type:       :ref:`ATTRIBUTE_DATA_TYPE`
        :param attribute_type:  :ref:`ATTRIBUTE_TYPE`
        :type  mesh_name:       str
        :type  attribute_name:  str
        :type  data_type:       int
        :type  attribute_type:  int

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._insert_attributes(mesh_name.encode(), attribute_name.encode(), data_type, attribute_type)
        




    def set_attribute_values(self, mesh_name, attribute_name, data_type, attribute_type, patch_id, vv):
        """
        Inserts an attribute set to a mesh
        
        :param mesh_name:       Mesh Name
        :param attribute_name:  Attribute Name
        :param data_type:       :ref:`ATTRIBUTE_DATA_TYPE`
        :param attribute_type:  :ref:`ATTRIBUTE_TYPE`
        :param patch_id:        Patch ID
        :param vv:              Attributes VV `GXVV <geosoft.gxapi.GXVV>`
        :type  mesh_name:       str
        :type  attribute_name:  str
        :type  data_type:       int
        :type  attribute_type:  int
        :type  patch_id:        int
        :type  vv:              GXVV

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_attribute_values(mesh_name.encode(), attribute_name.encode(), data_type, attribute_type, patch_id, vv)
        




    def get_attribute_values(self, mesh_name, attribute_name, data_type, attribute_type, patch_id, vv):
        """
        Inserts an attribute set to a mesh
        
        :param mesh_name:       Mesh Name
        :param attribute_name:  Attribute Name
        :param data_type:       :ref:`ATTRIBUTE_DATA_TYPE`
        :param attribute_type:  :ref:`ATTRIBUTE_TYPE`
        :param patch_id:        Patch ID
        :param vv:              Attributes VV `GXVV <geosoft.gxapi.GXVV>`
        :type  mesh_name:       str
        :type  attribute_name:  str
        :type  data_type:       int
        :type  attribute_type:  int
        :type  patch_id:        int
        :type  vv:              GXVV

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_attribute_values(mesh_name.encode(), attribute_name.encode(), data_type, attribute_type, patch_id, vv)
        



    @classmethod
    def import_grid_to_mesh(cls, grid_file_name, geosurface_filename, surface_name):
        """
        Imports a Grid to a Surface. Creates a new Geosurface file for the surface
        
        :param grid_file_name:       Grid File Name
        :param geosurface_filename:  Surface File Name
        :param surface_name:         Surface Item Name within the file
        :type  grid_file_name:       str
        :type  geosurface_filename:  str
        :type  surface_name:         str

        :returns:                    `GXMESH <geosoft.gxapi.GXMESH>` handle, terminates if creation fails
        :rtype:                      GXMESH

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMESH._import_grid_to_mesh(GXContext._get_tls_geo(), grid_file_name.encode(), geosurface_filename.encode(), surface_name.encode())
        return GXMESH(ret_val)




    def save(self):
        """
        Saves Mesh to the Project Cache and Geosurface file
        

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._save()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer