# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MqRemotePolicy(object):
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
        'req_channel': 'str',
        'req_qm': 'str',
        'req_ssl_cipher_spec': 'str',
        'req_use_jms_message': 'bool',
        'rep_use_jms_message': 'bool',
        'req_use_as_queue': 'bool',
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

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'req_channel': 'reqChannel',
        'req_qm': 'reqQM',
        'req_ssl_cipher_spec': 'reqSSLCipherSpec',
        'req_use_jms_message': 'reqUseJmsMessage',
        'rep_use_jms_message': 'repUseJmsMessage',
        'req_use_as_queue': 'reqUseAsQueue',
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

    def __init__(self, name=None, description=None, req_channel=None, req_qm=None, req_ssl_cipher_spec=None, req_use_jms_message=None, rep_use_jms_message=None, req_use_as_queue=None, process_response=None, synchronous=None, req_destination=None, req_topic=None, req_delivery_mode=None, req_message_type=None, req_field=None, req_user_name=None, req_password=None, rep_topic=None, rep_destination=None, rep_field=None, rep_allowed_message_types=None, initial_pool_connections=None, jms_priority=None, ssl_policy=None, use_ssl=None, rep_queue_temp=None, sync_timeout_millis=None, time_to_live_seconds=None, propagate_reply_to=None, propagate_ttl=None, host=None, port=None, enabled=None, comment=None):  # noqa: E501
        """MqRemotePolicy - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._req_channel = None
        self._req_qm = None
        self._req_ssl_cipher_spec = None
        self._req_use_jms_message = None
        self._rep_use_jms_message = None
        self._req_use_as_queue = None
        self._process_response = None
        self._synchronous = None
        self._req_destination = None
        self._req_topic = None
        self._req_delivery_mode = None
        self._req_message_type = None
        self._req_field = None
        self._req_user_name = None
        self._req_password = None
        self._rep_topic = None
        self._rep_destination = None
        self._rep_field = None
        self._rep_allowed_message_types = None
        self._initial_pool_connections = None
        self._jms_priority = None
        self._ssl_policy = None
        self._use_ssl = None
        self._rep_queue_temp = None
        self._sync_timeout_millis = None
        self._time_to_live_seconds = None
        self._propagate_reply_to = None
        self._propagate_ttl = None
        self._host = None
        self._port = None
        self._enabled = None
        self._comment = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if req_channel is not None:
            self.req_channel = req_channel
        if req_qm is not None:
            self.req_qm = req_qm
        if req_ssl_cipher_spec is not None:
            self.req_ssl_cipher_spec = req_ssl_cipher_spec
        if req_use_jms_message is not None:
            self.req_use_jms_message = req_use_jms_message
        if rep_use_jms_message is not None:
            self.rep_use_jms_message = rep_use_jms_message
        if req_use_as_queue is not None:
            self.req_use_as_queue = req_use_as_queue
        if process_response is not None:
            self.process_response = process_response
        if synchronous is not None:
            self.synchronous = synchronous
        if req_destination is not None:
            self.req_destination = req_destination
        if req_topic is not None:
            self.req_topic = req_topic
        if req_delivery_mode is not None:
            self.req_delivery_mode = req_delivery_mode
        if req_message_type is not None:
            self.req_message_type = req_message_type
        if req_field is not None:
            self.req_field = req_field
        if req_user_name is not None:
            self.req_user_name = req_user_name
        if req_password is not None:
            self.req_password = req_password
        if rep_topic is not None:
            self.rep_topic = rep_topic
        if rep_destination is not None:
            self.rep_destination = rep_destination
        if rep_field is not None:
            self.rep_field = rep_field
        if rep_allowed_message_types is not None:
            self.rep_allowed_message_types = rep_allowed_message_types
        if initial_pool_connections is not None:
            self.initial_pool_connections = initial_pool_connections
        if jms_priority is not None:
            self.jms_priority = jms_priority
        if ssl_policy is not None:
            self.ssl_policy = ssl_policy
        if use_ssl is not None:
            self.use_ssl = use_ssl
        if rep_queue_temp is not None:
            self.rep_queue_temp = rep_queue_temp
        if sync_timeout_millis is not None:
            self.sync_timeout_millis = sync_timeout_millis
        if time_to_live_seconds is not None:
            self.time_to_live_seconds = time_to_live_seconds
        if propagate_reply_to is not None:
            self.propagate_reply_to = propagate_reply_to
        if propagate_ttl is not None:
            self.propagate_ttl = propagate_ttl
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if enabled is not None:
            self.enabled = enabled
        if comment is not None:
            self.comment = comment

    @property
    def name(self):
        """Gets the name of this MqRemotePolicy.  # noqa: E501


        :return: The name of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MqRemotePolicy.


        :param name: The name of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this MqRemotePolicy.  # noqa: E501


        :return: The description of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MqRemotePolicy.


        :param description: The description of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def req_channel(self):
        """Gets the req_channel of this MqRemotePolicy.  # noqa: E501


        :return: The req_channel of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._req_channel

    @req_channel.setter
    def req_channel(self, req_channel):
        """Sets the req_channel of this MqRemotePolicy.


        :param req_channel: The req_channel of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._req_channel = req_channel

    @property
    def req_qm(self):
        """Gets the req_qm of this MqRemotePolicy.  # noqa: E501


        :return: The req_qm of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._req_qm

    @req_qm.setter
    def req_qm(self, req_qm):
        """Sets the req_qm of this MqRemotePolicy.


        :param req_qm: The req_qm of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._req_qm = req_qm

    @property
    def req_ssl_cipher_spec(self):
        """Gets the req_ssl_cipher_spec of this MqRemotePolicy.  # noqa: E501


        :return: The req_ssl_cipher_spec of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._req_ssl_cipher_spec

    @req_ssl_cipher_spec.setter
    def req_ssl_cipher_spec(self, req_ssl_cipher_spec):
        """Sets the req_ssl_cipher_spec of this MqRemotePolicy.


        :param req_ssl_cipher_spec: The req_ssl_cipher_spec of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._req_ssl_cipher_spec = req_ssl_cipher_spec

    @property
    def req_use_jms_message(self):
        """Gets the req_use_jms_message of this MqRemotePolicy.  # noqa: E501


        :return: The req_use_jms_message of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._req_use_jms_message

    @req_use_jms_message.setter
    def req_use_jms_message(self, req_use_jms_message):
        """Sets the req_use_jms_message of this MqRemotePolicy.


        :param req_use_jms_message: The req_use_jms_message of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._req_use_jms_message = req_use_jms_message

    @property
    def rep_use_jms_message(self):
        """Gets the rep_use_jms_message of this MqRemotePolicy.  # noqa: E501


        :return: The rep_use_jms_message of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._rep_use_jms_message

    @rep_use_jms_message.setter
    def rep_use_jms_message(self, rep_use_jms_message):
        """Sets the rep_use_jms_message of this MqRemotePolicy.


        :param rep_use_jms_message: The rep_use_jms_message of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._rep_use_jms_message = rep_use_jms_message

    @property
    def req_use_as_queue(self):
        """Gets the req_use_as_queue of this MqRemotePolicy.  # noqa: E501


        :return: The req_use_as_queue of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._req_use_as_queue

    @req_use_as_queue.setter
    def req_use_as_queue(self, req_use_as_queue):
        """Sets the req_use_as_queue of this MqRemotePolicy.


        :param req_use_as_queue: The req_use_as_queue of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._req_use_as_queue = req_use_as_queue

    @property
    def process_response(self):
        """Gets the process_response of this MqRemotePolicy.  # noqa: E501


        :return: The process_response of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._process_response

    @process_response.setter
    def process_response(self, process_response):
        """Sets the process_response of this MqRemotePolicy.


        :param process_response: The process_response of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._process_response = process_response

    @property
    def synchronous(self):
        """Gets the synchronous of this MqRemotePolicy.  # noqa: E501


        :return: The synchronous of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._synchronous

    @synchronous.setter
    def synchronous(self, synchronous):
        """Sets the synchronous of this MqRemotePolicy.


        :param synchronous: The synchronous of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._synchronous = synchronous

    @property
    def req_destination(self):
        """Gets the req_destination of this MqRemotePolicy.  # noqa: E501


        :return: The req_destination of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._req_destination

    @req_destination.setter
    def req_destination(self, req_destination):
        """Sets the req_destination of this MqRemotePolicy.


        :param req_destination: The req_destination of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._req_destination = req_destination

    @property
    def req_topic(self):
        """Gets the req_topic of this MqRemotePolicy.  # noqa: E501


        :return: The req_topic of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._req_topic

    @req_topic.setter
    def req_topic(self, req_topic):
        """Sets the req_topic of this MqRemotePolicy.


        :param req_topic: The req_topic of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._req_topic = req_topic

    @property
    def req_delivery_mode(self):
        """Gets the req_delivery_mode of this MqRemotePolicy.  # noqa: E501


        :return: The req_delivery_mode of this MqRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._req_delivery_mode

    @req_delivery_mode.setter
    def req_delivery_mode(self, req_delivery_mode):
        """Sets the req_delivery_mode of this MqRemotePolicy.


        :param req_delivery_mode: The req_delivery_mode of this MqRemotePolicy.  # noqa: E501
        :type: int
        """

        self._req_delivery_mode = req_delivery_mode

    @property
    def req_message_type(self):
        """Gets the req_message_type of this MqRemotePolicy.  # noqa: E501


        :return: The req_message_type of this MqRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._req_message_type

    @req_message_type.setter
    def req_message_type(self, req_message_type):
        """Sets the req_message_type of this MqRemotePolicy.


        :param req_message_type: The req_message_type of this MqRemotePolicy.  # noqa: E501
        :type: int
        """

        self._req_message_type = req_message_type

    @property
    def req_field(self):
        """Gets the req_field of this MqRemotePolicy.  # noqa: E501


        :return: The req_field of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._req_field

    @req_field.setter
    def req_field(self, req_field):
        """Sets the req_field of this MqRemotePolicy.


        :param req_field: The req_field of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._req_field = req_field

    @property
    def req_user_name(self):
        """Gets the req_user_name of this MqRemotePolicy.  # noqa: E501


        :return: The req_user_name of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._req_user_name

    @req_user_name.setter
    def req_user_name(self, req_user_name):
        """Sets the req_user_name of this MqRemotePolicy.


        :param req_user_name: The req_user_name of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._req_user_name = req_user_name

    @property
    def req_password(self):
        """Gets the req_password of this MqRemotePolicy.  # noqa: E501


        :return: The req_password of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._req_password

    @req_password.setter
    def req_password(self, req_password):
        """Sets the req_password of this MqRemotePolicy.


        :param req_password: The req_password of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._req_password = req_password

    @property
    def rep_topic(self):
        """Gets the rep_topic of this MqRemotePolicy.  # noqa: E501


        :return: The rep_topic of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._rep_topic

    @rep_topic.setter
    def rep_topic(self, rep_topic):
        """Sets the rep_topic of this MqRemotePolicy.


        :param rep_topic: The rep_topic of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._rep_topic = rep_topic

    @property
    def rep_destination(self):
        """Gets the rep_destination of this MqRemotePolicy.  # noqa: E501


        :return: The rep_destination of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._rep_destination

    @rep_destination.setter
    def rep_destination(self, rep_destination):
        """Sets the rep_destination of this MqRemotePolicy.


        :param rep_destination: The rep_destination of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._rep_destination = rep_destination

    @property
    def rep_field(self):
        """Gets the rep_field of this MqRemotePolicy.  # noqa: E501


        :return: The rep_field of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._rep_field

    @rep_field.setter
    def rep_field(self, rep_field):
        """Sets the rep_field of this MqRemotePolicy.


        :param rep_field: The rep_field of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._rep_field = rep_field

    @property
    def rep_allowed_message_types(self):
        """Gets the rep_allowed_message_types of this MqRemotePolicy.  # noqa: E501


        :return: The rep_allowed_message_types of this MqRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._rep_allowed_message_types

    @rep_allowed_message_types.setter
    def rep_allowed_message_types(self, rep_allowed_message_types):
        """Sets the rep_allowed_message_types of this MqRemotePolicy.


        :param rep_allowed_message_types: The rep_allowed_message_types of this MqRemotePolicy.  # noqa: E501
        :type: int
        """

        self._rep_allowed_message_types = rep_allowed_message_types

    @property
    def initial_pool_connections(self):
        """Gets the initial_pool_connections of this MqRemotePolicy.  # noqa: E501


        :return: The initial_pool_connections of this MqRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._initial_pool_connections

    @initial_pool_connections.setter
    def initial_pool_connections(self, initial_pool_connections):
        """Sets the initial_pool_connections of this MqRemotePolicy.


        :param initial_pool_connections: The initial_pool_connections of this MqRemotePolicy.  # noqa: E501
        :type: int
        """

        self._initial_pool_connections = initial_pool_connections

    @property
    def jms_priority(self):
        """Gets the jms_priority of this MqRemotePolicy.  # noqa: E501


        :return: The jms_priority of this MqRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._jms_priority

    @jms_priority.setter
    def jms_priority(self, jms_priority):
        """Sets the jms_priority of this MqRemotePolicy.


        :param jms_priority: The jms_priority of this MqRemotePolicy.  # noqa: E501
        :type: int
        """

        self._jms_priority = jms_priority

    @property
    def ssl_policy(self):
        """Gets the ssl_policy of this MqRemotePolicy.  # noqa: E501


        :return: The ssl_policy of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._ssl_policy

    @ssl_policy.setter
    def ssl_policy(self, ssl_policy):
        """Sets the ssl_policy of this MqRemotePolicy.


        :param ssl_policy: The ssl_policy of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._ssl_policy = ssl_policy

    @property
    def use_ssl(self):
        """Gets the use_ssl of this MqRemotePolicy.  # noqa: E501


        :return: The use_ssl of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this MqRemotePolicy.


        :param use_ssl: The use_ssl of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def rep_queue_temp(self):
        """Gets the rep_queue_temp of this MqRemotePolicy.  # noqa: E501


        :return: The rep_queue_temp of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._rep_queue_temp

    @rep_queue_temp.setter
    def rep_queue_temp(self, rep_queue_temp):
        """Sets the rep_queue_temp of this MqRemotePolicy.


        :param rep_queue_temp: The rep_queue_temp of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._rep_queue_temp = rep_queue_temp

    @property
    def sync_timeout_millis(self):
        """Gets the sync_timeout_millis of this MqRemotePolicy.  # noqa: E501


        :return: The sync_timeout_millis of this MqRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._sync_timeout_millis

    @sync_timeout_millis.setter
    def sync_timeout_millis(self, sync_timeout_millis):
        """Sets the sync_timeout_millis of this MqRemotePolicy.


        :param sync_timeout_millis: The sync_timeout_millis of this MqRemotePolicy.  # noqa: E501
        :type: int
        """

        self._sync_timeout_millis = sync_timeout_millis

    @property
    def time_to_live_seconds(self):
        """Gets the time_to_live_seconds of this MqRemotePolicy.  # noqa: E501


        :return: The time_to_live_seconds of this MqRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._time_to_live_seconds

    @time_to_live_seconds.setter
    def time_to_live_seconds(self, time_to_live_seconds):
        """Sets the time_to_live_seconds of this MqRemotePolicy.


        :param time_to_live_seconds: The time_to_live_seconds of this MqRemotePolicy.  # noqa: E501
        :type: int
        """

        self._time_to_live_seconds = time_to_live_seconds

    @property
    def propagate_reply_to(self):
        """Gets the propagate_reply_to of this MqRemotePolicy.  # noqa: E501


        :return: The propagate_reply_to of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._propagate_reply_to

    @propagate_reply_to.setter
    def propagate_reply_to(self, propagate_reply_to):
        """Sets the propagate_reply_to of this MqRemotePolicy.


        :param propagate_reply_to: The propagate_reply_to of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._propagate_reply_to = propagate_reply_to

    @property
    def propagate_ttl(self):
        """Gets the propagate_ttl of this MqRemotePolicy.  # noqa: E501


        :return: The propagate_ttl of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._propagate_ttl

    @propagate_ttl.setter
    def propagate_ttl(self, propagate_ttl):
        """Sets the propagate_ttl of this MqRemotePolicy.


        :param propagate_ttl: The propagate_ttl of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._propagate_ttl = propagate_ttl

    @property
    def host(self):
        """Gets the host of this MqRemotePolicy.  # noqa: E501


        :return: The host of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this MqRemotePolicy.


        :param host: The host of this MqRemotePolicy.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this MqRemotePolicy.  # noqa: E501


        :return: The port of this MqRemotePolicy.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MqRemotePolicy.


        :param port: The port of this MqRemotePolicy.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def enabled(self):
        """Gets the enabled of this MqRemotePolicy.  # noqa: E501


        :return: The enabled of this MqRemotePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this MqRemotePolicy.


        :param enabled: The enabled of this MqRemotePolicy.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def comment(self):
        """Gets the comment of this MqRemotePolicy.  # noqa: E501


        :return: The comment of this MqRemotePolicy.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this MqRemotePolicy.


        :param comment: The comment of this MqRemotePolicy.  # noqa: E501
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
        if not isinstance(other, MqRemotePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
