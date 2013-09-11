# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#

from QQManBasicBig5Parser import QQManBasicBig5Parser
from QQManTerminal import *

class QQManBig5Parser(QQManBasicBig5Parser):

    def __init__(self,terminal,update):
        super(QQManBig5Parser,self).__init__()
        self.__term = terminal
        self.__update = update

    def start(self,szie):
        pass

    def onOneByteWord(self,word):
        self.__term.addOneByteWord(word)

    def onTwoBytesWord(self,word):
        self.__term.addTwoBytesWord(word)

    def onCtrlChar(self,ctrl,par):
        if ctrl == 109: #m
            if len(par) > 0 and par[0] == '[':
                par = par[1:]
                if len(par) == 0:
                    self.__term.reset()
                else:
                    par = par.split(';')
                    for n in par:
                        if len(n) > 0:
                            n = int(n)
                            if n == 0:
                                self.__term.reset()
                            elif n == 1:
                                self.__term.enableLighting()
                            elif n == 7:
                                self.__term.exchangeColor()
                            elif n >= 30 and n <= 37:
                                self.__term.setColor(n)
                            elif n >= 40 and n <= 47:
                                self.__term.setBackground(n)
                        else:
                            self.__term.reset()

        elif ctrl == 8:     #back
            # Move cursor back
            x,y = self.__term.getCursor()
            self.__term.setCursor(x,y-1)
            
        elif ctrl == 10:    #\n
            # Change line
            x,y = self.__term.getCursor()
            if x+1 >= 24:
                self.__term.moveUp()
            else:
                self.__term.setCursor(x+1,y)

        elif ctrl == 13:    #\r
            # Move cursor to start of line
            x,y = self.__term.getCursor()
            self.__term.setCursor(x,0)
            
        elif ctrl == 72 or ctrl == 102: # H or f
            # Set cursor
            if par[-1] == '[':
                self.__term.setCursor(0,0)
            else:
                par = par[1:]
                x = int(par[:par.index(';')]) - 1
                y = int(par[par.index(';')+1:]) - 1
                self.__term.setCursor(x,y)
        
        elif ctrl == 74:    # J
            # Clear to cursor
            x,y = self.__term.getCursor()
            par = par[-1]
            if par == '1':
                #erase from begging to cursor
                self.__term.clear((0,0),(x,y))
            elif par == '2':
                #erase whole
                self.__term.clear((0,0),(23,79))
                self.__term.setCursor(0,0)
            else:
                #erase from cursor to the end
                self.__term.clear((x,y),(23,79))
            
        elif ctrl == 75:    # K 
            # Clear line
            x,y = self.__term.getCursor()
            par = par[-1]
            if par == '1':
                #clear from head of line to cursor
                self.__term.clear((x,0),(x,y))
            elif par == '2':
                #clear whole line
                self.__term.clear((x,0),(x,79))
            else:
                #clear from the cursor to the end of line.
                self.__term.clear((x,y),(x,79))

        elif ctrl == 77:    # M
            # Move down
            x,y = self.__term.getCursor()
            self.__term.moveDown()
            self.__term.setCursor(x,0)

        else:
            # 65 A
            # 66 B
            # 67 C
            # 68 D
            # 69 E
            # 104 h
            # 108 l
            # 110 n
            # 115 s
            # 117 u
            pass

    def commit(self):
        self.__update()
