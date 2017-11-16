from setuptools import setup
from setuptools import find_packages
import os

#Change this on major version number
major_minor_version = 1.0
#This will be overriden if build.info exists
build = 0


def __path(filename):
    return os.path.join(os.path.dirname(__file__),filename)



if os.path.exists(__path('build.info')):
    build = open(__path('build.info')).read().strip()

version= '{0}.{1}'.format(str(major_minor_version),str(build))

setup(
    name='forumsentry',
    version=version,
    long_description="Forum Sentry sdk for Python",
    author="awalker125",
    author_email="awalker125@users.noreply.github.com",
    include_package_data=True,
    zip_safe=False,
    install_requires=['futures;python_version<="2.7"'],
    packages=find_packages(),
    url="https://github.com/awalker125/forumsentry-sdk-for-python"
    
)
