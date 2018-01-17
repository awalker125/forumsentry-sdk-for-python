'''
Created on 8 Dec 2017

@author: walandre
'''
import unittest

import os
#import string
#import random
import json
import sys
import datetime

from forumsentry.serialization import Serialization
from forumsentry_api.models.http_listener_policy import HttpListenerPolicy
from tests.forumsentry import helper
from forumsentry_api.models.task_list_group import TaskListGroup
from forumsentry.errors import DeSerializationError
from datetime import date


class TestSerialization(unittest.TestCase):

    def setUp(self):
        self._unique_id = helper.id_generator()
        self._serialization = Serialization()
        self._whereami = os.path.dirname(__file__)  
        



    def tearDown(self):
        pass

    def test_serializationConstructor(self):
        serialization = Serialization()
        self.assertTrue(isinstance(serialization,Serialization))

    def test_serializeHttpListenerPolicy(self):
        
                #We will use HttpListenerPolicy as our test model
        model = HttpListenerPolicy()  # noqa: E501
        
        
        model.use_cookie_authentication = self._unique_id
        model.use_basic_authentication = self._unique_id
        model.acl_policy = self._unique_id
        model.ip_acl_policy = self._unique_id
        model.read_timeout_millis = self._unique_id
        model.password_parameter = self._unique_id
        model.use_digest_authentication = self._unique_id
        model.use_chunking = self._unique_id
        model.port = self._unique_id
        model.use_device_ip = self._unique_id
        model.name = self._unique_id
        model.description = self._unique_id
        model.use_form_post_authentication = self._unique_id
        model.listener_ssl_policy = self._unique_id
        model.username_parameter = self._unique_id
        model.enabled = self._unique_id
        model.interface = "WAN"
        model.error_template = self._unique_id
        model.listener_host = self._unique_id
        model.listener_ssl_enabled = self._unique_id
        model.password_authentication_realm = self._unique_id
        model.require_password_authentication = self._unique_id
        model.use_kerberos_authentication = self._unique_id
        
        j = self._serialization.serialize(model)

        data = json.loads(j)
        #print j
        self.assertEqual(data['name'], self._unique_id)
        
    def test_deserializeHttpListenerPolicy(self):
        
        test_name = sys._getframe().f_code.co_name
        
        filename = '{0}/../mocks/{1}'.format(self._whereami,test_name)
        
        j = None
        #get a json string to desrialize into an object
        with open(filename, 'r') as f:
            j = f.read()
        
        obj = self._serialization.deserialize(j, HttpListenerPolicy)

        self.assertIsInstance(obj, HttpListenerPolicy)
        self.assertEqual(obj.name, "LPXHVV")        
        self.assertEqual(obj.port, 80)
        self.assertEqual(obj.read_timeout_millis, 600)   


    def test_serializeNone(self):
        
        
        model = None
        
        j = self._serialization.serialize(model)

        data = json.loads(j)
        
        self.assertIsNone(data)

    def test_serializeList(self):
        
        
        model = ["The", "earth", "revolves", "around", "sun"]
        
        j = self._serialization.serialize(model)

        data = json.loads(j)
    
        self.assertIsInstance(data, list)
    




    def test_serializeTuple(self):
        
        
        model = ('a', 'b', 'c', 'd', 'e')
        
        j = self._serialization.serialize(model)

        data = json.loads(j)
    
        self.assertIsInstance(data, list)
  
    def test_serializeDateTime(self):
        

        now = datetime.datetime.now()
        
        j = self._serialization.serialize(now)
        
        #print j

        data = json.loads(j)
       
    
        self.assertIsInstance(data, unicode)  

    def test_serializeDict(self):
        
        #now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        model = {}
        model['name'] = self._unique_id
        
        j = self._serialization.serialize(model)

        data = json.loads(j)
       
    
        self.assertIsInstance(data, dict)  
        

    #up to here
    
    def test_deserialize_DeSerializationError1(self):
        '''
        Tests when we try to deserialize a date with an invalid date string
        '''
        test_name = sys._getframe().f_code.co_name
        
        j = "notadate"

        
        with self.assertRaises(DeSerializationError) as e:
            obj = self._serialization.deserialize(j, datetime.datetime)

    def test_deserialize_DeSerializationError2(self):
        '''
        Tests when we try to deserialize a date with an none string object
        '''
        test_name = sys._getframe().f_code.co_name
        
        j = {}
        j['nota'] = "date"

        
        with self.assertRaises(DeSerializationError) as e:
            obj = self._serialization.deserialize(j, datetime.datetime)

    def test_serializeTaskListGroup(self):
        
                #We will use HttpListenerPolicy as our test model
        model = TaskListGroup()  # noqa: E501
        model.name = self._unique_id
        model.task_lists = None

        
        j = self._serialization.serialize(model)

        data = json.loads(j)
        #print j
        self.assertEqual(data['name'], self._unique_id)

    def test_deserializeTaskListGroup(self):
        
        test_name = sys._getframe().f_code.co_name
        
        filename = '{0}/../mocks/{1}'.format(self._whereami,test_name)
        
        j = None
        #get a json string to desrialize into an object
        with open(filename, 'r') as f:
            j = f.read()
        
        obj = self._serialization.deserialize(j, TaskListGroup)

        self.assertIsInstance(obj, TaskListGroup)
        self.assertEqual(obj.name, "LPXHVV")        

    def test_deserializeObject(self):
        
        test_name = sys._getframe().f_code.co_name
        
        filename = '{0}/../mocks/{1}'.format(self._whereami,test_name)
        
        j = None
        #get a json string to desrialize into an object
        with open(filename, 'r') as f:
            j = f.read()
        
        obj = self._serialization.deserialize(j, object)

        self.assertIsInstance(obj, object)

    def test_deserializeDateTime(self):
        

        test_name = sys._getframe().f_code.co_name
        
        filename = '{0}/../mocks/{1}'.format(self._whereami,test_name)
        
        j = None
        #get a json string to desrialize into an object
        with open(filename, 'r') as f:
            j = f.read()
        
        obj = self._serialization.deserialize(j, datetime.datetime)

        #print type(obj)
        #print obj
        self.assertIn("2018-01-17", str(obj))


    def test_deserializeDate(self):
        

        test_name = sys._getframe().f_code.co_name
        
        filename = '{0}/../mocks/{1}'.format(self._whereami,test_name)
        
        j = None
        #get a json string to desrialize into an object
        with open(filename, 'r') as f:
            j = f.read()
        
        obj = self._serialization.deserialize(j, datetime.date)

        #print type(obj)
        #print obj
        self.assertIn("2018-01-17", str(obj))


    def test_deserializePrimitive(self):
        

        test_name = sys._getframe().f_code.co_name
        
        filename = '{0}/../mocks/{1}'.format(self._whereami,test_name)
        
        j = None
        #get a json string to desrialize into an object
        with open(filename, 'r') as f:
            j = f.read()
        
        obj = self._serialization.deserialize(j, long)

        #print type(obj)
        #print obj
        self.assertIsInstance(obj, long)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()