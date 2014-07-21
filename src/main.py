# coding: utf8
import sys, time
from PyQt4 import QtGui, QtCore
from ui import Ui_MainWindow
from serialHandler import SerialHandler
from protocolHandle import ProtocolHandler
from tcpIpHandler import TCPHandler

from dialog import Ui_Dialog

class SerialThread(QtCore.QThread):
    # 자료 수신 쓰레드 
    updated = QtCore.pyqtSignal(str, int)

    def __init__(self, ser, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.ser = ser

    def run(self):
        while True: 

            # 수신부 
            self.readSerialBuf = self.ser.readData(num = 1024)
            if not self.readSerialBuf :
                pass
            else:
                self.updated.emit(self.readSerialBuf, 1)


class SerialThreadAutoSend(QtCore.QThread):
    # 데이터 자동 전송 쓰레드 
    updated = QtCore.pyqtSignal(str, int)

    def __init__(self, ser, parent = None): 
        QtCore.QThread.__init__(self, parent)
        self.ser = ser

    def sendData(self):
        self.ser.writeData(self.data)
        self.updated.emit(self.data, 0) # 자료 전송 후, 송신표출창에 업데이트 
        
    def run(self):
        while True:
            # 자동 전송 체크박스 상태에 따라 동작 
            if self.status is False:  
                break

            self.ser.writeData(self.data)
            self.updated.emit(self.data, 0)
            
            time.sleep(self.intervalTime / 1000.0)


    def changeSetting(self, intervalTime, data ):
        self.intervalTime = intervalTime
        self.data = data

    def stopThread(self, status):
        self.status = status;


class mainForm(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ser = SerialHandler() # 시리얼 인스턴스 
        self.tcp = TCPHandler()    # TCP/IP 인스턴스 
        
        self.availableComport_into_comboBox(
            self.ser.searchAvailableComport()
        ) # 시리얼 포트 ComboBox 초기화

        self.autoSendChecked = False

        # 프로토콜 저장 기능 관련
        self.protocolHandler = ProtocolHandler()

    def recvThread(self, fd):
        # 자동 전송기능 관련 
        self.sendThreadHandle = SerialThreadAutoSend(fd)
        self.sendThreadHandle.updated.connect(self.updateText)

        # 수신 기능 관련 
        self.serialThreadHandle = SerialThread(fd)
        self.serialThreadHandle.updated.connect(self.updateText)

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
            self.serialThreadHandle.start()
            self.ui.pushButton_connect.setText(QtCore.QString(u'연결끊기'));     

    def slot_pushButton_sendData(self, status): # 데이터 전송 
        if self.ser.isOpen() is False:  # 시리얼 연결이 안되어 있을때
            return

        dataBuf = self.getAssembledProtocol()            
        self.sendThreadHandle.changeSetting(
            self.ui.spinBox_intervalTime.value(), dataBuf
        )                       # 자동전송 쓰레드의 전송데이터 값을 변경 

        if status is False:
            self.ui.pushButton_3.setText(u'전송')  
            if self.autoSendChecked is True: # 자동전송 기능 활성 검사 
                self.sendThreadHandle.stopThread(False)          
            else:
                self.sendThreadHandle.sendData()          
        else:
            self.ui.pushButton_3.setText(u'중지')
            self.sendThreadHandle.stopThread(True)          
            self.sendThreadHandle.start()


    def updateText( self, text, destination):
        dataLen = ''
        timeStamp = ''

        # Hex 값 표출 창
        # 옵션 검사 
        if 2 == self.ui.checkBox_timeStamp.checkState(): 
            # 타임 스탬프가 Checked 상태라면,
            timeStamp = '' + time.strftime('%Y-%m-%d %H:%M:%S')

        if 2 == self.ui.checkBox_dataLength.checkState(): 
            # 데이터 길이가 Checked 상태라면,
            dataLen = '' + str(len(text)) + ' Byte '

        buf = dataLen + timeStamp + '\n' + \
              str(
                  unicode(text).encode('utf-8')
              ).encode('hex') + '\n\n' # 확장 아스키 출력 에러 방지 

        if destination == 0:    # 송신 
            self.ui.textEdit_1.insertPlainText(buf)
            self.ui.textEdit_1.moveCursor(QtGui.QTextCursor.End) # 스크롤을 항상 끝으로 
        else:                   # 수신  
            self.ui.textEdit_3.insertPlainText(buf)
            self.ui.textEdit_3.moveCursor(QtGui.QTextCursor.End) # 스크롤을 항상 끝으로 

        # Ascii 값 표출 창 
        buf = dataLen + timeStamp + '\n' + text + '\n'

        if destination == 0: 
            self.ui.textEdit_4.insertPlainText(buf)
            self.ui.textEdit_4.moveCursor(QtGui.QTextCursor.End) # 스크롤을 항상 끝으로 
        else:
            self.ui.textEdit_2.insertPlainText(buf)
            self.ui.textEdit_2.moveCursor(QtGui.QTextCursor.End) # 스크롤을 항상 끝으로 

    def slot_comboBox_hexOrAscii(self, status): 
        # Hex 또는 Ascii 콤보 박스 
        if self.ui.comboBox_HexOrAscii.currentIndex() == 0:
            Data = str(self.ui.lineEdit_protocol.text()).encode('hex')
        else:
            try:
                Data = str(self.ui.lineEdit_protocol.text()).decode('hex')
            except:
                self.dialog = Ui_Dialog()

                self.dialog.exec_()
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

    def slot_radioBox_nothing(self): # 데이터 전송 
        self.ui.lineEdit_head1.setText('')
        self.ui.lineEdit_head2.setText('')
        self.ui.lineEdit_tail1.setText('')
        self.ui.lineEdit_tail2.setText('')

    def slot_radioBox_CR(self): # 데이터 전송 
        self.ui.lineEdit_head1.setText('')
        self.ui.lineEdit_head2.setText('')
        self.ui.lineEdit_tail1.setText('')
        self.ui.lineEdit_tail2.setText('0d')

    def slot_radioBox_LF(self): # 데이터 전송 
        self.ui.lineEdit_head1.setText('')
        self.ui.lineEdit_head2.setText('')
        self.ui.lineEdit_tail1.setText('')
        self.ui.lineEdit_tail2.setText('0a')

    def slot_radioBox_CRLF(self): # 데이터 전송 
        self.ui.lineEdit_head1.setText('')
        self.ui.lineEdit_head2.setText('')
        self.ui.lineEdit_tail1.setText('')
        self.ui.lineEdit_tail2.setText('0d0a')

    def slot_radioBox_STXETX(self): # 데이터 전송 
        self.ui.lineEdit_head1.setText('02')
        self.ui.lineEdit_head2.setText('')
        self.ui.lineEdit_tail1.setText('03')
        self.ui.lineEdit_tail2.setText('0d0a')

    def slot_checkBox_autoSendData(self, status):
        # 자동 전송 기능,
        self.autoSendChecked = status
        if status == True:
            self.ui.pushButton_3.setCheckable(True)
        else:
            self.ui.pushButton_3.setCheckable(False)
            self.sendThreadHandle.stopThread(False)          
            self.ui.pushButton_3.setText(u'전송')

    # 매크로 관련 메소드 
    def slot_pushButton_addProtocol(self):

        # 프로토콜 이름이 있는지 검사 
        # 이름이 없으면 그냥 무시 
        if '' == self.ui.lineEdit_protocolName.text():
            return

        # 열려있는 매크로 파일이 있는지 검사
        if False == self.protocolHandler.isOpenFile():
            self.fileName = QtGui.QFileDialog.getSaveFileName(None, 'Save File', '.prt')
            self.protocolHandler.createFile(self.fileName)
        else:
            pass

        # 프로토콜은 항상 HEX로만 저장 할 수 있게,
        # 입력 포맷 상태 확인
        protocol = self.ui.lineEdit_protocol.text()
        if self.ui.comboBox_HexOrAscii.currentIndex() == 1:
            protocol = str(protocol).encode('hex')            
            
        # 입력된 데이터를 읽어서 추가 
        self.protocolHandler.addProtocol(
            unicode(self.ui.lineEdit_protocolName.text()),
            self.ui.lineEdit_head1.text(),
            self.ui.lineEdit_head2.text(),
            protocol,
            self.ui.lineEdit_tail1.text(),
            self.ui.lineEdit_tail2.text() )

        self.reflashItemlist()
        self.ui.lineEdit_protocolName.setText('') # 프로토콜 이름란을 비움 
        self.selectedProtocol = self.protocolHandler.getProtocol() # 목록을 다시 읽어옴 
        selectedList = len(self.selectedProtocol['Protocol']) - 1
        self.slot_comboBox_protocolList(selectedList) # 추가된 마지막 프로토콜 표시, 배열 시작은 0부터 시작이라서 - 1
        self.ui.comboBox.setCurrentIndex(selectedList)

    def slot_pushButton_loadProtocol(self):
        # 프로토콜 파일에서 읽어오기  
        self.fileName = QtGui.QFileDialog.getOpenFileName(None, 'Save File', '.prt')
        if str(self.fileName) == '': # 파일을 선택하지 않았을 경우 
            return None

        self.protocolHandler.openFile(str(self.fileName))
        self.protocolHandler.open()
        self.reflashItemlist()

    def slot_pushButton_delProtocol(self):
        # 프로토콜 삭제 
        self.protocolHandler.delProtocol(self.ui.comboBox.currentIndex())
        self.reflashItemlist()


    def reflashItemlist(self):
        # 목록 비우기 
        countIndexNum = self.ui.comboBox.count()
        if 0 != countIndexNum:
            for i in range(countIndexNum):
                self.ui.comboBox.removeItem(0)

        # 목록 채우기 
        # JSON으로 저장된 프로토콜 저장파일을 읽어와서,
        # 순서대로 목록에 추가 
        self.selectedProtocol = self.protocolHandler.getProtocol()
        for i in range(len(self.selectedProtocol['Protocol'])):
            self.ui.comboBox.insertItem(
                i, 
                self.selectedProtocol['Protocol'][i]['Name'], ''
            )

    def slot_comboBox_protocolList(self, indexNumber):
        # 선택된 프로토콜 목록의 내용을 입력란에 표시 
        self.ui.lineEdit_head1.setText(str(self.selectedProtocol['Protocol'][indexNumber]['Head1']))
        self.ui.lineEdit_head2.setText(str(self.selectedProtocol['Protocol'][indexNumber]['Head2']))

        if self.ui.comboBox_HexOrAscii.currentIndex() == 0:
            self.ui.lineEdit_protocol.setText(self.selectedProtocol['Protocol'][indexNumber]['Protocol'])
        else:
            self.ui.lineEdit_protocol.setText(self.selectedProtocol['Protocol'][indexNumber]['Protocol'].decode('hex'))

        self.ui.lineEdit_tail1.setText(str(self.selectedProtocol['Protocol'][indexNumber]['Tail1']))
        self.ui.lineEdit_tail2.setText(str(self.selectedProtocol['Protocol'][indexNumber]['Tail2']))        


    def slot_pushButton_dataClean(self):
        # 송·수신창 비우기 
        self.ui.textEdit_1.setText('')
        self.ui.textEdit_3.setText('')
        self.ui.textEdit_2.setText('')
        self.ui.textEdit_4.setText('')


    def slot_pushButton_tcpConnection(self):
        # 설정된 TCP/IP의 정보를 알맞은 타입으로 저장
        tcpSetting = {
            'IP' : str(self.ui.lineEdit_IP_Address.text()),
            'Port' : int(self.ui.lineEdit_PortNumber.text())
        }
 
        if True != self.tcp.tcpConnect(tcpSetting): # 시리얼을 사용할 수 없는 상태
            self.tcp.close()
            self.ui.pushButton_tcpConnect.setText(QtCore.QString(u'연결하기'));
        else:
            self.recvThread(self.tcp)
            self.serialThreadHandle.start()
            self.ui.pushButton_tcpConnect.setText(QtCore.QString(u'연결끊기'));     



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = mainForm()
    myapp.show()
    sys.exit(app.exec_())
 
 
