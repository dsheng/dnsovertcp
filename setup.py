#!/usr/bin/env python

from __future__ import with_statement
from setuptools import setup, find_packages
from setuptools.command.sdist import sdist
from setuptools.command.install import install as _install

import os
import subprocess
try:
    from babel.messages import frontend
except ImportError:
    frontend = None

name = "dnsovertcp"
version = "1.0.0"

class install(_install):
    def run(self):
        _install.run(self)
         
class local_sdist(sdist):
    """Customized sdist hook - builds the ChangeLog file from VC first"""
    def run(self):
        if os.path.isdir('.bzr'):
            # We're in a bzr branch

            log_cmd = subprocess.Popen(["bzr", "log", "--gnu"],
                                       stdout=subprocess.PIPE)
            changelog = log_cmd.communicate()[0]
            with open("ChangeLog", "w") as changelog_file:
                changelog_file.write(changelog)
        
        sdist.run(self)
       
        
cmdclass = {'sdist': local_sdist,'install':install}

if frontend:
    cmdclass.update({
        'compile_catalog': frontend.compile_catalog,
        'extract_messages': frontend.extract_messages,
        'init_catalog': frontend.init_catalog,
        'update_catalog': frontend.update_catalog,
    })
    

setup(
    name=name,
    version=version,
    description='dnsovertcp',
    author='DSheng',
    url='https://github.com/dsheng/dnsovertcp',
    packages=find_packages(exclude=['test', 'bin']),
    test_suite='nose.collector',
    cmdclass={'install': install},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Environment :: No Input/Output (Daemon)',
        ],
    install_requires=[], # removed for better compat
    scripts=['bin/dns-overtcp'],
    entry_points={}
     )
