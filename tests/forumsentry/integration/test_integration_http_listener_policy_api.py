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

from forumsentry import  http_listener_policy_api
from forumsentry_api.models import HttpListenerPolicy
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
        self.assertIsInstance(created, HttpListenerPolicy)
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
        self.assertIsInstance(retrieved, HttpListenerPolicy)
        self.assertEqual(retrieved, model)
    
        #   __________   ___ .______     ______   .______     .___________.
        #  |   ____\  \ /  / |   _  \   /  __  \  |   _  \    |           |
        #  |  |__   \  V  /  |  |_)  | |  |  |  | |  |_)  |   `---|  |----`
        #  |   __|   >   <   |   ___/  |  |  |  | |      /        |  |     
        #  |  |____ /  .  \  |  |      |  `--'  | |  |\  \----.   |  |     
        #  |_______/__/ \__\ | _|       \______/  | _| `._____|   |__|     
        #                                                                  
    
        #check we can export the model    
        export_filename = tempfile.mktemp()
        
        exported = api.export(name,export_filename, "password")
        export_found = os.path.isfile(export_filename)
        
        self.assertTrue(exported)
        self.assertTrue(export_found)
          
        #   _______   _______ .______    __        ______   ____    ____ 
        #  |       \ |   ____||   _  \  |  |      /  __  \  \   \  /   / 
        #  |  .--.  ||  |__   |  |_)  | |  |     |  |  |  |  \   \/   /  
        #  |  |  |  ||   __|  |   ___/  |  |     |  |  |  |   \_    _/   
        #  |  '--'  ||  |____ |  |      |  `----.|  `--'  |     |  |     
        #  |_______/ |_______|| _|      |_______| \______/      |__|     
        #                                                                
        deployed = api.deploy(export_filename, "password")
        self.assertTrue(deployed)
        
        
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

    
        #cleanup
        os.remove(export_filename)
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()
