'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import mock
import sys
import tempfile
import os

from mock import mock_open
from mock.mock import patch


from forumsentry import api
from forumsentry.errors import BadVerbError, InvalidTypeError
from forumsentry_api import HttpListenerPolicy
from forumsentry.config import Config
from forumsentry.api import Api
from forumsentry.errors import ConfigError
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
 

    def tearDown(self):
        pass

    def test_str2Class(self):
        '''
        Tests we get a class from str2class
        '''
        self.assertEqual(self._api.str2Class("HttpListenerPolicy"),HttpListenerPolicy)

    
    def test_class2String(self):
        '''
        Tests we get a class from class2str
        '''
        self.assertEqual(self._api.class2String(HttpListenerPolicy),"HttpListenerPolicy")

    
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
        
    @mock.patch("forumsentry.api.requests.get")
    def test__request_GET(self, mock_get):
        '''
            Tests _request successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
        resp_text = self._api._request("GET", "/test")
        
        self.assertEqual(resp_text, "TEST")
        
    @mock.patch("forumsentry.api.requests.put")
    def test__request_PUT(self, mock_put):
        '''
            Tests _request successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_put.return_value = mock_resp
      
        resp_text = self._api._request("PUT", "/test")
        
        self.assertEqual(resp_text, "TEST")
    
    @mock.patch("forumsentry.api.requests.delete")
    def test__request_DELETE(self, mock_delete):
        '''
            Tests _request successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_delete.return_value = mock_resp
      
        resp_text = self._api._request("DELETE", "/test")
        
        self.assertEqual(resp_text, "TEST")           

    @mock.patch("forumsentry.api.requests.post")
    def test__request_file_download1(self, mock_get):
        '''
            Tests _request_file successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
        filename = tempfile.mktemp()
        
        mo = mock_open()
        with patch('forumsentry.api.open', mo):
             downloaded = self._api._request_file("/test",filename,download=True)
        
        self.assertTrue(downloaded)

    @mock.patch("forumsentry.api.requests.post")
    def test__request_file_download2(self, mock_get):
        '''
            Tests _request_file where the form data isnt a dictionary
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
      
      
        with self.assertRaises(InvalidTypeError) as e:
            downloaded = self._api._request_file("/test","test",form_data="astring",download=True)

        self.assertIn('object type does not match', e.exception.message)
      


    @mock.patch("forumsentry.api.requests.post")
    def test__request_file_upload1(self, mock_post):
        '''
            Tests _request_file successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_post.return_value = mock_resp
      
        whereami = os.path.dirname(__file__)  
        
        filename = '{0}/../mocks/{1}'.format(whereami,test_name)

        
        mo = mock_open()
        with patch('forumsentry.api.open', mo):
             uploaded = self._api._request_file("/test",filename,download=False)
        
        self.assertTrue(uploaded)        

    @mock.patch("forumsentry.api.requests.post")
    def test__request_file_upload2(self, mock_post):
        '''
            Tests _request_file where the form data isnt a dictionary
        '''
        test_name = sys._getframe().f_code.co_name
         
        
        mock_resp = helper._mock_response(test_name=test_name)
        mock_post.return_value = mock_resp
      
        whereami = os.path.dirname(__file__)  
        
        filename = '{0}/../mocks/{1}'.format(whereami,test_name)
      
        with self.assertRaises(InvalidTypeError) as e:
            downloaded = self._api._request_file("/test",filename,form_data="astring",download=False)

        self.assertIn('object type does not match', e.exception.message)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()