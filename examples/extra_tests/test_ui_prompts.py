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
        verification_checked = gxapi.int_ref()
        verification_checked.value = 1
        gxapi.GXSYS.display_task_dialog_ui('Message Title', 'Main Instruction', 'Content, with <a href="https://google.com">link</a>',
                                           gxapi.TD_BUTTON_OK, gxapi.GXLST.null(), gxapi.TD_ICON_ERROR,
                                           'Footer  with <a href="https://google.com">another link</a>', gxapi.TD_ICON_WARNING,
                                           'Verification checkbox text (uncheck this!)', verification_checked,
                                           'Expanded stuff...\n<a href="https://my.geosoft.com/subscriptions#/">My subscriptions</a>', '', '')
        self.assertEqual(verification_checked.value, 0)

    def test_confirm(self):
        self.start()
        verification_checked = gxapi.int_ref()
        answer = gxapi.GXSYS.display_task_dialog_ui('Message Title', '', 'Are you sure (click yes)?',
                                                    gxapi.TD_BUTTON_YES + gxapi.TD_BUTTON_NO, gxapi.GXLST.null(),
                                                    gxapi.TD_ICON_CONFIRMATION,
                                                    '', gxapi.TD_ICON_NONE,
                                                    '', verification_checked,
                                                    '', '', '')
        self.assertEqual(answer, gxapi.TD_ID_YES)

    def test_success(self):
        self.start()
        verification_checked = gxapi.int_ref()
        gxapi.GXSYS.display_task_dialog_ui('Message Title', '', 'Success!',
                                           gxapi.TD_BUTTON_CLOSE, gxapi.GXLST.null(), gxapi.TD_ICON_SUCCESS,
                                           '', gxapi.TD_ICON_NONE,
                                           '', verification_checked,
                                           '', '', '')

    def test_information(self):
        self.start()
        verification_checked = gxapi.int_ref()
        gxapi.GXSYS.display_task_dialog_ui('Message Title', '', 'Information',
                                           gxapi.TD_BUTTON_CLOSE, gxapi.GXLST.null(), gxapi.TD_ICON_INFORMATION,
                                           '', gxapi.TD_ICON_NONE,
                                           '', verification_checked,
                                           '', '', '')
    def test_none(self):
        self.start()
        verification_checked = gxapi.int_ref()
        gxapi.GXSYS.display_task_dialog_ui('Message Title', '', 'No Icon',
                                           gxapi.TD_BUTTON_CLOSE, gxapi.GXLST.null(), gxapi.TD_ICON_NONE,
                                           '', gxapi.TD_ICON_NONE,
                                           '', verification_checked,
                                           '', '', '')

    def test_custom_buttons(self):
        self.start()
        lst = gxapi.GXLST.create(1024);
        lst.add_item("Don't press this one", "50");
        lst.add_item("Press this one!", "123");
        verification_checked = gxapi.int_ref()
        answer = gxapi.GXSYS.display_task_dialog_ui('Message Title', '', 'Custom Buttons',
                                                    gxapi.TD_BUTTON_CLOSE, lst, gxapi.TD_ICON_CONFIRMATION,
                                                    '', gxapi.TD_ICON_NONE,
                                                    '', verification_checked,
                                                    '', '', '')
        self.assertEqual(answer, 123)

if __name__ == '__main__':
    unittest.main()
