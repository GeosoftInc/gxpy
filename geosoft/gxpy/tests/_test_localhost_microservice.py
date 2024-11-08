#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import unittest
import os
import numpy as np
from requests import get as http_get, post as http_post, exceptions as http_exceptions
import json

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.dap_client as gxdap
import geosoft.gxpy.geometry as gxgeo
import geosoft.gxpy.grid as gxgrd

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()

    @classmethod
    def tearDownClass(cls):
        cls.tearDownGXPYTest()

    def test_post(self):
        self.start()

        doit = {'doit': 'read a Flask tutorial', 'stuff': 'some stuff'}

        response = http_post('http://localhost:5000/dothis',
                            data=json.dumps(doit),
                            headers={'Content-Type': 'application/json', 'Accept': 'application/json'})

        if (response.ok):
            data = json.loads(response.content.decode('utf-8'))
            print(data)
        else:
            response.raise_for_status()

    def test_makiserver_get(self):
        self.start()

        message = {'doit': 'read a book'}

        pass

###############################################################################################

if __name__ == '__main__':

    gxc = gx.GXpy()
    print(gxc.gid)
    unittest.main()
