# coding: utf-8
# TCP/IP socket, client Handler

from PyQt4 import QtCore, QtGui, QtNetwork

class server(QtNetwork.QTcpServer):
    messageSignal = QtCore.pyqtSignal(str, int)
    commSignal = QtCore.pyqtSignal(str, int)

    def __init__(self, parent= None):
        super(server, self).__init__()

        QtCore.QObject.connect(self, QtCore.SIGNAL("newConnection()"),
                     self.sig_newConnection)

        self.connection = []


    # 소켓 설정 메소드
    def func_setConf(self, host, port, id):
        self.host = host
        if self.host is '': self.host = QtNetwork.QHostAddress.Any # 아이피를 적지 않으면 모든 곳에서 데이터를 다 받을 수 있다

        self.port = port
        self.id = id

    def func_start(self):
        return self.func_connect()

    def isOpen(self):
        return self.isListening()

    def start(self):
        return self.func_connect()

    def resume(self):
        pass

    def func_connect(self):
        retStatus = False
        if self.listen(QtNetwork.QHostAddress(self.host), self.port):
            if __package__ == None : print 'server is awake :: %s:%s' % (str(self.host), str(self.port))
            else:
                try:
                    self.messageSignal.emit(u'TCP/IP 서버를 열었습니다. :: %s:%s' % (str(self.host), str(self.serverPort())), self.id)
                except:
                    pass
                retStatus = True
        else:
            if __package__ == None : print "server couldn't wake up"
            else:
                try:
                    self.messageSignal.emit(u'TCP/IP 서버 생성을 실패하였습니다.', self.id)
                except:
                    pass
                retStatus = False
        return retStatus

    def send_data(self, text):
        for s in self.connection:
            s.write(str(text))

    def stop(self):
        self.close()
    def func_close(self):
        self.close()

    def sig_newConnection(self):
        clientConnection = self.nextPendingConnection()
        clientConnection.nextBlockSize = 0
        self.connection.append(clientConnection) # 동시 접속용
        if __package__ == None : print "connection %d" % len(self.connection)

        self.connect(clientConnection, QtCore.SIGNAL("readyRead()"),
                     self.sig_readReady)
        self.connect(clientConnection, QtCore.SIGNAL("disconnected()"),
                     self.removeConnection)
        self.connect(clientConnection, QtCore.SIGNAL("error()"),
                     self.socketError)


    def sig_readReady(self):
        if __package__ is None: print 'read to read'
        for s in self.connection:
            if s.bytesAvailable() > 0:
                self.recvBuf = ''
                self.recvBuf = s.readAll()
                self.commSignal.emit(str(QtCore.QString(self.recvBuf).toLatin1()), self.id)
                if __package__ == None: print 'server received : ', self.recvBuf
                if __package__ == None : print "connection %d" % len(self.connection)



    # 연결이 끊어진 소켓을 찾아서 삭제
    def removeConnection(self):
        for i in self.connection:
            if -1 == i.socketDescriptor():
                self.connection.remove(i)

    def socketError(self):
        pass



