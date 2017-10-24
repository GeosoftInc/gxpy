### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSTR:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSTR(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXSTR':
        """
        A null (undefined) instance of :class:`GXSTR`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXSTR` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXSTR`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Data Input


    @classmethod
    def scan_i(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSTR.scan_i(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def scan_date(cls, p1: str, p2: int) -> float:
        ret_val = gxapi_cy.WrapSTR.scan_date(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val



    @classmethod
    def scan_form(cls, p1: str, p2: int) -> float:
        ret_val = gxapi_cy.WrapSTR.scan_form(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val



    @classmethod
    def scan_r(cls, p1: str) -> float:
        ret_val = gxapi_cy.WrapSTR.scan_r(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def scan_time(cls, p1: str, p2: int) -> float:
        ret_val = gxapi_cy.WrapSTR.scan_time(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val




# File Name


    @classmethod
    def file_combine_parts(cls, p1: str, p2: str, p3: str, p4: str, p5: str, p6: str_ref) -> None:
        p6.value = gxapi_cy.WrapSTR.file_combine_parts(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.value.encode())
        



    @classmethod
    def file_ext(cls, p1: str, p2: str, p3: str_ref, p4: int) -> None:
        p3.value = gxapi_cy.WrapSTR.file_ext(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode(), p4)
        



    @classmethod
    def file_name_part(cls, p1: str, p2: str_ref, p4: int) -> None:
        p2.value = gxapi_cy.WrapSTR.file_name_part(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4)
        



    @classmethod
    def get_m_file(cls, p1: str, p2: str_ref, p4: int) -> None:
        p2.value = gxapi_cy.WrapSTR.get_m_file(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4)
        



    @classmethod
    def remove_qualifiers(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSTR.remove_qualifiers(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        




# Formating


    @classmethod
    def format_crc(cls, p1: int, p2: str_ref, p4: int) -> None:
        p2.value = gxapi_cy.WrapSTR.format_crc(GXContext._get_tls_geo(), p1, p2.value.encode(), p4)
        



    @classmethod
    def format_date(cls, p1: float, p2: str_ref, p4: int, p5: int) -> None:
        p2.value = gxapi_cy.WrapSTR.format_date(GXContext._get_tls_geo(), p1, p2.value.encode(), p4, p5)
        



    @classmethod
    def format_i(cls, p1: int, p2: str_ref, p4: int) -> None:
        p2.value = gxapi_cy.WrapSTR.format_i(GXContext._get_tls_geo(), p1, p2.value.encode(), p4)
        



    @classmethod
    def format_r(cls, p1: float, p2: str_ref, p4: int, p5: int) -> None:
        p2.value = gxapi_cy.WrapSTR.format_r(GXContext._get_tls_geo(), p1, p2.value.encode(), p4, p5)
        



    @classmethod
    def format_r2(cls, p1: float, p2: str_ref, p4: int, p5: int) -> None:
        p2.value = gxapi_cy.WrapSTR.format_r2(GXContext._get_tls_geo(), p1, p2.value.encode(), p4, p5)
        



    @classmethod
    def format_double(cls, p1: float, p2: str_ref, p4: int, p5: int, p6: int) -> None:
        p2.value = gxapi_cy.WrapSTR.format_double(GXContext._get_tls_geo(), p1, p2.value.encode(), p4, p5, p6)
        



    @classmethod
    def format_time(cls, p1: float, p2: str_ref, p4: int, p5: int, p6: int) -> None:
        p2.value = gxapi_cy.WrapSTR.format_time(GXContext._get_tls_geo(), p1, p2.value.encode(), p4, p5, p6)
        




# General


    @classmethod
    def escape(cls, p1: str_ref, p3: int) -> None:
        p1.value = gxapi_cy.WrapSTR.escape(GXContext._get_tls_geo(), p1.value.encode(), p3)
        



    @classmethod
    def char_(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSTR.char_(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def char_n(cls, p1: str, p2: int, p3: int) -> int:
        ret_val = gxapi_cy.WrapSTR.char_n(GXContext._get_tls_geo(), p1.encode(), p2, p3)
        return ret_val



    @classmethod
    def justify(cls, p1: str, p2: str_ref, p3: int, p4: int) -> None:
        p2.value = gxapi_cy.WrapSTR.justify(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p3, p4)
        



    @classmethod
    def replacei_match_string(cls, p1: str_ref, p2: str, p3: str) -> None:
        p1.value = gxapi_cy.WrapSTR.replacei_match_string(GXContext._get_tls_geo(), p1.value.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def replace_match_string(cls, p1: str_ref, p2: str, p3: str) -> None:
        p1.value = gxapi_cy.WrapSTR.replace_match_string(GXContext._get_tls_geo(), p1.value.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def set_char_n(cls, p1: str_ref, p2: int, p4: int) -> None:
        p1.value = gxapi_cy.WrapSTR.set_char_n(GXContext._get_tls_geo(), p1.value.encode(), p2, p4)
        



    @classmethod
    def split_string(cls, p1: str_ref, p2: str, p3: str_ref) -> None:
        p1.value, p3.value = gxapi_cy.WrapSTR.split_string(GXContext._get_tls_geo(), p1.value.encode(), p2.encode(), p3.value.encode())
        



    @classmethod
    def strcat(cls, p1: str_ref, p2: str) -> None:
        p1.value = gxapi_cy.WrapSTR.strcat(GXContext._get_tls_geo(), p1.value.encode(), p2.encode())
        



    @classmethod
    def strcmp(cls, p1: str, p2: str, p3: int) -> int:
        ret_val = gxapi_cy.WrapSTR.strcmp(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return ret_val



    @classmethod
    def strcpy(cls, p1: str_ref, p2: str) -> None:
        p1.value = gxapi_cy.WrapSTR.strcpy(GXContext._get_tls_geo(), p1.value.encode(), p2.encode())
        



    @classmethod
    def stri_mask(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSTR.stri_mask(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def strins(cls, p1: str_ref, p2: int, p3: str) -> None:
        p1.value = gxapi_cy.WrapSTR.strins(GXContext._get_tls_geo(), p1.value.encode(), p2, p3.encode())
        



    @classmethod
    def strlen(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSTR.strlen(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def str_mask(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSTR.str_mask(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def str_min(cls, p1: str_ref) -> int:
        ret_val, p1.value = gxapi_cy.WrapSTR.str_min(GXContext._get_tls_geo(), p1.value.encode())
        return ret_val



    @classmethod
    def str_min2(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapSTR.str_min2(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def strncmp(cls, p1: str, p2: str, p3: int, p4: int) -> int:
        ret_val = gxapi_cy.WrapSTR.strncmp(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4)
        return ret_val



    @classmethod
    def str_str(cls, p1: str, p2: str, p3: int) -> int:
        ret_val = gxapi_cy.WrapSTR.str_str(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return ret_val



    @classmethod
    def substr(cls, p1: str_ref, p3: str, p4: int, p5: int) -> None:
        p1.value = gxapi_cy.WrapSTR.substr(GXContext._get_tls_geo(), p1.value.encode(), p3.encode(), p4, p5)
        



    @classmethod
    def to_lower(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapSTR.to_lower(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def to_upper(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapSTR.to_upper(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def xyz_line(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapSTR.xyz_line(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def make_alpha(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapSTR.make_alpha(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def printf(cls, p1: str_ref, p3: str) -> None:
        p1.value = gxapi_cy.WrapSTR.printf(GXContext._get_tls_geo(), p1.value.encode(), p3.encode())
        



    @classmethod
    def replace_char(cls, p1: str_ref, p2: str, p3: str) -> None:
        p1.value = gxapi_cy.WrapSTR.replace_char(GXContext._get_tls_geo(), p1.value.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def replace_char2(cls, p1: str_ref, p2: str, p3: str) -> None:
        p1.value = gxapi_cy.WrapSTR.replace_char2(GXContext._get_tls_geo(), p1.value.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def replace_multi_char(cls, p1: str_ref, p2: str, p3: str) -> None:
        p1.value = gxapi_cy.WrapSTR.replace_multi_char(GXContext._get_tls_geo(), p1.value.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def replace_non_ascii(cls, p1: str_ref, p2: str) -> None:
        p1.value = gxapi_cy.WrapSTR.replace_non_ascii(GXContext._get_tls_geo(), p1.value.encode(), p2.encode())
        



    @classmethod
    def set_char(cls, p1: str_ref, p2: int) -> None:
        p1.value = gxapi_cy.WrapSTR.set_char(GXContext._get_tls_geo(), p1.value.encode(), p2)
        



    @classmethod
    def trim_quotes(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapSTR.trim_quotes(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def trim_space(cls, p1: str_ref, p2: int) -> None:
        p1.value = gxapi_cy.WrapSTR.trim_space(GXContext._get_tls_geo(), p1.value.encode(), p2)
        



    @classmethod
    def un_quote(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapSTR.un_quote(GXContext._get_tls_geo(), p1.value.encode())
        




# Misc


    @classmethod
    def gen_group_name(cls, p1: str, p2: str, p3: str, p4: str_ref) -> None:
        p4.value = gxapi_cy.WrapSTR.gen_group_name(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.value.encode())
        




# Tokenizing


    @classmethod
    def count_tokens(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapSTR.count_tokens(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def get_token(cls, p1: str_ref, p3: str, p4: int) -> None:
        p1.value = gxapi_cy.WrapSTR.get_token(GXContext._get_tls_geo(), p1.value.encode(), p3.encode(), p4)
        



    @classmethod
    def tokenize(cls, p1: str_ref, p2: str, p3: str, p4: str, p5: str) -> int:
        ret_val, p1.value = gxapi_cy.WrapSTR.tokenize(GXContext._get_tls_geo(), p1.value.encode(), p2.encode(), p3.encode(), p4.encode(), p5.encode())
        return ret_val



    @classmethod
    def tokens(cls, p1: str_ref, p2: str) -> int:
        ret_val, p1.value = gxapi_cy.WrapSTR.tokens(GXContext._get_tls_geo(), p1.value.encode(), p2.encode())
        return ret_val



    @classmethod
    def tokens2(cls, p1: str_ref, p2: str, p3: str, p4: str, p5: str) -> int:
        ret_val, p1.value = gxapi_cy.WrapSTR.tokens2(GXContext._get_tls_geo(), p1.value.encode(), p2.encode(), p3.encode(), p4.encode(), p5.encode())
        return ret_val



    @classmethod
    def parse_list(cls, p1: str, p2: 'GXVV') -> None:
        gxapi_cy.WrapSTR.parse_list(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer