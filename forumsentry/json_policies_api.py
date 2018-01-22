'''
Created on 11 Jan 2018

@author: walandre
'''
from forumsentry.api import Api
from requests.exceptions import HTTPError
from forumsentry_api.models import JsonPolicies
from forumsentry.errors import InvalidTypeError, ForumHTTPError

class JsonPoliciesApi(Api):
    '''
    Api for working with JsonPolicies
    '''
    
    path = "policies/jsonPolicies"
    policy_type = "JsonPolicies"
    
    virtual_directory_path = "virtualDirectories"
    virtual_directory_type = "VirtualDirectory"
    

    def __init__(self, config=None):
        '''
        Constructor
        '''
        super(JsonPoliciesApi, self).__init__(config=config)
    
    def get(self, name):
        ''' gets a JsonPolicies
        :param name: The name of the JsonPolicies we want to get.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: A JsonPolicies object.
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
        ''' delete a JsonPolicies
        :param name: The name of the JsonPolicies we want to delete.
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
        Creates/Updates a JsonPolicies on the forum sentry.
        :param name: The name of the JsonPolicies we want to create/update..
        :param obj: The JsonPolicies object to created/updated.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: The JsonPolicies object that was created/updated.
        '''        
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
            wrapped_error = ForumHTTPError(e)
            self._logger.error(wrapped_error)
            raise wrapped_error

    def export(self,name,fsg,password, agent=None):
        ''' export a task list to an fsg file
        :param name: The name of the task list we want to export.
        :param fsg: The file to save the export to.
        :param password: The password to encrypt the export with.
        :param agent: The agent to use if required
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: True/False.
        '''
        target_endpoint = "{0}/{1}/fsg".format(self.path, name)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))


        try:
            # this method will be patched for unit test
            #We dont expect any data back in a delete. If it fails we'll either get a 404 which means it doesnt exist or some other error which will be thrown up the stack.
            return self._export_fsg(target_endpoint, fsg, password,agent)
           
        except HTTPError as e:
            self._logger.debug(e)
            if e.response.status_code == 404:
                self._logger.warn("{0} not found".format(name))
                return False
            else:
                wrapped_error = ForumHTTPError(e)
                self._logger.error(wrapped_error)
                raise wrapped_error
    
    def deploy(self, fsg, password):
        '''
        Imports an fsg export. This will overwrite the configuration of the object contained within the export on the forum.
        '''
        return self._import_fsg(fsg, password)
    
    def get_virtual_directory(self,name,virtual_directory):
        ''' gets a virtual directory attached to a JsonPolicies
        :param name: The name of the JsonPolicies we want to get the virtual directory from.
        :param virtual_directory: The name of the VirtualDirectory we want to get.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: A VirtualDirectory object.
        '''
        target_endpoint = "{0}/{1}/{2}/{3}".format(self.path, name,self.virtual_directory_path,virtual_directory)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))

        try:
            # this method will be patched for unit test
            j = self._request("GET", target_endpoint)
            #print j
            self._logger.debug("json returned from {0} >>>>".format(target_endpoint))
            self._logger.debug(j)
            
            obj = self._serializer.deserialize(j, self.virtual_directory_type)
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
  
    def delete_virtual_directory(self,name,virtual_directory):
        ''' delete a virtual directory attached to a JsonPolicies
        :param name: The name of the JsonPolicies we want to delete the virtual directory from.
        :param virtual_directory: The name of the VirtualDirectory we want to delete.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: True/False.
        '''
        target_endpoint = "{0}/{1}/{2}/{3}".format(self.path, name,self.virtual_directory_path,virtual_directory)
      
        
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

    def set_virtual_directory(self,name,virtual_directory, obj):
        '''
        Creates/Updates a virtual directory attached to a JsonPolicies on the forum sentry.
        :param name: The name of the JsonPolicies we want to create/update..
        :param virtual_directory: The name of the VirtualDirectory we want to create/update.  
        :param obj: The VirtualDirectory object to created/updated.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: The VirtualDirectory object that was created/updated.
        '''        
        if not isinstance(obj, self.str2Class(self.virtual_directory_type)):
            raise InvalidTypeError(obj)
        
        target_endpoint = "{0}/{1}/{2}/{3}".format(self.path, name,self.virtual_directory_path,virtual_directory)
      
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))
        
        
        serialized_json = self._serializer.serialize(obj)
        
        self._logger.debug("serialized_json: {0}".format(serialized_json))
        
        try:
            # this method will be patched for unit test
            j = self._request("PUT", target_endpoint, serialized_json)
            
            self._logger.debug(j)
            
            obj = self._serializer.deserialize(j, self.virtual_directory_type)

            return obj
           
        except HTTPError as e: 
            wrapped_error = ForumHTTPError(e)
            self._logger.error(wrapped_error)
            raise wrapped_error
