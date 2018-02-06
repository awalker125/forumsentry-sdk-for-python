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
from forumsentry_api.models.ssl_initiation_policy import SslInitiationPolicy  # noqa: E501
#from forumsentry_api.rest import ApiException


class TestSslInitiationPolicy(unittest.TestCase):
    """SslInitiationPolicy unit test stubs"""

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def setUp(self):
        # FIXME: update assignements for none string types e.g boolean and int
        self._unique_id = self.id_generator()
        self._model = SslInitiationPolicy()  # noqa: E501
        
        
        self._model.ignore_hostname_verification = self._unique_id
        self._model.description = self._unique_id
        self._model.signer_group = self._unique_id
        self._model.key_pair = self._unique_id
        self._model.enabled_protocols = self._unique_id
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

    def testSslInitiationPolicy(self):
        """Test SslInitiationPolicy"""
        
        model = SslInitiationPolicy()  # noqa: E501
        self.assertTrue(isinstance(model, SslInitiationPolicy))

    def testSslInitiationPolicy_constructor(self):
        """Test SslInitiationPolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = SslInitiationPolicy(ignore_hostname_verification=None, description=None, signer_group=None, key_pair=None, enabled_protocols=None, name=None)  # noqa: E501
        self.assertTrue(isinstance(model, SslInitiationPolicy))

    def testSslInitiationPolicy_constructor_none_default(self):
        """Test SslInitiationPolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = SslInitiationPolicy(ignore_hostname_verification=self._unique_id, description=self._unique_id, signer_group=self._unique_id, key_pair=self._unique_id, enabled_protocols=self._unique_id, name=self._unique_id)  # noqa: E501
        self.assertTrue(isinstance(model, SslInitiationPolicy))

        
    def testSslInitiationPolicy_properties(self):
        """Test SslInitiationPolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        new_unique_id = self.id_generator()
        
        
        self._model.ignore_hostname_verification = new_unique_id
        self.assertEqual(self._model.ignore_hostname_verification,new_unique_id)
        self.assertNotEqual(self._model.ignore_hostname_verification,self._unique_id)
         
        self._model.description = new_unique_id
        self.assertEqual(self._model.description,new_unique_id)
        self.assertNotEqual(self._model.description,self._unique_id)
         
        self._model.signer_group = new_unique_id
        self.assertEqual(self._model.signer_group,new_unique_id)
        self.assertNotEqual(self._model.signer_group,self._unique_id)
         
        self._model.key_pair = new_unique_id
        self.assertEqual(self._model.key_pair,new_unique_id)
        self.assertNotEqual(self._model.key_pair,self._unique_id)
         
        self._model.enabled_protocols = new_unique_id
        self.assertEqual(self._model.enabled_protocols,new_unique_id)
        self.assertNotEqual(self._model.enabled_protocols,self._unique_id)
         
        self._model.name = new_unique_id
        self.assertEqual(self._model.name,new_unique_id)
        self.assertNotEqual(self._model.name,self._unique_id)
         


    def testSslInitiationPolicy_compare(self):
        """Test SslInitiationPolicy"""
        
        
        new_unique_id = self.id_generator()
        
        model_copy = copy.deepcopy(self._model)
        
        #check out compare works
        self.assertEqual(model_copy,self._model)
        
        #change something on the model
        model_copy.name = new_unique_id 
        
        #check our compare detects they arent equal
        self.assertNotEqual(model_copy,self._model)


    def testSslInitiationPolicy_to_dict(self):
        """Test SslInitiationPolicy"""
        
        to_dict_object = self._model.to_dict()        

        self.assertTrue(isinstance(to_dict_object,dict))
        
    def testSslInitiationPolicy_to_str(self):
        """Test SslInitiationPolicy"""
        
        to_str_object = self._model.to_str()        

        self.assertTrue(isinstance(to_str_object,str))
        




if __name__ == '__main__':
    unittest.main()
