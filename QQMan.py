# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from QQManView import *
from QQManTerminal import *
from QQManParser import *
from QQManConnect import *

from QQManBuilder import QQManBuilder

import sys

class QQMan(QMainWindow):

    __view = None
    __socket = None
    __builder = None

    def __init__(self,parent=None):
        super(QQMan,self).__init__(parent)
        self.initUI()
        self.__builder = QQManBuilder()

    def initUI(self):
        self.setWindowTitle('QQMan 0.2.1 (alpha)')
        self.setGeometry(500,200,700,500)
        
        #self.__inputLabel = QLabel(u'',self)

        self.__btn = QPushButton(self)
        self.__btn.setText(u'連線')
        
        self.__labelC = QLabel(u'連線方式',self)
        self.__cmboC = QComboBox(self)
        self.__cmboC.insertItem(1,'telnet')
        self.__cmboC.insertItem(2,'ssl')
       
        self.__labelD = QLabel(u'顯示方式',self)
        self.__cmboD = QComboBox(self)
        self.__cmboD.insertItem(1,'frame')
        self.__cmboD.insertItem(2,'web')

        self.__labelHost = QLabel(u'站台',self)
        self.__hostLine = QLineEdit(self)

        self.__labelPort = QLabel(u'埠口',self)
        self.__portLine = QLineEdit('23',self)

        self.statusBar().showMessage('NTU CSIE Design Pattern Final Project')

        self.__btn.clicked.connect(self.onBtnClicked)

    def onBtnClicked(self):
        host = self.__hostLine.text()
        port = self.__portLine.text()
        conn = self.__cmboC.currentText()
        disp = self.__cmboD.currentText()

        if len(host) > 0 and len(port):
            port = int(port)

            if not self.__socket == None:
                self.__socket.disconnect()

            self.__builder.setData()
            self.__builder.setView(self,disp)
            self.__builder.setParser()
            self.__builder.setConnection(host,port)

            self.__view,self.__socket = self.__builder.getResult()
            self.__socket.connect()
            
            self.__view.setGeometry(10,45,self._w-20,self._h-70)
            self.__view.show()
            self.__view.setFocus()

    def resizeEvent(self,event):
        oldSize = event.oldSize()
        newSize = event.size()

        w = newSize.width()
        h = newSize.height()

        self._w = w
        self._h = h

        self.__labelC.setGeometry(10,10,60,25)
        self.__cmboC.setGeometry(70,10,80,25)

        self.__labelHost.setGeometry(160,10,30,25)
        self.__hostLine.setGeometry(190,10,w-(320+190),25)

        self.__labelPort.setGeometry(w-310,10,30,25)
        self.__portLine.setGeometry(w-280,10,40,25)

        self.__labelD.setGeometry(w-230,10,60,25)
        self.__cmboD.setGeometry(w-170,10,100,25)

        self.__btn.setGeometry(w-60,10,50,25)

        if not self.__view == None:
            self.__view.setGeometry(10,45,newSize.width()-20,newSize.height()-70)
        #self.__inputLabel.setGeometry(10,newSize.height()-10,newSize.width(),10)

    def closeEvent(self,event):
        print 'close'

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    qqman = QQMan()
    qqman.show()
    sys.exit(app.exec_())


