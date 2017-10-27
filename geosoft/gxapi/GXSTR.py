### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSTR:
    """
    GXSTR class.

    This library is not a class. Use the `GXSTR` library functions
    to work with and manipulate string variables. Since the
    GX Programming Language does not provide string literal
    tokens, you must use these functions for any string operations
    you want to perform.
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
    def null(cls):
        """
        A null (undefined) instance of `GXSTR`
        
        :returns: A null `GXSTR`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXSTR` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXSTR`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Data Input


    @classmethod
    def scan_i(cls, str_val):
        """
        Convert a string to a GX int.
        """
        ret_val = gxapi_cy.WrapSTR.scan_i(GXContext._get_tls_geo(), str_val.encode())
        return ret_val



    @classmethod
    def scan_date(cls, str_val, type):
        """
        Convert a date string to a GX real.

        **Note:**

        OLD usage, use ScanForm_STR instead.
        """
        ret_val = gxapi_cy.WrapSTR.scan_date(GXContext._get_tls_geo(), str_val.encode(), type)
        return ret_val



    @classmethod
    def scan_form(cls, str_val, type):
        """
        Convert a formated string to a real.
        """
        ret_val = gxapi_cy.WrapSTR.scan_form(GXContext._get_tls_geo(), str_val.encode(), type)
        return ret_val



    @classmethod
    def scan_r(cls, str_val):
        """
        Convert a string to a GX real.
        """
        ret_val = gxapi_cy.WrapSTR.scan_r(GXContext._get_tls_geo(), str_val.encode())
        return ret_val



    @classmethod
    def scan_time(cls, str_val, type):
        """
        Convert a time string to a GX real.

        **Note:**

        OLD usage, use ScanForm_STR instead.
        """
        ret_val = gxapi_cy.WrapSTR.scan_time(GXContext._get_tls_geo(), str_val.encode(), type)
        return ret_val




# File Name


    @classmethod
    def file_combine_parts(cls, drive, dir, file, ext, qual, file_name):
        """
        Combine file parts to build a file name.
        """
        file_name.value = gxapi_cy.WrapSTR.file_combine_parts(GXContext._get_tls_geo(), drive.encode(), dir.encode(), file.encode(), ext.encode(), qual.encode(), file_name.value.encode())
        



    @classmethod
    def file_ext(cls, ifile, ext, ofile, opt):
        """
        Add a file extension onto a file name string.
        """
        ofile.value = gxapi_cy.WrapSTR.file_ext(GXContext._get_tls_geo(), ifile.encode(), ext.encode(), ofile.value.encode(), opt)
        



    @classmethod
    def file_name_part(cls, file, file_part, part):
        """
        Get part of a file name.
        """
        file_part.value = gxapi_cy.WrapSTR.file_name_part(GXContext._get_tls_geo(), file.encode(), file_part.value.encode(), part)
        



    @classmethod
    def get_m_file(cls, in_str, out_str, index):
        """
        Get the indexed filepath from a multiple filepath string

        **Note:**

        The multifile string must use '|' as a delimiter.
        Do not pass a string after calling `tokenize`.
        """
        out_str.value = gxapi_cy.WrapSTR.get_m_file(GXContext._get_tls_geo(), in_str.encode(), out_str.value.encode(), index)
        



    @classmethod
    def remove_qualifiers(cls, ifile, ofile):
        """
        Remove file qualifiers from a file name
        """
        ofile.value = gxapi_cy.WrapSTR.remove_qualifiers(GXContext._get_tls_geo(), ifile.encode(), ofile.value.encode())
        




