#import pydevd
#pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import json
import geosoft.gxpy.om as gxom


###############################################################################################

def test_get_user_input():

    gxom.user_message('TEST', 'Starting get_user_info test')
    gxom.pause('Testing pause\nSome descriptive text\nLine 2\nLine 3\nThis tests the ability for DGW to properly resize a a dialog..........')
    gxom.pause('Testing pause with cancel',cancel=True)

    ret = gxom.get_user_input('Testing string input','String is a bit long',default='test')
    print('string return: {}'.format(ret))

    ret = gxom.get_user_input('Testing float', 'Float', kind='float', default=1.5)
    print('float return: {}'.format(ret))

    ret = gxom.get_user_input('Testing int\nThis must be an integer value.', 'Int', kind='int', default=7)
    print('int return: {}'.format(ret))

    ret = gxom.get_user_input('Testing a list', 'List', kind='list', default='maki', items='maki, rider, explorer')
    print('list return: {}'.format(ret))

    input("Simple inputs test finished...")

def test_file():

    ret = gxom.get_user_input('Testing a file', 'Any file', kind='file', default='anyfile.dat')
    print('file return: {}'.format(ret))

    ret = gxom.get_user_input('Testing a file', 'New file', kind='newfile', default='new.dat')
    print('new file return: {}'.format(ret))

    ret = gxom.get_user_input('Testing a file', 'Old file', kind='oldfile')
    print('old file return: {}'.format(ret))

    ret = gxom.get_user_input('Testing a file *.grd,*.gdb', 'Some file', kind='file', default='maki.dat', filemask="*.grd,*.gdb")
    print('grid file return: {}'.format(ret))

    input("File inputs test finished...")

def test_multifile():

    ret = gxom.get_user_input('Testing a multi-file string default', 'Multiple files:', kind='file', default='maki.dat,mak2.dat;yamma.grd', filemask="**")
    print('multifile from string default return: {}'.format(ret))

    ret = gxom.get_user_input('Testing a multi-file list default', 'Multiple files:', kind='file', default=['maki.dat', 'list.', '4.5'], filemask="**")
    print('multifile from list default return: {}'.format(ret))

    ret = gxom.get_user_input('Testing a multi-file *.grd;', 'Multiple grids:', kind='file', filemask="**,*.grd")
    print('multifile grid return: {}'.format(ret))

    ret = gxom.get_user_input('Testing a multi-file *.map,*.gdb', 'Multiple grids:', kind='file', filemask=["**", "*.map", "*.gdb"])
    print('multifile grid return: {}'.format(ret))

    input("File inputs test finished...")

def test_state():
    state = gxom.state()
    print(json.dumps(state, indent=4))

def test_menus():
    env = gxom.menus()
    print(json.dumps(env, indent=4))

def test_scripting():
    import os
    import geosoft.gxapi as gxa

    # record script
    if os.path.exists("gxpy_om.gs"):
        os.remove("gxpy_om.gs")

    gxom.user_message('SCRIPTING TEST', 'Choose file name as gxpy_om.gs in the browse dialog for this test to succeed')
    gxa.GXSYS.do_command("[ID] ID_GX_RECORD")
    dir = os.path.split(__file__)[0]
    script_gx = os.path.join(dir, 'script_gx.py')
    gxa.GXSYS.do_command("[GX] {}".format(script_gx)) # We have to use do_command to record a GXs in script not run_gx
    gxa.GXSYS.do_command("[ID] ID_GX_ENDRECORD")

    with open("gxpy_om.gs", 'r') as f:
        script = f.read()

    # show script
    gxom.user_message('SCRIPTING TEST RESULT',
                      'The following should contain one SETINI of the value to SCRIPT_GX.VALUE\n\n{}'.format(script))

    # run script
    gxa.GXSYS.set_interactive(0)
    gxa.GXSYS.run_gx(script_gx)
    gxa.GXSYS.set_interactive(1)

def rungx():

    test_state()
    return

    test_scripting()
    test_get_user_input()
    test_file()
    test_multifile()
    test_menus()
    input("Finished testing om API - success...")

