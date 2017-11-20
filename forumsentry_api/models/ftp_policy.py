# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FtpPolicy(object):
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

    attribute_map = {
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

    def __init__(self, name=None, description=None, ip=None, read_timeout_millis=None, use_device_ip=None, interface=None, port=None, acl_policy=None, error_template=None, enabled=None, comment=None):  # noqa: E501
        """FtpPolicy - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._ip = None
        self._read_timeout_millis = None
        self._use_device_ip = None
        self._interface = None
        self._port = None
        self._acl_policy = None
        self._error_template = None
        self._enabled = None
        self._comment = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ip is not None:
            self.ip = ip
        if read_timeout_millis is not None:
            self.read_timeout_millis = read_timeout_millis
        if use_device_ip is not None:
            self.use_device_ip = use_device_ip
        if interface is not None:
            self.interface = interface
        if port is not None:
            self.port = port
        if acl_policy is not None:
            self.acl_policy = acl_policy
        if error_template is not None:
            self.error_template = error_template
        if enabled is not None:
            self.enabled = enabled
        if comment is not None:
            self.comment = comment

    @property
    def name(self):
        """Gets the name of this FtpPolicy.  # noqa: E501


        :return: The name of this FtpPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FtpPolicy.


        :param name: The name of this FtpPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this FtpPolicy.  # noqa: E501


        :return: The description of this FtpPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FtpPolicy.


        :param description: The description of this FtpPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip(self):
        """Gets the ip of this FtpPolicy.  # noqa: E501


        :return: The ip of this FtpPolicy.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this FtpPolicy.


        :param ip: The ip of this FtpPolicy.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def read_timeout_millis(self):
        """Gets the read_timeout_millis of this FtpPolicy.  # noqa: E501


        :return: The read_timeout_millis of this FtpPolicy.  # noqa: E501
        :rtype: int
        """
        return self._read_timeout_millis

    @read_timeout_millis.setter
    def read_timeout_millis(self, read_timeout_millis):
        """Sets the read_timeout_millis of this FtpPolicy.


        :param read_timeout_millis: The read_timeout_millis of this FtpPolicy.  # noqa: E501
        :type: int
        """

        self._read_timeout_millis = read_timeout_millis

    @property
    def use_device_ip(self):
        """Gets the use_device_ip of this FtpPolicy.  # noqa: E501


        :return: The use_device_ip of this FtpPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._use_device_ip

    @use_device_ip.setter
    def use_device_ip(self, use_device_ip):
        """Sets the use_device_ip of this FtpPolicy.


        :param use_device_ip: The use_device_ip of this FtpPolicy.  # noqa: E501
        :type: bool
        """

        self._use_device_ip = use_device_ip

    @property
    def interface(self):
        """Gets the interface of this FtpPolicy.  # noqa: E501


        :return: The interface of this FtpPolicy.  # noqa: E501
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this FtpPolicy.


        :param interface: The interface of this FtpPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["WAN", "LAN"]  # noqa: E501
        if interface not in allowed_values:
            raise ValueError(
                "Invalid value for `interface` ({0}), must be one of {1}"  # noqa: E501
                .format(interface, allowed_values)
            )

        self._interface = interface

    @property
    def port(self):
        """Gets the port of this FtpPolicy.  # noqa: E501


        :return: The port of this FtpPolicy.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this FtpPolicy.


        :param port: The port of this FtpPolicy.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def acl_policy(self):
        """Gets the acl_policy of this FtpPolicy.  # noqa: E501


        :return: The acl_policy of this FtpPolicy.  # noqa: E501
        :rtype: str
        """
        return self._acl_policy

    @acl_policy.setter
    def acl_policy(self, acl_policy):
        """Sets the acl_policy of this FtpPolicy.


        :param acl_policy: The acl_policy of this FtpPolicy.  # noqa: E501
        :type: str
        """

        self._acl_policy = acl_policy

    @property
    def error_template(self):
        """Gets the error_template of this FtpPolicy.  # noqa: E501


        :return: The error_template of this FtpPolicy.  # noqa: E501
        :rtype: str
        """
        return self._error_template

    @error_template.setter
    def error_template(self, error_template):
        """Sets the error_template of this FtpPolicy.


        :param error_template: The error_template of this FtpPolicy.  # noqa: E501
        :type: str
        """

        self._error_template = error_template

    @property
    def enabled(self):
        """Gets the enabled of this FtpPolicy.  # noqa: E501


        :return: The enabled of this FtpPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this FtpPolicy.


        :param enabled: The enabled of this FtpPolicy.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def comment(self):
        """Gets the comment of this FtpPolicy.  # noqa: E501


        :return: The comment of this FtpPolicy.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this FtpPolicy.


        :param comment: The comment of this FtpPolicy.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if not isinstance(other, FtpPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
