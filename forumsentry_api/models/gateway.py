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


class Gateway(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, max_threads=None, requests=None, average_load=None, average_memory=None, error_percentage=None, average_threads=None, average_established_connections=None, average_close_wait_connections=None, average_time_wait_connections=None, current_load=None, max_load=None, current_threads=None, current_memory=None, max_memory=None, current_established_connections=None, max_established_connections=None, current_close_wait_connections=None, max_close_wait_connections=None, current_time_wait_connections=None, max_time_wait_connections=None, name=None):
        """
        Gateway - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'max_threads': 'int',
            'requests': 'int',
            'average_load': 'str',
            'average_memory': 'str',
            'error_percentage': 'str',
            'average_threads': 'str',
            'average_established_connections': 'str',
            'average_close_wait_connections': 'str',
            'average_time_wait_connections': 'str',
            'current_load': 'str',
            'max_load': 'str',
            'current_threads': 'int',
            'current_memory': 'str',
            'max_memory': 'str',
            'current_established_connections': 'int',
            'max_established_connections': 'int',
            'current_close_wait_connections': 'int',
            'max_close_wait_connections': 'int',
            'current_time_wait_connections': 'int',
            'max_time_wait_connections': 'int',
            'name': 'str'
        }

        self.attribute_map = {
            'max_threads': 'maxThreads',
            'requests': 'requests',
            'average_load': 'averageLoad',
            'average_memory': 'averageMemory',
            'error_percentage': 'errorPercentage',
            'average_threads': 'averageThreads',
            'average_established_connections': 'averageEstablishedConnections',
            'average_close_wait_connections': 'averageCloseWaitConnections',
            'average_time_wait_connections': 'averageTimeWaitConnections',
            'current_load': 'currentLoad',
            'max_load': 'maxLoad',
            'current_threads': 'currentThreads',
            'current_memory': 'currentMemory',
            'max_memory': 'maxMemory',
            'current_established_connections': 'currentEstablishedConnections',
            'max_established_connections': 'maxEstablishedConnections',
            'current_close_wait_connections': 'currentCloseWaitConnections',
            'max_close_wait_connections': 'maxCloseWaitConnections',
            'current_time_wait_connections': 'currentTimeWaitConnections',
            'max_time_wait_connections': 'maxTimeWaitConnections',
            'name': 'name'
        }

        self._max_threads = max_threads
        self._requests = requests
        self._average_load = average_load
        self._average_memory = average_memory
        self._error_percentage = error_percentage
        self._average_threads = average_threads
        self._average_established_connections = average_established_connections
        self._average_close_wait_connections = average_close_wait_connections
        self._average_time_wait_connections = average_time_wait_connections
        self._current_load = current_load
        self._max_load = max_load
        self._current_threads = current_threads
        self._current_memory = current_memory
        self._max_memory = max_memory
        self._current_established_connections = current_established_connections
        self._max_established_connections = max_established_connections
        self._current_close_wait_connections = current_close_wait_connections
        self._max_close_wait_connections = max_close_wait_connections
        self._current_time_wait_connections = current_time_wait_connections
        self._max_time_wait_connections = max_time_wait_connections
        self._name = name

    @property
    def max_threads(self):
        """
        Gets the max_threads of this Gateway.


        :return: The max_threads of this Gateway.
        :rtype: int
        """
        return self._max_threads

    @max_threads.setter
    def max_threads(self, max_threads):
        """
        Sets the max_threads of this Gateway.


        :param max_threads: The max_threads of this Gateway.
        :type: int
        """

        self._max_threads = max_threads

    @property
    def requests(self):
        """
        Gets the requests of this Gateway.


        :return: The requests of this Gateway.
        :rtype: int
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """
        Sets the requests of this Gateway.


        :param requests: The requests of this Gateway.
        :type: int
        """

        self._requests = requests

    @property
    def average_load(self):
        """
        Gets the average_load of this Gateway.


        :return: The average_load of this Gateway.
        :rtype: str
        """
        return self._average_load

    @average_load.setter
    def average_load(self, average_load):
        """
        Sets the average_load of this Gateway.


        :param average_load: The average_load of this Gateway.
        :type: str
        """

        self._average_load = average_load

    @property
    def average_memory(self):
        """
        Gets the average_memory of this Gateway.


        :return: The average_memory of this Gateway.
        :rtype: str
        """
        return self._average_memory

    @average_memory.setter
    def average_memory(self, average_memory):
        """
        Sets the average_memory of this Gateway.


        :param average_memory: The average_memory of this Gateway.
        :type: str
        """

        self._average_memory = average_memory

    @property
    def error_percentage(self):
        """
        Gets the error_percentage of this Gateway.


        :return: The error_percentage of this Gateway.
        :rtype: str
        """
        return self._error_percentage

    @error_percentage.setter
    def error_percentage(self, error_percentage):
        """
        Sets the error_percentage of this Gateway.


        :param error_percentage: The error_percentage of this Gateway.
        :type: str
        """

        self._error_percentage = error_percentage

    @property
    def average_threads(self):
        """
        Gets the average_threads of this Gateway.


        :return: The average_threads of this Gateway.
        :rtype: str
        """
        return self._average_threads

    @average_threads.setter
    def average_threads(self, average_threads):
        """
        Sets the average_threads of this Gateway.


        :param average_threads: The average_threads of this Gateway.
        :type: str
        """

        self._average_threads = average_threads

    @property
    def average_established_connections(self):
        """
        Gets the average_established_connections of this Gateway.


        :return: The average_established_connections of this Gateway.
        :rtype: str
        """
        return self._average_established_connections

    @average_established_connections.setter
    def average_established_connections(self, average_established_connections):
        """
        Sets the average_established_connections of this Gateway.


        :param average_established_connections: The average_established_connections of this Gateway.
        :type: str
        """

        self._average_established_connections = average_established_connections

    @property
    def average_close_wait_connections(self):
        """
        Gets the average_close_wait_connections of this Gateway.


        :return: The average_close_wait_connections of this Gateway.
        :rtype: str
        """
        return self._average_close_wait_connections

    @average_close_wait_connections.setter
    def average_close_wait_connections(self, average_close_wait_connections):
        """
        Sets the average_close_wait_connections of this Gateway.


        :param average_close_wait_connections: The average_close_wait_connections of this Gateway.
        :type: str
        """

        self._average_close_wait_connections = average_close_wait_connections

    @property
    def average_time_wait_connections(self):
        """
        Gets the average_time_wait_connections of this Gateway.


        :return: The average_time_wait_connections of this Gateway.
        :rtype: str
        """
        return self._average_time_wait_connections

    @average_time_wait_connections.setter
    def average_time_wait_connections(self, average_time_wait_connections):
        """
        Sets the average_time_wait_connections of this Gateway.


        :param average_time_wait_connections: The average_time_wait_connections of this Gateway.
        :type: str
        """

        self._average_time_wait_connections = average_time_wait_connections

    @property
    def current_load(self):
        """
        Gets the current_load of this Gateway.


        :return: The current_load of this Gateway.
        :rtype: str
        """
        return self._current_load

    @current_load.setter
    def current_load(self, current_load):
        """
        Sets the current_load of this Gateway.


        :param current_load: The current_load of this Gateway.
        :type: str
        """

        self._current_load = current_load

    @property
    def max_load(self):
        """
        Gets the max_load of this Gateway.


        :return: The max_load of this Gateway.
        :rtype: str
        """
        return self._max_load

    @max_load.setter
    def max_load(self, max_load):
        """
        Sets the max_load of this Gateway.


        :param max_load: The max_load of this Gateway.
        :type: str
        """

        self._max_load = max_load

    @property
    def current_threads(self):
        """
        Gets the current_threads of this Gateway.


        :return: The current_threads of this Gateway.
        :rtype: int
        """
        return self._current_threads

    @current_threads.setter
    def current_threads(self, current_threads):
        """
        Sets the current_threads of this Gateway.


        :param current_threads: The current_threads of this Gateway.
        :type: int
        """

        self._current_threads = current_threads

    @property
    def current_memory(self):
        """
        Gets the current_memory of this Gateway.


        :return: The current_memory of this Gateway.
        :rtype: str
        """
        return self._current_memory

    @current_memory.setter
    def current_memory(self, current_memory):
        """
        Sets the current_memory of this Gateway.


        :param current_memory: The current_memory of this Gateway.
        :type: str
        """

        self._current_memory = current_memory

    @property
    def max_memory(self):
        """
        Gets the max_memory of this Gateway.


        :return: The max_memory of this Gateway.
        :rtype: str
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        """
        Sets the max_memory of this Gateway.


        :param max_memory: The max_memory of this Gateway.
        :type: str
        """

        self._max_memory = max_memory

    @property
    def current_established_connections(self):
        """
        Gets the current_established_connections of this Gateway.


        :return: The current_established_connections of this Gateway.
        :rtype: int
        """
        return self._current_established_connections

    @current_established_connections.setter
    def current_established_connections(self, current_established_connections):
        """
        Sets the current_established_connections of this Gateway.


        :param current_established_connections: The current_established_connections of this Gateway.
        :type: int
        """

        self._current_established_connections = current_established_connections

    @property
    def max_established_connections(self):
        """
        Gets the max_established_connections of this Gateway.


        :return: The max_established_connections of this Gateway.
        :rtype: int
        """
        return self._max_established_connections

    @max_established_connections.setter
    def max_established_connections(self, max_established_connections):
        """
        Sets the max_established_connections of this Gateway.


        :param max_established_connections: The max_established_connections of this Gateway.
        :type: int
        """

        self._max_established_connections = max_established_connections

    @property
    def current_close_wait_connections(self):
        """
        Gets the current_close_wait_connections of this Gateway.


        :return: The current_close_wait_connections of this Gateway.
        :rtype: int
        """
        return self._current_close_wait_connections

    @current_close_wait_connections.setter
    def current_close_wait_connections(self, current_close_wait_connections):
        """
        Sets the current_close_wait_connections of this Gateway.


        :param current_close_wait_connections: The current_close_wait_connections of this Gateway.
        :type: int
        """

        self._current_close_wait_connections = current_close_wait_connections

    @property
    def max_close_wait_connections(self):
        """
        Gets the max_close_wait_connections of this Gateway.


        :return: The max_close_wait_connections of this Gateway.
        :rtype: int
        """
        return self._max_close_wait_connections

    @max_close_wait_connections.setter
    def max_close_wait_connections(self, max_close_wait_connections):
        """
        Sets the max_close_wait_connections of this Gateway.


        :param max_close_wait_connections: The max_close_wait_connections of this Gateway.
        :type: int
        """

        self._max_close_wait_connections = max_close_wait_connections

    @property
    def current_time_wait_connections(self):
        """
        Gets the current_time_wait_connections of this Gateway.


        :return: The current_time_wait_connections of this Gateway.
        :rtype: int
        """
        return self._current_time_wait_connections

    @current_time_wait_connections.setter
    def current_time_wait_connections(self, current_time_wait_connections):
        """
        Sets the current_time_wait_connections of this Gateway.


        :param current_time_wait_connections: The current_time_wait_connections of this Gateway.
        :type: int
        """

        self._current_time_wait_connections = current_time_wait_connections

    @property
    def max_time_wait_connections(self):
        """
        Gets the max_time_wait_connections of this Gateway.


        :return: The max_time_wait_connections of this Gateway.
        :rtype: int
        """
        return self._max_time_wait_connections

    @max_time_wait_connections.setter
    def max_time_wait_connections(self, max_time_wait_connections):
        """
        Sets the max_time_wait_connections of this Gateway.


        :param max_time_wait_connections: The max_time_wait_connections of this Gateway.
        :type: int
        """

        self._max_time_wait_connections = max_time_wait_connections

    @property
    def name(self):
        """
        Gets the name of this Gateway.


        :return: The name of this Gateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Gateway.


        :param name: The name of this Gateway.
        :type: str
        """

        self._name = name

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