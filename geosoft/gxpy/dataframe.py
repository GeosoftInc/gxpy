"""
Table (records, fields) handling, inherits from Pandas (http://pandas.pydata.org/) base class.

:Classes:
    :`Data_frame`: dataframe that holds a table

.. seealso:: :class:`geosoft.gxapi.GXLTB`

.. note::

    Regression tests provide usage examples:     
    `dataframe tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_dataframe.py>`_
    
"""
import pandas as pd

import geosoft
import geosoft.gxapi as gxapi
from . import utility as gxu

__version__ = geosoft.__version__

def _t(s):
    return geosoft.gxpy.system.translate(s)

class DfException(geosoft.GXRuntimeError):
    """
    Exceptions from :mod:`geosoft.gxpy.dataframe`.

    .. versionadded:: 9.2
    """
    pass

def table_record(table, rec):
    """
    Return a dictionary of a single record from a table

    :param table:   table name
    :param rec:     record wanted
    :returns:       dictionary containing record values as strings

    .. versionadded:: 9.2
    """

    t = Data_frame(table, records=rec)
    return t.to_dict(orient='records')[0]

def table_column(table, col):
    """
    Return a dictionary of a column from a table

    :param table:   table name
    :param col:     column wanted
    :returns:       dictionary containing record values as strings

    .. versionadded:: 9.2
    """

    t = Data_frame(table, columns=col).to_dict(orient='index')
    d = {}
    for rec in t.keys():
        d[rec] = t[rec][col]
    return d

def Data_frame(initial=None, records=None, columns=None):
    """
    Pandas DataFrame from a Geosoft table.

    :parameters:
        :initial:   Geosoft table name, which is normally an ASCII csv file.  If the table cannot be
                    found in the project folder `user/csv` is searched, then the Geosoft `csv` folder.
        :records:   Record name to include, or a list of records to include.  If not specified all
                    records are included in the dataframe.
        :columns:   Column name to be included, or a list of column names to include.  If not specified all
                    columns are included in the dataframe.

    :raises:
        :DfException:    if no columns.records found in the table.  If only some fields are found the dataframe is
                         created with the found fields.
        :raises geosoft.gxapi.GXError:  if a requested record is not found.

    This returns a Pandas DataFrame instance, which can be accessed and used with standard Pandas
    calls.

    Column names from Geosoft table files are always uppercase, regardless
    of case used in the table file.

    Record/index names from Geosoft table files are case-sensitive.

    Example table file "rockcode.csv":

    .. code::

        / standard Geosoft rock codes
        CODE,LABEL,__DESCRIPTION,PATTERN,PAT_SIZE,PAT_DENSITY,PAT_THICKNESS,COLOR
        bau,BAU,BAUXITE,100,,,,RG49B181
        bif,BIF,"BANDED IRON FM",202,,,,R
        cal,CAL,CALCRETE,315,,,,B
        cbt,CBT,CARBONATITE,305,,,,R128G128B192

    .. code::

        include geosoft.gxpy as gxpy
        with gxpy.GXpy() as gx:
            df = gxpy.dataframe.Data_frame('rockcode')
            print(len(df))
            print(df.loc['bif', 'DESCRIPTION']) # "BANDED IRON FM"
            print(df.loc['bif'][1])             # "BANDED IRON FM"
            print(df.iloc[1,0])                 # "BIF"
            print(df.loc['cal', 'PATTERN'])     # "315"

    .. versionadded:: 9.2
    .. versionmodified:: 9.4
    """
    if not type(initial) is str:
        raise DfException(_t('Only Geosoft tables are supported.'))

    df = pd.DataFrame()

    if initial is None:
        return df

    lst = gxapi.GXLST.create(geosoft.gxpy.MAX_LST)
    sr = gxapi.str_ref()

    if records is None:
        try:
            ltb = gxapi.GXLTB.create(initial, 0, 1, '')
        except geosoft.gxapi.GXError as e:
            raise DfException(str(e))
    else:
        if type(records) is str:
            if not records:
                raise DfException(_t('Empty records string.'))
            try:
                ltb = gxapi.GXLTB.create(initial, 0, 1, records)
            except geosoft.gxapi.GXError as e:
                raise DfException(_t('Invalid table \'{}\' ({})').format(initial, str(e)))
            except geosoft.gxapi.GXAPIError as e:
                raise DfException(_t('Record \'{}\' not in \'{}\' ({})').format(records, initial, str(e)))
            records = None
        else:
            ltb = gxapi.GXLTB.create(initial, 0, 1, '')

    col_indexes = []
    for i in range(1, ltb.fields()):
        ltb.get_field(i, sr)
        if columns is None:
            incl = True
        elif type(columns) is str:
            incl = sr.value == columns
        else:
            incl = sr.value in columns
        if incl:
            df[sr.value] = ()
            col_indexes.append(i)

    if len(col_indexes) == 0:
        raise DfException(_t('Table has no columns or \'{}\' column(s) not found.'.format(columns)))

    if records is None:
        ltb.get_lst(0, lst)
        keys = list(gxu.dict_from_lst(lst, True))
        vlst = list(df.columns)
        for j in range(len(keys)):
            nf = 0
            for i in col_indexes:
                ltb.get_string(j, i, sr)
                vlst[nf] = sr.value
                nf += 1
            df.loc[keys[j]] = vlst

    else:  # selective read
        vlst = list(df.columns)
        for rec in records:
            j = ltb.find_key(rec)
            nf = 0
            for i in col_indexes:
                ltb.get_string(j, i, sr)
                vlst[nf] = sr.value
                nf += 1
            df.loc[rec] = vlst

    return df



