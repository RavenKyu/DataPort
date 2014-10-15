# -*- coding: utf-8 -*-
import sys, time
from PyQt4 import QtGui, QtCore
from ui import Ui_MainWindow
# from serialHandler import SerialHandler
# from protocolHandle import ProtocolHandler
# from tcpIpHandler import TCPHandler

from src.widgets.pannel.communicationPannel.communicationPannel import communicationPannel
from src.widgets.pannel.addTabPannel.addTabPannel import addTab

class tab_widget(QtGui.QWidget):
    def __init__(self, pannel, parent = None):
        super(tab_widget, self).__init__(parent)

        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(10, 10, 799, 540))

        self.pannel = pannel(self.widget)
        self.pannel.show()


class mainForm(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pannel = []

        # 기본 패널

        self.pannel.append(tab_widget(addTab, self))
        self.func_insert_tab(u'새로운 탭')
        self.pannel.append(tab_widget(communicationPannel, self))
        self.func_insert_tab(u'DataPort')

        QtCore.QObject.connect(self.pannel[0].pannel.ui.clb, QtCore.SIGNAL("clicked()"), self.AddTab)

    def AddTab(self):
        current_index = len(self.ui.tabWidget)

        self.pannel.append(tab_widget(communicationPannel, self))
        self.func_insert_tab(u'DataPort')

  # 프로그램을 닫으려 할때
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.warning(self,
            u'프로그램 종료', u"진행중인 모든 데이터 송·수신을 중지합니다.\n프로그램을 종료하시겠습니까?",
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
            QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        elif reply == QtGui.QMessageBox.No:
            event.ignore()

    def func_insert_tab(self, tab_name):
        """
        * 탭이 추가되면 항상 '새탭추가탭' 앞 쪽에 위치
        * 추가된 탭이 활성화
        """
        current_index = len(self.ui.tabWidget)
        self.ui.tabWidget.insertTab(current_index - 1, self.pannel[current_index], unicode(tab_name))
        self.ui.tabWidget.setCurrentIndex(current_index - 1)



    def slot_close_tab(self, tab_index):
        print tab_index

        if 1 == self.ui.tabWidget.count():
            # '새탭 추가탭'을 닫으려 할 경우
            return
        reply = QtGui.QMessageBox.warning(
            self,u'탭 닫기', u"저장하지 않은 작업 내용은 잃게됩니다.\n탭을 닫으시겠습니까?",
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
            QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.pannel.pop(tab_index + 1)
            self.ui.tabWidget.removeTab(tab_index)
        elif reply == QtGui.QMessageBox.No: pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = mainForm()
    myapp.show()
    sys.exit(app.exec_())
 
 
