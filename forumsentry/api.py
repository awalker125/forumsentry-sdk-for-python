'''
Created on 20 Nov 2017

@author: walandre
'''
import forumsentry_api.models
from forumsentry.config import Config

from forumsentry_api.models import http_listener_policy, http_remote_policy
import requests
from requests.auth import HTTPBasicAuth
import logging
import datetime
import json
import re
import six
import os
import tempfile
import sys
 
class Api(object):
    '''
                            
    '''

    # This map defines the policy types we currently support and the model they expect/return
    policy_types = {
        'httpListenerPolicies': 'HttpListenerPolicy',
        'httpRemotePolicies': 'HttpRemotePolicy'
    }


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


    def __init__(self, config=None):
        '''
        Api - Constructor
        
        
        '''
        if config is None:
            config = Config()
            self._config = config
        else:
            if isinstance(config, Config):
                self._config = config
            else:
                raise Exception("config object is not of type Config")
        
        self._logger = logging.getLogger("forumsentry")
        
        self._session = requests.Session()
        
       
           
       
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config):
        self._config = config

    def _update_session(self):
        
        auth = HTTPBasicAuth(self.config.username, self.config.password)
        self._session.auth = auth
        self._session.verify = self.config.verify_ssl
        self._session.headers.update({'Accept':'application/json'})
      

    def getForumSentryPolicy(self, policy_type, name):
        
        if policy_type not in self.policy_types:
            raise Exception("policy_type: {0} not supported".format(policy_type))
        
        self._update_session()
        
        target_url = "{0}/policies/{1}/{2}".format(self.config.forumsentry_url, policy_type, name)
        
        self._logger.debug("target_url: {0}".format(target_url))
        
        http_get = self._session.get(target_url)
        
        if http_get.status_code == 200:
            # deserialise into object
           
            object = self.deserialize(http_get, self.policy_types[policy_type])
            self._logger.debug(object)
            self._logger.debug(type(object))
            self._logger.debug(self.str2Class(self.policy_types[policy_type]))
            if not isinstance(object, self.str2Class(self.policy_types[policy_type])):
                raise Exception("failed to deserialize forum response into target object")
            return object
        elif http_get.status_code == 404:
            self._logger.warn("could not find policy: {0} of type: {1}".format(name, policy_type))
        else:
            raise Exception("unexpected http status code returned from forum")

    def createForumSentryPolicy(self, policy_type, name, object):
        
        if policy_type not in self.policy_types:
            raise Exception("policy_type: {0} not supported".format(policy_type))
        
        if not isinstance(object, self.str2Class(self.policy_types[policy_type])):
            raise Exception("object type: {0} does not match expected type {1} for policy type {2}".format(type(object),self.policy_types[policy_type], policy_type))
        
        
        self._update_session()
        
        target_url = "{0}/policies/{1}/{2}".format(self.config.forumsentry_url, policy_type, name)
        
        self._logger.debug("target_url: {0}".format(target_url))
        
        serialized_json = self.serialize(object)
        
        self._logger.debug("serialized_json: {0}".format(serialized_json))
        
        http_put = self._session.put(target_url,serialized_json)
        
        if http_put.status_code == 200:
            self._logger.info(http_put.text)
            # deserialise into object
           
            #object = self.deserialize(http_post, self.policy_types[policy_type])
            #self._logger.debug(object)
            #self._logger.debug(type(object))
            #self._logger.debug(self.str2Class(self.policy_types[policy_type]))
            #if not isinstance(object, self.str2Class(self.policy_types[policy_type])):
            #    raise Exception("failed to deserialize forum response into target object")
            #return object
        #elif http_get.status_code == 404:
        #    self._logger.warn("could not find policy: {0} of type: {1}".format(name, policy_type))
        else:
            self._logger.error(str(http_put.status_code) +" " + http_put.text)
            raise Exception("unexpected http status code returned from forum")        

    def serialize(self, obj):
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
            return [self.serialize(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.serialize(sub_obj)
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

        return {key: self.serialize(val)
                for key, val in six.iteritems(obj_dict)}


    def deserialize(self, response, response_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == "file":
            return self.__deserialize_file(response)

        # fetch data from response object
        try:
            self._logger.debug(response.text)
            data = json.loads(response.text)
        except ValueError:
            data = response.content

        return self.__deserialize(data, response_type)

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


    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                                 content_disposition).group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "wb") as f:
            f.write(response.data)

        return path

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
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
            raise Exception(
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
            raise Exception("Failed to parse `{0}` as datetime object".format(string))

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

    def str2Class(self, str):
        return getattr(forumsentry_api.models, str)
