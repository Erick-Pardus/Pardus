#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "zsnes_1_51/src"

def setup():
    autotools.configure("--enable-debug \
			 --disable-cpucheck \
			 --enable-release \
			 --disable-static \
			 force_arch=i686")

def build():
    autotools.make()

def install():
    pisitools.dobin("zsnesd")
    pisitools.rename("/usr/bin/zsnesd", "zsnes")
    pisitools.insinto("/usr/share/pixmaps", "icons/48x48x32.png", "zsnes.png")

    pisitools.dodoc("../docs/*.txt", "../docs/README.LINUX")
