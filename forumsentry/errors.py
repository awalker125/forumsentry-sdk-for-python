# -*- coding: utf-8 -*-
"""
Forumsentry Error Module

"""

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