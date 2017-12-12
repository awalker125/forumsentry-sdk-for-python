'''
Created on 8 Dec 2017

@author: walandre
'''
import unittest
from forumsentry.errors import SerializationError
from forumsentry.errors import DeSerializationError
from forumsentry.errors import BadVerbError
from forumsentry.errors import ConfigError
from forumsentry.errors import NotSupportedError
from forumsentry.errors import InvalidTypeError

class TestErrors(unittest.TestCase):


    def setUp(self):
        self._BadVerbError = BadVerbError('test')
        self._SerializationError = SerializationError('test')
        self._DeSerializationError = DeSerializationError('test')
        self._ConfigError = ConfigError('test')
        self._NotSupportedError = NotSupportedError('test')
        self._InvalidTypeError = InvalidTypeError('test')


    def test_NotSupportedError_implements_str(self):
        self.assertTrue(self._NotSupportedError.__str__ is not object.__str__)

        string = self._NotSupportedError.__str__()

        self.assertIn('invalid', string)

    def test_InvalidTypeError_implements_str(self):
        self.assertTrue(self._InvalidTypeError.__str__ is not object.__str__)

        string = self._InvalidTypeError.__str__()

        self.assertIn('invalid', string)


    def test_ConfigError_implements_str(self):
        self.assertTrue(self._ConfigError.__str__ is not object.__str__)

        string = self._ConfigError.__str__()

        self.assertIn('invalid', string)

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