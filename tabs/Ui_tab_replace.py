# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'h:\DataSet\ht_dataset\FileRename\tabs\tab_replace.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabReplace(object):
    def setupUi(self, TabReplace):
        TabReplace.setObjectName("TabReplace")
        TabReplace.resize(897, 561)
        self.gridLayout = QtWidgets.QGridLayout(TabReplace)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_src = QtWidgets.QLineEdit(TabReplace)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_src.sizePolicy().hasHeightForWidth())
        self.lineEdit_src.setSizePolicy(sizePolicy)
        self.lineEdit_src.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_src.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_src.setText("")
        self.lineEdit_src.setObjectName("lineEdit_src")
        self.horizontalLayout.addWidget(self.lineEdit_src)
        self.label = QtWidgets.QLabel(TabReplace)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_dst = QtWidgets.QLineEdit(TabReplace)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_dst.sizePolicy().hasHeightForWidth())
        self.lineEdit_dst.setSizePolicy(sizePolicy)
        self.lineEdit_dst.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_dst.setObjectName("lineEdit_dst")
        self.horizontalLayout.addWidget(self.lineEdit_dst)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(TabReplace)
        QtCore.QMetaObject.connectSlotsByName(TabReplace)

    def retranslateUi(self, TabReplace):
        _translate = QtCore.QCoreApplication.translate
        TabReplace.setWindowTitle(_translate("TabReplace", "Form"))
        self.label.setText(_translate("TabReplace", "替换为："))

