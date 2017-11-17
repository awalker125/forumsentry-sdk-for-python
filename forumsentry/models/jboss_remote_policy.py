# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

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


class JbossRemotePolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, process_response=None, synchronous=None, req_destination=None, req_topic=None, req_delivery_mode=None, req_message_type=None, req_field=None, req_user_name=None, req_password=None, rep_topic=None, rep_destination=None, rep_field=None, rep_allowed_message_types=None, initial_pool_connections=None, jms_priority=None, ssl_policy=None, use_ssl=None, rep_queue_temp=None, sync_timeout_millis=None, time_to_live_seconds=None, propagate_reply_to=None, propagate_ttl=None, host=None, port=None, enabled=None, comment=None):
        """
        JbossRemotePolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'process_response': 'bool',
            'synchronous': 'bool',
            'req_destination': 'str',
            'req_topic': 'bool',
            'req_delivery_mode': 'int',
            'req_message_type': 'int',
            'req_field': 'str',
            'req_user_name': 'str',
            'req_password': 'str',
            'rep_topic': 'bool',
            'rep_destination': 'str',
            'rep_field': 'str',
            'rep_allowed_message_types': 'int',
            'initial_pool_connections': 'int',
            'jms_priority': 'int',
            'ssl_policy': 'str',
            'use_ssl': 'bool',
            'rep_queue_temp': 'bool',
            'sync_timeout_millis': 'int',
            'time_to_live_seconds': 'int',
            'propagate_reply_to': 'bool',
            'propagate_ttl': 'bool',
            'host': 'str',
            'port': 'int',
            'enabled': 'bool',
            'comment': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'process_response': 'processResponse',
            'synchronous': 'synchronous',
            'req_destination': 'reqDestination',
            'req_topic': 'reqTopic',
            'req_delivery_mode': 'reqDeliveryMode',
            'req_message_type': 'reqMessageType',
            'req_field': 'reqField',
            'req_user_name': 'reqUserName',
            'req_password': 'reqPassword',
            'rep_topic': 'repTopic',
            'rep_destination': 'repDestination',
            'rep_field': 'repField',
            'rep_allowed_message_types': 'repAllowedMessageTypes',
            'initial_pool_connections': 'initialPoolConnections',
            'jms_priority': 'jmsPriority',
            'ssl_policy': 'sslPolicy',
            'use_ssl': 'useSSL',
            'rep_queue_temp': 'repQueueTemp',
            'sync_timeout_millis': 'syncTimeoutMillis',
            'time_to_live_seconds': 'timeToLiveSeconds',
            'propagate_reply_to': 'propagateReplyTo',
            'propagate_ttl': 'propagateTtl',
            'host': 'host',
            'port': 'port',
            'enabled': 'enabled',
            'comment': 'comment'
        }

        self._name = name
        self._description = description
        self._process_response = process_response
        self._synchronous = synchronous
        self._req_destination = req_destination
        self._req_topic = req_topic
        self._req_delivery_mode = req_delivery_mode
        self._req_message_type = req_message_type
        self._req_field = req_field
        self._req_user_name = req_user_name
        self._req_password = req_password
        self._rep_topic = rep_topic
        self._rep_destination = rep_destination
        self._rep_field = rep_field
        self._rep_allowed_message_types = rep_allowed_message_types
        self._initial_pool_connections = initial_pool_connections
        self._jms_priority = jms_priority
        self._ssl_policy = ssl_policy
        self._use_ssl = use_ssl
        self._rep_queue_temp = rep_queue_temp
        self._sync_timeout_millis = sync_timeout_millis
        self._time_to_live_seconds = time_to_live_seconds
        self._propagate_reply_to = propagate_reply_to
        self._propagate_ttl = propagate_ttl
        self._host = host
        self._port = port
        self._enabled = enabled
        self._comment = comment

    @property
    def name(self):
        """
        Gets the name of this JbossRemotePolicy.


        :return: The name of this JbossRemotePolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this JbossRemotePolicy.


        :param name: The name of this JbossRemotePolicy.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this JbossRemotePolicy.


        :return: The description of this JbossRemotePolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this JbossRemotePolicy.


        :param description: The description of this JbossRemotePolicy.
        :type: str
        """

        self._description = description

    @property
    def process_response(self):
        """
        Gets the process_response of this JbossRemotePolicy.


        :return: The process_response of this JbossRemotePolicy.
        :rtype: bool
        """
        return self._process_response

    @process_response.setter
    def process_response(self, process_response):
        """
        Sets the process_response of this JbossRemotePolicy.


        :param process_response: The process_response of this JbossRemotePolicy.
        :type: bool
        """

        self._process_response = process_response

    @property
    def synchronous(self):
        """
        Gets the synchronous of this JbossRemotePolicy.


        :return: The synchronous of this JbossRemotePolicy.
        :rtype: bool
        """
        return self._synchronous

    @synchronous.setter
    def synchronous(self, synchronous):
        """
        Sets the synchronous of this JbossRemotePolicy.


        :param synchronous: The synchronous of this JbossRemotePolicy.
        :type: bool
        """

        self._synchronous = synchronous

    @property
    def req_destination(self):
        """
        Gets the req_destination of this JbossRemotePolicy.


        :return: The req_destination of this JbossRemotePolicy.
        :rtype: str
        """
        return self._req_destination

    @req_destination.setter
    def req_destination(self, req_destination):
        """
        Sets the req_destination of this JbossRemotePolicy.


        :param req_destination: The req_destination of this JbossRemotePolicy.
        :type: str
        """

        self._req_destination = req_destination

    @property
    def req_topic(self):
        """
        Gets the req_topic of this JbossRemotePolicy.


        :return: The req_topic of this JbossRemotePolicy.
        :rtype: bool
        """
        return self._req_topic

    @req_topic.setter
    def req_topic(self, req_topic):
        """
        Sets the req_topic of this JbossRemotePolicy.


        :param req_topic: The req_topic of this JbossRemotePolicy.
        :type: bool
        """

        self._req_topic = req_topic

    @property
    def req_delivery_mode(self):
        """
        Gets the req_delivery_mode of this JbossRemotePolicy.


        :return: The req_delivery_mode of this JbossRemotePolicy.
        :rtype: int
        """
        return self._req_delivery_mode

    @req_delivery_mode.setter
    def req_delivery_mode(self, req_delivery_mode):
        """
        Sets the req_delivery_mode of this JbossRemotePolicy.


        :param req_delivery_mode: The req_delivery_mode of this JbossRemotePolicy.
        :type: int
        """

        self._req_delivery_mode = req_delivery_mode

    @property
    def req_message_type(self):
        """
        Gets the req_message_type of this JbossRemotePolicy.


        :return: The req_message_type of this JbossRemotePolicy.
        :rtype: int
        """
        return self._req_message_type

    @req_message_type.setter
    def req_message_type(self, req_message_type):
        """
        Sets the req_message_type of this JbossRemotePolicy.


        :param req_message_type: The req_message_type of this JbossRemotePolicy.
        :type: int
        """

        self._req_message_type = req_message_type

    @property
    def req_field(self):
        """
        Gets the req_field of this JbossRemotePolicy.


        :return: The req_field of this JbossRemotePolicy.
        :rtype: str
        """
        return self._req_field

    @req_field.setter
    def req_field(self, req_field):
        """
        Sets the req_field of this JbossRemotePolicy.


        :param req_field: The req_field of this JbossRemotePolicy.
        :type: str
        """

        self._req_field = req_field

    @property
    def req_user_name(self):
        """
        Gets the req_user_name of this JbossRemotePolicy.


        :return: The req_user_name of this JbossRemotePolicy.
        :rtype: str
        """
        return self._req_user_name

    @req_user_name.setter
    def req_user_name(self, req_user_name):
        """
        Sets the req_user_name of this JbossRemotePolicy.


        :param req_user_name: The req_user_name of this JbossRemotePolicy.
        :type: str
        """

        self._req_user_name = req_user_name

    @property
    def req_password(self):
        """
        Gets the req_password of this JbossRemotePolicy.


        :return: The req_password of this JbossRemotePolicy.
        :rtype: str
        """
        return self._req_password

    @req_password.setter
    def req_password(self, req_password):
        """
        Sets the req_password of this JbossRemotePolicy.


        :param req_password: The req_password of this JbossRemotePolicy.
        :type: str
        """

        self._req_password = req_password

    @property
    def rep_topic(self):
        """
        Gets the rep_topic of this JbossRemotePolicy.


        :return: The rep_topic of this JbossRemotePolicy.
        :rtype: bool
        """
        return self._rep_topic

    @rep_topic.setter
    def rep_topic(self, rep_topic):
        """
        Sets the rep_topic of this JbossRemotePolicy.


        :param rep_topic: The rep_topic of this JbossRemotePolicy.
        :type: bool
        """

        self._rep_topic = rep_topic

    @property
    def rep_destination(self):
        """
        Gets the rep_destination of this JbossRemotePolicy.


        :return: The rep_destination of this JbossRemotePolicy.
        :rtype: str
        """
        return self._rep_destination

    @rep_destination.setter
    def rep_destination(self, rep_destination):
        """
        Sets the rep_destination of this JbossRemotePolicy.


        :param rep_destination: The rep_destination of this JbossRemotePolicy.
        :type: str
        """

        self._rep_destination = rep_destination

    @property
    def rep_field(self):
        """
        Gets the rep_field of this JbossRemotePolicy.


        :return: The rep_field of this JbossRemotePolicy.
        :rtype: str
        """
        return self._rep_field

    @rep_field.setter
    def rep_field(self, rep_field):
        """
        Sets the rep_field of this JbossRemotePolicy.


        :param rep_field: The rep_field of this JbossRemotePolicy.
        :type: str
        """

        self._rep_field = rep_field

    @property
    def rep_allowed_message_types(self):
        """
        Gets the rep_allowed_message_types of this JbossRemotePolicy.


        :return: The rep_allowed_message_types of this JbossRemotePolicy.
        :rtype: int
        """
        return self._rep_allowed_message_types

    @rep_allowed_message_types.setter
    def rep_allowed_message_types(self, rep_allowed_message_types):
        """
        Sets the rep_allowed_message_types of this JbossRemotePolicy.


        :param rep_allowed_message_types: The rep_allowed_message_types of this JbossRemotePolicy.
        :type: int
        """

        self._rep_allowed_message_types = rep_allowed_message_types

    @property
    def initial_pool_connections(self):
        """
        Gets the initial_pool_connections of this JbossRemotePolicy.


        :return: The initial_pool_connections of this JbossRemotePolicy.
        :rtype: int
        """
        return self._initial_pool_connections

    @initial_pool_connections.setter
    def initial_pool_connections(self, initial_pool_connections):
        """
        Sets the initial_pool_connections of this JbossRemotePolicy.


        :param initial_pool_connections: The initial_pool_connections of this JbossRemotePolicy.
        :type: int
        """

        self._initial_pool_connections = initial_pool_connections

    @property
    def jms_priority(self):
        """
        Gets the jms_priority of this JbossRemotePolicy.


        :return: The jms_priority of this JbossRemotePolicy.
        :rtype: int
        """
        return self._jms_priority

    @jms_priority.setter
    def jms_priority(self, jms_priority):
        """
        Sets the jms_priority of this JbossRemotePolicy.


        :param jms_priority: The jms_priority of this JbossRemotePolicy.
        :type: int
        """

        self._jms_priority = jms_priority

    @property
    def ssl_policy(self):
        """
        Gets the ssl_policy of this JbossRemotePolicy.


        :return: The ssl_policy of this JbossRemotePolicy.
        :rtype: str
        """
        return self._ssl_policy

    @ssl_policy.setter
    def ssl_policy(self, ssl_policy):
        """
        Sets the ssl_policy of this JbossRemotePolicy.


        :param ssl_policy: The ssl_policy of this JbossRemotePolicy.
        :type: str
        """

        self._ssl_policy = ssl_policy

    @property
    def use_ssl(self):
        """
        Gets the use_ssl of this JbossRemotePolicy.


        :return: The use_ssl of this JbossRemotePolicy.
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """
        Sets the use_ssl of this JbossRemotePolicy.


        :param use_ssl: The use_ssl of this JbossRemotePolicy.
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def rep_queue_temp(self):
        """
        Gets the rep_queue_temp of this JbossRemotePolicy.


        :return: The rep_queue_temp of this JbossRemotePolicy.
        :rtype: bool
        """
        return self._rep_queue_temp

    @rep_queue_temp.setter
    def rep_queue_temp(self, rep_queue_temp):
        """
        Sets the rep_queue_temp of this JbossRemotePolicy.


        :param rep_queue_temp: The rep_queue_temp of this JbossRemotePolicy.
        :type: bool
        """

        self._rep_queue_temp = rep_queue_temp

    @property
    def sync_timeout_millis(self):
        """
        Gets the sync_timeout_millis of this JbossRemotePolicy.


        :return: The sync_timeout_millis of this JbossRemotePolicy.
        :rtype: int
        """
        return self._sync_timeout_millis

    @sync_timeout_millis.setter
    def sync_timeout_millis(self, sync_timeout_millis):
        """
        Sets the sync_timeout_millis of this JbossRemotePolicy.


        :param sync_timeout_millis: The sync_timeout_millis of this JbossRemotePolicy.
        :type: int
        """

        self._sync_timeout_millis = sync_timeout_millis

    @property
    def time_to_live_seconds(self):
        """
        Gets the time_to_live_seconds of this JbossRemotePolicy.


        :return: The time_to_live_seconds of this JbossRemotePolicy.
        :rtype: int
        """
        return self._time_to_live_seconds

    @time_to_live_seconds.setter
    def time_to_live_seconds(self, time_to_live_seconds):
        """
        Sets the time_to_live_seconds of this JbossRemotePolicy.


        :param time_to_live_seconds: The time_to_live_seconds of this JbossRemotePolicy.
        :type: int
        """

        self._time_to_live_seconds = time_to_live_seconds

    @property
    def propagate_reply_to(self):
        """
        Gets the propagate_reply_to of this JbossRemotePolicy.


        :return: The propagate_reply_to of this JbossRemotePolicy.
        :rtype: bool
        """
        return self._propagate_reply_to

    @propagate_reply_to.setter
    def propagate_reply_to(self, propagate_reply_to):
        """
        Sets the propagate_reply_to of this JbossRemotePolicy.


        :param propagate_reply_to: The propagate_reply_to of this JbossRemotePolicy.
        :type: bool
        """

        self._propagate_reply_to = propagate_reply_to

    @property
    def propagate_ttl(self):
        """
        Gets the propagate_ttl of this JbossRemotePolicy.


        :return: The propagate_ttl of this JbossRemotePolicy.
        :rtype: bool
        """
        return self._propagate_ttl

    @propagate_ttl.setter
    def propagate_ttl(self, propagate_ttl):
        """
        Sets the propagate_ttl of this JbossRemotePolicy.


        :param propagate_ttl: The propagate_ttl of this JbossRemotePolicy.
        :type: bool
        """

        self._propagate_ttl = propagate_ttl

    @property
    def host(self):
        """
        Gets the host of this JbossRemotePolicy.


        :return: The host of this JbossRemotePolicy.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this JbossRemotePolicy.


        :param host: The host of this JbossRemotePolicy.
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """
        Gets the port of this JbossRemotePolicy.


        :return: The port of this JbossRemotePolicy.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this JbossRemotePolicy.


        :param port: The port of this JbossRemotePolicy.
        :type: int
        """

        self._port = port

    @property
    def enabled(self):
        """
        Gets the enabled of this JbossRemotePolicy.


        :return: The enabled of this JbossRemotePolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this JbossRemotePolicy.


        :param enabled: The enabled of this JbossRemotePolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def comment(self):
        """
        Gets the comment of this JbossRemotePolicy.


        :return: The comment of this JbossRemotePolicy.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this JbossRemotePolicy.


        :param comment: The comment of this JbossRemotePolicy.
        :type: str
        """

        self._comment = comment

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