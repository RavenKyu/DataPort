# coding: utf-8
# XML을 이용한 프로토콜 저장 및 로드 
import json
import os

class ProtocolHandler():
    def __init__(self):
        self.fileFd = None
        self.protocolData = {'Protocol' : []}
        
    def __del__(self):
        if self.fileFd is not None:
            self.write()

    def isOpenFile(self):
        if file != self.fileFd.__class__:
            print type(self.fileFd)
            return False
        else:
            return True

    def createFile(self, fileName):
        try:
            self.fileFd = open(fileName, 'w+')
        except IOError:
            return False
        else:        
            return True

    def openFile(self, fileName):
        try:
            self.fileFd = open(fileName, 'r+')
        except IOError:
            return False
        else:        
            return True

    def addProtocol(self, name, head1, head2, protocol, tail1, tail2):
        self.protocolData['Protocol'].append(
                {
                    'Name' : str(name), 
                    'Head1' : str(head1), 'Head2' : str(head2), 
                    'Protocol' : str(protocol), 
                    'Tail1' : str(tail1), 'Tail2' : str(tail2) 
                }
        )

    def delProtocol(self, index):
        self.protocolData['Protocol'].pop(index)
        self.fileTruncate()
        json.dumps(self.protocolData, indent=4)
        return

    def getProtocol(self):
        return json.loads(json.dumps(self.protocolData))

    def write(self):
        data = json.dumps(self.protocolData, indent=4)
        self.fileFd.seek(0)
        self.fileFd.write(data)
        return

    def open(self):
        data = self.fileFd.read()
        self.protocolData = json.loads(data)
        return

    def fileTruncate(self):
        self.fileFd.seek(0, 0)  # 파일 끝으로 이동
        self.fileFd.truncate(self.fileFd.tell()) # 파일 크기만큼 지움 
