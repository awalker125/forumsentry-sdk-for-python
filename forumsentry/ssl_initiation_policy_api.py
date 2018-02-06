'''
Created on 11 Jan 2018

@author: walandre
'''
from forumsentry.api import Api
from requests.exceptions import HTTPError
#from forumsentry_api.models import SslInitiationPolicy
from forumsentry.errors import InvalidTypeError, ForumHTTPError

class SslInitiationPolicyApi(Api):
    '''
    Api for working with SslInitiationPolicies
    '''
    
    path = "policies/sslInitiationPolicies"
    policy_type = "SslInitiationPolicy"

    def __init__(self, config=None):
        '''
        Constructor
        '''
        super(SslInitiationPolicyApi, self).__init__(config=config)
    
    def get(self, name):
        ''' gets a SslInitiationPolicy
        :param name: The name of the SslInitiationPolicy we want to get.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: A SslInitiationPolicy object.
        '''
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
                wrapped_error = ForumHTTPError(e)
                self._logger.error(wrapped_error)
                raise wrapped_error

    def delete(self,name):
        ''' delete a SslInitiationPolicy
        :param name: The name of the SslInitiationPolicy we want to delete.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: True/False.
        '''
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
                wrapped_error = ForumHTTPError(e)
                self._logger.error(wrapped_error)
                raise wrapped_error

    def set(self,name, obj):
        '''
        Creates/Updates a SslInitiationPolicy the forum sentry.
        :param name: The name of the SslInitiationPolicy we want to create/update..
        :param obj: The SslInitiationPolicy  to created/updated.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: The SslInitiationPolicy object that was created/updated.
        '''
        if not isinstance(obj, self.str2Class(self.policy_type)):
            raise InvalidTypeError(obj)
        
        #This doesnt follow the normal pattern. It doesnt take /name
        target_endpoint = "{0}".format(self.path)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))
        
        
        serialized_json = self._serializer.serialize(obj)
        
        self._logger.debug("serialized_json: {0}".format(serialized_json))
        
        try:
            # this method will be patched for unit test
            j = self._request("POST", target_endpoint, serialized_json)
            
            self._logger.debug(j)
            
            obj = self._serializer.deserialize(j, self.policy_type)

            return obj
           
        except HTTPError as e:
            wrapped_error = ForumHTTPError(e)
            self._logger.error(wrapped_error)
            raise wrapped_error
