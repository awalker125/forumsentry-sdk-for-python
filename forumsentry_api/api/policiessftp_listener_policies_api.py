# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from forumsentry_api.api_client import ApiClient


class PoliciessftpListenerPoliciesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_or_update_policy(self, id, **kwargs):  # noqa: E501
        """creates or updates the SFTP Listener Policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_or_update_policy(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str description:
        :param bool enabled:
        :param str interface:
        :param str ip:
        :param str name:
        :param int port:
        :param int read_timeout_millis:
        :param bool use_device_ip:
        :return: SftpListenerPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_or_update_policy_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_or_update_policy_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def create_or_update_policy_with_http_info(self, id, **kwargs):  # noqa: E501
        """creates or updates the SFTP Listener Policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_or_update_policy_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str description:
        :param bool enabled:
        :param str interface:
        :param str ip:
        :param str name:
        :param int port:
        :param int read_timeout_millis:
        :param bool use_device_ip:
        :return: SftpListenerPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'description', 'enabled', 'interface', 'ip', 'name', 'port', 'read_timeout_millis', 'use_device_ip']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_or_update_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_or_update_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'description' in params:
            form_params.append(('description', params['description']))  # noqa: E501
        if 'enabled' in params:
            form_params.append(('enabled', params['enabled']))  # noqa: E501
        if 'interface' in params:
            form_params.append(('interface', params['interface']))  # noqa: E501
        if 'ip' in params:
            form_params.append(('ip', params['ip']))  # noqa: E501
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'port' in params:
            form_params.append(('port', params['port']))  # noqa: E501
        if 'read_timeout_millis' in params:
            form_params.append(('readTimeoutMillis', params['read_timeout_millis']))  # noqa: E501
        if 'use_device_ip' in params:
            form_params.append(('useDeviceIp', params['use_device_ip']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/sftpListenerPolicies/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SftpListenerPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_policy(self, name, **kwargs):  # noqa: E501
        """creates a new SFTP Listener Policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_policy(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param str description:
        :param bool enabled:
        :param str interface:
        :param str ip:
        :param int port:
        :param int read_timeout_millis:
        :param bool use_device_ip:
        :return: SftpListenerPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_policy_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_policy_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def create_policy_with_http_info(self, name, **kwargs):  # noqa: E501
        """creates a new SFTP Listener Policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_policy_with_http_info(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param str description:
        :param bool enabled:
        :param str interface:
        :param str ip:
        :param int port:
        :param int read_timeout_millis:
        :param bool use_device_ip:
        :return: SftpListenerPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'description', 'enabled', 'interface', 'ip', 'port', 'read_timeout_millis', 'use_device_ip']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'description' in params:
            form_params.append(('description', params['description']))  # noqa: E501
        if 'enabled' in params:
            form_params.append(('enabled', params['enabled']))  # noqa: E501
        if 'interface' in params:
            form_params.append(('interface', params['interface']))  # noqa: E501
        if 'ip' in params:
            form_params.append(('ip', params['ip']))  # noqa: E501
        if 'port' in params:
            form_params.append(('port', params['port']))  # noqa: E501
        if 'read_timeout_millis' in params:
            form_params.append(('readTimeoutMillis', params['read_timeout_millis']))  # noqa: E501
        if 'use_device_ip' in params:
            form_params.append(('useDeviceIp', params['use_device_ip']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/sftpListenerPolicies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SftpListenerPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_policy_copy(self, id, new_id, **kwargs):  # noqa: E501
        """creates a copy of the SFTP Listener Policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_policy_copy(id, new_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str new_id: (required)
        :return: SftpListenerPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_policy_copy_with_http_info(id, new_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_policy_copy_with_http_info(id, new_id, **kwargs)  # noqa: E501
            return data

    def create_policy_copy_with_http_info(self, id, new_id, **kwargs):  # noqa: E501
        """creates a copy of the SFTP Listener Policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_policy_copy_with_http_info(id, new_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str new_id: (required)
        :return: SftpListenerPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'new_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy_copy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_policy_copy`")  # noqa: E501
        # verify the required parameter 'new_id' is set
        if ('new_id' not in params or
                params['new_id'] is None):
            raise ValueError("Missing the required parameter `new_id` when calling `create_policy_copy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'new_id' in params:
            query_params.append(('newId', params['new_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/sftpListenerPolicies/{id}/copy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SftpListenerPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def export_fsg(self, id, password, **kwargs):  # noqa: E501
        """exports an fsg based on this policy to a file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.export_fsg(id, password, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str password: (required)
        :param str agent:
        :return: JavaIoOutputStream
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.export_fsg_with_http_info(id, password, **kwargs)  # noqa: E501
        else:
            (data) = self.export_fsg_with_http_info(id, password, **kwargs)  # noqa: E501
            return data

    def export_fsg_with_http_info(self, id, password, **kwargs):  # noqa: E501
        """exports an fsg based on this policy to a file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.export_fsg_with_http_info(id, password, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str password: (required)
        :param str agent:
        :return: JavaIoOutputStream
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'password', 'agent']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method export_fsg" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `export_fsg`")  # noqa: E501
        # verify the required parameter 'password' is set
        if ('password' not in params or
                params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `export_fsg`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'agent' in params:
            query_params.append(('agent', params['agent']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'password' in params:
            form_params.append(('password', params['password']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/sftpListenerPolicies/{id}/fsg', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JavaIoOutputStream',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_policy(self, id, **kwargs):  # noqa: E501
        """gets the SFTP Listener Policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_policy(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: SftpListenerPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_policy_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_policy_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_policy_with_http_info(self, id, **kwargs):  # noqa: E501
        """gets the SFTP Listener Policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_policy_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: SftpListenerPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/sftpListenerPolicies/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SftpListenerPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_policy_list(self, **kwargs):  # noqa: E501
        """returns a list of policies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_policy_list(async=True)
        >>> result = thread.get()

        :param async bool
        :return: PolicyList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_policy_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_policy_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_policy_list_with_http_info(self, **kwargs):  # noqa: E501
        """returns a list of policies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_policy_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: PolicyList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/sftpListenerPolicies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PolicyList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_policy(self, id, **kwargs):  # noqa: E501
        """deletes the policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_policy(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_policy_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_policy_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_policy_with_http_info(self, id, **kwargs):  # noqa: E501
        """deletes the policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_policy_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/sftpListenerPolicies/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transfer_fsg(self, id, agent_group, **kwargs):  # noqa: E501
        """transfers an fsg based on this policy to the specified agent group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.transfer_fsg(id, agent_group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str agent_group: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.transfer_fsg_with_http_info(id, agent_group, **kwargs)  # noqa: E501
        else:
            (data) = self.transfer_fsg_with_http_info(id, agent_group, **kwargs)  # noqa: E501
            return data

    def transfer_fsg_with_http_info(self, id, agent_group, **kwargs):  # noqa: E501
        """transfers an fsg based on this policy to the specified agent group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.transfer_fsg_with_http_info(id, agent_group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str agent_group: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'agent_group']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfer_fsg" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `transfer_fsg`")  # noqa: E501
        # verify the required parameter 'agent_group' is set
        if ('agent_group' not in params or
                params['agent_group'] is None):
            raise ValueError("Missing the required parameter `agent_group` when calling `transfer_fsg`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'agent_group' in params:
            query_params.append(('agentGroup', params['agent_group']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/sftpListenerPolicies/{id}/transfer', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
