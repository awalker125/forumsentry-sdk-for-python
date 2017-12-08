# coding: utf-8

"""
    forumsentry_api
    
"""


from __future__ import absolute_import

import unittest
import string
import random

import forumsentry_api
from forumsentry_api.models.http_remote_policy import HttpRemotePolicy  # noqa: E501
#from forumsentry_api.rest import ApiException


class TestHttpRemotePolicy(unittest.TestCase):
    """HttpRemotePolicy unit test stubs"""

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def setUp(self):
        # FIXME: update assignements for none string types e.g boolean and int
        self._unique_id = self.id_generator()
        self._model = HttpRemotePolicy()  # noqa: E501
        
        
        self._model.use_basic_auth = self._unique_id
        self._model.proxy_policy = self._unique_id
        self._model.ssl_initiation_policy = self._unique_id
        self._model.tcp_connection_timeout = self._unique_id
        self._model.http_authentication_user_policy = self._unique_id
        self._model.use_chunking = self._unique_id
        self._model.tcp_read_timeout = self._unique_id
        self._model.name = self._unique_id
        self._model.enable_ssl = self._unique_id
        self._model.remote_authentication = "NONE"
        self._model.remote_port = self._unique_id
        self._model.enabled = self._unique_id
        self._model.remote_server = self._unique_id
        self._model.process_response = self._unique_id

    def tearDown(self):
        pass

    def testHttpRemotePolicy(self):
        """Test HttpRemotePolicy"""
        
        model = HttpRemotePolicy()  # noqa: E501
        self.assertTrue(isinstance(model, HttpRemotePolicy))
        
    def testHttpRemotePolicy_properties(self):
        """Test HttpRemotePolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        new_unique_id = self.id_generator()
        
        
        self._model.use_basic_auth = new_unique_id
        self.assertEqual(self._model.use_basic_auth,new_unique_id)
        self.assertNotEqual(self._model.use_basic_auth,self._unique_id)
         
        self._model.proxy_policy = new_unique_id
        self.assertEqual(self._model.proxy_policy,new_unique_id)
        self.assertNotEqual(self._model.proxy_policy,self._unique_id)
         
        self._model.ssl_initiation_policy = new_unique_id
        self.assertEqual(self._model.ssl_initiation_policy,new_unique_id)
        self.assertNotEqual(self._model.ssl_initiation_policy,self._unique_id)
         
        self._model.tcp_connection_timeout = new_unique_id
        self.assertEqual(self._model.tcp_connection_timeout,new_unique_id)
        self.assertNotEqual(self._model.tcp_connection_timeout,self._unique_id)
         
        self._model.http_authentication_user_policy = new_unique_id
        self.assertEqual(self._model.http_authentication_user_policy,new_unique_id)
        self.assertNotEqual(self._model.http_authentication_user_policy,self._unique_id)
         
        self._model.use_chunking = new_unique_id
        self.assertEqual(self._model.use_chunking,new_unique_id)
        self.assertNotEqual(self._model.use_chunking,self._unique_id)
         
        self._model.tcp_read_timeout = new_unique_id
        self.assertEqual(self._model.tcp_read_timeout,new_unique_id)
        self.assertNotEqual(self._model.tcp_read_timeout,self._unique_id)
         
        self._model.name = new_unique_id
        self.assertEqual(self._model.name,new_unique_id)
        self.assertNotEqual(self._model.name,self._unique_id)
         
        self._model.enable_ssl = new_unique_id
        self.assertEqual(self._model.enable_ssl,new_unique_id)
        self.assertNotEqual(self._model.enable_ssl,self._unique_id)
         
        self._model.remote_authentication = "DYNAMIC"
        self.assertEqual(self._model.remote_authentication,"DYNAMIC")
        self.assertNotEqual(self._model.remote_authentication,"NONE")
         
        self._model.remote_port = new_unique_id
        self.assertEqual(self._model.remote_port,new_unique_id)
        self.assertNotEqual(self._model.remote_port,self._unique_id)
         
        self._model.enabled = new_unique_id
        self.assertEqual(self._model.enabled,new_unique_id)
        self.assertNotEqual(self._model.enabled,self._unique_id)
         
        self._model.remote_server = new_unique_id
        self.assertEqual(self._model.remote_server,new_unique_id)
        self.assertNotEqual(self._model.remote_server,self._unique_id)
         
        self._model.process_response = new_unique_id
        self.assertEqual(self._model.process_response,new_unique_id)
        self.assertNotEqual(self._model.process_response,self._unique_id)
         


if __name__ == '__main__':
    unittest.main()
