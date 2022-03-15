# -*- coding: utf-8 -*-
#
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


class TomcatManager:
    """
    An abstract class that represent the Tomcat manager.
    The manager can be accessed via the HTTP API or directly on the filesystem
    """

    def connect(self, path, **kwargs):
        """
        Connect to the tomcat manager
        """
        raise NotImplementedError()

    def tomcat_list_apps(self):
        """
        List apps deployed on tomcat
        """
        raise NotImplementedError()

    def server_infos(self):
        """
        Get informations about tomcat server
        """
        raise NotImplementedError()
