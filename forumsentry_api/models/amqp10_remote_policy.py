# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Amqp10RemotePolicy(object):
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
        'use_ssl': 'bool',
        'idle_timeout_millis': 'int',
        'credential_source': 'str',
        'user_policy': 'str',
        'ssl_policy': 'str',
        'transfer_timeout_millis': 'int',
        'name': 'str',
        'sasl_mechanism': 'str',
        'description': 'str',
        'remote_port': 'int',
        'enabled': 'bool',
        'remote_server': 'str',
        'process_response': 'bool'
    }

    attribute_map = {
        'use_ssl': 'useSsl',
        'idle_timeout_millis': 'idleTimeoutMillis',
        'credential_source': 'credentialSource',
        'user_policy': 'userPolicy',
        'ssl_policy': 'sslPolicy',
        'transfer_timeout_millis': 'transferTimeoutMillis',
        'name': 'name',
        'sasl_mechanism': 'saslMechanism',
        'description': 'description',
        'remote_port': 'remotePort',
        'enabled': 'enabled',
        'remote_server': 'remoteServer',
        'process_response': 'processResponse'
    }

    def __init__(self, use_ssl=None, idle_timeout_millis=None, credential_source=None, user_policy=None, ssl_policy=None, transfer_timeout_millis=None, name=None, sasl_mechanism=None, description=None, remote_port=None, enabled=None, remote_server=None, process_response=None):  # noqa: E501
        """Amqp10RemotePolicy - a model defined in Swagger"""  # noqa: E501

        self._use_ssl = None
        self._idle_timeout_millis = None
        self._credential_source = None
        self._user_policy = None
        self._ssl_policy = None
        self._transfer_timeout_millis = None
        self._name = None
        self._sasl_mechanism = None
        self._description = None
        self._remote_port = None
        self._enabled = None
        self._remote_server = None
        self._process_response = None
        self.discriminator = None

        if use_ssl is not None:
            self.use_ssl = use_ssl
        if idle_timeout_millis is not None:
            self.idle_timeout_millis = idle_timeout_millis
        if credential_source is not None:
            self.credential_source = credential_source
        if user_policy is not None:
            self.user_policy = user_policy
        if ssl_policy is not None:
            self.ssl_policy = ssl_policy
        if transfer_timeout_millis is not None:
            self.transfer_timeout_millis = transfer_timeout_millis
        if name is not None:
            self.name = name
        if sasl_mechanism is not None:
            self.sasl_mechanism = sasl_mechanism
        if description is not None:
            self.description = description
        if remote_port is not None:
            self.remote_port = remote_port
        if enabled is not None:
            self.enabled = enabled
        if remote_server is not None:
            self.remote_server = remote_server
        if process_response is not None:
            self.process_response = process_response

    @property
    def use_ssl(self):
        """Gets the use_ssl of this Amqp10RemotePolicy.  # noqa: E501


        :return: The use_ssl of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this Amqp10RemotePolicy.


        :param use_ssl: The use_ssl of this Amqp10RemotePolicy.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def idle_timeout_millis(self):
        """Gets the idle_timeout_millis of this Amqp10RemotePolicy.  # noqa: E501


        :return: The idle_timeout_millis of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._idle_timeout_millis

    @idle_timeout_millis.setter
    def idle_timeout_millis(self, idle_timeout_millis):
        """Sets the idle_timeout_millis of this Amqp10RemotePolicy.


        :param idle_timeout_millis: The idle_timeout_millis of this Amqp10RemotePolicy.  # noqa: E501
        :type: int
        """

        self._idle_timeout_millis = idle_timeout_millis

    @property
    def credential_source(self):
        """Gets the credential_source of this Amqp10RemotePolicy.  # noqa: E501


        :return: The credential_source of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._credential_source

    @credential_source.setter
    def credential_source(self, credential_source):
        """Sets the credential_source of this Amqp10RemotePolicy.


        :param credential_source: The credential_source of this Amqp10RemotePolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["STATIC", "DYNAMIC", "PROPAGATE"]  # noqa: E501
        if credential_source not in allowed_values:
            raise ValueError(
                "Invalid value for `credential_source` ({0}), must be one of {1}"  # noqa: E501
                .format(credential_source, allowed_values)
            )

        self._credential_source = credential_source

    @property
    def user_policy(self):
        """Gets the user_policy of this Amqp10RemotePolicy.  # noqa: E501


        :return: The user_policy of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._user_policy

    @user_policy.setter
    def user_policy(self, user_policy):
        """Sets the user_policy of this Amqp10RemotePolicy.


        :param user_policy: The user_policy of this Amqp10RemotePolicy.  # noqa: E501
        :type: str
        """

        self._user_policy = user_policy

    @property
    def ssl_policy(self):
        """Gets the ssl_policy of this Amqp10RemotePolicy.  # noqa: E501


        :return: The ssl_policy of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._ssl_policy

    @ssl_policy.setter
    def ssl_policy(self, ssl_policy):
        """Sets the ssl_policy of this Amqp10RemotePolicy.


        :param ssl_policy: The ssl_policy of this Amqp10RemotePolicy.  # noqa: E501
        :type: str
        """

        self._ssl_policy = ssl_policy

    @property
    def transfer_timeout_millis(self):
        """Gets the transfer_timeout_millis of this Amqp10RemotePolicy.  # noqa: E501


        :return: The transfer_timeout_millis of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._transfer_timeout_millis

    @transfer_timeout_millis.setter
    def transfer_timeout_millis(self, transfer_timeout_millis):
        """Sets the transfer_timeout_millis of this Amqp10RemotePolicy.


        :param transfer_timeout_millis: The transfer_timeout_millis of this Amqp10RemotePolicy.  # noqa: E501
        :type: int
        """

        self._transfer_timeout_millis = transfer_timeout_millis

    @property
    def name(self):
        """Gets the name of this Amqp10RemotePolicy.  # noqa: E501


        :return: The name of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Amqp10RemotePolicy.


        :param name: The name of this Amqp10RemotePolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sasl_mechanism(self):
        """Gets the sasl_mechanism of this Amqp10RemotePolicy.  # noqa: E501


        :return: The sasl_mechanism of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._sasl_mechanism

    @sasl_mechanism.setter
    def sasl_mechanism(self, sasl_mechanism):
        """Sets the sasl_mechanism of this Amqp10RemotePolicy.


        :param sasl_mechanism: The sasl_mechanism of this Amqp10RemotePolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "ANONYMOUS", "PLAIN", "CRAM_MD5", "EXTERNAL"]  # noqa: E501
        if sasl_mechanism not in allowed_values:
            raise ValueError(
                "Invalid value for `sasl_mechanism` ({0}), must be one of {1}"  # noqa: E501
                .format(sasl_mechanism, allowed_values)
            )

        self._sasl_mechanism = sasl_mechanism

    @property
    def description(self):
        """Gets the description of this Amqp10RemotePolicy.  # noqa: E501


        :return: The description of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Amqp10RemotePolicy.


        :param description: The description of this Amqp10RemotePolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def remote_port(self):
        """Gets the remote_port of this Amqp10RemotePolicy.  # noqa: E501


        :return: The remote_port of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        """Sets the remote_port of this Amqp10RemotePolicy.


        :param remote_port: The remote_port of this Amqp10RemotePolicy.  # noqa: E501
        :type: int
        """

        self._remote_port = remote_port

    @property
    def enabled(self):
        """Gets the enabled of this Amqp10RemotePolicy.  # noqa: E501


        :return: The enabled of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Amqp10RemotePolicy.


        :param enabled: The enabled of this Amqp10RemotePolicy.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def remote_server(self):
        """Gets the remote_server of this Amqp10RemotePolicy.  # noqa: E501


        :return: The remote_server of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._remote_server

    @remote_server.setter
    def remote_server(self, remote_server):
        """Sets the remote_server of this Amqp10RemotePolicy.


        :param remote_server: The remote_server of this Amqp10RemotePolicy.  # noqa: E501
        :type: str
        """

        self._remote_server = remote_server

    @property
    def process_response(self):
        """Gets the process_response of this Amqp10RemotePolicy.  # noqa: E501


        :return: The process_response of this Amqp10RemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._process_response

    @process_response.setter
    def process_response(self, process_response):
        """Sets the process_response of this Amqp10RemotePolicy.


        :param process_response: The process_response of this Amqp10RemotePolicy.  # noqa: E501
        :type: bool
        """

        self._process_response = process_response

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
        if not isinstance(other, Amqp10RemotePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
