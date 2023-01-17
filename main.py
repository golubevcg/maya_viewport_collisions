import moverlay as mo
from PySide2.QtCore import QPoint
from PySide2.QtCore import QSize
from PySide2.QtGui import QColor
from PySide2 import QtWidgets

import maya.cmds as cmds


qpb_state = True
enabled_color = "red"
disabled_color = "#505050"

qpb = QtWidgets.QPushButton("Test Button!")
qpb.setStyleSheet("background-color:%s" % disabled_color)

def enable_collisions():
    # get selection
    # get them as transform objects
    # get meshes under each transform
    # calculate global position of each mesh
    # pass this data to bullet engine
    # read move from controllers and feed that to bullet engine

    global qpb_state

    print('enable collisions')
    if qpb_state:
        color = enabled_color
        qpb_state = False
    else:
        color = disabled_color
        qpb_state = True

    qpb.setStyleSheet("background-color:%s" % color)

    pass

print(dir(mo.RelTo))

#Create manager and overlay definition
manager = mo.maya.overlayManager()
od = mo.overlayDef.OverlayDef(QSize(300, 100))

#Position relative to screen center and apply the style and color
od.style = mo.enums.OverlayStyle.Custom
od.attachment = mo.enums.RelTo.Center
od.bgColor = QColor(217, 217, 217, 255)

#Create this overlay
overlay = manager.createOverlay(od)

qpb.clicked.connect(enable_collisions)

#Assign body text
label = overlay.setAsWidget(qpb)

#Display the overlay bubble
manager.showAll()

# manager.deleteAll()