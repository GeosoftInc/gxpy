#import pydevd
#pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import json
import geosoft.gxpy.project as gxprj


###############################################################################################

def test_get_user_input():

    gxprj.user_message('TEST', 'Starting get_user_info test')
    gxprj.pause('Testing pause\nSome descriptive text\nLine 2\nLine 3\nThis tests the ability for DGW to properly resize a a dialog..........')
    gxprj.pause('Testing pause with cancel',cancel=True)

    ret = gxprj.get_user_input('Testing string input','String is a bit long',default='test')
    print('string return: {}'.format(ret))

    ret = gxprj.get_user_input('Testing float', 'Float', kind='float', default=1.5)
    print('float return: {}'.format(ret))

    ret = gxprj.get_user_input('Testing int\nThis must be an integer value.', 'Int', kind='int', default=7)
    print('int return: {}'.format(ret))

    ret = gxprj.get_user_input('Testing a list', 'List', kind='list', default='maki', items='maki, rider, explorer')
    print('list return: {}'.format(ret))

    input("Simple inputs test finished, press enter to continue...")

def test_file():

    ret = gxprj.get_user_input('Testing a file', 'Any file', kind='file', default='anyfile.dat')
    print('file return: {}'.format(ret))

    ret = gxprj.get_user_input('Testing a file', 'New file', kind='newfile', default='new.dat')
    print('new file return: {}'.format(ret))

    ret = gxprj.get_user_input('Testing a file', 'Old file', kind='oldfile')
    print('old file return: {}'.format(ret))

    ret = gxprj.get_user_input('Testing a file *.grd,*.gdb', 'Some file', kind='file', default='maki.dat', filemask="*.grd,*.gdb")
    print('grid file return: {}'.format(ret))

    input("File inputs test finished, press enter to continue...")

def test_multifile():

    ret = gxprj.get_user_input('Testing a multi-file string default', 'Multiple files:', kind='file', default='maki.dat,mak2.dat;yamma.grd', filemask="**")
    print('multifile from string default return: {}'.format(ret))

    ret = gxprj.get_user_input('Testing a multi-file list default', 'Multiple files:', kind='file', default=['maki.dat', 'list.', '4.5'], filemask="**")
    print('multifile from list default return: {}'.format(ret))

    ret = gxprj.get_user_input('Testing a multi-file *.grd;', 'Multiple grids:', kind='file', filemask=["**,*.grd"])
    print('multifile grid return: {}'.format(ret))

    ret = gxprj.get_user_input('Testing a multi-file *.map,*.gdb', 'Multiple maps/gdb:', kind='file', filemask=["**", "*.map", "*.gdb"])
    print('multifile map/gdb return: {}'.format(ret))

    input("File inputs test finished, press enter to continue...")

def test_scripting():
    import os
    import geosoft.gxapi as gxa

    py_file = 'py_file.py'
    gs_file = 'project.gs'
    
    with open(py_file, 'w+') as f:
        f.write('import geosoft\n')
        f.write('def rungx():\n')
        f.write('   pass\n')

    gxprj.user_message('SCRIPTING TEST', 'Enter "project" in the next browse dialog.')
    gxa.GXSYS.do_command("[ID] ID_GX_RECORD")
    gxa.GXSYS.do_command("[GX] {}".format(py_file))
    gxa.GXSYS.do_command("[ID] ID_GX_ENDRECORD")

    with open(gs_file, 'r') as f:
        script = f.read()
    gxprj.user_message('SCRIPTING TEST RESULT',
                      'The following should contain "GX py_file.py"\n{}'.format(script))

    # run script
    gxa.GXSYS.set_interactive(0)
    gxa.GXSYS.run_gs(os.path.normpath(gs_file))
    gxa.GXSYS.set_interactive(1)

    os.remove(gs_file)
    os.remove(py_file)

def test_project():
    project  = gxprj.Geosoft_project()
    # open project in debugger and verify content of properties.
    pass

def rungx():

    gxprj.user_message('Running:', __file__)

    test_project()
    test_get_user_input()
    test_file()
    test_multifile()
    test_scripting()

    gxprj.user_message('Project test', "test finished")
