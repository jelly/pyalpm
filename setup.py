# -*- coding: utf-8 -*-
import os
import subprocess
from distutils.cmd import Command
from distutils.core import Extension, setup

os.putenv('LC_CTYPE', 'en_US.UTF-8')

pyalpm_version = '0.8'

cflags = ['-Wall', '-Wextra', '-Werror',
    '-Wconversion',
    '-Wno-unused-parameter',
    '-Wno-unused-function',
    '-Wno-format',
    '-Wdeclaration-after-statement',
    '-ansi', '-D_FILE_OFFSET_BITS=64']

alpm = Extension('pyalpm',
    libraries = ['alpm'],
    extra_compile_args = cflags + ['-DVERSION="%s"' % pyalpm_version],
    language = 'C',
    sources = [
        'src/pyalpm.c',
        'src/util.c',
        'src/package.c',
        'src/db.c',
        'src/options.c',
        'src/handle.c',
        'src/transaction.c'
        ],
    depends = [
        'src/handle.h',
        'src/db.h',
        'src/options.h',
        'src/package.h',
        'src/pyalpm.h',
        'src/util.h',
        ])

class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        raise SystemExit(
            subprocess.call(['nosetests',
                             'tests']))


setup(name = 'pyalpm',
      version = pyalpm_version,
      description = 'libalpm bindings for Python 3',
      author = "Rémy Oudompheng",
      author_email = "remy@archlinux.org",
      url = "http://projects.archlinux.org/users/remy/pyalpm.git",
      packages = ["pycman"],
      scripts = ["scripts/lsoptdepends"] + ["scripts/pycman-" + i
          for i in ['database', 'deptest', 'query', 'remove', 'sync', 'upgrade', 'version']],
      ext_modules = [alpm],
      cmdclass = {
          'test': TestCommand
        })

# vim: set ts=4 sw=4 et tw=0:
