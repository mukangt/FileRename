# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'h:\DataSet\ht_dataset\FileRename\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1523, 971)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_fileCnt = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_fileCnt.sizePolicy().hasHeightForWidth())
        self.label_fileCnt.setSizePolicy(sizePolicy)
        self.label_fileCnt.setTextFormat(QtCore.Qt.PlainText)
        self.label_fileCnt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileCnt.setWordWrap(False)
        self.label_fileCnt.setObjectName("label_fileCnt")
        self.verticalLayout_4.addWidget(self.label_fileCnt)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_addFiles = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addFiles.sizePolicy().hasHeightForWidth())
        self.pushButton_addFiles.setSizePolicy(sizePolicy)
        self.pushButton_addFiles.setFlat(False)
        self.pushButton_addFiles.setObjectName("pushButton_addFiles")
        self.horizontalLayout_2.addWidget(self.pushButton_addFiles)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.frame)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_startRename = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_startRename.sizePolicy().hasHeightForWidth())
        self.pushButton_startRename.setSizePolicy(sizePolicy)
        self.pushButton_startRename.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_startRename.setObjectName("pushButton_startRename")
        self.horizontalLayout_3.addWidget(self.pushButton_startRename)
        self.pushButton_preview = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_preview.sizePolicy().hasHeightForWidth())
        self.pushButton_preview.setSizePolicy(sizePolicy)
        self.pushButton_preview.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_preview.setObjectName("pushButton_preview")
        self.horizontalLayout_3.addWidget(self.pushButton_preview)
        self.pushButton_clearFiles = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clearFiles.sizePolicy().hasHeightForWidth())
        self.pushButton_clearFiles.setSizePolicy(sizePolicy)
        self.pushButton_clearFiles.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_clearFiles.setObjectName("pushButton_clearFiles")
        self.horizontalLayout_3.addWidget(self.pushButton_clearFiles)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_src = QtWidgets.QLabel(self.centralwidget)
        self.label_src.setObjectName("label_src")
        self.verticalLayout.addWidget(self.label_src)
        self.listWidget_src = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_src.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_src.setObjectName("listWidget_src")
        self.verticalLayout.addWidget(self.listWidget_src)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalScrollBar_sync = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar_sync.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_sync.setObjectName("verticalScrollBar_sync")
        self.horizontalLayout.addWidget(self.verticalScrollBar_sync)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_dst = QtWidgets.QLabel(self.centralwidget)
        self.label_dst.setObjectName("label_dst")
        self.verticalLayout_2.addWidget(self.label_dst)
        self.listWidget_dst = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_dst.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_dst.setObjectName("listWidget_dst")
        self.verticalLayout_2.addWidget(self.listWidget_dst)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_fileCnt.setText(_translate("MainWindow", "当前需要处理的文件数为：0个"))
        self.pushButton_addFiles.setText(_translate("MainWindow", "点击添加文件"))
        self.pushButton_startRename.setText(_translate("MainWindow", "开始批量重命名"))
        self.pushButton_preview.setText(_translate("MainWindow", "预览"))
        self.pushButton_clearFiles.setText(_translate("MainWindow", "清空添加文件"))
        self.label_src.setText(_translate("MainWindow", "原文件名："))
        self.label_dst.setText(_translate("MainWindow", "修改后的文件名："))

