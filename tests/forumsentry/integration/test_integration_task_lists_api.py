'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import sys
import tempfile
from tests.forumsentry.integration.test_integration import TestIntegration
#import string
#import random

from forumsentry import   task_lists_api
from forumsentry_api.models.task_list import TaskList




class TestIntegrationtTaskListsApi(TestIntegration):
    '''
        Intergration tests for TaskListsApi
    '''


 
    def test_integration_task_lists_api(self):
        '''
            This runs our integration test for http_listener_policy_api
        '''
        
        #setup
        test_name = sys._getframe().f_code.co_name
        
        fsg_filename = self.getFsgFileName(test_name)
    
        
        #create the api to test
        api = task_lists_api.TaskListsApi(self._conf)
        
        #create a model on the forum
        created = api.deploy(fsg_filename, self._forum_fsg_import_password)
        
        #check what we created is correct
        self.assertTrue(created)


        #check we can retrieve the model
        retrieved = api.get(test_name)
        self.assertIsInstance(retrieved, TaskList)
    
        #check we can export the model    
        export_filename = tempfile.mktemp()
        
        exported = api.export(test_name,export_filename, "password")
        export_found = os.path.isfile(export_filename)
        
        self.assertTrue(exported)
        self.assertTrue(export_found)
        #cleanup
        os.remove(export_filename)
        
        
        
        #check we can delete the model
        deleted = api.delete(test_name)
        self.assertTrue(deleted)

        #Check its really gone  
        notfound = api.get(test_name)
        self.assertIsNone(notfound)


        
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()
