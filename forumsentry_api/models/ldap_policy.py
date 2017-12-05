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


class LdapPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, certificate_id=None, authentication_type=None, host=None, restrict_menus=None, filter_value=None, use_ssl=None, enabled=None, principal=None, context=None, referral_processing=None, read_timeout_minutes=None, user_id=None, name=None, description=None, password_id=None, cache_timeout=None, filter_id=None, group_id=None, dn_id=None, search_scope=None, context_type=None, email_id=None, port=None, role_policy=None):
        """
        LdapPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'certificate_id': 'str',
            'authentication_type': 'str',
            'host': 'str',
            'restrict_menus': 'bool',
            'filter_value': 'str',
            'use_ssl': 'bool',
            'enabled': 'bool',
            'principal': 'str',
            'context': 'str',
            'referral_processing': 'str',
            'read_timeout_minutes': 'int',
            'user_id': 'str',
            'name': 'str',
            'description': 'str',
            'password_id': 'str',
            'cache_timeout': 'int',
            'filter_id': 'str',
            'group_id': 'str',
            'dn_id': 'str',
            'search_scope': 'str',
            'context_type': 'str',
            'email_id': 'str',
            'port': 'int',
            'role_policy': 'str'
        }

        self.attribute_map = {
            'certificate_id': 'certificateId',
            'authentication_type': 'authenticationType',
            'host': 'host',
            'restrict_menus': 'restrictMenus',
            'filter_value': 'filterValue',
            'use_ssl': 'useSsl',
            'enabled': 'enabled',
            'principal': 'principal',
            'context': 'context',
            'referral_processing': 'referralProcessing',
            'read_timeout_minutes': 'readTimeoutMinutes',
            'user_id': 'userId',
            'name': 'name',
            'description': 'description',
            'password_id': 'passwordId',
            'cache_timeout': 'cacheTimeout',
            'filter_id': 'filterId',
            'group_id': 'groupId',
            'dn_id': 'dnId',
            'search_scope': 'searchScope',
            'context_type': 'contextType',
            'email_id': 'emailId',
            'port': 'port',
            'role_policy': 'rolePolicy'
        }

        self._certificate_id = certificate_id
        self._authentication_type = authentication_type
        self._host = host
        self._restrict_menus = restrict_menus
        self._filter_value = filter_value
        self._use_ssl = use_ssl
        self._enabled = enabled
        self._principal = principal
        self._context = context
        self._referral_processing = referral_processing
        self._read_timeout_minutes = read_timeout_minutes
        self._user_id = user_id
        self._name = name
        self._description = description
        self._password_id = password_id
        self._cache_timeout = cache_timeout
        self._filter_id = filter_id
        self._group_id = group_id
        self._dn_id = dn_id
        self._search_scope = search_scope
        self._context_type = context_type
        self._email_id = email_id
        self._port = port
        self._role_policy = role_policy

    @property
    def certificate_id(self):
        """
        Gets the certificate_id of this LdapPolicy.


        :return: The certificate_id of this LdapPolicy.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this LdapPolicy.


        :param certificate_id: The certificate_id of this LdapPolicy.
        :type: str
        """

        self._certificate_id = certificate_id

    @property
    def authentication_type(self):
        """
        Gets the authentication_type of this LdapPolicy.


        :return: The authentication_type of this LdapPolicy.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """
        Sets the authentication_type of this LdapPolicy.


        :param authentication_type: The authentication_type of this LdapPolicy.
        :type: str
        """
        allowed_values = ["NONE", "SIMPLE", "SASL"]
        if authentication_type not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_type` ({0}), must be one of {1}"
                .format(authentication_type, allowed_values)
            )

        self._authentication_type = authentication_type

    @property
    def host(self):
        """
        Gets the host of this LdapPolicy.


        :return: The host of this LdapPolicy.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this LdapPolicy.


        :param host: The host of this LdapPolicy.
        :type: str
        """

        self._host = host

    @property
    def restrict_menus(self):
        """
        Gets the restrict_menus of this LdapPolicy.


        :return: The restrict_menus of this LdapPolicy.
        :rtype: bool
        """
        return self._restrict_menus

    @restrict_menus.setter
    def restrict_menus(self, restrict_menus):
        """
        Sets the restrict_menus of this LdapPolicy.


        :param restrict_menus: The restrict_menus of this LdapPolicy.
        :type: bool
        """

        self._restrict_menus = restrict_menus

    @property
    def filter_value(self):
        """
        Gets the filter_value of this LdapPolicy.


        :return: The filter_value of this LdapPolicy.
        :rtype: str
        """
        return self._filter_value

    @filter_value.setter
    def filter_value(self, filter_value):
        """
        Sets the filter_value of this LdapPolicy.


        :param filter_value: The filter_value of this LdapPolicy.
        :type: str
        """

        self._filter_value = filter_value

    @property
    def use_ssl(self):
        """
        Gets the use_ssl of this LdapPolicy.


        :return: The use_ssl of this LdapPolicy.
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """
        Sets the use_ssl of this LdapPolicy.


        :param use_ssl: The use_ssl of this LdapPolicy.
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def enabled(self):
        """
        Gets the enabled of this LdapPolicy.


        :return: The enabled of this LdapPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this LdapPolicy.


        :param enabled: The enabled of this LdapPolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def principal(self):
        """
        Gets the principal of this LdapPolicy.


        :return: The principal of this LdapPolicy.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """
        Sets the principal of this LdapPolicy.


        :param principal: The principal of this LdapPolicy.
        :type: str
        """

        self._principal = principal

    @property
    def context(self):
        """
        Gets the context of this LdapPolicy.


        :return: The context of this LdapPolicy.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this LdapPolicy.


        :param context: The context of this LdapPolicy.
        :type: str
        """

        self._context = context

    @property
    def referral_processing(self):
        """
        Gets the referral_processing of this LdapPolicy.


        :return: The referral_processing of this LdapPolicy.
        :rtype: str
        """
        return self._referral_processing

    @referral_processing.setter
    def referral_processing(self, referral_processing):
        """
        Sets the referral_processing of this LdapPolicy.


        :param referral_processing: The referral_processing of this LdapPolicy.
        :type: str
        """
        allowed_values = ["FOLLOW", "IGNORE", "THROW"]
        if referral_processing not in allowed_values:
            raise ValueError(
                "Invalid value for `referral_processing` ({0}), must be one of {1}"
                .format(referral_processing, allowed_values)
            )

        self._referral_processing = referral_processing

    @property
    def read_timeout_minutes(self):
        """
        Gets the read_timeout_minutes of this LdapPolicy.


        :return: The read_timeout_minutes of this LdapPolicy.
        :rtype: int
        """
        return self._read_timeout_minutes

    @read_timeout_minutes.setter
    def read_timeout_minutes(self, read_timeout_minutes):
        """
        Sets the read_timeout_minutes of this LdapPolicy.


        :param read_timeout_minutes: The read_timeout_minutes of this LdapPolicy.
        :type: int
        """

        self._read_timeout_minutes = read_timeout_minutes

    @property
    def user_id(self):
        """
        Gets the user_id of this LdapPolicy.


        :return: The user_id of this LdapPolicy.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this LdapPolicy.


        :param user_id: The user_id of this LdapPolicy.
        :type: str
        """

        self._user_id = user_id

    @property
    def name(self):
        """
        Gets the name of this LdapPolicy.


        :return: The name of this LdapPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LdapPolicy.


        :param name: The name of this LdapPolicy.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this LdapPolicy.


        :return: The description of this LdapPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LdapPolicy.


        :param description: The description of this LdapPolicy.
        :type: str
        """

        self._description = description

    @property
    def password_id(self):
        """
        Gets the password_id of this LdapPolicy.


        :return: The password_id of this LdapPolicy.
        :rtype: str
        """
        return self._password_id

    @password_id.setter
    def password_id(self, password_id):
        """
        Sets the password_id of this LdapPolicy.


        :param password_id: The password_id of this LdapPolicy.
        :type: str
        """

        self._password_id = password_id

    @property
    def cache_timeout(self):
        """
        Gets the cache_timeout of this LdapPolicy.


        :return: The cache_timeout of this LdapPolicy.
        :rtype: int
        """
        return self._cache_timeout

    @cache_timeout.setter
    def cache_timeout(self, cache_timeout):
        """
        Sets the cache_timeout of this LdapPolicy.


        :param cache_timeout: The cache_timeout of this LdapPolicy.
        :type: int
        """

        self._cache_timeout = cache_timeout

    @property
    def filter_id(self):
        """
        Gets the filter_id of this LdapPolicy.


        :return: The filter_id of this LdapPolicy.
        :rtype: str
        """
        return self._filter_id

    @filter_id.setter
    def filter_id(self, filter_id):
        """
        Sets the filter_id of this LdapPolicy.


        :param filter_id: The filter_id of this LdapPolicy.
        :type: str
        """

        self._filter_id = filter_id

    @property
    def group_id(self):
        """
        Gets the group_id of this LdapPolicy.


        :return: The group_id of this LdapPolicy.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this LdapPolicy.


        :param group_id: The group_id of this LdapPolicy.
        :type: str
        """

        self._group_id = group_id

    @property
    def dn_id(self):
        """
        Gets the dn_id of this LdapPolicy.


        :return: The dn_id of this LdapPolicy.
        :rtype: str
        """
        return self._dn_id

    @dn_id.setter
    def dn_id(self, dn_id):
        """
        Sets the dn_id of this LdapPolicy.


        :param dn_id: The dn_id of this LdapPolicy.
        :type: str
        """

        self._dn_id = dn_id

    @property
    def search_scope(self):
        """
        Gets the search_scope of this LdapPolicy.


        :return: The search_scope of this LdapPolicy.
        :rtype: str
        """
        return self._search_scope

    @search_scope.setter
    def search_scope(self, search_scope):
        """
        Sets the search_scope of this LdapPolicy.


        :param search_scope: The search_scope of this LdapPolicy.
        :type: str
        """
        allowed_values = ["OBJECT_SCOPE", "ONELEVEL_SCOPE", "SUBTREE_SCOPE"]
        if search_scope not in allowed_values:
            raise ValueError(
                "Invalid value for `search_scope` ({0}), must be one of {1}"
                .format(search_scope, allowed_values)
            )

        self._search_scope = search_scope

    @property
    def context_type(self):
        """
        Gets the context_type of this LdapPolicy.


        :return: The context_type of this LdapPolicy.
        :rtype: str
        """
        return self._context_type

    @context_type.setter
    def context_type(self, context_type):
        """
        Sets the context_type of this LdapPolicy.


        :param context_type: The context_type of this LdapPolicy.
        :type: str
        """
        allowed_values = ["USER", "GROUP"]
        if context_type not in allowed_values:
            raise ValueError(
                "Invalid value for `context_type` ({0}), must be one of {1}"
                .format(context_type, allowed_values)
            )

        self._context_type = context_type

    @property
    def email_id(self):
        """
        Gets the email_id of this LdapPolicy.


        :return: The email_id of this LdapPolicy.
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """
        Sets the email_id of this LdapPolicy.


        :param email_id: The email_id of this LdapPolicy.
        :type: str
        """

        self._email_id = email_id

    @property
    def port(self):
        """
        Gets the port of this LdapPolicy.


        :return: The port of this LdapPolicy.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this LdapPolicy.


        :param port: The port of this LdapPolicy.
        :type: int
        """

        self._port = port

    @property
    def role_policy(self):
        """
        Gets the role_policy of this LdapPolicy.


        :return: The role_policy of this LdapPolicy.
        :rtype: str
        """
        return self._role_policy

    @role_policy.setter
    def role_policy(self, role_policy):
        """
        Sets the role_policy of this LdapPolicy.


        :param role_policy: The role_policy of this LdapPolicy.
        :type: str
        """

        self._role_policy = role_policy

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