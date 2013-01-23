#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import glob

shelltools.export("HOME", get.workDIR())

AppDir = "/opt/LibreOffice"
NoStrip = ["%s/lib/libreoffice/basis-link/share" % AppDir, "%s/lib/libreoffice/share" % AppDir]

def getJobCount():
    # If jobs field in pisi.conf is greater than 1, use 'this value - 1' as number of cpus. There is also a max-jobs configure opt. but it's buggy now
    return max(int(get.makeJOBS().strip().replace("-j", "")) - 1, 8)

def setup():  
        # Remove previous Linux build scripts if any
    for f in glob.glob("Linux*Set.sh"):
        shelltools.unlink(f)

    autotools.autoconf("-f")
    
    shelltools.system("./autogen.sh --with-system-libs \
				    --with-lang='' \
				    --with-system-headers \
				    --with-system-mozilla \
				    --with-system-zlib \
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
				    --with-x \
				    --with-system-redland \
				    --with-system-libmspub \
				    --without-system-dicts \
				    --without-system-nss \
				    --without-afms \
				    --without-fonts \
				    --without-myspell-dicts \
				    --without-system-clucene \
				    --without-system-altlinuxhyph \
				    --without-system-jars \
				    --without-system-hsqldb \
				    --with-servlet-api-jar=/usr/share/java/servlet-api.jar \
				    --with-jdk-home=/opt/sun-jdk \
				    --with-external-dict-dir=/usr/share/myspell ")

    #--without-system-hsqldb \ libreoffice hsqldb 1.8.0 üzerini desteklemiyor.

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "README")

