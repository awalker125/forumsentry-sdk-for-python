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
    
            # Logging Settings
        #self._logger = {}
        #self._logger["package_logger"] = logging.getLogger("forumsentry")
        # self._logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        #self._logger_format = '%(asctime)s %(levelname)s %(message)s'
        
        #self._logger_formatter = logging.Formatter(self._logger_format)
        # Log stream handler
        #self._logger_stream_handler = None
        # Log file handler
        #self._logger_file_handler = None
        # Debug file location
        #self._logger_file = None
        
        #self._logger_stream = False
        
        #self._setup_logging()
      
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
            logging.basicConfig(level=default_level, format=default_format)
            
        self._logger = logging.getLogger("forumsentry")
        self._logger.debug("logging init complete")
        
        

 
 
#     def _setup_logging(self):
#         
#         if self._logger_file:
#             # If set logging file,
#             # then add file handler
#             self._logger_file_handler = logging.FileHandler(self._logger_file)
#             self._logger_file_handler.setFormatter(self._logger_formatter)
#             for k, l in six.iteritems(self._logger):
#                 l.addHandler(self._logger_file_handler)
#         else:
#             if self._logger_file_handler:
#                 for k, l in six.iteritems(self._logger):
#                     l.removeHandler(self._logger_file_handler)
#                 self._logger_file_handler = None
# 
#         if self.logger_stream:
#             # If stream logging is set then create a handler and add to each logger
# 
#             self._logger_stream_handler = logging.StreamHandler()
#             self._logger_stream_handler.setFormatter(self._logger_formatter)
#             for k, l in six.iteritems(self._logger):
#                 l.addHandler(self._logger_stream_handler)
#         else:
#             # If stream logging is not set then remove the handler from each logger and delete
#             if self._logger_stream_handler:
#                 for k, l in six.iteritems(self._logger):
#                     l.removeHandler(self._logger_stream_handler)
#                 self._logger_stream_handler = None
        
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


#     @property
#     def logger_stream(self):
#         return self._logger_stream
#     
#     @logger_stream.setter
#     def logger_stream(self, value):
#         """Enable stream logger
# 
#         :param value: if stream logger should be enabled
#         :type: bool
#         """
#         self._logger_stream = value
#         self._setup_logging()
    
    
#     @property
#     def logger_file(self):
#         """The logger file.
# 
#         If the logger_file is None, then add stream handler and remove file
#         handler. Otherwise, add file handler and remove stream handler.
# 
#         :param value: The logger_file path.
#         :type: str
#         """
#         return self._logger_file
# 
#     @logger_file.setter
#     def logger_file(self, value):
#         """The logger file.
# 
#         If the logger_file is None, then add stream handler and remove file
#         handler. Otherwise, add file handler and remove stream handler.
# 
#         :param value: The logger_file path.
#         :type: str
#         """
#         self._logger_file = value
#         self._setup_logging()

# 
#     @property
#     def debug(self):
#         """Debug status
# 
#         :param value: The debug status, True or False.
#         :type: bool
#         """
#         return self._debug
# 
#     @debug.setter
#     def debug(self, value):
#         """Debug status
# 
#         :param value: The debug status, True or False.
#         :type: bool
#         """
#         self._debug = value
#         if self._debug:
#             # if debug status is True, turn on debug logging
#             self._enable_debug()
#         else:
#             # if debug status is False, turn off debug logging,
#             # setting log level to default `logging.WARNING`
#             self._disable_debug()
# 
#     def _enable_debug(self):
#         
#         for k, l in six.iteritems(self._logger):
#             l.setLevel(logging.DEBUG)
#             # turn on httplib debug
#         httplib.HTTPConnection.debuglevel = 1
#     
#     def _disable_debug(self):
#         
#         for k, l in six.iteritems(self._logger):
#             l.setLevel(logging.WARNING)
#             # turn on httplib debug
#         httplib.HTTPConnection.debuglevel = 0    

#     @property
#     def logger_format(self):
#         """The logger format.
# 
#         The logger_formatter will be updated when sets logger_format.
# 
#         :param value: The format string.
#         :type: str
#         """
#         return self._logger_format
# 
#     @logger_format.setter
#     def logger_format(self, value):
#         """The logger format.
# 
#         The logger_formatter will be updated when sets logger_format.
# 
#         :param value: The format string.
#         :type: str
#         """
#         self._logger_format = value
#         self._logger_formatter = logging.Formatter(self._logger_format)
