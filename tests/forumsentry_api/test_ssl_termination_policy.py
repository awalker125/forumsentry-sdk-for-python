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
from forumsentry_api.models.ssl_termination_policy import SslTerminationPolicy  # noqa: E501
#from forumsentry_api.rest import ApiException


class TestSslTerminationPolicy(unittest.TestCase):
    """SslTerminationPolicy unit test stubs"""

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def setUp(self):
        # FIXME: update assignements for none string types e.g boolean and int
        self._unique_id = self.id_generator()
        self._model = SslTerminationPolicy(key_pair=self._unique_id)  # noqa: E501
        
        
        self._model.associate_dn_to_user = self._unique_id
        self._model.description = self._unique_id
        self._model.signer_group = self._unique_id
        self._model.key_pair = self._unique_id
        self._model.acl_policy = self._unique_id
        self._model.use_user_attr_only = self._unique_id
        self._model.enabled_protocols = self._unique_id
        self._model.authenticate_client = self._unique_id
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

    def testSslTerminationPolicy(self):
        """Test SslTerminationPolicy"""
        
        model = SslTerminationPolicy(key_pair=self._unique_id)  # noqa: E501
        self.assertTrue(isinstance(model, SslTerminationPolicy))

    def testSslTerminationPolicy_constructor(self):
        """Test SslTerminationPolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = SslTerminationPolicy(associate_dn_to_user=None, description=None, signer_group=None, key_pair=self._unique_id, acl_policy=None, use_user_attr_only=None, enabled_protocols=None, authenticate_client=None, name=None)  # noqa: E501
        self.assertTrue(isinstance(model, SslTerminationPolicy))

    def testSslTerminationPolicy_constructor_none_default(self):
        """Test SslTerminationPolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        model = SslTerminationPolicy(associate_dn_to_user=self._unique_id, description=self._unique_id, signer_group=self._unique_id, key_pair=self._unique_id, acl_policy=self._unique_id, use_user_attr_only=self._unique_id, enabled_protocols=self._unique_id, authenticate_client=self._unique_id, name=self._unique_id)  # noqa: E501
        self.assertTrue(isinstance(model, SslTerminationPolicy))

        
    def testSslTerminationPolicy_properties(self):
        """Test SslTerminationPolicy"""
        # FIXME: update assignements for none string types e.g boolean and int
        
        new_unique_id = self.id_generator()
        
        
        self._model.associate_dn_to_user = new_unique_id
        self.assertEqual(self._model.associate_dn_to_user,new_unique_id)
        self.assertNotEqual(self._model.associate_dn_to_user,self._unique_id)
         
        self._model.description = new_unique_id
        self.assertEqual(self._model.description,new_unique_id)
        self.assertNotEqual(self._model.description,self._unique_id)
         
        self._model.signer_group = new_unique_id
        self.assertEqual(self._model.signer_group,new_unique_id)
        self.assertNotEqual(self._model.signer_group,self._unique_id)
         
        self._model.key_pair = new_unique_id
        self.assertEqual(self._model.key_pair,new_unique_id)
        self.assertNotEqual(self._model.key_pair,self._unique_id)
         
        self._model.acl_policy = new_unique_id
        self.assertEqual(self._model.acl_policy,new_unique_id)
        self.assertNotEqual(self._model.acl_policy,self._unique_id)
         
        self._model.use_user_attr_only = new_unique_id
        self.assertEqual(self._model.use_user_attr_only,new_unique_id)
        self.assertNotEqual(self._model.use_user_attr_only,self._unique_id)
         
        self._model.enabled_protocols = new_unique_id
        self.assertEqual(self._model.enabled_protocols,new_unique_id)
        self.assertNotEqual(self._model.enabled_protocols,self._unique_id)
         
        self._model.authenticate_client = new_unique_id
        self.assertEqual(self._model.authenticate_client,new_unique_id)
        self.assertNotEqual(self._model.authenticate_client,self._unique_id)
         
        self._model.name = new_unique_id
        self.assertEqual(self._model.name,new_unique_id)
        self.assertNotEqual(self._model.name,self._unique_id)
         


    def testSslTerminationPolicy_compare(self):
        """Test SslTerminationPolicy"""
        
        
        new_unique_id = self.id_generator()
        
        model_copy = copy.deepcopy(self._model)
        
        #check out compare works
        self.assertEqual(model_copy,self._model)
        
        #change something on the model
        model_copy.name = new_unique_id 
        
        #check our compare detects they arent equal
        self.assertNotEqual(model_copy,self._model)


    def testSslTerminationPolicy_to_dict(self):
        """Test SslTerminationPolicy"""
        
        to_dict_object = self._model.to_dict()        

        self.assertTrue(isinstance(to_dict_object,dict))
        
    def testSslTerminationPolicy_to_str(self):
        """Test SslTerminationPolicy"""
        
        to_str_object = self._model.to_str()        

        self.assertTrue(isinstance(to_str_object,str))
        




if __name__ == '__main__':
    unittest.main()
