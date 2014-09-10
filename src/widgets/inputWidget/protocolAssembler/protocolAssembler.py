# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from ui import Ui_Form

class protocolAssembler(QtGui.QWidget):
    sendSignal = QtCore.pyqtSignal(str, int)

    def __init__(self, parent=None):
        super(protocolAssembler, self).__init__(parent)

        # 화면 구성
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def slot_hex_or_ascii(self, status):
        # Hex 또는 Ascii 콤보 박스
        data = ''
        if self.ui.cb_hex_ascii.currentIndex() == 0:
            data = str(self.ui.le_data.text().toLatin1()).encode('hex')
        else:
            try:
                data = str(self.ui.le_data.text().toLatin1()).decode('hex')
            except Exception as detail:
                print detail

        self.ui.le_data.setText(data)

    def get_assembled_data(self):
        # 프로토콜란에 입력된 데이터를 하나의 문자열로 취합
        status = self.ui.cb_hex_ascii.currentIndex()
        head1 = '' + str(self.ui.le_header_1.text()).decode('hex')
        head2 = '' + str(self.ui.le_header_2.text()).decode('hex')

        if 0 == status:         # HEX 상태일 경우
            protocol = '' + str(self.ui.le_data.text()).decode('hex')
        else:
            protocol = '' + str(self.ui.le_data.text().toLatin1())

        tail1 = '' + str(self.ui.le_tail_1.text()).decode('hex')
        tail2 = '' + str(self.ui.le_tail_2.text()).decode('hex')

        data = '' + head1 + head2 + protocol + tail1 + tail2

        if __package__ is None:
            print data

        return data

    def slot_no_item(self):
        self.ui.le_header_1.setText('')
        self.ui.le_header_2.setText('')
        self.ui.le_tail_1.setText('')
        self.ui.le_tail_2.setText('')

    def slot_cr(self):
        self.ui.le_header_1.setText('')
        self.ui.le_header_2.setText('')
        self.ui.le_tail_1.setText('')
        self.ui.le_tail_2.setText('0d')

    def slot_lf(self):
        self.ui.le_header_1.setText('')
        self.ui.le_header_2.setText('')
        self.ui.le_tail_1.setText('')
        self.ui.le_tail_2.setText('0a')

    def slot_crlf(self):
        self.ui.le_header_1.setText('')
        self.ui.le_header_2.setText('')
        self.ui.le_tail_1.setText('')
        self.ui.le_tail_2.setText('0d0a')

    def slot_stx_etx_crlf(self):
        self.ui.le_header_1.setText('02')
        self.ui.le_header_2.setText('')
        self.ui.le_tail_1.setText('03')
        self.ui.le_tail_2.setText('0d0a')

if '__main__' == __name__:
    application = QtGui.QApplication(sys.argv)
    test = protocolAssembler()
    pb = QtGui.QPushButton('get data')
    pb.connect(pb, QtCore.SIGNAL("clicked()"), test.get_assembled_data)
    pb.show()

    test.show()

    sys.exit(application.exec_())