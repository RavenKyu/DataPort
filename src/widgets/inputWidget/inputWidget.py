# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from ui import Ui_Form
import time

class threadSendData(QtCore.QThread):
    def __init__(self, send_signal):
        super(threadSendData, self).__init__()
        self.device_handler = None
        self.send_signal = send_signal

        # 변수 초기화
        self.state = False
        self.data = None
        self.interval = 1000
        self.location = 0

    def __del__(self):
        self.state = False

    def set_conf(self, data, interval, device_handler, location):
        self.data = data
        self.interval = interval
        self.device_handler = device_handler
        self.location = location

    def send_data(self):
        """ 입력받은 데이터가 없을 때 """
        if not self.data:
            return

        if __package__ is None:
            print self.data
        else:
            self.device_handler.send_data(self.data)
            self.send_signal.emit(self.data, self.location)

    def stop(self):
        self.state = False

    def is_running(self):
        return self.state

    def run(self):
        self.state = True
        while True:
            if self.state is False or self.data is None:
                break

            if __package__ is None:
                print self.data
            else:
                self.device_handler.sendData(self.data)
                self.send_signal.emit(self.data, self.location)

            time.sleep(int(self.interval) / 1000.0)


class inputPannel(QtGui.QWidget):
    commSignal = QtCore.pyqtSignal(str, int)

    START = True
    STOP = False

    def __init__(self, parent= None):
        super(inputPannel, self).__init__(parent)

        # 화면 구성
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.device_handler = None
        self.location = None

        from src.widgets.inputWidget.protocolAssembler.protocolAssembler import protocolAssembler
        self.protocol_assembler = protocolAssembler(self.ui.widget_protocolAssembler)

        from src.widgets.inputWidget.protocolMangerWidget.protocolManagerWidget import protocolManager
        self.protocol_manager = protocolManager(self.ui.widget_protocol_manager)

        # 클래스간의 통신을 위한 설정
        self.protocol_assembler.set_handler(self.protocol_manager)
        self.protocol_manager.set_handler(self.protocol_assembler)

        # self.protocol_manager.ui.pb_save.connect(
        #     self.protocol_manager.ui.pb_save,
        #     QtCore.SIGNAL("clicked()"),
        #     self.sig_protocol_manager_save
        #     )

        self.send_thread = threadSendData(self.commSignal)

    def set_conf(self, device_handler, location):
        self.device_handler = device_handler
        self.location = location
        self.send_thread.set_conf(None, 0, self.device_handler, location)

    def slot_send_data(self):
        interval = int(self.ui.sp_intervalTime.text())
        check_auto_send = self.ui.checkBox_autoSending.isChecked()
        if self.device_handler is None: # 통신설정이 이루어지지 않았음
            if __package__ is None:
                print 'No Handler'
            return
        if self.device_handler.isOpen() is not True:
            if __package__ is None:
                print 'device is not open now'
            return

        data_buf = self.protocol_assembler.get_assembled_data()
        self.send_thread.set_conf(data_buf, interval, self.device_handler, self.location)

        if self.send_thread.is_running() is True:
            self.ui.pb_sendButton.setText(u'전송')
            self.send_thread.stop()
        else:
            if check_auto_send is True: # 자동전송 기능 활성 검사
                self.ui.pb_sendButton.setText(u'중지')
                self.send_thread.stop()
                self.send_thread.start()
            else:
                self.send_thread.send_data() # 한번 보내기



# 모듈 단독 실행 코드
if '__main__' == __name__:
    import serial
    ser = serial.Serial('com12')

    application = QtGui.QApplication(sys.argv)
    test = inputPannel(ser)
    test.show()
    sys.exit(application.exec_())