#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    CFLAGS = get.CFLAGS()
    shelltools.export("CFLAGS",CFLAGS.replace(" -fstack-protector",""))
    autotools.configure("--disable-werror \
			 --with-grubdir=grub2 \
			 --program-transform-name='s,grub,grub2,'\
			 --program-prefix= \
			 --htmldir='/usr/share/doc/${PF}/html' ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "BUGS", "ChangeLog", "COPYING", "TODO", "README")
