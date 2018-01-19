# coding: utf-8

"""
    forumsentry_api
    
"""


from __future__ import absolute_import

import unittest
import string
import random
import copy

import forumsentry_api
from forumsentry_api.models.json_policies import JsonPolicies  # noqa: E501
#from forumsentry_api.rest import ApiException


class TestJsonPolicies(unittest.TestCase):
    """JsonPolicies unit test stubs"""

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def setUp(self):
        # FIXME: update assignements for none string types e.g boolean and int
        self._unique_id = self.id_generator()
        self._model = JsonPolicies()  # noqa: E501
        
        
        self._model.remote_path = self._unique_id
        self._model.listener_policy = self._unique_id
        self._model.name = self._unique_id
        self._model.virtual_path = self._unique_id
        self._model.remote_policy = self._unique_id
        self._model.description = self._unique_id
        self._model.request_process_type = 'TASK_LIST'
        self._model.response_process_type = 'TASK_LIST'
        self._model.idp_group = self._unique_id
        self._model.request_process = self._unique_id
        self._model.response_process = self._unique_id

    def tearDown(self):
        pass

	'''
		>>>> custom tests
	'''
	#	
	#	Replace with custom tests to increase coverage to 100%. Typically this will be where a value error is thrown on a setter method. This is difficult to template.
	#
	'''
		<<<< custom tests
	'''

    def testJsonPolicies(self):
        """Test JsonPolicies"""
        
        model = JsonPolicies()  # noqa: E501
        self.assertTrue(isinstance(model, JsonPolicies))

    def testJsonPolicies_constructor(self):
        """Test JsonPolicies"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = JsonPolicies(remote_path=None, listener_policy=None, name=None, virtual_path=None, remote_policy=None, description=None, request_process_type=None, response_process_type=None, idp_group=None, request_process=None, response_process=None)  # noqa: E501
        self.assertTrue(isinstance(model, JsonPolicies))

    def testJsonPolicies_constructor_none_default(self):
        """Test JsonPolicies"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = JsonPolicies(remote_path=self._unique_id, listener_policy=self._unique_id, name=self._unique_id, virtual_path=self._unique_id, remote_policy=self._unique_id, description=self._unique_id, request_process_type=self._unique_id, response_process_type=self._unique_id, idp_group=self._unique_id, request_process=self._unique_id, response_process=self._unique_id)  # noqa: E501
        self.assertTrue(isinstance(model, JsonPolicies))

        
    def testJsonPolicies_properties(self):
        """Test JsonPolicies"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        new_unique_id = self.id_generator()
        
        
        self._model.remote_path = new_unique_id
        self.assertEqual(self._model.remote_path,new_unique_id)
        self.assertNotEqual(self._model.remote_path,self._unique_id)
         
        self._model.listener_policy = new_unique_id
        self.assertEqual(self._model.listener_policy,new_unique_id)
        self.assertNotEqual(self._model.listener_policy,self._unique_id)
         
        self._model.name = new_unique_id
        self.assertEqual(self._model.name,new_unique_id)
        self.assertNotEqual(self._model.name,self._unique_id)
         
        self._model.virtual_path = new_unique_id
        self.assertEqual(self._model.virtual_path,new_unique_id)
        self.assertNotEqual(self._model.virtual_path,self._unique_id)
         
        self._model.remote_policy = new_unique_id
        self.assertEqual(self._model.remote_policy,new_unique_id)
        self.assertNotEqual(self._model.remote_policy,self._unique_id)
         
        self._model.description = new_unique_id
        self.assertEqual(self._model.description,new_unique_id)
        self.assertNotEqual(self._model.description,self._unique_id)
         
        self._model.request_process_type = 'TASK_LIST'
        self.assertEqual(self._model.request_process_type,'TASK_LIST')
        self.assertNotEqual(self._model.request_process_type,self._unique_id)
         
        self._model.response_process_type = 'TASK_LIST'
        self.assertEqual(self._model.response_process_type,'TASK_LIST')
        self.assertNotEqual(self._model.response_process_type,self._unique_id)
         
        self._model.idp_group = new_unique_id
        self.assertEqual(self._model.idp_group,new_unique_id)
        self.assertNotEqual(self._model.idp_group,self._unique_id)
         
        self._model.request_process = new_unique_id
        self.assertEqual(self._model.request_process,new_unique_id)
        self.assertNotEqual(self._model.request_process,self._unique_id)
         
        self._model.response_process = new_unique_id
        self.assertEqual(self._model.response_process,new_unique_id)
        self.assertNotEqual(self._model.response_process,self._unique_id)
         


    def testJsonPolicies_compare(self):
        """Test JsonPolicies"""
        
        
        new_unique_id = self.id_generator()
        
        model_copy = copy.deepcopy(self._model)
        
        #check out compare works
        self.assertEqual(model_copy,self._model)
        
        #change something on the model
        model_copy.name = new_unique_id 
        
        #check our compare detects they arent equal
        self.assertNotEqual(model_copy,self._model)


    def testJsonPolicies_to_dict(self):
        """Test JsonPolicies"""
        
        to_dict_object = self._model.to_dict()        

        self.assertTrue(isinstance(to_dict_object,dict))
        
    def testJsonPolicies_to_str(self):
        """Test JsonPolicies"""
        
        to_str_object = self._model.to_str()        

        self.assertTrue(isinstance(to_str_object,str))
        




if __name__ == '__main__':
    unittest.main()
