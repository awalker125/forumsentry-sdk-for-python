'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import sys
from tests.forumsentry.integration.test_integration import TestIntegration
#import string
#import random

from forumsentry import api, serialization, configuration_import_api,\
    http_listener_policy_api
from forumsentry_api import HttpListenerPolicy
from forumsentry.config import Config
from tests.forumsentry import helper
import tempfile



class TestIntegrationConfigurationImportApi(TestIntegration):
    '''
        Intergration tests for HttpListenerPolicyApi
    '''


 

    def test_integration_configuration_import_api(self):
        
        #setup
        test_name = sys._getframe().f_code.co_name
       
        fsg_filename = self.getFsgFileName(test_name)

        api = configuration_import_api.ConfigurationImportApi(self._conf)
        
        #Import our fsg file
        import_result = api.import_fsg(fsg_filename,self._forum_fsg_import_password)
        
        self.assertTrue(import_result)

        #our fsg has an http listener so we'll check its there and then delete
        api2 = http_listener_policy_api.HttpListenerPolicyApi(self._conf)
                #check we can retrieve the model
        retrieved = api2.get(test_name)
        self.assertIsInstance(retrieved, HttpListenerPolicy)
        self.assertEqual(retrieved.name, test_name)
        
        
        #check we can delete the model
        deleted = api2.delete(test_name)
        self.assertTrue(deleted)

        #Check its really gone  
        notfound = api2.get(test_name)
        self.assertIsNone(notfound)
        
        
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()
