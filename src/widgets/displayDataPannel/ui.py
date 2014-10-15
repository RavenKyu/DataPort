# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Wed Sep 17 11:59:32 2014
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

class Ui_displayPannel(object):
    def setupUi(self, displayPannel):
        displayPannel.setObjectName(_fromUtf8("displayPannel"))
        displayPannel.resize(622, 347)
        self.groupBox_4 = QtGui.QGroupBox(displayPannel)
        self.groupBox_4.setGeometry(QtCore.QRect(230, 0, 391, 311))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.toolBox_3 = QtGui.QToolBox(self.groupBox_4)
        self.toolBox_3.setGeometry(QtCore.QRect(10, 20, 371, 281))
        self.toolBox_3.setObjectName(_fromUtf8("toolBox_3"))
        self.page_5 = QtGui.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 371, 229))
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.te_sendHex = QtGui.QTextEdit(self.page_5)
        self.te_sendHex.setGeometry(QtCore.QRect(0, 0, 371, 231))
        self.te_sendHex.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.te_sendHex.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.te_sendHex.setObjectName(_fromUtf8("te_sendHex"))
        self.toolBox_3.addItem(self.page_5, _fromUtf8(""))
        self.page_6 = QtGui.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 371, 229))
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.te_sendAscii = QtGui.QTextEdit(self.page_6)
        self.te_sendAscii.setGeometry(QtCore.QRect(0, 0, 371, 231))
        self.te_sendAscii.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.te_sendAscii.setObjectName(_fromUtf8("te_sendAscii"))
        self.toolBox_3.addItem(self.page_6, _fromUtf8(""))
        self.groupBox_6 = QtGui.QGroupBox(displayPannel)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 311, 621, 36))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_6)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 11, 421, 20))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_17.setMargin(0)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.chkb_timeStamp = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.chkb_timeStamp.setChecked(True)
        self.chkb_timeStamp.setTristate(False)
        self.chkb_timeStamp.setObjectName(_fromUtf8("chkb_timeStamp"))
        self.horizontalLayout_17.addWidget(self.chkb_timeStamp)
        self.chkb_dataLength = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.chkb_dataLength.setChecked(True)
        self.chkb_dataLength.setObjectName(_fromUtf8("chkb_dataLength"))
        self.horizontalLayout_17.addWidget(self.chkb_dataLength)
        self.pb_clearShowWindow = QtGui.QPushButton(self.groupBox_6)
        self.pb_clearShowWindow.setGeometry(QtCore.QRect(469, 11, 145, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_clearShowWindow.sizePolicy().hasHeightForWidth())
        self.pb_clearShowWindow.setSizePolicy(sizePolicy)
        self.pb_clearShowWindow.setMinimumSize(QtCore.QSize(0, 15))
        self.pb_clearShowWindow.setMaximumSize(QtCore.QSize(200, 20))
        self.pb_clearShowWindow.setObjectName(_fromUtf8("pb_clearShowWindow"))
        self.groupBox_5 = QtGui.QGroupBox(displayPannel)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 0, 221, 311))
        self.groupBox_5.setAutoFillBackground(False)
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.toolBox = QtGui.QToolBox(self.groupBox_5)
        self.toolBox.setGeometry(QtCore.QRect(10, 20, 201, 281))
        self.toolBox.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.RepublicOfKorea))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 201, 229))
        self.page.setObjectName(_fromUtf8("page"))
        self.te_recvHex = QtGui.QTextEdit(self.page)
        self.te_recvHex.setGeometry(QtCore.QRect(0, 0, 201, 231))
        self.te_recvHex.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.te_recvHex.setObjectName(_fromUtf8("te_recvHex"))
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 201, 229))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.te_recvAscii = QtGui.QTextEdit(self.page_2)
        self.te_recvAscii.setGeometry(QtCore.QRect(0, 0, 201, 231))
        self.te_recvAscii.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.te_recvAscii.setObjectName(_fromUtf8("te_recvAscii"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))

        self.retranslateUi(displayPannel)
        self.toolBox_3.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)
        QtCore.QObject.connect(self.pb_clearShowWindow, QtCore.SIGNAL(_fromUtf8("clicked()")), displayPannel.slot_clear_display)
        QtCore.QMetaObject.connectSlotsByName(displayPannel)

    def retranslateUi(self, displayPannel):
        displayPannel.setWindowTitle(_translate("displayPannel", "Form", None))
        self.groupBox_4.setTitle(_translate("displayPannel", "수신", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_5), _translate("displayPannel", "Hex", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_6), _translate("displayPannel", "Ascii", None))
        self.groupBox_6.setTitle(_translate("displayPannel", "송 · 수신 데이터 표출 옵션", None))
        self.chkb_timeStamp.setText(_translate("displayPannel", "타임 스탬프", None))
        self.chkb_dataLength.setText(_translate("displayPannel", "데이터 길이", None))
        self.pb_clearShowWindow.setText(_translate("displayPannel", "송 · 수신창 지우기", None))
        self.groupBox_5.setTitle(_translate("displayPannel", "송신", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("displayPannel", "Hex", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("displayPannel", "Ascii", None))

