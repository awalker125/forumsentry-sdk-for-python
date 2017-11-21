# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
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
from forumsentry_api.apis.policiesamqp_listener_policies_api import PoliciesamqpListenerPoliciesApi


class TestPoliciesamqpListenerPoliciesApi(unittest.TestCase):
    """ PoliciesamqpListenerPoliciesApi unit test stubs """

    def setUp(self):
        self.api = forumsentry_api.apis.policiesamqp_listener_policies_api.PoliciesamqpListenerPoliciesApi()

    def tearDown(self):
        pass

    def test_create_or_update_policy(self):
        """
        Test case for create_or_update_policy

        creates or updates the policy
        """
        pass

    def test_create_policy(self):
        """
        Test case for create_policy

        creates a new policy
        """
        pass

    def test_create_policy_copy(self):
        """
        Test case for create_policy_copy

        creates a copy of the policy
        """
        pass

    def test_export_fsg(self):
        """
        Test case for export_fsg

        exports an fsg based on this policy to a file
        """
        pass

    def test_get_policy(self):
        """
        Test case for get_policy

        gets the policy
        """
        pass

    def test_get_policy_list(self):
        """
        Test case for get_policy_list

        returns a list of policies
        """
        pass

    def test_remove_policy(self):
        """
        Test case for remove_policy

        deletes the policy
        """
        pass

    def test_transfer_fsg(self):
        """
        Test case for transfer_fsg

        transfers an fsg based on this policy to the specified agent group
        """
        pass


if __name__ == '__main__':
    unittest.main()