# Formating


    @classmethod
    def format_crc(cls, pul_crc, buff, width):
        """
        Convert a GX CRC value to a string.
        """
        buff.value = gxapi_cy.WrapSTR.format_crc(GXContext._get_tls_geo(), pul_crc, buff.value.encode(), width)
        



    @classmethod
    def format_date(cls, real, buff, width, type):
        """
        Convert a GX real to a date string.
        """
        buff.value = gxapi_cy.WrapSTR.format_date(GXContext._get_tls_geo(), real, buff.value.encode(), width, type)
        



    @classmethod
    def format_i(cls, int, buff, width):
        """
        Convert a GX int to a string.
        """
        buff.value = gxapi_cy.WrapSTR.format_i(GXContext._get_tls_geo(), int, buff.value.encode(), width)
        



    @classmethod
    def format_r(cls, real, buff, width, sig):
        """
        Convert a GX real to a string with significant digits.
        """
        buff.value = gxapi_cy.WrapSTR.format_r(GXContext._get_tls_geo(), real, buff.value.encode(), width, sig)
        



    @classmethod
    def format_r2(cls, real, buff, width, sig):
        """
        Convert a GX real to a string with given decimals.
        """
        buff.value = gxapi_cy.WrapSTR.format_r2(GXContext._get_tls_geo(), real, buff.value.encode(), width, sig)
        



    @classmethod
    def format_double(cls, real, buff, type, width, dec):
        """
        Convert a GX real to a string.
        """
        buff.value = gxapi_cy.WrapSTR.format_double(GXContext._get_tls_geo(), real, buff.value.encode(), type, width, dec)
        



    @classmethod
    def format_time(cls, real, buff, width, deci, type):
        """
        Convert a GX real to a time string.
        """
        buff.value = gxapi_cy.WrapSTR.format_time(GXContext._get_tls_geo(), real, buff.value.encode(), width, deci, type)
        




