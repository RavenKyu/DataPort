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

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = mainForm()
    myapp.show()
    sys.exit(app.exec_())
 
 
