# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui

from ui import Ui_Form

class protocolManager(QtGui.QWidget):
    def __init__(self, parent = None):
        super(protocolManager, self).__init__(parent) # __init__(parent)가 아니면 메인에서 본 위젯의 시그널을 받을 수 없음

        # 화면 구성
        self.ui = Ui_Form()
        self.ui.setupUi(self)



# 모듈 단독 실행 코드
if '__main__' == __name__:
    application = QtGui.QApplication(sys.argv)
    test = protocolManager()
    test.show()
    sys.exit(application.exec_())