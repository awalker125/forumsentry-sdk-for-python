'''
Created on 20 Nov 2017

@author: walandre
'''
import unittest
import forumsentry.helper as helper


class Test(unittest.TestCase):

 

    def setUp(self):
        self.helper = helper.Helper()


    def tearDown(self):
        pass


    def testStark(self):
        self.assertEqual("Winter is coming", self.helper.stark())
    
    def testLanister(self):
        self.assertEqual("A Lanister always pays his debts", self.helper.lanister())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStart']
    unittest.main()