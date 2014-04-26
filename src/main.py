# coding: utf-8
import sys, time
from PyQt4 import QtGui, QtCore
from ui import Ui_MainWindow
from serialHandler import SerialHandler

class mainForm(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ser = SerialHandler() # 시리얼 인스턴스 
        
        self.availableComport_into_comboBox(
            self.ser.searchAvailableComport()
        ) # 시리얼 포트 ComboBox 초기화

    # 사용 가능한 시리얼 포트를 찾아서 ComboBox에 추가
    def availableComport_into_comboBox(self, comNum):
        for i in comNum:
            self.ui.comboBox_Comport.addItem(
                QtCore.QString('COM' + str(i))
            ) 

    def slot_pushButton_serialConnection(self):
        # 설정된 시리얼의 정보를 알맞은 타입으로 저장
        serSetting = {'comPort' : self.ui.comboBox_Comport.currentText(),
                      'comBaudrate' : int(self.ui.comboBox_Baudrate.currentText()),
                      'parityBit' : self.ui.comboBox_parityBit.currentIndex(),
                      'stopBit' : int(self.ui.comboBox_stopBit.currentText())}
 
        self.serSetting = self.ser.convertSerSetting(serSetting) # OS 호환성 및 설정을 위해 값 변경
 
        if True != self.ser.serConnect(serSetting): # 시리얼을 사용할 수 없는 상태
            self.ser.serClose()
            self.ui.pushButton_connect.setText(QtCore.QString(u'연결하기'));
        else:
            self.ui.pushButton_connect.setText(QtCore.QString(u'연결끊기'));     

    def slot_pushButton_sendData(self): # 데이터 전송 
        if self.ser.isOpen() is False:  # 시리얼 연결이 안되어 있을때
            return
            
        dataBuf = ''
        dataBuf = self.getAssembledProtocol() # 프로토콜 데이터 취합 

        self.ser.writeData(dataBuf)
        self.updateText(dataBuf, 0)

    def updateText( self, text, destination):
        # Hex 값 표출 창 
        dataLen = len(text) 
        # dataLen = len(text) / 2
        buf  = '(' + str(dataLen) + ' Byte)\n' + str(text).encode('hex') + '\n'
        if destination == 0:    # 송신 
            self.ui.textEdit_1.insertPlainText(buf)
        else:                   # 수신  
            self.ui.textEdit_3.insertPlainText(buf)

        # Ascii 값 표출 창 
        dataLen = len(text) 
        buf = '(' + str(dataLen) + ' Byte)\n' + text + '\n'
        if destination == 0: 
            self.ui.textEdit_4.insertPlainText(buf)
        else:
            self.ui.textEdit_2.insertPlainText(buf)

    def slot_comboBox_hexOrAscii(self, status): 
        # Hex 또는 Ascii 콤보 박스 
        if self.ui.comboBox_HexOrAscii.currentIndex() == 0:
            Data = str(self.ui.lineEdit_protocol.text()).encode('hex')
        else:
            Data = str(self.ui.lineEdit_protocol.text()).decode('hex')
        self.ui.lineEdit_protocol.setText(Data)


    def getAssembledProtocol(self):
        # 프로토콜란에 입력된 데이터를 하나의 문자열로 취합 
        status = self.ui.comboBox_HexOrAscii.currentIndex()
        head1 = '' + str(self.ui.lineEdit_head1.text()).decode('hex')
        head2 = '' + str(self.ui.lineEdit_head2.text()).decode('hex')
        
        if 0 == status:         # HEX 상태일 경우 
            protocol = '' + str(self.ui.lineEdit_protocol.text()).decode('hex')
        else:
            protocol = '' + self.ui.lineEdit_protocol.text()

        tail1 = '' + str(self.ui.lineEdit_tail1.text()).decode('hex')
        tail2 = '' + str(self.ui.lineEdit_tail2.text()).decode('hex')
        dataBuf = '' + head1 + head2 + protocol + tail1 + tail2
            
        return dataBuf

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = mainForm()
    myapp.show()
    sys.exit(app.exec_())
 
 
