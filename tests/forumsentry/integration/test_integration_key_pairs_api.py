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

from forumsentry import  KeyPairsApi
import tempfile
from forumsentry_api.models.virtual_directory import VirtualDirectory



class TestIntegrationKeyPairsApi(TestIntegration):


    def test_integration_key_pairs_api(self):
        '''
            Integration tests for KeyPairsApi
        '''
        
        #setup
        test_name = sys._getframe().f_code.co_name
        name = test_name + self._unique_id
        
        testdata_dir = '{0}/../../testdata/'.format(self._whereami)
        
        #See the dev docs for how to create this
        p12 = '{0}/keyPairs/forumsentry-sdk-for-python.p12'.format(testdata_dir)
        
        #create the api to test
        api = KeyPairsApi(self._conf)      
              

        

        #  .______    __  ___   ______     _______.__   ___   
        #  |   _  \  |  |/  /  /      |   /       /_ | |__ \  
        #  |  |_)  | |  '  /  |  ,----'  |   (----`| |    ) | 
        #  |   ___/  |    <   |  |        \   \    | |   / /  
        #  |  |      |  .  \  |  `----.----)   |   | |  / /_  
        #  | _|      |__|\__\  \______|_______/    |_| |____| 
        #                                                     

        
        #create a model on the forum
        uploaded = api.pkcs12(name, p12, "password", "password", create_signer_group=True)
        
        #check what we created is correct
        self.assertTrue(uploaded)
        

        #    _______  _______ .___________.
        #   /  _____||   ____||           |
        #  |  |  __  |  |__   `---|  |----`
        #  |  | |_ | |   __|      |  |     
        #  |  |__| | |  |____     |  |     
        #   \______| |_______|    |__|     
        #                                  

        #check we can retrieve the model
        retrieved = api.get(name)
        self.assertEqual(retrieved, name)
    
    
       
        
        #   _______   _______ .______    __        ______   ____    ____ 
        #  |       \ |   ____||   _  \  |  |      /  __  \  \   \  /   / 
        #  |  .--.  ||  |__   |  |_)  | |  |     |  |  |  |  \   \/   /  
        #  |  |  |  ||   __|  |   ___/  |  |     |  |  |  |   \_    _/   
        #  |  '--'  ||  |____ |  |      |  `----.|  `--'  |     |  |     
        #  |_______/ |_______|| _|      |_______| \______/      |__|     
        #                                                                
        deploy_test_fsg = self.getFsgFileName(test_name)
        
        deployed = api.deploy(deploy_test_fsg, "password")
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

        #check we can delete the model
        deleted2 = api.delete(test_name)
        self.assertTrue(deleted2)

        #Check its really gone  
        notfound2 = api.get(test_name)
        self.assertIsNone(notfound2)
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()
