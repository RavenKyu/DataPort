# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Sun Jul 27 06:16:12 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(161, 191)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 161, 191))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 141, 161))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget_5)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout_7.addWidget(self.comboBox)
        self.lineEdit_protocolName = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit_protocolName.setObjectName(_fromUtf8("lineEdit_protocolName"))
        self.verticalLayout_7.addWidget(self.lineEdit_protocolName)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_7.addWidget(self.pushButton_2)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_7.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_7.addWidget(self.pushButton_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_3.setTitle(_translate("Form", "프로토콜 관리", None))
        self.pushButton_2.setText(_translate("Form", "프로토콜 불러오기", None))
        self.pushButton_4.setText(_translate("Form", "프로토콜 저장하기", None))
        self.pushButton_5.setText(_translate("Form", "프로토콜 삭제하기", None))

