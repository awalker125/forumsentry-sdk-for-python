# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RestPolicies(object):
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
        'remote_path': 'str',
        'listener_policy': 'str',
        'name': 'str',
        'virtual_path': 'str',
        'remote_policy': 'str',
        'description': 'str',
        'request_process_type': 'str',
        'response_process_type': 'str',
        'idp_group': 'str',
        'request_process': 'str',
        'response_process': 'str'
    }

    attribute_map = {
        'remote_path': 'remotePath',
        'listener_policy': 'listenerPolicy',
        'name': 'name',
        'virtual_path': 'virtualPath',
        'remote_policy': 'remotePolicy',
        'description': 'description',
        'request_process_type': 'requestProcessType',
        'response_process_type': 'responseProcessType',
        'idp_group': 'idpGroup',
        'request_process': 'requestProcess',
        'response_process': 'responseProcess'
    }

    def __init__(self, remote_path=None, listener_policy=None, name=None, virtual_path=None, remote_policy=None, description=None, request_process_type=None, response_process_type=None, idp_group=None, request_process=None, response_process=None):  # noqa: E501
        """RestPolicies - a model defined in Swagger"""  # noqa: E501

        self._remote_path = None
        self._listener_policy = None
        self._name = None
        self._virtual_path = None
        self._remote_policy = None
        self._description = None
        self._request_process_type = None
        self._response_process_type = None
        self._idp_group = None
        self._request_process = None
        self._response_process = None
        self.discriminator = None

        if remote_path is not None:
            self.remote_path = remote_path
        if listener_policy is not None:
            self.listener_policy = listener_policy
        if name is not None:
            self.name = name
        if virtual_path is not None:
            self.virtual_path = virtual_path
        if remote_policy is not None:
            self.remote_policy = remote_policy
        if description is not None:
            self.description = description
        if request_process_type is not None:
            self.request_process_type = request_process_type
        if response_process_type is not None:
            self.response_process_type = response_process_type
        if idp_group is not None:
            self.idp_group = idp_group
        if request_process is not None:
            self.request_process = request_process
        if response_process is not None:
            self.response_process = response_process

    @property
    def remote_path(self):
        """Gets the remote_path of this RestPolicies.  # noqa: E501


        :return: The remote_path of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._remote_path

    @remote_path.setter
    def remote_path(self, remote_path):
        """Sets the remote_path of this RestPolicies.


        :param remote_path: The remote_path of this RestPolicies.  # noqa: E501
        :type: str
        """

        self._remote_path = remote_path

    @property
    def listener_policy(self):
        """Gets the listener_policy of this RestPolicies.  # noqa: E501


        :return: The listener_policy of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._listener_policy

    @listener_policy.setter
    def listener_policy(self, listener_policy):
        """Sets the listener_policy of this RestPolicies.


        :param listener_policy: The listener_policy of this RestPolicies.  # noqa: E501
        :type: str
        """

        self._listener_policy = listener_policy

    @property
    def name(self):
        """Gets the name of this RestPolicies.  # noqa: E501


        :return: The name of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RestPolicies.


        :param name: The name of this RestPolicies.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def virtual_path(self):
        """Gets the virtual_path of this RestPolicies.  # noqa: E501


        :return: The virtual_path of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._virtual_path

    @virtual_path.setter
    def virtual_path(self, virtual_path):
        """Sets the virtual_path of this RestPolicies.


        :param virtual_path: The virtual_path of this RestPolicies.  # noqa: E501
        :type: str
        """

        self._virtual_path = virtual_path

    @property
    def remote_policy(self):
        """Gets the remote_policy of this RestPolicies.  # noqa: E501


        :return: The remote_policy of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._remote_policy

    @remote_policy.setter
    def remote_policy(self, remote_policy):
        """Sets the remote_policy of this RestPolicies.


        :param remote_policy: The remote_policy of this RestPolicies.  # noqa: E501
        :type: str
        """

        self._remote_policy = remote_policy

    @property
    def description(self):
        """Gets the description of this RestPolicies.  # noqa: E501


        :return: The description of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RestPolicies.


        :param description: The description of this RestPolicies.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def request_process_type(self):
        """Gets the request_process_type of this RestPolicies.  # noqa: E501


        :return: The request_process_type of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._request_process_type

    @request_process_type.setter
    def request_process_type(self, request_process_type):
        """Sets the request_process_type of this RestPolicies.


        :param request_process_type: The request_process_type of this RestPolicies.  # noqa: E501
        :type: str
        """
        allowed_values = ["TASK_LIST", "TASK_LIST_GROUP"]  # noqa: E501
        if request_process_type not in allowed_values:
            raise ValueError(
                "Invalid value for `request_process_type` ({0}), must be one of {1}"  # noqa: E501
                .format(request_process_type, allowed_values)
            )

        self._request_process_type = request_process_type

    @property
    def response_process_type(self):
        """Gets the response_process_type of this RestPolicies.  # noqa: E501


        :return: The response_process_type of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._response_process_type

    @response_process_type.setter
    def response_process_type(self, response_process_type):
        """Sets the response_process_type of this RestPolicies.


        :param response_process_type: The response_process_type of this RestPolicies.  # noqa: E501
        :type: str
        """
        allowed_values = ["TASK_LIST", "TASK_LIST_GROUP"]  # noqa: E501
        if response_process_type not in allowed_values:
            raise ValueError(
                "Invalid value for `response_process_type` ({0}), must be one of {1}"  # noqa: E501
                .format(response_process_type, allowed_values)
            )

        self._response_process_type = response_process_type

    @property
    def idp_group(self):
        """Gets the idp_group of this RestPolicies.  # noqa: E501


        :return: The idp_group of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._idp_group

    @idp_group.setter
    def idp_group(self, idp_group):
        """Sets the idp_group of this RestPolicies.


        :param idp_group: The idp_group of this RestPolicies.  # noqa: E501
        :type: str
        """

        self._idp_group = idp_group

    @property
    def request_process(self):
        """Gets the request_process of this RestPolicies.  # noqa: E501


        :return: The request_process of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._request_process

    @request_process.setter
    def request_process(self, request_process):
        """Sets the request_process of this RestPolicies.


        :param request_process: The request_process of this RestPolicies.  # noqa: E501
        :type: str
        """

        self._request_process = request_process

    @property
    def response_process(self):
        """Gets the response_process of this RestPolicies.  # noqa: E501


        :return: The response_process of this RestPolicies.  # noqa: E501
        :rtype: str
        """
        return self._response_process

    @response_process.setter
    def response_process(self, response_process):
        """Sets the response_process of this RestPolicies.


        :param response_process: The response_process of this RestPolicies.  # noqa: E501
        :type: str
        """

        self._response_process = response_process

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
        if not isinstance(other, RestPolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
