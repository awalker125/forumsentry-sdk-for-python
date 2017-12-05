# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SftpListenerPolicy(object):
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
        'read_timeout_millis': 'int',
        'ip': 'str',
        'port': 'int',
        'use_device_ip': 'bool',
        'name': 'str',
        'description': 'str',
        'enabled': 'bool',
        'interface': 'str'
    }

    attribute_map = {
        'read_timeout_millis': 'readTimeoutMillis',
        'ip': 'ip',
        'port': 'port',
        'use_device_ip': 'useDeviceIp',
        'name': 'name',
        'description': 'description',
        'enabled': 'enabled',
        'interface': 'interface'
    }

    def __init__(self, read_timeout_millis=None, ip=None, port=None, use_device_ip=None, name=None, description=None, enabled=None, interface=None):  # noqa: E501
        """SftpListenerPolicy - a model defined in Swagger"""  # noqa: E501

        self._read_timeout_millis = None
        self._ip = None
        self._port = None
        self._use_device_ip = None
        self._name = None
        self._description = None
        self._enabled = None
        self._interface = None
        self.discriminator = None

        if read_timeout_millis is not None:
            self.read_timeout_millis = read_timeout_millis
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if use_device_ip is not None:
            self.use_device_ip = use_device_ip
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if interface is not None:
            self.interface = interface

    @property
    def read_timeout_millis(self):
        """Gets the read_timeout_millis of this SftpListenerPolicy.  # noqa: E501


        :return: The read_timeout_millis of this SftpListenerPolicy.  # noqa: E501
        :rtype: int
        """
        return self._read_timeout_millis

    @read_timeout_millis.setter
    def read_timeout_millis(self, read_timeout_millis):
        """Sets the read_timeout_millis of this SftpListenerPolicy.


        :param read_timeout_millis: The read_timeout_millis of this SftpListenerPolicy.  # noqa: E501
        :type: int
        """

        self._read_timeout_millis = read_timeout_millis

    @property
    def ip(self):
        """Gets the ip of this SftpListenerPolicy.  # noqa: E501


        :return: The ip of this SftpListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SftpListenerPolicy.


        :param ip: The ip of this SftpListenerPolicy.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def port(self):
        """Gets the port of this SftpListenerPolicy.  # noqa: E501


        :return: The port of this SftpListenerPolicy.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SftpListenerPolicy.


        :param port: The port of this SftpListenerPolicy.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def use_device_ip(self):
        """Gets the use_device_ip of this SftpListenerPolicy.  # noqa: E501


        :return: The use_device_ip of this SftpListenerPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._use_device_ip

    @use_device_ip.setter
    def use_device_ip(self, use_device_ip):
        """Sets the use_device_ip of this SftpListenerPolicy.


        :param use_device_ip: The use_device_ip of this SftpListenerPolicy.  # noqa: E501
        :type: bool
        """

        self._use_device_ip = use_device_ip

    @property
    def name(self):
        """Gets the name of this SftpListenerPolicy.  # noqa: E501


        :return: The name of this SftpListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SftpListenerPolicy.


        :param name: The name of this SftpListenerPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this SftpListenerPolicy.  # noqa: E501


        :return: The description of this SftpListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SftpListenerPolicy.


        :param description: The description of this SftpListenerPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this SftpListenerPolicy.  # noqa: E501


        :return: The enabled of this SftpListenerPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SftpListenerPolicy.


        :param enabled: The enabled of this SftpListenerPolicy.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def interface(self):
        """Gets the interface of this SftpListenerPolicy.  # noqa: E501


        :return: The interface of this SftpListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this SftpListenerPolicy.


        :param interface: The interface of this SftpListenerPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["WAN", "LAN"]  # noqa: E501
        if interface not in allowed_values:
            raise ValueError(
                "Invalid value for `interface` ({0}), must be one of {1}"  # noqa: E501
                .format(interface, allowed_values)
            )

        self._interface = interface

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
        if not isinstance(other, SftpListenerPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
