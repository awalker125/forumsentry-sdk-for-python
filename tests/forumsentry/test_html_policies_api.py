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

from forumsentry import  html_policies_api
from forumsentry_api.models import HtmlPolicies
from requests.exceptions import HTTPError
from forumsentry.errors import  InvalidTypeError
from forumsentry.errors import ForumHTTPError
from tests.forumsentry import helper
from forumsentry_api.models.html_policies import HtmlPolicies
import tempfile
from mock.mock import patch
from forumsentry_api.models.http_listener_policy import HttpListenerPolicy
from forumsentry_api.models.virtual_directory import VirtualDirectory


class TestApi(unittest.TestCase):

    def setUp(self):
        self._api = html_policies_api.HtmlPoliciesApi()
        
        self._unique_id = helper.id_generator()


    @mock.patch("forumsentry.api.requests.get")
    def test_html_policies_api_get1(self, mock_get):
        '''
            Tests the when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
        htmlPolices = self._api.get("bill")
        
        self.assertTrue(isinstance(htmlPolices, HtmlPolicies))
        self.assertEqual(htmlPolices.name, "bill")

    @mock.patch("forumsentry.api.requests.get")
    def test_html_policies_api_get2(self, mock_get):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
        
        mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
        mock_get.return_value = mock_resp
        
        htmlPolices = self._api.get("bill")  
        
        self.assertEqual(htmlPolices, None)
      
    @mock.patch("forumsentry.api.requests.get")
    def test_html_policies_api_get3(self, mock_get):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_get.return_value = mock_resp
         
        with self.assertRaises(ForumHTTPError) as e: 
            htmlPolices = self._api.get("bill")  
         
       #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)
    
    @mock.patch("forumsentry.api.requests.put")
    def test_html_policies_api_set1(self, mock_put):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        #mock_get.return_value  = self.loadMock(test_name)
        mock_resp = helper._mock_response(test_name=test_name)
        mock_put.return_value = mock_resp
         
        model = HtmlPolicies()  # noqa: E501
        model.name = test_name
        model.remote_path = test_name
        model.listener_policy = test_name
        model.virtual_path = test_name
        model.remote_policy = test_name
        model.description = test_name
        model.request_process_type = "TASK_LIST"
        model.response_process_type = "TASK_LIST"
        model.idp_group = test_name
        model.request_process = test_name
        model.response_process = test_name
                 
        created = self._api.set(test_name, model)
         
        self.assertIsInstance(created, HtmlPolicies)
        self.assertEqual(created, model)
        self.assertEqual(created.name, test_name)

    @mock.patch("forumsentry.api.requests.put")
    def test_html_policies_api_set2(self, mock_put):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        model = HtmlPolicies()  # noqa: E501
        model.name = "bill"
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_put.return_value = mock_resp
         
        with self.assertRaises(ForumHTTPError) as e: 
            htmlPolices = self._api.set("bill",model)  
         
       #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)

    @mock.patch("forumsentry.api.requests.put")
    def test_html_policies_api_set3(self, mock_put):
        '''
            Tests when an invalid object for type is passed
        '''
        test_name = sys._getframe().f_code.co_name
 
        
        invalid_object = HttpListenerPolicy("bill")
         
        with self.assertRaises(InvalidTypeError) as e: 
            self._api.set("bill", invalid_object)  
         
       #print e.exception.message
        self.assertEqual(HttpListenerPolicy, e.exception.argument)
        self.assertIn('object type does not match expected for type', e.exception.message)

    @mock.patch("forumsentry.api.requests.delete")
    def test_html_policies_api_delete1(self, mock_delete):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response()
        mock_delete.return_value = mock_resp
        
      
        deleted = self._api.delete("bill")
                
        self.assertTrue(deleted)

    @mock.patch("forumsentry.api.requests.delete")
    def test_html_policies_api_delete2(self, mock_delete):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
        mock_delete.return_value = mock_resp
        
      
        deleted = self._api.delete( "bill")
                
        self.assertTrue(deleted)

    @mock.patch("forumsentry.api.requests.delete")
    def test_html_policies_api_delete3(self, mock_delete):
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
      
    @mock.patch("forumsentry.api.requests.post")
    def test_html_policies_api_export1(self, mock_post):
        '''
            Tests the when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        mock_resp = helper._mock_response(test_name=test_name)
        mock_post.return_value = mock_resp


        filename = tempfile.mktemp()
        
        #Cant get this to work via a decorator
        mo = mock_open()
        with patch('forumsentry.api.open', mo):
            exported = self._api.export("bill", filename, "bob")
        
        self.assertTrue(exported)
        

    @mock.patch("forumsentry.api.requests.post")
    def test_html_policies_api_export2(self, mock_post):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
        mock_post.return_value = mock_resp


        filename = tempfile.mktemp()
        
        #Cant get this to work via a decorator
        mo = mock_open()
        with patch('forumsentry.api.open', mo):
            exported = self._api.export("bill", filename, "bob")
        
        self.assertFalse(exported)


    @mock.patch("forumsentry.api.requests.post")
    def test_html_policies_api_export3(self, mock_post):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         

        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_post.return_value = mock_resp
        
        filename = tempfile.mktemp()
         
        with self.assertRaises(ForumHTTPError) as e: 
           exported = self._api.export("bill", filename, "bob") 
        
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)    
                 

    @mock.patch("forumsentry.api.requests.post")
    def test_html_policies_api_deploy1(self, mock_post):
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
    def test_html_policies_api_deploy2(self, mock_post):
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
        

    @mock.patch("forumsentry.api.requests.get")
    def test_html_policies_api_get_virtual_directory1(self, mock_get):
        '''
            Tests the when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
        virtual_directory = self._api.get_virtual_directory('bill', 'bob')
        
        self.assertTrue(isinstance(virtual_directory, VirtualDirectory))
        self.assertEqual(virtual_directory.name, "bob")

    @mock.patch("forumsentry.api.requests.get")
    def test_html_policies_api_get_virtual_directory2(self, mock_get):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
        
        mock_resp = helper._mock_response(status=404,raise_for_status="bob not found")
        mock_get.return_value = mock_resp
        
        virtual_directory = self._api.get_virtual_directory('bill', 'bob')
        
        self.assertEqual(virtual_directory, None)
      
    @mock.patch("forumsentry.api.requests.get")
    def test_html_policies_api_get_virtual_directory3(self, mock_get):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_get.return_value = mock_resp
         
        with self.assertRaises(ForumHTTPError) as e: 
            virtual_directory = self._api.get_virtual_directory('bill', 'bob')
         
       #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)
    
    @mock.patch("forumsentry.api.requests.put")
    def test_html_policies_api_set_virtual_directory1(self, mock_put):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        #mock_get.return_value  = self.loadMock(test_name)
        mock_resp = helper._mock_response(test_name=test_name)
        mock_put.return_value = mock_resp
         
        model = VirtualDirectory()  # noqa: E501
        model.name = test_name
        model.acl_policy = ""
        model.description = ""
        model.enabled = False
        model.error_template = ""
        model.listener_policy = ""
        model.remote_path = ""
        model.remote_policy = ""
        model.request_filter_policy = ""
        model.request_process = ""
        model.request_process_type = "TASK_LIST"
        model.response_process = ""
        model._response_process_type = "TASK_LIST"
        model.use_remote_policy = False
        model.virtual_host = ""
        model.virtual_path = "/bob"
                 
        created = self._api.set_virtual_directory('bill', 'bob',model)
         
        self.assertIsInstance(created, VirtualDirectory)
        self.assertEqual(created, model)
        self.assertEqual(created.name, test_name)

    @mock.patch("forumsentry.api.requests.put")
    def test_html_policies_api_set_virtual_directory2(self, mock_put):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        model = VirtualDirectory()  # noqa: E501
        model.name = "bill"
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_put.return_value = mock_resp
         
        with self.assertRaises(ForumHTTPError) as e: 
            created = self._api.set_virtual_directory('bill', 'bob',model)
         
       #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)

    @mock.patch("forumsentry.api.requests.put")
    def test_html_policies_api_set_virtual_directory3(self, mock_put):
        '''
            Tests when an invalid object for type is passed
        '''
        test_name = sys._getframe().f_code.co_name
 
        
        invalid_object = HttpListenerPolicy("bill")
         
        with self.assertRaises(InvalidTypeError) as e: 
            created = self._api.set_virtual_directory('bill', 'bob',invalid_object)
         
       #print e.exception.message
        self.assertEqual(HttpListenerPolicy, e.exception.argument)
        self.assertIn('object type does not match expected for type', e.exception.message)

    @mock.patch("forumsentry.api.requests.delete")
    def test_html_policies_api_delete_virtual_directory1(self, mock_delete):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response()
        mock_delete.return_value = mock_resp
        
      
        deleted = self._api.delete_virtual_directory("bill","bob")
                
        self.assertTrue(deleted)

    @mock.patch("forumsentry.api.requests.delete")
    def test_html_policies_api_delete_virtual_directory2(self, mock_delete):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
        mock_delete.return_value = mock_resp
        
      
        deleted = self._api.delete_virtual_directory("bill","bob")
                
        self.assertTrue(deleted)

    @mock.patch("forumsentry.api.requests.delete")
    def test_html_policies_api_delete_virtual_directory3(self, mock_delete):
        '''
            Tests requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_delete.return_value = mock_resp
        
      
        with self.assertRaises(ForumHTTPError) as e: 
            deleted = self._api.delete_virtual_directory("bill","bob")
         
        #print e.exception.message
        self.assertEqual(500, e.exception.cause.response.status_code)
        self.assertIn('internal error', e.exception.message)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()