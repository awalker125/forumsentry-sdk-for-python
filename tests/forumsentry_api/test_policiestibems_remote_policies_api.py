# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import forumsentry_api
from .policiestibems_remote_policies_api import PoliciestibemsRemotePoliciesApi  # noqa: E501
from forumsentry_api.rest import ApiException


class TestPoliciestibemsRemotePoliciesApi(unittest.TestCase):
    """PoliciestibemsRemotePoliciesApi unit test stubs"""

    def setUp(self):
        self.api = .policiestibems_remote_policies_api.PoliciestibemsRemotePoliciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_or_update_policy(self):
        """Test case for create_or_update_policy

        creates or updates the policy  # noqa: E501
        """
        pass

    def test_create_policy(self):
        """Test case for create_policy

        creates a new policy  # noqa: E501
        """
        pass

    def test_create_policy_copy(self):
        """Test case for create_policy_copy

        creates a copy of the policy  # noqa: E501
        """
        pass

    def test_export_fsg(self):
        """Test case for export_fsg

        exports an fsg based on this policy to a file  # noqa: E501
        """
        pass

    def test_get_policy(self):
        """Test case for get_policy

        gets the policy  # noqa: E501
        """
        pass

    def test_get_policy_list(self):
        """Test case for get_policy_list

        returns a list of policies  # noqa: E501
        """
        pass

    def test_remove_policy(self):
        """Test case for remove_policy

        deletes the policy  # noqa: E501
        """
        pass

    def test_transfer_fsg(self):
        """Test case for transfer_fsg

        transfers an fsg based on this policy to the specified agent group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
