
import geosoft.gxpy.project as gxprj
import geosoft.gxapi as gxa

# This GX is used in a test, during script recording, and the script should only contain its parameters
# but not ones from user_input.gx
def rungx():
    float_val = gxa.GXSYS.get_double("SCRIPT_GX", "VALUE")
    if gxa.GXSYS.interactive() != 0:
        ret_val = gxprj.get_user_input('SCRIPT GX (interactive)', 'Float', kind='float', default=float_val)
        print('float return: {}'.format(ret_val))
        gxa.GXSYS.set_double("SCRIPT_GX", "VALUE", ret_val)
    else:
        gxa.GXSYS.set_interactive(1) # Restore interactive mod to make dialogs appear
        gxprj.user_message('SCRIPT GX (non interactive)', "Received value: {}".format(float_val))

