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


class PolicieskeyPairsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

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
            '/policies/keyPairs', 'GET',
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

    def import_jks_store(self, key_store_password, key_store_file, **kwargs):  # noqa: E501
        """import Java Key Store (JKS) File  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_jks_store(key_store_password, key_store_file, async=True)
        >>> result = thread.get()

        :param async bool
        :param str key_store_password: (required)
        :param  key_store_file: (required)
        :param Object key_import_information:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.import_jks_store_with_http_info(key_store_password, key_store_file, **kwargs)  # noqa: E501
        else:
            (data) = self.import_jks_store_with_http_info(key_store_password, key_store_file, **kwargs)  # noqa: E501
            return data

    def import_jks_store_with_http_info(self, key_store_password, key_store_file, **kwargs):  # noqa: E501
        """import Java Key Store (JKS) File  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_jks_store_with_http_info(key_store_password, key_store_file, async=True)
        >>> result = thread.get()

        :param async bool
        :param str key_store_password: (required)
        :param  key_store_file: (required)
        :param Object key_import_information:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_store_password', 'key_store_file', 'key_import_information']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_jks_store" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_store_password' is set
        if ('key_store_password' not in params or
                params['key_store_password'] is None):
            raise ValueError("Missing the required parameter `key_store_password` when calling `import_jks_store`")  # noqa: E501
        # verify the required parameter 'key_store_file' is set
        if ('key_store_file' not in params or
                params['key_store_file'] is None):
            raise ValueError("Missing the required parameter `key_store_file` when calling `import_jks_store`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'key_store_password' in params:
            form_params.append(('keyStorePassword', params['key_store_password']))  # noqa: E501
        if 'key_import_information' in params:
            form_params.append(('keyImportInformation', params['key_import_information']))  # noqa: E501

        body_params = None
        if 'key_store_file' in params:
            body_params = params['key_store_file']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/keyPairs/import/jksStore', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_pkcs12(self, name, key_and_certificate_file, **kwargs):  # noqa: E501
        """import PKCS#12 key pairs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_pkcs12(name, key_and_certificate_file, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param  key_and_certificate_file: private key and public certificate to be imported (required)
        :param bool create_signer_group:
        :param str file_integrity_password:
        :param str password: passphrase to decrypt the key pair
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.import_pkcs12_with_http_info(name, key_and_certificate_file, **kwargs)  # noqa: E501
        else:
            (data) = self.import_pkcs12_with_http_info(name, key_and_certificate_file, **kwargs)  # noqa: E501
            return data

    def import_pkcs12_with_http_info(self, name, key_and_certificate_file, **kwargs):  # noqa: E501
        """import PKCS#12 key pairs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_pkcs12_with_http_info(name, key_and_certificate_file, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param  key_and_certificate_file: private key and public certificate to be imported (required)
        :param bool create_signer_group:
        :param str file_integrity_password:
        :param str password: passphrase to decrypt the key pair
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'key_and_certificate_file', 'create_signer_group', 'file_integrity_password', 'password']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_pkcs12" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `import_pkcs12`")  # noqa: E501
        # verify the required parameter 'key_and_certificate_file' is set
        if ('key_and_certificate_file' not in params or
                params['key_and_certificate_file'] is None):
            raise ValueError("Missing the required parameter `key_and_certificate_file` when calling `import_pkcs12`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'create_signer_group' in params:
            form_params.append(('createSignerGroup', params['create_signer_group']))  # noqa: E501
        if 'file_integrity_password' in params:
            form_params.append(('fileIntegrityPassword', params['file_integrity_password']))  # noqa: E501
        if 'password' in params:
            form_params.append(('password', params['password']))  # noqa: E501

        body_params = None
        if 'key_and_certificate_file' in params:
            body_params = params['key_and_certificate_file']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/keyPairs/import/pkcs12', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_pkcs1_or_pkcs8(self, name, certificate_file, key_file, **kwargs):  # noqa: E501
        """import PKCS#1 or PKCS#8 key pairs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_pkcs1_or_pkcs8(name, certificate_file, key_file, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param  certificate_file: (required)
        :param  key_file: (required)
        :param bool create_signer_group:
        :param str password: passphrase to decrypt the key pair
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.import_pkcs1_or_pkcs8_with_http_info(name, certificate_file, key_file, **kwargs)  # noqa: E501
        else:
            (data) = self.import_pkcs1_or_pkcs8_with_http_info(name, certificate_file, key_file, **kwargs)  # noqa: E501
            return data

    def import_pkcs1_or_pkcs8_with_http_info(self, name, certificate_file, key_file, **kwargs):  # noqa: E501
        """import PKCS#1 or PKCS#8 key pairs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_pkcs1_or_pkcs8_with_http_info(name, certificate_file, key_file, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param  certificate_file: (required)
        :param  key_file: (required)
        :param bool create_signer_group:
        :param str password: passphrase to decrypt the key pair
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'certificate_file', 'key_file', 'create_signer_group', 'password']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_pkcs1_or_pkcs8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `import_pkcs1_or_pkcs8`")  # noqa: E501
        # verify the required parameter 'certificate_file' is set
        if ('certificate_file' not in params or
                params['certificate_file'] is None):
            raise ValueError("Missing the required parameter `certificate_file` when calling `import_pkcs1_or_pkcs8`")  # noqa: E501
        # verify the required parameter 'key_file' is set
        if ('key_file' not in params or
                params['key_file'] is None):
            raise ValueError("Missing the required parameter `key_file` when calling `import_pkcs1_or_pkcs8`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'create_signer_group' in params:
            form_params.append(('createSignerGroup', params['create_signer_group']))  # noqa: E501
        if 'password' in params:
            form_params.append(('password', params['password']))  # noqa: E501

        body_params = None
        if 'key_file' in params:
            body_params = params['key_file']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/keyPairs/import/pkcs1OrPkcs8', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_x509_or7_file(self, name, certificate_file, **kwargs):  # noqa: E501
        """import X.509 OR PKCS#7 public certificates  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_x509_or7_file(name, certificate_file, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param  certificate_file: (required)
        :param bool create_signer_group:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.import_x509_or7_file_with_http_info(name, certificate_file, **kwargs)  # noqa: E501
        else:
            (data) = self.import_x509_or7_file_with_http_info(name, certificate_file, **kwargs)  # noqa: E501
            return data

    def import_x509_or7_file_with_http_info(self, name, certificate_file, **kwargs):  # noqa: E501
        """import X.509 OR PKCS#7 public certificates  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_x509_or7_file_with_http_info(name, certificate_file, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param  certificate_file: (required)
        :param bool create_signer_group:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'certificate_file', 'create_signer_group']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_x509_or7_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `import_x509_or7_file`")  # noqa: E501
        # verify the required parameter 'certificate_file' is set
        if ('certificate_file' not in params or
                params['certificate_file'] is None):
            raise ValueError("Missing the required parameter `certificate_file` when calling `import_x509_or7_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'create_signer_group' in params:
            form_params.append(('createSignerGroup', params['create_signer_group']))  # noqa: E501

        body_params = None
        if 'certificate_file' in params:
            body_params = params['certificate_file']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/keyPairs/import/fileX509OrPkcs7', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_x509_or7_ldap(self, ldap_attribute, ldap_query, ldap_server, name, port, **kwargs):  # noqa: E501
        """import X.509 OR PKCS#7 public certificates with LDAP  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_x509_or7_ldap(ldap_attribute, ldap_query, ldap_server, name, port, async=True)
        >>> result = thread.get()

        :param async bool
        :param str ldap_attribute: (required)
        :param str ldap_query: (required)
        :param str ldap_server: (required)
        :param str name: (required)
        :param str port: (required)
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
        if kwargs.get('async'):
            return self.import_x509_or7_ldap_with_http_info(ldap_attribute, ldap_query, ldap_server, name, port, **kwargs)  # noqa: E501
        else:
            (data) = self.import_x509_or7_ldap_with_http_info(ldap_attribute, ldap_query, ldap_server, name, port, **kwargs)  # noqa: E501
            return data

    def import_x509_or7_ldap_with_http_info(self, ldap_attribute, ldap_query, ldap_server, name, port, **kwargs):  # noqa: E501
        """import X.509 OR PKCS#7 public certificates with LDAP  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.import_x509_or7_ldap_with_http_info(ldap_attribute, ldap_query, ldap_server, name, port, async=True)
        >>> result = thread.get()

        :param async bool
        :param str ldap_attribute: (required)
        :param str ldap_query: (required)
        :param str ldap_server: (required)
        :param str name: (required)
        :param str port: (required)
        :param bool authenticate_server:
        :param bool create_signer_group:
        :param str password:
        :param str user:
        :param bool use_ssl:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ldap_attribute', 'ldap_query', 'ldap_server', 'name', 'port', 'authenticate_server', 'create_signer_group', 'password', 'user', 'use_ssl']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_x509_or7_ldap" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ldap_attribute' is set
        if ('ldap_attribute' not in params or
                params['ldap_attribute'] is None):
            raise ValueError("Missing the required parameter `ldap_attribute` when calling `import_x509_or7_ldap`")  # noqa: E501
        # verify the required parameter 'ldap_query' is set
        if ('ldap_query' not in params or
                params['ldap_query'] is None):
            raise ValueError("Missing the required parameter `ldap_query` when calling `import_x509_or7_ldap`")  # noqa: E501
        # verify the required parameter 'ldap_server' is set
        if ('ldap_server' not in params or
                params['ldap_server'] is None):
            raise ValueError("Missing the required parameter `ldap_server` when calling `import_x509_or7_ldap`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `import_x509_or7_ldap`")  # noqa: E501
        # verify the required parameter 'port' is set
        if ('port' not in params or
                params['port'] is None):
            raise ValueError("Missing the required parameter `port` when calling `import_x509_or7_ldap`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'ldap_attribute' in params:
            form_params.append(('ldapAttribute', params['ldap_attribute']))  # noqa: E501
        if 'ldap_query' in params:
            form_params.append(('ldapQuery', params['ldap_query']))  # noqa: E501
        if 'ldap_server' in params:
            form_params.append(('ldapServer', params['ldap_server']))  # noqa: E501
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'port' in params:
            form_params.append(('port', params['port']))  # noqa: E501
        if 'authenticate_server' in params:
            form_params.append(('authenticateServer', params['authenticate_server']))  # noqa: E501
        if 'create_signer_group' in params:
            form_params.append(('createSignerGroup', params['create_signer_group']))  # noqa: E501
        if 'password' in params:
            form_params.append(('password', params['password']))  # noqa: E501
        if 'user' in params:
            form_params.append(('user', params['user']))  # noqa: E501
        if 'use_ssl' in params:
            form_params.append(('useSSL', params['use_ssl']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/policies/keyPairs/import/ldapX509OrPkcs7', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
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
            '/policies/keyPairs/{id}', 'DELETE',
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
