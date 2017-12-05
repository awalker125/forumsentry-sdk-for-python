# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MqRemotePolicy1(object):
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
        'req_password': 'str',
        'req_field': 'str',
        'rep_use_jms_message': 'bool',
        'host': 'str',
        'jms_priority': 'int',
        'sync_timeout_millis': 'int',
        'req_qm': 'str',
        'rep_queue_temp': 'bool',
        'req_user_name': 'str',
        'req_use_jms_message': 'bool',
        'propagate_reply_to': 'bool',
        'req_topic': 'bool',
        'name': 'str',
        'req_destination': 'str',
        'rep_allowed_message_types': 'int',
        'description': 'str',
        'req_use_as_queue': 'bool',
        'req_channel': 'str',
        'propagate_ttl': 'bool',
        'req_message_type': 'int',
        'enabled': 'bool',
        'synchronous': 'bool',
        'time_to_live_seconds': 'int',
        'use_ssl': 'bool',
        'req_delivery_mode': 'int',
        'process_response': 'bool',
        'initial_pool_connections': 'int',
        'req_ssl_cipher_spec': 'str',
        'ssl_policy': 'str',
        'rep_topic': 'bool',
        'port': 'int',
        'rep_destination': 'str'
    }

    attribute_map = {
        'req_password': 'reqPassword',
        'req_field': 'reqField',
        'rep_use_jms_message': 'repUseJmsMessage',
        'host': 'host',
        'jms_priority': 'jmsPriority',
        'sync_timeout_millis': 'syncTimeoutMillis',
        'req_qm': 'reqQM',
        'rep_queue_temp': 'repQueueTemp',
        'req_user_name': 'reqUserName',
        'req_use_jms_message': 'reqUseJmsMessage',
        'propagate_reply_to': 'propagateReplyTo',
        'req_topic': 'reqTopic',
        'name': 'name',
        'req_destination': 'reqDestination',
        'rep_allowed_message_types': 'repAllowedMessageTypes',
        'description': 'description',
        'req_use_as_queue': 'reqUseAsQueue',
        'req_channel': 'reqChannel',
        'propagate_ttl': 'propagateTtl',
        'req_message_type': 'reqMessageType',
        'enabled': 'enabled',
        'synchronous': 'synchronous',
        'time_to_live_seconds': 'timeToLiveSeconds',
        'use_ssl': 'useSSL',
        'req_delivery_mode': 'reqDeliveryMode',
        'process_response': 'processResponse',
        'initial_pool_connections': 'initialPoolConnections',
        'req_ssl_cipher_spec': 'reqSSLCipherSpec',
        'ssl_policy': 'sslPolicy',
        'rep_topic': 'repTopic',
        'port': 'port',
        'rep_destination': 'repDestination'
    }

    def __init__(self, req_password=None, req_field=None, rep_use_jms_message=None, host=None, jms_priority=None, sync_timeout_millis=None, req_qm=None, rep_queue_temp=None, req_user_name=None, req_use_jms_message=None, propagate_reply_to=None, req_topic=None, name=None, req_destination=None, rep_allowed_message_types=None, description=None, req_use_as_queue=None, req_channel=None, propagate_ttl=None, req_message_type=None, enabled=None, synchronous=None, time_to_live_seconds=None, use_ssl=None, req_delivery_mode=None, process_response=None, initial_pool_connections=None, req_ssl_cipher_spec=None, ssl_policy=None, rep_topic=None, port=None, rep_destination=None):  # noqa: E501
        """MqRemotePolicy1 - a model defined in Swagger"""  # noqa: E501

        self._req_password = None
        self._req_field = None
        self._rep_use_jms_message = None
        self._host = None
        self._jms_priority = None
        self._sync_timeout_millis = None
        self._req_qm = None
        self._rep_queue_temp = None
        self._req_user_name = None
        self._req_use_jms_message = None
        self._propagate_reply_to = None
        self._req_topic = None
        self._name = None
        self._req_destination = None
        self._rep_allowed_message_types = None
        self._description = None
        self._req_use_as_queue = None
        self._req_channel = None
        self._propagate_ttl = None
        self._req_message_type = None
        self._enabled = None
        self._synchronous = None
        self._time_to_live_seconds = None
        self._use_ssl = None
        self._req_delivery_mode = None
        self._process_response = None
        self._initial_pool_connections = None
        self._req_ssl_cipher_spec = None
        self._ssl_policy = None
        self._rep_topic = None
        self._port = None
        self._rep_destination = None
        self.discriminator = None

        if req_password is not None:
            self.req_password = req_password
        if req_field is not None:
            self.req_field = req_field
        if rep_use_jms_message is not None:
            self.rep_use_jms_message = rep_use_jms_message
        if host is not None:
            self.host = host
        if jms_priority is not None:
            self.jms_priority = jms_priority
        if sync_timeout_millis is not None:
            self.sync_timeout_millis = sync_timeout_millis
        if req_qm is not None:
            self.req_qm = req_qm
        if rep_queue_temp is not None:
            self.rep_queue_temp = rep_queue_temp
        if req_user_name is not None:
            self.req_user_name = req_user_name
        if req_use_jms_message is not None:
            self.req_use_jms_message = req_use_jms_message
        if propagate_reply_to is not None:
            self.propagate_reply_to = propagate_reply_to
        if req_topic is not None:
            self.req_topic = req_topic
        self.name = name
        if req_destination is not None:
            self.req_destination = req_destination
        if rep_allowed_message_types is not None:
            self.rep_allowed_message_types = rep_allowed_message_types
        if description is not None:
            self.description = description
        if req_use_as_queue is not None:
            self.req_use_as_queue = req_use_as_queue
        if req_channel is not None:
            self.req_channel = req_channel
        if propagate_ttl is not None:
            self.propagate_ttl = propagate_ttl
        if req_message_type is not None:
            self.req_message_type = req_message_type
        if enabled is not None:
            self.enabled = enabled
        if synchronous is not None:
            self.synchronous = synchronous
        if time_to_live_seconds is not None:
            self.time_to_live_seconds = time_to_live_seconds
        if use_ssl is not None:
            self.use_ssl = use_ssl
        if req_delivery_mode is not None:
            self.req_delivery_mode = req_delivery_mode
        if process_response is not None:
            self.process_response = process_response
        if initial_pool_connections is not None:
            self.initial_pool_connections = initial_pool_connections
        if req_ssl_cipher_spec is not None:
            self.req_ssl_cipher_spec = req_ssl_cipher_spec
        if ssl_policy is not None:
            self.ssl_policy = ssl_policy
        if rep_topic is not None:
            self.rep_topic = rep_topic
        if port is not None:
            self.port = port
        if rep_destination is not None:
            self.rep_destination = rep_destination

    @property
    def req_password(self):
        """Gets the req_password of this MqRemotePolicy1.  # noqa: E501


        :return: The req_password of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._req_password

    @req_password.setter
    def req_password(self, req_password):
        """Sets the req_password of this MqRemotePolicy1.


        :param req_password: The req_password of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._req_password = req_password

    @property
    def req_field(self):
        """Gets the req_field of this MqRemotePolicy1.  # noqa: E501


        :return: The req_field of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._req_field

    @req_field.setter
    def req_field(self, req_field):
        """Sets the req_field of this MqRemotePolicy1.


        :param req_field: The req_field of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._req_field = req_field

    @property
    def rep_use_jms_message(self):
        """Gets the rep_use_jms_message of this MqRemotePolicy1.  # noqa: E501


        :return: The rep_use_jms_message of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._rep_use_jms_message

    @rep_use_jms_message.setter
    def rep_use_jms_message(self, rep_use_jms_message):
        """Sets the rep_use_jms_message of this MqRemotePolicy1.


        :param rep_use_jms_message: The rep_use_jms_message of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._rep_use_jms_message = rep_use_jms_message

    @property
    def host(self):
        """Gets the host of this MqRemotePolicy1.  # noqa: E501


        :return: The host of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this MqRemotePolicy1.


        :param host: The host of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def jms_priority(self):
        """Gets the jms_priority of this MqRemotePolicy1.  # noqa: E501


        :return: The jms_priority of this MqRemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._jms_priority

    @jms_priority.setter
    def jms_priority(self, jms_priority):
        """Sets the jms_priority of this MqRemotePolicy1.


        :param jms_priority: The jms_priority of this MqRemotePolicy1.  # noqa: E501
        :type: int
        """

        self._jms_priority = jms_priority

    @property
    def sync_timeout_millis(self):
        """Gets the sync_timeout_millis of this MqRemotePolicy1.  # noqa: E501


        :return: The sync_timeout_millis of this MqRemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._sync_timeout_millis

    @sync_timeout_millis.setter
    def sync_timeout_millis(self, sync_timeout_millis):
        """Sets the sync_timeout_millis of this MqRemotePolicy1.


        :param sync_timeout_millis: The sync_timeout_millis of this MqRemotePolicy1.  # noqa: E501
        :type: int
        """

        self._sync_timeout_millis = sync_timeout_millis

    @property
    def req_qm(self):
        """Gets the req_qm of this MqRemotePolicy1.  # noqa: E501


        :return: The req_qm of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._req_qm

    @req_qm.setter
    def req_qm(self, req_qm):
        """Sets the req_qm of this MqRemotePolicy1.


        :param req_qm: The req_qm of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._req_qm = req_qm

    @property
    def rep_queue_temp(self):
        """Gets the rep_queue_temp of this MqRemotePolicy1.  # noqa: E501


        :return: The rep_queue_temp of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._rep_queue_temp

    @rep_queue_temp.setter
    def rep_queue_temp(self, rep_queue_temp):
        """Sets the rep_queue_temp of this MqRemotePolicy1.


        :param rep_queue_temp: The rep_queue_temp of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._rep_queue_temp = rep_queue_temp

    @property
    def req_user_name(self):
        """Gets the req_user_name of this MqRemotePolicy1.  # noqa: E501


        :return: The req_user_name of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._req_user_name

    @req_user_name.setter
    def req_user_name(self, req_user_name):
        """Sets the req_user_name of this MqRemotePolicy1.


        :param req_user_name: The req_user_name of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._req_user_name = req_user_name

    @property
    def req_use_jms_message(self):
        """Gets the req_use_jms_message of this MqRemotePolicy1.  # noqa: E501


        :return: The req_use_jms_message of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._req_use_jms_message

    @req_use_jms_message.setter
    def req_use_jms_message(self, req_use_jms_message):
        """Sets the req_use_jms_message of this MqRemotePolicy1.


        :param req_use_jms_message: The req_use_jms_message of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._req_use_jms_message = req_use_jms_message

    @property
    def propagate_reply_to(self):
        """Gets the propagate_reply_to of this MqRemotePolicy1.  # noqa: E501


        :return: The propagate_reply_to of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._propagate_reply_to

    @propagate_reply_to.setter
    def propagate_reply_to(self, propagate_reply_to):
        """Sets the propagate_reply_to of this MqRemotePolicy1.


        :param propagate_reply_to: The propagate_reply_to of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._propagate_reply_to = propagate_reply_to

    @property
    def req_topic(self):
        """Gets the req_topic of this MqRemotePolicy1.  # noqa: E501


        :return: The req_topic of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._req_topic

    @req_topic.setter
    def req_topic(self, req_topic):
        """Sets the req_topic of this MqRemotePolicy1.


        :param req_topic: The req_topic of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._req_topic = req_topic

    @property
    def name(self):
        """Gets the name of this MqRemotePolicy1.  # noqa: E501


        :return: The name of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MqRemotePolicy1.


        :param name: The name of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def req_destination(self):
        """Gets the req_destination of this MqRemotePolicy1.  # noqa: E501


        :return: The req_destination of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._req_destination

    @req_destination.setter
    def req_destination(self, req_destination):
        """Sets the req_destination of this MqRemotePolicy1.


        :param req_destination: The req_destination of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._req_destination = req_destination

    @property
    def rep_allowed_message_types(self):
        """Gets the rep_allowed_message_types of this MqRemotePolicy1.  # noqa: E501


        :return: The rep_allowed_message_types of this MqRemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._rep_allowed_message_types

    @rep_allowed_message_types.setter
    def rep_allowed_message_types(self, rep_allowed_message_types):
        """Sets the rep_allowed_message_types of this MqRemotePolicy1.


        :param rep_allowed_message_types: The rep_allowed_message_types of this MqRemotePolicy1.  # noqa: E501
        :type: int
        """

        self._rep_allowed_message_types = rep_allowed_message_types

    @property
    def description(self):
        """Gets the description of this MqRemotePolicy1.  # noqa: E501


        :return: The description of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MqRemotePolicy1.


        :param description: The description of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def req_use_as_queue(self):
        """Gets the req_use_as_queue of this MqRemotePolicy1.  # noqa: E501


        :return: The req_use_as_queue of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._req_use_as_queue

    @req_use_as_queue.setter
    def req_use_as_queue(self, req_use_as_queue):
        """Sets the req_use_as_queue of this MqRemotePolicy1.


        :param req_use_as_queue: The req_use_as_queue of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._req_use_as_queue = req_use_as_queue

    @property
    def req_channel(self):
        """Gets the req_channel of this MqRemotePolicy1.  # noqa: E501


        :return: The req_channel of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._req_channel

    @req_channel.setter
    def req_channel(self, req_channel):
        """Sets the req_channel of this MqRemotePolicy1.


        :param req_channel: The req_channel of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._req_channel = req_channel

    @property
    def propagate_ttl(self):
        """Gets the propagate_ttl of this MqRemotePolicy1.  # noqa: E501


        :return: The propagate_ttl of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._propagate_ttl

    @propagate_ttl.setter
    def propagate_ttl(self, propagate_ttl):
        """Sets the propagate_ttl of this MqRemotePolicy1.


        :param propagate_ttl: The propagate_ttl of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._propagate_ttl = propagate_ttl

    @property
    def req_message_type(self):
        """Gets the req_message_type of this MqRemotePolicy1.  # noqa: E501


        :return: The req_message_type of this MqRemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._req_message_type

    @req_message_type.setter
    def req_message_type(self, req_message_type):
        """Sets the req_message_type of this MqRemotePolicy1.


        :param req_message_type: The req_message_type of this MqRemotePolicy1.  # noqa: E501
        :type: int
        """

        self._req_message_type = req_message_type

    @property
    def enabled(self):
        """Gets the enabled of this MqRemotePolicy1.  # noqa: E501


        :return: The enabled of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this MqRemotePolicy1.


        :param enabled: The enabled of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def synchronous(self):
        """Gets the synchronous of this MqRemotePolicy1.  # noqa: E501


        :return: The synchronous of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._synchronous

    @synchronous.setter
    def synchronous(self, synchronous):
        """Sets the synchronous of this MqRemotePolicy1.


        :param synchronous: The synchronous of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._synchronous = synchronous

    @property
    def time_to_live_seconds(self):
        """Gets the time_to_live_seconds of this MqRemotePolicy1.  # noqa: E501


        :return: The time_to_live_seconds of this MqRemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._time_to_live_seconds

    @time_to_live_seconds.setter
    def time_to_live_seconds(self, time_to_live_seconds):
        """Sets the time_to_live_seconds of this MqRemotePolicy1.


        :param time_to_live_seconds: The time_to_live_seconds of this MqRemotePolicy1.  # noqa: E501
        :type: int
        """

        self._time_to_live_seconds = time_to_live_seconds

    @property
    def use_ssl(self):
        """Gets the use_ssl of this MqRemotePolicy1.  # noqa: E501


        :return: The use_ssl of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this MqRemotePolicy1.


        :param use_ssl: The use_ssl of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def req_delivery_mode(self):
        """Gets the req_delivery_mode of this MqRemotePolicy1.  # noqa: E501


        :return: The req_delivery_mode of this MqRemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._req_delivery_mode

    @req_delivery_mode.setter
    def req_delivery_mode(self, req_delivery_mode):
        """Sets the req_delivery_mode of this MqRemotePolicy1.


        :param req_delivery_mode: The req_delivery_mode of this MqRemotePolicy1.  # noqa: E501
        :type: int
        """

        self._req_delivery_mode = req_delivery_mode

    @property
    def process_response(self):
        """Gets the process_response of this MqRemotePolicy1.  # noqa: E501


        :return: The process_response of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._process_response

    @process_response.setter
    def process_response(self, process_response):
        """Sets the process_response of this MqRemotePolicy1.


        :param process_response: The process_response of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._process_response = process_response

    @property
    def initial_pool_connections(self):
        """Gets the initial_pool_connections of this MqRemotePolicy1.  # noqa: E501


        :return: The initial_pool_connections of this MqRemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._initial_pool_connections

    @initial_pool_connections.setter
    def initial_pool_connections(self, initial_pool_connections):
        """Sets the initial_pool_connections of this MqRemotePolicy1.


        :param initial_pool_connections: The initial_pool_connections of this MqRemotePolicy1.  # noqa: E501
        :type: int
        """

        self._initial_pool_connections = initial_pool_connections

    @property
    def req_ssl_cipher_spec(self):
        """Gets the req_ssl_cipher_spec of this MqRemotePolicy1.  # noqa: E501


        :return: The req_ssl_cipher_spec of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._req_ssl_cipher_spec

    @req_ssl_cipher_spec.setter
    def req_ssl_cipher_spec(self, req_ssl_cipher_spec):
        """Sets the req_ssl_cipher_spec of this MqRemotePolicy1.


        :param req_ssl_cipher_spec: The req_ssl_cipher_spec of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._req_ssl_cipher_spec = req_ssl_cipher_spec

    @property
    def ssl_policy(self):
        """Gets the ssl_policy of this MqRemotePolicy1.  # noqa: E501


        :return: The ssl_policy of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._ssl_policy

    @ssl_policy.setter
    def ssl_policy(self, ssl_policy):
        """Sets the ssl_policy of this MqRemotePolicy1.


        :param ssl_policy: The ssl_policy of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._ssl_policy = ssl_policy

    @property
    def rep_topic(self):
        """Gets the rep_topic of this MqRemotePolicy1.  # noqa: E501


        :return: The rep_topic of this MqRemotePolicy1.  # noqa: E501
        :rtype: bool
        """
        return self._rep_topic

    @rep_topic.setter
    def rep_topic(self, rep_topic):
        """Sets the rep_topic of this MqRemotePolicy1.


        :param rep_topic: The rep_topic of this MqRemotePolicy1.  # noqa: E501
        :type: bool
        """

        self._rep_topic = rep_topic

    @property
    def port(self):
        """Gets the port of this MqRemotePolicy1.  # noqa: E501


        :return: The port of this MqRemotePolicy1.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MqRemotePolicy1.


        :param port: The port of this MqRemotePolicy1.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def rep_destination(self):
        """Gets the rep_destination of this MqRemotePolicy1.  # noqa: E501


        :return: The rep_destination of this MqRemotePolicy1.  # noqa: E501
        :rtype: str
        """
        return self._rep_destination

    @rep_destination.setter
    def rep_destination(self, rep_destination):
        """Sets the rep_destination of this MqRemotePolicy1.


        :param rep_destination: The rep_destination of this MqRemotePolicy1.  # noqa: E501
        :type: str
        """

        self._rep_destination = rep_destination

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
        if not isinstance(other, MqRemotePolicy1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
