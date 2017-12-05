# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import forumsentry_api
from forumsentry_api.api.policiesip_ac_ls_api import PoliciesipACLsApi  # noqa: E501
from forumsentry_api.rest import ApiException


class TestPoliciesipACLsApi(unittest.TestCase):
    """PoliciesipACLsApi unit test stubs"""

    def setUp(self):
        self.api = forumsentry_api.api.policiesip_ac_ls_api.PoliciesipACLsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_or_update_policy(self):
        """Test case for create_or_update_policy

        creates or updates the IP ACL Policy  # noqa: E501
        """
        pass

    def test_create_policy(self):
        """Test case for create_policy

        creates a new IP ACL Policy  # noqa: E501
        """
        pass

    def test_get_policy(self):
        """Test case for get_policy

        gets the IP ACL Policy  # noqa: E501
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


if __name__ == '__main__':
    unittest.main()
