'''
Created on 8 Dec 2017

@author: walandre
'''
import unittest
from forumsentry.errors import SerializationError, DeSerializationError
from forumsentry.errors import BadVerbError


class TestErrors(unittest.TestCase):


    def setUp(self):
        self._BadVerbError = BadVerbError('test')
        self._SerializationError = SerializationError('test')
        self._DeSerializationError = DeSerializationError('test')


    def test_BadVerbError_implements_str(self):
        self.assertTrue(self._BadVerbError.__str__ is not object.__str__)

        string = self._BadVerbError.__str__()

        self.assertIn('invalid', string)
 
    def test_SerializationError_implements_str(self):
        self.assertTrue(self._SerializationError.__str__ is not object.__str__)

        string = self._SerializationError.__str__()

        self.assertIn('invalid', string)       
    
    def test_DeSerializationError_implements_str(self):
        self.assertTrue(self._DeSerializationError.__str__ is not object.__str__)

        string = self._DeSerializationError.__str__()

        self.assertIn('invalid', string)  

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testErrors']
    unittest.main()