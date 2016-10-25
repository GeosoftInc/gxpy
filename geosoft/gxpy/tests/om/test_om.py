#import pydevd
import geosoft.gxapi as gxapi
import geosoft.gxpy.om as gxom


def environment(self, formated_indent=-1):
    ''' :returns: Geosoft environment information as a dictionary'''

    def_menus = gxapi.GXLST.create(512)
    loaded_menus = gxapi.GXLST.create(512)
    user_menus = gxapi.GXLST.create(512)
    try:
        gxapi.GXSYS.get_loaded_menus(def_menus, loaded_menus, user_menus)
        def_menus = gxu.dictFromLst(def_menus),
        loaded_menus = gxu.dictFromLst(loaded_menus),
        user_menus = gxu.dictFromLst(user_menus),
    except:
        def_menus = loaded_menus = user_menus = ""

    info = {'gid': self.gid,
            'current_date': gxapi.GXSYS.date(),
            'current_utc_date': gxapi.GXSYS.utc_date(),
            'current_time': gxapi.GXSYS.time(),
            'current_utc_time': gxapi.GXSYS.utc_time(),
            'license_class': self.license_class(),
            'menu_default': def_menus,
            'menu_loaded': loaded_menus,
            'menu_user': user_menus,
            'folder_workspace': self.folder_workspace(),
            'folder_temp': self.folder_temp(),
            'folder_user': self.folder_user(),
            'id_window_main': self.main_wind_id(),
            'id_window_active': self.active_wind_id(),
            'id_thread': gxapi.GXSYS.get_thread_id(),
            }


###############################################################################################

def rungx():

    # pydevd modules supports remote debugging - see Debugging Python Extensions in the GX Developer documentation
    # pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

    gxom.pause('Testing pause')
    gxom.pause('Testing pause\nSome descriptive mumbo-gumbo.........')
    gxom.pause('Testing pause with cancel',cancel='Cancel')

    ret = gxom.get_user_input('Testing string input','String',default='test')
    if ret != 'test':
        gxom.pause('You should gave entered \'test\', but you entered \'{}\''.format(ret))
    ret = gxom.get_user_input('Testing float', 'Float', kind='float', default=1.5)
    if ret != 1.5:
        gxom.pause('You should gave entered \'1.5\', but you entered \'{}\''.format(ret))
    ret = gxom.get_user_input('Testing int', 'Int', kind='int', default=7)
    if ret != 7:
        gxom.pause('You should gave entered \'7\', but you entered \'{}\''.format(ret))
    ret = gxom.get_user_input('Testing a list', 'List', kind='list', default='maki', items='maki, rider, explorer')
    if ret != 'maki':
        gxom.pause('You should gave entered \'maki\', but you entered \'{}\''.format(ret))