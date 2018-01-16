'''
Created on 8 Dec 2017

@author: walandre
'''

import forumsentry_api.models
import datetime
import json
import re
import six
import sys
#import os
#import tempfile
import logging
from forumsentry.errors import DeSerializationError
from __builtin__ import str

class Serialization(object):
    '''
    This class is responsible for serializing our models to and from json.
    
    It uses the swagger_types (dict) and attribute_map (dict) in each model to do this.

    These are created automatically by the swagger code gen tool.
    
    '''


    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  # noqa: F821
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }


    def __init__(self):
        '''
        Constructor
        '''
        self._logger = logging.getLogger("forumsentry")
 
    def serialize(self,obj):  
        sanitized = self._serialize(obj)
        j = json.dumps(sanitized)
#         print sys._getframe().f_code.co_name
#         print j
#         print type(j)
        return j
 
    def _serialize(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self._serialize(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self._serialize(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `swagger_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in six.iteritems(obj.swagger_types)
                        if getattr(obj, attr) is not None}

        return {key: self._serialize(val)
                for key, val in six.iteritems(obj_dict)}

    def deserialize(self, j, response_type):
        """Deserializes data into an object.

        :param j: json to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        #if response_type == "file":
        #    return self.__deserialize_file(data)

        # fetch data from response object
        #try:
        #    self._logger.debug(response.text)
        #    data = json.loads(response.text)
        #except ValueError:
        #    data = response.content
#         print sys._getframe().f_code.co_name
#         print j
        try:
            data = json.loads(j)
            return self.__deserialize(data, response_type)
        except TypeError as e:
            raise DeSerializationError(e)
        except Exception as ex:
            raise DeSerializationError(ex)
        
    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match('list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match('dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(forumsentry_api.models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)


#     def __deserialize_file(self, response):
#         """Deserializes body to file
# 
#         Saves response body into a file in a temporary folder,
#         using the filename from the `Content-Disposition` header if provided.
# 
#         :param response:  RESTResponse.
#         :return: file path.
#         """
#         fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
#         os.close(fd)
#         os.remove(path)
# 
#         content_disposition = response.getheader("Content-Disposition")
#         if content_disposition:
#             filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
#                                  content_disposition).group(1)
#             path = os.path.join(os.path.dirname(path), filename)
# 
#         with open(path, "wb") as f:
#             f.write(response.data)
# 
#         return path

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            #print klass
            return klass(data)
        except UnicodeEncodeError:
            return six.u(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise DeSerializationError(
               "Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datatime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise DeSerializationError("Failed to parse `{0}` as datetime object".format(string))

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        if not klass.swagger_types and not hasattr(klass,
                                                   'get_real_child_model'):
            return data

        kwargs = {}
        if klass.swagger_types is not None:
            for attr, attr_type in six.iteritems(klass.swagger_types):
                if (data is not None and
                        klass.attribute_map[attr] in data and
                        isinstance(data, (list, dict))):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)

        instance = klass(**kwargs)

        if hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance
       