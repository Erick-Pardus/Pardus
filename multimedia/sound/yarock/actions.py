#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Yarock_%s_source" % get.srcVERSION()

def setup():
    qt4.configure(parameters="PREFIX=/usr")

def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.dodoc("CHANGES", "COPYING")
