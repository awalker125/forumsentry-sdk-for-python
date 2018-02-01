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

from forumsentry import  json_policies_api
from forumsentry_api.models import JsonPolicies
import tempfile
from forumsentry_api.models.virtual_directory import VirtualDirectory



class TestIntegrationJsonPoliciesApi(TestIntegration):


    def test_integration_json_policies_api(self):
        '''
            Integration tests for JsonPoliciesApi
        '''
        
        #setup
        test_name = sys._getframe().f_code.co_name
        name = test_name + self._unique_id
        
        model = self.loadModel(test_name, JsonPolicies)
        model.name = name
        
        #verify we loaded the right model
        self.assertIsInstance(model, JsonPolicies)
        self.assertEqual(model.name, name)
        
        virtual_directory_model = self.loadVirtualDirectoryModel(test_name)
        virtual_directory_model.name = name

        self.assertIsInstance(virtual_directory_model, VirtualDirectory)
        self.assertEqual(virtual_directory_model.name, name)

  
        #create the api to test
        api = json_policies_api.JsonPoliciesApi(self._conf)      
        

        #       _______. _______ .___________. __    __  .______   
        #      /       ||   ____||           ||  |  |  | |   _  \  
        #     |   (----`|  |__   `---|  |----`|  |  |  | |  |_)  | 
        #      \   \    |   __|      |  |     |  |  |  | |   ___/  
        #  .----)   |   |  |____     |  |     |  `--'  | |  |      
        #  |_______/    |_______|    |__|      \______/  | _|      
        #                                                          
        
        #We need listner to test the creation of json policy so we'll import them and then delete the json policy
        
        setup_fsg = self.getFsgFileName(test_name)
        imported = api.deploy(setup_fsg, self._forum_fsg_import_password)
        
        self.assertTrue(imported)
        
        #delete the json policy we imported leaving the listner/remote
        deleted = api.delete(test_name)
        self.assertTrue(deleted)

        #Check its really gone  
        notfound = api.get(test_name)
        self.assertIsNone(notfound)
        
        

        
        
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
        self.assertIsInstance(created, JsonPolicies)
        self.assertEqual(created, model)
        
        
        
        #       _______. _______ .___________.  ____    ____  __  .______     .___________. __    __       ___       __             _______   __  .______       _______   ______ .___________.  ______   .______     ____    ____ 
        #      /       ||   ____||           |  \   \  /   / |  | |   _  \    |           ||  |  |  |     /   \     |  |           |       \ |  | |   _  \     |   ____| /      ||           | /  __  \  |   _  \    \   \  /   / 
        #     |   (----`|  |__   `---|  |----`   \   \/   /  |  | |  |_)  |   `---|  |----`|  |  |  |    /  ^  \    |  |           |  .--.  ||  | |  |_)  |    |  |__   |  ,----'`---|  |----`|  |  |  | |  |_)  |    \   \/   /  
        #      \   \    |   __|      |  |         \      /   |  | |      /        |  |     |  |  |  |   /  /_\  \   |  |           |  |  |  ||  | |      /     |   __|  |  |         |  |     |  |  |  | |      /      \_    _/   
        #  .----)   |   |  |____     |  |          \    /    |  | |  |\  \----.   |  |     |  `--'  |  /  _____  \  |  `----.      |  '--'  ||  | |  |\  \----.|  |____ |  `----.    |  |     |  `--'  | |  |\  \----.   |  |     
        #  |_______/    |_______|    |__|     ______\__/     |__| | _| `._____|   |__|      \______/  /__/     \__\ |_______| _____|_______/ |__| | _| `._____||_______| \______|    |__|      \______/  | _| `._____|   |__|     
        #                                    |______|                                                                        |______|                                                                                             

        created_virtual_directory = api.set_virtual_directory(name, name, virtual_directory_model)
        
        #check what we created is correct
        self.assertIsInstance(created_virtual_directory, VirtualDirectory)
        self.assertEqual(created_virtual_directory, virtual_directory_model)


        #    _______  _______ .___________.  ____    ____  __  .______     .___________. __    __       ___       __             _______   __  .______       _______   ______ .___________.  ______   .______     ____    ____ 
        #   /  _____||   ____||           |  \   \  /   / |  | |   _  \    |           ||  |  |  |     /   \     |  |           |       \ |  | |   _  \     |   ____| /      ||           | /  __  \  |   _  \    \   \  /   / 
        #  |  |  __  |  |__   `---|  |----`   \   \/   /  |  | |  |_)  |   `---|  |----`|  |  |  |    /  ^  \    |  |           |  .--.  ||  | |  |_)  |    |  |__   |  ,----'`---|  |----`|  |  |  | |  |_)  |    \   \/   /  
        #  |  | |_ | |   __|      |  |         \      /   |  | |      /        |  |     |  |  |  |   /  /_\  \   |  |           |  |  |  ||  | |      /     |   __|  |  |         |  |     |  |  |  | |      /      \_    _/   
        #  |  |__| | |  |____     |  |          \    /    |  | |  |\  \----.   |  |     |  `--'  |  /  _____  \  |  `----.      |  '--'  ||  | |  |\  \----.|  |____ |  `----.    |  |     |  `--'  | |  |\  \----.   |  |     
        #   \______| |_______|    |__|     ______\__/     |__| | _| `._____|   |__|      \______/  /__/     \__\ |_______| _____|_______/ |__| | _| `._____||_______| \______|    |__|      \______/  | _| `._____|   |__|     
        #                                 |______|                                                                        |______|                                                                                             

        #check we can retrieve the model
        retrieved_virtual_directory = api.get_virtual_directory(name,name)
        self.assertIsInstance(retrieved_virtual_directory, VirtualDirectory)
        self.assertEqual(retrieved_virtual_directory, virtual_directory_model)



        #   _______   _______  __       _______ .___________. _______  ____    ____  __  .______     .___________. __    __       ___       __             _______   __  .______       _______   ______ .___________.  ______   .______     ____    ____ 
        #  |       \ |   ____||  |     |   ____||           ||   ____| \   \  /   / |  | |   _  \    |           ||  |  |  |     /   \     |  |           |       \ |  | |   _  \     |   ____| /      ||           | /  __  \  |   _  \    \   \  /   / 
        #  |  .--.  ||  |__   |  |     |  |__   `---|  |----`|  |__     \   \/   /  |  | |  |_)  |   `---|  |----`|  |  |  |    /  ^  \    |  |           |  .--.  ||  | |  |_)  |    |  |__   |  ,----'`---|  |----`|  |  |  | |  |_)  |    \   \/   /  
        #  |  |  |  ||   __|  |  |     |   __|      |  |     |   __|     \      /   |  | |      /        |  |     |  |  |  |   /  /_\  \   |  |           |  |  |  ||  | |      /     |   __|  |  |         |  |     |  |  |  | |      /      \_    _/   
        #  |  '--'  ||  |____ |  `----.|  |____     |  |     |  |____     \    /    |  | |  |\  \----.   |  |     |  `--'  |  /  _____  \  |  `----.      |  '--'  ||  | |  |\  \----.|  |____ |  `----.    |  |     |  `--'  | |  |\  \----.   |  |     
        #  |_______/ |_______||_______||_______|    |__|     |_______|_____\__/     |__| | _| `._____|   |__|      \______/  /__/     \__\ |_______| _____|_______/ |__| | _| `._____||_______| \______|    |__|      \______/  | _| `._____|   |__|     
        #                                                           |______|                                                                        |______|                                                                                             

        #check we can delete the model
        deleted_virtual_directory = api.delete_virtual_directory(name,name)
        self.assertTrue(deleted_virtual_directory)

        #Check its really gone  
        notfound_virtual_directory = api.get_virtual_directory(name,name)
        self.assertIsNone(notfound_virtual_directory)


        #    _______  _______ .___________.
        #   /  _____||   ____||           |
        #  |  |  __  |  |__   `---|  |----`
        #  |  | |_ | |   __|      |  |     
        #  |  |__| | |  |____     |  |     
        #   \______| |_______|    |__|     
        #                                  

        #check we can retrieve the model
        retrieved = api.get(name)
        self.assertIsInstance(retrieved, JsonPolicies)
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
