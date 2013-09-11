# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#

class QQManTermWord(object):

    __lighting = False

    __background = ''

    __color = ''

    __word = u''

    __isTwoBytes = False

    def __init__(self):
        self.reset()
        
    def reset(self):
        self.__background = '#000000'
        self.__color = '#C0C0C0'
        self.__lighting = False
        self.__word = u''
        self.__isTwoBytes = False

    def copy(self,termWord):
        self.__word,self.__isTwoBytes,self.__color,self.__background,self.__lighting = termWord.getWordForDrawing()

    def setWord(self,word,color='#C0C0C0',background='#000000',lighting = False):
        self.__word = word
        self.__background = background
        self.__color = color
        self.__lighting = False
        if ord(word) < 128:
            self.__isTwoBytes = False
        else:
            self.__isTwoBytes = True

    def setBackground(self,background):
        self.__background = background

    def setColor(self,color):
        self.__color = color

    def enableLighting(self,light):
        self.__lighting = light

    def getWord(self):
        return self.__word;

    # return word,is2B,color,bg,light
    def getWordForDrawing(self):
        return (self.__word,self.__isTwoBytes,self.__color,self.__background,self.__lighting)

    def getBackground(self):
        return self.__background

    def getColor(self):
        return self.__color

    def isLighting(self):
        return self.__lighting

    def isTwoBytes(self):
        return self.__isTwoBytes

