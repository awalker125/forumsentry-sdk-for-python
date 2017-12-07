'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
from forumsentry import api


class Test(unittest.TestCase):

 

    def setUp(self):
        self._api = api.Api()


    def tearDown(self):
        pass


    def testhelloWorld(self):
        self.assertEqual("helloWorld", self._api.helloWorld())
    



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()