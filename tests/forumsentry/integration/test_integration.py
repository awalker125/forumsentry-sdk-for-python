'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import sys
#import string
#import random

from forumsentry import api, serialization
from forumsentry.config import Config
from tests.forumsentry import helper



class TestIntegration(unittest.TestCase):
    '''
        This is the base intergration test class that all intergration tests will inherit from
    
        Each API will have its own intergration test. The process is
        
        None FSG
        ========
        
        1) load a json representation of the model
        2) use the create/upsert to create an object in forum
        3) load the model from the api
        4) delete the object from the api
        
        FSG
        ======
        1) use the create/upsert to create an object in forum via fsg import
        3) load the model from the api
        4) delete the object from the api
    '''


 

    def setUp(self):
        
        # this test needs a real forum to do
        self._unique_id = helper.id_generator()
        self._whereami = os.path.dirname(__file__)  
        
        
        self._forum_rest_api_host = os.getenv("FORUM_REST_API_HOST", None)
        self._forum_rest_api_port = os.getenv("FORUM_REST_API_PORT", None)
        self._forum_rest_api_user = os.getenv("FORUM_REST_API_USER", None)
        self._forum_rest_api_password = os.getenv("FORUM_REST_API_PASSWORD", None)
        self._forum_rest_api_protocol = os.getenv("FORUM_REST_API_PROTOCOL", None)
        self._forum_fsg_import_password = os.getenv("FORUM_FSG_IMPORT_PASSWORD", 'password')
        
        if self._forum_rest_api_host is None:
            self.skipTest("FORUM_REST_API_HOST not found. This is required for integration testing")
        
        if self._forum_rest_api_port is None:
            self.skipTest("FORUM_REST_API_PORT not found. This is required for integration testing")
        
        if self._forum_rest_api_user is None:
            self.skipTest("FORUM_REST_API_USER not found. This is required for integration testing")
        
        if self._forum_rest_api_password is None:
            self.skipTest("FORUM_REST_API_PASSWORD not found. This is required for integration testing")
        
        if self._forum_rest_api_protocol is None:
            self.skipTest("FORUM_REST_API_PROTOCOL not found. This is required for integration testing")
        
        self._conf = Config()
        #conf.debug = True
        self._conf.host = self._forum_rest_api_host
        self._conf.port = self._forum_rest_api_port
        self._conf.username = self._forum_rest_api_user
        self._conf.password = self._forum_rest_api_password
        self._conf.protocol = self._forum_rest_api_protocol
        self._api = api.Api(self._conf)
        #self._configuration_import_api = configuration_import_api.ConfigurationImportApi(self._conf)
        self._serializer = serialization.Serialization()


        
    def loadModel(self, test_name, model_type):
        
        testdata_dir = '{0}/../../testdata/'.format(self._whereami)
        model_file = '{0}/{1}.json'.format(testdata_dir,test_name)
        
        with open(model_file, 'r') as f:
            to_serialize = f.read()
            #model_type_class = self._api.str2Class(model_type)                
            model = self._serializer.deserialize(to_serialize, model_type)
            
            return model
    
    def getFsgFileName(self,test_name):
        testdata_dir = '{0}/../../testdata/'.format(self._whereami)
        fsg_filename = '{0}/{1}.fsg'.format(testdata_dir,test_name)
        return  fsg_filename   

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()
