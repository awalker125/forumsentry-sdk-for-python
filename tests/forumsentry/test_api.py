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



class TestApi(unittest.TestCase):

 

    def setUp(self):
        self._api = api.Api()


    def _mock_response(
            self,
            status=200,
            test_name=None,
            raise_for_status=None):
        """
        since we typically test a bunch of different
        requests calls for a service, we are going to do
        a lot of mock responses, so its usually a good idea
        to have a helper function that builds these things
        """
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
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
        
        test_name = sys._getframe().f_code.co_name
        
        #mock_get.return_value  = self.loadMock(test_name)
        mock_resp = self._mock_response(test_name=test_name)
        mock_get.return_value = mock_resp
        
        httpListenerPolicy = self._api.getForumSentryPolicy("httpListenerPolicies", "bill")
        
        self.assertTrue(isinstance(httpListenerPolicy, HttpListenerPolicy))
        self.assertEqual(httpListenerPolicy.name, "bill")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()