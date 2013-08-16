"""
example_module.example
~~~~~

:copyright: (c) 2010-2013 by Luis Morales
:license: BSD, see LICENSE for more details.
"""


from forge.module import Module


class Example(Module):
    """
    installs a example package
    """

    def __init__(self, user):
        super(Example, self).__init__(user)
        self.message('installing example package')
        self.packages_install = [
            'joe',
        ]
        self.requires_root()

    def execute(self):
        self.progress('updating all packages')
        self.run('apt-get update')
        self.run('apt-get upgrade -y')

        for package in self.packages_install:
            self.progress('installing ' + package)
            self.install_package(package)

    def is_valid(self):
        return True
