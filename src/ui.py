# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Fri Jul 25 00:54:03 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(831, 646)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabw_pannel = QtGui.QTabWidget(self.centralwidget)
        self.tabw_pannel.setGeometry(QtCore.QRect(6, 10, 821, 591))
        self.tabw_pannel.setBaseSize(QtCore.QSize(0, 6))
        self.tabw_pannel.setAcceptDrops(False)
        self.tabw_pannel.setDocumentMode(False)
        self.tabw_pannel.setTabsClosable(True)
        self.tabw_pannel.setMovable(True)
        self.tabw_pannel.setObjectName(_fromUtf8("tabw_pannel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_Protocol = QtGui.QAction(MainWindow)
        self.actionNew_Protocol.setObjectName(_fromUtf8("actionNew_Protocol"))
        self.actionOpen_Protocol = QtGui.QAction(MainWindow)
        self.actionOpen_Protocol.setObjectName(_fromUtf8("actionOpen_Protocol"))
        self.actionSave_Protocol = QtGui.QAction(MainWindow)
        self.actionSave_Protocol.setObjectName(_fromUtf8("actionSave_Protocol"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabw_pannel.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu.setTitle(_translate("MainWindow", "파일", None))
        self.actionNew_Protocol.setText(_translate("MainWindow", "New Protocol", None))
        self.actionOpen_Protocol.setText(_translate("MainWindow", "Open Protocol", None))
        self.actionSave_Protocol.setText(_translate("MainWindow", "Save Protocol", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.action.setText(_translate("MainWindow", "실황 화면", None))
        self.action_2.setText(_translate("MainWindow", "종료", None))

