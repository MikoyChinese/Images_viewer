# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication, QDir, QPoint, QFile
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.dirViewer import FileViewer
from ui.myListWidget import MyListWidget


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
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.listWidget = MyListWidget(parent=self.centralWidget)
        self.listWidget.setObjectName("listWidget")

        self.gridLayout.addWidget(self.listWidget, 1, 1, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.listWidget.setAction(self.moveItem, self.removeItem)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

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
        pass

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
                    print('Remove File: %s' %file_name)
                self.createPicListWidget(self.current_root)
            else:
                pass


if __name__ == '__main__':
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
