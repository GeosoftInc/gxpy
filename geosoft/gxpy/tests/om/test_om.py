#import pydevd
#pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import json
import geosoft.gxapi as gxapi
import geosoft.gxpy.om as gxom


###############################################################################################

def test_get_user_input():

    gxom.pause('Testing pause')
    gxom.pause('Testing pause\nSome descriptive mumbo-gumbo.........')
    gxom.pause('Testing pause with cancel',cancel='Cancel')

    ret = gxom.get_user_input('Testing string input','String is a bit long',default='test')
    print(ret)

    ret = gxom.get_user_input('Testing float', 'Float', kind='float', default=1.5)
    print(ret)

    ret = gxom.get_user_input('Testing int', 'Int', kind='int', default=7)
    print(ret)

    ret = gxom.get_user_input('Testing a list', 'List', kind='list', default='maki', items='maki, rider, explorer')
    print(ret)

    ret = gxom.get_user_input('Testing a file', 'Enter maki2.dat', kind='file', default='maki.dat')
    print(ret)

    ret = gxom.get_user_input('Testing a multi-file', 'Multiple files:', kind='file', default='maki.dat', filemask="**")
    print (ret)

    ret = gxom.get_user_input('Testing a multi-file', 'Multiple grids:', kind='file', default='maki.dat', filemask="**,*.grd")
    print (ret)

    pass

def test_state():

    state = gxom.state()
    print(json.dumps(state, indent=4))

def test_menus():
    env = gxom.menus()
    print(json.dumps(env, indent=4))

def rungx():

    try:
        test_get_user_input()
        test_state()
        test_menus()
    except:
        input("There was a problem...")
        exit(1)
    input("Success...")
    exit(0)

