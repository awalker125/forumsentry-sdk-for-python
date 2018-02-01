Logging
=======

Defaults
--------

By default, (if you do nothing) the forumsentry sdk for python will setup the root logger to stream to stderr.

This works better with ansible and other tools that may call it.

Additionally logging level is set to **FATAL** which means no messages will be emitted from forumsentry sdk for python.


Debugging
---------

If the environment **FSENTRY_DEBUG** is set then the logging level will be set to debug 

.. code-block:: bash

    export FSENTRY_DEBUG=TRUE


Config
------


A yaml config file can be used to gain full control over logging.

Set the environment variable **FSENTRY_LOG_YAML** to the location of your yaml config file.

E.g

.. code-block:: bash

    export FSENTRY_LOG_YAML=/etc/fsentry.yaml

The default location if the **FSENTRY_LOG_YAML** is **~/fsentry_log.yaml**

If the file given by **FSENTRY_LOG_YAML** or the default **~/fsentry_log.yaml** exists then those settings will be used.

If the file is not found then the default above will be used.

See below for an example config

.. code-block:: yaml

   ---
   
   #https://docs.python.org/2/library/logging.config.html#logging-config-dictschema
   
   version: 1
   disable_existing_loggers: False
   formatters:
       simple:
           format: "%(asctime)s - %(levelname)s - %(name)s - %(module)s.%(funcName)s: %(message)s"
   
   handlers:
       console:
           class: logging.StreamHandler
           level: ERROR
           formatter: simple
           stream: ext://sys.stderr
   
   
       debug_file_handler:
           class: logging.handlers.RotatingFileHandler
           level: DEBUG
           formatter: simple
           filename: /tmp/logs/debug.log
           maxBytes: 10485760 # 10MB
           backupCount: 20
           encoding: utf8
   
       info_file_handler:
           class: logging.handlers.RotatingFileHandler
           level: INFO
           formatter: simple
           filename: /tmp/logs/info.log
           maxBytes: 10485760 # 10MB
           backupCount: 20
           encoding: utf8
   
       error_file_handler:
           class: logging.handlers.RotatingFileHandler
           level: ERROR
           formatter: simple
           filename: /tmp/logs/errors.log
           maxBytes: 10485760 # 10MB
           backupCount: 20
           encoding: utf8
   
   loggers:
       forumsentry:
           level: DEBUG
           handlers: [console, debug_file_handler, info_file_handler, error_file_handler]
           propagate: false
       urllib3:
           level: CRITICAL
           handlers: [console, info_file_handler, error_file_handler]
   root:
       level: CRITICAL
       handlers: [console, info_file_handler, error_file_handler]


