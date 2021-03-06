# coding: utf-8

"""
    forumsentry_api
    
"""


import pprint
import re  # noqa: F401

import six


class TaskListGroup(object):
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
        'description': 'str',
        'task_lists': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'task_lists': 'taskLists',
        'name': 'name'
    }

    def __init__(self, description=None, task_lists=None, name=None):  # noqa: E501
        """TaskListGroup - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._task_lists = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self._description = description
        if task_lists is not None:
            self._task_lists = task_lists
        if name is not None:
            self._name = name

    @property
    def description(self):
        """Gets the description of this TaskListGroup.  # noqa: E501


        :return: The description of this TaskListGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskListGroup.


        :param description: The description of this TaskListGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def task_lists(self):
        """Gets the task_lists of this TaskListGroup.  # noqa: E501


        :return: The task_lists of this TaskListGroup.  # noqa: E501
        :rtype: str
        """
        return self._task_lists

    @task_lists.setter
    def task_lists(self, task_lists):
        """Sets the task_lists of this TaskListGroup.


        :param task_lists: The task_lists of this TaskListGroup.  # noqa: E501
        :type: str
        """
        self._task_lists = task_lists

    @property
    def name(self):
        """Gets the name of this TaskListGroup.  # noqa: E501


        :return: The name of this TaskListGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskListGroup.


        :param name: The name of this TaskListGroup.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, TaskListGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
