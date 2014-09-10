# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from src.lib.serial_lib.serialHandler import SerialHandler

class serialReceiveThread(QtCore.QThread, SerialHandler):
    messageSignal = QtCore.pyqtSignal(str, int)
    commSignal = QtCore.pyqtSignal(str, int)


    def __init__(self, location, parent = None):
        super(serialReceiveThread, self).__init__(parent)
        SerialHandler.__init__(self)

        self.readSerialBuf = None
        self.location = location
        self.status = True

    def stop(self):
        self.status = False

    def resume(self):
        self.status = True

    def run(self):
        while True:
            if self.status is False:
                break

            self.readSerialBuf = self.readData(num= 1024)
            if not self.readSerialBuf:
                continue
            else:
                self.commSignal.emit(str(self.readSerialBuf), self.location)






if __name__ == '__main__':
    from src.widgets.communicationWidgets.communicaiotnSet import communicationSetWidget
    import sys

    def start():
        print 'aaa'

    app = QtGui.QApplication(sys.argv)
    setWidget = communicationSetWidget()
    setWidget.show()
    pb = QtGui.QPushButton(u'a')
    QtCore.QObject.connect(pb, QtCore.SIGNAL('clicked()'), start)
    pb.show()

    conf = setWidget.func_getValue()



    sys.exit(app.exec_())