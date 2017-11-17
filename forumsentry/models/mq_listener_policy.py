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

from pprint import pformat
from six import iteritems
import re


class MqListenerPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, acl_policy=None, error_template=None, enabled=None, comment=None):
        """
        MqListenerPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'acl_policy': 'str',
            'error_template': 'str',
            'enabled': 'bool',
            'comment': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'acl_policy': 'aclPolicy',
            'error_template': 'errorTemplate',
            'enabled': 'enabled',
            'comment': 'comment'
        }

        self._name = name
        self._description = description
        self._acl_policy = acl_policy
        self._error_template = error_template
        self._enabled = enabled
        self._comment = comment

    @property
    def name(self):
        """
        Gets the name of this MqListenerPolicy.


        :return: The name of this MqListenerPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MqListenerPolicy.


        :param name: The name of this MqListenerPolicy.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this MqListenerPolicy.


        :return: The description of this MqListenerPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MqListenerPolicy.


        :param description: The description of this MqListenerPolicy.
        :type: str
        """

        self._description = description

    @property
    def acl_policy(self):
        """
        Gets the acl_policy of this MqListenerPolicy.


        :return: The acl_policy of this MqListenerPolicy.
        :rtype: str
        """
        return self._acl_policy

    @acl_policy.setter
    def acl_policy(self, acl_policy):
        """
        Sets the acl_policy of this MqListenerPolicy.


        :param acl_policy: The acl_policy of this MqListenerPolicy.
        :type: str
        """

        self._acl_policy = acl_policy

    @property
    def error_template(self):
        """
        Gets the error_template of this MqListenerPolicy.


        :return: The error_template of this MqListenerPolicy.
        :rtype: str
        """
        return self._error_template

    @error_template.setter
    def error_template(self, error_template):
        """
        Sets the error_template of this MqListenerPolicy.


        :param error_template: The error_template of this MqListenerPolicy.
        :type: str
        """

        self._error_template = error_template

    @property
    def enabled(self):
        """
        Gets the enabled of this MqListenerPolicy.


        :return: The enabled of this MqListenerPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this MqListenerPolicy.


        :param enabled: The enabled of this MqListenerPolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def comment(self):
        """
        Gets the comment of this MqListenerPolicy.


        :return: The comment of this MqListenerPolicy.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this MqListenerPolicy.


        :param comment: The comment of this MqListenerPolicy.
        :type: str
        """

        self._comment = comment

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
