# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class S3RemotePolicy1(object):
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
        'use_basic_auth': 'bool',
        'proxy_policy': 'str',
        'ssl_initiation_policy': 'str',
        'tcp_connection_timeout': 'int',
        'http_authentication_user_policy': 'str',
        'use_chunking': 'bool',
        'tcp_read_timeout': 'int',
        'name': 'str',
        'enable_ssl': 'bool',
        'remote_authentication': 'str',
        'remote_port': 'int',
        'enabled': 'bool',
        'remote_server': 'str',
        'process_response': 'bool'
    }

    attribute_map = {
        'use_basic_auth': 'useBasicAuth',
        'proxy_policy': 'proxyPolicy',
        'ssl_initiation_policy': 'SSLInitiationPolicy',
        'tcp_connection_timeout': 'tcpConnectionTimeout',
        'http_authentication_user_policy': 'httpAuthenticationUserPolicy',
        'use_chunking': 'useChunking',
        'tcp_read_timeout': 'tcpReadTimeout',
        'name': 'name',
        'enable_ssl': 'enableSSL',
        'remote_authentication': 'remoteAuthentication',
        'remote_port': 'remotePort',
        'enabled': 'enabled',
        'remote_server': 'remoteServer',
        'process_response': 'processResponse'
    }

    def __init__(self, use_basic_auth=None, proxy_policy=None, ssl_initiation_policy=None, tcp_connection_timeout=None, http_authentication_user_policy=None, use_chunking=None, tcp_read_timeout=None, name=None, enable_ssl=None, remote_authentication=None, remote_port=None, enabled=None, remote_server=None, process_response=None):  # noqa: E501
        """S3RemotePolicy1 - a model defined in Swagger"""  # noqa: E501

        self._use_basic_auth = None
        self._proxy_policy = None
        self._ssl_initiation_policy = None
        self._tcp_connection_timeout = None
        self._http_authentication_user_policy = None
        self._use_chunking = None
        self._tcp_read_timeout = None
        self._name = None
        self._enable_ssl = None
        self._remote_authentication = None
        self._remote_port = None
        self._enabled = None
        self._remote_server = None
        self._process_response = None
        self.discriminator = None

        if use_basic_auth is not None:
            self.use_basic_auth = use_basic_auth
        if proxy_policy is not None:
            self.proxy_policy = proxy_policy
        if ssl_initiation_policy is not None:
            self.ssl_initiation_policy = ssl_initiation_policy
        if tcp_connection_timeout is not None:
            self.tcp_connection_timeout = tcp_connection_timeout
        if http_authentication_user_policy is not None:
            self.http_authentication_user_policy = http_authentication_user_policy
        if use_chunking is not None:
            self.use_chunking = use_chunking
        if tcp_read_timeout is not None:
            self.tcp_read_timeout = tcp_read_timeout
        self.name = name
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if remote_authentication is not None:
            self.remote_authentication = remote_authentication
        self.remote_port = remote_port
        if enabled is not None:
            self.enabled = enabled
        self.remote_server = remote_server
        if process_response is not None:
            self.process_response = process_response

    @property
    def use_basic_auth(self):
        """Gets the use_basic_auth of this S3RemotePolicy1.  # noqa: E501


        :return: The use_basic_auth of this S3RemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._use_basic_auth

    @use_basic_auth.setter
    def use_basic_auth(self, use_basic_auth):
        """Sets the use_basic_auth of this S3RemotePolicy1.


        :param use_basic_auth: The use_basic_auth of this S3RemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._use_basic_auth = use_basic_auth

    @property
    def proxy_policy(self):
        """Gets the proxy_policy of this S3RemotePolicy1.  # noqa: E501


        :return: The proxy_policy of this S3RemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._proxy_policy

    @proxy_policy.setter
    def proxy_policy(self, proxy_policy):
        """Sets the proxy_policy of this S3RemotePolicy1.


        :param proxy_policy: The proxy_policy of this S3RemotePolicy1.  # noqa: E501
        :type: str
        """

        self._proxy_policy = proxy_policy

    @property
    def ssl_initiation_policy(self):
        """Gets the ssl_initiation_policy of this S3RemotePolicy1.  # noqa: E501


        :return: The ssl_initiation_policy of this S3RemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._ssl_initiation_policy

    @ssl_initiation_policy.setter
    def ssl_initiation_policy(self, ssl_initiation_policy):
        """Sets the ssl_initiation_policy of this S3RemotePolicy1.


        :param ssl_initiation_policy: The ssl_initiation_policy of this S3RemotePolicy1.  # noqa: E501
        :type: str
        """

        self._ssl_initiation_policy = ssl_initiation_policy

    @property
    def tcp_connection_timeout(self):
        """Gets the tcp_connection_timeout of this S3RemotePolicy1.  # noqa: E501


        :return: The tcp_connection_timeout of this S3RemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._tcp_connection_timeout

    @tcp_connection_timeout.setter
    def tcp_connection_timeout(self, tcp_connection_timeout):
        """Sets the tcp_connection_timeout of this S3RemotePolicy1.


        :param tcp_connection_timeout: The tcp_connection_timeout of this S3RemotePolicy1.  # noqa: E501
        :type: int
        """

        self._tcp_connection_timeout = tcp_connection_timeout

    @property
    def http_authentication_user_policy(self):
        """Gets the http_authentication_user_policy of this S3RemotePolicy1.  # noqa: E501


        :return: The http_authentication_user_policy of this S3RemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._http_authentication_user_policy

    @http_authentication_user_policy.setter
    def http_authentication_user_policy(self, http_authentication_user_policy):
        """Sets the http_authentication_user_policy of this S3RemotePolicy1.


        :param http_authentication_user_policy: The http_authentication_user_policy of this S3RemotePolicy1.  # noqa: E501
        :type: str
        """

        self._http_authentication_user_policy = http_authentication_user_policy

    @property
    def use_chunking(self):
        """Gets the use_chunking of this S3RemotePolicy1.  # noqa: E501


        :return: The use_chunking of this S3RemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._use_chunking

    @use_chunking.setter
    def use_chunking(self, use_chunking):
        """Sets the use_chunking of this S3RemotePolicy1.


        :param use_chunking: The use_chunking of this S3RemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._use_chunking = use_chunking

    @property
    def tcp_read_timeout(self):
        """Gets the tcp_read_timeout of this S3RemotePolicy1.  # noqa: E501


        :return: The tcp_read_timeout of this S3RemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._tcp_read_timeout

    @tcp_read_timeout.setter
    def tcp_read_timeout(self, tcp_read_timeout):
        """Sets the tcp_read_timeout of this S3RemotePolicy1.


        :param tcp_read_timeout: The tcp_read_timeout of this S3RemotePolicy1.  # noqa: E501
        :type: int
        """

        self._tcp_read_timeout = tcp_read_timeout

    @property
    def name(self):
        """Gets the name of this S3RemotePolicy1.  # noqa: E501


        :return: The name of this S3RemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this S3RemotePolicy1.


        :param name: The name of this S3RemotePolicy1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this S3RemotePolicy1.  # noqa: E501


        :return: The enable_ssl of this S3RemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this S3RemotePolicy1.


        :param enable_ssl: The enable_ssl of this S3RemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._enable_ssl = enable_ssl

    @property
    def remote_authentication(self):
        """Gets the remote_authentication of this S3RemotePolicy1.  # noqa: E501


        :return: The remote_authentication of this S3RemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._remote_authentication

    @remote_authentication.setter
    def remote_authentication(self, remote_authentication):
        """Sets the remote_authentication of this S3RemotePolicy1.


        :param remote_authentication: The remote_authentication of this S3RemotePolicy1.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "STATIC", "DYNAMIC", "PROPAGATE"]  # noqa: E501
        if remote_authentication not in allowed_values:
            raise ValueError(
                "Invalid value for `remote_authentication` ({0}), must be one of {1}"  # noqa: E501
                .format(remote_authentication, allowed_values)
            )

        self._remote_authentication = remote_authentication

    @property
    def remote_port(self):
        """Gets the remote_port of this S3RemotePolicy1.  # noqa: E501


        :return: The remote_port of this S3RemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        """Sets the remote_port of this S3RemotePolicy1.


        :param remote_port: The remote_port of this S3RemotePolicy1.  # noqa: E501
        :type: int
        """
        if remote_port is None:
            raise ValueError("Invalid value for `remote_port`, must not be `None`")  # noqa: E501

        self._remote_port = remote_port

    @property
    def enabled(self):
        """Gets the enabled of this S3RemotePolicy1.  # noqa: E501


        :return: The enabled of this S3RemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this S3RemotePolicy1.


        :param enabled: The enabled of this S3RemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def remote_server(self):
        """Gets the remote_server of this S3RemotePolicy1.  # noqa: E501


        :return: The remote_server of this S3RemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._remote_server

    @remote_server.setter
    def remote_server(self, remote_server):
        """Sets the remote_server of this S3RemotePolicy1.


        :param remote_server: The remote_server of this S3RemotePolicy1.  # noqa: E501
        :type: str
        """
        if remote_server is None:
            raise ValueError("Invalid value for `remote_server`, must not be `None`")  # noqa: E501

        self._remote_server = remote_server

    @property
    def process_response(self):
        """Gets the process_response of this S3RemotePolicy1.  # noqa: E501


        :return: The process_response of this S3RemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._process_response

    @process_response.setter
    def process_response(self, process_response):
        """Sets the process_response of this S3RemotePolicy1.


        :param process_response: The process_response of this S3RemotePolicy1.  # noqa: E501
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
        if not isinstance(other, S3RemotePolicy1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
