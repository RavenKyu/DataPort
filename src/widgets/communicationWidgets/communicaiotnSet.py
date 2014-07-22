# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from ui import Ui_commSetWidget

from src.lib.serial_lib.serialHandler import SerialHandler

class communicationSetWidget(QtGui.QWidget):
    def __init__(self, parent = None):
        super(communicationSetWidget, self).__init__(parent) # __init__(parent)가 아니면 메인에서 본 위젯의 시그널을 받을 수 없음

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
        serSetting = {'comPort' : self.ui.cb_comPort.currentText(),
                      'baudrate' : int(self.ui.cb_baudrate.currentText()),
                      'dataBit' : int(self.ui.cb_dataBit.currentText()),
                      'parityBit' : self.ui.cb_parityBit.currentIndex(),
                      'stopBit' : int(self.ui.cb_stopBit.currentText())}
        return serSetting



# 모듈 단독 실행 코드
if '__main__' == __name__:
    application = QtGui.QApplication(sys.argv)
    test = communicationSetWidget()
    test.show()

    sys.exit(application.exec_())