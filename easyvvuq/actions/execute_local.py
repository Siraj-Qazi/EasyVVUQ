"""Provides element to execute a shell command in a given directory.
"""

import os
import sys
from . import BaseAction

__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"


class ExecuteLocal(BaseAction):

    def __init__(self, run_cmd):
        """
        Provides an action element to run a shell command in a specified
        directory.

        Parameters
        ----------

        run_cmd : str
            Command to execute.

        """

        # Need to expand users, get absolute path and dereference symlinks
        self.run_cmd = os.path.realpath(os.path.expanduser(run_cmd))

    def act_on_dir(self, target_dir):
        """
        Executes `self.run_cmd` in the shell in `target_dir`.

        target_dir : str
            Directory in which to execute command.

        """

        full_cmd = f'cd {target_dir}\n{self.run_cmd}\n'
        result = os.system(full_cmd)
        if result != 0:
            sys.exit(f'Non-zero exit code from command "{full_cmd}"\n')
