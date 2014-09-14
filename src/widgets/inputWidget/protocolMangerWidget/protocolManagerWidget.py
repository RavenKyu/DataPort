# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui, QtCore
from src.widgets.inputWidget.protocolMangerWidget.ui import Ui_Form
from src.lib.file_lib.protocolHandle import ProtocolHandler

class protocolManager(QtGui.QWidget):
    def __init__(self, parent=None):
        """ __init__(parent)가 아니면 메인에서 본 위젯의 시그널을 받을 수 없음 """
        super(protocolManager, self).__init__(parent)

        # 화면 구성
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.handler = None
        self.protocol_handler = ProtocolHandler()

        self.file_name = None
        self.selected_protocol = None

    def set_handler(self, handler):
        self.handler = handler

    def slot_save(self):
        prt = self.handler.get_protocol()
        # 프로토콜 이름이 있는지 검사
        # 이름이 없으면 그냥 무시
        if '' == self.ui.le_protocol_name.text():
            return

        # 열려있는 매크로 파일이 있는지 검사
        if self.protocol_handler.isOpenFile() is False:
            self.file_name = unicode(QtGui.QFileDialog.getSaveFileName(None, u'프로토콜 파일 생성', '.prt'))
            self.protocol_handler.createFile(self.file_name)

        self.protocol_handler.addProtocol(
            unicode(self.ui.le_protocol_name.text()),
            prt['head1'], prt['head2'],
            prt['data'],
            prt['tail1'], prt['tail2']
        )

        self.reflash_item_list()
        self.ui.le_protocol_name.setText('') # 프로토콜 이름란을 비움
        self.selected_protocol = self.protocol_handler.getProtocol() # 목록을 다시 읽어옴
        selected_list = len(self.selected_protocol['protocol']) - 1
        self.slot_set_selected_protocol(selected_list) # 추가된 마지막 프로토콜 표시, 배열 시작은 0부터 시작이라서 - 1
        self.ui.cb_protocol_list.setCurrentIndex(selected_list)


    def slot_set_selected_protocol(self, index_number):
        # 선택된 프로토콜 목록의 내용을 입력란에 표시
        self.handler.ui.le_header_1.setText(str(self.selected_protocol['protocol'][index_number]['head1']))
        self.handler.ui.le_header_2.setText(str(self.selected_protocol['protocol'][index_number]['head2']))

        if self.handler.ui.cb_hex_ascii.currentIndex() == 0:
            self.handler.ui.le_data.setText(self.selected_protocol['protocol'][index_number]['data'])
        else:
            self.handler.ui.le_data.setText(self.selected_protocol['protocol'][index_number]['data'].decode('hex'))

        self.handler.ui.le_tail_1.setText(str(self.selected_protocol['protocol'][index_number]['tail1']))
        self.handler.ui.le_tail_2.setText(str(self.selected_protocol['protocol'][index_number]['tail2']))

    def reflash_item_list(self):
        # 목록 비우기
        count_index_num = self.ui.cb_protocol_list.count()
        if 0 != count_index_num:
            for i in range(count_index_num):
                self.ui.cb_protocol_list.removeItem(0)

        # 목록 채우기
        # JSON으로 저장된 프로토콜 저장파일을 읽어와서,
        # 순서대로 목록에 추가
        self.selected_protocol = self.protocol_handler.getProtocol()
        for i in range(len(self.selected_protocol['protocol'])):
            self.ui.cb_protocol_list.insertItem(
                i,
                self.selected_protocol['protocol'][i]['name'], ''
            )


    def slot_load(self):
        # 프로토콜 파일에서 읽어오기
        self.file_name = unicode(QtGui.QFileDialog.getOpenFileName(None, '프로토콜 파일 불러오기', '.prt'))
        if self.file_name == '':
            return

        self.protocol_handler.openFile(self.file_name)
        self.protocol_handler.open()
        self.reflash_item_list()

    def slot_del(self):
        # 프로토콜 삭제
        self.protocol_handler.delProtocol(self.ui.cb_protocol_list.currentIndex())
        self.reflash_item_list()

    def slot_show_dial(self):
        pass

# 모듈 단독 실행 코드
if '__main__' == __name__:
    application = QtGui.QApplication(sys.argv)
    from src.widgets.inputWidget.protocolAssembler.protocolAssembler import protocolAssembler
    prt_manager = protocolAssembler()
    test = protocolManager()
    test.set_handler(prt_manager)
    test.show()
    sys.exit(application.exec_())