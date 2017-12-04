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


class JbossListenerPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, acl_policy=None, host=None, number_of_sessions=None, user_name=None, is_password_auth=None, field=None, ignore_jms_reply_to=None, response_delivery_mode=None, name=None, destination=None, description=None, is_topic=None, enabled=None, is_synchronous=None, error_template=None, use_ssl=None, password=None, ssl_policy=None, port=None):
        """
        JbossListenerPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'acl_policy': 'str',
            'host': 'str',
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

        self.attribute_map = {
            'acl_policy': 'aclPolicy',
            'host': 'host',
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

        self._acl_policy = acl_policy
        self._host = host
        self._number_of_sessions = number_of_sessions
        self._user_name = user_name
        self._is_password_auth = is_password_auth
        self._field = field
        self._ignore_jms_reply_to = ignore_jms_reply_to
        self._response_delivery_mode = response_delivery_mode
        self._name = name
        self._destination = destination
        self._description = description
        self._is_topic = is_topic
        self._enabled = enabled
        self._is_synchronous = is_synchronous
        self._error_template = error_template
        self._use_ssl = use_ssl
        self._password = password
        self._ssl_policy = ssl_policy
        self._port = port

    @property
    def acl_policy(self):
        """
        Gets the acl_policy of this JbossListenerPolicy.


        :return: The acl_policy of this JbossListenerPolicy.
        :rtype: str
        """
        return self._acl_policy

    @acl_policy.setter
    def acl_policy(self, acl_policy):
        """
        Sets the acl_policy of this JbossListenerPolicy.


        :param acl_policy: The acl_policy of this JbossListenerPolicy.
        :type: str
        """

        self._acl_policy = acl_policy

    @property
    def host(self):
        """
        Gets the host of this JbossListenerPolicy.


        :return: The host of this JbossListenerPolicy.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this JbossListenerPolicy.


        :param host: The host of this JbossListenerPolicy.
        :type: str
        """

        self._host = host

    @property
    def number_of_sessions(self):
        """
        Gets the number_of_sessions of this JbossListenerPolicy.


        :return: The number_of_sessions of this JbossListenerPolicy.
        :rtype: int
        """
        return self._number_of_sessions

    @number_of_sessions.setter
    def number_of_sessions(self, number_of_sessions):
        """
        Sets the number_of_sessions of this JbossListenerPolicy.


        :param number_of_sessions: The number_of_sessions of this JbossListenerPolicy.
        :type: int
        """

        self._number_of_sessions = number_of_sessions

    @property
    def user_name(self):
        """
        Gets the user_name of this JbossListenerPolicy.


        :return: The user_name of this JbossListenerPolicy.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this JbossListenerPolicy.


        :param user_name: The user_name of this JbossListenerPolicy.
        :type: str
        """

        self._user_name = user_name

    @property
    def is_password_auth(self):
        """
        Gets the is_password_auth of this JbossListenerPolicy.


        :return: The is_password_auth of this JbossListenerPolicy.
        :rtype: bool
        """
        return self._is_password_auth

    @is_password_auth.setter
    def is_password_auth(self, is_password_auth):
        """
        Sets the is_password_auth of this JbossListenerPolicy.


        :param is_password_auth: The is_password_auth of this JbossListenerPolicy.
        :type: bool
        """

        self._is_password_auth = is_password_auth

    @property
    def field(self):
        """
        Gets the field of this JbossListenerPolicy.


        :return: The field of this JbossListenerPolicy.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this JbossListenerPolicy.


        :param field: The field of this JbossListenerPolicy.
        :type: str
        """

        self._field = field

    @property
    def ignore_jms_reply_to(self):
        """
        Gets the ignore_jms_reply_to of this JbossListenerPolicy.


        :return: The ignore_jms_reply_to of this JbossListenerPolicy.
        :rtype: bool
        """
        return self._ignore_jms_reply_to

    @ignore_jms_reply_to.setter
    def ignore_jms_reply_to(self, ignore_jms_reply_to):
        """
        Sets the ignore_jms_reply_to of this JbossListenerPolicy.


        :param ignore_jms_reply_to: The ignore_jms_reply_to of this JbossListenerPolicy.
        :type: bool
        """

        self._ignore_jms_reply_to = ignore_jms_reply_to

    @property
    def response_delivery_mode(self):
        """
        Gets the response_delivery_mode of this JbossListenerPolicy.


        :return: The response_delivery_mode of this JbossListenerPolicy.
        :rtype: int
        """
        return self._response_delivery_mode

    @response_delivery_mode.setter
    def response_delivery_mode(self, response_delivery_mode):
        """
        Sets the response_delivery_mode of this JbossListenerPolicy.


        :param response_delivery_mode: The response_delivery_mode of this JbossListenerPolicy.
        :type: int
        """

        self._response_delivery_mode = response_delivery_mode

    @property
    def name(self):
        """
        Gets the name of this JbossListenerPolicy.


        :return: The name of this JbossListenerPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this JbossListenerPolicy.


        :param name: The name of this JbossListenerPolicy.
        :type: str
        """

        self._name = name

    @property
    def destination(self):
        """
        Gets the destination of this JbossListenerPolicy.


        :return: The destination of this JbossListenerPolicy.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this JbossListenerPolicy.


        :param destination: The destination of this JbossListenerPolicy.
        :type: str
        """

        self._destination = destination

    @property
    def description(self):
        """
        Gets the description of this JbossListenerPolicy.


        :return: The description of this JbossListenerPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this JbossListenerPolicy.


        :param description: The description of this JbossListenerPolicy.
        :type: str
        """

        self._description = description

    @property
    def is_topic(self):
        """
        Gets the is_topic of this JbossListenerPolicy.


        :return: The is_topic of this JbossListenerPolicy.
        :rtype: bool
        """
        return self._is_topic

    @is_topic.setter
    def is_topic(self, is_topic):
        """
        Sets the is_topic of this JbossListenerPolicy.


        :param is_topic: The is_topic of this JbossListenerPolicy.
        :type: bool
        """

        self._is_topic = is_topic

    @property
    def enabled(self):
        """
        Gets the enabled of this JbossListenerPolicy.


        :return: The enabled of this JbossListenerPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this JbossListenerPolicy.


        :param enabled: The enabled of this JbossListenerPolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def is_synchronous(self):
        """
        Gets the is_synchronous of this JbossListenerPolicy.


        :return: The is_synchronous of this JbossListenerPolicy.
        :rtype: bool
        """
        return self._is_synchronous

    @is_synchronous.setter
    def is_synchronous(self, is_synchronous):
        """
        Sets the is_synchronous of this JbossListenerPolicy.


        :param is_synchronous: The is_synchronous of this JbossListenerPolicy.
        :type: bool
        """

        self._is_synchronous = is_synchronous

    @property
    def error_template(self):
        """
        Gets the error_template of this JbossListenerPolicy.


        :return: The error_template of this JbossListenerPolicy.
        :rtype: str
        """
        return self._error_template

    @error_template.setter
    def error_template(self, error_template):
        """
        Sets the error_template of this JbossListenerPolicy.


        :param error_template: The error_template of this JbossListenerPolicy.
        :type: str
        """

        self._error_template = error_template

    @property
    def use_ssl(self):
        """
        Gets the use_ssl of this JbossListenerPolicy.


        :return: The use_ssl of this JbossListenerPolicy.
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """
        Sets the use_ssl of this JbossListenerPolicy.


        :param use_ssl: The use_ssl of this JbossListenerPolicy.
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def password(self):
        """
        Gets the password of this JbossListenerPolicy.


        :return: The password of this JbossListenerPolicy.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this JbossListenerPolicy.


        :param password: The password of this JbossListenerPolicy.
        :type: str
        """

        self._password = password

    @property
    def ssl_policy(self):
        """
        Gets the ssl_policy of this JbossListenerPolicy.


        :return: The ssl_policy of this JbossListenerPolicy.
        :rtype: str
        """
        return self._ssl_policy

    @ssl_policy.setter
    def ssl_policy(self, ssl_policy):
        """
        Sets the ssl_policy of this JbossListenerPolicy.


        :param ssl_policy: The ssl_policy of this JbossListenerPolicy.
        :type: str
        """

        self._ssl_policy = ssl_policy

    @property
    def port(self):
        """
        Gets the port of this JbossListenerPolicy.


        :return: The port of this JbossListenerPolicy.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this JbossListenerPolicy.


        :param port: The port of this JbossListenerPolicy.
        :type: int
        """

        self._port = port

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
