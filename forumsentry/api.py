'''
Created on 20 Nov 2017

@author: walandre
'''
import forumsentry_api.models
from forumsentry.config import Config
from forumsentry.serialization import Serialization
from forumsentry.errors import BadVerbError, DeSerializationError, NotSupportedError, InvalidTypeError, ConfigError

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
from requests.exceptions import HTTPError
 
class Api(object):
    '''
                            
    '''

    # This map defines the policy types we currently support and the model they expect/return
    policy_types = {
        'httpListenerPolicies': 'HttpListenerPolicy',
        'httpRemotePolicies': 'HttpRemotePolicy'
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
                raise ConfigError(type(config))
        
        self._logger = logging.getLogger("forumsentry")
        
        self._serializer = Serialization()
        
        self._session = requests.Session()
        
       
           
       
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config):
        self._config = config

    
    def _request(self, verb, endpoint, data=None):
        """Request a url.
        :param endpoint: The api endpoint we want to call.
        :param veb: POST, GET, PUT, or DELETE.
        :param params: Optional build parameters.
        :type params: dict
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: A JSON object with the response from the API.
        """

        
        auth = HTTPBasicAuth(self.config.username, self.config.password)
        headers = {
            'Accept': 'application/json',
        }

        resp = None
        
        request_url = "{0}/{1}".format(self.config.forumsentry_url, endpoint)

        if verb == 'GET':
            resp = requests.get(request_url, auth=auth, headers=headers,verify=False)
        elif verb == 'POST':
            resp = requests.post(request_url, auth=auth, headers=headers, data=data,verify=False)
        elif verb == 'PUT':
            resp = requests.put(request_url, auth=auth, headers=headers, data=data,verify=False)
        elif verb == 'DELETE':
            resp = requests.delete(request_url, auth=auth, headers=headers,verify=False)
        else:
            raise BadVerbError(verb)

        resp.raise_for_status()
        
        self._logger.debug(resp.json())
        
        return resp.json()
      

    def getForumSentryPolicy(self, policy_type, name):
        
        if policy_type not in self.policy_types:
            raise Exception("policy_type: {0} not supported".format(policy_type))
        
        #self._update_session()
        
        target_endpoint = "policies/{0}/{1}".format(policy_type, name)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))

        try:
            # this method will be patched for unit test
            json = self._request("GET", target_endpoint)
            #print json
            self._logger.debug("json returned from {0} >>>>".format(target_endpoint))
            self._logger.debug(json)
            
            obj = self._serializer.deserialize(json, self.policy_types[policy_type])
            #print obj
            self._logger.debug("object after deserialize >>>>")
            
            if not isinstance(obj, self.str2Class(self.policy_types[policy_type])):
                raise DeSerializationError(json)
            return obj
           
        except HTTPError as e:
            self._logger.debug(e)
            if e.response.status_code == 404:
                self._logger.warn("{0} not found".format(name))
                return None
            else:
                self._logger.error("An unexpected HTTP response occurred: ", e)
                raise e
        
    def createForumSentryPolicy(self, policy_type, name, obj):
        
        if policy_type not in self.policy_types:
            raise NotSupportedError("policy_type: {0} not supported".format(policy_type))
        
        if not isinstance(obj, self.str2Class(self.policy_types[policy_type])):
            raise InvalidTypeError(type(obj))
        
        
        #self._update_session()
        
        target_endpoint = "policies/{0}/{1}".format(policy_type, name)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))
        
        
        serialized_json = self._serializer.serialize(obj)
        
        self._logger.debug("serialized_json: {0}".format(serialized_json))
        
        try:
            # this method will be patched for unit test
            json = self._request("PUT", target_endpoint, serialized_json)
            
            self._logger.debug(json)
            
            obj = self._serializer.deserialize(json, self.policy_types[policy_type])
            if not isinstance(obj, self.str2Class(self.policy_types[policy_type])):
                raise DeSerializationError(json)
            return obj
           
        except HTTPError as e:
            self._logger.debug(e)
            self._logger.error("An unexpected HTTP response occurred: ", e)
            raise e
             


    def str2Class(self, str):
        return getattr(forumsentry_api.models, str)
