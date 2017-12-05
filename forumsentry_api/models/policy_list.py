# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from forumsentry_api.models.policy import Policy  # noqa: F401,E501


class PolicyList(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'policy': 'list[Policy]'
    }

    attribute_map = {
        'policy': 'policy'
    }

    def __init__(self, policy=None):  # noqa: E501
        """PolicyList - a model defined in Swagger"""  # noqa: E501

        self._policy = None
        self.discriminator = None

        if policy is not None:
            self.policy = policy

    @property
    def policy(self):
        """Gets the policy of this PolicyList.  # noqa: E501


        :return: The policy of this PolicyList.  # noqa: E501
        :rtype: list[Policy]
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PolicyList.


        :param policy: The policy of this PolicyList.  # noqa: E501
        :type: list[Policy]
        """

        self._policy = policy

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
