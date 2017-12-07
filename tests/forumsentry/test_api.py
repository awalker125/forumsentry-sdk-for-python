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

    



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()