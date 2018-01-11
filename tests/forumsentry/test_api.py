'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import mock
import forumsentry
import sys

import os
import string
import random
import json
import sys


from mock import Mock

from forumsentry import api
from forumsentry.errors import BadVerbError
from forumsentry_api import HttpListenerPolicy
from requests.exceptions import HTTPError
from forumsentry.config import Config
from forumsentry.api import Api
from forumsentry.errors import ConfigError, NotSupportedError, InvalidTypeError
from tests.forumsentry import helper




class TestApi(unittest.TestCase):

    def setUp(self):
        self._api = api.Api()
        
        self._unique_id = helper.id_generator()
        
        
        #We will use HttpListenerPolicy as our test model
        self._model = HttpListenerPolicy()  # noqa: E501        
        self._model.use_cookie_authentication = self._unique_id
        self._model.use_basic_authentication = self._unique_id
        self._model.acl_policy = self._unique_id
        self._model.ip_acl_policy = self._unique_id
        self._model.read_timeout_millis = self._unique_id
        self._model.password_parameter = self._unique_id
        self._model.use_digest_authentication = self._unique_id
        self._model.use_chunking = self._unique_id
        self._model.port = self._unique_id
        self._model.use_device_ip = self._unique_id
        self._model.name = self._unique_id
        self._model.description = self._unique_id
        self._model.use_form_post_authentication = self._unique_id
        self._model.listener_ssl_policy = self._unique_id
        self._model.username_parameter = self._unique_id
        self._model.enabled = self._unique_id
        self._model.interface = "WAN"
        self._model.error_template = self._unique_id
        self._model.listener_host = self._unique_id
        self._model.listener_ssl_enabled = self._unique_id
        self._model.password_authentication_realm = self._unique_id
        self._model.require_password_authentication = self._unique_id
        self._model.use_kerberos_authentication = self._unique_id
 
    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def _mock_response(
            self,
            status=200,
            test_name=None,
            raise_for_status=None):
        """
        Helper function to build a mock response to request get/post etc..
        This object get injected into the code when request.get would have called the api
        """
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        
        
        
        if raise_for_status:
            http_error = HTTPError(raise_for_status)
            http_error.response = mock.Mock()
            http_error.response.status_code = status
            
            mock_resp.raise_for_status.side_effect = http_error
        # set status code and content
        mock_resp.status_code = status
 
        whereami = os.path.dirname(__file__)  
        
        filename = '{0}/../mocks/{1}'.format(whereami,test_name)

        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                mock_resp.text = f.read()
        
        return mock_resp


    def tearDown(self):
        pass

    def test_str2Class(self):
        '''
        Tests we get a class from str2class
        '''
        self.assertEqual(self._api.str2Class("HttpListenerPolicy"),HttpListenerPolicy)

    def test__request_bad_verb(self):
        '''
        Tests we get an excpetion on sending a bad verb to _requests
        '''
        with self.assertRaises(BadVerbError) as e:
            self._api._request('BAD', 'dummy')

        self.assertEqual('BAD', e.exception.argument)
        self.assertIn('DELETE', e.exception.message)


    def test_Api_constructor(self):
        '''
        Tests constructor
        '''
        conf_default = Config()
        api = Api(conf_default)
        
        self.assertIsInstance(api, Api)
        
        with self.assertRaises(ConfigError) as e:
            api_bad_config = Api(config="not_a_config_object")
        
        self.assertIn('Could not load config', e.exception.message)
        self.assertEqual(type("not_a_config_object"), e.exception.argument)
        

    def test_Api_update_config(self):
        '''
        Tests we can update the config object of the api
        '''
        conf1 = Config(host="conf1")
        conf2 = Config(host="conf2")
        api = Api(config=conf1)
        self.assertEqual(api.config.host,"conf1")
        
        api.config = conf2
        self.assertEqual(api.config.host,"conf2")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()