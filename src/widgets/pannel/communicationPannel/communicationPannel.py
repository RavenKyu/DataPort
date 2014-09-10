# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

from ui import Ui_Pannel
from src.widgets.communicationWidgets.communicaiotnSet import communicationSetWidget
from src.widgets.displayDataPannel.displayDataPannel import displayDataPannel
from src.widgets.inputWidget.inputWidget import inputPannel
from src.widgets.protocolMangerWidget.protocolManagerWidget import protocolManager

from src.lib.serial_lib.serialThread import serialReceiveThread

from src.lib.tcpip_lib.tcpipHandler import server
from src.lib.tcpip_lib.tcpipHandler import socket

class communicationPannel(QtGui.QWidget):
    RECV_DATA = 1
    SEND_DATA = 0

    def __init__(self, parent = None):
        super(communicationPannel, self).__init__(parent) # __init__(parent)가 아니면 메인에서 본 위젯의 시그널을 받을 수 없음

        # 화면 구성
        self.ui = Ui_Pannel()
        self.ui.setupUi(self)

        # 통신설정 위젯
        self.commSetWidget = communicationSetWidget(self.ui.widgetCommSet)

        # 송·수신 데이터 표출
        self.displayDataPannel = displayDataPannel(self.ui.widgetDisplayPannel)

        # 입력 창 위젯
        self.inputWidget = inputPannel(self.ui.widgetInputManager)
        self.inputWidget.ui.pb_sendButton.setEnabled(False)

        # 입력 창 위젯
        self.protocolManager = protocolManager(self.ui.widgetProtocolManager)


        # 통신 핸들러 선언(기본값으로 SerialHandler)
        self.comm_handle = serialReceiveThread(self.RECV_DATA)



    def showData(self, data, location, msg=None):
        self.displayDataPannel.showData(data, location)



    def slot_connect(self):
        if self.comm_handle.isOpen() is True:
            self.comm_handle.stop()
            self.comm_handle.func_close()
            self.commSetWidget.ui.commSettingGroup.setEnabled(True)
            self.inputWidget.ui.pb_sendButton.setEnabled(False)
            self.ui.pb_connect.setText(QtCore.QString(u'연결하기'))

        else:
            conf = self.commSetWidget.func_getValue() # 통신설정 정보 가져오기
            if conf['commType'] == 'serial':
                self.comm_handle = serialReceiveThread(self.RECV_DATA)
                self.comm_handle.func_setConf(conf)


            elif conf['commType'] == 'tcpip':
                if conf['type'] == 'server':
                    self.comm_handle = server()
                elif conf['type'] == 'socket':
                    self.comm_handle = socket()
                self.comm_handle.func_setConf(conf['ipAddress'], conf['port'], self.RECV_DATA)

            if self.comm_handle.func_connect() is True: # 연결 시도
                # 시그널
                if conf['commType'] == 'serial':
                    self.comm_handle.resume()
                    self.comm_handle.start()
                # self.comm_handle.messageSignal.connect(self.showData)
                self.inputWidget.set_conf(self.comm_handle, self.SEND_DATA)

                self.comm_handle.commSignal.connect(self.showData)
                self.inputWidget.commSignal.connect(self.showData)

                self.commSetWidget.ui.commSettingGroup.setEnabled(False)
                self.inputWidget.ui.pb_sendButton.setEnabled(True)
                self.ui.pb_connect.setText(QtCore.QString(u'연결끊기'))







        # if self.ser.serConnect(serSetting) is not True: # 시리얼을 사용할 수 없는 상태
        #     self.ser.serClose()
        #     self.ui.pb_connect.setText(QtCore.QString(u'연결하기'));
        # else:
        #     self.serialThreadHandle.start()
        #     self.ui.pb_connect.setText(QtCore.QString(u'연결끊기'));

# 모듈 단독 실행 코드
if '__main__' == __name__:
    application = QtGui.QApplication(sys.argv)
    test = communicationPannel()
    test.show()
    sys.exit(application.exec_())