# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'h:\DataSet\ht_dataset\FileRename\tabs\tab_config.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabConfig(object):
    def setupUi(self, TabConfig):
        TabConfig.setObjectName("TabConfig")
        TabConfig.resize(878, 714)
        self.gridLayout = QtWidgets.QGridLayout(TabConfig)
        self.gridLayout.setObjectName("gridLayout")
        self.label_previewNum = QtWidgets.QLabel(TabConfig)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_previewNum.setFont(font)
        self.label_previewNum.setObjectName("label_previewNum")
        self.gridLayout.addWidget(self.label_previewNum, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_topN = QtWidgets.QRadioButton(TabConfig)
        self.radioButton_topN.setChecked(True)
        self.radioButton_topN.setObjectName("radioButton_topN")
        self.horizontalLayout.addWidget(self.radioButton_topN)
        self.radioButton_all = QtWidgets.QRadioButton(TabConfig)
        self.radioButton_all.setObjectName("radioButton_all")
        self.horizontalLayout.addWidget(self.radioButton_all)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label_folderPath = QtWidgets.QLabel(TabConfig)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_folderPath.setFont(font)
        self.label_folderPath.setObjectName("label_folderPath")
        self.gridLayout.addWidget(self.label_folderPath, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_folderPath = QtWidgets.QLineEdit(TabConfig)
        self.lineEdit_folderPath.setEnabled(False)
        self.lineEdit_folderPath.setText("")
        self.lineEdit_folderPath.setObjectName("lineEdit_folderPath")
        self.horizontalLayout_2.addWidget(self.lineEdit_folderPath)
        self.pushButton_selectFolder = QtWidgets.QPushButton(TabConfig)
        self.pushButton_selectFolder.setObjectName("pushButton_selectFolder")
        self.horizontalLayout_2.addWidget(self.pushButton_selectFolder)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.retranslateUi(TabConfig)
        QtCore.QMetaObject.connectSlotsByName(TabConfig)

    def retranslateUi(self, TabConfig):
        _translate = QtCore.QCoreApplication.translate
        TabConfig.setWindowTitle(_translate("TabConfig", "Form"))
        self.label_previewNum.setText(_translate("TabConfig", "预览个数："))
        self.radioButton_topN.setText(_translate("TabConfig", "前30个（默认）"))
        self.radioButton_all.setText(_translate("TabConfig", "全部文件（文件多的话会卡）"))
        self.label_folderPath.setText(_translate("TabConfig", "文件位置："))
        self.pushButton_selectFolder.setText(_translate("TabConfig", "选择目录"))

