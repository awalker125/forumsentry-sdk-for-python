# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import forumsentry_api
from forumsentry_api.api.configurationimport_api import ConfigurationimportApi  # noqa: E501
from forumsentry_api.rest import ApiException


class TestConfigurationimportApi(unittest.TestCase):
    """ConfigurationimportApi unit test stubs"""

    def setUp(self):
        self.api = forumsentry_api.api.configurationimport_api.ConfigurationimportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_import_configuration(self):
        """Test case for import_configuration

        imports a configuration file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
