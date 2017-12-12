'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import sys
import string
import random

from forumsentry import api, serialization
from forumsentry_api import HttpListenerPolicy
from forumsentry.config import Config



class TestIntegration(unittest.TestCase):
    '''
    tests data to be created during startup should be named as follows and placed in ../testdata
    test_integration_<policy_type>_<model_type>_<test_id>
    e.g
    test_integration_httpListenerPolicies_HttpListenerPolicy_1
    
    We will load the json via the deserializer and change its name property to be a <unique_id>_<test_id>
    
    On tear down we will attempt to delete these
    '''
 

    def setUp(self):
        
        # this test needs a real forum to do
        self._unique_id = self.id_generator()
        self._whereami = os.path.dirname(__file__)  
        
        
        self._forum_rest_api_host = os.getenv("FORUM_REST_API_HOST", None)
        self._forum_rest_api_port = os.getenv("FORUM_REST_API_PORT", None)
        self._forum_rest_api_user = os.getenv("FORUM_REST_API_USER", None)
        self._forum_rest_api_password = os.getenv("FORUM_REST_API_PASSWORD", None)
        self._forum_rest_api_protocol = os.getenv("FORUM_REST_API_PROTOCOL", None)
        
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
        
        conf = Config()
        #conf.debug = True
        conf.host = self._forum_rest_api_host
        conf.port = self._forum_rest_api_port
        conf.username = self._forum_rest_api_user
        conf.password = self._forum_rest_api_password
        conf.protocol = self._forum_rest_api_protocol
        self._api = api.Api(conf)
        self._serializer = serialization.Serialization()

        self.createTestData()
        


        
        
    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
        
    def createTestData(self):
        
        #test_integration_<policy_type>_<model_type>_<test_id>
        #e.g
        #test_integration_httpListenerPolicies_HttpListenerPolicy_1
    
        
        testdata_dir = '{0}/../testdata/'.format(self._whereami)
        
        for f in os.listdir(testdata_dir):
            if f.startswith("test_integration"):
                filename = os.path.join(testdata_dir, f)
                parts = f.split("_")
                prefix_a = parts[0]
                prefix_b = parts[1]
                policy_type = parts[2]
                model_type = parts[3]
                test_id = parts[4]
                #uncomment for debug
#                 print "filename: {0}".format(filename)     
#                 print "prefix_a: {0}".format(prefix_a)
#                 print "prefix_b: {0}".format(prefix_b)
#                 print "policy_type: {0}".format(policy_type)
#                 print "model_type: {0}".format(model_type)
#                 print "test_id: {0}".format(test_id)

                with open(filename, 'r') as f:
                    to_serialize = f.read()
                    model_type_class = self._api.str2Class(model_type)                
                    model = self._serializer.deserialize(to_serialize, model_type_class)
                    
                    item_name = "{0}_{1}".format(self._unique_id,test_id)
                    model.name = item_name
                    
                    self._api.createOrUpdateForumSentryPolicy(policy_type, item_name, model)


                
                
        
        
    def removeTestData(self):    
                #test_integration_<policy_type>_<model_type>_<test_id>
        #e.g
        #test_integration_httpListenerPolicies_HttpListenerPolicy_1
    
        
        testdata_dir = '{0}/../testdata/'.format(self._whereami)
        
        for f in os.listdir(testdata_dir):
            if f.startswith("test_integration"):
                filename = os.path.join(testdata_dir, f)
                parts = f.split("_")
                prefix_a = parts[0]
                prefix_b = parts[1]
                policy_type = parts[2]
                model_type = parts[3]
                test_id = parts[4]
                #uncomment for debug
#                 print "filename: {0}".format(filename)     
#                 print "prefix_a: {0}".format(prefix_a)
#                 print "prefix_b: {0}".format(prefix_b)
#                 print "policy_type: {0}".format(policy_type)
#                 print "model_type: {0}".format(model_type)
#                 print "test_id: {0}".format(test_id)
                
                item_name = "{0}_{1}".format(self._unique_id,test_id)    
                self._api.deleteForumSentryPolicy(policy_type, item_name)

    def tearDown(self):
        self.removeTestData()

    def _tests(self):
        for name in sorted(dir(self)):
            if name.startswith("test_integration"):
                yield name, getattr(self, name) 

    def test_integration_getForumSentryPolicy_httpListenerPolicies_HttpListenerPolicy_1(self):
        '''
            This needs a listner policy on the forum call test_integration_get_http_listener
        '''
        
        test_name = sys._getframe().f_code.co_name
        parts = test_name.split("_")
        prefix_a = parts[0]
        prefix_b = parts[1]
        method = parts[2]
        policy_type = parts[3]
        model_type = parts[4]
        test_id = parts[5]
        #uncomment for debug
        #print "test_name: {0}".format(test_name)     
        #print "prefix_a: {0}".format(prefix_a)
        #print "prefix_b: {0}".format(prefix_b)
        #print "method: {0}".format(method)
        #print "policy_type: {0}".format(policy_type)
        #print "model_type: {0}".format(model_type)
        #print "test_id: {0}".format(test_id)
                
        item_name = "{0}_{1}".format(self._unique_id,test_id)
        
        httpListenerPolicy = self._api.getForumSentryPolicy("httpListenerPolicies", item_name)
        
        self.assertTrue(isinstance(httpListenerPolicy, HttpListenerPolicy))
        self.assertEqual(httpListenerPolicy.name, item_name)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()
