'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import mock
import forumsentry
import sys

from mock import MagicMock
from mock import Mock

from forumsentry import api
from forumsentry.errors import BadVerbError
from forumsentry_api import HttpListenerPolicy
from forumsentry.config import Config



class TestIntegration(unittest.TestCase):

 

    def setUp(self):
        
        #this test needs a real forum to do
        
        self._forum_rest_api_host = os.getenv("FORUM_REST_API_HOST", None)
        self._forum_rest_api_port = os.getenv("FORUM_REST_API_PORT", None)
        self._forum_rest_api_user = os.getenv("FORUM_REST_API_USER", None)
        self._forum_rest_api_password = os.getenv("FORUM_REST_API_PASSWORD", None)
        
        if self._forum_rest_api_host is None:
            self.skipTest("FORUM_REST_API_HOST not found. This is required for integration testing")
        
        if self._forum_rest_api_port is None:
            self.skipTest("FORUM_REST_API_PORT not found. This is required for integration testing")
        
        if self._forum_rest_api_user is None:
            self.skipTest("FORUM_REST_API_USER not found. This is required for integration testing")
        
        if self._forum_rest_api_password is None:
            self.skipTest("FORUM_REST_API_PASSWORD not found. This is required for integration testing")
        
        conf = Config()
        conf.host = self._forum_rest_api_host
        conf.port = self._forum_rest_api_port
        conf.username = self._forum_rest_api_user
        conf.password = self._forum_rest_api_password
        self._api = api.Api(conf)


    def tearDown(self):
        pass


    def test_integration_get_http_listener(self):
        '''
            This needs a listner policy on the forum call test_integration_get_http_listener
        '''
        
        test_name = sys._getframe().f_code.co_name
        
        httpListenerPolicy = self._api.getForumSentryPolicy("httpListenerPolicies", test_name)
        
        self.assertTrue(isinstance(httpListenerPolicy, HttpListenerPolicy))
        self.assertEqual(httpListenerPolicy.name, test_name)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()