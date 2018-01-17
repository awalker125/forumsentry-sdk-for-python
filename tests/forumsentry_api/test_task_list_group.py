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
from forumsentry_api.models.task_list_group import TaskListGroup  # noqa: E501
#from forumsentry_api.rest import ApiException


class TestTaskListGroup(unittest.TestCase):
    """TaskListGroup unit test stubs"""

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def setUp(self):
        # FIXME: update assignements for none string types e.g boolean and int
        self._unique_id = self.id_generator()
        self._model = TaskListGroup()  # noqa: E501
        
        
        self._model.description = self._unique_id
        self._model.task_lists = self._unique_id
        self._model.name = self._unique_id

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

    def testTaskListGroup(self):
        """Test TaskListGroup"""
        
        model = TaskListGroup()  # noqa: E501
        self.assertTrue(isinstance(model, TaskListGroup))

    def testTaskListGroup_constructor(self):
        """Test TaskListGroup"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = TaskListGroup(description=None, task_lists=None, name=None)  # noqa: E501
        self.assertTrue(isinstance(model, TaskListGroup))

    def testTaskListGroup_constructor_none_default(self):
        """Test TaskListGroup"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = TaskListGroup(description=self._unique_id, task_lists=self._unique_id, name=self._unique_id)  # noqa: E501
        self.assertTrue(isinstance(model, TaskListGroup))

        
    def testTaskListGroup_properties(self):
        """Test TaskListGroup"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        new_unique_id = self.id_generator()
        
        
        self._model.description = new_unique_id
        self.assertEqual(self._model.description,new_unique_id)
        self.assertNotEqual(self._model.description,self._unique_id)
         
        self._model.task_lists = new_unique_id
        self.assertEqual(self._model.task_lists,new_unique_id)
        self.assertNotEqual(self._model.task_lists,self._unique_id)
         
        self._model.name = new_unique_id
        self.assertEqual(self._model.name,new_unique_id)
        self.assertNotEqual(self._model.name,self._unique_id)
         


    def testTaskListGroup_compare(self):
        """Test TaskListGroup"""
        
        
        new_unique_id = self.id_generator()
        
        model_copy = copy.deepcopy(self._model)
        
        #check out compare works
        self.assertEqual(model_copy,self._model)
        
        #change something on the model
        model_copy.name = new_unique_id 
        
        #check our compare detects they arent equal
        self.assertNotEqual(model_copy,self._model)


    def testTaskListGroup_to_dict(self):
        """Test TaskListGroup"""
        
        to_dict_object = self._model.to_dict()        

        self.assertTrue(isinstance(to_dict_object,dict))
        
    def testTaskListGroup_to_str(self):
        """Test TaskListGroup"""
        
        to_str_object = self._model.to_str()        

        self.assertTrue(isinstance(to_str_object,str))
        




if __name__ == '__main__':
    unittest.main()
