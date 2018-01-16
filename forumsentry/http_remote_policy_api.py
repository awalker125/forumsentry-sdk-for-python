'''
Created on 11 Jan 2018

@author: walandre
'''
from forumsentry.api import Api
from requests.exceptions import HTTPError
from forumsentry_api.models.http_remote_policy import HttpRemotePolicy
from forumsentry.errors import InvalidTypeError

class HttpRemotePolicyApi(Api):
    '''
    Api for working with HttpRemotePolicies
    '''
    
    path = "policies/httpRemotePolicies"
    policy_type = "HttpRemotePolicy"

    def __init__(self, config=None):
        '''
        Constructor
        '''
        super(HttpRemotePolicyApi, self).__init__(config=config)
    
    def get(self, name):
        
        target_endpoint = "{0}/{1}".format(self.path, name)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))

        try:
            # this method will be patched for unit test
            j = self._request("GET", target_endpoint)
            #print j
            self._logger.debug("json returned from {0} >>>>".format(target_endpoint))
            self._logger.debug(j)
            
            obj = self._serializer.deserialize(j, self.policy_type)
            #print obj
            self._logger.debug("object after deserialize >>>>")
            
            return obj
           
        except HTTPError as e:
            self._logger.debug(e)
            if e.response.status_code == 404:
                self._logger.warn("{0} not found".format(name))
                return None
            else:
                self._logger.error("An unexpected HTTP response occurred: ", e)
                raise e

    def delete(self,name):

        target_endpoint = "{0}/{1}".format(self.path, name)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))

        try:
            # this method will be patched for unit test
            #We dont expect any data back in a delete. If it fails we'll either get a 404 which means it doesnt exist or some other error which will be thrown up the stack.
            self._request("DELETE", target_endpoint)
            return True
           
        except HTTPError as e:
            self._logger.debug(e)
            if e.response.status_code == 404:
                self._logger.warn("{0} not found".format(name))
                return True
            else:
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

    def export(self,name,fsg,password):
        ''' export a task list to an fsg file
        :param name: The name of the HttpRemotePolicy we want to export.
        :param fsg: The file to save the export to.
        :param password: The password to encrypt the export with.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: True/False.
        '''
        target_endpoint = "{0}/{1}/fsg".format(self.path, name)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))

        try:
            # this method will be patched for unit test
            return self._export_fsg(target_endpoint, fsg, password)
           
        except HTTPError as e:
            self._logger.debug(e)
            if e.response.status_code == 404:
                self._logger.warn("{0} not found".format(name))
                return False
            else:
                self._logger.error("An unexpected HTTP response occurred: ", e)
                raise e