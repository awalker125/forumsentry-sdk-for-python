'''
Created on 11 Jan 2018

@author: walandre
'''
from forumsentry.api import Api
import requests
from requests.exceptions import HTTPError
from forumsentry_api.models.http_listener_policy import HttpListenerPolicy
from forumsentry.errors import InvalidTypeError
import os.path

class ConfigurationImportApi(Api):
    '''
    classdocs
    '''
    
    path = "/configuration/import?format=fsg"

    def __init__(self, config=None):
        '''
        Constructor
        '''
        super(ConfigurationImportApi, self).__init__(config=config)
    
    def import_fsg(self,fsg,password):
        
        target_endpoint = self.path
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))
        
        form_data = {}
        form_data['password'] = password
        
        try:
            # this method will be patched for unit test
            text = self._request_file(target_endpoint, fsg, form_data)
            
            self._logger.debug(text)
            
            return text
           
        except HTTPError as e:
            self._logger.debug(e)
            self._logger.error("An unexpected HTTP response occurred: ", e)
            raise e
        
        
        
     
     
        





    def upsert(self,name, obj):
        
        if not isinstance(obj, self.str2Class(self.policy_type)):
            raise InvalidTypeError(obj)
        
        target_endpoint = "{0}/{1}".format(self.path, name)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))
        
        
        serialized_json = self._serializer.serialize(obj)
        
        self._logger.debug("serialized_json: {0}".format(serialized_json))
        
        try:
            # this method will be patched for unit test
            j = self._request("PUT", target_endpoint, serialized_json)
            
            self._logger.debug(j)
            
            obj = self._serializer.deserialize(j, self.policy_type)

            return obj
           
        except HTTPError as e:
            self._logger.debug(e)
            self._logger.error("An unexpected HTTP response occurred: ", e)
            raise e