# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

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


class S3RemotePolicy1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, use_basic_auth=None, proxy_policy=None, ssl_initiation_policy=None, tcp_connection_timeout=None, http_authentication_user_policy=None, use_chunking=None, tcp_read_timeout=None, name=None, enable_ssl=None, remote_authentication=None, remote_port=None, enabled=None, remote_server=None, process_response=None):
        """
        S3RemotePolicy1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
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

        self.attribute_map = {
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

        self._use_basic_auth = use_basic_auth
        self._proxy_policy = proxy_policy
        self._ssl_initiation_policy = ssl_initiation_policy
        self._tcp_connection_timeout = tcp_connection_timeout
        self._http_authentication_user_policy = http_authentication_user_policy
        self._use_chunking = use_chunking
        self._tcp_read_timeout = tcp_read_timeout
        self._name = name
        self._enable_ssl = enable_ssl
        self._remote_authentication = remote_authentication
        self._remote_port = remote_port
        self._enabled = enabled
        self._remote_server = remote_server
        self._process_response = process_response

    @property
    def use_basic_auth(self):
        """
        Gets the use_basic_auth of this S3RemotePolicy1.


        :return: The use_basic_auth of this S3RemotePolicy1.
        :rtype: bool
        """
        return self._use_basic_auth

    @use_basic_auth.setter
    def use_basic_auth(self, use_basic_auth):
        """
        Sets the use_basic_auth of this S3RemotePolicy1.


        :param use_basic_auth: The use_basic_auth of this S3RemotePolicy1.
        :type: bool
        """

        self._use_basic_auth = use_basic_auth

    @property
    def proxy_policy(self):
        """
        Gets the proxy_policy of this S3RemotePolicy1.


        :return: The proxy_policy of this S3RemotePolicy1.
        :rtype: str
        """
        return self._proxy_policy

    @proxy_policy.setter
    def proxy_policy(self, proxy_policy):
        """
        Sets the proxy_policy of this S3RemotePolicy1.


        :param proxy_policy: The proxy_policy of this S3RemotePolicy1.
        :type: str
        """

        self._proxy_policy = proxy_policy

    @property
    def ssl_initiation_policy(self):
        """
        Gets the ssl_initiation_policy of this S3RemotePolicy1.


        :return: The ssl_initiation_policy of this S3RemotePolicy1.
        :rtype: str
        """
        return self._ssl_initiation_policy

    @ssl_initiation_policy.setter
    def ssl_initiation_policy(self, ssl_initiation_policy):
        """
        Sets the ssl_initiation_policy of this S3RemotePolicy1.


        :param ssl_initiation_policy: The ssl_initiation_policy of this S3RemotePolicy1.
        :type: str
        """

        self._ssl_initiation_policy = ssl_initiation_policy

    @property
    def tcp_connection_timeout(self):
        """
        Gets the tcp_connection_timeout of this S3RemotePolicy1.


        :return: The tcp_connection_timeout of this S3RemotePolicy1.
        :rtype: int
        """
        return self._tcp_connection_timeout

    @tcp_connection_timeout.setter
    def tcp_connection_timeout(self, tcp_connection_timeout):
        """
        Sets the tcp_connection_timeout of this S3RemotePolicy1.


        :param tcp_connection_timeout: The tcp_connection_timeout of this S3RemotePolicy1.
        :type: int
        """

        self._tcp_connection_timeout = tcp_connection_timeout

    @property
    def http_authentication_user_policy(self):
        """
        Gets the http_authentication_user_policy of this S3RemotePolicy1.


        :return: The http_authentication_user_policy of this S3RemotePolicy1.
        :rtype: str
        """
        return self._http_authentication_user_policy

    @http_authentication_user_policy.setter
    def http_authentication_user_policy(self, http_authentication_user_policy):
        """
        Sets the http_authentication_user_policy of this S3RemotePolicy1.


        :param http_authentication_user_policy: The http_authentication_user_policy of this S3RemotePolicy1.
        :type: str
        """

        self._http_authentication_user_policy = http_authentication_user_policy

    @property
    def use_chunking(self):
        """
        Gets the use_chunking of this S3RemotePolicy1.


        :return: The use_chunking of this S3RemotePolicy1.
        :rtype: bool
        """
        return self._use_chunking

    @use_chunking.setter
    def use_chunking(self, use_chunking):
        """
        Sets the use_chunking of this S3RemotePolicy1.


        :param use_chunking: The use_chunking of this S3RemotePolicy1.
        :type: bool
        """

        self._use_chunking = use_chunking

    @property
    def tcp_read_timeout(self):
        """
        Gets the tcp_read_timeout of this S3RemotePolicy1.


        :return: The tcp_read_timeout of this S3RemotePolicy1.
        :rtype: int
        """
        return self._tcp_read_timeout

    @tcp_read_timeout.setter
    def tcp_read_timeout(self, tcp_read_timeout):
        """
        Sets the tcp_read_timeout of this S3RemotePolicy1.


        :param tcp_read_timeout: The tcp_read_timeout of this S3RemotePolicy1.
        :type: int
        """

        self._tcp_read_timeout = tcp_read_timeout

    @property
    def name(self):
        """
        Gets the name of this S3RemotePolicy1.


        :return: The name of this S3RemotePolicy1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this S3RemotePolicy1.


        :param name: The name of this S3RemotePolicy1.
        :type: str
        """

        self._name = name

    @property
    def enable_ssl(self):
        """
        Gets the enable_ssl of this S3RemotePolicy1.


        :return: The enable_ssl of this S3RemotePolicy1.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """
        Sets the enable_ssl of this S3RemotePolicy1.


        :param enable_ssl: The enable_ssl of this S3RemotePolicy1.
        :type: bool
        """

        self._enable_ssl = enable_ssl

    @property
    def remote_authentication(self):
        """
        Gets the remote_authentication of this S3RemotePolicy1.


        :return: The remote_authentication of this S3RemotePolicy1.
        :rtype: str
        """
        return self._remote_authentication

    @remote_authentication.setter
    def remote_authentication(self, remote_authentication):
        """
        Sets the remote_authentication of this S3RemotePolicy1.


        :param remote_authentication: The remote_authentication of this S3RemotePolicy1.
        :type: str
        """
        allowed_values = ["NONE", "STATIC", "DYNAMIC", "PROPAGATE"]
        if remote_authentication not in allowed_values:
            raise ValueError(
                "Invalid value for `remote_authentication` ({0}), must be one of {1}"
                .format(remote_authentication, allowed_values)
            )

        self._remote_authentication = remote_authentication

    @property
    def remote_port(self):
        """
        Gets the remote_port of this S3RemotePolicy1.


        :return: The remote_port of this S3RemotePolicy1.
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        """
        Sets the remote_port of this S3RemotePolicy1.


        :param remote_port: The remote_port of this S3RemotePolicy1.
        :type: int
        """

        self._remote_port = remote_port

    @property
    def enabled(self):
        """
        Gets the enabled of this S3RemotePolicy1.


        :return: The enabled of this S3RemotePolicy1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this S3RemotePolicy1.


        :param enabled: The enabled of this S3RemotePolicy1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def remote_server(self):
        """
        Gets the remote_server of this S3RemotePolicy1.


        :return: The remote_server of this S3RemotePolicy1.
        :rtype: str
        """
        return self._remote_server

    @remote_server.setter
    def remote_server(self, remote_server):
        """
        Sets the remote_server of this S3RemotePolicy1.


        :param remote_server: The remote_server of this S3RemotePolicy1.
        :type: str
        """

        self._remote_server = remote_server

    @property
    def process_response(self):
        """
        Gets the process_response of this S3RemotePolicy1.


        :return: The process_response of this S3RemotePolicy1.
        :rtype: bool
        """
        return self._process_response

    @process_response.setter
    def process_response(self, process_response):
        """
        Sets the process_response of this S3RemotePolicy1.


        :param process_response: The process_response of this S3RemotePolicy1.
        :type: bool
        """

        self._process_response = process_response

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