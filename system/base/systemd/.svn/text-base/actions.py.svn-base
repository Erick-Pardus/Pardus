#!/usr/bin/python
# -*- coding: utf-8 -*-
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.configure("--with-rootprefix= \
                         --libexecdir=/lib \
                         --localstatedir=/var \
                         --sysconfdir=/etc \
                         --with-pamlibdir=/lib/security \
                         --with-distro=pardus \
                         --with-usb-ids-path=/usr/share/misc/usb.ids \
                         --with-pci-ids-path=/usr/share/misc/pci.ids \
                         --with-firmware-path=/lib/firmware:/lib/firmware/updates \
                         --enable-split-usr \
                         --disable-static \
                         --disable-selinux")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #sysvinit compability
    for binary in ["reboot","halt","poweroff","shutdown","telinit","runlevel"]:
        pisitools.dosym("../bin/systemctl","/sbin/%s" % binary)
    pisitools.dosym("../lib/systemd/systemd","/bin/systemd")
    pisitools.dosym("../bin/systemd","/sbin/init")
    pisitools.dosym("loginctl","/bin/systemd-loginctl")

    #udev
    pisitools.dosym("../lib/udev/scsi_id", "/sbin/scsi_id")
    pisitools.dosym("../lib/systemd/systemd-udevd", "/sbin/udevd")
    pisitools.dosym("../../lib/systemd/systemd-udevd", "/lib/udev/udevd")
    pisitools.dosym("./systemd-udevd.8", "/usr/share/man/man8/udevd.8")
    pisitools.dosym("../usr/bin/udevadm", "/sbin/udevadm")
    
    pisitools.dodir("/lib/firmware/updates")
    pisitools.dodir("/etc/udev/agents.d/usb")
    shelltools.touch("%s/etc/scsi_id.config" % get.installDIR())
    
    for runlevel in range(2,6):
        shelltools.touch("%s/etc/systemd/system/runlevel%s.target" % (get.installDIR(),runlevel))

    for DIR in ["basic", "default", "dbus", "syslog"]:
        pisitools.dodir("/lib/systemd/system/%s.target.wants" % DIR)

    for DIR in ["system", "user"]:
        pisitools.dodir("/lib/systemd/%s-generators" % DIR)

    for DIR in ["net","hugepages","pts","shm"]:
        pisitools.dodir("/lib/udev/devices/%s" % DIR)


    for DIR in ("tmpfiles.d", "sysctl.d", "binfmt.d", "modules-load.d"):
        pisitools.dodir("/etc/%s" % DIR)

    pisitools.dodoc("LICENSE*", "README*", "NEWS", "TODO")
