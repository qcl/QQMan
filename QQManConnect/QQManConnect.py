# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#

class QQManConnect(object):

    def __init__(self,host,port):
        self.__host = host
        self.__port = port

    def connect(self):
        raise NotImplementedError("Please impliment connect") 

    def disconnect(self):
        raise NotImplementedError("Please impliment disconnect")

    def getHost(self):
        return self.__host

    def getPort(self):
        return self.__port

    def write(self,data):
        raise NotImplementedError("Please impliment write")

