"""
lminit.recipes.recipe
~~~~~

:copyright: (c) 2010-2013 by Luis Morales
:license: BSD, see LICENSE for more details.
"""

import os
import sys
import subprocess
import shlex

import apt

from cli import green, blue, cyan, red


class Module(object):
    """
    Base class for module packages
    """

    temp = '/tmp'

    def __init__(self, user):
        self.user = user
        self.home = os.path.expanduser('~' + user)
        assert os.path.exists(self.home)

        self.cache = None

    def is_valid(self):
        raise NotImplementedError()

    def requires_root(self):
        if not os.geteuid() == 0:
            sys.exit(red("You need root to run this module"))

    def banner(self):
        """text progress separator"""
        print cyan('****************************************************************')

    def message(self, string):
        print blue('- ' + string)

    def progress(self, string):
        print green('\t* ' + string)

    def run(self, command, as_root=True):
        fnull = open(os.devnull, 'w')
        parts = shlex.split(command)
        args = parts if as_root else ['sudo', '-u', self.user] + parts
        result = subprocess.call(args, stdout=fnull, stderr=fnull)
        fnull.close()
        return result

    def is_success(self, command, as_root=True):
        return self.run(command, as_root) == 0

    def __init_apt_cache(self):
        """
        Initialize the apt cache class
        """
        if not self.cache:
            self.cache = apt.Cache()
            self.apt_update()

    def apt_update(self):
        """
        updates apt cache
        """
        self.cache.update()
        self.cache.open(None)

    def upgrade(self):
        """
        upgrades system packages after performing apt-get update
        """
        self.__init_apt_cache()
        self.apt_update()
        self.cache.upgrade()

    def install_package(self, package):
        """
        install a package via apt-get install
        """

        self.__init_apt_cache()
        self.cache[package].mark_install()
        self.cache.commit()

    def remove_package(self, package):
        """
        removes a package via apt-get remove
        """

        self.__init_apt_cache()
        self.cache[package].mark_delete()
        self.cache.commit()

    def add_apt_repo(self, ppa):
        """
        softwareproperties.SoftwareProperties seems to only be installed in the python3 packages so we use self.run
        adds a ppa repo via add-apt-repository
        """
        self.run('add-apt-repository -y ' + ppa)
        self.apt_update()

    def replace_text(self, filename, old, new, as_root=True):
        command = 'sed -i "s/%s/%s/" %s' % (old, new, filename)
        self.run(command, as_root)

    def append_text(self, filename, text=''):
        with open(filename, "a") as _file:
            _file.write(text + '\n')

    def wget(self, url, as_root=True):
        command = "wget -q --no-check-certificate " + url
        return self.run(command, as_root)

    def is_ok(self, string):
        result = raw_input(string + '? [y/n]\n').strip().lower()
        if result == 'y':
            return True
        if result == 'n':
            return False
        return self.is_ok(string)

    def execute(self):
        """
        Default module method
        """
        raise NotImplementedError()

    def __repr__(self):
        return '%s: user=%r, home=%r' % (self.__class__.__name__, self.user, self.home)
