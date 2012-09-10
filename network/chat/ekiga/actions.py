#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2009  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.in", "gconftool-2 --shutdown", "")
    autotools.configure("--disable-schemas-install \
                         --disable-dependency-tracking \
                         --disable-maintainer-mode \
                         --disable-scrollkeeper \
                         --disable-eds \
                         --disable-gdu \
                         --enable-gstreamer \
                         --enable-avahi \
                         --enable-xv\
                         --enable-dbus \
                         --enable-dbus_service \
                         --enable-fast-install \
                         --enable-libtool-lock \
                         --enable-static=no \
                         --sysconfdir=/etc \
                         --prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/etc/gconf/schemas", "ekiga.schemas")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "FAQ", "INSTALL", "NEWS", "README", "TODO")