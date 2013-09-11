# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from QQManTerminal import *

class QQManFrameView(QFrame):

    __rectW = 0
    __rectH = 0

    __cellSize = 0
    __fontSize = 0

    __th = 0
    __tw = 0

    __ws = 0
    __hs = 0

    __write = None

    def __init__(self,data,parent = None):
        super(QQManFrameView,self).__init__(parent)

        self.__data = data

        self.initUI()

    def initUI(self):
        self.setStyleSheet('background:#000000')
        self.setFrameStyle(QFrame.Plain)

        self.setAttribute(Qt.WA_InputMethodEnabled,True)
        self.setFocus(Qt.ActiveWindowFocusReason)

    def paintEvent(self,event):
        
        rect = event.rect()
        rectW = rect.width()
        rectH = rect.height()

        if not rectW == self.__rectW or not rectH == self.__rectH:
            avgH = rectH/48
            avgW = rectW/80

            if avgH > avgW:
                self.__cellSize = avgW*2
            else:
                self.__cellSize = avgH*2

            fontSize = 1
            while True:
                tmpFont = QFont(u'文泉驛微米黑',fontSize)
                tmpFont.setPointSize(fontSize)
                fm = QFontMetricsF(tmpFont)
                pixW = fm.width('8')
                pixH = fm.height()
                if pixW >= self.__cellSize or pixH >= self.__cellSize:
                    break
                fontSize = fontSize + 1

            self.__fontSize = fontSize
            
            self.__th = self.__cellSize*24
            self.__tw = self.__cellSize*40
            self.__ws = (rectW - self.__tw)/2
            self.__hs = (rectH - self.__th)/2

        else:
            tmpFont = QFont(u'文泉驛微米黑',self.__fontSize)
            
        th = self.__th
        tw = self.__tw
        ws = self.__ws
        hs = self.__hs
        z  = self.__cellSize/2

        canvas = QPainter()
        canvas.begin(self)

        canvas.setFont(tmpFont)
        canvas.setBackgroundMode(Qt.OpaqueMode)

        skip = False
        for x in range(24):
            for y in range(80):

                # FIXME & TODO
                # using the dirty bit to reduce draw time
                # if self.__data.isDirty(x,y):
                #    self.__data.setClean(x,y)
                #else:
                #    continue

                if skip:
                    skip = False
                    continue

                word,is2B,color,background,lighting = self.__data.getWord(x,y).getWordForDrawing()

                canvas.setPen(QColor(background))
                canvas.setBrush(QColor(background))
                
                if is2B:
                    canvas.drawRect( ws + y*z,
                                     hs + x*z*2,
                                     2*z,
                                     2*z)
                    canvas.setPen(QColor(color))
                    canvas.setBackground(QColor(background))
                    canvas.drawText( ws + y*z,
                                     hs + x*z*2,
                                     2*z,
                                     2*z,
                                     Qt.AlignCenter,
                                     word)
                    skip = True
                else:
                    canvas.drawRect( ws + y*z,
                                     hs + x*z*2,
                                     z,
                                     2*z)
                    if len(word) > 0:
                        canvas.setPen(QColor(color))
                        canvas.setBackground(QColor(background))
                        canvas.drawText( ws + y*z,
                                         hs + x*z*2,
                                         z,
                                         2*z,
                                         Qt.AlignCenter,
                                         word)
        
        canvas.setPen(QColor('red'))
        canvas.setBrush(QColor('red'))
        x,y = self.__data.getCursor()
        canvas.drawLine( ws + y*z,
                         hs + x*z*2 + 2*z,
                         ws + y*z + z,
                         hs + x*z*2 + 2*z)
        canvas.end()

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

    def inputMethodEvent(self,event):
        # TODO
        # Chinese input
        pass

    def closeEvent(self,event):
        print 'close'
