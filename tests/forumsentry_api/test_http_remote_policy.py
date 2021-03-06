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

    '''
        >>>> custom tests
    '''
    #    
    #    Replace with custom tests to increase coverage to 100%. Typically this will be where a value error is thrown on a setter method. This is difficult to template.
    #
    '''
        <<<< custom tests
    '''

    def testHttpRemotePolicy(self):
        """Test HttpRemotePolicy"""
        
        model = HttpRemotePolicy()  # noqa: E501
        self.assertTrue(isinstance(model, HttpRemotePolicy))

    def testHttpRemotePolicy_constructor(self):
        """Test HttpRemotePolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = HttpRemotePolicy(use_basic_auth=None, proxy_policy=None, ssl_initiation_policy=None, tcp_connection_timeout=None, http_authentication_user_policy=None, use_chunking=None, tcp_read_timeout=None, name=None, enable_ssl=None, remote_authentication=None, remote_port=None, enabled=None, remote_server=None, process_response=None)  # noqa: E501
        self.assertTrue(isinstance(model, HttpRemotePolicy))

    def testHttpRemotePolicy_constructor_none_default(self):
        """Test HttpRemotePolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = HttpRemotePolicy(use_basic_auth=self._unique_id, proxy_policy=self._unique_id, ssl_initiation_policy=self._unique_id, tcp_connection_timeout=self._unique_id, http_authentication_user_policy=self._unique_id, use_chunking=self._unique_id, tcp_read_timeout=self._unique_id, name=self._unique_id, enable_ssl=self._unique_id, remote_authentication=self._unique_id, remote_port=self._unique_id, enabled=self._unique_id, remote_server=self._unique_id, process_response=self._unique_id)  # noqa: E501
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
         
        self._model.remote_authentication = "NONE"
        self.assertEqual(self._model.remote_authentication,"NONE")
        self.assertNotEqual(self._model.remote_authentication,self._unique_id)
         
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
         


    def testHttpRemotePolicy_compare(self):
        """Test HttpRemotePolicy"""
        
        
        new_unique_id = self.id_generator()
        
        model_copy = copy.deepcopy(self._model)
        
        #check out compare works
        self.assertEqual(model_copy,self._model)
        
        #change something on the model
        model_copy.name = new_unique_id 
        
        #check our compare detects they arent equal
        self.assertNotEqual(model_copy,self._model)


    def testHttpRemotePolicy_to_dict(self):
        """Test HttpRemotePolicy"""
        
        to_dict_object = self._model.to_dict()        

        self.assertTrue(isinstance(to_dict_object,dict))
        
    def testHttpRemotePolicy_to_str(self):
        """Test HttpRemotePolicy"""
        
        to_str_object = self._model.to_str()        

        self.assertTrue(isinstance(to_str_object,str))
        




if __name__ == '__main__':
    unittest.main()
