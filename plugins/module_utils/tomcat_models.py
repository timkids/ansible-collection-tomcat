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

import enum


class TomcatError(Exception):
    """
    Base class for all errors raised on tomcat modules.

    .. versionadded:: 1.0.0
    """
    pass


class TomcatConnectionError(TomcatError):
    """
    Error when connecting to tomcat API.

    .. versionadded:: 1.0.0
    """
    pass


class TomcatBadArguments(TomcatError):
    """
    Bad arguments used with the modules.

    .. versionadded:: 1.0.0
    """
    pass


@enum.unique
class TomcatStatusCode(enum.Enum):
    """
    Return code of an operation on tomcat.

    This enum is used when the module use the API or the direct access to interact with
    Tomcat.

    .. versionadded:: 1.0.0
    """
    OK = "OK"
    FAIL = "FAIL"
    NOTFOUND = "NOTFOUND"


@enum.unique
class TomcatApplicationState(enum.Enum):
    """
    Possible application state on a tomcat container.

    .. versionadded:: 1.0.0
    """
    RUNNING = "running"
    STOPPED = "stopped"
