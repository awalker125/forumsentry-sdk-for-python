'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import mock
import sys
import string
import random
from mock import mock_open

from forumsentry import  ssl_termination_policy_api
from forumsentry_api.models import HttpListenerPolicy
from forumsentry.errors import ForumHTTPError
from forumsentry.errors import  InvalidTypeError
from tests.forumsentry import helper
from forumsentry_api.models.http_remote_policy import HttpRemotePolicy
import tempfile
from mock.mock import patch
from forumsentry_api.models.ssl_termination_policy import SslTerminationPolicy


class TestApi(unittest.TestCase):

    def setUp(self):
        self._api = ssl_termination_policy_api.SslTerminationPolicyApi()
        
        self._unique_id = helper.id_generator()
        
        
        #We will use HttpListenerPolicy as our test model
        self._model = SslTerminationPolicy(key_pair=self._unique_id)  # noqa: E501        

        


    @mock.patch("forumsentry.api.requests.get")
    def test_ssl_termination_policy_api_get1(self, mock_get):
        '''
            Tests the when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
        have_state = self._api.get("bill")
        
        self.assertTrue(isinstance(have_state, SslTerminationPolicy))
        self.assertEqual(have_state.name, "bill")

    @mock.patch("forumsentry.api.requests.get")
    def test_ssl_termination_policy_api_get2(self, mock_get):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
        
        mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
        mock_get.return_value = mock_resp
        
        have_state = self._api.get("bill")  
        
        self.assertEqual(have_state, None)
      
    @mock.patch("forumsentry.api.requests.get")
    def test_ssl_termination_policy_api_get3(self, mock_get):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_get.return_value = mock_resp
         
        with self.assertRaises(ForumHTTPError) as e: 
            have_state = self._api.get("bill")  
         
       #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)
    
    @mock.patch("forumsentry.api.requests.post")
    def test_ssl_termination_policy_api_set1(self, mock_put):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        #mock_get.return_value  = self.loadMock(test_name)
        mock_resp = helper._mock_response(test_name=test_name)
        mock_put.return_value = mock_resp
         
        model = SslTerminationPolicy(key_pair=test_name)  # noqa: E501
        model.name = test_name
        model.authenticate_client = False
        model.enabled_protocols = ['TLSv1.2','TLSv1.1']
        model.associate_dn_to_user = False
        model.use_user_attr_only = False
         
        created = self._api.set(test_name, model)
         
        self.assertIsInstance(created, SslTerminationPolicy)
        self.assertEqual(created, model)
        self.assertEqual(created.name, test_name)

    @mock.patch("forumsentry.api.requests.post")
    def test_ssl_termination_policy_api_set2(self, mock_put):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        model = SslTerminationPolicy(key_pair="bill")  # noqa: E501
        model.name = "bill"
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_put.return_value = mock_resp
         
        with self.assertRaises(ForumHTTPError) as e: 
            created = self._api.set("bill",model)  
         
       #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)

    @mock.patch("forumsentry.api.requests.post")
    def test_ssl_termination_policy_api_set3(self, mock_put):
        '''
            Tests when an invalid object for type is passed
        '''
        test_name = sys._getframe().f_code.co_name
 
        
        invalid_object = HttpRemotePolicy("bill")
         
        with self.assertRaises(InvalidTypeError) as e: 
            self._api.set("bill", invalid_object)  
         
       #print e.exception.message
        self.assertEqual(HttpRemotePolicy, e.exception.argument)
        self.assertIn('object type does not match expected for type', e.exception.message)

    @mock.patch("forumsentry.api.requests.delete")
    def test_ssl_termination_policy_api_delete1(self, mock_delete):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response()
        mock_delete.return_value = mock_resp
        
      
        deleted = self._api.delete("bill")
                
        self.assertTrue(deleted)

    @mock.patch("forumsentry.api.requests.delete")
    def test_ssl_termination_policy_api_delete2(self, mock_delete):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
        mock_delete.return_value = mock_resp
        
      
        deleted = self._api.delete( "bill")
                
        self.assertTrue(deleted)

    @mock.patch("forumsentry.api.requests.delete")
    def test_ssl_termination_policy_api_delete3(self, mock_delete):
        '''
            Tests requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_delete.return_value = mock_resp
        
      
        with self.assertRaises(ForumHTTPError) as e: 
            deleted = self._api.delete("bill")  
         
        #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)
      
    
        

        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()