# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Mon Jul 28 04:01:36 2014
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

class Ui_Pannel(object):
    def setupUi(self, Pannel):
        Pannel.setObjectName(_fromUtf8("Pannel"))
        Pannel.resize(799, 540)
        self.pb_connect = QtGui.QPushButton(Pannel)
        self.pb_connect.setGeometry(QtCore.QRect(0, 320, 161, 23))
        self.pb_connect.setObjectName(_fromUtf8("pb_connect"))
        self.widgetCommSet = QtGui.QWidget(Pannel)
        self.widgetCommSet.setGeometry(QtCore.QRect(0, 0, 161, 311))
        self.widgetCommSet.setObjectName(_fromUtf8("widgetCommSet"))
        self.widgetDisplayPannel = QtGui.QWidget(Pannel)
        self.widgetDisplayPannel.setGeometry(QtCore.QRect(170, 0, 631, 347))
        self.widgetDisplayPannel.setAutoFillBackground(False)
        self.widgetDisplayPannel.setObjectName(_fromUtf8("widgetDisplayPannel"))
        self.widgetInputManager = QtGui.QWidget(Pannel)
        self.widgetInputManager.setGeometry(QtCore.QRect(0, 350, 620, 191))
        self.widgetInputManager.setMinimumSize(QtCore.QSize(124, 0))
        self.widgetInputManager.setBaseSize(QtCore.QSize(86, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.widgetInputManager.setPalette(palette)
        self.widgetInputManager.setToolTip(_fromUtf8(""))
        self.widgetInputManager.setObjectName(_fromUtf8("widgetInputManager"))
        self.widgetProtocolManager = QtGui.QWidget(Pannel)
        self.widgetProtocolManager.setGeometry(QtCore.QRect(630, 350, 171, 191))
        self.widgetProtocolManager.setObjectName(_fromUtf8("widgetProtocolManager"))

        self.retranslateUi(Pannel)
        QtCore.QObject.connect(self.pb_connect, QtCore.SIGNAL(_fromUtf8("clicked()")), Pannel.slot_connect)
        QtCore.QMetaObject.connectSlotsByName(Pannel)

    def retranslateUi(self, Pannel):
        Pannel.setWindowTitle(_translate("Pannel", "Form", None))
        self.pb_connect.setText(_translate("Pannel", "연결", None))