class socket(QtNetwork.QTcpSocket):
    messageSignal = QtCore.pyqtSignal(str, int)
    commSignal = QtCore.pyqtSignal(str, int)

    def __init__(self, parent = None):
        super(socket, self).__init__()

        self.setSocketOption(QtNetwork.QTcpSocket.KeepAliveOption, QtCore.QVariant(1))

        # 시그널 설정
        self.connected.connect(self.sig_connected)
        self.disconnected.connect(self.sig_disconnected)
        self.error.connect(self.sig_error)
        self.readyRead.connect(self.sig_readyRead)



    def func_start(self):
        self.start()

    def resume(self):
        pass

    def start(self):
        self.messageSignal.emit(u'접속 테스트', self.id)
        self.func_connect()
        # self.func_close()




    # 소켓 설정 메소드
    def func_setConf(self, host, port, id, reconnect= True, protocol=u'단순 전달', loggerId='000000'):
        self.host = host
        self.port = port
        self.id = id
        self.reconnect = reconnect
        self.protocol = protocol
        self.loggerId = loggerId


    def func_connect(self):
        if __package__ is None: # 단독 실행 모드 디버그
            print 'Connect to %s:%s' % (self.host, self.port)
        self.messageSignal.emit(u'%s:%s 에 연결하는중...' % (str(self.host), int(self.port)), self.id)

        QtNetwork.QTcpSocket.abort(self)
        QtNetwork.QTcpSocket.connectToHost(self, self.host, self.port)
        QtNetwork.QTcpSocket.waitForConnected(self)
        if self.state() != QtNetwork.QAbstractSocket.ConnectedState:
            self.messageSignal.emit(u'서버와의 접속이 연결되지 않았습니다..', self.id)
            return False
        else:
            self.messageSignal.emit(u'서버와 접속되었습니다.', self.id)
            return True

    def isOpen(self):
        if self.state() == QtNetwork.QAbstractSocket.ConnectedState: return True
        else: return False


    def stop(self):
        if self.state() != QtNetwork.QAbstractSocket.ConnectedState: return False
        self.disconnectFromHost()
        if self.state() >= QtNetwork.QAbstractSocket.ConnectedState:
            self.waitForDisconnected()
            self.disconnected()




    def func_close(self):
        self.stop()

    def send_data(self, data):
        if self.state() != QtNetwork.QAbstractSocket.ConnectedState:
            self.func_connect()

        if self.state() < QtNetwork.QAbstractSocket.ConnectingState:
            self.func_close()
            self.messageSignal.emit(u'서버와의 접속이 끊어져 있습니다..', self.id)
            if __package__ is None: print 'disconnected on server.. : %d' % self.state()
            return

        elif self.state() == QtNetwork.QAbstractSocket.ConnectingState:
            self.messageSignal.emit(u'서버와의 접속 시도중..', self.id)

        elif self.state() == QtNetwork.QAbstractSocket.ConnectedState:
            self.writeData(data)
            # self.commSignal.emit(data, 0)
            if __package__ is None: print data




    def sig_readyRead(self):
        if __package__ is None: print 'read to read'
        if self.bytesAvailable():
            self.recvBuf = ''
            self.recvBuf = self.readAll()
            self.commSignal.emit(str(QtCore.QString(self.recvBuf).toLatin1()), 1)
            if __package__ is None: print self.recvBuf


    def sig_connected(self):
        if __package__ is None: print 'connected'

    def sig_disconnected(self): # 접속이 끊어지면 연결이 될 때까지 지속적으로 연결을 시도 한다.
        # QtCore.QMetaObject.invokeMethod(self, 'func_reconnect',  QtCore.Qt.QueuedConnection)
        if __package__ is None: print 'disconnected'

    def sig_error(self):
        # QtCore.QMetaObject.invokeMethod(self, 'func_reconnect',  QtCore.Qt.QueuedConnection)
        if __package__ is None: print 'error'

    @QtCore.pyqtSlot()
    def func_reconnect(self):
        if self.reconnect is not True:
            return
        self.messageSignal.emit(u'서버에 재 접속중입니다.', self.id)
        self.func_connect()



if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    inputBox = QtGui.QWidget()
    lineEdit = QtGui.QLineEdit(inputBox)
    submitButton = QtGui.QPushButton(u'send',inputBox)

    hBox = QtGui.QHBoxLayout()
    hBox.addWidget(lineEdit)
    hBox.addWidget(submitButton)
    inputBox.setLayout(hBox)

    inputBox.show()





    testSocket = socket()
    testSocket.func_setConf('127.0.0.1', 2007, 0)
    testSocket.func_connect()
    # testSocket2 = socket()
    # testSocket2.func_setConf('127.0.0.1', 2000, 0)
    # testSocket.func_connect()
    # testSocket2.func_connect()


    # testServer = server()
    # testServer.func_setConf('127.0.0.1',2002,1)
    # testServer.func_connect()

    # data1 ='01'.decode('hex') + '255008x1001,01MN,201408061659,2790, 790, 790,   0,   0,   0,10583, -999, -999,   1,    1,  10, 3560,  24,  28,2397,2397, 154,    0x3d' + '04'.decode('hex')
    # data2 ='01'.decode('hex') + '255009x1001,01MN,201408061659,2790, 790, 790,   0,   0,   0,10583, -999, -999,   1,    1,  10, 3560,  24,  28,2397,2397, 154,    0x3d' + '04'.decode('hex')
    def test():
        text = lineEdit.text()

        testSocket.writeData(text)


    QtCore.QObject.connect(submitButton,QtCore.SIGNAL('clicked()'),test)
    sys.exit(app.exec_())