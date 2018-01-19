# -*- coding: utf-8 -*-
"""
Forumsentry Error Module

"""
from requests.exceptions import HTTPError

class ConfigError(Exception):
    """Exception raises for bad config

    :param argument: The argument that was passed into the function.
    """
    message = "Could not load config"

    def __init__(self, argument):
        # Call the base class constructor with the parameters it needs
        super(ConfigError, self).__init__()
        self.argument = type(argument)
        self.message = ConfigError.message

    def __str__(self):
        return '{0} is invalid. {1}'.format(self.argument, self.message)

class BadVerbError(Exception):
    """Exception raises for bad HTTP verb

    :param argument: The argument that was passed into the function.
    """
    message = "verb must be one of 'GET', 'POST', 'PUT' or 'DELETE'"

    def __init__(self, argument):
        # Call the base class constructor with the parameters it needs
        super(BadVerbError, self).__init__()
        self.argument = argument
        self.message = BadVerbError.message

    def __str__(self):
        return '{0} is invalid. {1}'.format(self.argument, self.message)
        
class SerializationError(Exception):
    """Exception raises for serialization failures

    :param argument: The argument that was passed into the function.
    """
    message = "Serialization of object to json failed"

    def __init__(self, argument):
        # Call the base class constructor with the parameters it needs
        super(SerializationError, self).__init__()
        self.argument = argument
        self.message = SerializationError.message

    def __str__(self):
        return '{0} is invalid. {1}'.format(self.argument, self.message)

class DeSerializationError(Exception):
    """Exception raises for deserialization failures

    :param argument: The argument that was passed into the function.
    """
    message = "Deserialization of object from json failed"

    def __init__(self, argument):
        # Call the base class constructor with the parameters it needs
        super(DeSerializationError, self).__init__()
        self.argument = argument
        self.message = DeSerializationError.message

    def __str__(self):
        return '{0} is invalid. {1}'.format(self.argument, self.message)

class NotSupportedError(Exception):
    """Exception raises for unsupported policies/types

    :param argument: The argument that was passed into the function.
    """
    message = "not supported"

    def __init__(self, argument):
        # Call the base class constructor with the parameters it needs
        super(NotSupportedError, self).__init__()
        self.argument = argument
        self.message = NotSupportedError.message

    def __str__(self):
        return '{0} is invalid. {1}'.format(self.argument, self.message)

class InvalidTypeError(Exception):
    """Exception raised when an invalid object is used with a particular policies/types

    :param argument: The argument that was passed into the function.
    """
    message = "object type does not match expected for type"

    def __init__(self, argument):
        # Call the base class constructor with the parameters it needs
        super(InvalidTypeError, self).__init__()
        self.argument = type(argument)
        self.message = InvalidTypeError.message

    def __str__(self):
        return '{0} is invalid. {1}'.format(self.argument, self.message)


class ForumHTTPError(Exception):
    """
    Exception raised when forum sends a none 2XX HTTP Error code
    :param cause: The request HTTPError that caused this exception
    """

    def __init__(self, cause):
        # Call the base class constructor with the parameters it needs
        super(ForumHTTPError, self).__init__()
        self.cause = cause
        self.message = "{0} - {1}".format(cause.message, cause.response.text)

    def __str__(self):
        return self.message

    
# class KnownAnomalyError(Exception):
#     """
#     Exception raised when an valid object is used with a particular policies/types where an anomaly exists which causes the forum to return an error. 
#     An example is TaskListGroup which has an optional taskLists string field. If you send '' as the string the forum throws a 400 "Invalid parameter taskLists:" error.
#     Unfortunately if you create an TaskListGroup with taskLists set to None forum return taskLists = '' in the json document.
# 
#     :param argument: The argument that was passed into the function.
#     """
#     message = "provided value is known to cause an exception"
# 
#     def __init__(self, argument, field):
#         # Call the base class constructor with the parameters it needs
#         super(KnownAnomalyError, self).__init__()
#         self.argument = type(argument)
#         self.message = KnownAnomalyError.message
# 
#     def __str__(self):
#         return '{0} is invalid. {1}'.format(self.argument, self.message)              