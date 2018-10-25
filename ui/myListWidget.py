# -*- coding: utf-8 -*-
"""
---------------------------------
 Author: Mikoy
---------------------------------
 Github: github.com/MikoyChinese
---------------------------------
 Description: Date[2018-10-22], Re-write the class of QListWidget to achieve the target that RightClicked Meau.
---------------------------------
"""

from PyQt5.QtWidgets import QListWidget, QMenu, QAction
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt, QSize


class MyListWidget(QListWidget):
    def __init__(self, parent=None):
        super(MyListWidget, self).__init__(parent)
        self.setViewMode(QListWidget.IconMode)
        self.setSpacing(10)
        self.setMovement(QListWidget.Static)
        self.setResizeMode(QListWidget.Adjust)
        self.setSelectionMode(QListWidget.ExtendedSelection)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setSelectionRectVisible(True)
        self.ok = False
        self.ctrlPressed = False
        self.zoomSizes = [60, 80, 100, 120, 240, 360]
        self.zoomNum = 3
        self.zoomAdjust(self.zoomNum)

    def rightMenuShow(self):
        if self.ok:
            rightMenu = QMenu(self)
            moveAction = QAction(u'移动', triggered=self.action_1)
            removeAction = QAction('Delete', triggered=self.action_2)
            # Add action to rightMenu and show at the point(x, y), your mouse clicked.
            rightMenu.addAction(moveAction)
            rightMenu.addAction(removeAction)
            # QCursor.pos() return the global window's coordinate.
            if (self.itemAt(self.mapFromGlobal(QCursor.pos())) != None):
                rightMenu.exec_(QCursor.pos())

    def setAction(self, action_1, action_2):
        self.action_1 = action_1
        self.action_2 = action_2
        self.ok = True


    """
    Re-writed the wheelEvent to large or limited the size of item while pressing the [Ctrl] key.
    """

    def wheelEvent(self, event):
        if self.ctrlPressed:
            #
            delta = event.angleDelta()
            oriention = delta.y()/8
            if oriention > 0:
                self.zoomNum += 1
                if self.zoomNum > len(self.zoomSizes) - 1:
                    self.zoomNum = len(self.zoomSizes) - 1
            else:
                self.zoomNum -= 1
                if self.zoomNum < 0:
                    self.zoomNum = 0
            # Adjust the size of the widget.
            self.zoomAdjust(self.zoomNum)
        else:
            return super().wheelEvent(event)

    def keyReleaseEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Control:
            self.ctrlPressed = False
        return super().keyReleaseEvent(QKeyEvent)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Control:
            self.ctrlPressed = True
        return super().keyPressEvent(QKeyEvent)

    def zoomAdjust(self, zoomNum=2):
        icon_size = QSize(self.zoomSizes[zoomNum] - 20, self.zoomSizes[zoomNum] - 20)
        grid_size = QSize(self.zoomSizes[zoomNum], self.zoomSizes[zoomNum])
        self.setIconSize(icon_size)
        self.setGridSize(grid_size)
        self.update()


