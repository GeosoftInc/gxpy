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
class GXFFT2(gxapi_cy.WrapFFT2):
    """
    GXFFT2 class.

    2-D Fast Fourier Transforms
    These methods now work with an `GXIMG <geosoft.gxapi.GXIMG>` object, instead of creating
    their own `GXFFT2 <geosoft.gxapi.GXFFT2>` object.
    """

    def __init__(self, handle=0):
        super(GXFFT2, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXFFT2 <geosoft.gxapi.GXFFT2>`
        
        :returns: A null `GXFFT2 <geosoft.gxapi.GXFFT2>`
        :rtype:   GXFFT2
        """
        return GXFFT2()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def fft2_in(cls, im_gi, trn_fil, spc_fil):
        """
        `GXFFT2 <geosoft.gxapi.GXFFT2>` transform
        
        :param im_gi:    Input image
        :param trn_fil:  Output Transform file name string
        :param spc_fil:  Output Power Spectrum file name string
        :type  im_gi:    GXIMG
        :type  trn_fil:  str
        :type  spc_fil:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapFFT2._fft2_in(GXContext._get_tls_geo(), im_gi, trn_fil.encode(), spc_fil.encode())
        



    @classmethod
    def filter_pg(cls, pg, con_fil, tr, dx, dy, rot):
        """
        Apply 2D `GXFFT <geosoft.gxapi.GXFFT>` filters to data in pager
        
        :param pg:       Pager obj
        :param con_fil:  sConFil - `GXFFT <geosoft.gxapi.GXFFT>` filter control file
        :param tr:       `GXTR <geosoft.gxapi.GXTR>` obj
        :param dx:       rDx - X increment
        :param dy:       rDy - Y increment
        :param rot:      rRot- Rotation degree
        :type  pg:       GXPG
        :type  con_fil:  str
        :type  tr:       GXTR
        :type  dx:       float
        :type  dy:       float
        :type  rot:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapFFT2._filter_pg(GXContext._get_tls_geo(), pg, con_fil.encode(), tr, dx, dy, rot)
        



    @classmethod
    def flt(cls, im_gi, out_fil, con_fil):
        """
        `GXFFT2 <geosoft.gxapi.GXFFT2>` filter
        
        :param im_gi:    Input image (Transform grid)
        :param out_fil:  Output file (Transform grid)
        :param con_fil:  Control file
        :type  im_gi:    GXIMG
        :type  out_fil:  str
        :type  con_fil:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapFFT2._flt(GXContext._get_tls_geo(), im_gi, out_fil.encode(), con_fil.encode())
        



    @classmethod
    def flt_inv(cls, im_gi, out_fil, con_fil):
        """
        `GXFFT2 <geosoft.gxapi.GXFFT2>` filter and inverse
        
        :param im_gi:    Input image (Transform grid)
        :param out_fil:  Output file
        :param con_fil:  Control file
        :type  im_gi:    GXIMG
        :type  out_fil:  str
        :type  con_fil:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapFFT2._flt_inv(GXContext._get_tls_geo(), im_gi, out_fil.encode(), con_fil.encode())
        



    @classmethod
    def pow_spc(cls, im_gi, spc_fil):
        """
        `GXFFT2 <geosoft.gxapi.GXFFT2>` transform power spectrum
        
        :param im_gi:    Input image (Transform grid)
        :param spc_fil:  Output Power Spectrum file name string
        :type  im_gi:    GXIMG
        :type  spc_fil:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapFFT2._pow_spc(GXContext._get_tls_geo(), im_gi, spc_fil.encode())
        



    @classmethod
    def rad_spc(cls, im_gi, spc_fil):
        """
        `GXFFT2 <geosoft.gxapi.GXFFT2>` transform Radially averaged power spectrum
        
        :param im_gi:    Input image (Transform grid)
        :param spc_fil:  Output Radial Spectrum file name string
        :type  im_gi:    GXIMG
        :type  spc_fil:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapFFT2._rad_spc(GXContext._get_tls_geo(), im_gi, spc_fil.encode())
        



    @classmethod
    def rad_spc_alt(cls, im_gi, spc_fil):
        """
        `GXFFT2 <geosoft.gxapi.GXFFT2>` transform Radially averaged power spectrum - log before average and no normalization
        
        :param im_gi:    Input image (Transform grid)
        :param spc_fil:  Output Radial Spectrum file name string
        :type  im_gi:    GXIMG
        :type  spc_fil:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapFFT2._rad_spc_alt(GXContext._get_tls_geo(), im_gi, spc_fil.encode())
        



    @classmethod
    def rad_spc1(cls, img, vv):
        """
        `GXFFT2 <geosoft.gxapi.GXFFT2>` transform Radially averaged power spectrum for one `GXIMG <geosoft.gxapi.GXIMG>`
        
        :param img:  Input image (Transform grid)
        :param vv:   Output Radial Spectrum `GXVV <geosoft.gxapi.GXVV>`
        :type  img:  GXIMG
        :type  vv:   GXVV

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapFFT2._rad_spc1(GXContext._get_tls_geo(), img, vv)
        



    @classmethod
    def rad_spc2(cls, img1, img2, vv, v_vst, opt):
        """
        `GXFFT2 <geosoft.gxapi.GXFFT2>` transform Radially averaged power spectrum for two IMGs
        
        :param img1:   Input image1 (Transform grid1 - G)
        :param img2:   Input image2 (Transform grid2 - H)
        :param vv:     Output Radial Spectrum `GXVV <geosoft.gxapi.GXVV>`
        :param v_vst:  Output Radial Spectrum Standard deviation VVst	(Null: no calc)
        :param opt:    lOpt - 1: <Re(GH*/HH*)> `GXVV <geosoft.gxapi.GXVV>`;  0: <Re(GH*)> `GXVV <geosoft.gxapi.GXVV>`
        :type  img1:   GXIMG
        :type  img2:   GXIMG
        :type  vv:     GXVV
        :type  v_vst:  GXVV
        :type  opt:    int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapFFT2._rad_spc2(GXContext._get_tls_geo(), img1, img2, vv, v_vst, opt)
        



    @classmethod
    def td_xd_y(cls, img_tx, img_ty, out_fil, inv_flg):
        """
        `GXFFT2 <geosoft.gxapi.GXFFT2>` filter (calculate T from the derivatives Tx and Ty)
        
        :param img_tx:   Input dX image (Transform grid)
        :param img_ty:   Input dY image (Transform grid)
        :param out_fil:  Output T file name
        :param inv_flg:  0 - no invers, 1 - invers `GXFFT <geosoft.gxapi.GXFFT>` applied
        :type  img_tx:   GXIMG
        :type  img_ty:   GXIMG
        :type  out_fil:  str
        :type  inv_flg:  int

        .. versionadded:: 5.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapFFT2._td_xd_y(GXContext._get_tls_geo(), img_tx, img_ty, out_fil.encode(), inv_flg)
        



    @classmethod
    def trans_pg(cls, pg, opt):
        """
        Apply 2D `GXFFT <geosoft.gxapi.GXFFT>` transform to data in pager
        
        :param pg:   Pager obj
        :param opt:  :ref:`FFT2_PG`
        :type  pg:   GXPG
        :type  opt:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapFFT2._trans_pg(GXContext._get_tls_geo(), pg, opt)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer