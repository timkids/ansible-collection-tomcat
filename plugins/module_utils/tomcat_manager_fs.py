# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Timkids
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from os import path, access, R_OK

from ansible_collections.timkids.tomcat.plugins.module_utils.tomcat_manager import TomcatManager
from ansible_collections.timkids.tomcat.plugins.module_utils.tomcat_models import TomcatConnectionError


class TomcatManagerFS(TomcatManager):
    """
    An abstract class that represent the Tomcat manager.
    The manager can be accessed via the HTTP API or directly on the filesystem
    """

    def __init__(self, module):
        TomcatManager.__init__(self)
        self.__path = None
        self.__module = module

    def _parse_version_sh_output(self, version_out):
        pass

    def connect(self, path, **kwargs):
        """
        Connect to the tomcat manager
        """

        # Check that the path is accessible
        if not path.isabs(path) and not path.isdir(path):
            raise TomcatConnectionError("Path {1} is not a tomcat_home directory.".format(path))

        # Check if the path is a true tomcat_home
        tomcat_files_to_check = [
            "bin/catalina.sh",
            "lib/catalina.jar",
        ]

        check_result = False
        for file_to_check in tomcat_files_to_check:
            full_path_file = path.join(path, file_to_check)
            check_result &= (path.isfile(full_path_file) and access(full_path_file, R_OK))

        if not check_result:
            raise TomcatConnectionError("Path {1} is not a tomcat_home directory.".format(path))

        self.__path = path

    def tomcat_list_apps(self):
        """
        List apps deployed on tomcat
        """
        pass

    def server_infos(self):
        """
        Get informations about tomcat server
        """
        # Use the version.sh script
        tomcat_bin_dir = path.join(self.__path, "bin")
        tomcat_version_shell = path.join(tomcat_bin_dir, "version.sh")

        rc, version_out, err = self.__module.run_command(["%s" % tomcat_version_shell])

        if rc != 0:
            self.__module.fail_json(msg="Failed to run version.sh", rc=rc, err=err)

        if version_out:
            self.__module.log(version_out)
            # device_state = lsdev_out.split()[1]
            # return True, device_state

            """
Using CATALINA_BASE:   /usr/local/tomcat
Using CATALINA_HOME:   /usr/local/tomcat
Using CATALINA_TMPDIR: /usr/local/tomcat/temp
Using JRE_HOME:        /usr/local/openjdk-11
Using CLASSPATH:       /usr/local/tomcat/bin/bootstrap.jar:/usr/local/tomcat/bin/tomcat-juli.jar
Using CATALINA_OPTS:
NOTE: Picked up JDK_JAVA_OPTIONS:  --add-opens=java.base/java.lang=ALL-UNNAMED
--add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED
--add-opens=java.base/java.util.concurrent=ALL-UNNAMED --add-opens=java.rmi/sun.rmi.transport=ALL-UNNAMED
Server version: Apache Tomcat/10.0.17
Server built:   Feb 21 2022 19:36:49 UTC
Server number:  10.0.17.0
OS Name:        Linux
OS Version:     5.10.0-10-amd64
Architecture:   amd64
JVM Version:    11.0.14.1+1
JVM Vendor:     Oracle Corporation
            """
