'''
Created on 20 Nov 2017

@author: walandre
'''
import forumsentry_api.models
from forumsentry.config import Config
from forumsentry.serialization import Serialization
from forumsentry.errors import BadVerbError, DeSerializationError, NotSupportedError, InvalidTypeError, ConfigError

from forumsentry_api.models import http_listener_policy
from forumsentry_api.models import http_remote_policy
from forumsentry_api.models import html_policies
from forumsentry_api.models import html_policy
import requests
from requests.auth import HTTPBasicAuth
import logging
# import datetime
import json
import os.path
# import re
# import six
# import os
# import tempfile
# import sys
from requests.exceptions import HTTPError
 
class Api(object):
    '''
                            
    '''
    # This map defines the policy types we currently support and the model they expect/return
    policy_types = {
        'httpListenerPolicies': 'HttpListenerPolicy',
        'httpRemotePolicies': 'HttpRemotePolicy',
        'htmlPolicies': 'HtmlPolicies'
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
                raise ConfigError(config)
        
        self._logger = logging.getLogger("forumsentry")
        
        self._serializer = Serialization()
        
        self._session = requests.Session()
            
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config):
        self._config = config
 
    def str2Class(self, string):
        return getattr(forumsentry_api.models, string)
 
    def class2String(self, klass):
        return klass.__name__
 
    def _request(self, verb, endpoint, body=None):
        """Request a url.
        :param endpoint: The api endpoint we want to call.
        :param verb: GET, PUT, or DELETE.
        :param body: json to be sent in body of request
        :type params: dict
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: A JSON object with the response from the API.
        """
        data = None
        if body is not None:
            data = json.loads(body)
        
        auth = HTTPBasicAuth(self.config.username, self.config.password)
        headers = {
            'Accept': 'application/json',
        }

        resp = None
        
        request_url = "{0}/{1}".format(self.config.forumsentry_url, endpoint)

        if verb == 'GET':
            resp = requests.get(request_url, auth=auth, headers=headers,verify=False)
        elif verb == 'PUT':
            resp = requests.put(request_url, auth=auth, headers=headers, data=data,verify=False)
        elif verb == 'DELETE':
            resp = requests.delete(request_url, auth=auth, headers=headers,verify=False)
        else:
            raise BadVerbError(verb)

        resp.raise_for_status()
        
        self._logger.debug(resp.text)
        return resp.text

        
    def _request_file(self,endpoint,filename, form_data=None):    
        """Request a url.
        :param endpoint: The api endpoint we want to call.
        :param filename: Path to the file to upload
        :param form_data: form data to submit. E.g password=password_123
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :raises IOError: When file not found or unreadable
        :returns: A JSON object with the response from the API.
        """
        
        resp = None
        
        if not os.path.isfile(filename):
            raise IOError("{0} not found".format(filename))   
 
        files = {'file': (open(filename, 'rb'))}
        
        auth = HTTPBasicAuth(self.config.username, self.config.password)
        
        request_url = "{0}/{1}".format(self.config.forumsentry_url, endpoint)
        
        if form_data is not None:
            if type(form_data) == type(dict()):
                resp = requests.post(request_url, auth=auth, verify=False, files=files, data=form_data)
            else:
                self._logger.error("Expected a dictionary of form params to post")
                raise InvalidTypeError(form_data)
        else:
            resp = requests.post(request_url, auth=auth, verify=False, files=files)
        
        
        resp.raise_for_status()
        
        self._logger.debug(resp.text)
        return resp.text
            

