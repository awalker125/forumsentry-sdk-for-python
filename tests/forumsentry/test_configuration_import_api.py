'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import os
import mock
import sys
import string
import random

from forumsentry import configuration_import_api
from requests.exceptions import HTTPError
from tests.forumsentry import helper



class TestApi(unittest.TestCase):

    def setUp(self):
        self._api = configuration_import_api.ConfigurationImportApi()
        
        self._unique_id = helper.id_generator()
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

        
    @mock.patch("forumsentry.api.requests.post")
    def test_configuration_import_api_import_fsg1(self, mock_post):
        '''
            Tests when requests gets a successful response from forum
        '''
        test_name = sys._getframe().f_code.co_name
         
        #mock_get.return_value  = self.loadMock(test_name)
        mock_resp = self._mock_response(test_name=test_name)
        mock_post.return_value = mock_resp
        
        password = test_name
        whereami = os.path.dirname(__file__)  
        
        filename = '{0}/../mocks/{1}'.format(whereami,test_name)
         
        import_result = self._api.import_fsg(filename, password)
         
        self.assertTrue(import_result)


    def test_configuration_import_api_import_fsg2(self):
        '''
            Tests when the import file doesnt exist
        '''
        test_name = sys._getframe().f_code.co_name
        
        password = test_name
        filename = 'doesntexist'
        with self.assertRaises(IOError) as e: 
            self._api.import_fsg(filename, password)
         

        self.assertIn('not found', e.exception.message) 

 
 
    @mock.patch("forumsentry.api.requests.post")
    def test_configuration_import_api_import_fsg3(self, mock_post):
        '''
            Tests when requests gets a 500 response from forum
        '''
        test_name = sys._getframe().f_code.co_name
          
        password = test_name
        whereami = os.path.dirname(__file__)  
        
        filename = '{0}/../mocks/{1}'.format(whereami,test_name)
         
        
        mock_resp = self._mock_response(status=500,raise_for_status="internal error")
        mock_post.return_value = mock_resp
          
        with self.assertRaises(HTTPError) as e: 
            text = self._api.import_fsg(filename, password)
          

        self.assertEqual(500, e.exception.response.status_code)
        self.assertIn('internal error', e.exception.message)
 



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()