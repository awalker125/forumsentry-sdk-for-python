'''
Created on 8 Dec 2017

@author: walandre
'''
import unittest
from forumsentry.config import Config


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
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()