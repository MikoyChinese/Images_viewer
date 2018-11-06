# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import sys, os, shutil
from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication, QDir, QPoint, QFile
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.dirViewer import FileViewer
from ui.myListWidget import MyListWidget
from ui.myListView import MyListView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 800))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QSize(1280, 783))
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtWidgets.QTreeView(self.centralWidget)
        self.treeView.setObjectName("treeView")

        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 1)

        '''
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)
        '''

        self.listView_HLayout = QtWidgets.QHBoxLayout()
        self.listView_HLayout.setContentsMargins(11, 11, 11, 11)
        self.listView_HLayout.setSpacing(6)
        self.listView_HLayout.setObjectName("listView_HLayout")
        self.lstView_addButton = QtWidgets.QPushButton(self.centralWidget)
        self.lstView_addButton.setObjectName("lstView_addButton")
        self.lstView_selectedButton = QtWidgets.QPushButton(self.centralWidget)
        self.lstView_selectedButton.setObjectName("lstView_selectedButton")
        self.listView_HLayout.addWidget(self.lstView_selectedButton)
        self.listView_HLayout.addWidget(self.lstView_addButton)
        self.gridLayout.addLayout(self.listView_HLayout, 2, 2, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_0 = QtWidgets.QLabel(self.centralWidget)
        self.label_0.setObjectName("label_0")

        self.horizontalLayout.addWidget(self.label_0)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.listWidget = MyListWidget(parent=self.centralWidget)
        self.listWidget.setObjectName("listWidget")

        self.gridLayout.addWidget(self.listWidget, 1, 1, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = MyListView(self.centralWidget)
        self.listView.setObjectName("listView")

        self.verticalLayout.addWidget(self.listView)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.listWidget.setAction(self.moveItem, self.removeItem)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Images_viewer", "Images_viewer"))
        self.lstView_addButton.setText(u'添加目录')
        self.lstView_selectedButton.setText(u"选择此目录")
        self.label_0.setText("Nothing.")

        # move_to_lst which will save all the path pics will be saved in.
        self.move_to_lst = []
        # Initial the listView's list.
        self.listView.setList(self.move_to_lst)

        # Button <Signal>:
        self.lstView_addButton.clicked.connect(self.listView.open_FileDialog)
        self.lstView_selectedButton.clicked.connect(self.listView.getSelectedPath)
        self.listView.signal_selectedPath.connect(self.listView.moveToUp)
        # Add a fiction that move the selected item up to top which was doubleclicked.
        self.listView.doubleClicked.connect(self.listView.getSelectedPath)

    def createPicListWidget(self, msg):
        self.current_root = msg
        # Clear the old pics list. Restore to show images
        self.listWidget.clear()
        # Get the currentItem of treeview.
        files_dir = QDir(msg)
        # Create the fillter to select what pics nessary.
        files_dir.setFilter(QDir.Files | QDir.NoSymLinks)
        # Sort by Name.
        files_dir.setSorting(QDir.Name)
        files_dir.setNameFilters(['*.png', '*.jpg', '*.jpeg', '*.bmp'])
        pics_list = files_dir.entryList()

        # Show each pic to listWidgetItem.
        for pic in pics_list:
            pic_icon = QIcon(files_dir.absolutePath() + '/' + pic)
            # Define the item of QListWiget.
            pic_item = QtWidgets.QListWidgetItem()
            pic_item.setIcon(pic_icon)
            pic_item.setText(pic)
            pic_item.setToolTip(pic)

            # pic_item.setSizeHint(QSize(120, 120))
            self.listWidget.addItem(pic_item)

    def moveItem(self):
        lst = self.listView.lst
        if lst:
            path = lst[-1]
            if not os.path.exists(path):
                QtWidgets.QMessageBox.warning(self.listWidget, 'Warning:', '目录: [%s] 不存在, 请核查!' % path,
                                              QtWidgets.QMessageBox.Yes)
                return
            items = self.listWidget.selectedItems()
            if (len(items)  == 0):
                return
            else:
                for item in items:
                    file_name = self.current_root + '/' + item.text()
                    dst_file_name = path + '/' + item.text()
                    shutil.move(file_name, dst_file_name)
                self.createPicListWidget(self.current_root)

    def removeItem(self):
        items = self.listWidget.selectedItems()
        if (len(items) == 0):
            return
        else:
            reply = QtWidgets.QMessageBox.question(self.listWidget, 'Information:', '确认删除吗？',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                for item in items:
                    file_name = self.current_root + '/' + item.text()
                    file = QFile(file_name)
                    file.remove()
                self.createPicListWidget(self.current_root)
            else:
                pass



def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    file_viewer = FileViewer(parent=ui)
    file_viewer.signal_GetFilePath.connect(ui.createPicListWidget)
    ui.treeView.doubleClicked.connect(file_viewer.getFilePath)

    ui.listWidget.customContextMenuRequested[QPoint].connect(ui.listWidget.rightMenuShow)

    mainWindow.show()
    sys.exit(app.exec_())
