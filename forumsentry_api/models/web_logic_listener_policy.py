# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WebLogicListenerPolicy(object):
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
        'acl_policy': 'str',
        'number_of_sessions': 'int',
        'user_name': 'str',
        'is_password_auth': 'bool',
        'field': 'str',
        'ignore_jms_reply_to': 'bool',
        'response_delivery_mode': 'int',
        'name': 'str',
        'destination': 'str',
        'description': 'str',
        'is_topic': 'bool',
        'enabled': 'bool',
        'is_synchronous': 'bool',
        'error_template': 'str',
        'use_ssl': 'bool',
        'password': 'str',
        'ssl_policy': 'str',
        'port': 'int'
    }

    attribute_map = {
        'acl_policy': 'aclPolicy',
        'number_of_sessions': 'numberOfSessions',
        'user_name': 'userName',
        'is_password_auth': 'isPasswordAuth',
        'field': 'field',
        'ignore_jms_reply_to': 'ignoreJmsReplyTo',
        'response_delivery_mode': 'responseDeliveryMode',
        'name': 'name',
        'destination': 'destination',
        'description': 'description',
        'is_topic': 'isTopic',
        'enabled': 'enabled',
        'is_synchronous': 'isSynchronous',
        'error_template': 'errorTemplate',
        'use_ssl': 'useSsl',
        'password': 'password',
        'ssl_policy': 'sslPolicy',
        'port': 'port'
    }

    def __init__(self, acl_policy=None, number_of_sessions=None, user_name=None, is_password_auth=None, field=None, ignore_jms_reply_to=None, response_delivery_mode=None, name=None, destination=None, description=None, is_topic=None, enabled=None, is_synchronous=None, error_template=None, use_ssl=None, password=None, ssl_policy=None, port=None):  # noqa: E501
        """WebLogicListenerPolicy - a model defined in Swagger"""  # noqa: E501

        self._acl_policy = None
        self._number_of_sessions = None
        self._user_name = None
        self._is_password_auth = None
        self._field = None
        self._ignore_jms_reply_to = None
        self._response_delivery_mode = None
        self._name = None
        self._destination = None
        self._description = None
        self._is_topic = None
        self._enabled = None
        self._is_synchronous = None
        self._error_template = None
        self._use_ssl = None
        self._password = None
        self._ssl_policy = None
        self._port = None
        self.discriminator = None

        if acl_policy is not None:
            self.acl_policy = acl_policy
        if number_of_sessions is not None:
            self.number_of_sessions = number_of_sessions
        if user_name is not None:
            self.user_name = user_name
        if is_password_auth is not None:
            self.is_password_auth = is_password_auth
        if field is not None:
            self.field = field
        if ignore_jms_reply_to is not None:
            self.ignore_jms_reply_to = ignore_jms_reply_to
        if response_delivery_mode is not None:
            self.response_delivery_mode = response_delivery_mode
        if name is not None:
            self.name = name
        if destination is not None:
            self.destination = destination
        if description is not None:
            self.description = description
        if is_topic is not None:
            self.is_topic = is_topic
        if enabled is not None:
            self.enabled = enabled
        if is_synchronous is not None:
            self.is_synchronous = is_synchronous
        if error_template is not None:
            self.error_template = error_template
        if use_ssl is not None:
            self.use_ssl = use_ssl
        if password is not None:
            self.password = password
        if ssl_policy is not None:
            self.ssl_policy = ssl_policy
        if port is not None:
            self.port = port

    @property
    def acl_policy(self):
        """Gets the acl_policy of this WebLogicListenerPolicy.  # noqa: E501


        :return: The acl_policy of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._acl_policy

    @acl_policy.setter
    def acl_policy(self, acl_policy):
        """Sets the acl_policy of this WebLogicListenerPolicy.


        :param acl_policy: The acl_policy of this WebLogicListenerPolicy.  # noqa: E501
        :type: str
        """

        self._acl_policy = acl_policy

    @property
    def number_of_sessions(self):
        """Gets the number_of_sessions of this WebLogicListenerPolicy.  # noqa: E501


        :return: The number_of_sessions of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: int
        """
        return self._number_of_sessions

    @number_of_sessions.setter
    def number_of_sessions(self, number_of_sessions):
        """Sets the number_of_sessions of this WebLogicListenerPolicy.


        :param number_of_sessions: The number_of_sessions of this WebLogicListenerPolicy.  # noqa: E501
        :type: int
        """

        self._number_of_sessions = number_of_sessions

    @property
    def user_name(self):
        """Gets the user_name of this WebLogicListenerPolicy.  # noqa: E501


        :return: The user_name of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this WebLogicListenerPolicy.


        :param user_name: The user_name of this WebLogicListenerPolicy.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def is_password_auth(self):
        """Gets the is_password_auth of this WebLogicListenerPolicy.  # noqa: E501


        :return: The is_password_auth of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._is_password_auth

    @is_password_auth.setter
    def is_password_auth(self, is_password_auth):
        """Sets the is_password_auth of this WebLogicListenerPolicy.


        :param is_password_auth: The is_password_auth of this WebLogicListenerPolicy.  # noqa: E501
        :type: bool
        """

        self._is_password_auth = is_password_auth

    @property
    def field(self):
        """Gets the field of this WebLogicListenerPolicy.  # noqa: E501


        :return: The field of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this WebLogicListenerPolicy.


        :param field: The field of this WebLogicListenerPolicy.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def ignore_jms_reply_to(self):
        """Gets the ignore_jms_reply_to of this WebLogicListenerPolicy.  # noqa: E501


        :return: The ignore_jms_reply_to of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_jms_reply_to

    @ignore_jms_reply_to.setter
    def ignore_jms_reply_to(self, ignore_jms_reply_to):
        """Sets the ignore_jms_reply_to of this WebLogicListenerPolicy.


        :param ignore_jms_reply_to: The ignore_jms_reply_to of this WebLogicListenerPolicy.  # noqa: E501
        :type: bool
        """

        self._ignore_jms_reply_to = ignore_jms_reply_to

    @property
    def response_delivery_mode(self):
        """Gets the response_delivery_mode of this WebLogicListenerPolicy.  # noqa: E501


        :return: The response_delivery_mode of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: int
        """
        return self._response_delivery_mode

    @response_delivery_mode.setter
    def response_delivery_mode(self, response_delivery_mode):
        """Sets the response_delivery_mode of this WebLogicListenerPolicy.


        :param response_delivery_mode: The response_delivery_mode of this WebLogicListenerPolicy.  # noqa: E501
        :type: int
        """

        self._response_delivery_mode = response_delivery_mode

    @property
    def name(self):
        """Gets the name of this WebLogicListenerPolicy.  # noqa: E501


        :return: The name of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebLogicListenerPolicy.


        :param name: The name of this WebLogicListenerPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def destination(self):
        """Gets the destination of this WebLogicListenerPolicy.  # noqa: E501


        :return: The destination of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this WebLogicListenerPolicy.


        :param destination: The destination of this WebLogicListenerPolicy.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def description(self):
        """Gets the description of this WebLogicListenerPolicy.  # noqa: E501


        :return: The description of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebLogicListenerPolicy.


        :param description: The description of this WebLogicListenerPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_topic(self):
        """Gets the is_topic of this WebLogicListenerPolicy.  # noqa: E501


        :return: The is_topic of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._is_topic

    @is_topic.setter
    def is_topic(self, is_topic):
        """Sets the is_topic of this WebLogicListenerPolicy.


        :param is_topic: The is_topic of this WebLogicListenerPolicy.  # noqa: E501
        :type: bool
        """

        self._is_topic = is_topic

    @property
    def enabled(self):
        """Gets the enabled of this WebLogicListenerPolicy.  # noqa: E501


        :return: The enabled of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WebLogicListenerPolicy.


        :param enabled: The enabled of this WebLogicListenerPolicy.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def is_synchronous(self):
        """Gets the is_synchronous of this WebLogicListenerPolicy.  # noqa: E501


        :return: The is_synchronous of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._is_synchronous

    @is_synchronous.setter
    def is_synchronous(self, is_synchronous):
        """Sets the is_synchronous of this WebLogicListenerPolicy.


        :param is_synchronous: The is_synchronous of this WebLogicListenerPolicy.  # noqa: E501
        :type: bool
        """

        self._is_synchronous = is_synchronous

    @property
    def error_template(self):
        """Gets the error_template of this WebLogicListenerPolicy.  # noqa: E501


        :return: The error_template of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._error_template

    @error_template.setter
    def error_template(self, error_template):
        """Sets the error_template of this WebLogicListenerPolicy.


        :param error_template: The error_template of this WebLogicListenerPolicy.  # noqa: E501
        :type: str
        """

        self._error_template = error_template

    @property
    def use_ssl(self):
        """Gets the use_ssl of this WebLogicListenerPolicy.  # noqa: E501


        :return: The use_ssl of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this WebLogicListenerPolicy.


        :param use_ssl: The use_ssl of this WebLogicListenerPolicy.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def password(self):
        """Gets the password of this WebLogicListenerPolicy.  # noqa: E501


        :return: The password of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this WebLogicListenerPolicy.


        :param password: The password of this WebLogicListenerPolicy.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def ssl_policy(self):
        """Gets the ssl_policy of this WebLogicListenerPolicy.  # noqa: E501


        :return: The ssl_policy of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: str
        """
        return self._ssl_policy

    @ssl_policy.setter
    def ssl_policy(self, ssl_policy):
        """Sets the ssl_policy of this WebLogicListenerPolicy.


        :param ssl_policy: The ssl_policy of this WebLogicListenerPolicy.  # noqa: E501
        :type: str
        """

        self._ssl_policy = ssl_policy

    @property
    def port(self):
        """Gets the port of this WebLogicListenerPolicy.  # noqa: E501


        :return: The port of this WebLogicListenerPolicy.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this WebLogicListenerPolicy.


        :param port: The port of this WebLogicListenerPolicy.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if not isinstance(other, WebLogicListenerPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
