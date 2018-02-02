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

from forumsentry import  key_pairs_api
from forumsentry_api.models import JsonPolicies
from requests.exceptions import HTTPError
from forumsentry.errors import  InvalidTypeError
from forumsentry.errors import ForumHTTPError
from tests.forumsentry import helper
import tempfile
from mock.mock import patch
from forumsentry_api.models.http_listener_policy import HttpListenerPolicy
from forumsentry_api.models.virtual_directory import VirtualDirectory
from __builtin__ import str


class TestApi(unittest.TestCase):

    def setUp(self):
        self._api = key_pairs_api.KeyPairsApi()
        
        self._unique_id = helper.id_generator()


    @mock.patch("forumsentry.api.requests.get")
    def test_key_pairs_api_get1(self, mock_get):
        '''
            Tests the when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
        key_pair = self._api.get("test1")
        
        self.assertEqual(key_pair, "test1")

    @mock.patch("forumsentry.api.requests.get")
    def test_key_pairs_api_get2(self, mock_get):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
        mock_get.return_value = mock_resp
         
        keyPairs = self._api.get("bill")  
         
        self.assertEqual(keyPairs, None)
       
    @mock.patch("forumsentry.api.requests.get")
    def test_key_pairs_api_get3(self, mock_get):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
          
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_get.return_value = mock_resp
          
        with self.assertRaises(ForumHTTPError) as e: 
            keyPairs = self._api.get("bill")  
          
       #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)
        
    @mock.patch("forumsentry.api.requests.get")
    def test_key_pairs_api_get4(self, mock_get):
        '''
            Tests the when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
        key_pair = self._api.get("doesntexit")
        
        self.assertIsNone(key_pair)
        
    @mock.patch("forumsentry.api.requests.get")
    def test_key_pairs_api_get5(self, mock_get):
        '''
            Tests we get an exception if what comes back from the forum was somehow not json
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
        with self.assertRaises(ValueError) as e: 
            key_pair = self._api.get("doesntexit")

        

    @mock.patch("forumsentry.api.requests.delete")
    def test_key_pairs_api_delete1(self, mock_delete):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
          
         
        mock_resp = helper._mock_response()
        mock_delete.return_value = mock_resp
         
       
        deleted = self._api.delete("bill")
                 
        self.assertTrue(deleted)
 
    @mock.patch("forumsentry.api.requests.delete")
    def test_key_pairs_api_delete2(self, mock_delete):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
          
         
        mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
        mock_delete.return_value = mock_resp
         
       
        deleted = self._api.delete( "bill")
                 
        self.assertTrue(deleted)
 
    @mock.patch("forumsentry.api.requests.delete")
    def test_key_pairs_api_delete3(self, mock_delete):
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
       
#     @mock.patch("forumsentry.api.requests.post")
#     def test_key_pairs_api_export1(self, mock_post):
#         '''
#             Tests the when requests gets a successful response from forum
#         '''
#         test_name = sys._getframe().f_code.co_name
#           
#         mock_resp = helper._mock_response(test_name=test_name)
#         mock_post.return_value = mock_resp
#  
#  
#         filename = tempfile.mktemp()
#          
#         #Cant get this to work via a decorator
#         mo = mock_open()
#         with patch('forumsentry.api.open', mo):
#             exported = self._api.export("bill", filename, "bob")
#          
#         self.assertTrue(exported)
#          
#  
#     @mock.patch("forumsentry.api.requests.post")
#     def test_key_pairs_api_export2(self, mock_post):
#         '''
#             Tests when requests gets a 404 response from forum
#         '''
#         test_name = sys._getframe().f_code.co_name
#           
#         mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
#         mock_post.return_value = mock_resp
#  
#  
#         filename = tempfile.mktemp()
#          
#         #Cant get this to work via a decorator
#         mo = mock_open()
#         with patch('forumsentry.api.open', mo):
#             exported = self._api.export("bill", filename, "bob")
#          
#         self.assertFalse(exported)
#  
#  
#     @mock.patch("forumsentry.api.requests.post")
#     def test_key_pairs_api_export3(self, mock_post):
#         '''
#             Tests when requests gets a 500 response from forum
#         '''
#         test_name = sys._getframe().f_code.co_name
#           
#  
#         mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
#         mock_post.return_value = mock_resp
#          
#         filename = tempfile.mktemp()
#           
#         with self.assertRaises(ForumHTTPError) as e: 
#            exported = self._api.export("bill", filename, "bob") 
#          
#         self.assertEqual(500, e.exception.cause.response.status_code)
#         self.assertIn('internal error', e.exception.message)    
                  
 
    @mock.patch("forumsentry.api.requests.post")
    def test_key_pairs_api_deploy1(self, mock_post):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
          
        #mock_get.return_value  = self.loadMock(test_name)
        mock_resp = helper._mock_response(test_name=test_name)
        mock_post.return_value = mock_resp
         
        whereami = os.path.dirname(__file__)  
         
        filename = '{0}/../mocks/{1}'.format(whereami,test_name)
          
          
        created = self._api.deploy( filename, "password")
          
        self.assertTrue(created)
 
    @mock.patch("forumsentry.api.requests.post")
    def test_key_pairs_api_deploy2(self, mock_post):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
          
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_post.return_value = mock_resp
        
        whereami = os.path.dirname(__file__)  
         
        filename = '{0}/../mocks/{1}'.format(whereami,test_name) 
          
        with self.assertRaises(ForumHTTPError) as e: 
            created = self._api.deploy( filename, "password")
          
       #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)
         
    @mock.patch("forumsentry.api.requests.post")
    def test_key_pairs_api_pkcs12_1(self, mock_post):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
          
        #mock_get.return_value  = self.loadMock(test_name)
        mock_resp = helper._mock_response(test_name=test_name)
        mock_post.return_value = mock_resp
         
        whereami = os.path.dirname(__file__)  
         
        p12 = '{0}/../mocks/{1}'.format(whereami,test_name)
          
        created = self._api.pkcs12("test",p12, "password","password",create_signer_group=True)
          
        self.assertTrue(created)

    @mock.patch("forumsentry.api.requests.post")
    def test_key_pairs_api_pkcs12_2(self, mock_post):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
          
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_post.return_value = mock_resp
        
        whereami = os.path.dirname(__file__)  
         
        p12 = '{0}/../mocks/{1}'.format(whereami,test_name)
          
       
        with self.assertRaises(ForumHTTPError) as e: 
            created = self._api.pkcs12("test",p12, "password","password",create_signer_group=True)
        
       #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()