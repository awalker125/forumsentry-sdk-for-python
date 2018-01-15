'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import sys
from test_integration import TestIntegration
#import string
#import random

from forumsentry import api, serialization, configuration_import_api,\
    http_listener_policy_api
from forumsentry_api import HttpListenerPolicy
from forumsentry.config import Config
from tests.forumsentry import helper
import tempfile



class TestIntegration(TestIntegration):


    def test_integration_http_listener_policy_api(self):
        '''
            Intergration tests for HttpListenerPolicyApi
        '''
        
        #setup
        test_name = sys._getframe().f_code.co_name
        model = self.loadModel(test_name, HttpListenerPolicy)
        name = test_name + self._unique_id
        model.name = name
        
        #verify we loaded the right model
        self.assertIsInstance(model, HttpListenerPolicy)
        self.assertEqual(model.name, name)
        
        #create the api to test
        api = http_listener_policy_api.HttpListenerPolicyApi(self._conf)
        
        #create a model on the forum
        created = api.upsert(name, model)
        
        #check what we created is correct
        self.assertIsInstance(created, HttpListenerPolicy)
        self.assertEqual(created, model)

        #check we can retrieve the model
        retrieved = api.get(name)
        self.assertIsInstance(retrieved, HttpListenerPolicy)
        self.assertEqual(retrieved, model)
    
        #check we can export the model    
        export_filename = tempfile.mktemp()
        
        exported = api.export(name,export_filename, "password")
        export_found = os.path.isfile(export_filename)
        
        self.assertTrue(exported)
        self.assertTrue(export_found)
        #cleanup
        os.remove(export_filename)
        
        
        
        #check we can delete the model
        deleted = api.delete(name)
        self.assertTrue(deleted)

        #Check its really gone  
        notfound = api.get(name)
        self.assertIsNone(notfound)

    
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()
