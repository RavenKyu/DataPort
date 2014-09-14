# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Thu Sep 11 23:01:25 2014
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
        Form.resize(792, 191)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 620, 191))
        self.groupBox.setMinimumSize(QtCore.QSize(124, 0))
        self.groupBox.setBaseSize(QtCore.QSize(86, 0))
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
        self.groupBox.setPalette(palette)
        self.groupBox.setToolTip(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget_protocolAssembler = QtGui.QWidget(self.groupBox)
        self.widget_protocolAssembler.setGeometry(QtCore.QRect(10, 20, 601, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.widget_protocolAssembler.setPalette(palette)
        self.widget_protocolAssembler.setObjectName(_fromUtf8("widget_protocolAssembler"))
        self.pb_sendButton = QtGui.QPushButton(self.groupBox)
        self.pb_sendButton.setGeometry(QtCore.QRect(10, 129, 600, 50))
        self.pb_sendButton.setCheckable(False)
        self.pb_sendButton.setAutoDefault(False)
        self.pb_sendButton.setDefault(False)
        self.pb_sendButton.setFlat(False)
        self.pb_sendButton.setObjectName(_fromUtf8("pb_sendButton"))
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 100, 601, 27))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_20.setMargin(0)
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.checkBox_autoSending = QtGui.QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_autoSending.setObjectName(_fromUtf8("checkBox_autoSending"))
        self.horizontalLayout_20.addWidget(self.checkBox_autoSending)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_15 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(12, 0))
        self.label_15.setMaximumSize(QtCore.QSize(68, 16777215))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_21.addWidget(self.label_15)
        self.sp_intervalTime = QtGui.QSpinBox(self.horizontalLayoutWidget_6)
        self.sp_intervalTime.setMaximum(999999999)
        self.sp_intervalTime.setObjectName(_fromUtf8("sp_intervalTime"))
        self.horizontalLayout_21.addWidget(self.sp_intervalTime)
        self.label_16 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(23, 0))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_21.addWidget(self.label_16)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)
        self.widget_protocol_manager = QtGui.QWidget(Form)
        self.widget_protocol_manager.setGeometry(QtCore.QRect(630, 0, 161, 191))
        self.widget_protocol_manager.setObjectName(_fromUtf8("widget_protocol_manager"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pb_sendButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.slot_send_data)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "입력", None))
        self.pb_sendButton.setText(_translate("Form", "전송", None))
        self.checkBox_autoSending.setText(_translate("Form", "자동 전송", None))
        self.label_15.setText(_translate("Form", "전송 간격", None))
        self.label_16.setText(_translate("Form", "ms", None))