# General


    @classmethod
    def escape(cls, str_val, opt):
        """
        Convert/replace escape sequences in strings.

        **Note:**

        Escape characters:
        
        \\a      bell
        \\b      backspace
        \\f      formfeed
        \\n      new line
        \\r      carriage return
        \\t      tab
        \\v      vertical tab
        \\"      quote character
        \\x      take 'x' literally
        \\      backslash
        \\ooo    octal up to 3 characters
        \\xhh    hex up to 2 characters
        
        A common use of this function is to convert double-quote characters in
        a user unput string to \\" so the string can be placed in a tokenized
        string.
        """
        str_val.value = gxapi_cy.WrapSTR.escape(GXContext._get_tls_geo(), str_val.value.encode(), opt)
        



    @classmethod
    def char_(cls, str_val):
        """
        Returns the ASCII value of a character.
        """
        ret_val = gxapi_cy.WrapSTR.char_(GXContext._get_tls_geo(), str_val.encode())
        return ret_val



    @classmethod
    def char_n(cls, str_val, c, max):
        """
        Returns the ASCII value of the n'th character.
        """
        ret_val = gxapi_cy.WrapSTR.char_n(GXContext._get_tls_geo(), str_val.encode(), c, max)
        return ret_val



    @classmethod
    def justify(cls, in_str, out_str, width, just):
        """
        Justify a string

        **Note:**

        If the string is too big to fit in the number of display characters,
        the output string will be "**" justified as specified.
        """
        out_str.value = gxapi_cy.WrapSTR.justify(GXContext._get_tls_geo(), in_str.encode(), out_str.value.encode(), width, just)
        



    @classmethod
    def replacei_match_string(cls, istr, old, new):
        """
        Replaces all occurances of match string by replacement string with case insensitive.

        **Note:**

        If the replacement string is "" (NULL character)
        then the string to replace is removed from the
        input string, and the string is shortened.
        """
        istr.value = gxapi_cy.WrapSTR.replacei_match_string(GXContext._get_tls_geo(), istr.value.encode(), old.encode(), new.encode())
        



    @classmethod
    def replace_match_string(cls, istr, old, new):
        """
        Replaces all occurances of match string by replacement string with case sensitive.

        **Note:**

        If the replacement string is "" (NULL character)
        then the string to replace is removed from the
        input string, and the string is shortened.
        """
        istr.value = gxapi_cy.WrapSTR.replace_match_string(GXContext._get_tls_geo(), istr.value.encode(), old.encode(), new.encode())
        



    @classmethod
    def set_char_n(cls, str_val, c, ascii):
        """
        Set the n'th character of a string using an ASCII value
        """
        str_val.value = gxapi_cy.WrapSTR.set_char_n(GXContext._get_tls_geo(), str_val.value.encode(), c, ascii)
        



    @classmethod
    def split_string(cls, origstr, ch, split):
        """
        Splits a string in two on a character.

        **Note:**

        The original string is modified by terminating it
        at the character split.
        
        The part of the string past the character split is
        copied to the split string.
        
        Split characters in quoted strings are ignored.
        
        This function is mainly intended to separate comments
        from control file strings.
        """
        origstr.value, split.value = gxapi_cy.WrapSTR.split_string(GXContext._get_tls_geo(), origstr.value.encode(), ch.encode(), split.value.encode())
        



    @classmethod
    def strcat(cls, dest, orig):
        """
        This method contatinates a string.
        """
        dest.value = gxapi_cy.WrapSTR.strcat(GXContext._get_tls_geo(), dest.value.encode(), orig.encode())
        



    @classmethod
    def strcmp(cls, first, second, mode):
        """
        This method compares two strings and returns these values
        """
        ret_val = gxapi_cy.WrapSTR.strcmp(GXContext._get_tls_geo(), first.encode(), second.encode(), mode)
        return ret_val



    @classmethod
    def strcpy(cls, dest, orig):
        """
        This method copies a string into another string.
        """
        dest.value = gxapi_cy.WrapSTR.strcpy(GXContext._get_tls_geo(), dest.value.encode(), orig.encode())
        



    @classmethod
    def stri_mask(cls, mask, test):
        """
        Case insensitive comparison of two strings.

        **Note:**

        Mask characters '*' - matches any one or more up to
        next character
        '?' - matches one character
        
        Test is case insensitive
        """
        ret_val = gxapi_cy.WrapSTR.stri_mask(GXContext._get_tls_geo(), mask.encode(), test.encode())
        return ret_val



    @classmethod
    def strins(cls, dest, ins, orig):
        """
        This method inserts a string at a specified position.

        **Note:**

        If the specified position does not fall within the current string
        the source string will simply be Concatenated.
        """
        dest.value = gxapi_cy.WrapSTR.strins(GXContext._get_tls_geo(), dest.value.encode(), ins, orig.encode())
        



    @classmethod
    def strlen(cls, str_val):
        """
        Returns the length of a string.
        """
        ret_val = gxapi_cy.WrapSTR.strlen(GXContext._get_tls_geo(), str_val.encode())
        return ret_val



    @classmethod
    def str_mask(cls, mask, test):
        """
        Case sensitive comparison of two strings.

        **Note:**

        Mask characters '*' - matches any one or more up to
        next character
        '?' - matches one character
        
        Test is case sensitive
        """
        ret_val = gxapi_cy.WrapSTR.str_mask(GXContext._get_tls_geo(), mask.encode(), test.encode())
        return ret_val



    @classmethod
    def str_min(cls, str_val):
        """
        Remove spaces and tabs and return length

        **Note:**

        String may be modified. This function should not be
        used to determine if a file name string is defined, because
        a valid file name can contain spaces, and once "tested" the
        name will be altered. Instead, use `str_min2`, or use
        `GXSYS.file_exist` to see if the file actually exists.
        """
        ret_val, str_val.value = gxapi_cy.WrapSTR.str_min(GXContext._get_tls_geo(), str_val.value.encode())
        return ret_val



    @classmethod
    def str_min2(cls, str_val):
        """
        Length less spaces and tabs, string unchanged.
        """
        ret_val = gxapi_cy.WrapSTR.str_min2(GXContext._get_tls_geo(), str_val.encode())
        return ret_val



    @classmethod
    def strncmp(cls, first, second, n_char, mode):
        """
        Compares two strings to a given number of characters.
        """
        ret_val = gxapi_cy.WrapSTR.strncmp(GXContext._get_tls_geo(), first.encode(), second.encode(), n_char, mode)
        return ret_val



    @classmethod
    def str_str(cls, str_val, sub, mode):
        """
        Scan a string for the occurrence of a given substring.
        """
        ret_val = gxapi_cy.WrapSTR.str_str(GXContext._get_tls_geo(), str_val.encode(), sub.encode(), mode)
        return ret_val



    @classmethod
    def substr(cls, dest, orig, start, length):
        """
        Extract part of a string.

        **Note:**

        The destination string length will be less than the
        requested length if the substring is not fully enclosed
        in the origin string.
        """
        dest.value = gxapi_cy.WrapSTR.substr(GXContext._get_tls_geo(), dest.value.encode(), orig.encode(), start, length)
        



    @classmethod
    def to_lower(cls, str_val):
        """
        Convert a string to lower case.
        """
        str_val.value = gxapi_cy.WrapSTR.to_lower(GXContext._get_tls_geo(), str_val.value.encode())
        



    @classmethod
    def to_upper(cls, str_val):
        """
        Convert a string to upper case.
        """
        str_val.value = gxapi_cy.WrapSTR.to_upper(GXContext._get_tls_geo(), str_val.value.encode())
        



    @classmethod
    def xyz_line(cls, line, xyz):
        """
        Make a valid XYZ line name from a valid `GXDB` line name.
        """
        xyz.value = gxapi_cy.WrapSTR.xyz_line(GXContext._get_tls_geo(), line.encode(), xyz.value.encode())
        



    @classmethod
    def make_alpha(cls, str_val):
        """
        Turns all non alpha-numeric characters into an _.

        **Note:**

        THE STRING IS MODIFIED.
        """
        str_val.value = gxapi_cy.WrapSTR.make_alpha(GXContext._get_tls_geo(), str_val.value.encode())
        



    @classmethod
    def printf(cls, dest, mask):
        """
        Variable Argument PrintF function
        """
        dest.value = gxapi_cy.WrapSTR.printf(GXContext._get_tls_geo(), dest.value.encode(), mask.encode())
        



    @classmethod
    def replace_char(cls, istr, old, new):
        """
        Replaces characters in a string.

        **Note:**

        If the input replacement character is "", then the
        string will be truncated at the first character to replace.
        """
        istr.value = gxapi_cy.WrapSTR.replace_char(GXContext._get_tls_geo(), istr.value.encode(), old.encode(), new.encode())
        



    @classmethod
    def replace_char2(cls, istr, old, new):
        """
        Replaces characters in a string, supports simple removal.

        **Note:**

        If the replacement character is "" (NULL character)
        then the character to replace is removed from the
        input string, and the string is shortened.
        """
        istr.value = gxapi_cy.WrapSTR.replace_char2(GXContext._get_tls_geo(), istr.value.encode(), old.encode(), new.encode())
        



    @classmethod
    def replace_multi_char(cls, istr, old, new):
        """
        Replaces multiple characters in a string.

        **Note:**

        The number of characters to replace must equal
        the number of replacement characters.
        """
        istr.value = gxapi_cy.WrapSTR.replace_multi_char(GXContext._get_tls_geo(), istr.value.encode(), old.encode(), new.encode())
        



    @classmethod
    def replace_non_ascii(cls, str_val, rpl):
        """
        Replace non-ASCII characters in a string.

        **Note:**

        All characthers > 127 will be replaced by the first character
        of the replacement string.
        """
        str_val.value = gxapi_cy.WrapSTR.replace_non_ascii(GXContext._get_tls_geo(), str_val.value.encode(), rpl.encode())
        



    @classmethod
    def set_char(cls, str_val, ascii):
        """
        Set a string's first character using an ASCII value of a character.
        """
        str_val.value = gxapi_cy.WrapSTR.set_char(GXContext._get_tls_geo(), str_val.value.encode(), ascii)
        



    @classmethod
    def trim_quotes(cls, str_val):
        """
        Remove double quotes.

        **Note:**

        THE STRING IS MODIFIED.
        This method goes through the string and removes all spaces in a
        string except those enclosed in quotes. It then removes
        any quotes. It is usfull for trimming unwanted spaces from
        an input string but allows the user to use quotes as well.
        If a quote follows a backslash, the quote is retained and
        the backslash is deleted. These quotes are NOT treated as
        delimiters.
        """
        str_val.value = gxapi_cy.WrapSTR.trim_quotes(GXContext._get_tls_geo(), str_val.value.encode())
        



    @classmethod
    def trim_space(cls, str_val, trim):
        """
        Remove leading and/or trailing whitespace.

        **Note:**

        THE STRING IS MODIFIED.
        Whitespace characters are defined as space, tab, carriage return,
        new line, vertical tab or formfeed (0x09 to 0x0D, 0x20)
        """
        str_val.value = gxapi_cy.WrapSTR.trim_space(GXContext._get_tls_geo(), str_val.value.encode(), trim)
        



    @classmethod
    def un_quote(cls, str_val):
        """
        Remove double quotes from string

        **Note:**

        THE STRING IS MODIFIED.
        The pointers will be advanced past a first character
        quote and a last character quote will be set to .\\0'.
        Both first and last characters must be quotes for the
        triming to take place.
        """
        str_val.value = gxapi_cy.WrapSTR.un_quote(GXContext._get_tls_geo(), str_val.value.encode())
        




