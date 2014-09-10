# -*- coding: utf-8  -*-

import sys, time

from PyQt4 import QtGui, QtCore

from ui import Ui_displayPannel

class displayDataPannel(QtGui.QWidget):
    def __init__(self, parent = None):
        super(displayDataPannel, self).__init__(parent) # __init__(parent)가 아니면 메인에서 본 위젯의 시그널을 받을 수 없음

        # 화면 구성
        self.ui = Ui_displayPannel()
        self.ui.setupUi(self)

    def showData(self, text, destination):
        dataLen = ''
        timeStamp = ''

        text = (str(text.toUtf8()).decode("utf-8")).encode('latin-1') # QString을 str 타입으로 변환


        # 옵션 검사
        if self.ui.chkb_timeStamp.isChecked() is True:
            # 타임 스탬프가 Checked 상태라면,
            timeStamp = '' + time.strftime('%Y-%m-%d %H:%M:%S')

        if self.ui.chkb_dataLength.isChecked() is True:
            # 데이터 길이가 Checked 상태라면,
            dataLen = '' + str(len(text)) + ' Byte(s) '


        # Hex 값 표출 창
        buf = dataLen + timeStamp + '\n' + \
              text.encode('hex') + '\n'

        if destination == 0:    # 송신
            self.ui.te_recvHex.moveCursor(QtGui.QTextCursor.End)
            self.ui.te_recvHex.insertPlainText(buf)
            self.ui.te_recvHex.moveCursor(QtGui.QTextCursor.End)
        else:                   # 수신
            self.ui.te_sendHex.moveCursor(QtGui.QTextCursor.End)
            self.ui.te_sendHex.insertPlainText(buf)
            self.ui.te_sendHex.moveCursor(QtGui.QTextCursor.End)

        # Ascii 값 표출 창
        buf = dataLen + timeStamp + '\n' + text + '\n'

        if destination == 0:
            self.ui.te_recvAscii.moveCursor(QtGui.QTextCursor.End)
            self.ui.te_recvAscii.insertPlainText(buf)
            self.ui.te_recvAscii.moveCursor(QtGui.QTextCursor.End)
        else:
            self.ui.te_sendAscii.moveCursor(QtGui.QTextCursor.End)
            self.ui.te_sendAscii.insertPlainText(buf)
            self.ui.te_sendAscii.moveCursor(QtGui.QTextCursor.End)



# 모듈 단독 실행 코드
if '__main__' == __name__:
    application = QtGui.QApplication(sys.argv)
    test = displayDataPannel()
    test.show()
    sys.exit(application.exec_())