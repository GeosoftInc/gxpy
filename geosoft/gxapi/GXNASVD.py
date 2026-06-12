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
class GXNASVD(gxapi_cy.WrapNASVD):
    """
    GXNASVD class.

    The `GXNASVD <geosoft.gxapi.GXNASVD>` class provides functionality for Noise-Adjusted Singular Value Decomposition
    (NASVD) analysis of spectral data. This class wraps the GamMontaj library functions
    for performing Hovgaard-normalized SVD analysis and spectral reconstruction.

    The database (`GXDB <geosoft.gxapi.GXDB>`) provided to the NASVD class is cached and used for later reconstruction,
    so the database must remain valid for the lifetime of the NASVD object.
    """

    def __init__(self, handle=0):
        super(GXNASVD, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXNASVD <geosoft.gxapi.GXNASVD>`
        
        :returns: A null `GXNASVD <geosoft.gxapi.GXNASVD>`
        :rtype:   GXNASVD
        """
        return GXNASVD()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Constructors


    @classmethod
    def create(cls, db, channel, mask_channel, num_components, start, end):
        """
        
        Create an NASVD object and perform SVD analysis
        
        :param db:              `GXDB <geosoft.gxapi.GXDB>` Object
        :param channel:         Spectral data channel name
        :param mask_channel:    mask_channel name (optional)
        :param num_components:  Number of eigenvectors to calculate (1 to min(M,N))
        :param start:           Inclusive starting index of the spectral data, ranging from (1, numChannels). Provide 1 or `GS_S4DM <geosoft.gxapi.GS_S4DM>` to use the beginning of the spectrum.
        :param end:             Inclusive ending index of the spectral data, ranging from (1, numChannels). Provide numChannels or `GS_S4DM <geosoft.gxapi.GS_S4DM>` to use the end of the spectrum.
        :type  db:              GXDB
        :type  channel:         str
        :type  mask_channel:    str
        :type  num_components:  int
        :type  start:           int
        :type  end:             int

        :returns:               NASVD Object
        :rtype:                 GXNASVD

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Creates an NASVD object and performs the initial Hovgaard-normalized SVD analysis
        on the specified spectral channel data. The analysis extracts eigenvectors, scores,
        and singular values that can be used for spectral reconstruction and noise reduction.

        The input data is automatically normalized using the Hovgaard method before SVD.
        Results are stored internally in the NASVD object for later reconstruction use, including
        a line list of all lines that were used to calculate the eigenvectors. Subsequent spectra
        reconstruction will apply to the original list of lines used to create the NASVD object.

        It is common in radiometrics processing to exclude certain channels from smoothing operations.
        To facilitate this, 'start' and 'end' are provided as inclusive 1-based indices to define the range of spectral
        data to be used in the analysis. Use 1 or `GS_S4DM <geosoft.gxapi.GS_S4DM>` for 'start' to indicate the beginning of the spectrum,
        and use `GS_S4DM <geosoft.gxapi.GS_S4DM>` for 'end' to indicate the end of the spectrum.

        The optional mask channel allows the pre-selection of rows to include in the analysis.
        A dummy value in the mask channel indicates points not included. Valid data points should be indicated with "1".
        """
        
        ret_val = gxapi_cy.WrapNASVD._create(GXContext._get_tls_geo(), db, channel.encode(), mask_channel.encode(), num_components, start, end)
        return GXNASVD(ret_val)




# Destructors





# Analysis



    def get_num_components(self):
        """
        
        Get the number of components calculated during SVD analysis
        

        :returns:      Number of components available
        :rtype:        int

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        ret_val = self._get_num_components()
        return ret_val




    def get_singular_value(self, component):
        """
        
        Get a specific singular value
        
        :param component:  Component index (0-based)
        :type  component:  int

        :returns:          The singular value
        :rtype:            float

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        ret_val = self._get_singular_value(component)
        return ret_val




    def get_eigen_vector(self, component, vv):
        """
        
        Get eigenvector data for a specific component
        
        :param component:  Component index (0-based)
        :param vv:         VV to receive eigenvector data
        :type  component:  int
        :type  vv:         GXVV

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Retrieves the eigenvector data for the specified component index.
        The eigenvector represents the spectral pattern for that component.
        """
        
        self._get_eigen_vector(component, vv)
        




    def get_scores(self, component, vv):
        """
        
        Get score data for a specific component
        
        :param component:  Component index (0-based)
        :param vv:         VV to receive score data
        :type  component:  int
        :type  vv:         GXVV

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Retrieves the score data for the specified component index.
        Scores represent the strength of each component at each spatial location.
        """
        
        self._get_scores(component, vv)
        




    def get_partition_details(self, head, tail, total):
        """
        
        Get the number of pass-through (head and tail) channels, and the total number of channels (head + data + tail).
        
        :param head:   (out) Number of head pass-through channels.
        :param tail:   (out) Number of tail pass-through channels.
        :param total:  (out) Total number of channels, including (head + data + tail).
        :type  head:   int_ref
        :type  tail:   int_ref
        :type  total:  int_ref

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Retrieves the partition details for the specified NASVD object.
        This includes the number of pass-through channels (head and tail) and the total number of channels.
        """
        
        head.value, tail.value, total.value = self._get_partition_details(head.value, tail.value, total.value)
        




# Reconstruction



    def reconstruct_spectrum(self, db, num_components_to_use, output_channel, scores_channel):
        """
        
        Reconstruct spectral data using selected components
        
        :param db:                     `GXDB <geosoft.gxapi.GXDB>` Object
        :param num_components_to_use:  Number of leading components to use for reconstruction
        :param output_channel:         Output channel name for reconstructed spectral data
        :param scores_channel:         scores_output channel name for reconstructed spectral data
        :type  db:                     GXDB
        :type  num_components_to_use:  int
        :type  output_channel:         str
        :type  scores_channel:         str

        .. versionadded:: 2026.1.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Performs spectral reconstruction using only the first N eigenvectors/components.
        This effectively filters the data by removing noise associated with higher-order
        components while preserving the signal in the dominant components.

        The reconstructed data is written to the specified output channel on all lines used
        to create the NASVD object originally (see NASVD::Create, for more details).
        """
        
        self._reconstruct_spectrum(db, num_components_to_use, output_channel.encode(), scores_channel.encode())
        




# Utilities



    def get_cumulative_eigenvector_contribution(self, vv):
        """
        
        Calculate the variance explained by each component
        
        :param vv:     VV to receive cumulative eigenvector contribution percentages
        :type  vv:     GXVV

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Calculates cumulative eigenvector contribution percentages  for each component 
        based on their singular values. This helps determine how many components
        are needed to achieve a desired level of accuracy in the reconstruction.
        """
        
        self._get_cumulative_eigenvector_contribution(vv)
        



    @classmethod
    def get_maximum_element_count(cls, maximum):
        """
        
        Get the maximum number of elements that can be processed by NASVD
        
        :param maximum:  Maximum number of elements (rows * columns) that can be processed by NASVD
        :type  maximum:  int_ref

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Returns the maximum number of elements that can be processed
        by the NASVD algorithm to avoid memory allocation failures. This
        value is stored as an advanced setting in Oasis montaj.
        """
        
        maximum.value = gxapi_cy.WrapNASVD._get_maximum_element_count(GXContext._get_tls_geo(), maximum.value)
        




# Serialization



    def serialize(self, output_directory):
        """
        
        Serialize the NASVD object
        
        :param output_directory:  The output directory to place the serialized files. A new directory will be created if it does not exist. Any existing files in the directory will be overwritten.
        :type  output_directory:  str

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Serializes the NASVD object to a format suitable for storage or transmission.
        """
        
        self._serialize(output_directory.encode())
        



    @classmethod
    def deserialize(cls, output_directory):
        """
        
        Create an NASVD object and perform SVD analysis
        
        :param output_directory:  The output directory containing the serialized files. The directory must exist and contain allrequired files, including eigenvectors, singular values, and scores.
        :type  output_directory:  str

        :returns:                 NASVD Object
        :rtype:                   GXNASVD

        .. versionadded:: 2025.2.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** 
        """
        
        ret_val = gxapi_cy.WrapNASVD._deserialize(GXContext._get_tls_geo(), output_directory.encode())
        return GXNASVD(ret_val)




    def deserialize_scores(self, db, directory_name, scores_channel):
        """
        
        Deserialize the scores matrix from file
        
        :param db:              `GXDB <geosoft.gxapi.GXDB>` Object
        :param directory_name:  The directory containing the serialized scores file. The directory must exist.
        :param scores_channel:  scores_output channel name for reconstructed spectral data
        :type  db:              GXDB
        :type  directory_name:  str
        :type  scores_channel:  str

        :returns:               Scores Object
        :rtype:                 int

        .. versionadded:: 2026.1.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** 
        """
        
        ret_val = self._deserialize_scores(db, directory_name.encode(), scores_channel.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block

### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer