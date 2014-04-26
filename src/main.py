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


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = mainForm()
    myapp.show()
    sys.exit(app.exec_())
 
 
