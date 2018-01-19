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
from forumsentry_api.models.virtual_directory import VirtualDirectory  # noqa: E501
#from forumsentry_api.rest import ApiException


class TestVirtualDirectory(unittest.TestCase):
    """VirtualDirectory unit test stubs"""

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def setUp(self):
        # FIXME: update assignements for none string types e.g boolean and int
        self._unique_id = self.id_generator()
        self._model = VirtualDirectory()  # noqa: E501
        
        
        self._model.acl_policy = self._unique_id
        self._model.remote_path = self._unique_id
        self._model.virtual_host = self._unique_id
        self._model.name = self._unique_id
        self._model.enabled = self._unique_id
        self._model.listener_policy = self._unique_id
        self._model.description = self._unique_id
        self._model.request_process_type = 'TASK_LIST_GROUP'
        self._model.virtual_path = self._unique_id
        self._model.error_template = self._unique_id
        self._model.use_remote_policy = self._unique_id
        self._model.response_process_type = 'TASK_LIST_GROUP'
        self._model.remote_policy = self._unique_id
        self._model.request_process = self._unique_id
        self._model.request_filter_policy = self._unique_id
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

    def testVirtualDirectory(self):
        """Test VirtualDirectory"""
        
        model = VirtualDirectory()  # noqa: E501
        self.assertTrue(isinstance(model, VirtualDirectory))

    def testVirtualDirectory_constructor(self):
        """Test VirtualDirectory"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = VirtualDirectory(acl_policy=None, remote_path=None, virtual_host=None, name=None, enabled=None, listener_policy=None, description=None, request_process_type=None, virtual_path=None, error_template=None, use_remote_policy=None, response_process_type=None, remote_policy=None, request_process=None, request_filter_policy=None, response_process=None)  # noqa: E501
        self.assertTrue(isinstance(model, VirtualDirectory))

    def testVirtualDirectory_constructor_none_default(self):
        """Test VirtualDirectory"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = VirtualDirectory(acl_policy=self._unique_id, remote_path=self._unique_id, virtual_host=self._unique_id, name=self._unique_id, enabled=self._unique_id, listener_policy=self._unique_id, description=self._unique_id, request_process_type=self._unique_id, virtual_path=self._unique_id, error_template=self._unique_id, use_remote_policy=self._unique_id, response_process_type=self._unique_id, remote_policy=self._unique_id, request_process=self._unique_id, request_filter_policy=self._unique_id, response_process=self._unique_id)  # noqa: E501
        self.assertTrue(isinstance(model, VirtualDirectory))

        
    def testVirtualDirectory_properties(self):
        """Test VirtualDirectory"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        new_unique_id = self.id_generator()
        
        
        self._model.acl_policy = new_unique_id
        self.assertEqual(self._model.acl_policy,new_unique_id)
        self.assertNotEqual(self._model.acl_policy,self._unique_id)
         
        self._model.remote_path = new_unique_id
        self.assertEqual(self._model.remote_path,new_unique_id)
        self.assertNotEqual(self._model.remote_path,self._unique_id)
         
        self._model.virtual_host = new_unique_id
        self.assertEqual(self._model.virtual_host,new_unique_id)
        self.assertNotEqual(self._model.virtual_host,self._unique_id)
         
        self._model.name = new_unique_id
        self.assertEqual(self._model.name,new_unique_id)
        self.assertNotEqual(self._model.name,self._unique_id)
         
        self._model.enabled = new_unique_id
        self.assertEqual(self._model.enabled,new_unique_id)
        self.assertNotEqual(self._model.enabled,self._unique_id)
         
        self._model.listener_policy = new_unique_id
        self.assertEqual(self._model.listener_policy,new_unique_id)
        self.assertNotEqual(self._model.listener_policy,self._unique_id)
         
        self._model.description = new_unique_id
        self.assertEqual(self._model.description,new_unique_id)
        self.assertNotEqual(self._model.description,self._unique_id)
         
        self._model.request_process_type = 'TASK_LIST_GROUP'
        self.assertEqual(self._model.request_process_type,'TASK_LIST_GROUP')
        self.assertNotEqual(self._model.request_process_type,self._unique_id)
         
        self._model.virtual_path = new_unique_id
        self.assertEqual(self._model.virtual_path,new_unique_id)
        self.assertNotEqual(self._model.virtual_path,self._unique_id)
         
        self._model.error_template = new_unique_id
        self.assertEqual(self._model.error_template,new_unique_id)
        self.assertNotEqual(self._model.error_template,self._unique_id)
         
        self._model.use_remote_policy = new_unique_id
        self.assertEqual(self._model.use_remote_policy,new_unique_id)
        self.assertNotEqual(self._model.use_remote_policy,self._unique_id)
         
        self._model.response_process_type = 'TASK_LIST_GROUP'
        self.assertEqual(self._model.response_process_type,'TASK_LIST_GROUP')
        self.assertNotEqual(self._model.response_process_type,self._unique_id)
         
        self._model.remote_policy = new_unique_id
        self.assertEqual(self._model.remote_policy,new_unique_id)
        self.assertNotEqual(self._model.remote_policy,self._unique_id)
         
        self._model.request_process = new_unique_id
        self.assertEqual(self._model.request_process,new_unique_id)
        self.assertNotEqual(self._model.request_process,self._unique_id)
         
        self._model.request_filter_policy = new_unique_id
        self.assertEqual(self._model.request_filter_policy,new_unique_id)
        self.assertNotEqual(self._model.request_filter_policy,self._unique_id)
         
        self._model.response_process = new_unique_id
        self.assertEqual(self._model.response_process,new_unique_id)
        self.assertNotEqual(self._model.response_process,self._unique_id)
         


    def testVirtualDirectory_compare(self):
        """Test VirtualDirectory"""
        
        
        new_unique_id = self.id_generator()
        
        model_copy = copy.deepcopy(self._model)
        
        #check out compare works
        self.assertEqual(model_copy,self._model)
        
        #change something on the model
        model_copy.name = new_unique_id 
        
        #check our compare detects they arent equal
        self.assertNotEqual(model_copy,self._model)


    def testVirtualDirectory_to_dict(self):
        """Test VirtualDirectory"""
        
        to_dict_object = self._model.to_dict()        

        self.assertTrue(isinstance(to_dict_object,dict))
        
    def testVirtualDirectory_to_str(self):
        """Test VirtualDirectory"""
        
        to_str_object = self._model.to_str()        

        self.assertTrue(isinstance(to_str_object,str))
        




if __name__ == '__main__':
    unittest.main()
