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


class SmtpListenerPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, ip=None, read_timeout_millis=None, use_device_ip=None, interface=None, port=None, acl_policy=None, error_template=None, enabled=None, comment=None):
        """
        SmtpListenerPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'ip': 'str',
            'read_timeout_millis': 'int',
            'use_device_ip': 'bool',
            'interface': 'str',
            'port': 'int',
            'acl_policy': 'str',
            'error_template': 'str',
            'enabled': 'bool',
            'comment': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'ip': 'ip',
            'read_timeout_millis': 'readTimeoutMillis',
            'use_device_ip': 'useDeviceIp',
            'interface': 'interface',
            'port': 'port',
            'acl_policy': 'aclPolicy',
            'error_template': 'errorTemplate',
            'enabled': 'enabled',
            'comment': 'comment'
        }

        self._name = name
        self._description = description
        self._ip = ip
        self._read_timeout_millis = read_timeout_millis
        self._use_device_ip = use_device_ip
        self._interface = interface
        self._port = port
        self._acl_policy = acl_policy
        self._error_template = error_template
        self._enabled = enabled
        self._comment = comment

    @property
    def name(self):
        """
        Gets the name of this SmtpListenerPolicy.


        :return: The name of this SmtpListenerPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SmtpListenerPolicy.


        :param name: The name of this SmtpListenerPolicy.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SmtpListenerPolicy.


        :return: The description of this SmtpListenerPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SmtpListenerPolicy.


        :param description: The description of this SmtpListenerPolicy.
        :type: str
        """

        self._description = description

    @property
    def ip(self):
        """
        Gets the ip of this SmtpListenerPolicy.


        :return: The ip of this SmtpListenerPolicy.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this SmtpListenerPolicy.


        :param ip: The ip of this SmtpListenerPolicy.
        :type: str
        """

        self._ip = ip

    @property
    def read_timeout_millis(self):
        """
        Gets the read_timeout_millis of this SmtpListenerPolicy.


        :return: The read_timeout_millis of this SmtpListenerPolicy.
        :rtype: int
        """
        return self._read_timeout_millis

    @read_timeout_millis.setter
    def read_timeout_millis(self, read_timeout_millis):
        """
        Sets the read_timeout_millis of this SmtpListenerPolicy.


        :param read_timeout_millis: The read_timeout_millis of this SmtpListenerPolicy.
        :type: int
        """

        self._read_timeout_millis = read_timeout_millis

    @property
    def use_device_ip(self):
        """
        Gets the use_device_ip of this SmtpListenerPolicy.


        :return: The use_device_ip of this SmtpListenerPolicy.
        :rtype: bool
        """
        return self._use_device_ip

    @use_device_ip.setter
    def use_device_ip(self, use_device_ip):
        """
        Sets the use_device_ip of this SmtpListenerPolicy.


        :param use_device_ip: The use_device_ip of this SmtpListenerPolicy.
        :type: bool
        """

        self._use_device_ip = use_device_ip

    @property
    def interface(self):
        """
        Gets the interface of this SmtpListenerPolicy.


        :return: The interface of this SmtpListenerPolicy.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """
        Sets the interface of this SmtpListenerPolicy.


        :param interface: The interface of this SmtpListenerPolicy.
        :type: str
        """
        allowed_values = ["WAN", "LAN"]
        if interface not in allowed_values:
            raise ValueError(
                "Invalid value for `interface` ({0}), must be one of {1}"
                .format(interface, allowed_values)
            )

        self._interface = interface

    @property
    def port(self):
        """
        Gets the port of this SmtpListenerPolicy.


        :return: The port of this SmtpListenerPolicy.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this SmtpListenerPolicy.


        :param port: The port of this SmtpListenerPolicy.
        :type: int
        """

        self._port = port

    @property
    def acl_policy(self):
        """
        Gets the acl_policy of this SmtpListenerPolicy.


        :return: The acl_policy of this SmtpListenerPolicy.
        :rtype: str
        """
        return self._acl_policy

    @acl_policy.setter
    def acl_policy(self, acl_policy):
        """
        Sets the acl_policy of this SmtpListenerPolicy.


        :param acl_policy: The acl_policy of this SmtpListenerPolicy.
        :type: str
        """

        self._acl_policy = acl_policy

    @property
    def error_template(self):
        """
        Gets the error_template of this SmtpListenerPolicy.


        :return: The error_template of this SmtpListenerPolicy.
        :rtype: str
        """
        return self._error_template

    @error_template.setter
    def error_template(self, error_template):
        """
        Sets the error_template of this SmtpListenerPolicy.


        :param error_template: The error_template of this SmtpListenerPolicy.
        :type: str
        """

        self._error_template = error_template

    @property
    def enabled(self):
        """
        Gets the enabled of this SmtpListenerPolicy.


        :return: The enabled of this SmtpListenerPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SmtpListenerPolicy.


        :param enabled: The enabled of this SmtpListenerPolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def comment(self):
        """
        Gets the comment of this SmtpListenerPolicy.


        :return: The comment of this SmtpListenerPolicy.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this SmtpListenerPolicy.


        :param comment: The comment of this SmtpListenerPolicy.
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
