'''
Created on 20 Nov 2017

@author: walandre
'''
import forumsentry_api.models
from forumsentry.config import Config
from forumsentry.serialization import Serialization
from forumsentry.errors import BadVerbError, DeSerializationError, NotSupportedError, InvalidTypeError, ConfigError,\
    ForumHTTPError

from forumsentry_api.models import http_listener_policy
from forumsentry_api.models import http_remote_policy
from forumsentry_api.models import html_policies
from forumsentry_api.models import html_policy
import requests
from requests.auth import HTTPBasicAuth
import logging
import json
import os.path


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
            resp = requests.get(request_url, auth=auth, headers=headers,verify=self.config.verify_ssl)
        elif verb == 'PUT':
            resp = requests.put(request_url, auth=auth, headers=headers, data=data,verify=self.config.verify_ssl)
        elif verb == 'DELETE':
            resp = requests.delete(request_url, auth=auth, headers=headers,verify=self.config.verify_ssl)
        else:
            raise BadVerbError(verb)


        resp.raise_for_status()
        
        self._logger.debug(resp.text)
        return resp.text
    
    def _request_file(self,endpoint, filename,form_data=None, download=True):    
        """
        :param endpoint: The api endpoint we want to call.
        :param filename: Path to the file to upload/download
        :param form_data: form data to submit. E.g password=password_123
        :param download: If we should download default. Set to true to upload. In forum both export and import are http POST
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :raises IOError: When file not found or unreadable
        :returns: True/False
        """
        
        resp = None
        
        auth = HTTPBasicAuth(self.config.username, self.config.password)
        request_url = "{0}/{1}".format(self.config.forumsentry_url, endpoint)
        
        if download:
            #We are getting a file from a remote url
            
            if form_data is not None:
                if type(form_data) == type(dict()):
                    resp = requests.post(request_url, auth=auth, verify=self.config.verify_ssl, data=form_data)
                else:
                    self._logger.error("Expected a dictionary of form params to post")
                    raise InvalidTypeError(form_data)
            else:
                resp = requests.post(request_url, auth=auth, verify=self.config.verify_ssl)
            
            resp.raise_for_status()
            
            with open(filename, 'wb') as f:
                f.write(resp.content)
            
            return True
        
        else:
            
            if not os.path.isfile(filename):
                raise IOError("{0} not found".format(filename)) 
            
            files = {'file': (open(filename, 'rb'))}
            
            if form_data is not None:
                if type(form_data) == type(dict()):
                    resp = requests.post(request_url, auth=auth, verify=self.config.verify_ssl, files=files, data=form_data)
                else:
                    self._logger.error("Expected a dictionary of form params to post")
                    raise InvalidTypeError(form_data)
            else:
                resp = requests.post(request_url, auth=auth, verify=self.config.verify_ssl, files=files)
            
            resp.raise_for_status()
            
            self._logger.debug(resp.text)
            
            return True    
    
    def _export_fsg(self,endpoint,fsg,password, agent=None):
        
        form_data = {}
        form_data['password'] = password
        
        if agent is not None:
            endpoint = "{0}?agent={1}".format(endpoint,agent)
               
        
        return self._request_file(endpoint, fsg, form_data,download=True)
    
      
                
    def _import_fsg(self,fsg,password):
        
        target_endpoint = "configuration/import?format=fsg"
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))
        
        form_data = {}
        form_data['password'] = password
        
        try:
            # this method will be patched for unit test
            return self._request_file(target_endpoint, fsg, form_data,download=False)
            
           
        except HTTPError as e:
            wrapped_error = ForumHTTPError(e)
            self._logger.error(wrapped_error)
            raise wrapped_error

        
