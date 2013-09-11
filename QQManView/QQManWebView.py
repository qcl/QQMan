# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

from QQManTerminal import *

class QQManWebView(QWebView):

    def __init__(self,data,parent = None):
        super(QQManWebView,self).__init__(parent)

        self.__data = data
        self.setHtml(u"<html><body><h1>測試</h1></body><html>")

    def setWrite(self,write):
        self.__write = write

    def keyPressEvent(self,event):
        if self.__write != None:
            if len(event.text()) == 1:
                self.__write(str(event.text()))
            else:
                key = event.key()
                if key == Qt.Key_Left:
                    self.__write('\x1bOD')
                elif  key == Qt.Key_Right:
                    self.__write('\x1bOC')
                elif  key == Qt.Key_Up:
                    self.__write('\x1bOA')
                elif  key == Qt.Key_Down:
                    self.__write('\x1bOB')
                elif  key == Qt.Key_Backspace:
                    self.__write('\b')
                elif  key == Qt.Key_Return:
                    self.__write('\r')
                elif  key == Qt.Key_Enter:
                    self.__write('\r')
                elif  key == Qt.Key_Delete:
                    self.__write('\x1b[3~')
                elif  key == Qt.Key_Home:
                    self.__write('\x1b[1~')
                elif  key == Qt.Key_End:
                    self.__write('\x1b[4~')
                elif  key == Qt.Key_PageUp:
                    self.__write('\x1b[5~')
                elif  key == Qt.Key_PageDown:
                    self.__write('\x1b[6~')
                elif  key == Qt.Key_Tab:
                    self.__write('\t')
                elif  key == Qt.Key_Escape:
                    self.__write('\x1b')
        else:
            print 'No write function, please call setWrite function to set write function'

    
    def update(self):
        html = u'<html><body><pre>'
        skip = False
        for x in range(24):
            for y in range(80):
                if skip:
                    skip = False
                    continue
                word,is2B,color,background,lighting = self.__data.getWord(x,y).getWordForDrawing()
                
                if is2B:
                    skip = True
                    html = html + word

                else:
                    if len(word) == 0:
                        html = html + ' '
                    else:
                        html = html + word
                
            html = html + u'\r\n'
        html = html + u'</pre></body><html>'
        self.setHtml(html)
        
