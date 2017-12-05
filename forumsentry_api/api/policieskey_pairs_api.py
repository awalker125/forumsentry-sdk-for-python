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


class PolicieskeyPairsApi(object):
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

        resource_path = '/policies/keyPairs'.replace('{format}', 'json')
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

    def import_jks_store(self, key_store_password, key_store_file, **kwargs):
        """
        import Java Key Store (JKS) File
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_jks_store(key_store_password, key_store_file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key_store_password:  (required)
        :param  key_store_file:  (required)
        :param Object key_import_information: 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.import_jks_store_with_http_info(key_store_password, key_store_file, **kwargs)
        else:
            (data) = self.import_jks_store_with_http_info(key_store_password, key_store_file, **kwargs)
            return data

    def import_jks_store_with_http_info(self, key_store_password, key_store_file, **kwargs):
        """
        import Java Key Store (JKS) File
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_jks_store_with_http_info(key_store_password, key_store_file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key_store_password:  (required)
        :param  key_store_file:  (required)
        :param Object key_import_information: 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_store_password', 'key_store_file', 'key_import_information']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_jks_store" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_store_password' is set
        if ('key_store_password' not in params) or (params['key_store_password'] is None):
            raise ValueError("Missing the required parameter `key_store_password` when calling `import_jks_store`")
        # verify the required parameter 'key_store_file' is set
        if ('key_store_file' not in params) or (params['key_store_file'] is None):
            raise ValueError("Missing the required parameter `key_store_file` when calling `import_jks_store`")

        resource_path = '/policies/keyPairs/import/jksStore'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'key_store_password' in params:
            form_params.append(('keyStorePassword', params['key_store_password']))
        if 'key_import_information' in params:
            form_params.append(('keyImportInformation', params['key_import_information']))

        body_params = None
        if 'key_store_file' in params:
            body_params = params['key_store_file']

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

    def import_pkcs12(self, name, key_and_certificate_file, **kwargs):
        """
        import PKCS#12 key pairs
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_pkcs12(name, key_and_certificate_file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name:  (required)
        :param  key_and_certificate_file: private key and public certificate to be imported (required)
        :param bool create_signer_group: 
        :param str file_integrity_password: 
        :param str password: passphrase to decrypt the key pair
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.import_pkcs12_with_http_info(name, key_and_certificate_file, **kwargs)
        else:
            (data) = self.import_pkcs12_with_http_info(name, key_and_certificate_file, **kwargs)
            return data

    def import_pkcs12_with_http_info(self, name, key_and_certificate_file, **kwargs):
        """
        import PKCS#12 key pairs
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_pkcs12_with_http_info(name, key_and_certificate_file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name:  (required)
        :param  key_and_certificate_file: private key and public certificate to be imported (required)
        :param bool create_signer_group: 
        :param str file_integrity_password: 
        :param str password: passphrase to decrypt the key pair
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'key_and_certificate_file', 'create_signer_group', 'file_integrity_password', 'password']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_pkcs12" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `import_pkcs12`")
        # verify the required parameter 'key_and_certificate_file' is set
        if ('key_and_certificate_file' not in params) or (params['key_and_certificate_file'] is None):
            raise ValueError("Missing the required parameter `key_and_certificate_file` when calling `import_pkcs12`")

        resource_path = '/policies/keyPairs/import/pkcs12'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'create_signer_group' in params:
            form_params.append(('createSignerGroup', params['create_signer_group']))
        if 'file_integrity_password' in params:
            form_params.append(('fileIntegrityPassword', params['file_integrity_password']))
        if 'password' in params:
            form_params.append(('password', params['password']))

        body_params = None
        if 'key_and_certificate_file' in params:
            body_params = params['key_and_certificate_file']

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

    def import_pkcs1_or_pkcs8(self, name, certificate_file, key_file, **kwargs):
        """
        import PKCS#1 or PKCS#8 key pairs
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_pkcs1_or_pkcs8(name, certificate_file, key_file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name:  (required)
        :param  certificate_file:  (required)
        :param  key_file:  (required)
        :param bool create_signer_group: 
        :param str password: passphrase to decrypt the key pair
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.import_pkcs1_or_pkcs8_with_http_info(name, certificate_file, key_file, **kwargs)
        else:
            (data) = self.import_pkcs1_or_pkcs8_with_http_info(name, certificate_file, key_file, **kwargs)
            return data

    def import_pkcs1_or_pkcs8_with_http_info(self, name, certificate_file, key_file, **kwargs):
        """
        import PKCS#1 or PKCS#8 key pairs
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_pkcs1_or_pkcs8_with_http_info(name, certificate_file, key_file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name:  (required)
        :param  certificate_file:  (required)
        :param  key_file:  (required)
        :param bool create_signer_group: 
        :param str password: passphrase to decrypt the key pair
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'certificate_file', 'key_file', 'create_signer_group', 'password']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_pkcs1_or_pkcs8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `import_pkcs1_or_pkcs8`")
        # verify the required parameter 'certificate_file' is set
        if ('certificate_file' not in params) or (params['certificate_file'] is None):
            raise ValueError("Missing the required parameter `certificate_file` when calling `import_pkcs1_or_pkcs8`")
        # verify the required parameter 'key_file' is set
        if ('key_file' not in params) or (params['key_file'] is None):
            raise ValueError("Missing the required parameter `key_file` when calling `import_pkcs1_or_pkcs8`")

        resource_path = '/policies/keyPairs/import/pkcs1OrPkcs8'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'create_signer_group' in params:
            form_params.append(('createSignerGroup', params['create_signer_group']))
        if 'password' in params:
            form_params.append(('password', params['password']))

        body_params = None
        if 'key_file' in params:
            body_params = params['key_file']

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

    def import_x509_or7_file(self, name, certificate_file, **kwargs):
        """
        import X.509 OR PKCS#7 public certificates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_x509_or7_file(name, certificate_file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name:  (required)
        :param  certificate_file:  (required)
        :param bool create_signer_group: 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.import_x509_or7_file_with_http_info(name, certificate_file, **kwargs)
        else:
            (data) = self.import_x509_or7_file_with_http_info(name, certificate_file, **kwargs)
            return data

    def import_x509_or7_file_with_http_info(self, name, certificate_file, **kwargs):
        """
        import X.509 OR PKCS#7 public certificates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_x509_or7_file_with_http_info(name, certificate_file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name:  (required)
        :param  certificate_file:  (required)
        :param bool create_signer_group: 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'certificate_file', 'create_signer_group']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_x509_or7_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `import_x509_or7_file`")
        # verify the required parameter 'certificate_file' is set
        if ('certificate_file' not in params) or (params['certificate_file'] is None):
            raise ValueError("Missing the required parameter `certificate_file` when calling `import_x509_or7_file`")

        resource_path = '/policies/keyPairs/import/fileX509OrPkcs7'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'create_signer_group' in params:
            form_params.append(('createSignerGroup', params['create_signer_group']))

        body_params = None
        if 'certificate_file' in params:
            body_params = params['certificate_file']

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

    def import_x509_or7_ldap(self, ldap_attribute, ldap_query, ldap_server, name, port, **kwargs):
        """
        import X.509 OR PKCS#7 public certificates with LDAP
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_x509_or7_ldap(ldap_attribute, ldap_query, ldap_server, name, port, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str ldap_attribute:  (required)
        :param str ldap_query:  (required)
        :param str ldap_server:  (required)
        :param str name:  (required)
        :param str port:  (required)
        :param bool authenticate_server: 
        :param bool create_signer_group: 
        :param str password: 
        :param str user: 
        :param bool use_ssl: 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.import_x509_or7_ldap_with_http_info(ldap_attribute, ldap_query, ldap_server, name, port, **kwargs)
        else:
            (data) = self.import_x509_or7_ldap_with_http_info(ldap_attribute, ldap_query, ldap_server, name, port, **kwargs)
            return data

    def import_x509_or7_ldap_with_http_info(self, ldap_attribute, ldap_query, ldap_server, name, port, **kwargs):
        """
        import X.509 OR PKCS#7 public certificates with LDAP
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.import_x509_or7_ldap_with_http_info(ldap_attribute, ldap_query, ldap_server, name, port, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str ldap_attribute:  (required)
        :param str ldap_query:  (required)
        :param str ldap_server:  (required)
        :param str name:  (required)
        :param str port:  (required)
        :param bool authenticate_server: 
        :param bool create_signer_group: 
        :param str password: 
        :param str user: 
        :param bool use_ssl: 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ldap_attribute', 'ldap_query', 'ldap_server', 'name', 'port', 'authenticate_server', 'create_signer_group', 'password', 'user', 'use_ssl']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_x509_or7_ldap" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ldap_attribute' is set
        if ('ldap_attribute' not in params) or (params['ldap_attribute'] is None):
            raise ValueError("Missing the required parameter `ldap_attribute` when calling `import_x509_or7_ldap`")
        # verify the required parameter 'ldap_query' is set
        if ('ldap_query' not in params) or (params['ldap_query'] is None):
            raise ValueError("Missing the required parameter `ldap_query` when calling `import_x509_or7_ldap`")
        # verify the required parameter 'ldap_server' is set
        if ('ldap_server' not in params) or (params['ldap_server'] is None):
            raise ValueError("Missing the required parameter `ldap_server` when calling `import_x509_or7_ldap`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `import_x509_or7_ldap`")
        # verify the required parameter 'port' is set
        if ('port' not in params) or (params['port'] is None):
            raise ValueError("Missing the required parameter `port` when calling `import_x509_or7_ldap`")

        resource_path = '/policies/keyPairs/import/ldapX509OrPkcs7'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'ldap_attribute' in params:
            form_params.append(('ldapAttribute', params['ldap_attribute']))
        if 'ldap_query' in params:
            form_params.append(('ldapQuery', params['ldap_query']))
        if 'ldap_server' in params:
            form_params.append(('ldapServer', params['ldap_server']))
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'port' in params:
            form_params.append(('port', params['port']))
        if 'authenticate_server' in params:
            form_params.append(('authenticateServer', params['authenticate_server']))
        if 'create_signer_group' in params:
            form_params.append(('createSignerGroup', params['create_signer_group']))
        if 'password' in params:
            form_params.append(('password', params['password']))
        if 'user' in params:
            form_params.append(('user', params['user']))
        if 'use_ssl' in params:
            form_params.append(('useSSL', params['use_ssl']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain'])
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
                                            response_type='str',
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

        resource_path = '/policies/keyPairs/{id}'.replace('{format}', 'json')
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