# Misc


    @classmethod
    def gen_group_name(cls, istr1, istr2, istr3, ostr):
        """
        Generate a group name string
        from type string, database and channel(optional) strings..

        **Note:**

        The output group name string is formed in the way of typestr_dbstr_chstr.
        If the database/channel strings is too long to fit the output string
        (max total length of 1040, including the NULL ending), then
        the typestr will always be kept the full length to be the first part,
        while the dbstr and/or chstr will be shortened to be the
        second and/or third part of the output string.

        .. seealso::

            GenNewGroupName_MVIEW
        """
        ostr.value = gxapi_cy.WrapSTR.gen_group_name(GXContext._get_tls_geo(), istr1.encode(), istr2.encode(), istr3.encode(), ostr.value.encode())
        




# Tokenizing


    @classmethod
    def count_tokens(cls, str_val, delims):
        """
        Counts number of tokens.

        **Note:**

        Delimiters are "soft" in that one or more delimiters
        is considered a single delimiter, and preceding and
        trailing delimiters are ignored.
        
        DO NOT use this function except in GXC code. The corresponding
        `get_token` function will not operate correctly in GX.Net code.
        """
        ret_val = gxapi_cy.WrapSTR.count_tokens(GXContext._get_tls_geo(), str_val.encode(), delims.encode())
        return ret_val



    @classmethod
    def get_token(cls, dest, orig, tok):
        """
        Get a token from a tokenized string.

        **Note:**

        Call `tokens`  to prepare the tokenized
        string.
        You MUST NOT get tokens beyond number of tokens returned
        by `tokens` or `tokens2`.
        The first token has index 0.
        
        DO NOT use this function except in GXC code.
        `get_token` function will not operate correctly in GX.Net code.

        .. seealso::

            `tokens`, GetToken_STR
        """
        dest.value = gxapi_cy.WrapSTR.get_token(GXContext._get_tls_geo(), dest.value.encode(), orig.encode(), tok)
        



    @classmethod
    def tokenize(cls, str_val, soft, hard, esc, quote):
        """
        Tokenize a string based on any characters.

        **Note:**

        This uses a finite state machine to tokenize on these
        rules:
        
        1. Any one character following an escape delimiter is
        treated as a normal character.
        
        2. Any characters inside a quote string are treated as
        normal characters.
        
        3. Any number of Soft delimiters in sequence without a
        hard delimiter are treated as one hard delimited.
        
        4. Any number of soft delimiters can preceed or follow
        a hard delimiter and are ignored.
        
        
        EXAMPLE
        
        Soft = [ ]   Hard = [,]   Escape = [\\]    Quote = ["]
        
        [this is a , , the "test," of   ,  \\,\\" my delimite  fi,]
        
        Results in:
        
        [this] [is] [a] [] [the] ["test,"] [of] [\\,\\"] [my] [delimite] [fi] []
        
        
        NOT use this function except in GXC code. The corresponding
        etToken_STR function will not operate correctly in GX.Net code.

        .. seealso::

            GetToken_STR
        """
        ret_val, str_val.value = gxapi_cy.WrapSTR.tokenize(GXContext._get_tls_geo(), str_val.value.encode(), soft.encode(), hard.encode(), esc.encode(), quote.encode())
        return ret_val



    @classmethod
    def tokens(cls, str_val, delims):
        """
        Tokenize a string

        **Note:**

        Delimiters in the string are reduced to a single NULL.
        Delimiters withing double quoted strings are ignored.
        Use GetToken_STR to extract tokens.
        
        DO NOT use this function except in GXC code. The corresponding
        `get_token` function will not operate correctly in GX.Net code.

        .. seealso::

            `tokens2`, GetToken_STR
        """
        ret_val, str_val.value = gxapi_cy.WrapSTR.tokens(GXContext._get_tls_geo(), str_val.value.encode(), delims.encode())
        return ret_val



    @classmethod
    def tokens2(cls, str_val, soft, hard, esc, quote):
        """
        General tokenize a string

        **Note:**

        This function is for old GX compatibility only.
        See `tokenize`.
        
        DO NOT use this function except in GXC code. The corresponding
        `get_token` function will not operate correctly in GX.Net code.
        """
        ret_val, str_val.value = gxapi_cy.WrapSTR.tokens2(GXContext._get_tls_geo(), str_val.value.encode(), soft.encode(), hard.encode(), esc.encode(), quote.encode())
        return ret_val



    @classmethod
    def parse_list(cls, str_val, gvv):
        """
        Parse a tokenized list to get a selection list.

        **Note:**

        Given a list such as "1,3,4,6-9,12", it fills the
        input buffer with 1 if the number is selected,
        0 if not. The items are delimited with spaces
        or commas, and ranges are acceptable, either using
        a "-" or ":", e.g.  3-6 and 3:6 both mean 3,4,5, and 6.
        Only values from 0 to one less than the buffer length
        are used.  Out-of-range values are ignored.
        """
        gxapi_cy.WrapSTR.parse_list(GXContext._get_tls_geo(), str_val.encode(), gvv._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer