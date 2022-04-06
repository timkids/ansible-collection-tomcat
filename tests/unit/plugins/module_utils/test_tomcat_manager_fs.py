# -*- coding: utf-8 -*-
#
# This file is part of Ansible
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest
from unittest import TestCase
from unittest.mock import MagicMock, patch

from ansible.module_utils import basic

from ansible_collections.timkids.tomcat.plugins.module_utils.tomcat_manager_fs import TomcatManagerFS
from ansible_collections.timkids.tomcat.plugins.module_utils.tomcat_models import TomcatConnectionError, TomcatBadArguments
from ansible_collections.timkids.tomcat.tests.unit.plugins.module_utils.models import TOMCAT_VERSION_SH_OUTPUT

class AnsibleExitJson(Exception):
    """Exception class to be raised by module.exit_json and caught by the test case"""
    pass


class AnsibleFailJson(Exception):
    """Exception class to be raised by module.fail_json and caught by the test case"""
    pass


class TomcatManagerFsTestSuite(TestCase):

    def setUp(self):
        super(TomcatManagerFsTestSuite, self).setUp()

        self.module = MagicMock()

    def tearDown(self):
        """Teardown."""
        super(TomcatManagerFsTestSuite, self).tearDown()

    def test_fs_connection_bad_args(self):
        tomcatManager = TomcatManagerFS(self.module)

        with pytest.raises(TomcatBadArguments):
            tomcatManager.connect()

    def test_fs_connection_absent_directory(self):
        tomcatManager = TomcatManagerFS(self.module)

        with pytest.raises(TomcatConnectionError):
            tomcatManager.connect(tomcat_home="fake_path")

    @patch('os.path.isdir')
    def test_fs_connection_not_abs_directory(self, mock_is_dir):
        mock_is_dir.return_value = True
        tomcatManager = TomcatManagerFS(self.module)

        with pytest.raises(TomcatConnectionError):
            tomcatManager.connect(tomcat_home="fake_path")

    @patch('os.path.isdir')
    @patch('os.path.isabs')
    def test_fs_connection_not_tomcat_dir(self, mock_is_dir, mock_is_abs):
        mock_is_dir.return_value = True
        mock_is_abs.return_value = True
        tomcatManager = TomcatManagerFS(self.module)

        with pytest.raises(TomcatConnectionError):
            tomcatManager.connect(tomcat_home="fake_path")

    @patch('os.path.isdir')
    @patch('os.path.isabs')
    @patch('os.path.isfile')
    def test_fs_connection_bad_tomcat_dir_access(self, mock_is_dir, mock_is_abs, mock_is_file):
        mock_is_dir.return_value = True
        mock_is_abs.return_value = True
        mock_is_file.return_value = True
        tomcatManager = TomcatManagerFS(self.module)

        with pytest.raises(TomcatConnectionError):
            tomcatManager.connect(tomcat_home="fake_path")

    @patch('ansible_collections.timkids.tomcat.plugins.module_utils.tomcat_manager_fs.TomcatManagerFS._is_tomcat_dir')
    @patch('os.path.isabs')
    @patch('os.path.isdir')
    @patch('os.path.isfile')
    def test_fs_connection_valid_tomcat_dir(self, mock_access, mock_is_abs, mock_is_dir, mock_is_file):
        mock_is_dir.return_value = True
        mock_is_abs.return_value = True
        mock_is_file.return_value = True
        mock_access.return_value = True
        tomcatManager = TomcatManagerFS(self.module)

        res = tomcatManager.connect(tomcat_home="fake_path")

        self.assertTrue(res)

    @patch('ansible_collections.timkids.tomcat.plugins.module_utils.tomcat_manager_fs.TomcatManagerFS._is_tomcat_dir')
    @patch('os.path.isabs')
    @patch('os.path.isdir')
    @patch('os.path.isfile')
    def test_fs_tomcat_version(self, mock_access, mock_is_abs, mock_is_dir, mock_is_file):
        mock_is_dir.return_value = True
        mock_is_abs.return_value = True
        mock_is_file.return_value = True
        mock_access.return_value = True

        amodule = MagicMock()
        run_command = MagicMock()
        run_command.return_value = (0, TOMCAT_VERSION_SH_OUTPUT, '')
        amodule.run_command = run_command

        tomcatManager = TomcatManagerFS(amodule)

        res = tomcatManager.connect(tomcat_home="fake_path")


        server_infos = tomcatManager.server_infos()

        self.assertEqual(server_infos, '10.0.17.0')

        # Check that run_command has been called
        run_command.assert_called_once_with(['fake_path/bin/version.sh'])
        self.assertEqual(run_command.call_count, 1)
