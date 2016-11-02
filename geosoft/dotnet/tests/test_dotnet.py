# import pydevd
# pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import json
import geosoft.gxapi as gxapi
import geosoft.dotnet as gdn

def test_dialog():
    dlg = gdn.Splitter()
    dlg.ShowDialog()


def test_dialog():
    dlg = gdn.Splitter()
    dlg.ShowDialog()

def rungx():
    test_dialog()
    input("Finished testing dotnet API - success...")