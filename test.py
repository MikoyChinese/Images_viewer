# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class FileViewer(QMainWindow):
    def __init__(self, parent=None):
        super(FileViewer, self).__init__(parent)
        self.setWindowTitle(self.tr("文件浏览器"))

        mainWidget = QWidget()
        mainLayout = QGridLayout()
        self.LineEditDir = QLineEdit(self)
        self.ListWidgetFile = QListWidget(self)
        mainLayout.addWidget(self.LineEditDir, 0, 0)
        mainLayout.addWidget(self.ListWidgetFile, 1, 0)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
        self.setMouseTracking(True)
        self.ListWidgetFile.itemDoubleClicked.connect(self.slotShowDir)

    def showFileInfoList(self, list):
        self.ListWidgetFile.clear()
        for i in range(len(list)):
            tmpFileInfo = list[i]
            if tmpFileInfo.isDir():
                icon = QIcon("./icons/folder.gif")
                fileName = tmpFileInfo.fileName()
                tmp = QListWidgetItem(icon, fileName)
                self.ListWidgetFile.addItem(tmp)

    def slotShow(self, dir1):
        list = dir1.entryInfoList(QDir.AllEntries, QDir.DirsFirst)
        self.showFileInfoList(list)

    def slotShowDir(self):
        item = self.ListWidgetFile.currentItem()
        str = item.text()
        dir = QDir()
        dir.setPath(self.LineEditDir.text())
        dir.cd(str)
        self.LineEditDir.setText(dir.absolutePath())
        self.slotShow(dir)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            dir = QDir()
            dir.setPath(self.LineEditDir.text())
            self.LineEditDir.setText(dir.absolutePath())
            self.slotShow(dir)


app = QApplication(sys.argv)
dialog = FileViewer()
dialog.show()
app.exec_()
