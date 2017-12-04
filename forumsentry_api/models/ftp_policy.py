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


class FtpPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, use_pasv_ip=None, remote_ssl_termination_policy=None, listener_ftps_mode=None, start_pasv_port=None, read_timeout_millis=None, ip=None, prevent_user_host_syntax=None, remote_server=None, get_pgp_policy=None, remote_ssl_initiation_policy=None, end_pasv_port=None, put_compression_mode=None, port=None, use_device_ip=None, get_compression_mode=None, remote_ftps_auth_mode=None, name=None, put_pgp_policy=None, process_as_xml=None, listener_ssl_termination_policy=None, description=None, remote_port=None, listener_ssl_enabled=None, comment=None, remote_ftps_mode=None, enabled=None, interface=None, user_policy_rule=None, passv_ip_override=None, pasv_ip=None, remote_ssl_enabled=None, listener_ftps_auth_mode=None, listener_ssl_initiation_policy=None):
        """
        FtpPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'use_pasv_ip': 'bool',
            'remote_ssl_termination_policy': 'str',
            'listener_ftps_mode': 'str',
            'start_pasv_port': 'int',
            'read_timeout_millis': 'int',
            'ip': 'str',
            'prevent_user_host_syntax': 'bool',
            'remote_server': 'str',
            'get_pgp_policy': 'str',
            'remote_ssl_initiation_policy': 'str',
            'end_pasv_port': 'int',
            'put_compression_mode': 'str',
            'port': 'int',
            'use_device_ip': 'bool',
            'get_compression_mode': 'str',
            'remote_ftps_auth_mode': 'str',
            'name': 'str',
            'put_pgp_policy': 'str',
            'process_as_xml': 'bool',
            'listener_ssl_termination_policy': 'str',
            'description': 'str',
            'remote_port': 'int',
            'listener_ssl_enabled': 'bool',
            'comment': 'str',
            'remote_ftps_mode': 'str',
            'enabled': 'bool',
            'interface': 'str',
            'user_policy_rule': 'str',
            'passv_ip_override': 'bool',
            'pasv_ip': 'str',
            'remote_ssl_enabled': 'bool',
            'listener_ftps_auth_mode': 'str',
            'listener_ssl_initiation_policy': 'str'
        }

        self.attribute_map = {
            'use_pasv_ip': 'usePasvIp',
            'remote_ssl_termination_policy': 'remoteSslTerminationPolicy',
            'listener_ftps_mode': 'listenerFtpsMode',
            'start_pasv_port': 'startPasvPort',
            'read_timeout_millis': 'readTimeoutMillis',
            'ip': 'ip',
            'prevent_user_host_syntax': 'preventUserHostSyntax',
            'remote_server': 'remoteServer',
            'get_pgp_policy': 'getPgpPolicy',
            'remote_ssl_initiation_policy': 'remoteSslInitiationPolicy',
            'end_pasv_port': 'endPasvPort',
            'put_compression_mode': 'putCompressionMode',
            'port': 'port',
            'use_device_ip': 'useDeviceIp',
            'get_compression_mode': 'getCompressionMode',
            'remote_ftps_auth_mode': 'remoteFtpsAuthMode',
            'name': 'name',
            'put_pgp_policy': 'putPgpPolicy',
            'process_as_xml': 'processAsXml',
            'listener_ssl_termination_policy': 'listenerSslTerminationPolicy',
            'description': 'description',
            'remote_port': 'remotePort',
            'listener_ssl_enabled': 'listenerSslEnabled',
            'comment': 'comment',
            'remote_ftps_mode': 'remoteFtpsMode',
            'enabled': 'enabled',
            'interface': 'interface',
            'user_policy_rule': 'userPolicyRule',
            'passv_ip_override': 'passvIpOverride',
            'pasv_ip': 'pasvIp',
            'remote_ssl_enabled': 'remoteSslEnabled',
            'listener_ftps_auth_mode': 'listenerFtpsAuthMode',
            'listener_ssl_initiation_policy': 'listenerSslInitiationPolicy'
        }

        self._use_pasv_ip = use_pasv_ip
        self._remote_ssl_termination_policy = remote_ssl_termination_policy
        self._listener_ftps_mode = listener_ftps_mode
        self._start_pasv_port = start_pasv_port
        self._read_timeout_millis = read_timeout_millis
        self._ip = ip
        self._prevent_user_host_syntax = prevent_user_host_syntax
        self._remote_server = remote_server
        self._get_pgp_policy = get_pgp_policy
        self._remote_ssl_initiation_policy = remote_ssl_initiation_policy
        self._end_pasv_port = end_pasv_port
        self._put_compression_mode = put_compression_mode
        self._port = port
        self._use_device_ip = use_device_ip
        self._get_compression_mode = get_compression_mode
        self._remote_ftps_auth_mode = remote_ftps_auth_mode
        self._name = name
        self._put_pgp_policy = put_pgp_policy
        self._process_as_xml = process_as_xml
        self._listener_ssl_termination_policy = listener_ssl_termination_policy
        self._description = description
        self._remote_port = remote_port
        self._listener_ssl_enabled = listener_ssl_enabled
        self._comment = comment
        self._remote_ftps_mode = remote_ftps_mode
        self._enabled = enabled
        self._interface = interface
        self._user_policy_rule = user_policy_rule
        self._passv_ip_override = passv_ip_override
        self._pasv_ip = pasv_ip
        self._remote_ssl_enabled = remote_ssl_enabled
        self._listener_ftps_auth_mode = listener_ftps_auth_mode
        self._listener_ssl_initiation_policy = listener_ssl_initiation_policy

    @property
    def use_pasv_ip(self):
        """
        Gets the use_pasv_ip of this FtpPolicy.


        :return: The use_pasv_ip of this FtpPolicy.
        :rtype: bool
        """
        return self._use_pasv_ip

    @use_pasv_ip.setter
    def use_pasv_ip(self, use_pasv_ip):
        """
        Sets the use_pasv_ip of this FtpPolicy.


        :param use_pasv_ip: The use_pasv_ip of this FtpPolicy.
        :type: bool
        """

        self._use_pasv_ip = use_pasv_ip

    @property
    def remote_ssl_termination_policy(self):
        """
        Gets the remote_ssl_termination_policy of this FtpPolicy.


        :return: The remote_ssl_termination_policy of this FtpPolicy.
        :rtype: str
        """
        return self._remote_ssl_termination_policy

    @remote_ssl_termination_policy.setter
    def remote_ssl_termination_policy(self, remote_ssl_termination_policy):
        """
        Sets the remote_ssl_termination_policy of this FtpPolicy.


        :param remote_ssl_termination_policy: The remote_ssl_termination_policy of this FtpPolicy.
        :type: str
        """

        self._remote_ssl_termination_policy = remote_ssl_termination_policy

    @property
    def listener_ftps_mode(self):
        """
        Gets the listener_ftps_mode of this FtpPolicy.


        :return: The listener_ftps_mode of this FtpPolicy.
        :rtype: str
        """
        return self._listener_ftps_mode

    @listener_ftps_mode.setter
    def listener_ftps_mode(self, listener_ftps_mode):
        """
        Sets the listener_ftps_mode of this FtpPolicy.


        :param listener_ftps_mode: The listener_ftps_mode of this FtpPolicy.
        :type: str
        """
        allowed_values = ["EXPLICIT", "IMPLICIT"]
        if listener_ftps_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `listener_ftps_mode` ({0}), must be one of {1}"
                .format(listener_ftps_mode, allowed_values)
            )

        self._listener_ftps_mode = listener_ftps_mode

    @property
    def start_pasv_port(self):
        """
        Gets the start_pasv_port of this FtpPolicy.


        :return: The start_pasv_port of this FtpPolicy.
        :rtype: int
        """
        return self._start_pasv_port

    @start_pasv_port.setter
    def start_pasv_port(self, start_pasv_port):
        """
        Sets the start_pasv_port of this FtpPolicy.


        :param start_pasv_port: The start_pasv_port of this FtpPolicy.
        :type: int
        """

        self._start_pasv_port = start_pasv_port

    @property
    def read_timeout_millis(self):
        """
        Gets the read_timeout_millis of this FtpPolicy.


        :return: The read_timeout_millis of this FtpPolicy.
        :rtype: int
        """
        return self._read_timeout_millis

    @read_timeout_millis.setter
    def read_timeout_millis(self, read_timeout_millis):
        """
        Sets the read_timeout_millis of this FtpPolicy.


        :param read_timeout_millis: The read_timeout_millis of this FtpPolicy.
        :type: int
        """

        self._read_timeout_millis = read_timeout_millis

    @property
    def ip(self):
        """
        Gets the ip of this FtpPolicy.


        :return: The ip of this FtpPolicy.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this FtpPolicy.


        :param ip: The ip of this FtpPolicy.
        :type: str
        """

        self._ip = ip

    @property
    def prevent_user_host_syntax(self):
        """
        Gets the prevent_user_host_syntax of this FtpPolicy.


        :return: The prevent_user_host_syntax of this FtpPolicy.
        :rtype: bool
        """
        return self._prevent_user_host_syntax

    @prevent_user_host_syntax.setter
    def prevent_user_host_syntax(self, prevent_user_host_syntax):
        """
        Sets the prevent_user_host_syntax of this FtpPolicy.


        :param prevent_user_host_syntax: The prevent_user_host_syntax of this FtpPolicy.
        :type: bool
        """

        self._prevent_user_host_syntax = prevent_user_host_syntax

    @property
    def remote_server(self):
        """
        Gets the remote_server of this FtpPolicy.


        :return: The remote_server of this FtpPolicy.
        :rtype: str
        """
        return self._remote_server

    @remote_server.setter
    def remote_server(self, remote_server):
        """
        Sets the remote_server of this FtpPolicy.


        :param remote_server: The remote_server of this FtpPolicy.
        :type: str
        """

        self._remote_server = remote_server

    @property
    def get_pgp_policy(self):
        """
        Gets the get_pgp_policy of this FtpPolicy.


        :return: The get_pgp_policy of this FtpPolicy.
        :rtype: str
        """
        return self._get_pgp_policy

    @get_pgp_policy.setter
    def get_pgp_policy(self, get_pgp_policy):
        """
        Sets the get_pgp_policy of this FtpPolicy.


        :param get_pgp_policy: The get_pgp_policy of this FtpPolicy.
        :type: str
        """

        self._get_pgp_policy = get_pgp_policy

    @property
    def remote_ssl_initiation_policy(self):
        """
        Gets the remote_ssl_initiation_policy of this FtpPolicy.


        :return: The remote_ssl_initiation_policy of this FtpPolicy.
        :rtype: str
        """
        return self._remote_ssl_initiation_policy

    @remote_ssl_initiation_policy.setter
    def remote_ssl_initiation_policy(self, remote_ssl_initiation_policy):
        """
        Sets the remote_ssl_initiation_policy of this FtpPolicy.


        :param remote_ssl_initiation_policy: The remote_ssl_initiation_policy of this FtpPolicy.
        :type: str
        """

        self._remote_ssl_initiation_policy = remote_ssl_initiation_policy

    @property
    def end_pasv_port(self):
        """
        Gets the end_pasv_port of this FtpPolicy.


        :return: The end_pasv_port of this FtpPolicy.
        :rtype: int
        """
        return self._end_pasv_port

    @end_pasv_port.setter
    def end_pasv_port(self, end_pasv_port):
        """
        Sets the end_pasv_port of this FtpPolicy.


        :param end_pasv_port: The end_pasv_port of this FtpPolicy.
        :type: int
        """

        self._end_pasv_port = end_pasv_port

    @property
    def put_compression_mode(self):
        """
        Gets the put_compression_mode of this FtpPolicy.


        :return: The put_compression_mode of this FtpPolicy.
        :rtype: str
        """
        return self._put_compression_mode

    @put_compression_mode.setter
    def put_compression_mode(self, put_compression_mode):
        """
        Sets the put_compression_mode of this FtpPolicy.


        :param put_compression_mode: The put_compression_mode of this FtpPolicy.
        :type: str
        """
        allowed_values = ["NONE", "ZIP_COMPRESS", "ZIP_DECOMPRESS", "GZIP_COMPRESS", "GZIP_DECOMPRESS"]
        if put_compression_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `put_compression_mode` ({0}), must be one of {1}"
                .format(put_compression_mode, allowed_values)
            )

        self._put_compression_mode = put_compression_mode

    @property
    def port(self):
        """
        Gets the port of this FtpPolicy.


        :return: The port of this FtpPolicy.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this FtpPolicy.


        :param port: The port of this FtpPolicy.
        :type: int
        """

        self._port = port

    @property
    def use_device_ip(self):
        """
        Gets the use_device_ip of this FtpPolicy.


        :return: The use_device_ip of this FtpPolicy.
        :rtype: bool
        """
        return self._use_device_ip

    @use_device_ip.setter
    def use_device_ip(self, use_device_ip):
        """
        Sets the use_device_ip of this FtpPolicy.


        :param use_device_ip: The use_device_ip of this FtpPolicy.
        :type: bool
        """

        self._use_device_ip = use_device_ip

    @property
    def get_compression_mode(self):
        """
        Gets the get_compression_mode of this FtpPolicy.


        :return: The get_compression_mode of this FtpPolicy.
        :rtype: str
        """
        return self._get_compression_mode

    @get_compression_mode.setter
    def get_compression_mode(self, get_compression_mode):
        """
        Sets the get_compression_mode of this FtpPolicy.


        :param get_compression_mode: The get_compression_mode of this FtpPolicy.
        :type: str
        """
        allowed_values = ["NONE", "ZIP_COMPRESS", "ZIP_DECOMPRESS", "GZIP_COMPRESS", "GZIP_DECOMPRESS"]
        if get_compression_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `get_compression_mode` ({0}), must be one of {1}"
                .format(get_compression_mode, allowed_values)
            )

        self._get_compression_mode = get_compression_mode

    @property
    def remote_ftps_auth_mode(self):
        """
        Gets the remote_ftps_auth_mode of this FtpPolicy.


        :return: The remote_ftps_auth_mode of this FtpPolicy.
        :rtype: str
        """
        return self._remote_ftps_auth_mode

    @remote_ftps_auth_mode.setter
    def remote_ftps_auth_mode(self, remote_ftps_auth_mode):
        """
        Sets the remote_ftps_auth_mode of this FtpPolicy.


        :param remote_ftps_auth_mode: The remote_ftps_auth_mode of this FtpPolicy.
        :type: str
        """
        allowed_values = ["TLS", "SSL"]
        if remote_ftps_auth_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `remote_ftps_auth_mode` ({0}), must be one of {1}"
                .format(remote_ftps_auth_mode, allowed_values)
            )

        self._remote_ftps_auth_mode = remote_ftps_auth_mode

    @property
    def name(self):
        """
        Gets the name of this FtpPolicy.


        :return: The name of this FtpPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FtpPolicy.


        :param name: The name of this FtpPolicy.
        :type: str
        """

        self._name = name

    @property
    def put_pgp_policy(self):
        """
        Gets the put_pgp_policy of this FtpPolicy.


        :return: The put_pgp_policy of this FtpPolicy.
        :rtype: str
        """
        return self._put_pgp_policy

    @put_pgp_policy.setter
    def put_pgp_policy(self, put_pgp_policy):
        """
        Sets the put_pgp_policy of this FtpPolicy.


        :param put_pgp_policy: The put_pgp_policy of this FtpPolicy.
        :type: str
        """

        self._put_pgp_policy = put_pgp_policy

    @property
    def process_as_xml(self):
        """
        Gets the process_as_xml of this FtpPolicy.


        :return: The process_as_xml of this FtpPolicy.
        :rtype: bool
        """
        return self._process_as_xml

    @process_as_xml.setter
    def process_as_xml(self, process_as_xml):
        """
        Sets the process_as_xml of this FtpPolicy.


        :param process_as_xml: The process_as_xml of this FtpPolicy.
        :type: bool
        """

        self._process_as_xml = process_as_xml

    @property
    def listener_ssl_termination_policy(self):
        """
        Gets the listener_ssl_termination_policy of this FtpPolicy.


        :return: The listener_ssl_termination_policy of this FtpPolicy.
        :rtype: str
        """
        return self._listener_ssl_termination_policy

    @listener_ssl_termination_policy.setter
    def listener_ssl_termination_policy(self, listener_ssl_termination_policy):
        """
        Sets the listener_ssl_termination_policy of this FtpPolicy.


        :param listener_ssl_termination_policy: The listener_ssl_termination_policy of this FtpPolicy.
        :type: str
        """

        self._listener_ssl_termination_policy = listener_ssl_termination_policy

    @property
    def description(self):
        """
        Gets the description of this FtpPolicy.


        :return: The description of this FtpPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FtpPolicy.


        :param description: The description of this FtpPolicy.
        :type: str
        """

        self._description = description

    @property
    def remote_port(self):
        """
        Gets the remote_port of this FtpPolicy.


        :return: The remote_port of this FtpPolicy.
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        """
        Sets the remote_port of this FtpPolicy.


        :param remote_port: The remote_port of this FtpPolicy.
        :type: int
        """

        self._remote_port = remote_port

    @property
    def listener_ssl_enabled(self):
        """
        Gets the listener_ssl_enabled of this FtpPolicy.


        :return: The listener_ssl_enabled of this FtpPolicy.
        :rtype: bool
        """
        return self._listener_ssl_enabled

    @listener_ssl_enabled.setter
    def listener_ssl_enabled(self, listener_ssl_enabled):
        """
        Sets the listener_ssl_enabled of this FtpPolicy.


        :param listener_ssl_enabled: The listener_ssl_enabled of this FtpPolicy.
        :type: bool
        """

        self._listener_ssl_enabled = listener_ssl_enabled

    @property
    def comment(self):
        """
        Gets the comment of this FtpPolicy.


        :return: The comment of this FtpPolicy.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this FtpPolicy.


        :param comment: The comment of this FtpPolicy.
        :type: str
        """

        self._comment = comment

    @property
    def remote_ftps_mode(self):
        """
        Gets the remote_ftps_mode of this FtpPolicy.


        :return: The remote_ftps_mode of this FtpPolicy.
        :rtype: str
        """
        return self._remote_ftps_mode

    @remote_ftps_mode.setter
    def remote_ftps_mode(self, remote_ftps_mode):
        """
        Sets the remote_ftps_mode of this FtpPolicy.


        :param remote_ftps_mode: The remote_ftps_mode of this FtpPolicy.
        :type: str
        """
        allowed_values = ["EXPLICIT", "IMPLICIT"]
        if remote_ftps_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `remote_ftps_mode` ({0}), must be one of {1}"
                .format(remote_ftps_mode, allowed_values)
            )

        self._remote_ftps_mode = remote_ftps_mode

    @property
    def enabled(self):
        """
        Gets the enabled of this FtpPolicy.


        :return: The enabled of this FtpPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this FtpPolicy.


        :param enabled: The enabled of this FtpPolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def interface(self):
        """
        Gets the interface of this FtpPolicy.


        :return: The interface of this FtpPolicy.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """
        Sets the interface of this FtpPolicy.


        :param interface: The interface of this FtpPolicy.
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
    def user_policy_rule(self):
        """
        Gets the user_policy_rule of this FtpPolicy.


        :return: The user_policy_rule of this FtpPolicy.
        :rtype: str
        """
        return self._user_policy_rule

    @user_policy_rule.setter
    def user_policy_rule(self, user_policy_rule):
        """
        Sets the user_policy_rule of this FtpPolicy.


        :param user_policy_rule: The user_policy_rule of this FtpPolicy.
        :type: str
        """
        allowed_values = ["REQUIRED", "OPTIONAL", "IGNORED"]
        if user_policy_rule not in allowed_values:
            raise ValueError(
                "Invalid value for `user_policy_rule` ({0}), must be one of {1}"
                .format(user_policy_rule, allowed_values)
            )

        self._user_policy_rule = user_policy_rule

    @property
    def passv_ip_override(self):
        """
        Gets the passv_ip_override of this FtpPolicy.


        :return: The passv_ip_override of this FtpPolicy.
        :rtype: bool
        """
        return self._passv_ip_override

    @passv_ip_override.setter
    def passv_ip_override(self, passv_ip_override):
        """
        Sets the passv_ip_override of this FtpPolicy.


        :param passv_ip_override: The passv_ip_override of this FtpPolicy.
        :type: bool
        """

        self._passv_ip_override = passv_ip_override

    @property
    def pasv_ip(self):
        """
        Gets the pasv_ip of this FtpPolicy.


        :return: The pasv_ip of this FtpPolicy.
        :rtype: str
        """
        return self._pasv_ip

    @pasv_ip.setter
    def pasv_ip(self, pasv_ip):
        """
        Sets the pasv_ip of this FtpPolicy.


        :param pasv_ip: The pasv_ip of this FtpPolicy.
        :type: str
        """

        self._pasv_ip = pasv_ip

    @property
    def remote_ssl_enabled(self):
        """
        Gets the remote_ssl_enabled of this FtpPolicy.


        :return: The remote_ssl_enabled of this FtpPolicy.
        :rtype: bool
        """
        return self._remote_ssl_enabled

    @remote_ssl_enabled.setter
    def remote_ssl_enabled(self, remote_ssl_enabled):
        """
        Sets the remote_ssl_enabled of this FtpPolicy.


        :param remote_ssl_enabled: The remote_ssl_enabled of this FtpPolicy.
        :type: bool
        """

        self._remote_ssl_enabled = remote_ssl_enabled

    @property
    def listener_ftps_auth_mode(self):
        """
        Gets the listener_ftps_auth_mode of this FtpPolicy.


        :return: The listener_ftps_auth_mode of this FtpPolicy.
        :rtype: str
        """
        return self._listener_ftps_auth_mode

    @listener_ftps_auth_mode.setter
    def listener_ftps_auth_mode(self, listener_ftps_auth_mode):
        """
        Sets the listener_ftps_auth_mode of this FtpPolicy.


        :param listener_ftps_auth_mode: The listener_ftps_auth_mode of this FtpPolicy.
        :type: str
        """
        allowed_values = ["TLS", "SSL"]
        if listener_ftps_auth_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `listener_ftps_auth_mode` ({0}), must be one of {1}"
                .format(listener_ftps_auth_mode, allowed_values)
            )

        self._listener_ftps_auth_mode = listener_ftps_auth_mode

    @property
    def listener_ssl_initiation_policy(self):
        """
        Gets the listener_ssl_initiation_policy of this FtpPolicy.


        :return: The listener_ssl_initiation_policy of this FtpPolicy.
        :rtype: str
        """
        return self._listener_ssl_initiation_policy

    @listener_ssl_initiation_policy.setter
    def listener_ssl_initiation_policy(self, listener_ssl_initiation_policy):
        """
        Sets the listener_ssl_initiation_policy of this FtpPolicy.


        :param listener_ssl_initiation_policy: The listener_ssl_initiation_policy of this FtpPolicy.
        :type: str
        """

        self._listener_ssl_initiation_policy = listener_ssl_initiation_policy

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
