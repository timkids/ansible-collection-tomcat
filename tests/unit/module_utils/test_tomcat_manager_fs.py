# -*- coding: utf-8 -*-
#
# This file is part of Ansible
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest

from ansible_collections.amazon.aws.tests.unit.compat.mock import MagicMock
from ansible_collections.timkids.tomcat.tests.unit.compat import unittest

from ansible_collections.timkids.tomcat.plugins.module_utils.tomcat_manager_fs import TomcatManagerFS


class TomcatManagerFsTestSuite(unittest.TestCase):

    def setUp(self):
        self.module = MagicMock()
        pass

    def test_server_infos_success(self):
        pass
