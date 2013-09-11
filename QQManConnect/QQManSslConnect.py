# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#

from QQManConnect import QQManConnect
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *

class QQManSslConnect(QQManConnect):
    
    def __onRead(self):
        byte = self.__socket.bytesAvailable()
        data = self.__socket.read(byte)
        self.__read(data)
    
    def __onDisconnect(self):
        self.__disconnect()
        self.__socket.close()

    def __defaultRead(data):
        print data
    
    def __defaultDisconnect():
        print 'disconnect'

    def __init__(self,host,port,onRead=__defaultRead,onDisconnect=__defaultDisconnect):
        self.__host = host
        self.__port = port

        self.__read = onRead
        self.__disconnect = onDisconnect

        self.__socket = QSslSocket()
        QObject.connect(self.__socket,SIGNAL('readyRead()'),self.__onRead)
        QObject.connect(self.__socket,SIGNAL('disconnected()'),self.__onDisconnect)

    def connect(self):
        self.__socket.connectToHost(self.__host,self.__port)

    def disconnect(self):
        self.__socket.close()

    def write(self,data):
        self.__socket.write(data)
