#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc/tripwire")

def build():
    autotools.make()

def install():
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #pisitools.insinto("")
    
    pisitools.dodoc("COMM*", "ChangeLog", "COPY*", "TRADE*", "policy/*.txt")
