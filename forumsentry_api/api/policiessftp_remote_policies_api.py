# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PoliciessftpRemotePoliciesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_or_update_policy(self, id, **kwargs):
        """
        creates or updates the SFTP Remote Policy
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_or_update_policy(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :param str description: 
        :param bool enabled: 
        :param str name: 
        :param int remote_port: 
        :param str remote_server: 
        :return: SftpRemotePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_or_update_policy_with_http_info(id, **kwargs)
        else:
            (data) = self.create_or_update_policy_with_http_info(id, **kwargs)
            return data

    def create_or_update_policy_with_http_info(self, id, **kwargs):
        """
        creates or updates the SFTP Remote Policy
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_or_update_policy_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :param str description: 
        :param bool enabled: 
        :param str name: 
        :param int remote_port: 
        :param str remote_server: 
        :return: SftpRemotePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'description', 'enabled', 'name', 'remote_port', 'remote_server']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_or_update_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_or_update_policy`")

        resource_path = '/policies/sftpRemotePolicies/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'description' in params:
            form_params.append(('description', params['description']))
        if 'enabled' in params:
            form_params.append(('enabled', params['enabled']))
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'remote_port' in params:
            form_params.append(('remotePort', params['remote_port']))
        if 'remote_server' in params:
            form_params.append(('remoteServer', params['remote_server']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SftpRemotePolicy',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def create_policy(self, name, remote_port, remote_server, **kwargs):
        """
        creates a new SFTP Remote Policy
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_policy(name, remote_port, remote_server, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name:  (required)
        :param int remote_port:  (required)
        :param str remote_server:  (required)
        :param str description: 
        :param bool enabled: 
        :return: SftpRemotePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_policy_with_http_info(name, remote_port, remote_server, **kwargs)
        else:
            (data) = self.create_policy_with_http_info(name, remote_port, remote_server, **kwargs)
            return data

    def create_policy_with_http_info(self, name, remote_port, remote_server, **kwargs):
        """
        creates a new SFTP Remote Policy
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_policy_with_http_info(name, remote_port, remote_server, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name:  (required)
        :param int remote_port:  (required)
        :param str remote_server:  (required)
        :param str description: 
        :param bool enabled: 
        :return: SftpRemotePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'remote_port', 'remote_server', 'description', 'enabled']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create_policy`")
        # verify the required parameter 'remote_port' is set
        if ('remote_port' not in params) or (params['remote_port'] is None):
            raise ValueError("Missing the required parameter `remote_port` when calling `create_policy`")
        # verify the required parameter 'remote_server' is set
        if ('remote_server' not in params) or (params['remote_server'] is None):
            raise ValueError("Missing the required parameter `remote_server` when calling `create_policy`")

        resource_path = '/policies/sftpRemotePolicies'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'remote_port' in params:
            form_params.append(('remotePort', params['remote_port']))
        if 'remote_server' in params:
            form_params.append(('remoteServer', params['remote_server']))
        if 'description' in params:
            form_params.append(('description', params['description']))
        if 'enabled' in params:
            form_params.append(('enabled', params['enabled']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SftpRemotePolicy',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def create_policy_copy(self, id, new_id, **kwargs):
        """
        creates a copy of the SFTP Remote Policy
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_policy_copy(id, new_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :param str new_id:  (required)
        :return: SftpRemotePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_policy_copy_with_http_info(id, new_id, **kwargs)
        else:
            (data) = self.create_policy_copy_with_http_info(id, new_id, **kwargs)
            return data

    def create_policy_copy_with_http_info(self, id, new_id, **kwargs):
        """
        creates a copy of the SFTP Remote Policy
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_policy_copy_with_http_info(id, new_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :param str new_id:  (required)
        :return: SftpRemotePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'new_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy_copy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_policy_copy`")
        # verify the required parameter 'new_id' is set
        if ('new_id' not in params) or (params['new_id'] is None):
            raise ValueError("Missing the required parameter `new_id` when calling `create_policy_copy`")

        resource_path = '/policies/sftpRemotePolicies/{id}/copy'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'new_id' in params:
            query_params['newId'] = params['new_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SftpRemotePolicy',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def export_fsg(self, id, password, **kwargs):
        """
        exports an fsg based on this policy to a file
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.export_fsg(id, password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :param str password:  (required)
        :param str agent: 
        :return: JavaIoOutputStream
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.export_fsg_with_http_info(id, password, **kwargs)
        else:
            (data) = self.export_fsg_with_http_info(id, password, **kwargs)
            return data

    def export_fsg_with_http_info(self, id, password, **kwargs):
        """
        exports an fsg based on this policy to a file
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.export_fsg_with_http_info(id, password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :param str password:  (required)
        :param str agent: 
        :return: JavaIoOutputStream
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'password', 'agent']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method export_fsg" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `export_fsg`")
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `export_fsg`")

        resource_path = '/policies/sftpRemotePolicies/{id}/fsg'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'agent' in params:
            query_params['agent'] = params['agent']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'password' in params:
            form_params.append(('password', params['password']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/octet-stream'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='JavaIoOutputStream',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_policy(self, id, **kwargs):
        """
        gets the SFTP Remote Policy
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_policy(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :return: SftpRemotePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_policy_with_http_info(id, **kwargs)
        else:
            (data) = self.get_policy_with_http_info(id, **kwargs)
            return data

    def get_policy_with_http_info(self, id, **kwargs):
        """
        gets the SFTP Remote Policy
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_policy_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :return: SftpRemotePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_policy`")

        resource_path = '/policies/sftpRemotePolicies/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SftpRemotePolicy',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_policy_list(self, **kwargs):
        """
        returns a list of policies
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_policy_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: PolicyList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_policy_list_with_http_info(**kwargs)
        else:
            (data) = self.get_policy_list_with_http_info(**kwargs)
            return data

    def get_policy_list_with_http_info(self, **kwargs):
        """
        returns a list of policies
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_policy_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: PolicyList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy_list" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/policies/sftpRemotePolicies'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PolicyList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def remove_policy(self, id, **kwargs):
        """
        deletes the policy
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_policy(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.remove_policy_with_http_info(id, **kwargs)
        else:
            (data) = self.remove_policy_with_http_info(id, **kwargs)
            return data

    def remove_policy_with_http_info(self, id, **kwargs):
        """
        deletes the policy
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_policy_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_policy`")

        resource_path = '/policies/sftpRemotePolicies/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def transfer_fsg(self, id, agent_group, **kwargs):
        """
        transfers an fsg based on this policy to the specified agent group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.transfer_fsg(id, agent_group, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :param str agent_group:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.transfer_fsg_with_http_info(id, agent_group, **kwargs)
        else:
            (data) = self.transfer_fsg_with_http_info(id, agent_group, **kwargs)
            return data

    def transfer_fsg_with_http_info(self, id, agent_group, **kwargs):
        """
        transfers an fsg based on this policy to the specified agent group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.transfer_fsg_with_http_info(id, agent_group, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :param str agent_group:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'agent_group']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfer_fsg" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `transfer_fsg`")
        # verify the required parameter 'agent_group' is set
        if ('agent_group' not in params) or (params['agent_group'] is None):
            raise ValueError("Missing the required parameter `agent_group` when calling `transfer_fsg`")

        resource_path = '/policies/sftpRemotePolicies/{id}/transfer'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'agent_group' in params:
            query_params['agentGroup'] = params['agent_group']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
