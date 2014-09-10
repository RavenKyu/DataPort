# coding: utf-8
import serial
from sys import platform as _platform
class SerialHandler():
    def __init__(self):
        self.osType = _platform
        self.ser = serial.Serial()

    def func_close(self):
        try:
            self.ser.close()
        except:
            pass

    def isOpen(self):
        return self.ser.isOpen()

    def convertSerSetting(self, serSetting):
        # 리눅스용

        if "linux" == self.osType:
            serSetting['comPort'] = str('' + '/dev/ttyS' + serSetting['comPort'][3:]) # Comport 설정
        elif "win32" == self.osType:
            serSetting['comPort'] = str('' + 'com' + serSetting['comPort'][3:]) # Comport 설정

        if 'NONE' == serSetting['parityBit']: # Parity Bit 설정
            serSetting['parityBit'] = 'N'
        elif 'ODD' == serSetting['parityBit']:
            serSetting['parityBit'] = 'O'
        elif 'EVEN' == serSetting['parityBit']:
            serSetting['parityBit'] = 'E'

        serSetting['dataBit'] = int(serSetting['dataBit'])

        return serSetting

    # 사용 가능한 시리얼 포트 검색
    def searchAvailableComport(self):
        availableComport = []

        if "linux" == self.osType:
            for i in range(255):
                try:
                    self.ser = serial.Serial('/dev/ttyS' + str(i))
                except:
                    pass
                else:
                    availableComport.append(i)
                    self.ser.close()

        elif "win32" == self.osType:
            for i in range(255):
                try:
                    self.ser = serial.Serial('com' + str(i))
                except:
                    pass
                else:
                    availableComport.append(i)
                    self.ser.close()
        return availableComport

    def func_setConf(self, serSetting):
        self.port = serSetting['comPort']
        self.baudrate = serSetting['baudrate']
        self.bytesize = serSetting['dataBit']
        self.parity = serSetting['parityBit']
        self.stopbits = serSetting['stopBit']
        self.timeout = 0.1


    def func_connect(self):
        try:
            self.ser = serial.Serial(port = self.port,
                                     baudrate = self.baudrate,
                                     bytesize = self.bytesize,
                                     parity = self.parity,
                                     stopbits = self.stopbits,
                                     timeout = self.timeout)
        except Exception as detail:
            print detail
            return False
        else:
            if True is self.ser.isOpen():
                return True

    def sendData(self, data):
        self.ser.write(data)

    def readData(self, num = 1):
        return self.ser.read(num)

    def readSerialStream(self, head, tail, bufferSize, act):
        readBuffer = ''
        tempBuff = ''

        if 'HEAD_TO_TAIL' == act:
            for i in range(bufferSize):
                tempBuff = self.ser.read(1)

                if tempBuff is not None:
                    readBuffer = readBuffer + tempBuff

                if readBuffer[0] == chr(head):
                    if readBuffer[-1] == chr(tail):
                        return readBuffer

        if 'TAIL_AND_TAIL' == act:
            for i in range(bufferSize):

                tempBuff = self.ser.read(1)
                if tempBuff is not None:
                    readBuffer = readBuffer + tempBuff

                if len(readBuffer) >= 2 and readBuffer[-2] == chr(head):
                    if readBuffer[-1] == chr(tail):
                        return readBuffer

        return None