# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from ui import Ui_commSetWidget

from src.lib.serial_lib.serialHandler import SerialHandler

class communicationSetWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(communicationSetWidget, self).__init__(parent)  # __init__(parent)가 아니면 메인에서 본 위젯의 시그널을 받을 수 없음

        # 화면 구성
        self.ui = Ui_commSetWidget()
        self.ui.setupUi(self)

        self.ser = SerialHandler()

        # 시리얼 포트 ComboBox 초기화
        self.availableComport_into_comboBox(
            self.ser.searchAvailableComport())

    def availableComport_into_comboBox(self, comNum):
        for i in comNum:
            self.ui.cb_comPort.addItem(
                QtCore.QString('COM' + str(i)))


    def func_getValue(self):
        serSetting = {}

        # 선택된 통신 장치에 따라 다른 값을 반환
        if self.ui.rb_serialSelected.isChecked() is True:
            serSetting = {
                'commType': 'serial',
                'comPort': str(self.ui.cb_comPort.currentText()),
                'baudrate': int(self.ui.cb_baudrate.currentText()),
                'dataBit': int(self.ui.cb_dataBit.currentText()),
                'parityBit': str(self.ui.cb_parityBit.currentText()),
                'stopBit': int(self.ui.cb_stopBit.currentText())
            }
            serSetting = self.ser.convertSerSetting(serSetting)

        elif self.ui.rb_tcpipSelected.isChecked() is True:
            serSetting = {
                'commType': 'tcpip',
                'ipAddress': str(self.ui.le_ipAddress.text()),
                'port': int(self.ui.le_portNumber.text()),
                'type': 'server' if self.ui.rb_server.isChecked() is True else 'socket'
            }

        if __package__ is None:
            print serSetting

        return serSetting


# 모듈 단독 실행 코드
if '__main__' == __name__:
    application = QtGui.QApplication(sys.argv)
    test = communicationSetWidget()

    test.show()
    button = QtGui.QPushButton('click')
    button.show()
    QtCore.QObject.connect(button, QtCore.SIGNAL('clicked()'), test.func_getValue)

    sys.exit(application.exec_())