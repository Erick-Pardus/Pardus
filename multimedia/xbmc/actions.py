#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xbmc-11.0"
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./bootstrap")
    pisitools.dosed("configure", "-ldts" , "-ldca")
    pisitools.dosed("xbmc/utils/SystemInfo.cpp","lsb_release -d","cat /etc/pardus-release")
    autotools.rawConfigure("--disable-ccache \
                            --disable-optimizations \
                            --disable-external-python \
                            --enable-goom \
                            --enable-gl \
                            --enable-ffmpeg \
                            --disable-liba52 \
                            --disable-libdts \
                            --disable-avahi \
                            --enable-rtmp \
                            --enable-vdpau \
                            --disable-hal \
                            --prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.doman("docs/manpages/*")
    pisitools.dodoc("README.linux","*.txt","LICENSE.GPL")
