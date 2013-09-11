# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#
from QQManView import *
from QQManTerminal import *
from QQManParser import *
from QQManConnect import *

class QQManBuilder(object):

    __data = None
    __view = None
    __parser = None
    __socket = None

    def __init__(self):
        pass
    
    def setData(self,term = None):
        if term == 'Terminal' or term == None:
            self.__data = QQManTerminal()
        else:
            self.__data = QQManTerminal()

    def setView(self,parent,view = None):
        if view == None or view == 'frame':
            self.__view = QQManFrameView(self.__data,parent)
        elif view == 'web':
            self.__view = QQManWebView(self.__data,parent)
        else:
            self.__view = QQManFrameView(self.__data,parent)

    def setParser(self,parser = None):
        if parser == None or parser == 'big5':
            self.__parser = QQManBig5Parser(self.__data,self.__view.update)
        else:
            self.__parser = QQManBig5Parser(self.__data,self.__view.update)

    def setConnection(self,host,port,connType = None):
        if connType == None or connType == 'telnet':
            self.__socket = QQManTelnetConnect(host,port,onRead=self.__parser.feed)
        elif connType == 'ssl' or connType == 'ssh':
            self.__socket = QQManSslConnect(host,port,onRead=self.__parser.feed)
        else:
            self.__socket = QQManTelnetConnect(host,port,onRead=self.__parser.feed)

    def getResult(self):
        self.__view.setWrite(self.__socket.write)
        return (self.__view,self.__socket)
