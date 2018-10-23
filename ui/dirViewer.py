# -*- coding: utf-8 -*-

import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTreeWidgetItem, QFileSystemModel
from PyQt5.QtCore import QDir, pyqtSignal, QObject

# Hex of folder.gif
FOLDER_GIF = b'GIF89a\x0f\x00\r\x00\xa2\xff\x00\xff\xff\xcf\xff\xff\x90\xff\xcf\x90\xef\xef\xef\xcf\xcf`\x90\x90\x00\x00\x00\x00\xc0\xc0\xc0!\xf9\x04\x01\x00\x00\x07\x00,\x00\x00\x00\x00\x0f\x00\r\x00@\x03=xW\xcc\xa6P\x15\x10\xaa\x15\x01\x0bb\xa6\xfd\x17w\x18di\x9a\x05\xa1\xaeD\xd3,\x14Xi\xdc\xa4e\xb8\xa0\x8b\xc5\x00\xc4\x85G\x04\xf6+\x1a)\xb5\x18\xe8\x96\\\xe6\x02\xcd\xd9s\xd7aYY\x86\x04\x00;'


class FileViewer(QObject):

    signal_GetFilePath = pyqtSignal(str)

    def __init__(self, parent=None):
        super(FileViewer,self).__init__()
        self.parent = parent
        self.treeView = self.parent.treeView
        self.showRootDir()
#       self.treeView.itemDoubleClicked.connect(self.slotShowDir)

    def create_icon(self):
        icon = '../icons/folder.gif'
        if not os.path.exists('../icons/folder.gif'):
            open(icon, 'wb').write(FOLDER_GIF)

    def showRootDir(self):
        # Get the Home Dir of this OS.
        root_dir = os.path.expanduser('~')
        """
        icon = QIcon("../icons/folder.gif")
        tmp = QTreeWidgetItem()
        tmp.setText(0, root_dir)
        tmp.setIcon(0, icon)
        self.treeView.addTopLevelItem(tmp)        
        """
        self.root_model = MyQFileSystemModel()
        self.root_model.setRootPath(root_dir)
        # Filter all dirs and not show the '.', '..' items.
        self.root_model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.treeView.setModel(self.root_model)
        self.treeView.setRootIndex(self.root_model.index(root_dir))

    def getFilePath(self):
        index = self.treeView.currentIndex()
        model = index.model()
        file_path = model.filePath(index)
        self.signal_GetFilePath.emit(file_path)


    def showFileInfoList(self, list):
        self.treeView.clear()
        for i in range(len(list)):
            tmpFileInfo = list[i]
            if tmpFileInfo.isDir():
                icon = QIcon("./icons/folder.gif")
                fileName = tmpFileInfo.fileName()
                tmp = QTreeWidgetItem(self.treeView, fileName)
                tmp.setIcon(icon)
                self.treeView.addTopLevelItem(tmp)

    def slotShow(self, dir):
        list = dir.entryInfoList(QDir.AllEntries, QDir.DirsFirst)
        self.showFileInfoList(list)

    def slotShowDir(self):
        item = self.treeView.currentItem()
        str = item.text()
        while item.parent():
            yield str
            str = item.parent().text() + '/' + str
            item = item.parent()

        dir = QDir()
        dir.setPath(str)
        dir.cd(str)
        self.slotShow(dir)

class MyQFileSystemModel(QFileSystemModel):
    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return 1