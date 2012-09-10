#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules

def setup():
    pythonmodules.run("setup.py clean")

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
