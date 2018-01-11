'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import mock
import forumsentry
import sys

import os
import string
import random
import json
import sys


from mock import Mock

from forumsentry import api, http_listener_policy_api
from forumsentry.errors import BadVerbError
from forumsentry_api import HttpListenerPolicy
from requests.exceptions import HTTPError
from forumsentry.config import Config
from forumsentry.api import Api
from forumsentry.errors import ConfigError, NotSupportedError, InvalidTypeError
from tests.forumsentry import helper
from forumsentry_api.models.http_remote_policy import HttpRemotePolicy




class TestApi(unittest.TestCase):

    def setUp(self):
        self._api = http_listener_policy_api.HttpListenerPolicyApi()
        
        self._unique_id = helper.id_generator()
        
        
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
 
    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def _mock_response(
            self,
            status=200,
            test_name=None,
            raise_for_status=None):
        """
        Helper function to build a mock response to request get/post etc..
        This object get injected into the code when request.get would have called the api
        """
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        
        
        
        if raise_for_status:
            http_error = HTTPError(raise_for_status)
            http_error.response = mock.Mock()
            http_error.response.status_code = status
            
            mock_resp.raise_for_status.side_effect = http_error
        # set status code and content
        mock_resp.status_code = status
 
        whereami = os.path.dirname(__file__)  
        
        filename = '{0}/../mocks/{1}'.format(whereami,test_name)

        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                mock_resp.text = f.read()
        
        return mock_resp


    def tearDown(self):
        pass


        


    @mock.patch("forumsentry.api.requests.get")
    def test_http_listener_policy_api_get1(self, mock_get):
        '''
            Tests the when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = self._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
        httpListenerPolicy = self._api.get("bill")
        
        self.assertTrue(isinstance(httpListenerPolicy, HttpListenerPolicy))
        self.assertEqual(httpListenerPolicy.name, "bill")

    @mock.patch("forumsentry.api.requests.get")
    def test_http_listener_policy_api_get2(self, mock_get):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
        
        mock_resp = self._mock_response(status=404,raise_for_status="bill not found")
        mock_get.return_value = mock_resp
        
        httpListenerPolicy = self._api.get("bill")  
        
        self.assertEqual(httpListenerPolicy, None)

        
    @mock.patch("forumsentry.api.requests.get")
    def test_http_listener_policy_api_get3(self, mock_get):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        mock_resp = self._mock_response(status=500,raise_for_status="internal error")
        mock_get.return_value = mock_resp
         
        with self.assertRaises(HTTPError) as e: 
            httpListenerPolicy = self._api.get("bill")  
         
       #print e.exception.message
        self.assertEqual(500, e.exception.response.status_code)
        self.assertIn('internal error', e.exception.message)
    
#     @mock.patch("forumsentry.api.requests.get")
#     def test_get4(self, mock_get):
#         '''
#             Tests when a bad policy type is passed in
#         '''
#         test_name = sys._getframe().f_code.co_name
#  
#          
#         with self.assertRaises(NotSupportedError) as e: 
#             self._api.getForumSentryPolicy(test_name, "bill")  
#          
#        #print e.exception.message
#         self.assertEqual(test_name, e.exception.argument)
#         self.assertIn('not supported', e.exception.message)
        
        
    @mock.patch("forumsentry.api.requests.put")
    def test_http_listener_policy_api_upsert1(self, mock_put):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        #mock_get.return_value  = self.loadMock(test_name)
        mock_resp = self._mock_response(test_name=test_name)
        mock_put.return_value = mock_resp
         
        model = HttpListenerPolicy()  # noqa: E501
        model.use_cookie_authentication = False
        model.use_basic_authentication = False
        model.acl_policy = None
        model.ip_acl_policy = None
        model.read_timeout_millis = 600
        model.password_parameter = None
        model.use_digest_authentication = False
        model.use_chunking = True
        model.port = 600
        model.use_device_ip = True
        model.name = test_name
        model.description = test_name
        model.use_form_post_authentication = False
        model.listener_ssl_policy = None
        model.username_parameter = None
        model.enabled = True
        model.interface = "WAN"
        model.error_template = "Default"
        model.listener_host = None
        model.listener_ssl_enabled = False
        model.password_authentication_realm = None
        model.require_password_authentication = False
        model.use_kerberos_authentication = False
         
        created = self._api.upsert(test_name, model)
         
        self.assertIsInstance(created, HttpListenerPolicy)
        self.assertEqual(created, model)
        self.assertEqual(created.name, test_name)


    @mock.patch("forumsentry.api.requests.put")
    def test_http_listener_policy_api_upsert2(self, mock_put):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        model = HttpListenerPolicy()  # noqa: E501
        model.name = "bill"
        mock_resp = self._mock_response(status=500,raise_for_status="internal error")
        mock_put.return_value = mock_resp
         
        with self.assertRaises(HTTPError) as e: 
            httpListenerPolicy = self._api.upsert("bill",model)  
         
       #print e.exception.message
        self.assertEqual(500, e.exception.response.status_code)
        self.assertIn('internal error', e.exception.message)

    @mock.patch("forumsentry.api.requests.put")
    def test_http_listener_policy_api_upsert3(self, mock_put):
        '''
            Tests when an invalid object for type is passed
        '''
        test_name = sys._getframe().f_code.co_name
 
        
        invalid_object = HttpRemotePolicy("bill")
         
        with self.assertRaises(InvalidTypeError) as e: 
            self._api.upsert("bill", invalid_object)  
         
       #print e.exception.message
        self.assertEqual(HttpRemotePolicy, e.exception.argument)
        self.assertIn('object type does not match expected for type', e.exception.message)

    @mock.patch("forumsentry.api.requests.delete")
    def test_http_listener_policy_api_delete1(self, mock_delete):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = self._mock_response()
        mock_delete.return_value = mock_resp
        
      
        deleted = self._api.delete("bill")
                
        self.assertTrue(deleted)

    @mock.patch("forumsentry.api.requests.delete")
    def test_http_listener_policy_api_delete2(self, mock_delete):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = self._mock_response(status=404,raise_for_status="bill not found")
        mock_delete.return_value = mock_resp
        
      
        deleted = self._api.delete( "bill")
                
        self.assertTrue(deleted)

    @mock.patch("forumsentry.api.requests.delete")
    def test_http_listener_policy_api_delete3(self, mock_delete):
        '''
            Tests requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = self._mock_response(status=500,raise_for_status="internal error")
        mock_delete.return_value = mock_resp
        
      
        with self.assertRaises(HTTPError) as e: 
            deleted = self._api.delete("bill")  
         
        #print e.exception.message
        self.assertEqual(500, e.exception.response.status_code)
        self.assertIn('internal error', e.exception.message)
      


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()