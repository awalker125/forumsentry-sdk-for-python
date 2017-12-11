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


    def testConfigConstructor(self):
        config = Config()
        self.assertTrue(isinstance(config,Config))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()