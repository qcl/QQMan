# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#

from QQManParser import QQManParser
from extraBig5_0xF9D6_0xFEFE import ExtraBig5_0xF9D6_0xFEFE
from extraBig5_0x8140_0xA0FE import ExtraBig5_0x8140_0xA0FE
from extraBig5_0xC940_0xF9D5 import ExtraBig5_0xC940_0xF9D5
from extraBig5_0xC6A1_0xC8FE import ExtraBig5_0xC6A1_0xC8FE

class QQManBasicBig5Parser(QQManParser):

    def __init__(self):
        self.extraTable = ExtraBig5_0xF9D6_0xFEFE(ExtraBig5_0x8140_0xA0FE(ExtraBig5_0xC940_0xF9D5(ExtraBig5_0xC6A1_0xC8FE())))

    def feed(self,big5str):
       
        # Remove FF FD 00 (Do binary transmission)
        while True:
            try:
                x = big5str.index('\xff\xfd\x00')
            except:
                break
            
            if x < len(big5str):
                pass
                big5str = big5str[:x]+big5str[x+2:]
            else:
                break
       
        self.start(len(big5str))

        # Parsing
        
        is2B = False        # Flag of 2 bytes word
        byteBuf = ''        # Buffer for 1st char in 2 bytes word
        
        isCtrl = False      # Flag of control char
        ctrlBuf = ''        # Control char buffer

        for byte in big5str:
            ascii_num = ord(byte)

            if isCtrl:

                if ascii_num in [65,66,67,68,69,72,74,75,77,102,104,108,109,110,115,117]:
                    isCtrl = False
                    self.onCtrlChar(ascii_num,ctrlBuf)
                    ctrlBuf = ''
                    pass
                else:
                    ctrlBuf = ctrlBuf + byte
                    pass

                continue
            
            if ascii_num == 27: #Control Char
                isCtrl = True
                continue

            if is2B:
                word = '%s%s' % (byteBuf,byte)

                #Chain of Responsibility
                try:
                    word = word.decode('big5')
                except:
                    word = '%02X%02X' % (ord(byteBuf),ascii_num)
                    word = self.extraTable.decode(word)
                    if len(word)==0:
                        word = unichr(0x25A1)
                        # print '%02X%02X' % (ord(byteBuf),ascii_num)

                self.onTwoBytesWord(word)
                is2B = False
            else:
                if ascii_num < 128:
                    if ascii_num in [8,10,13]:
                        self.onCtrlChar(ascii_num,'')
                    elif ascii_num > 31 and ascii_num < 127:
                        self.onOneByteWord(byte)
                    else:
                        pass
        
                else:   #Big5 word
                    # 1st char in a 2 bytes word
                    is2B = True
                    byteBuf = byte
        
        # After reading all data in this `feed'
        # call commit as a notification
        self.commit()

    # On Parsing One Byte Word
    def onOneByteWord(self,word):
        raise NotImplementedError("Please impliment onOneByteWord in subclass")

    def onTwoBytesWord(self,word):
        raise NotImplementedError("Please impliment onTwoBytesWord in subclass")

    def onCtrlChar(self,ctrl,par=None):
        raise NotImplementedError("Please impliment onCtrlChar in subclass")

    def start(self,size):
        raise NotImplementedError("Please impliment start in subslass")

    def commit(self):
        raise NotImplementedError("Please impliment commit in subslass")
