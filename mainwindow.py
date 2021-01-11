'''
Author: mukangt
Date: 2021-01-07 13:43:51
LastEditors: mukangt
LastEditTime: 2021-01-11 11:52:28
Description: 
'''
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets

from tabs.Ui_tab_config import Ui_TabConfig
from tabs.Ui_tab_digit import Ui_TabDigit
from tabs.Ui_tab_replace import Ui_TabReplace
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('文件批量重命名工具')

        self.initUI()
        self.connectSigSlot()

        self.renames = list()
        self.filenames = list()

    def initUI(self):
        # hide progress bar
        # self.ui.progressBar.setVisible(False)

        # add tabs
        self.tabs = dict()
        self.tabs_func = dict()

        # digit tab
        tab_digit, tab_digit_ui = self.setupTabDigit()
        self.tabs[tab_digit] = tab_digit_ui
        self.tabs_func[tab_digit] = self.tab_digit_rename
        self.ui.tabWidget.addTab(tab_digit, '按数字重命名')
        self.ui.tabWidget.setCurrentIndex(0)
        # replace tab
        tab_replace, tab_replace_ui = self.setupTabReplace()
        self.tabs[tab_replace] = tab_replace_ui
        self.tabs_func[tab_replace] = self.tab_replace_rename
        self.ui.tabWidget.addTab(tab_replace, '替换')  # '中文'.decode('utf-8')
        # config tab
        tab_config, tab_config_ui = self.setupTabConfig()
        self.tabs[tab_config] = tab_config_ui
        self.tabs_func[tab_config] = self.tab_config_rename
        self.ui.tabWidget.addTab(tab_config, '系统配置')

    def setupTabDigit(self):
        tab = QtWidgets.QWidget(self)
        tab_ui = Ui_TabDigit()
        tab_ui.setupUi(tab)

        tab_ui.lineEdit_numLen.setEnabled(False)

        def enable_lineedit_numlen(state):
            if state == 0:
                tab_ui.lineEdit_numLen.setEnabled(False)
            elif state == 2:
                tab_ui.lineEdit_numLen.setEnabled(True)

        tab_ui.checkBox_numLen.stateChanged.connect(enable_lineedit_numlen)
        tab_ui.lineEdit_mould.setText('<self>_#')
        tab_ui.lineEdit_numStart.setText('0')
        tab_ui.lineEdit_numStep.setText('1')
        tab_ui.lineEdit_numLen.setText('4')

        return tab, tab_ui

    def setupTabReplace(self):
        tab = QtWidgets.QWidget(self)
        tab_ui = Ui_TabReplace()
        tab_ui.setupUi(tab)

        return tab, tab_ui

    def setupTabConfig(self):
        tab = QtWidgets.QWidget(self)
        tab_ui = Ui_TabConfig()
        tab_ui.setupUi(tab)

        cwd = os.getcwd()
        defaultFolderPath = os.path.join(cwd, 'renamed')
        tab_ui.lineEdit_folderPath.setText(defaultFolderPath)
        self.foldername = defaultFolderPath

        if tab_ui.radioButton_topN.isChecked():
            self.showNum = 'topN'
        else:
            self.showNum = 'all'

        def selectSaveFolder():
            self.foldername = QtWidgets.QFileDialog.getExistingDirectory(
                self,
                '选择重命名文件保存目录',
                '.',
            )

            # self.foldername = os.path.join(self.foldername)  # change '/' to '\'
            # os.makedirs(self.foldername)
            tab_ui.lineEdit_folderPath.setText(self.foldername)

        # change save folder
        tab_ui.pushButton_selectFolder.clicked.connect(selectSaveFolder)

        return tab, tab_ui

    def connectSigSlot(self):
        # sync vertical scroll bar
        self.ui.listWidget_src.verticalScrollBar().rangeChanged.connect(
            self.ui.verticalScrollBar_sync.setRange)
        self.ui.verticalScrollBar_sync.valueChanged.connect(
            self.ui.listWidget_src.verticalScrollBar().setValue)
        self.ui.verticalScrollBar_sync.valueChanged.connect(
            self.ui.listWidget_dst.verticalScrollBar().setValue)
        self.ui.listWidget_src.verticalScrollBar().valueChanged.connect(
            self.ui.verticalScrollBar_sync.setValue)
        self.ui.listWidget_dst.verticalScrollBar().valueChanged.connect(
            self.ui.verticalScrollBar_sync.setValue)

        # load files
        self.ui.pushButton_addFiles.clicked.connect(self.loadFiles)

        # clear added files
        self.ui.pushButton_clearFiles.clicked.connect(self.clearFiles)

        # preview files
        self.ui.pushButton_preview.clicked.connect(self.previewFiles)

        # rename files
        self.ui.pushButton_startRename.clicked.connect(self.renameFiles)

    def loadFiles(self):
        self.filenames, _ = QtWidgets.QFileDialog.getOpenFileNames(
            self,
            '选择需要重命名的文件（一个或多个）',
            '.',
        )
        text = '当前需要处理的文件数为：{}个'.format(len(self.filenames))
        self.ui.label_fileCnt.setText(text)

    def clearFiles(self):
        text = '当前需要处理的文件数为：{}个'.format(0)
        self.ui.label_fileCnt.setText(text)

        self.clearList()
        self.filenames.clear()

    def clearList(self):
        self.ui.listWidget_src.clear()
        self.ui.listWidget_dst.clear()
        self.renames.clear()

    def previewFiles(self):
        self.clearList()
        renameFunc = self.getRenameFunc()
        for i, f in enumerate(self.filenames):
            src_name = os.path.basename(f)
            self.ui.listWidget_src.addItem(src_name)

            dst_name = renameFunc(src_name, i)
            self.ui.listWidget_dst.addItem(dst_name)

            self.renames.append(os.path.join(self.foldername, dst_name))

    def getRenameFunc(self):
        tab = self.ui.tabWidget.currentWidget()
        tab_ui = self.tabs[tab]

        return self.tabs_func[tab](tab_ui)

    def renameFiles(self):
        if not self.renames:
            return

        if not os.path.exists(self.foldername):
            os.makedirs(self.foldername)

        # self.ui.progressBar.setVisible(True)
        # self.ui.progressBar.setMaximum(len(self.filenames))
        total_num = len(self.filenames)
        self.ui.progressBar.setValue(0)
        for i, (src, dst) in enumerate(zip(self.filenames, self.renames)):
            shutil.copy(src, dst)
            self.ui.progressBar.setValue((i + 1) * 100 // total_num)

    def tab_replace_rename(self, tab_ui):
        src = tab_ui.lineEdit_src.text()
        dst = tab_ui.lineEdit_dst.text()

        def rename(input, i):
            name, ext = os.path.splitext(input)
            name = name.replace(src, dst)
            return ''.join([name, ext])

        return rename

    def tab_config_rename(self, tab_ui):
        def rename(input, i):
            output = input
            return output

        return rename

    def tab_digit_rename(self, tab_ui):
        def sortByName():
            self.filenames.sort()

        def sortByReversedName():
            self.filenames.sort(reverse=True)

        sortFuncs = {
            'sortByName': sortByName,
            'sortByReversedName': sortByReversedName
        }

        if tab_ui.radioButton_sortByName.isChecked():
            sortFuncs['sortByName']()
        else:
            sortFuncs['sortByReversedName']()

        mould = tab_ui.lineEdit_mould.text()

        num_start = int(tab_ui.lineEdit_numStart.text())
        num_step = int(tab_ui.lineEdit_numStep.text())
        num_len = 1
        if tab_ui.checkBox_numLen.isChecked():
            num_len = int(tab_ui.lineEdit_numLen.text())

        def rename(input, i):
            name, ext = os.path.splitext(input)
            name_tmp = mould.replace('<self>', name)

            n = num_start + i * num_step
            num_tmp = '{{:0>{}d}}'.format(num_len).format(n)

            name_tmp = name_tmp.replace('#', num_tmp)
            output = ''.join([name_tmp, ext])

            return output

        return rename