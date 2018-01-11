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
from tests.forumsentry import helper



class TestIntegration(unittest.TestCase):
    '''
    tests data to be created during startup should be named as follows and placed in ../testdata
    test_integration_<policy_type>_<model_type>_<test_id>
    e.g
    test_integration_httpListenerPolicies_HttpListenerPolicy_1
    
    We will load the json via the deserializer and change its name property to be a <unique_id>_<test_id>
    
    On tear down we will attempt to delete these
    '''

#     policy_types = {
#         'httpListenerPolicies': 'HttpListenerPolicy',
#         'httpRemotePolicies': 'HttpRemotePolicy',
#         'htmlPolicies': 'HtmlPolicies'
#     }
    
    policy_types = {
        'httpListenerPolicies': 'HttpListenerPolicy',
        'httpRemotePolicies': 'HttpRemotePolicy'
    }
    
    #The ids below relate to the names in the corresponding test data directory
    tests = {
        'generic_intergration_getForumSentryPolicy_policyType_policyObject_where_exists': 1,
        'generic_intergration_getForumSentryPolicy_policyType_policyObject_where_doesnt_exist': 2,
        'generic_intergration_deleteForumSentryPolicy_policyType_policyObject_where_doesnt_exist': 3,  
        'generic_intergration_deleteForumSentryPolicy_policyType_policyObject_where_exists': 4,  
        'generic_intergration_createForumSentryPolicy_policyType_policyObject': 5,  
     
    }
 

    def setUp(self):
        
        # this test needs a real forum to do
        self._unique_id = helper.id_generator()
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
        
        
    def createTestData(self):
        
        #test_integration_<policy_type>_<model_type>_<test_id>
        #e.g
        #test_integration_httpListenerPolicies_HttpListenerPolicy_1
    
        
        testdata_dir = '{0}/../testdata/'.format(self._whereami)
        
        for f in sorted(os.listdir(testdata_dir)):
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
                    
                    item_name = self.get_item_name(model_type,test_id)
                    model.name = item_name
                    
                    self._api.createOrUpdateForumSentryPolicy(policy_type, item_name, model)

    def get_item_name(self,policy_object_name,test_id):
        
        
        return "{0}_{1}_{2}".format(self._unique_id,test_id,policy_object_name)

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
                
                item_name = self.get_item_name(model_type,test_id)
                self._api.deleteForumSentryPolicy(policy_type, item_name)

    def tearDown(self):
       # self.removeTestData()
       pass

    def test_integration(self):
        '''
            This runs our generic tests against all of types
        '''
        for policy_type, policy_object_name in self.policy_types.items():
            
            for generic_test_name, test_id  in self.tests.items():
            
                policy_object = self._api.str2Class(policy_object_name)
                test = getattr(self, generic_test_name)
                test(policy_type,policy_object,test_id)
                        
    def generic_intergration_getForumSentryPolicy_policyType_policyObject_where_exists(self, policy_type, policy_object, test_id):
        
        policy_object_name = self._api.class2String(policy_object)

        item_name = self.get_item_name(policy_object_name,str(test_id))        

        model = self._api.getForumSentryPolicy(policy_type, item_name)
     
        self.assertTrue(isinstance(model, policy_object))
        self.assertEqual(model.name, item_name)

    def generic_intergration_getForumSentryPolicy_policyType_policyObject_where_doesnt_exist(self, policy_type, policy_object, test_id):
        
        policy_object_name = self._api.class2String(policy_object)

        item_name = self.get_item_name(policy_object_name,str(test_id))        
        
        model = self._api.getForumSentryPolicy(policy_type, item_name)
        
        self.assertEqual(model, None)    

    def generic_intergration_deleteForumSentryPolicy_policyType_policyObject_where_doesnt_exist(self, policy_type, policy_object, test_id):
        
        policy_object_name = self._api.class2String(policy_object)

        item_name = self.get_item_name(policy_object_name,str(test_id))        
        
        deleted = self._api.deleteForumSentryPolicy(policy_type, item_name)
        
        self.assertEqual(deleted, True)  

    def generic_intergration_deleteForumSentryPolicy_policyType_policyObject_where_exists(self, policy_type, policy_object, test_id):
        
        policy_object_name = self._api.class2String(policy_object)

        item_name = self.get_item_name(policy_object_name,str(test_id))        
        
        #first check it exists
        model = self._api.getForumSentryPolicy(policy_type, item_name)
        
        self.assertTrue(isinstance(model, policy_object))
        self.assertEqual(model.name, item_name)
        
        #Next delete it
        deleted = self._api.deleteForumSentryPolicy(policy_type, item_name)
        
        self.assertEqual(deleted, True)     
    
    def generic_intergration_createForumSentryPolicy_policyType_policyObject(self, policy_type, policy_object, test_id):
        
        policy_object_name = self._api.class2String(policy_object)

        item_name = self.get_item_name(policy_object_name,str(test_id))        
        
        #first get our basic policy from the forum. This is created by createTestData on setup
        initial_model = self._api.getForumSentryPolicy(policy_type, item_name)
        
        self.assertTrue(isinstance(initial_model, policy_object))
        self.assertEqual(initial_model.name, item_name)
        
        new_item_name = item_name + "_NEW"
        
        initial_model.name = new_item_name
        
        #Next create a copy of it on forum
        new_model = self._api.createOrUpdateForumSentryPolicy(policy_type,new_item_name, initial_model)
        
        self.assertEqual(initial_model, new_model)
        
        #Next check its there on the forum and we can read it
        
        retrieved_new_model = self._api.getForumSentryPolicy(policy_type, new_item_name)
        
        self.assertEqual(retrieved_new_model, new_model)
        
        #Next we modify the policy
        
        retrieved_new_model.enabled = False
        
        self._api.createOrUpdateForumSentryPolicy(policy_type,new_item_name, retrieved_new_model)
        
        #Clean up by deleting the policy we created and modified
        
        deleted = self._api.deleteForumSentryPolicy(policy_type, new_item_name)
        
        self.assertEqual(deleted, True)
 


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()
