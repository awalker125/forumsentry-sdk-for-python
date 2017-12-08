# coding: utf-8

"""
    forumsentry_api
    
"""


from __future__ import absolute_import

import unittest
import string
import random
import copy

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

    def testHttpListenerPolicy_constructor(self):
        """Test HttpListenerPolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = HttpListenerPolicy(use_cookie_authentication=None, use_basic_authentication=None, acl_policy=None, ip_acl_policy=None, read_timeout_millis=None, password_parameter=None, use_digest_authentication=None, use_chunking=None, port=None, use_device_ip=None, name=None, description=None, use_form_post_authentication=None, listener_ssl_policy=None, username_parameter=None, enabled=None, interface=None, error_template=None, listener_host=None, listener_ssl_enabled=None, password_authentication_realm=None, require_password_authentication=None, use_kerberos_authentication=None)  # noqa: E501
        self.assertTrue(isinstance(model, HttpListenerPolicy))

    def testHttpListenerPolicy_constructor_none_default(self):
        """Test HttpListenerPolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = HttpListenerPolicy(use_cookie_authentication=self._unique_id, use_basic_authentication=self._unique_id, acl_policy=self._unique_id, ip_acl_policy=self._unique_id, read_timeout_millis=self._unique_id, password_parameter=self._unique_id, use_digest_authentication=self._unique_id, use_chunking=self._unique_id, port=self._unique_id, use_device_ip=self._unique_id, name=self._unique_id, description=self._unique_id, use_form_post_authentication=self._unique_id, listener_ssl_policy=self._unique_id, username_parameter=self._unique_id, enabled=self._unique_id, interface=self._unique_id, error_template=self._unique_id, listener_host=self._unique_id, listener_ssl_enabled=self._unique_id, password_authentication_realm=self._unique_id, require_password_authentication=self._unique_id, use_kerberos_authentication=self._unique_id)  # noqa: E501
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
         
        self._model.interface = "WAN"
        self.assertEqual(self._model.interface,"WAN")
        self.assertNotEqual(self._model.interface,self._unique_id)
         
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
         


    def testHttpListenerPolicy_compare(self):
        """Test HttpListenerPolicy"""
        
        
        new_unique_id = self.id_generator()
        
        model_copy = copy.deepcopy(self._model)
        
        #check out compare works
        self.assertEqual(model_copy,self._model)
        
        #change something on the model
        model_copy.name = new_unique_id 
        
        #check our compare detects they arent equal
        self.assertNotEqual(model_copy,self._model)


    def testHttpListenerPolicy_to_dict(self):
        """Test HttpListenerPolicy"""
        
        to_dict_object = self._model.to_dict()        

        self.assertTrue(isinstance(to_dict_object,dict))
        
    def testHttpListenerPolicy_to_str(self):
        """Test HttpListenerPolicy"""
        
        to_str_object = self._model.to_str()        

        self.assertTrue(isinstance(to_str_object,str))
        




if __name__ == '__main__':
    unittest.main()
