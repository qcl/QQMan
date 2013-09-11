# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#

from QQManTermWord import QQManTermWord

class QQManTerminal(object):

    __lightingTable = {'#000000':'#808080',
                       '#800000':'#ff0000',
                       '#000080':'#0000ff',
                       '#008000':'#00ff00',
                       '#008080':'#00ffff',
                       '#800080':'#ff00ff',
                       '#808000':'#ffff00',
                       '#C0C0C0':'#ffffff'}

    __colorTable = { 30:'#000000',
                     31:'#800000',
                     32:'#008000',
                     33:'#808000',
                     34:'#000080',
                     35:'#800080',
                     36:'#008080',
                     37:'#C0C0C0'}

    __backgroundTable = { 40:'#000000',
                          41:'#800000',
                          42:'#008000',
                          43:'#808000',
                          44:'#000080',
                          45:'#800080',
                          46:'#008080',
                          47:'#C0C0C0'}

    __cursor = (0,0)

    __data = []

    __dirty = []

    __color = '#C0C0C0'

    __background = '#000000'

    __lighting = False

    def __cursorAddOne(self):
        x,y = self.__cursor
        self.__cursor = (x,y+1)

    def __cursorAddTwo(self):
        x,y = self.__cursor
        y = y + 2
        if y >= 80:
            x = x + 1
            y = 0
        if x >= 24:
            x = 0
        self.__cursor = (x,y)

    def __init__(self):
        self.__cursor = (0,0)

        for i in range(24):
            self.__data.append([])
            self.__dirty.append([])
            for j in range(80):
                self.__data[i].append(QQManTermWord())
                self.__dirty[i].append(False)

    def setCursor(self,x,y):
        self.__cursor = (x,y)

    def addOneByteWord(self,word):
        x,y = self.__cursor
        try:
            self.__data[x][y].setWord(word,self.__color,self.__background,self.__lighting)
            self.__dirty[x][y] = True
        except:
            pass

        # FIXME
        self.__cursorAddOne()

    def addTwoBytesWord(self,word):
        x,y = self.__cursor

        try:
            self.__data[x][y].setWord(word,self.__color,self.__background,self.__lighting)
            self.__dirty[x][y] = True
            self.__dirty[x][y+1] = True
        except:
            pass

        # FIXME
        self.__cursorAddTwo()

    def clear(self,From,To):
        fx,fy = From
        tx,ty = To
        
        if fx == tx:
            for j in range(fy,ty+1):
                self.__data[fx][j].reset()
                self.__dirty[fx][j] = True
        else:
            for j in range(fy,80):
                self.__data[fx][j].reset()
                self.__dirty[fx][j] = True
            for i in range(fx+1,tx):
                for j in range(80):
                    self.__data[i][j].reset()
                    self.__dirty[i][j] = True
            for j in range(0,ty+1):
                self.__data[tx][j].reset()
                self.__dirty[tx][j] = True

    def setColor(self,colorCode):
        if self.__lighting:
            self.__color = self.__lightingTable[self.__colorTable[colorCode]]
        else:
            self.__color = self.__colorTable[colorCode]

    def setBackground(self,bgc):
        self.__background = self.__backgroundTable[bgc]

    def enableLighting(self):
        if not self.__lighting:
            self.__lighting = True
            self.__color = self.__lightingTable[self.__color]

    def exchangeColor(self):
        tmp = self.__color
        self.__color = self.__background
        self.__background = tmp
    
    def reset(self):
        self.__color = '#C0C0C0'
        self.__background = '#000000'
        self.__lighting = False

    def moveUp(self):
        for i in range(23):
            for j in range(80):
                self.__data[i][j].copy(self.__data[i+1][j])
                self.__dirty[i][j] = True

    def moveDown(self):
        for i in range(23):
            for j in range(80):
                self.__data[23-i][j].copy(self.__data[22-i][j])
                self.__dirty[23-i][j] = True
        self.clear((0,0),(0,79))

    def getCursor(self):
        return self.__cursor

    def getWord(self,x,y):
        return self.__data[x][y]

    def isDirty(self,x,y):
        return self.__dirty[x][y]

    def setClean(self,x,y):
        self.__dirty[x][y] = False
