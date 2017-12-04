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


class VirtualDirectory1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, acl_policy=None, remote_path=None, virtual_host=None, name=None, enabled=None, listener_policy=None, description=None, request_process_type=None, virtual_path=None, error_template=None, use_remote_policy=None, response_process_type=None, remote_policy=None, request_process=None, request_filter_policy=None, response_process=None):
        """
        VirtualDirectory1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'acl_policy': 'str',
            'remote_path': 'str',
            'virtual_host': 'str',
            'name': 'str',
            'enabled': 'bool',
            'listener_policy': 'str',
            'description': 'str',
            'request_process_type': 'str',
            'virtual_path': 'str',
            'error_template': 'str',
            'use_remote_policy': 'bool',
            'response_process_type': 'str',
            'remote_policy': 'str',
            'request_process': 'str',
            'request_filter_policy': 'str',
            'response_process': 'str'
        }

        self.attribute_map = {
            'acl_policy': 'aclPolicy',
            'remote_path': 'remotePath',
            'virtual_host': 'virtualHost',
            'name': 'name',
            'enabled': 'enabled',
            'listener_policy': 'listenerPolicy',
            'description': 'description',
            'request_process_type': 'requestProcessType',
            'virtual_path': 'virtualPath',
            'error_template': 'errorTemplate',
            'use_remote_policy': 'useRemotePolicy',
            'response_process_type': 'responseProcessType',
            'remote_policy': 'remotePolicy',
            'request_process': 'requestProcess',
            'request_filter_policy': 'requestFilterPolicy',
            'response_process': 'responseProcess'
        }

        self._acl_policy = acl_policy
        self._remote_path = remote_path
        self._virtual_host = virtual_host
        self._name = name
        self._enabled = enabled
        self._listener_policy = listener_policy
        self._description = description
        self._request_process_type = request_process_type
        self._virtual_path = virtual_path
        self._error_template = error_template
        self._use_remote_policy = use_remote_policy
        self._response_process_type = response_process_type
        self._remote_policy = remote_policy
        self._request_process = request_process
        self._request_filter_policy = request_filter_policy
        self._response_process = response_process

    @property
    def acl_policy(self):
        """
        Gets the acl_policy of this VirtualDirectory1.


        :return: The acl_policy of this VirtualDirectory1.
        :rtype: str
        """
        return self._acl_policy

    @acl_policy.setter
    def acl_policy(self, acl_policy):
        """
        Sets the acl_policy of this VirtualDirectory1.


        :param acl_policy: The acl_policy of this VirtualDirectory1.
        :type: str
        """

        self._acl_policy = acl_policy

    @property
    def remote_path(self):
        """
        Gets the remote_path of this VirtualDirectory1.


        :return: The remote_path of this VirtualDirectory1.
        :rtype: str
        """
        return self._remote_path

    @remote_path.setter
    def remote_path(self, remote_path):
        """
        Sets the remote_path of this VirtualDirectory1.


        :param remote_path: The remote_path of this VirtualDirectory1.
        :type: str
        """

        self._remote_path = remote_path

    @property
    def virtual_host(self):
        """
        Gets the virtual_host of this VirtualDirectory1.


        :return: The virtual_host of this VirtualDirectory1.
        :rtype: str
        """
        return self._virtual_host

    @virtual_host.setter
    def virtual_host(self, virtual_host):
        """
        Sets the virtual_host of this VirtualDirectory1.


        :param virtual_host: The virtual_host of this VirtualDirectory1.
        :type: str
        """

        self._virtual_host = virtual_host

    @property
    def name(self):
        """
        Gets the name of this VirtualDirectory1.


        :return: The name of this VirtualDirectory1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VirtualDirectory1.


        :param name: The name of this VirtualDirectory1.
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """
        Gets the enabled of this VirtualDirectory1.


        :return: The enabled of this VirtualDirectory1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this VirtualDirectory1.


        :param enabled: The enabled of this VirtualDirectory1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def listener_policy(self):
        """
        Gets the listener_policy of this VirtualDirectory1.


        :return: The listener_policy of this VirtualDirectory1.
        :rtype: str
        """
        return self._listener_policy

    @listener_policy.setter
    def listener_policy(self, listener_policy):
        """
        Sets the listener_policy of this VirtualDirectory1.


        :param listener_policy: The listener_policy of this VirtualDirectory1.
        :type: str
        """

        self._listener_policy = listener_policy

    @property
    def description(self):
        """
        Gets the description of this VirtualDirectory1.


        :return: The description of this VirtualDirectory1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VirtualDirectory1.


        :param description: The description of this VirtualDirectory1.
        :type: str
        """

        self._description = description

    @property
    def request_process_type(self):
        """
        Gets the request_process_type of this VirtualDirectory1.


        :return: The request_process_type of this VirtualDirectory1.
        :rtype: str
        """
        return self._request_process_type

    @request_process_type.setter
    def request_process_type(self, request_process_type):
        """
        Sets the request_process_type of this VirtualDirectory1.


        :param request_process_type: The request_process_type of this VirtualDirectory1.
        :type: str
        """
        allowed_values = ["TASK_LIST", "TASK_LIST_GROUP"]
        if request_process_type not in allowed_values:
            raise ValueError(
                "Invalid value for `request_process_type` ({0}), must be one of {1}"
                .format(request_process_type, allowed_values)
            )

        self._request_process_type = request_process_type

    @property
    def virtual_path(self):
        """
        Gets the virtual_path of this VirtualDirectory1.


        :return: The virtual_path of this VirtualDirectory1.
        :rtype: str
        """
        return self._virtual_path

    @virtual_path.setter
    def virtual_path(self, virtual_path):
        """
        Sets the virtual_path of this VirtualDirectory1.


        :param virtual_path: The virtual_path of this VirtualDirectory1.
        :type: str
        """

        self._virtual_path = virtual_path

    @property
    def error_template(self):
        """
        Gets the error_template of this VirtualDirectory1.


        :return: The error_template of this VirtualDirectory1.
        :rtype: str
        """
        return self._error_template

    @error_template.setter
    def error_template(self, error_template):
        """
        Sets the error_template of this VirtualDirectory1.


        :param error_template: The error_template of this VirtualDirectory1.
        :type: str
        """

        self._error_template = error_template

    @property
    def use_remote_policy(self):
        """
        Gets the use_remote_policy of this VirtualDirectory1.


        :return: The use_remote_policy of this VirtualDirectory1.
        :rtype: bool
        """
        return self._use_remote_policy

    @use_remote_policy.setter
    def use_remote_policy(self, use_remote_policy):
        """
        Sets the use_remote_policy of this VirtualDirectory1.


        :param use_remote_policy: The use_remote_policy of this VirtualDirectory1.
        :type: bool
        """

        self._use_remote_policy = use_remote_policy

    @property
    def response_process_type(self):
        """
        Gets the response_process_type of this VirtualDirectory1.


        :return: The response_process_type of this VirtualDirectory1.
        :rtype: str
        """
        return self._response_process_type

    @response_process_type.setter
    def response_process_type(self, response_process_type):
        """
        Sets the response_process_type of this VirtualDirectory1.


        :param response_process_type: The response_process_type of this VirtualDirectory1.
        :type: str
        """
        allowed_values = ["TASK_LIST", "TASK_LIST_GROUP"]
        if response_process_type not in allowed_values:
            raise ValueError(
                "Invalid value for `response_process_type` ({0}), must be one of {1}"
                .format(response_process_type, allowed_values)
            )

        self._response_process_type = response_process_type

    @property
    def remote_policy(self):
        """
        Gets the remote_policy of this VirtualDirectory1.


        :return: The remote_policy of this VirtualDirectory1.
        :rtype: str
        """
        return self._remote_policy

    @remote_policy.setter
    def remote_policy(self, remote_policy):
        """
        Sets the remote_policy of this VirtualDirectory1.


        :param remote_policy: The remote_policy of this VirtualDirectory1.
        :type: str
        """

        self._remote_policy = remote_policy

    @property
    def request_process(self):
        """
        Gets the request_process of this VirtualDirectory1.


        :return: The request_process of this VirtualDirectory1.
        :rtype: str
        """
        return self._request_process

    @request_process.setter
    def request_process(self, request_process):
        """
        Sets the request_process of this VirtualDirectory1.


        :param request_process: The request_process of this VirtualDirectory1.
        :type: str
        """

        self._request_process = request_process

    @property
    def request_filter_policy(self):
        """
        Gets the request_filter_policy of this VirtualDirectory1.


        :return: The request_filter_policy of this VirtualDirectory1.
        :rtype: str
        """
        return self._request_filter_policy

    @request_filter_policy.setter
    def request_filter_policy(self, request_filter_policy):
        """
        Sets the request_filter_policy of this VirtualDirectory1.


        :param request_filter_policy: The request_filter_policy of this VirtualDirectory1.
        :type: str
        """

        self._request_filter_policy = request_filter_policy

    @property
    def response_process(self):
        """
        Gets the response_process of this VirtualDirectory1.


        :return: The response_process of this VirtualDirectory1.
        :rtype: str
        """
        return self._response_process

    @response_process.setter
    def response_process(self, response_process):
        """
        Sets the response_process of this VirtualDirectory1.


        :param response_process: The response_process of this VirtualDirectory1.
        :type: str
        """

        self._response_process = response_process

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
