# import pydevd
# pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import os
import numpy as np
import unittest

import geosoft.gxapi as gxapi
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.view as gxv
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.group as gxg
import geosoft.gxpy.system as gxsys

from geosoft.gxpy.tests.base import GXPYTest


def rungx():
    raise Exception("This is not an extension.  Please use a python interpreter.")

class Test(GXPYTest):

    def test_full(self):
        self.start()
        """
        static display_task_dialog_ui((str)arg1, (str)arg2, (str)arg3, (int)arg4, (GXLST)arg5, (int)arg6, (str)arg7, (int)arg8, (str)arg9, (int_ref)arg10, (str)arg11, (str)arg12, (str)arg13) → int:
Show a Windows TaskDialog UI (see https://msdn.microsoft.com/en-us/library/windows/desktop/bb760441(v=vs.85).aspx).
Parameters:	
arg1 (str) – Title
arg2 (str) – Main instruction (empty string for none)
arg3 (str) – Content (empty string for none)
arg4 (int) – Common Buttons, one of TD_BUTTON
arg5 (geosoft.gxapi.GXLST) – Optional LST of custom buttons. Name in LST will be used for button text, while value should be an int to return. Pass (LST)0 to only use standard button flags.
arg6 (int) – Icon TD_ICON
arg7 (str) – Footer (empty string for none)
arg8 (int) – Footer Icon TD_ICON
arg9 (str) – Verification checkbox text (empty string for none)
arg10 (geosoft.gxapi.int_ref) – Verification checkbox checked (in/out)
arg11 (str) – Expanded information (empty string for none)
arg12 (str) – Collapsed control text for expanded information (empty string for default; ‘More’)
arg13 (str) – Expanded control text for expanded information (empty string for default; ‘Less’)
Returns:	
Button ID. One of TD_ID or the int value from LST of custom buttons.
Return type:	
int
New in version 9.3.0.
        """
        verification_checked = gxapi.int_ref()
        verification_checked.value = 1
        gxapi.GXSYS.display_task_dialog_ui('title', 'Main instruction', 'content <a href="https://google.com">Hyperlink</a>',
                                           gxapi.TD_BUTTON_OK, gxapi.GXLST.null(), gxapi.TD_ICON_ERROR,
                                           'Footer  <a href="https://google.com">Hyperlink</a>', gxapi.TD_ICON_WARNING,
                                           "Verification, uncheck this!", verification_checked,
                                           'Expanded stuff...\n <a href="https://my.geosoft.com/subscriptions#/">My subscriptions</a>', '', '')
        self.assertEqual(verification_checked.value, 0)

if __name__ == '__main__':
    unittest.main()
