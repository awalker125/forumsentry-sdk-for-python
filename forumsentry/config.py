'''
Created on 7 Dec 2017

@author: walandre
'''

import logging
import logging.config
import os
from os.path import expanduser
import urllib3
import yaml


import six
from six.moves import http_client as httplib
import sys


class Config(object):
    '''
    classdocs
    '''


    def __init__(self, host=None, port=None, protocol=None, context=None, username=None, password=None, verify_ssl=True, ssl_ca_file=None):
        '''
        Constructor
        '''
        
        # some defaults
        
        self._host = "localhost"
        self._port = "443"
        self._protocol = "https"
        self._context = "/restApi/v1.0"
        self._username = ""
        self._password = ""
        
         # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self._verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self._ssl_ca_cert = None
        # client certificate file
        #self._cert_file = None
        # client key file
        #self._key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        #self._assert_hostname = None
         
        if host is not None:
            self._host = host
        if port is not None:
            self._port = port
        if protocol is not None:
            self._protocol = protocol            
        if context is not None:
            self._context = context             
        if username is not None:
            self._username = username             
        if password is not None:
            self._password = password
        if ssl_ca_file is not None:
            self._ssl_ca_file = ssl_ca_file
        
        self._verify_ssl = verify_ssl
          
        if os.getenv("FSENTRY_DEBUG", None) is not None:
            self.__setup_logging(default_level=logging.DEBUG)
        else:
            self.__setup_logging()
 
    def __setup_logging(self, default_level=logging.FATAL):
        """
        Setup logging configuration
        #https://docs.python.org/2/library/logging.config.html#logging-config-dictschema
        """
        #print default_level
        default_format = "%(asctime)s - %(levelname)s - %(name)s - %(module)s.%(funcName)s: %(message)s"
        
        home_dir = expanduser("~")
        
        logging_config = os.getenv("FSENTRY_LOG_YAML", '{0}/fsentry_log.yaml'.format(home_dir))
        
        
        if os.path.exists(logging_config):
            #try as if logging_config is an absolute path
            with open(logging_config, 'rt') as f:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
        else:
            #print "WARN: could not find {0}".format(logging_config)
            #log to stderr. This works better with ansible
            logging.basicConfig(level=default_level, format=default_format,stream=sys.stderr)
            
        self._logger = logging.getLogger("forumsentry")
        self._logger.debug("logging init complete")
        
        
        
    @property
    def host(self):
        """Gets the forumsentry host.  # noqa: E501


        :return: The forumsentry host.  # noqa: E501
        :rtype: str
        """
        return self._host
    
    @host.setter
    def host(self, host):
        """Sets the forumsentry host.


        :param host: The host of this forumsentry.  # noqa: E501
        :type: str
        """
        self._host = host
        
    @property
    def port(self):
        """Gets the forumsentry port.  # noqa: E501


        :return: The forumsentry port.  # noqa: E501
        :rtype: int
        """
        return self._port
    
    @port.setter
    def port(self, port):
        """Sets the forumsentry port.


        :param port: The port of this forumsentry.  # noqa: E501
        :type: int
        """
        self._port = port
        

    @property
    def username(self):
        """Gets the forumsentry username.  # noqa: E501


        :return: The forumsentry username.  # noqa: E501
        :rtype: str
        """
        return self._username
    
    @username.setter
    def username(self, username):
        """Sets the forumsentry username.


        :param username: The username of this forumsentry.  # noqa: E501
        :type: str
        """
        self._username = username
    
    @property
    def password(self):
        """Gets the forumsentry password.  # noqa: E501


        :return: The forumsentry password.  # noqa: E501
        :rtype: str
        """
        return self._password
    
    @password.setter
    def password(self, password):
        """Sets the forumsentry password.


        :param password: The password of this forumsentry.  # noqa: E501
        :type: str
        """
        self._password = password        
        

    @property
    def protocol(self):
        """Gets the forumsentry protocol.  # noqa: E501


        :return: The forumsentry protocol.  # noqa: E501
        :rtype: str
        """
        return self._protocol
    
    @protocol.setter
    def protocol(self, protocol):
        """Sets the forumsentry protocol.


        :param protocol: The protocol of this forumsentry.  # noqa: E501
        :type: str
        """
        self._protocol = protocol
    

    @property
    def context(self):
        """Gets the forumsentry context.  # noqa: E501


        :return: The forumsentry context.  # noqa: E501
        :rtype: str
        """
        return self._context
    
    @context.setter
    def context(self, context):
        """Sets the forumsentry context.


        :param context: The context of this forumsentry.  # noqa: E501
        :type: str
        """
        self._context = context

    @property
    def verify_ssl(self):
        """Gets if we should verify ssl when connecting to forum.  # noqa: E501


        :return: The value of verify_ssl propertu.  # noqa: E501
        :rtype: bool
        """
        return self._verify_ssl
    
    @verify_ssl.setter
    def verify_ssl(self, verify_ssl):
        """Sets if we should verify ssl when connecting to forum.


        :param verify_ssl: if we should verify ssl when connecting to forum.  # noqa: E501
        :type: bool
        """
        self._verify_ssl = verify_ssl

    @property
    def ssl_ca_file(self):
        """Gets the forumsentry ssl_ca_file.  # noqa: E501


        :return: The forumsentry ssl_ca_file.  # noqa: E501
        :rtype: str
        """
        return self._ssl_ca_file
    
    @ssl_ca_file.setter
    def ssl_ca_file(self, ssl_ca_file):
        """Sets the forumsentry ssl_ca_file.


        :param ssl_ca_file: The ssl_ca_file of this forumsentry.  # noqa: E501
        :type: str
        """
        self._ssl_ca_file = ssl_ca_file
        
    @property
    def forumsentry_url(self):
        url = "{0}://{1}:{2}{3}".format(self._protocol, self._host, str(self._port), self._context)
        self._logger.debug("url: {0}".format(url))
        return url
    
    @property
    def basic_authentication_header(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        
        if not self._username:
            self._logger.warn("username not set")
        if not self._password:
            self._logger.warn("password not set")
        ba_auth_header = urllib3.util.make_headers(basic_auth=self._username + ':' + self._password).get('authorization')
        
        self._logger.debug("ba_auth_header: {0}".format(ba_auth_header))
        return ba_auth_header
