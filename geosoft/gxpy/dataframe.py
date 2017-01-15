
import pandas as pd

import geosoft
import geosoft.gxapi as gxapi
from . import utility as gxu

__version__ = geosoft.__version__

def _t(s):
    return geosoft.gxpy.system.translate(s)

class DfException(Exception):
    '''
    Exceptions from this module.

    .. versionadded:: 9.2
    '''
    pass

def table_record(table, rec):
    """
    Return a dictionary of a record from a table
    :param table:   table name
    :param rec:     record wanted
    :return:        dictionary containing record values as strings
    """

    t = GXdf(table, records=rec)
    return t.to_dict(orient='records')[0]

def table_column(table, col):
    """
    Return a dictionary of a column from a table
    :param table:   table name
    :param col:     column wanted
    :return:        dictionary containing record values as strings
    """

    t = GXdf(table, columns=col).to_dict(orient='index')
    d = {}
    for rec in t.keys():
        d[rec] = t[rec][col]
    return d

class GXdf(pd.DataFrame):
    '''
    Pandas DataFrame from a Geosoft table.

    :parameters:
        :table:     geosoft table name, which is normally an ASCII csv file.  If the table cannot be
                    found in the project folder `user/csv` is searched, then the geosoft `csv` folder.
        :records:   Record name to include, or a list of records to include.  If not specified all
                    records are included.
        :columns:   Column name to be included, or a list of column names to include.  If not specified all
                    columns are included.

    :raises:
        :DfException:    if no columns.records found in the table.  If only some fields are found the dataframe is
                         created with the found fields.
        :raises geosoft.gxapi.GXError:  if a requested record is not found.

    .. versionadded:: 9.2
    '''

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __init__(self, initial=None, records=None, columns=None, **kwa):
        super().__init__(**kwa)

        if initial is not None:

            if type(initial) is str:

                lst = gxapi.GXLST.create(geosoft.gxpy.MAX_LST)
                sr = gxapi.str_ref()

                if records is None:
                    try:
                        ltb = gxapi.GXLTB.create(initial, 0, 1, '')
                    except geosoft.gxapi.GXError as e:
                        raise DfException(str(e))
                else:
                    if type(records) is str:
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
                        self[sr.value] = ()
                        col_indexes.append(i)

                if len(col_indexes) == 0:
                    raise DfException(_t('Table has no columns or \'{}\' column(s) not found.'.format(columns)))
                    
                if records is None:
                    ltb.get_lst(0, lst)
                    keys = list(gxu.dict_from_lst(lst, True))
                    vlst = list(self.columns)
                    for j in range(len(keys)):
                        nf = 0
                        for i in col_indexes:
                            ltb.get_string(j, i, sr)
                            vlst[nf] = sr.value
                            nf += 1
                        self.loc[keys[j]] = vlst

                else:  # selective read
                    vlst = list(self.columns)
                    for rec in records:
                        j = ltb.find_key(rec)
                        nf = 0
                        for i in col_indexes:
                            ltb.get_string(j, i, sr)
                            vlst[nf] = sr.value
                            nf += 1
                        self.loc[rec] = vlst

            else:
                raise DfException(_t('Only tables currently supported.'))