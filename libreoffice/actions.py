#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./autogen.sh --with-jdk-home=/opt/sun-jdk \
				    --with-system-libs \
				    --with-lang='' \
				    --with-system-headers \
				    --with-system-mozilla \
				    --with-system-zlib \
				    --without-system-nss \
				    --with-system-mdds \
				    --with-system-orcus \
				    --with-system-libcmis \
				    --with-system-libcdr \
				    --with-system-cppunit \
				    --with-system-graphite \
				    --with-system-libwpg \
				    --with-system-libwps \
				    --with-system-ucpp \				    
				    --with-system-liblangtag \
				    --with-system-redland\
				    --without-system-clucene \
				    --without-system-libmspub \
				    --without-system-altlinuxhyph \
				    --without-system-jars \
				    --without-system-hsqldb \
				    --disable-mathmldtd \
				    --disable-epm \
				    --disable-gnome-vfs \
				    --enable-gio \
				    --enable-symbols \
				    --enable-dbus \
				    --enable-opengl \
				    --enable-vba \
				    --disable-gtk \
				    --enable-ext-presenter-minimizer \
				    --enable-ext-nlpsolver \
				    --enable-ext-wiki-publisher \
				    --with-servlet-api-jar=/usr/share/java/servlet-api.jar \
				    --with-system-mythes \
				    --with-system-dicts \
				    --with-external-dict-dir=/usr/share/myspell \
				    --without-myspell-dicts \
				    --without-fonts \
				    --without-ppds \
				    --without-afms \
				    --disable-gstreamer \
				    --with-vendor='Pardus' \
				    --enable-fetch-external ")

    #--without-system-hsqldb \ libreoffice hsqldb 1.8.0 üzerini desteklemiyor.

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "README")

