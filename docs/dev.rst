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

Code Coverage
~~~~~~~~~~~~~

This project attempts to have 100% code coverage. when you run ``make test`` code coverage is automatically ran. You can view the code coverage report locally by opening up the index.html file in the ``htmlcov`` directory that gets created when you run ``make test``. 


Swagger
------------

The forumsentry provide swagger documentation. A tools directory is provided with a script to generate python models from the swagger api.

To run this
	
.. code:: bash

	cd tools
	export REST_API_HOST=xxxxxxxxxxxxx
	export REST_API_USER=xxxxxxxxxxxxx
	export REST_API_PASSWORD=xxxxxxxxxxx
	./generate_code.sh

This will place the models swagger generated code in a folder _build

* Note: _build is listed in the .gitignore file. For now you will need to manually merge/extract anything useful from there. *


Documentation
-------------

This project uses sphinx for documentation. You can generate the latest docs locally by running ``make docs``. You can then view them by opening up the ``index.html`` file in the ``docs/build/html`` directory. 

Linting and Style
-----------------

This project follows the `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ style guidelines. You can install ``pylint`` in order to ensure that all of your code is compliant with this standard. 



