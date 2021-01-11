'''
Author: mukangt
Date: 2021-01-07 16:14:01
LastEditors: mukangt
LastEditTime: 2021-01-07 16:16:42
Description: 
'''
import sys

from PyQt5 import QtWidgets

from mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())