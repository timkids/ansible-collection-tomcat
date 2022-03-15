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

import json

# from ansible.module_utils.common.text.converters import to_text
from ansible.module_utils.basic import env_fallback
# from ansible.module_utils.urls import fetch_url, basic_auth_header


class TomcatHelper:
    """
    Manage tomcat on the module
    """

    def __init__(self, module):
        self.module = module

    @staticmethod
    def tomcat_argument_spec():
        return dict(
            url=dict(type='str', fallback=(env_fallback, ['TOMCAT_URL'])),
            username=dict(type='str', fallback=(env_fallback, ['TOMCAT_USERNAME'])),
            password=dict(type='str', no_log=True, fallback=(env_fallback, ['TOMCAT_PASSWORD'])),
            tomcat_home=dict(type='str', required=True, fallback=(env_fallback, ['TOMCAT_HOME']))
        )

    @staticmethod
    def tomcat_mutually_exclusive():
        return []

    @staticmethod
    def tomcat_required_one_of():
        return []

    @staticmethod
    def tomcat_required_together():
        return []

    def connect(self):
        pass

    def tomcat_list_apps(self):
        """
        List apps deployed on tomcat
        """
        pass
