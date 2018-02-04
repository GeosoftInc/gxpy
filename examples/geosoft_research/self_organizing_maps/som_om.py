# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:15:34 2014

@author: Ian
"""

#The following 2 lines to support remote debugging
#import pydevd
#pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import os

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.project as gxpj
import geosoft.gxpy.gdb as gxgdb

#t translation
def _(s): return s

def _same(f1, f2):
    f1 = os.path.normpath(f1)
    f2 = os.path.normpath(f2)
    if f1 == f2:
        return True
    try:
        return os.path.samefile(f1, f2)
    except FileNotFoundError:
        return False

def rungx():

    gxu.check_version('9.2')

    with gxpj.Geosoft_project() as pj:
        gdb_name = pj.current_database
        if not gdb_name:
            gxpj.message(_('No current database'), _('An open database is required.'))
        state = pj.current_db_state()

    # settings
    settings = gxu.get_parameters('SOM_OM')

    # if different database, reset database-dependent settings
    if not _same(gdb_name, settings.get('GDB_NAME', '')):
        settings['GDB_NAME'] = os.path.normpath(gdb_name)
        with gxgdb.Geosoft_gdb() as gdb:
            chans = state['disp_chan_list']
        channorm = {}
        for c in chans:
            channorm[c] = 0
        settings['INPUT_DATA'] = channorm
        settings.pop('FILTER', None)

    # analyse data
    gxapi.GXEDB.un_load(gdb_name)
    try:
        script = os.path.join(os.path.split(__file__)[0], 'som_om_qt5.py')
        results = gxu.run_external_python(script, '', '', settings)
    except:
        gxapi.GXEDB.load(gdb_name)
        raise

    # save results
    gxu.save_parameters('SOM_OM', results)

    gxapi.GXEDB.load(gdb_name)

