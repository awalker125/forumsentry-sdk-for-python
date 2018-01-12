'''
Created on 8 Dec 2017

@author: walandre
'''
import unittest

import os
#import string
#import random
import json
import sys

from forumsentry.serialization import Serialization
from forumsentry_api.models.http_listener_policy import HttpListenerPolicy
from tests.forumsentry import helper

class TestSerialization(unittest.TestCase):

    def setUp(self):
        self._unique_id = helper.id_generator()
        self._serialization = Serialization()
        self._whereami = os.path.dirname(__file__)  
        
        #We will use HttpListenerPolicy as our test model
        self._model = HttpListenerPolicy()  # noqa: E501
        
        
        self._model.use_cookie_authentication = self._unique_id
        self._model.use_basic_authentication = self._unique_id
        self._model.acl_policy = self._unique_id
        self._model.ip_acl_policy = self._unique_id
        self._model.read_timeout_millis = self._unique_id
        self._model.password_parameter = self._unique_id
        self._model.use_digest_authentication = self._unique_id
        self._model.use_chunking = self._unique_id
        self._model.port = self._unique_id
        self._model.use_device_ip = self._unique_id
        self._model.name = self._unique_id
        self._model.description = self._unique_id
        self._model.use_form_post_authentication = self._unique_id
        self._model.listener_ssl_policy = self._unique_id
        self._model.username_parameter = self._unique_id
        self._model.enabled = self._unique_id
        self._model.interface = "WAN"
        self._model.error_template = self._unique_id
        self._model.listener_host = self._unique_id
        self._model.listener_ssl_enabled = self._unique_id
        self._model.password_authentication_realm = self._unique_id
        self._model.require_password_authentication = self._unique_id
        self._model.use_kerberos_authentication = self._unique_id


    def tearDown(self):
        pass

    def test_serializationConstructor(self):
        serialization = Serialization()
        self.assertTrue(isinstance(serialization,Serialization))

    def test_serializeHttpListenerPolicy(self):
        
        j = self._serialization.serialize(self._model)

        data = json.loads(j)
        #print j
        self.assertEqual(data['name'], self._unique_id)
        
    def test_deserializeHttpListenerPolicy(self):
        
        test_name = sys._getframe().f_code.co_name
        
        filename = '{0}/../mocks/{1}'.format(self._whereami,test_name)
        
        j = None
        #get a json string to desrialize into an object
        with open(filename, 'r') as f:
            j = f.read()
        
        obj = self._serialization.deserialize(j, HttpListenerPolicy)

        self.assertIsInstance(obj, HttpListenerPolicy)
        self.assertEqual(obj.name, "LPXHVV")        
        self.assertEqual(obj.port, 80)
        self.assertEqual(obj.read_timeout_millis, 600)   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()