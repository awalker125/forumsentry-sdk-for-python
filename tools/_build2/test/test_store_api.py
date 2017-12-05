# coding: utf-8

"""
    Swagger Petstore

    This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import forumsentry_api
from forumsentry_api.rest import ApiException
from forumsentry_api.apis.store_api import StoreApi


class TestStoreApi(unittest.TestCase):
    """ StoreApi unit test stubs """

    def setUp(self):
        self.api = forumsentry_api.apis.store_api.StoreApi()

    def tearDown(self):
        pass

    def test_delete_order(self):
        """
        Test case for delete_order

        Delete purchase order by ID
        """
        pass

    def test_get_inventory(self):
        """
        Test case for get_inventory

        Returns pet inventories by status
        """
        pass

    def test_get_order_by_id(self):
        """
        Test case for get_order_by_id

        Find purchase order by ID
        """
        pass

    def test_place_order(self):
        """
        Test case for place_order

        Place an order for a pet
        """
        pass


if __name__ == '__main__':
    unittest.main()
