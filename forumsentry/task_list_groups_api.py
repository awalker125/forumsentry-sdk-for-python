'''
Created on 11 Jan 2018

@author: walandre
'''
from forumsentry.api import Api
from requests.exceptions import HTTPError
from forumsentry_api.models.task_list import TaskList
from forumsentry.errors import InvalidTypeError, ForumHTTPError

class TaskListGroupsApi(Api):
    '''
    Api for working with TaskListGroups
    '''
    
    path = "policies/taskListGroups"
    policy_type = "TaskListGroup"

    def __init__(self, config=None):
        '''
        Constructor
        '''
        super(TaskListGroupsApi, self).__init__(config=config)
    
    def get(self, name):
        ''' gets a TaskListGroup
        :param name: The name of the TaskListGroup we want to get.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: A TaskListGroup object.
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
            
            #Forum throws a 400 error if you set the taskLists to '' but forum return taskLists: '' if taskList is None :-(
            if not obj.task_lists:
                obj.task_lists = None
            
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
        ''' delete a TaskListGroup
        :param name: The name of the TaskListGroup we want to delete.
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
        Creates/Updates a TaskListGroup on the forum sentry. 
        :param name: The name of the TaskListGroup we want to create/update..
        :param obj: The TaskListGroup object to created/updated.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: The TaskListGroup object that was created/updated.
        '''
        
        if not isinstance(obj, self.str2Class(self.policy_type)):
            raise InvalidTypeError(obj)
        
        if obj.task_lists is not None:
            if not obj.task_lists:
                self._logger.warn("task_lists cannot be set to an empty string. It must be a valid comma separated list of task lists that exist in the forum")
                obj.task_lists = None
        
        target_endpoint = "{0}/{1}".format(self.path, name)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))
        
        
        serialized_json = self._serializer.serialize(obj)
        
        self._logger.debug("serialized_json: {0}".format(serialized_json))
        
        try:
            # this method will be patched for unit test
            j = self._request("PUT", target_endpoint, serialized_json)
            
            self._logger.debug(j)
            
            obj = self._serializer.deserialize(j, self.policy_type)
            
            #Forum throws a 400 error if you set the taskLists to '' but forum return taskLists: '' if taskList is None :-(
            if not obj.task_lists:
                obj.task_lists = None

            return obj
           
        except HTTPError as e:
            wrapped_error = ForumHTTPError(e)
            self._logger.error(wrapped_error)
            raise wrapped_error
        
    def export(self,name,fsg,password):
        ''' export a TaskListGroup to an fsg file
        :param name: The name of the task list group we want to export.
        :param fsg: The file to save the export to.
        :param password: The password to encrypt the export with.
        :raises requests.exceptions.HTTPError: When response code is not successful.
        :returns: True/False.
        '''
        target_endpoint = "{0}/{1}/fsg".format(self.path, name)
        
        self._logger.debug("target_endpoint: {0}".format(target_endpoint))

        try:
            # this method will be patched for unit test
            #We dont expect any data back in a delete. If it fails we'll either get a 404 which means it doesnt exist or some other error which will be thrown up the stack.
            return self._export_fsg(target_endpoint, fsg, password)
           
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
        
    
