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
from requests.exceptions import HTTPError



class TestApi(unittest.TestCase):

 

    def setUp(self):
        self._api = api.Api()


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
                mock_resp.json.return_value = f.read()

        return mock_resp


    def tearDown(self):
        pass

    def test_bad_verb(self):

        with self.assertRaises(BadVerbError) as e:
            self._api._request('BAD', 'dummy')

        self.assertEqual('BAD', e.exception.argument)
        self.assertIn('DELETE', e.exception.message)


    @mock.patch("forumsentry.api.requests.get")
    def test_getForumSentryPolicy1(self, mock_get):
        '''
            Tests the getForumSentryPolicy method when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
        
        #mock_get.return_value  = self.loadMock(test_name)
        mock_resp = self._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
        
        httpListenerPolicy = self._api.getForumSentryPolicy("httpListenerPolicies", "bill")
        
        self.assertTrue(isinstance(httpListenerPolicy, HttpListenerPolicy))
        self.assertEqual(httpListenerPolicy.name, "bill")

    @mock.patch("forumsentry.api.requests.get")
    def test_getForumSentryPolicy2(self, mock_get):
        '''
            Tests the getForumSentryPolicy method when requests gets a 404 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
        
        mock_resp = self._mock_response(status=404,raise_for_status="bill not found")
        mock_get.return_value = mock_resp
        
        httpListenerPolicy = self._api.getForumSentryPolicy("httpListenerPolicies", "bill")  
        
        self.assertEqual(httpListenerPolicy, None)

        
    @mock.patch("forumsentry.api.requests.get")
    def test_getForumSentryPolicy3(self, mock_get):
        '''
            Tests the getForumSentryPolicy method when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
        
        mock_resp = self._mock_response(status=500,raise_for_status="internal error")
        mock_get.return_value = mock_resp
        
        with self.assertRaises(HTTPError) as e: 
            httpListenerPolicy = self._api.getForumSentryPolicy("httpListenerPolicies", "bill")  
        
       #print e.exception.message
        self.assertEqual(500, e.exception.response.status_code)
        self.assertIn('internal error', e.exception.message)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()