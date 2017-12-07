Quickstart
==========

Installation
------------

You can install the latest version of forumsentry with: 

::

    pip install forumsentry

Basic Usage
-----------


Import the Forum Sentry API and start using methods:

::

    from forumsentry.api import api

    forumsentry = api(username="admin",password="password")

    # get a list of all listenerPolices
    forumsentry.get_listener_polices()


