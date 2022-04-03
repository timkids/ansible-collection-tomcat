# -*- coding: utf-8 -*-
#
# This file is part of Ansible
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest
from unittest import TestCase
from unittest.mock import MagicMock, patch

from ansible_collections.timkids.tomcat.plugins.module_utils.tomcat_manager_fs import TomcatManagerFS
from ansible_collections.timkids.tomcat.plugins.module_utils.tomcat_models import TomcatConnectionError

class TomcatManagerFsTestSuite(TestCase):

    def setUp(self):
        super(TomcatManagerFsTestSuite, self).setUp()

        self.module = MagicMock()


    def tearDown(self):
        """Teardown."""
        super(TomcatManagerFsTestSuite, self).tearDown()


    def test_fs_connection_absent_directory(self):
        tomcatManager = TomcatManagerFS(self.module)

        with pytest.raises(TomcatConnectionError):
            tomcatManager.connect("fake_path")

    @patch('os.path.isdir')
    def test_fs_connection_not_abs_directory(self, mock_is_dir):
        mock_is_dir.return_value = True
        tomcatManager = TomcatManagerFS(self.module)

        with pytest.raises(TomcatConnectionError):
            tomcatManager.connect("fake_path")
