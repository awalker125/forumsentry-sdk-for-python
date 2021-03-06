Developer Documentation
=======================

Installing Development Environment
----------------------------------

Your life will be a lot better if you use a virtualenv when working with python.

1. Fork and Clone this repo
2. Install `python-pip <https://pip.pypa.io/en/stable/installing/>`__ and `virtualenv <https://virtualenv.pypa.io/en/stable/>`__ if you do not already have it.
3. Create a new virtualenv with ``virtualenv forumsentry-sdk-for-python``.
4. Actiavte the new virtualenv with ``source forumsentry-sdk-for-python/bin/activate``.
5. Run ``make dev``
6. Hack away!

Running Tests
-------------

Tests can be found in the ``tests`` directory. 

You can run tests with ``make tests``. 

If you want to run a specific test file you can do so with:

::

    python -m unittest tests/sentry/test_$MODULE.py

This project has two main types of tests.

* Unit tests. These are tests of specific functions using mocked API data.
* Integration tests. These are tests that actually hit a forum sentry device. Unfortunately, this will need to be setup by the developer and conectivity from the machine running the tests established. 

In order to run the intergration tests then setup the following environment variables.

:: 
   export FORUM_REST_API_HOST=forumsentry-dev
   export FORUM_REST_API_PORT=8081
   export FORUM_REST_API_USER=admin
   export FORUM_REST_API_PASSWORD=*******    


Code Coverage
~~~~~~~~~~~~~

This project attempts to have 100% code coverage. when you run ``make test`` code coverage is automatically ran. You can view the code coverage report locally by opening up the index.html file in the ``htmlcov`` directory that gets created when you run ``make test``. 


Swagger
-------

The forumsentry provide swagger documentation. A tools directory is provided with a script to generate python models from the swagger api.

To run this
	
.. code:: bash

	cd tools
	export FORUM_REST_API_HOST=xxxxxxxxxxxxx
	export FORUM_REST_API_USER=xxxxxxxxxxxxx
	export FORUM_REST_API_PASSWORD=xxxxxxxxxxx
	./generate_code.sh

This will place the models swagger generated code in a folder _build

* Note: _build is listed in the .gitignore file. For now you will need to manually merge/extract anything useful from there. *

If you need to make changes to the generate code first see if it can be made in the templates under tools/templates/python. That way adding new models will be easier in the future.

Documentation
-------------

This project uses sphinx for documentation. You can generate the latest docs locally by running ``make docs``. You can then view them by opening up the ``index.html`` file in the ``docs/build/html`` directory. 

Linting and Style
-----------------

This project follows the `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ style guidelines. You can install ``pylint`` in order to ensure that all of your code is compliant with this standard. 

Generating p12 for testing
--------------------------

When working with the KeyPairs API we need a p12 to upload. To create one use the following

.. code-block:: bash

   #Create a temp server cert with SANs
   export CNAME=forumsentry-sdk-for-python
   export PASSWORD=password
   #create private key
   openssl genrsa -out ${CNAME}.key 4096
   #create temp CA
   openssl req -new -x509 -sha256 -nodes -days 3650  -key ${CNAME}.key -out ${CNAME}-ca.pem -subj "/CN=${CNAME}-ca"
   #cp ${CNAME}-ca.pem /etc/pki/ca-trust/source/anchors/${CNAME}-ca.pem; update-ca-trust extract
   #create config file for request/signing
   cat /etc/pki/tls/openssl.cnf > ${CNAME}.cnf
   cat >> ${CNAME}.cnf  << END
   [req]
   req_extensions = v3_req
   
   [ v3_req ]
   
   # Extensions to add to a certificate request
   
   basicConstraints = CA:FALSE
   keyUsage = nonRepudiation, digitalSignature, keyEncipherment
   extendedKeyUsage = serverAuth
   subjectAltName = @alt_names
   
   [alt_names]
   DNS.1 = ${CNAME}
   END
   
   #Generate CSR
   openssl req -subj "/CN=${CNAME}" -sha256 -new -key ${CNAME}.key -out ${CNAME}.csr  -config ${CNAME}.cnf
   #Sign the CSR with the temp CA
   openssl x509 -req  -sha256 -in ${CNAME}.csr -CA ${CNAME}-ca.pem -CAkey ${CNAME}.key -CAcreateserial -out ${CNAME}.cer -days 730 -extfile ${CNAME}.cnf -extensions v3_req
   #Create passphrase file 
   echo -n ${PASSWORD} > .${CNAME}_passphrase
   
   #Create p12
   openssl pkcs12 -export -out  ${CNAME}.p12  -in ${CNAME}.cer -inkey ${CNAME}.key -certfile ${CNAME}-ca.pem -password file:.${CNAME}_passphrase
   #Create jks
   keytool -importkeystore -srckeystore ${CNAME}.p12 -srcstoretype pkcs12 -destkeystore ${CNAME}.jks -deststoretype JKS -srcstorepass ${PASSWORD}  -deststorepass ${PASSWORD}


