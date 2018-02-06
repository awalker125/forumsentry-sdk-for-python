'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import sys
from tests.forumsentry.integration.test_integration import TestIntegration
#from tests.forumsentry.integration.test_integration import TestIntegration
#import string
#import random

from forumsentry import  ssl_termination_policy_api
from forumsentry import ConfigurationImportApi
from forumsentry_api.models import SslTerminationPolicy
import tempfile



class TestIntegrationSslTerminationPolicyApi(TestIntegration):


    def test_integration_ssl_termination_policy_api(self):
        '''
            Integration tests for SslTerminationPolicyApi
        '''
        
        #We'd normally use the test name but its too long for the key pair names in forum
        key_pair_name = 'test_integration_ssl_termination'
        
        #setup
        test_name = sys._getframe().f_code.co_name
        model = self.loadModel(test_name, SslTerminationPolicy)
        name = test_name + self._unique_id
        model.name = name
        model.key_pair = key_pair_name
        
        #verify we loaded the right model
        self.assertIsInstance(model, SslTerminationPolicy)
        self.assertEqual(model.name, name)
        
        #create the api to test
        api = ssl_termination_policy_api.SslTerminationPolicyApi(self._conf)
        
        
                #       _______. _______ .___________. __    __  .______   
        #      /       ||   ____||           ||  |  |  | |   _  \  
        #     |   (----`|  |__   `---|  |----`|  |  |  | |  |_)  | 
        #      \   \    |   __|      |  |     |  |  |  | |   ___/  
        #  .----)   |   |  |____     |  |     |  `--'  | |  |      
        #  |_______/    |_______|    |__|      \______/  | _|      
        #                                                          
        

        #We usually name these as test_name but its too long for the key pair names in forum
        setup_fsg = self.getFsgFileName(key_pair_name)
        configuration_import_api = ConfigurationImportApi(self._conf)
        #Have to use config import because there is no fsg on key pair api directly
        imported = configuration_import_api.deploy(setup_fsg, self._forum_fsg_import_password)
        
        self.assertTrue(imported)
        
        
        #       _______. _______ .___________.
        #      /       ||   ____||           |
        #     |   (----`|  |__   `---|  |----`
        #      \   \    |   __|      |  |     
        #  .----)   |   |  |____     |  |     
        #  |_______/    |_______|    |__|     
        #                                     

        
        
        #create a model on the forum
        created = api.set(name, model)
        
        #check what we created is correct
        self.assertIsInstance(created, SslTerminationPolicy)
        self.assertEqual(created, model)

        #    _______  _______ .___________.
        #   /  _____||   ____||           |
        #  |  |  __  |  |__   `---|  |----`
        #  |  | |_ | |   __|      |  |     
        #  |  |__| | |  |____     |  |     
        #   \______| |_______|    |__|     
        #                                  

        #check we can retrieve the model
        retrieved = api.get(name)
        self.assertIsInstance(retrieved, SslTerminationPolicy)
        self.assertEqual(retrieved, model)
        
        #   _______   _______  __       _______ .___________. _______ 
        #  |       \ |   ____||  |     |   ____||           ||   ____|
        #  |  .--.  ||  |__   |  |     |  |__   `---|  |----`|  |__   
        #  |  |  |  ||   __|  |  |     |   __|      |  |     |   __|  
        #  |  '--'  ||  |____ |  `----.|  |____     |  |     |  |____ 
        #  |_______/ |_______||_______||_______|    |__|     |_______|
        #                                                             
            
        #check we can delete the model
        deleted = api.delete(name)
        self.assertTrue(deleted)

        #Check its really gone  
        notfound = api.get(name)
        self.assertIsNone(notfound)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()
