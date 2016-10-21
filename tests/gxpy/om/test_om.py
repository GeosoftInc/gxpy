# import pydevd
import geosoft.gxpy.om as gxom


###############################################################################################

def rungx():

    # pydevd modules supports remote debugging - see Debugging Python Extensions in the GX Developer documentation
    # pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

    gxom.pause('Testing pause')
    gxom.pause('Testing pause\nSome descriptive mumbo-gumbo.........')
    gxom.pause('Testing pause with cancel',cancel='Cancel')

    ret = gxom.get_user_input('Testing string input','String',default='test')
    if ret != 'test':
        gxom.pause('You should gave entered \'test\', but you enetered {}'.format(ret))
    ret = gxom.get_user_input('Testing float', 'Float', kind='float', default=1.5)
    if ret != 1.5:
        gxom.pause('You should gave entered \'1.5\', but you enetered {}'.format(ret))
    ret = gxom.get_user_input('Testing int', 'Int', kind='int', default=7)
    if ret != 7:
        gxom.pause('You should gave entered \'7\', but you enetered {}'.format(ret))
    ret = gxom.get_user_input('Testing a list', 'List', kind='list', default='maki', items='maki, rider, explorer')
    if ret != 'maki':
        gxom.pause('You should gave entered \'maki\', but you enetered {}'.format(ret))