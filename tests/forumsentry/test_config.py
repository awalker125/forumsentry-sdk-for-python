'''
Created on 8 Dec 2017

@author: walandre
'''
import unittest
from forumsentry.config import Config
import os

class TestConfig(unittest.TestCase):


    def setUp(self):
        self._config = Config()


    def tearDown(self):
        pass


    def testConfig_constructor(self):
        config = Config()
        self.assertTrue(isinstance(config,Config))

    def testConfig_none_default_constructor(self):
        config = Config(host="notlocalhost", 
                        port=21, 
                        protocol="https", 
                        context="/rest", 
                        username="admin123", 
                        password="password_123", 
                        verify_ssl=True, 
                        ssl_ca_file="doesntexist")
        self.assertTrue(isinstance(config,Config))
        self.assertEqual(config.host,"notlocalhost")
        self.assertEqual(config.port,21)
        self.assertEqual(config.protocol,"https")
        self.assertEqual(config.context,"/rest")
        self.assertEqual(config.username,"admin123")
        self.assertEqual(config.password,"password_123")
        self.assertEqual(config.verify_ssl,True)
        self.assertEqual(config.ssl_ca_file,"doesntexist")
        self.assertEqual(config.forumsentry_url,"https://notlocalhost:21/rest")

    def testConfig_getter_setter(self):
        config = Config()
        
#         config.basic_authentication_header = "test"
#         self.assertEqual(config.basic_authentication_header,"test")
#       
        #Run this first to test empty username and password warnings
        self.assertEqual(config.basic_authentication_header,"Basic Og==")
  
        config.context = "/test"
        self.assertEqual(config.context,"/test")

        config.host = "test"
        self.assertEqual(config.host,"test")

        

        config.password = "test"
        self.assertEqual(config.password,"test")

        config.username = "test"
        self.assertEqual(config.username,"test")

        self.assertEqual(config.basic_authentication_header,"Basic dGVzdDp0ZXN0")
  

        config.port = 60
        self.assertEqual(config.port,60)
        
        config.protocol = "test"
        self.assertEqual(config.protocol,"test")
        
        config.verify_ssl = True
        self.assertEqual(config.verify_ssl,True)
        
        config.ssl_ca_file = "test"
        self.assertEqual(config.ssl_ca_file,"test")
        
        self.assertEqual(config.forumsentry_url,"test://test:60/test")

        config.debug = True
        self.assertEqual(config.debug,True)
        
        config.debug = False
        self.assertEqual(config.debug,False)
        
        #Turn on file logging
        config.logger_file = "test.log"
        self.assertEqual(config.logger_file,"test.log")
        
        #Turn off file logging
        config.logger_file = None
        self.assertEqual(config.logger_file,None)
        
        #Turn on stream logging
        config.logger_stream = True
        self.assertEqual(config.logger_stream,True)
        
        #Turn off stream logging
        config.logger_stream = False
        self.assertEqual(config.logger_stream,False)
        
        config.logger_format = "test"
        self.assertEqual(config.logger_format,"test")       
        

    def testConfig_FSSENTRY_DEBUG(self):
        
        os.environ["FSSENTRY_DEBUG"] = "true"
        
        conf = Config()
        
        os.unsetenv("FSSENTRY_DEBUG")
        
        self.assertTrue(conf.debug)
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()