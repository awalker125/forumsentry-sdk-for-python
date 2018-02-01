import os
import sys

from setuptools import setup
from setuptools.command.install import install
from setuptools import find_packages

#Change this on major/minor version number change. You must create a git tag at the same tag called with the same value
# git tag "0.1"
# git push --tags
VERSION = "0.14"


def __path(filename):
    return os.path.join(os.path.dirname(__file__),filename)

#Change this on major version number
#major_minor_version = 1.0
#This will be overriden if build.info exists
build = os.getenv('CIRCLE_BUILD_NUM',0)

if os.path.exists(__path('build.info')):
    build = open(__path('build.info')).read().strip()

version= '{0}.{1}'.format(str(VERSION),str(build))




def readme():
    """print long description"""
    with open('README.rst') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

setup(
    name="forumsentry",
    version=version,
    description="Forum Sentry sdk for Python",
    long_description=readme(),
    url="https://github.com/awalker125/forumsentry-sdk-for-python",
    author="awalker125",
    author_email="awalker125@users.noreply.github.com",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7"
    ],
    keywords='forumsentry automation api sdk',
    packages=['forumsentry', 'forumsentry_api', 'forumsentry_api.models' ],
    install_requires=['futures','requests','urllib3'],
    python_requires='>=2.7',
    include_package_data=True,
    zip_safe=False,
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
