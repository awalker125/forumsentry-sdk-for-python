# pylint: disable-all
import json
import os
import pprint
import unittest
#from unittest.mock import MagicMock

#app imports
import forumsentry.controller.helper as helper



class TestCircleCIApi(unittest.TestCase):

#    def setUp(self):

# 
#     def loadMock(self, filename):
#         """helper function to open mock responses"""
#         filename = 'tests/mocks/{0}'.format(filename)
# 
#         with open(filename, 'r') as f:
#             self.c._request = MagicMock(return_value=f.read())

    def test_housestark(self):

        self.assertEqual('winter is coming', helper.housestark())



