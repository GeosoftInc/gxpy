#  Copyright (c) 2025 Bentley Systems, Incorporated. All rights reserved.

### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
import warnings
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block

### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEVOOBJMETA(gxapi_cy.WrapEVOOBJMETA):
    """
    GXEVOOBJMETA class.

    The `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` class is used to create Evo object metadata including object uuid, object path,
    version id, created at, created by, etag, workspace id, modified at, modified by and bounding box properties.

    **Note:**

    
    """

    def __init__(self, handle=0):
        super(GXEVOOBJMETA, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>`
        
        :returns: A null `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>`
        :rtype:   GXEVOOBJMETA
        """
        return GXEVOOBJMETA()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create_default(cls):
        """
        
        Create an empty `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object.
        

        :returns:    `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object
        :rtype:      GXEVOOBJMETA

        .. versionadded:: 2025.1.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = gxapi_cy.WrapEVOOBJMETA._create_default(GXContext._get_tls_geo())
        return GXEVOOBJMETA(ret_val)



    @classmethod
    def create(cls, metadata):
        """
        
        Create an `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object.
        
        :param metadata:  Evo object metadata in JSON string, refer to H_EVOOBJMETA or annotations for Seequent.Evo.Client.Api.Core.GeoscienceObjectMetadata
        :type  metadata:  str

        :returns:         `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object
        :rtype:           GXEVOOBJMETA

        .. versionadded:: 2025.1.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        ret_val = gxapi_cy.WrapEVOOBJMETA._create(GXContext._get_tls_geo(), metadata.encode())
        return GXEVOOBJMETA(ret_val)






    def get_workspace_id(self, workspace_id):
        """
        
        Return the Evo workspace Id.
        
        :param workspace_id:  workspace id
        :type  workspace_id:  str_ref

        .. versionadded:: 2025.1.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        workspace_id.value = self._get_workspace_id(workspace_id.value.encode())
        




    def get_object_id(self, object_id):
        """
        
        Return the Evo object Id.
        
        :param object_id:  object id
        :type  object_id:  str_ref

        .. versionadded:: 2025.1.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        object_id.value = self._get_object_id(object_id.value.encode())
        




    def get_version_id(self, version_id):
        """
        
        Return the Evo object version Id.
        
        :param version_id:  version id of the Evo object at the time of the last publish
        :type  version_id:  str_ref

        .. versionadded:: 2026.1.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        version_id.value = self._get_version_id(version_id.value.encode())
        




    def get_modified_at(self, modified_at):
        """
        
        Return the Evo object modified at.
        
        :param modified_at:  modified at
        :type  modified_at:  str_ref

        .. versionadded:: 2025.1.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        modified_at.value = self._get_modified_at(modified_at.value.encode())
        




    def get_bounding_box(self, bounding_box):
        """
        
        Get Evo object bounding box in JSON string.
        
        :param bounding_box:  JSON string for bounding box, refer to H_EVOBOUNDINGBOX or annotations for Seequent.Evo.Client.Api.Core.Goose.Model.BoundingBox
        :type  bounding_box:  str_ref

        .. versionadded:: 2025.1.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        bounding_box.value = self._get_bounding_box(bounding_box.value.encode())
        




    def get_source_checksum(self, checksum):
        """
        
        Return the source file checksum stored at publish time.
        
        :param checksum:  SHA-256 checksum hex string of the source file
        :type  checksum:  str_ref

        .. versionadded:: 2026.1.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns the SHA-256 checksum of the local source file (e.g. the Geosoft grid file)
        that was computed when the object was last published to the Evo workspace.
        Returns an empty string if no checksum has been stored.
        The checksum is stored in the metadata JSON via `create <geosoft.gxapi.GXEVOOBJMETA.create>` and
        is not modifiable through a setter — to update it, create a new `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>`
        from an updated JSON string that includes the ``source_checksum`` field.
        """
        
        checksum.value = self._get_source_checksum(checksum.value.encode())
        




    def get_manifest_hash(self, manifest_hash):
        """
        
        Return the manifest hash stored after translation.
        
        :param manifest_hash:  SHA-256 hash hex string of the JSON manifest
        :type  manifest_hash:  str_ref

        .. versionadded:: 2026.2.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns the SHA-256 hash of the JSON manifest file that was computed after
        translating the source file to a geoscience object. The manifest hash uniquely
        identifies the translated object (structure + data references).
        Returns an empty string if no manifest hash has been stored.
        """
        
        manifest_hash.value = self._get_manifest_hash(manifest_hash.value.encode())
        




    def get_blob_hash_count(self):
        """
        
        Return the number of blob hashes stored.
        

        :returns:     Number of blob hashes
        :rtype:       int

        .. versionadded:: 2026.2.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns the count of blob content hashes stored in this metadata object.
        Blob hashes are the content-addressable identifiers for the Parquet data files
        that comprise the geoscience object.
        """
        
        ret_val = self._get_blob_hash_count()
        return ret_val




    def get_blob_hash(self, index, blob_hash):
        """
        
        Return a blob hash by index.
        
        :param index:      zero-based index of the blob hash to retrieve
        :param blob_hash:  blob content hash hex string
        :type  index:      int
        :type  blob_hash:  str_ref

        :returns:          0 on success, 1 if index out of range
        :rtype:            int

        .. versionadded:: 2026.2.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns the blob hash at the specified index. Use `get_blob_hash_count <geosoft.gxapi.GXEVOOBJMETA.get_blob_hash_count>`
        to determine the valid range of indices. Index 0 typically corresponds to the main
        data blob, with subsequent indices for auxiliary data (e.g., additional elevation
        grids or attributes).
        Returns 0 on success, 1 if the index is out of range.
        """
        
        ret_val, blob_hash.value = self._get_blob_hash(index, blob_hash.value.encode())
        return ret_val




    def set_source_checksum(self, checksum):
        """
        
        Set the source file checksum on an existing `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object.
        
        :param checksum:  SHA-256 checksum hex string of the source file
        :type  checksum:  str

        .. versionadded:: 2026.2.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Updates the ``source_checksum`` field in place without affecting any other fields
        (object id, version id, workspace id, path, etc.). Intended for cache-update
        workflows where only the local-file checksum needs to be written back after a
        successful translation or publish, avoiding a full JSON round-trip.
        """
        
        self._set_source_checksum(checksum.encode())
        




    def set_manifest_hash(self, manifest_hash):
        """
        
        Set the manifest hash on an existing `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object.
        
        :param manifest_hash:  SHA-256 hash hex string of the JSON manifest
        :type  manifest_hash:  str

        .. versionadded:: 2026.2.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Updates the ``manifest_hash`` field in place without affecting any other fields.
        The manifest hash is the SHA-256 hash of the translated geoscience object's JSON
        manifest and is used as the Tier 2 cache key.
        """
        
        self._set_manifest_hash(manifest_hash.encode())
        




    def set_blob_hashes(self, blob_hashes_json):
        """
        
        Replace the blob hash list on an existing `GXEVOOBJMETA <geosoft.gxapi.GXEVOOBJMETA>` object.
        
        :param blob_hashes_json:  JSON array string of blob content hash hex strings, e.g. ``["hash1","hash2"]``
        :type  blob_hashes_json:  str

        .. versionadded:: 2026.2.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Replaces the entire ``blob_hashes`` list in a single call using a JSON array
        string (e.g. ``["hash1","hash2"]``).  Passing an empty array (``[]``) clears
        the list.  All other metadata fields are left unchanged.
        Blob hashes are the content-addressable identifiers for the Parquet data files
        that comprise the geoscience object.
        """
        
        self._set_blob_hashes(blob_hashes_json.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block

### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer