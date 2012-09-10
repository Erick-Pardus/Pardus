#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DDONT_INSTALL_GCONF_SCHEMAS=1 \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBINARY_PACKAGE_BUILD=1 \
                          -DBUILD_USERMANUAL=0", sourceDir="..")
    
def build():
    shelltools.cd("build")
    cmaketools.make()
    
def install():
    shelltools.cd("build")
    cmaketools.install()
