# -*- coding: utf-8 -*-
"""
---------------------------------
 Author: Mikoy
---------------------------------
 Github: github.com/MikoyChinese
---------------------------------
 Description: Date[2018-10-24], Re-write the class of QListView.
---------------------------------
"""

from PyQt5.QtWidgets import QListView, QFileDialog
from PyQt5.QtCore import QStringListModel, pyqtSignal


class MyListView(QListView):

    signal_selectedPath = pyqtSignal(str)
    def __init__(self, parent=None):
        super(MyListView, self).__init__(parent)
        self.setWordWrap(True)
        self.setEditTriggers(QListView.NoEditTriggers)

    def setList(self, lst=list):
        self.lst = lst

    def open_FileDialog(self):
        path = QFileDialog.getExistingDirectory(self, u"请选择需要添加的路径：", '/')
        if path != '':
            self.addListPath(path)

    def addListPath(self, path):
        if path != '':
            self.lst.append(path)
            lst = self.lst.copy()
            lst.reverse()
            slm = QStringListModel()
            slm.setStringList(lst)
            self.setModel(slm)

    def getSelectedPath(self):
        if self.selectedIndexes():
            index = self.currentIndex()
            model = index.model()
            text = model.data(index, 0)
            self.signal_selectedPath.emit(text)

    def moveToUp(self, selectedPath):
        if self.lst[-1] != selectedPath and selectedPath != '':
                self.lst.remove(selectedPath)
                self.addListPath(selectedPath)




