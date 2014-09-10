# coding: utf-8
from socket import *
from sys import platform as _platform

class TCPHandler():
    def __init__(self):
        self.osType = _platform
  
    def tcpConnect(self, serSetting):
        try:
            self.ser = socket(AF_INET, SOCK_STREAM)
            self.ser.connect((str(serSetting['IP']),
                         serSetting['Port'])
            )       
        except:
            print 'Failed'
            return False
        else:
            # if True is self.ser.isOpen():
            #     print 'TCP is connected.'
                # return True
            return True
 
    def isOpen(self):
        # return self.ser.isOpen()
        return True


    def writeData(self, data):
        self.ser.send(data)

    def readData(self, num = 1):
        return self.ser.recv(num)

    def readSerailStream(self, head, tail, bufferSize, act):
        readBuffer = ''
        tempBuff = ''
        
        if 'HEAD_TO_TAIL' == act:
            for i in range(bufferSize):
                tempBuff = self.ser.recv(1)

                if tempBuff is not None:
                    readBuffer = readBuffer + tempBuff

                if readBuffer[0] == chr(head):
                    if readBuffer[-1] == chr(tail):
                        return readBuffer

        if 'TAIL_AND_TAIL' == act:
            for i in range(bufferSize):

                tempBuff = self.ser.recv(1)
                if tempBuff is not None:
                    readBuffer = readBuffer + tempBuff

                if len(readBuffer) >= 2 and readBuffer[-2] == chr(head):
                    if readBuffer[-1] == chr(tail):
                        return readBuffer
            
        return None

