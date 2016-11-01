#import pydevd
#pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import json
import geosoft.gxapi as gxapi
import geosoft.gxpy.om as gxom


###############################################################################################

def test_get_user_input():

    gxom.pause('Testing pause, no info')
    gxom.pause('Testing pause\nSome descriptive mumbo-gumbo.........')
    gxom.pause('Testing pause with cancel',cancel=True)

    ret = gxom.get_user_input('Testing string input','String is a bit long',default='test')
    print(ret)

    ret = gxom.get_user_input('Testing float', 'Float', kind='float', default=1.5)
    print(ret)

    ret = gxom.get_user_input('Testing int\nThis needs to be an integer value as nothing else is allowed.\nI hope you understand.\nSorry about that.\nI am Canadian after all.', 'Int', kind='int', default=7)
    print(ret)

    ret = gxom.get_user_input('Testing a list', 'List', kind='list', default='maki', items='maki, rider, explorer')
    print(ret)

    ret = gxom.get_user_input('Testing a file', 'Any file', kind='file', default='anyfile.dat')
    print(ret)

    ret = gxom.get_user_input('Testing a file', 'New file', kind='newfile', default='new.dat')
    print(ret)

    ret = gxom.get_user_input('Testing a file', 'Old file', kind='oldfile')
    print(ret)

    ret = gxom.get_user_input('Testing a file *.grd', 'Some file', kind='file', default='maki.dat', filemask="*.grd")
    print(ret)

    ret = gxom.get_user_input('Testing a multi-file/nSome extra info here, and long-winded too.', 'Multiple files:', kind='multifile', default='maki.dat')
    print (ret)

    ret = gxom.get_user_input('Testing a multi-file *.grd;*.hgd', 'Multiple grids:', kind='multifile', default='maki.dat', filemask="*.grd;*.hgd")
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
        input("User inputs test finished...")
        test_state()
        test_menus()
    except:
        input("There was a problem...")
        exit(1)
    input("Success...")
    exit(0)

