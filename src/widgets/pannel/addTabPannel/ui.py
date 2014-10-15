# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Tue Sep 16 14:10:03 2014
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(799, 540)
        self.clb = QtGui.QCommandLinkButton(Form)
        self.clb.setGeometry(QtCore.QRect(21, 15, 756, 79))
        self.clb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clb.setAutoFillBackground(False)
        self.clb.setIconSize(QtCore.QSize(40, 40))
        self.clb.setObjectName(_fromUtf8("clb"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.clb, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.slot_add_data_port)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.clb.setText(_translate("Form", "DataPort 탭 추가\n"
"시리얼 및 TCP 통신, 입력했던 프로토콜 저장, 자동 전송 기능", None))

