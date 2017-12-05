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


class ConfigurationimportApi(object):
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

    def import_configuration(self, format, password, file, **kwargs):
        """
        imports a configuration file
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_configuration(format, password, file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str format: format of the configuration file (required)
        :param str password: passphrase with which to decrypt the fsx file (required)
        :param file file: fsx file to be imported (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.import_configuration_with_http_info(format, password, file, **kwargs)
        else:
            (data) = self.import_configuration_with_http_info(format, password, file, **kwargs)
            return data

    def import_configuration_with_http_info(self, format, password, file, **kwargs):
        """
        imports a configuration file
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_configuration_with_http_info(format, password, file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str format: format of the configuration file (required)
        :param str password: passphrase with which to decrypt the fsx file (required)
        :param file file: fsx file to be imported (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'password', 'file']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params) or (params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `import_configuration`")
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `import_configuration`")
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `import_configuration`")

        resource_path = '/configuration/import'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'format' in params:
            query_params['format'] = params['format']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'password' in params:
            form_params.append(('password', params['password']))
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
