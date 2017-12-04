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

from pprint import pformat
from six import iteritems
import re


class WsdlPolicies1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, port_information=None, process_request=None, wsdl_library=None, wsdl_port_name=None, post_response_process_type=None, wsdl_binding_name=None, body_validation=None, wsdl_port_type_name=None, user_name=None, wsdl_source=None, wsdl_url=None, name=None, post_response_process=None, post_request_process_type=None, header_validation=None, description=None, request_process_type=None, post_process_response=None, wsdl_definition_name=None, wsi_validation=None, post_process_request=None, operations=None, post_request_process=None, response_process_type=None, idp_group=None, password=None, process_response=None, request_process=None, allow_additional_headers=None, wsdl_namespace=None, response_process=None, wsdl_service_name=None, envelope_validation=None):
        """
        WsdlPolicies1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'port_information': 'JSONArray',
            'process_request': 'bool',
            'wsdl_library': 'str',
            'wsdl_port_name': 'str',
            'post_response_process_type': 'str',
            'wsdl_binding_name': 'str',
            'body_validation': 'bool',
            'wsdl_port_type_name': 'str',
            'user_name': 'str',
            'wsdl_source': 'str',
            'wsdl_url': 'str',
            'name': 'str',
            'post_response_process': 'str',
            'post_request_process_type': 'str',
            'header_validation': 'bool',
            'description': 'str',
            'request_process_type': 'str',
            'post_process_response': 'bool',
            'wsdl_definition_name': 'str',
            'wsi_validation': 'bool',
            'post_process_request': 'bool',
            'operations': 'list[str]',
            'post_request_process': 'str',
            'response_process_type': 'str',
            'idp_group': 'str',
            'password': 'str',
            'process_response': 'bool',
            'request_process': 'str',
            'allow_additional_headers': 'bool',
            'wsdl_namespace': 'str',
            'response_process': 'str',
            'wsdl_service_name': 'str',
            'envelope_validation': 'bool'
        }

        self.attribute_map = {
            'port_information': 'portInformation',
            'process_request': 'processRequest',
            'wsdl_library': 'wsdlLibrary',
            'wsdl_port_name': 'wsdlPortName',
            'post_response_process_type': 'postResponseProcessType',
            'wsdl_binding_name': 'wsdlBindingName',
            'body_validation': 'bodyValidation',
            'wsdl_port_type_name': 'wsdlPortTypeName',
            'user_name': 'userName',
            'wsdl_source': 'wsdlSource',
            'wsdl_url': 'wsdlUrl',
            'name': 'name',
            'post_response_process': 'postResponseProcess',
            'post_request_process_type': 'postRequestProcessType',
            'header_validation': 'headerValidation',
            'description': 'description',
            'request_process_type': 'requestProcessType',
            'post_process_response': 'postProcessResponse',
            'wsdl_definition_name': 'wsdlDefinitionName',
            'wsi_validation': 'wsiValidation',
            'post_process_request': 'postProcessRequest',
            'operations': 'operations',
            'post_request_process': 'postRequestProcess',
            'response_process_type': 'responseProcessType',
            'idp_group': 'idpGroup',
            'password': 'password',
            'process_response': 'processResponse',
            'request_process': 'requestProcess',
            'allow_additional_headers': 'allowAdditionalHeaders',
            'wsdl_namespace': 'wsdlNamespace',
            'response_process': 'responseProcess',
            'wsdl_service_name': 'wsdlServiceName',
            'envelope_validation': 'envelopeValidation'
        }

        self._port_information = port_information
        self._process_request = process_request
        self._wsdl_library = wsdl_library
        self._wsdl_port_name = wsdl_port_name
        self._post_response_process_type = post_response_process_type
        self._wsdl_binding_name = wsdl_binding_name
        self._body_validation = body_validation
        self._wsdl_port_type_name = wsdl_port_type_name
        self._user_name = user_name
        self._wsdl_source = wsdl_source
        self._wsdl_url = wsdl_url
        self._name = name
        self._post_response_process = post_response_process
        self._post_request_process_type = post_request_process_type
        self._header_validation = header_validation
        self._description = description
        self._request_process_type = request_process_type
        self._post_process_response = post_process_response
        self._wsdl_definition_name = wsdl_definition_name
        self._wsi_validation = wsi_validation
        self._post_process_request = post_process_request
        self._operations = operations
        self._post_request_process = post_request_process
        self._response_process_type = response_process_type
        self._idp_group = idp_group
        self._password = password
        self._process_response = process_response
        self._request_process = request_process
        self._allow_additional_headers = allow_additional_headers
        self._wsdl_namespace = wsdl_namespace
        self._response_process = response_process
        self._wsdl_service_name = wsdl_service_name
        self._envelope_validation = envelope_validation

    @property
    def port_information(self):
        """
        Gets the port_information of this WsdlPolicies1.


        :return: The port_information of this WsdlPolicies1.
        :rtype: JSONArray
        """
        return self._port_information

    @port_information.setter
    def port_information(self, port_information):
        """
        Sets the port_information of this WsdlPolicies1.


        :param port_information: The port_information of this WsdlPolicies1.
        :type: JSONArray
        """

        self._port_information = port_information

    @property
    def process_request(self):
        """
        Gets the process_request of this WsdlPolicies1.


        :return: The process_request of this WsdlPolicies1.
        :rtype: bool
        """
        return self._process_request

    @process_request.setter
    def process_request(self, process_request):
        """
        Sets the process_request of this WsdlPolicies1.


        :param process_request: The process_request of this WsdlPolicies1.
        :type: bool
        """

        self._process_request = process_request

    @property
    def wsdl_library(self):
        """
        Gets the wsdl_library of this WsdlPolicies1.


        :return: The wsdl_library of this WsdlPolicies1.
        :rtype: str
        """
        return self._wsdl_library

    @wsdl_library.setter
    def wsdl_library(self, wsdl_library):
        """
        Sets the wsdl_library of this WsdlPolicies1.


        :param wsdl_library: The wsdl_library of this WsdlPolicies1.
        :type: str
        """

        self._wsdl_library = wsdl_library

    @property
    def wsdl_port_name(self):
        """
        Gets the wsdl_port_name of this WsdlPolicies1.


        :return: The wsdl_port_name of this WsdlPolicies1.
        :rtype: str
        """
        return self._wsdl_port_name

    @wsdl_port_name.setter
    def wsdl_port_name(self, wsdl_port_name):
        """
        Sets the wsdl_port_name of this WsdlPolicies1.


        :param wsdl_port_name: The wsdl_port_name of this WsdlPolicies1.
        :type: str
        """

        self._wsdl_port_name = wsdl_port_name

    @property
    def post_response_process_type(self):
        """
        Gets the post_response_process_type of this WsdlPolicies1.


        :return: The post_response_process_type of this WsdlPolicies1.
        :rtype: str
        """
        return self._post_response_process_type

    @post_response_process_type.setter
    def post_response_process_type(self, post_response_process_type):
        """
        Sets the post_response_process_type of this WsdlPolicies1.


        :param post_response_process_type: The post_response_process_type of this WsdlPolicies1.
        :type: str
        """
        allowed_values = ["TASK_LIST", "TASK_LIST_GROUP"]
        if post_response_process_type not in allowed_values:
            raise ValueError(
                "Invalid value for `post_response_process_type` ({0}), must be one of {1}"
                .format(post_response_process_type, allowed_values)
            )

        self._post_response_process_type = post_response_process_type

    @property
    def wsdl_binding_name(self):
        """
        Gets the wsdl_binding_name of this WsdlPolicies1.


        :return: The wsdl_binding_name of this WsdlPolicies1.
        :rtype: str
        """
        return self._wsdl_binding_name

    @wsdl_binding_name.setter
    def wsdl_binding_name(self, wsdl_binding_name):
        """
        Sets the wsdl_binding_name of this WsdlPolicies1.


        :param wsdl_binding_name: The wsdl_binding_name of this WsdlPolicies1.
        :type: str
        """

        self._wsdl_binding_name = wsdl_binding_name

    @property
    def body_validation(self):
        """
        Gets the body_validation of this WsdlPolicies1.


        :return: The body_validation of this WsdlPolicies1.
        :rtype: bool
        """
        return self._body_validation

    @body_validation.setter
    def body_validation(self, body_validation):
        """
        Sets the body_validation of this WsdlPolicies1.


        :param body_validation: The body_validation of this WsdlPolicies1.
        :type: bool
        """

        self._body_validation = body_validation

    @property
    def wsdl_port_type_name(self):
        """
        Gets the wsdl_port_type_name of this WsdlPolicies1.


        :return: The wsdl_port_type_name of this WsdlPolicies1.
        :rtype: str
        """
        return self._wsdl_port_type_name

    @wsdl_port_type_name.setter
    def wsdl_port_type_name(self, wsdl_port_type_name):
        """
        Sets the wsdl_port_type_name of this WsdlPolicies1.


        :param wsdl_port_type_name: The wsdl_port_type_name of this WsdlPolicies1.
        :type: str
        """

        self._wsdl_port_type_name = wsdl_port_type_name

    @property
    def user_name(self):
        """
        Gets the user_name of this WsdlPolicies1.


        :return: The user_name of this WsdlPolicies1.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this WsdlPolicies1.


        :param user_name: The user_name of this WsdlPolicies1.
        :type: str
        """

        self._user_name = user_name

    @property
    def wsdl_source(self):
        """
        Gets the wsdl_source of this WsdlPolicies1.


        :return: The wsdl_source of this WsdlPolicies1.
        :rtype: str
        """
        return self._wsdl_source

    @wsdl_source.setter
    def wsdl_source(self, wsdl_source):
        """
        Sets the wsdl_source of this WsdlPolicies1.


        :param wsdl_source: The wsdl_source of this WsdlPolicies1.
        :type: str
        """
        allowed_values = ["URL", "WSDL Library"]
        if wsdl_source not in allowed_values:
            raise ValueError(
                "Invalid value for `wsdl_source` ({0}), must be one of {1}"
                .format(wsdl_source, allowed_values)
            )

        self._wsdl_source = wsdl_source

    @property
    def wsdl_url(self):
        """
        Gets the wsdl_url of this WsdlPolicies1.


        :return: The wsdl_url of this WsdlPolicies1.
        :rtype: str
        """
        return self._wsdl_url

    @wsdl_url.setter
    def wsdl_url(self, wsdl_url):
        """
        Sets the wsdl_url of this WsdlPolicies1.


        :param wsdl_url: The wsdl_url of this WsdlPolicies1.
        :type: str
        """

        self._wsdl_url = wsdl_url

    @property
    def name(self):
        """
        Gets the name of this WsdlPolicies1.


        :return: The name of this WsdlPolicies1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WsdlPolicies1.


        :param name: The name of this WsdlPolicies1.
        :type: str
        """

        self._name = name

    @property
    def post_response_process(self):
        """
        Gets the post_response_process of this WsdlPolicies1.


        :return: The post_response_process of this WsdlPolicies1.
        :rtype: str
        """
        return self._post_response_process

    @post_response_process.setter
    def post_response_process(self, post_response_process):
        """
        Sets the post_response_process of this WsdlPolicies1.


        :param post_response_process: The post_response_process of this WsdlPolicies1.
        :type: str
        """

        self._post_response_process = post_response_process

    @property
    def post_request_process_type(self):
        """
        Gets the post_request_process_type of this WsdlPolicies1.


        :return: The post_request_process_type of this WsdlPolicies1.
        :rtype: str
        """
        return self._post_request_process_type

    @post_request_process_type.setter
    def post_request_process_type(self, post_request_process_type):
        """
        Sets the post_request_process_type of this WsdlPolicies1.


        :param post_request_process_type: The post_request_process_type of this WsdlPolicies1.
        :type: str
        """
        allowed_values = ["TASK_LIST", "TASK_LIST_GROUP"]
        if post_request_process_type not in allowed_values:
            raise ValueError(
                "Invalid value for `post_request_process_type` ({0}), must be one of {1}"
                .format(post_request_process_type, allowed_values)
            )

        self._post_request_process_type = post_request_process_type

    @property
    def header_validation(self):
        """
        Gets the header_validation of this WsdlPolicies1.


        :return: The header_validation of this WsdlPolicies1.
        :rtype: bool
        """
        return self._header_validation

    @header_validation.setter
    def header_validation(self, header_validation):
        """
        Sets the header_validation of this WsdlPolicies1.


        :param header_validation: The header_validation of this WsdlPolicies1.
        :type: bool
        """

        self._header_validation = header_validation

    @property
    def description(self):
        """
        Gets the description of this WsdlPolicies1.


        :return: The description of this WsdlPolicies1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WsdlPolicies1.


        :param description: The description of this WsdlPolicies1.
        :type: str
        """

        self._description = description

    @property
    def request_process_type(self):
        """
        Gets the request_process_type of this WsdlPolicies1.


        :return: The request_process_type of this WsdlPolicies1.
        :rtype: str
        """
        return self._request_process_type

    @request_process_type.setter
    def request_process_type(self, request_process_type):
        """
        Sets the request_process_type of this WsdlPolicies1.


        :param request_process_type: The request_process_type of this WsdlPolicies1.
        :type: str
        """
        allowed_values = ["TASK_LIST", "TASK_LIST_GROUP"]
        if request_process_type not in allowed_values:
            raise ValueError(
                "Invalid value for `request_process_type` ({0}), must be one of {1}"
                .format(request_process_type, allowed_values)
            )

        self._request_process_type = request_process_type

    @property
    def post_process_response(self):
        """
        Gets the post_process_response of this WsdlPolicies1.


        :return: The post_process_response of this WsdlPolicies1.
        :rtype: bool
        """
        return self._post_process_response

    @post_process_response.setter
    def post_process_response(self, post_process_response):
        """
        Sets the post_process_response of this WsdlPolicies1.


        :param post_process_response: The post_process_response of this WsdlPolicies1.
        :type: bool
        """

        self._post_process_response = post_process_response

    @property
    def wsdl_definition_name(self):
        """
        Gets the wsdl_definition_name of this WsdlPolicies1.


        :return: The wsdl_definition_name of this WsdlPolicies1.
        :rtype: str
        """
        return self._wsdl_definition_name

    @wsdl_definition_name.setter
    def wsdl_definition_name(self, wsdl_definition_name):
        """
        Sets the wsdl_definition_name of this WsdlPolicies1.


        :param wsdl_definition_name: The wsdl_definition_name of this WsdlPolicies1.
        :type: str
        """

        self._wsdl_definition_name = wsdl_definition_name

    @property
    def wsi_validation(self):
        """
        Gets the wsi_validation of this WsdlPolicies1.


        :return: The wsi_validation of this WsdlPolicies1.
        :rtype: bool
        """
        return self._wsi_validation

    @wsi_validation.setter
    def wsi_validation(self, wsi_validation):
        """
        Sets the wsi_validation of this WsdlPolicies1.


        :param wsi_validation: The wsi_validation of this WsdlPolicies1.
        :type: bool
        """

        self._wsi_validation = wsi_validation

    @property
    def post_process_request(self):
        """
        Gets the post_process_request of this WsdlPolicies1.


        :return: The post_process_request of this WsdlPolicies1.
        :rtype: bool
        """
        return self._post_process_request

    @post_process_request.setter
    def post_process_request(self, post_process_request):
        """
        Sets the post_process_request of this WsdlPolicies1.


        :param post_process_request: The post_process_request of this WsdlPolicies1.
        :type: bool
        """

        self._post_process_request = post_process_request

    @property
    def operations(self):
        """
        Gets the operations of this WsdlPolicies1.


        :return: The operations of this WsdlPolicies1.
        :rtype: list[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """
        Sets the operations of this WsdlPolicies1.


        :param operations: The operations of this WsdlPolicies1.
        :type: list[str]
        """

        self._operations = operations

    @property
    def post_request_process(self):
        """
        Gets the post_request_process of this WsdlPolicies1.


        :return: The post_request_process of this WsdlPolicies1.
        :rtype: str
        """
        return self._post_request_process

    @post_request_process.setter
    def post_request_process(self, post_request_process):
        """
        Sets the post_request_process of this WsdlPolicies1.


        :param post_request_process: The post_request_process of this WsdlPolicies1.
        :type: str
        """

        self._post_request_process = post_request_process

    @property
    def response_process_type(self):
        """
        Gets the response_process_type of this WsdlPolicies1.


        :return: The response_process_type of this WsdlPolicies1.
        :rtype: str
        """
        return self._response_process_type

    @response_process_type.setter
    def response_process_type(self, response_process_type):
        """
        Sets the response_process_type of this WsdlPolicies1.


        :param response_process_type: The response_process_type of this WsdlPolicies1.
        :type: str
        """
        allowed_values = ["TASK_LIST", "TASK_LIST_GROUP"]
        if response_process_type not in allowed_values:
            raise ValueError(
                "Invalid value for `response_process_type` ({0}), must be one of {1}"
                .format(response_process_type, allowed_values)
            )

        self._response_process_type = response_process_type

    @property
    def idp_group(self):
        """
        Gets the idp_group of this WsdlPolicies1.


        :return: The idp_group of this WsdlPolicies1.
        :rtype: str
        """
        return self._idp_group

    @idp_group.setter
    def idp_group(self, idp_group):
        """
        Sets the idp_group of this WsdlPolicies1.


        :param idp_group: The idp_group of this WsdlPolicies1.
        :type: str
        """

        self._idp_group = idp_group

    @property
    def password(self):
        """
        Gets the password of this WsdlPolicies1.


        :return: The password of this WsdlPolicies1.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this WsdlPolicies1.


        :param password: The password of this WsdlPolicies1.
        :type: str
        """

        self._password = password

    @property
    def process_response(self):
        """
        Gets the process_response of this WsdlPolicies1.


        :return: The process_response of this WsdlPolicies1.
        :rtype: bool
        """
        return self._process_response

    @process_response.setter
    def process_response(self, process_response):
        """
        Sets the process_response of this WsdlPolicies1.


        :param process_response: The process_response of this WsdlPolicies1.
        :type: bool
        """

        self._process_response = process_response

    @property
    def request_process(self):
        """
        Gets the request_process of this WsdlPolicies1.


        :return: The request_process of this WsdlPolicies1.
        :rtype: str
        """
        return self._request_process

    @request_process.setter
    def request_process(self, request_process):
        """
        Sets the request_process of this WsdlPolicies1.


        :param request_process: The request_process of this WsdlPolicies1.
        :type: str
        """

        self._request_process = request_process

    @property
    def allow_additional_headers(self):
        """
        Gets the allow_additional_headers of this WsdlPolicies1.


        :return: The allow_additional_headers of this WsdlPolicies1.
        :rtype: bool
        """
        return self._allow_additional_headers

    @allow_additional_headers.setter
    def allow_additional_headers(self, allow_additional_headers):
        """
        Sets the allow_additional_headers of this WsdlPolicies1.


        :param allow_additional_headers: The allow_additional_headers of this WsdlPolicies1.
        :type: bool
        """

        self._allow_additional_headers = allow_additional_headers

    @property
    def wsdl_namespace(self):
        """
        Gets the wsdl_namespace of this WsdlPolicies1.


        :return: The wsdl_namespace of this WsdlPolicies1.
        :rtype: str
        """
        return self._wsdl_namespace

    @wsdl_namespace.setter
    def wsdl_namespace(self, wsdl_namespace):
        """
        Sets the wsdl_namespace of this WsdlPolicies1.


        :param wsdl_namespace: The wsdl_namespace of this WsdlPolicies1.
        :type: str
        """

        self._wsdl_namespace = wsdl_namespace

    @property
    def response_process(self):
        """
        Gets the response_process of this WsdlPolicies1.


        :return: The response_process of this WsdlPolicies1.
        :rtype: str
        """
        return self._response_process

    @response_process.setter
    def response_process(self, response_process):
        """
        Sets the response_process of this WsdlPolicies1.


        :param response_process: The response_process of this WsdlPolicies1.
        :type: str
        """

        self._response_process = response_process

    @property
    def wsdl_service_name(self):
        """
        Gets the wsdl_service_name of this WsdlPolicies1.


        :return: The wsdl_service_name of this WsdlPolicies1.
        :rtype: str
        """
        return self._wsdl_service_name

    @wsdl_service_name.setter
    def wsdl_service_name(self, wsdl_service_name):
        """
        Sets the wsdl_service_name of this WsdlPolicies1.


        :param wsdl_service_name: The wsdl_service_name of this WsdlPolicies1.
        :type: str
        """

        self._wsdl_service_name = wsdl_service_name

    @property
    def envelope_validation(self):
        """
        Gets the envelope_validation of this WsdlPolicies1.


        :return: The envelope_validation of this WsdlPolicies1.
        :rtype: bool
        """
        return self._envelope_validation

    @envelope_validation.setter
    def envelope_validation(self, envelope_validation):
        """
        Sets the envelope_validation of this WsdlPolicies1.


        :param envelope_validation: The envelope_validation of this WsdlPolicies1.
        :type: bool
        """

        self._envelope_validation = envelope_validation

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
