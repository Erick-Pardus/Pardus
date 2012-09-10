#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    options = "--without-python \
	       --without-threads "

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/emul32/bin "
        shelltools.export("CC", "%s -m32" % get.CC())

    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        # prevent that binaries under /usr/bin overwrites 64-bit binaries
        pisitools.removeDir("/emul32")
        pisitools.removeDir("/usr/share/gtk-doc")
        return

    #for i in ["", "-python"]:
        #pisitools.rename("/%s/libxml2%s-%s" % (get.docDIR(), i, get.srcVERSION()), "libxml2%s" % i)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
    pisitools.removeDir("/usr/share/gtk-doc")
