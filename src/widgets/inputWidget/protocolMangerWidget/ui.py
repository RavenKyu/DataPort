# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Sun Sep 21 15:59:21 2014
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
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 140, 160))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.cb_protocol_list = QtGui.QComboBox(self.verticalLayoutWidget_5)
        self.cb_protocol_list.setObjectName(_fromUtf8("cb_protocol_list"))
        self.verticalLayout_7.addWidget(self.cb_protocol_list)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.le_protocol_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.le_protocol_name.setObjectName(_fromUtf8("le_protocol_name"))
        self.horizontalLayout.addWidget(self.le_protocol_name)
        self.pb_save = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pb_save.setMaximumSize(QtCore.QSize(35, 16777215))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.horizontalLayout.addWidget(self.pb_save)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.pb_load = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pb_load.setObjectName(_fromUtf8("pb_load"))
        self.verticalLayout_7.addWidget(self.pb_load)
        self.pb_delete = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pb_delete.setObjectName(_fromUtf8("pb_delete"))
        self.verticalLayout_7.addWidget(self.pb_delete)
        self.pb_show_dialbox = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pb_show_dialbox.setObjectName(_fromUtf8("pb_show_dialbox"))
        self.verticalLayout_7.addWidget(self.pb_show_dialbox)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pb_save, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.slot_save)
        QtCore.QObject.connect(self.pb_load, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.slot_load)
        QtCore.QObject.connect(self.pb_delete, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.slot_del)
        QtCore.QObject.connect(self.pb_show_dialbox, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.slot_show_dial)
        QtCore.QObject.connect(self.cb_protocol_list, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), Form.slot_set_selected_protocol)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_3.setTitle(_translate("Form", "프로토콜 관리", None))
        self.pb_save.setText(_translate("Form", "저장", None))
        self.pb_load.setText(_translate("Form", "프로토콜 불러오기", None))
        self.pb_delete.setText(_translate("Form", "프로토콜 삭제하기", None))
        self.pb_show_dialbox.setText(_translate("Form", "다이얼 형태 보기", None))

