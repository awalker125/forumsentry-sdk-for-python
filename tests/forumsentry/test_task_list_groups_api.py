
'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import mock
import sys


from forumsentry import task_list_groups_api
from requests.exceptions import HTTPError
from forumsentry.errors import InvalidTypeError
from tests.forumsentry import helper
from forumsentry_api.models.http_remote_policy import HttpRemotePolicy
from forumsentry_api.models.task_list import TaskList
from mock.mock import mock_open, patch
import tempfile
from forumsentry_api.models.task_list_group import TaskListGroup




class TestApi(unittest.TestCase):

    def setUp(self):
        self._api = task_list_groups_api.TaskListGroupsApi()
        
        self._unique_id = helper.id_generator()
        
        self._model = TaskListGroup()  # noqa: E501        
        self._model.name = self._unique_id
        self._model.description = self._unique_id
       

    @mock.patch("forumsentry.api.requests.get")
    def test_task_list_groups_api_get1(self, mock_get):
        '''
            Tests the when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
        taskListGroup = self._api.get(test_name)
        
        self.assertIsInstance(taskListGroup, TaskListGroup)
        self.assertEqual(taskListGroup.name, test_name)

    @mock.patch("forumsentry.api.requests.get")
    def test_task_list_groups_api_get2(self, mock_get):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
        
        mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
        mock_get.return_value = mock_resp
        
        taskList = self._api.get("bill")  
        
        self.assertEqual(taskList, None)
      
    @mock.patch("forumsentry.api.requests.get")
    def test_task_list_groups_api_get3(self, mock_get):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_get.return_value = mock_resp
         
        with self.assertRaises(HTTPError) as e: 
            taskListGroup = self._api.get("bill")  
         
       #print e.exception.message
        self.assertEqual(500, e.exception.response.status_code)
        self.assertIn('internal error', e.exception.message)
      
    @mock.patch("forumsentry.api.requests.post")
    def test_task_list_groups_api_deploy1(self, mock_post):
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
    def test_task_list_groups_api_deploy2(self, mock_post):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_post.return_value = mock_resp
       
        whereami = os.path.dirname(__file__)  
        
        filename = '{0}/../mocks/{1}'.format(whereami,test_name) 
         
        with self.assertRaises(HTTPError) as e: 
            created = self._api.deploy( filename, "password")
         
       #print e.exception.message
        self.assertEqual(500, e.exception.response.status_code)
        self.assertIn('internal error', e.exception.message)

    @mock.patch("forumsentry.api.requests.delete")
    def test_task_list_groups_api_delete1(self, mock_delete):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response()
        mock_delete.return_value = mock_resp
        
      
        deleted = self._api.delete("bill")
                
        self.assertTrue(deleted)

    @mock.patch("forumsentry.api.requests.delete")
    def test_task_list_groups_api_delete2(self, mock_delete):
        '''
            Tests when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(status=404,raise_for_status="bill not found")
        mock_delete.return_value = mock_resp
        
      
        deleted = self._api.delete( "bill")
                
        self.assertTrue(deleted)

    @mock.patch("forumsentry.api.requests.delete")
    def test_task_list_groups_api_delete3(self, mock_delete):
        '''
            Tests requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_delete.return_value = mock_resp
        
      
        with self.assertRaises(HTTPError) as e: 
            deleted = self._api.delete("bill")  
         
        #print e.exception.message
        self.assertEqual(500, e.exception.response.status_code)
        self.assertIn('internal error', e.exception.message)
      

    @mock.patch("forumsentry.api.requests.post")
    def test_task_list_groups_api_export1(self, mock_post):
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
    def test_task_list_groups_api_export2(self, mock_post):
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
    def test_task_list_groups_api_export3(self, mock_post):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         

        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_post.return_value = mock_resp
        
        filename = tempfile.mktemp()
         
        with self.assertRaises(HTTPError) as e: 
           exported = self._api.export("bill", filename, "bob") 
        
        self.assertEqual(500, e.exception.response.status_code)
        self.assertIn('internal error', e.exception.message)    


    @mock.patch("forumsentry.api.requests.put")
    def test_task_list_groups_api_set1(self, mock_put):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        #mock_get.return_value  = self.loadMock(test_name)
        mock_resp = helper._mock_response(test_name=test_name)
        mock_put.return_value = mock_resp
         
        model = TaskListGroup()  # noqa: E501
        model.name = test_name
        model.description = test_name
        model.task_lists = ""
         
        created = self._api.set(test_name, model)
         
        self.assertIsInstance(created, TaskListGroup)
        self.assertEqual(created, model)
        self.assertEqual(created.name, test_name)

    @mock.patch("forumsentry.api.requests.put")
    def test_task_list_groups_api_set2(self, mock_put):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        model = TaskListGroup()  # noqa: E501
        model.name = "bill"
        mock_resp = helper._mock_response(status=500,raise_for_status="internal error")
        mock_put.return_value = mock_resp
         
        with self.assertRaises(HTTPError) as e: 
            taskListGroup = self._api.set("bill",model)  
         
       #print e.exception.message
        self.assertEqual(500, e.exception.response.status_code)
        self.assertIn('internal error', e.exception.message)

    @mock.patch("forumsentry.api.requests.put")
    def test_task_list_groups_api_set3(self, mock_put):
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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()