#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("prefix=/usr \
                         --includedir=/usr/include/gdbm \
                         --with-gdbm183-includedir=/usr/include/gdbm \
                         --with-gdbm183-libdir=/usr/lib \
                         --enable-libgdbm-compat")

def build():
    autotools.make("-j1")

def install():
    #autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    autotools.rawInstall("INSTALL_ROOT=%s includedir=/usr/include/gdbm" % get.installDIR())

    pisitools.dodoc("ChangeLog", "NEWS", "README")
