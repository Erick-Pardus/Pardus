#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "VTK"

utils = ["vtkEncodeString", "lproj"]

examples = ["HierarchicalBoxPipeline",
            "MultiBlock",
            "Arrays",
            "Cube",
            "RGrid",
            "SGrid",
            "Medical1",
            "Medical2",
            "Medical3",
            "finance",
            "AmbientSpheres",
            "Cylinder",
            "DiffuseSpheres",
            "SpecularSpheres",
            "Cone",
            "Cone2",
            "Cone3",
            "Cone4",
            "Cone5",
            "Cone6"]

testing =  ["CommonCxxTests",
            "TestCxxFeatures",
            "TestInstantiator",
            "FilteringCxxTests",
            "GraphicsCxxTests",
            "GenericFilteringCxxTests",
            "ImagingCxxTests",
            "IOCxxTests",
            "RenderingCxxTests",
            "VTKBenchMark",
            "VolumeRenderingCxxTests",
            "WidgetsCxxTests",
            "SocketClient",
            "SocketServer",]

def setup():
    cmaketools.configure("-DBUILD_DOCUMENTATION:BOOL=OFF \
                          -DBUILD_TESTING=OFF \
                          -DBUILD_EXAMPLES=OFF \
                          -DBUILD_SHARED_LIBS=ON \
                          -DCMAKE_SKIP_RPATH=YES \
                          -DVTK_INSTALL_INCLUDE_DIR:PATH=/include/vtk \
                          -DVTK_INSTALL_LIB_DIR:PATH=/lib/vtk \
                          -DVTK_INSTALL_QT_DIR=/lib/qt4/plugins/designer \
                          -DTK_INTERNAL_PATH:PATH=/usr/include/tk-private/generic \
                          -DVTK_PYTHON_SETUP_ARGS=\"--prefix=/usr --root=%s\" \
                          -DVTK_WRAP_JAVA:BOOL=OFF \
                          -DVTK_WRAP_TCL:BOOL=OFF \
                          -DVTK_WRAP_PYTHON:BOOL=ON \
                          -DVTK_WRAP_PYTHON_SIP:BOOL=ON \
                          -DSIP_INCLUDE_DIR=/usr/include/%s \
                          -DVTK_USE_INFOVIS:BOOL=ON \
                          -DVTK_USE_VIEWS:BOOL=ON \
                          -DVTK_USE_BOOST:BOOL=ON \
                          -DVTK_USE_GL2PS=ON \
                          -DVTK_USE_GUISUPPORT:BOOL=ON \
                          -DVTK_USE_MYSQL:BOOL=ON \
                          -DVTK_USE_POSTGRES:BOOL=ON \
                          -DVTK_USE_OGGTHEORA_ENCODER=ON \
                          -DVTK_USE_PARALLEL:BOOL=ON \
                          -DVTK_USE_SYSTEM_LIBRARIES=ON \
                          -DVTK_USE_SYSTEM_LIBPROJ4=OFF \
                          -DVTK_USE_QT=ON \
                          -DVTK_USE_QVTK_QTOPENGL:BOOL=ON \
                          -DVTK_USE_QVTK=ON" % (get.installDIR(), get.curPYTHON()))

def build():
    shelltools.export("CFLAGS", "%s -D_UNICODE" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -D_UNICODE" % get.CXXFLAGS())
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("README.html")
