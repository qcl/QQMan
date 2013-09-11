# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#
# uging Big5-2003 http://moztw.org/docs/big5/table/big5_2003-b2u.txt

class ExtraBig5(object):

  def __init__(self):
    self.initB2U()
  
  def encode(self,unico):
    raise NotImplementedError('Please build big5 table')
  
  def decode(self,byte):
    raise NotImplementedError('Please build big5 table')
  
  def initB2U(self):
    raise NotImplementedError('Please build big5 table')

