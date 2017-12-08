# coding: utf-8

"""
    forumsentry_api
    
"""


from __future__ import absolute_import

import unittest
import string
import random

import forumsentry_api
from forumsentry_api.models.http_listener_policy import HttpListenerPolicy  # noqa: E501
#from forumsentry_api.rest import ApiException


class TestHttpListenerPolicy(unittest.TestCase):
    """HttpListenerPolicy unit test stubs"""

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def setUp(self):
        # FIXME: update assignements for none string types e.g boolean and int
        self._unique_id = self.id_generator()
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

    def testHttpListenerPolicy(self):
        """Test HttpListenerPolicy"""
        
        model = HttpListenerPolicy()  # noqa: E501
        self.assertTrue(isinstance(model, HttpListenerPolicy))
        
    def testHttpListenerPolicy_properties(self):
        """Test HttpListenerPolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        new_unique_id = self.id_generator()
        
        
        self._model.use_cookie_authentication = new_unique_id
        self.assertEqual(self._model.use_cookie_authentication,new_unique_id)
        self.assertNotEqual(self._model.use_cookie_authentication,self._unique_id)
         
        self._model.use_basic_authentication = new_unique_id
        self.assertEqual(self._model.use_basic_authentication,new_unique_id)
        self.assertNotEqual(self._model.use_basic_authentication,self._unique_id)
         
        self._model.acl_policy = new_unique_id
        self.assertEqual(self._model.acl_policy,new_unique_id)
        self.assertNotEqual(self._model.acl_policy,self._unique_id)
         
        self._model.ip_acl_policy = new_unique_id
        self.assertEqual(self._model.ip_acl_policy,new_unique_id)
        self.assertNotEqual(self._model.ip_acl_policy,self._unique_id)
         
        self._model.read_timeout_millis = new_unique_id
        self.assertEqual(self._model.read_timeout_millis,new_unique_id)
        self.assertNotEqual(self._model.read_timeout_millis,self._unique_id)
         
        self._model.password_parameter = new_unique_id
        self.assertEqual(self._model.password_parameter,new_unique_id)
        self.assertNotEqual(self._model.password_parameter,self._unique_id)
         
        self._model.use_digest_authentication = new_unique_id
        self.assertEqual(self._model.use_digest_authentication,new_unique_id)
        self.assertNotEqual(self._model.use_digest_authentication,self._unique_id)
         
        self._model.use_chunking = new_unique_id
        self.assertEqual(self._model.use_chunking,new_unique_id)
        self.assertNotEqual(self._model.use_chunking,self._unique_id)
         
        self._model.port = new_unique_id
        self.assertEqual(self._model.port,new_unique_id)
        self.assertNotEqual(self._model.port,self._unique_id)
         
        self._model.use_device_ip = new_unique_id
        self.assertEqual(self._model.use_device_ip,new_unique_id)
        self.assertNotEqual(self._model.use_device_ip,self._unique_id)
         
        self._model.name = new_unique_id
        self.assertEqual(self._model.name,new_unique_id)
        self.assertNotEqual(self._model.name,self._unique_id)
         
        self._model.description = new_unique_id
        self.assertEqual(self._model.description,new_unique_id)
        self.assertNotEqual(self._model.description,self._unique_id)
         
        self._model.use_form_post_authentication = new_unique_id
        self.assertEqual(self._model.use_form_post_authentication,new_unique_id)
        self.assertNotEqual(self._model.use_form_post_authentication,self._unique_id)
         
        self._model.listener_ssl_policy = new_unique_id
        self.assertEqual(self._model.listener_ssl_policy,new_unique_id)
        self.assertNotEqual(self._model.listener_ssl_policy,self._unique_id)
         
        self._model.username_parameter = new_unique_id
        self.assertEqual(self._model.username_parameter,new_unique_id)
        self.assertNotEqual(self._model.username_parameter,self._unique_id)
         
        self._model.enabled = new_unique_id
        self.assertEqual(self._model.enabled,new_unique_id)
        self.assertNotEqual(self._model.enabled,self._unique_id)
         
        self._model.interface = "LAN"
        self.assertEqual(self._model.interface,"LAN")
        self.assertNotEqual(self._model.interface,"WAN")
         
        self._model.error_template = new_unique_id
        self.assertEqual(self._model.error_template,new_unique_id)
        self.assertNotEqual(self._model.error_template,self._unique_id)
         
        self._model.listener_host = new_unique_id
        self.assertEqual(self._model.listener_host,new_unique_id)
        self.assertNotEqual(self._model.listener_host,self._unique_id)
         
        self._model.listener_ssl_enabled = new_unique_id
        self.assertEqual(self._model.listener_ssl_enabled,new_unique_id)
        self.assertNotEqual(self._model.listener_ssl_enabled,self._unique_id)
         
        self._model.password_authentication_realm = new_unique_id
        self.assertEqual(self._model.password_authentication_realm,new_unique_id)
        self.assertNotEqual(self._model.password_authentication_realm,self._unique_id)
         
        self._model.require_password_authentication = new_unique_id
        self.assertEqual(self._model.require_password_authentication,new_unique_id)
        self.assertNotEqual(self._model.require_password_authentication,self._unique_id)
         
        self._model.use_kerberos_authentication = new_unique_id
        self.assertEqual(self._model.use_kerberos_authentication,new_unique_id)
        self.assertNotEqual(self._model.use_kerberos_authentication,self._unique_id)
         


if __name__ == '__main__':
    unittest.main()
