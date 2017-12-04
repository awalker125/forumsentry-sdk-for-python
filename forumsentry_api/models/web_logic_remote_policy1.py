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


class WebLogicRemotePolicy1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, req_password=None, req_field=None, jms_priority=None, sync_timeout_millis=None, rep_queue_temp=None, req_user_name=None, propagate_reply_to=None, req_topic=None, name=None, req_destination=None, rep_allowed_message_types=None, description=None, propagate_ttl=None, req_message_type=None, enabled=None, synchronous=None, time_to_live_seconds=None, use_ssl=None, req_delivery_mode=None, process_response=None, ssl_policy=None, rep_topic=None, port=None, rep_destination=None):
        """
        WebLogicRemotePolicy1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'req_password': 'str',
            'req_field': 'str',
            'jms_priority': 'int',
            'sync_timeout_millis': 'int',
            'rep_queue_temp': 'bool',
            'req_user_name': 'str',
            'propagate_reply_to': 'bool',
            'req_topic': 'bool',
            'name': 'str',
            'req_destination': 'str',
            'rep_allowed_message_types': 'int',
            'description': 'str',
            'propagate_ttl': 'bool',
            'req_message_type': 'int',
            'enabled': 'bool',
            'synchronous': 'bool',
            'time_to_live_seconds': 'int',
            'use_ssl': 'bool',
            'req_delivery_mode': 'int',
            'process_response': 'bool',
            'ssl_policy': 'str',
            'rep_topic': 'bool',
            'port': 'int',
            'rep_destination': 'str'
        }

        self.attribute_map = {
            'req_password': 'reqPassword',
            'req_field': 'reqField',
            'jms_priority': 'jmsPriority',
            'sync_timeout_millis': 'syncTimeoutMillis',
            'rep_queue_temp': 'repQueueTemp',
            'req_user_name': 'reqUserName',
            'propagate_reply_to': 'propagateReplyTo',
            'req_topic': 'reqTopic',
            'name': 'name',
            'req_destination': 'reqDestination',
            'rep_allowed_message_types': 'repAllowedMessageTypes',
            'description': 'description',
            'propagate_ttl': 'propagateTtl',
            'req_message_type': 'reqMessageType',
            'enabled': 'enabled',
            'synchronous': 'synchronous',
            'time_to_live_seconds': 'timeToLiveSeconds',
            'use_ssl': 'useSSL',
            'req_delivery_mode': 'reqDeliveryMode',
            'process_response': 'processResponse',
            'ssl_policy': 'sslPolicy',
            'rep_topic': 'repTopic',
            'port': 'port',
            'rep_destination': 'repDestination'
        }

        self._req_password = req_password
        self._req_field = req_field
        self._jms_priority = jms_priority
        self._sync_timeout_millis = sync_timeout_millis
        self._rep_queue_temp = rep_queue_temp
        self._req_user_name = req_user_name
        self._propagate_reply_to = propagate_reply_to
        self._req_topic = req_topic
        self._name = name
        self._req_destination = req_destination
        self._rep_allowed_message_types = rep_allowed_message_types
        self._description = description
        self._propagate_ttl = propagate_ttl
        self._req_message_type = req_message_type
        self._enabled = enabled
        self._synchronous = synchronous
        self._time_to_live_seconds = time_to_live_seconds
        self._use_ssl = use_ssl
        self._req_delivery_mode = req_delivery_mode
        self._process_response = process_response
        self._ssl_policy = ssl_policy
        self._rep_topic = rep_topic
        self._port = port
        self._rep_destination = rep_destination

    @property
    def req_password(self):
        """
        Gets the req_password of this WebLogicRemotePolicy1.


        :return: The req_password of this WebLogicRemotePolicy1.
        :rtype: str
        """
        return self._req_password

    @req_password.setter
    def req_password(self, req_password):
        """
        Sets the req_password of this WebLogicRemotePolicy1.


        :param req_password: The req_password of this WebLogicRemotePolicy1.
        :type: str
        """

        self._req_password = req_password

    @property
    def req_field(self):
        """
        Gets the req_field of this WebLogicRemotePolicy1.


        :return: The req_field of this WebLogicRemotePolicy1.
        :rtype: str
        """
        return self._req_field

    @req_field.setter
    def req_field(self, req_field):
        """
        Sets the req_field of this WebLogicRemotePolicy1.


        :param req_field: The req_field of this WebLogicRemotePolicy1.
        :type: str
        """

        self._req_field = req_field

    @property
    def jms_priority(self):
        """
        Gets the jms_priority of this WebLogicRemotePolicy1.


        :return: The jms_priority of this WebLogicRemotePolicy1.
        :rtype: int
        """
        return self._jms_priority

    @jms_priority.setter
    def jms_priority(self, jms_priority):
        """
        Sets the jms_priority of this WebLogicRemotePolicy1.


        :param jms_priority: The jms_priority of this WebLogicRemotePolicy1.
        :type: int
        """

        self._jms_priority = jms_priority

    @property
    def sync_timeout_millis(self):
        """
        Gets the sync_timeout_millis of this WebLogicRemotePolicy1.


        :return: The sync_timeout_millis of this WebLogicRemotePolicy1.
        :rtype: int
        """
        return self._sync_timeout_millis

    @sync_timeout_millis.setter
    def sync_timeout_millis(self, sync_timeout_millis):
        """
        Sets the sync_timeout_millis of this WebLogicRemotePolicy1.


        :param sync_timeout_millis: The sync_timeout_millis of this WebLogicRemotePolicy1.
        :type: int
        """

        self._sync_timeout_millis = sync_timeout_millis

    @property
    def rep_queue_temp(self):
        """
        Gets the rep_queue_temp of this WebLogicRemotePolicy1.


        :return: The rep_queue_temp of this WebLogicRemotePolicy1.
        :rtype: bool
        """
        return self._rep_queue_temp

    @rep_queue_temp.setter
    def rep_queue_temp(self, rep_queue_temp):
        """
        Sets the rep_queue_temp of this WebLogicRemotePolicy1.


        :param rep_queue_temp: The rep_queue_temp of this WebLogicRemotePolicy1.
        :type: bool
        """

        self._rep_queue_temp = rep_queue_temp

    @property
    def req_user_name(self):
        """
        Gets the req_user_name of this WebLogicRemotePolicy1.


        :return: The req_user_name of this WebLogicRemotePolicy1.
        :rtype: str
        """
        return self._req_user_name

    @req_user_name.setter
    def req_user_name(self, req_user_name):
        """
        Sets the req_user_name of this WebLogicRemotePolicy1.


        :param req_user_name: The req_user_name of this WebLogicRemotePolicy1.
        :type: str
        """

        self._req_user_name = req_user_name

    @property
    def propagate_reply_to(self):
        """
        Gets the propagate_reply_to of this WebLogicRemotePolicy1.


        :return: The propagate_reply_to of this WebLogicRemotePolicy1.
        :rtype: bool
        """
        return self._propagate_reply_to

    @propagate_reply_to.setter
    def propagate_reply_to(self, propagate_reply_to):
        """
        Sets the propagate_reply_to of this WebLogicRemotePolicy1.


        :param propagate_reply_to: The propagate_reply_to of this WebLogicRemotePolicy1.
        :type: bool
        """

        self._propagate_reply_to = propagate_reply_to

    @property
    def req_topic(self):
        """
        Gets the req_topic of this WebLogicRemotePolicy1.


        :return: The req_topic of this WebLogicRemotePolicy1.
        :rtype: bool
        """
        return self._req_topic

    @req_topic.setter
    def req_topic(self, req_topic):
        """
        Sets the req_topic of this WebLogicRemotePolicy1.


        :param req_topic: The req_topic of this WebLogicRemotePolicy1.
        :type: bool
        """

        self._req_topic = req_topic

    @property
    def name(self):
        """
        Gets the name of this WebLogicRemotePolicy1.


        :return: The name of this WebLogicRemotePolicy1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WebLogicRemotePolicy1.


        :param name: The name of this WebLogicRemotePolicy1.
        :type: str
        """

        self._name = name

    @property
    def req_destination(self):
        """
        Gets the req_destination of this WebLogicRemotePolicy1.


        :return: The req_destination of this WebLogicRemotePolicy1.
        :rtype: str
        """
        return self._req_destination

    @req_destination.setter
    def req_destination(self, req_destination):
        """
        Sets the req_destination of this WebLogicRemotePolicy1.


        :param req_destination: The req_destination of this WebLogicRemotePolicy1.
        :type: str
        """

        self._req_destination = req_destination

    @property
    def rep_allowed_message_types(self):
        """
        Gets the rep_allowed_message_types of this WebLogicRemotePolicy1.


        :return: The rep_allowed_message_types of this WebLogicRemotePolicy1.
        :rtype: int
        """
        return self._rep_allowed_message_types

    @rep_allowed_message_types.setter
    def rep_allowed_message_types(self, rep_allowed_message_types):
        """
        Sets the rep_allowed_message_types of this WebLogicRemotePolicy1.


        :param rep_allowed_message_types: The rep_allowed_message_types of this WebLogicRemotePolicy1.
        :type: int
        """

        self._rep_allowed_message_types = rep_allowed_message_types

    @property
    def description(self):
        """
        Gets the description of this WebLogicRemotePolicy1.


        :return: The description of this WebLogicRemotePolicy1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WebLogicRemotePolicy1.


        :param description: The description of this WebLogicRemotePolicy1.
        :type: str
        """

        self._description = description

    @property
    def propagate_ttl(self):
        """
        Gets the propagate_ttl of this WebLogicRemotePolicy1.


        :return: The propagate_ttl of this WebLogicRemotePolicy1.
        :rtype: bool
        """
        return self._propagate_ttl

    @propagate_ttl.setter
    def propagate_ttl(self, propagate_ttl):
        """
        Sets the propagate_ttl of this WebLogicRemotePolicy1.


        :param propagate_ttl: The propagate_ttl of this WebLogicRemotePolicy1.
        :type: bool
        """

        self._propagate_ttl = propagate_ttl

    @property
    def req_message_type(self):
        """
        Gets the req_message_type of this WebLogicRemotePolicy1.


        :return: The req_message_type of this WebLogicRemotePolicy1.
        :rtype: int
        """
        return self._req_message_type

    @req_message_type.setter
    def req_message_type(self, req_message_type):
        """
        Sets the req_message_type of this WebLogicRemotePolicy1.


        :param req_message_type: The req_message_type of this WebLogicRemotePolicy1.
        :type: int
        """

        self._req_message_type = req_message_type

    @property
    def enabled(self):
        """
        Gets the enabled of this WebLogicRemotePolicy1.


        :return: The enabled of this WebLogicRemotePolicy1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this WebLogicRemotePolicy1.


        :param enabled: The enabled of this WebLogicRemotePolicy1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def synchronous(self):
        """
        Gets the synchronous of this WebLogicRemotePolicy1.


        :return: The synchronous of this WebLogicRemotePolicy1.
        :rtype: bool
        """
        return self._synchronous

    @synchronous.setter
    def synchronous(self, synchronous):
        """
        Sets the synchronous of this WebLogicRemotePolicy1.


        :param synchronous: The synchronous of this WebLogicRemotePolicy1.
        :type: bool
        """

        self._synchronous = synchronous

    @property
    def time_to_live_seconds(self):
        """
        Gets the time_to_live_seconds of this WebLogicRemotePolicy1.


        :return: The time_to_live_seconds of this WebLogicRemotePolicy1.
        :rtype: int
        """
        return self._time_to_live_seconds

    @time_to_live_seconds.setter
    def time_to_live_seconds(self, time_to_live_seconds):
        """
        Sets the time_to_live_seconds of this WebLogicRemotePolicy1.


        :param time_to_live_seconds: The time_to_live_seconds of this WebLogicRemotePolicy1.
        :type: int
        """

        self._time_to_live_seconds = time_to_live_seconds

    @property
    def use_ssl(self):
        """
        Gets the use_ssl of this WebLogicRemotePolicy1.


        :return: The use_ssl of this WebLogicRemotePolicy1.
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """
        Sets the use_ssl of this WebLogicRemotePolicy1.


        :param use_ssl: The use_ssl of this WebLogicRemotePolicy1.
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def req_delivery_mode(self):
        """
        Gets the req_delivery_mode of this WebLogicRemotePolicy1.


        :return: The req_delivery_mode of this WebLogicRemotePolicy1.
        :rtype: int
        """
        return self._req_delivery_mode

    @req_delivery_mode.setter
    def req_delivery_mode(self, req_delivery_mode):
        """
        Sets the req_delivery_mode of this WebLogicRemotePolicy1.


        :param req_delivery_mode: The req_delivery_mode of this WebLogicRemotePolicy1.
        :type: int
        """

        self._req_delivery_mode = req_delivery_mode

    @property
    def process_response(self):
        """
        Gets the process_response of this WebLogicRemotePolicy1.


        :return: The process_response of this WebLogicRemotePolicy1.
        :rtype: bool
        """
        return self._process_response

    @process_response.setter
    def process_response(self, process_response):
        """
        Sets the process_response of this WebLogicRemotePolicy1.


        :param process_response: The process_response of this WebLogicRemotePolicy1.
        :type: bool
        """

        self._process_response = process_response

    @property
    def ssl_policy(self):
        """
        Gets the ssl_policy of this WebLogicRemotePolicy1.


        :return: The ssl_policy of this WebLogicRemotePolicy1.
        :rtype: str
        """
        return self._ssl_policy

    @ssl_policy.setter
    def ssl_policy(self, ssl_policy):
        """
        Sets the ssl_policy of this WebLogicRemotePolicy1.


        :param ssl_policy: The ssl_policy of this WebLogicRemotePolicy1.
        :type: str
        """

        self._ssl_policy = ssl_policy

    @property
    def rep_topic(self):
        """
        Gets the rep_topic of this WebLogicRemotePolicy1.


        :return: The rep_topic of this WebLogicRemotePolicy1.
        :rtype: bool
        """
        return self._rep_topic

    @rep_topic.setter
    def rep_topic(self, rep_topic):
        """
        Sets the rep_topic of this WebLogicRemotePolicy1.


        :param rep_topic: The rep_topic of this WebLogicRemotePolicy1.
        :type: bool
        """

        self._rep_topic = rep_topic

    @property
    def port(self):
        """
        Gets the port of this WebLogicRemotePolicy1.


        :return: The port of this WebLogicRemotePolicy1.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this WebLogicRemotePolicy1.


        :param port: The port of this WebLogicRemotePolicy1.
        :type: int
        """

        self._port = port

    @property
    def rep_destination(self):
        """
        Gets the rep_destination of this WebLogicRemotePolicy1.


        :return: The rep_destination of this WebLogicRemotePolicy1.
        :rtype: str
        """
        return self._rep_destination

    @rep_destination.setter
    def rep_destination(self, rep_destination):
        """
        Sets the rep_destination of this WebLogicRemotePolicy1.


        :param rep_destination: The rep_destination of this WebLogicRemotePolicy1.
        :type: str
        """

        self._rep_destination = rep_destination

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
