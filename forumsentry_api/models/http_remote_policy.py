# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

forumsentry_api/models.AuthMode  # noqa: F401,E501
forumsentry_api/models.RemoteAuthentication  # noqa: F401,E501


class HttpRemotePolicy(object):
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
        'ssl_initiation_policy': 'str',
        'auth_mode': 'AuthMode',
        'http_authentication_user_policy': 'str',
        'proxy_policy': 'str',
        'remote_authentication': 'RemoteAuthentication',
        'process_response': 'bool',
        'tcp_connection_timeout': 'int',
        'use_chunking': 'bool',
        'enable_ssl': 'bool',
        'tcp_read_timeout': 'int',
        'use_basic_auth': 'bool',
        'remote_port': 'int',
        'remote_server': 'str',
        'enabled': 'bool',
        'comment': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'ssl_initiation_policy': 'sslInitiationPolicy',
        'auth_mode': 'authMode',
        'http_authentication_user_policy': 'httpAuthenticationUserPolicy',
        'proxy_policy': 'proxyPolicy',
        'remote_authentication': 'remoteAuthentication',
        'process_response': 'processResponse',
        'tcp_connection_timeout': 'tcpConnectionTimeout',
        'use_chunking': 'useChunking',
        'enable_ssl': 'enableSSL',
        'tcp_read_timeout': 'tcpReadTimeout',
        'use_basic_auth': 'useBasicAuth',
        'remote_port': 'remotePort',
        'remote_server': 'remoteServer',
        'enabled': 'enabled',
        'comment': 'comment'
    }

    def __init__(self, name=None, description=None, ssl_initiation_policy=None, auth_mode=None, http_authentication_user_policy=None, proxy_policy=None, remote_authentication=None, process_response=None, tcp_connection_timeout=None, use_chunking=None, enable_ssl=None, tcp_read_timeout=None, use_basic_auth=None, remote_port=None, remote_server=None, enabled=None, comment=None):  # noqa: E501
        """HttpRemotePolicy - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._ssl_initiation_policy = None
        self._auth_mode = None
        self._http_authentication_user_policy = None
        self._proxy_policy = None
        self._remote_authentication = None
        self._process_response = None
        self._tcp_connection_timeout = None
        self._use_chunking = None
        self._enable_ssl = None
        self._tcp_read_timeout = None
        self._use_basic_auth = None
        self._remote_port = None
        self._remote_server = None
        self._enabled = None
        self._comment = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ssl_initiation_policy is not None:
            self.ssl_initiation_policy = ssl_initiation_policy
        if auth_mode is not None:
            self.auth_mode = auth_mode
        if http_authentication_user_policy is not None:
            self.http_authentication_user_policy = http_authentication_user_policy
        if proxy_policy is not None:
            self.proxy_policy = proxy_policy
        if remote_authentication is not None:
            self.remote_authentication = remote_authentication
        if process_response is not None:
            self.process_response = process_response
        if tcp_connection_timeout is not None:
            self.tcp_connection_timeout = tcp_connection_timeout
        if use_chunking is not None:
            self.use_chunking = use_chunking
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if tcp_read_timeout is not None:
            self.tcp_read_timeout = tcp_read_timeout
        if use_basic_auth is not None:
            self.use_basic_auth = use_basic_auth
        if remote_port is not None:
            self.remote_port = remote_port
        if remote_server is not None:
            self.remote_server = remote_server
        if enabled is not None:
            self.enabled = enabled
        if comment is not None:
            self.comment = comment

    @property
    def name(self):
        """Gets the name of this HttpRemotePolicy.  # noqa: E501


        :return: The name of this HttpRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HttpRemotePolicy.


        :param name: The name of this HttpRemotePolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this HttpRemotePolicy.  # noqa: E501


        :return: The description of this HttpRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HttpRemotePolicy.


        :param description: The description of this HttpRemotePolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ssl_initiation_policy(self):
        """Gets the ssl_initiation_policy of this HttpRemotePolicy.  # noqa: E501


        :return: The ssl_initiation_policy of this HttpRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._ssl_initiation_policy

    @ssl_initiation_policy.setter
    def ssl_initiation_policy(self, ssl_initiation_policy):
        """Sets the ssl_initiation_policy of this HttpRemotePolicy.


        :param ssl_initiation_policy: The ssl_initiation_policy of this HttpRemotePolicy.  # noqa: E501
        :type: str
        """

        self._ssl_initiation_policy = ssl_initiation_policy

    @property
    def auth_mode(self):
        """Gets the auth_mode of this HttpRemotePolicy.  # noqa: E501


        :return: The auth_mode of this HttpRemotePolicy.  # noqa: E501
        :rtype: AuthMode
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """Sets the auth_mode of this HttpRemotePolicy.


        :param auth_mode: The auth_mode of this HttpRemotePolicy.  # noqa: E501
        :type: AuthMode
        """

        self._auth_mode = auth_mode

    @property
    def http_authentication_user_policy(self):
        """Gets the http_authentication_user_policy of this HttpRemotePolicy.  # noqa: E501


        :return: The http_authentication_user_policy of this HttpRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._http_authentication_user_policy

    @http_authentication_user_policy.setter
    def http_authentication_user_policy(self, http_authentication_user_policy):
        """Sets the http_authentication_user_policy of this HttpRemotePolicy.


        :param http_authentication_user_policy: The http_authentication_user_policy of this HttpRemotePolicy.  # noqa: E501
        :type: str
        """

        self._http_authentication_user_policy = http_authentication_user_policy

    @property
    def proxy_policy(self):
        """Gets the proxy_policy of this HttpRemotePolicy.  # noqa: E501


        :return: The proxy_policy of this HttpRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._proxy_policy

    @proxy_policy.setter
    def proxy_policy(self, proxy_policy):
        """Sets the proxy_policy of this HttpRemotePolicy.


        :param proxy_policy: The proxy_policy of this HttpRemotePolicy.  # noqa: E501
        :type: str
        """

        self._proxy_policy = proxy_policy

    @property
    def remote_authentication(self):
        """Gets the remote_authentication of this HttpRemotePolicy.  # noqa: E501


        :return: The remote_authentication of this HttpRemotePolicy.  # noqa: E501
        :rtype: RemoteAuthentication
        """
        return self._remote_authentication

    @remote_authentication.setter
    def remote_authentication(self, remote_authentication):
        """Sets the remote_authentication of this HttpRemotePolicy.


        :param remote_authentication: The remote_authentication of this HttpRemotePolicy.  # noqa: E501
        :type: RemoteAuthentication
        """

        self._remote_authentication = remote_authentication

    @property
    def process_response(self):
        """Gets the process_response of this HttpRemotePolicy.  # noqa: E501


        :return: The process_response of this HttpRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._process_response

    @process_response.setter
    def process_response(self, process_response):
        """Sets the process_response of this HttpRemotePolicy.


        :param process_response: The process_response of this HttpRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._process_response = process_response

    @property
    def tcp_connection_timeout(self):
        """Gets the tcp_connection_timeout of this HttpRemotePolicy.  # noqa: E501


        :return: The tcp_connection_timeout of this HttpRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._tcp_connection_timeout

    @tcp_connection_timeout.setter
    def tcp_connection_timeout(self, tcp_connection_timeout):
        """Sets the tcp_connection_timeout of this HttpRemotePolicy.


        :param tcp_connection_timeout: The tcp_connection_timeout of this HttpRemotePolicy.  # noqa: E501
        :type: int
        """

        self._tcp_connection_timeout = tcp_connection_timeout

    @property
    def use_chunking(self):
        """Gets the use_chunking of this HttpRemotePolicy.  # noqa: E501


        :return: The use_chunking of this HttpRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._use_chunking

    @use_chunking.setter
    def use_chunking(self, use_chunking):
        """Sets the use_chunking of this HttpRemotePolicy.


        :param use_chunking: The use_chunking of this HttpRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._use_chunking = use_chunking

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this HttpRemotePolicy.  # noqa: E501


        :return: The enable_ssl of this HttpRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this HttpRemotePolicy.


        :param enable_ssl: The enable_ssl of this HttpRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._enable_ssl = enable_ssl

    @property
    def tcp_read_timeout(self):
        """Gets the tcp_read_timeout of this HttpRemotePolicy.  # noqa: E501


        :return: The tcp_read_timeout of this HttpRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._tcp_read_timeout

    @tcp_read_timeout.setter
    def tcp_read_timeout(self, tcp_read_timeout):
        """Sets the tcp_read_timeout of this HttpRemotePolicy.


        :param tcp_read_timeout: The tcp_read_timeout of this HttpRemotePolicy.  # noqa: E501
        :type: int
        """

        self._tcp_read_timeout = tcp_read_timeout

    @property
    def use_basic_auth(self):
        """Gets the use_basic_auth of this HttpRemotePolicy.  # noqa: E501


        :return: The use_basic_auth of this HttpRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._use_basic_auth

    @use_basic_auth.setter
    def use_basic_auth(self, use_basic_auth):
        """Sets the use_basic_auth of this HttpRemotePolicy.


        :param use_basic_auth: The use_basic_auth of this HttpRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._use_basic_auth = use_basic_auth

    @property
    def remote_port(self):
        """Gets the remote_port of this HttpRemotePolicy.  # noqa: E501


        :return: The remote_port of this HttpRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        """Sets the remote_port of this HttpRemotePolicy.


        :param remote_port: The remote_port of this HttpRemotePolicy.  # noqa: E501
        :type: int
        """

        self._remote_port = remote_port

    @property
    def remote_server(self):
        """Gets the remote_server of this HttpRemotePolicy.  # noqa: E501


        :return: The remote_server of this HttpRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._remote_server

    @remote_server.setter
    def remote_server(self, remote_server):
        """Sets the remote_server of this HttpRemotePolicy.


        :param remote_server: The remote_server of this HttpRemotePolicy.  # noqa: E501
        :type: str
        """

        self._remote_server = remote_server

    @property
    def enabled(self):
        """Gets the enabled of this HttpRemotePolicy.  # noqa: E501


        :return: The enabled of this HttpRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this HttpRemotePolicy.


        :param enabled: The enabled of this HttpRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def comment(self):
        """Gets the comment of this HttpRemotePolicy.  # noqa: E501


        :return: The comment of this HttpRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this HttpRemotePolicy.


        :param comment: The comment of this HttpRemotePolicy.  # noqa: E501
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
        if not isinstance(other, HttpRemotePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
