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
from forumsentry_api.models.document import Document  # noqa: E501
#from forumsentry_api.rest import ApiException


class TestDocument(unittest.TestCase):
    """Document unit test stubs"""

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def setUp(self):
        # FIXME: update assignements for none string types e.g boolean and int
        self._unique_id = self.id_generator()
        self._model = Document()  # noqa: E501
        
        
        self._model.description = self._unique_id
        self._model.document = self._unique_id
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

    def testDocument(self):
        """Test Document"""
        
        model = Document()  # noqa: E501
        self.assertTrue(isinstance(model, Document))

    def testDocument_constructor(self):
        """Test Document"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = Document(description=None, document=None, name=None)  # noqa: E501
        self.assertTrue(isinstance(model, Document))

    def testDocument_constructor_none_default(self):
        """Test Document"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = Document(description=self._unique_id, document=self._unique_id, name=self._unique_id)  # noqa: E501
        self.assertTrue(isinstance(model, Document))

        
    def testDocument_properties(self):
        """Test Document"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        new_unique_id = self.id_generator()
        
        
        self._model.description = new_unique_id
        self.assertEqual(self._model.description,new_unique_id)
        self.assertNotEqual(self._model.description,self._unique_id)
         
        self._model.document = new_unique_id
        self.assertEqual(self._model.document,new_unique_id)
        self.assertNotEqual(self._model.document,self._unique_id)
         
        self._model.name = new_unique_id
        self.assertEqual(self._model.name,new_unique_id)
        self.assertNotEqual(self._model.name,self._unique_id)
         


    def testDocument_compare(self):
        """Test Document"""
        
        
        new_unique_id = self.id_generator()
        
        model_copy = copy.deepcopy(self._model)
        
        #check out compare works
        self.assertEqual(model_copy,self._model)
        
        #change something on the model
        model_copy.name = new_unique_id 
        
        #check our compare detects they arent equal
        self.assertNotEqual(model_copy,self._model)


    def testDocument_to_dict(self):
        """Test Document"""
        
        to_dict_object = self._model.to_dict()        

        self.assertTrue(isinstance(to_dict_object,dict))
        
    def testDocument_to_str(self):
        """Test Document"""
        
        to_str_object = self._model.to_str()        

        self.assertTrue(isinstance(to_str_object,str))
        




if __name__ == '__main__':
    unittest.main()
