# -*- coding: utf-8 -*-
# NTU CSIE Design Pattern Final Project - QQMan
# Group 10
# B97501046 & B98902018
#
# uging Big5-2003 http://moztw.org/docs/big5/table/big5_2003-b2u.txt

from extraBig5 import ExtraBig5

class ExtraBig5_0xC6A1_0xC8FE(ExtraBig5):

  table_u2b = {}
  table = {}
  Next = None

  def __init__(self,theNext=None):
    super(ExtraBig5_0xC6A1_0xC8FE,self).__init__()
    if not theNext == None:
      self.Next = theNext
  
  # encode function
  # input: unicode char
  # return: a value of input char in big5 encoding 
  def encode(self,unico):
    s = '%04X' % unico
    # FIXME
    b = '0x%s' % self.table_u2b[s]
    return int(b,16)
    
  # decode function
  # input: 2 bytes data
  # return: a unicode char
  def decode(self,byte):
    try:
      return unichr(self.table[byte])
    except:
      if self.Next == None:
        return unichr(0x25A1)
      else:
        return self.Next.decode(byte)
  
  
  # init table
  def initB2U(self):
    self.table['C6A1'] = 0x2460
    self.table['C6A2'] = 0x2461
    self.table['C6A3'] = 0x2462
    self.table['C6A4'] = 0x2463
    self.table['C6A5'] = 0x2464
    self.table['C6A6'] = 0x2465
    self.table['C6A7'] = 0x2466
    self.table['C6A8'] = 0x2467
    self.table['C6A9'] = 0x2468
    self.table['C6AA'] = 0x2469
    self.table['C6AB'] = 0x2474
    self.table['C6AC'] = 0x2475
    self.table['C6AD'] = 0x2476
    self.table['C6AE'] = 0x2477
    self.table['C6AF'] = 0x2478
    self.table['C6B0'] = 0x2479
    self.table['C6B1'] = 0x247A
    self.table['C6B2'] = 0x247B
    self.table['C6B3'] = 0x247C
    self.table['C6B4'] = 0x247D
    self.table['C6B5'] = 0x2170
    self.table['C6B6'] = 0x2171
    self.table['C6B7'] = 0x2172
    self.table['C6B8'] = 0x2173
    self.table['C6B9'] = 0x2174
    self.table['C6BA'] = 0x2175
    self.table['C6BB'] = 0x2176
    self.table['C6BC'] = 0x2177
    self.table['C6BD'] = 0x2178
    self.table['C6BE'] = 0x2179
    self.table['C6BF'] = 0x2F02
    self.table['C6C0'] = 0x2F03
    self.table['C6C1'] = 0x2F05
    self.table['C6C2'] = 0x2F07
    self.table['C6C3'] = 0x2F0C
    self.table['C6C4'] = 0x2F0D
    self.table['C6C5'] = 0x2F0E
    self.table['C6C6'] = 0x2F13
    self.table['C6C7'] = 0x2F16
    self.table['C6C8'] = 0x2F19
    self.table['C6C9'] = 0x2F1B
    self.table['C6CA'] = 0x2F22
    self.table['C6CB'] = 0x2F27
    self.table['C6CC'] = 0x2F2E
    self.table['C6CD'] = 0x2F33
    self.table['C6CE'] = 0x2F34
    self.table['C6CF'] = 0x2F35
    self.table['C6D0'] = 0x2F39
    self.table['C6D1'] = 0x2F3A
    self.table['C6D2'] = 0x2F41
    self.table['C6D3'] = 0x2F46
    self.table['C6D4'] = 0x2F67
    self.table['C6D5'] = 0x2F68
    self.table['C6D6'] = 0x2FA1
    self.table['C6D7'] = 0x2FAA
    self.table['C6D8'] = 0x00A8
    self.table['C6D9'] = 0xFF3E
    self.table['C6DA'] = 0x30FD
    self.table['C6DB'] = 0x30FE
    self.table['C6DC'] = 0x309D
    self.table['C6DD'] = 0x309E
    self.table['C6E0'] = 0x3005
    self.table['C6E1'] = 0x3006
    self.table['C6E2'] = 0x3007
    self.table['C6E3'] = 0x30FC
    self.table['C6E4'] = 0xFF3B
    self.table['C6E5'] = 0xFF3D
    self.table['C6E6'] = 0x273D
    self.table['C6E7'] = 0x3041
    self.table['C6E8'] = 0x3042
    self.table['C6E9'] = 0x3043
    self.table['C6EA'] = 0x3044
    self.table['C6EB'] = 0x3045
    self.table['C6EC'] = 0x3046
    self.table['C6ED'] = 0x3047
    self.table['C6EE'] = 0x3048
    self.table['C6EF'] = 0x3049
    self.table['C6F0'] = 0x304A
    self.table['C6F1'] = 0x304B
    self.table['C6F2'] = 0x304C
    self.table['C6F3'] = 0x304D
    self.table['C6F4'] = 0x304E
    self.table['C6F5'] = 0x304F
    self.table['C6F6'] = 0x3050
    self.table['C6F7'] = 0x3051
    self.table['C6F8'] = 0x3052
    self.table['C6F9'] = 0x3053
    self.table['C6FA'] = 0x3054
    self.table['C6FB'] = 0x3055
    self.table['C6FC'] = 0x3056
    self.table['C6FD'] = 0x3057
    self.table['C6FE'] = 0x3058
    self.table['C740'] = 0x3059
    self.table['C741'] = 0x305A
    self.table['C742'] = 0x305B
    self.table['C743'] = 0x305C
    self.table['C744'] = 0x305D
    self.table['C745'] = 0x305E
    self.table['C746'] = 0x305F
    self.table['C747'] = 0x3060
    self.table['C748'] = 0x3061
    self.table['C749'] = 0x3062
    self.table['C74A'] = 0x3063
    self.table['C74B'] = 0x3064
    self.table['C74C'] = 0x3065
    self.table['C74D'] = 0x3066
    self.table['C74E'] = 0x3067
    self.table['C74F'] = 0x3068
    self.table['C750'] = 0x3069
    self.table['C751'] = 0x306A
    self.table['C752'] = 0x306B
    self.table['C753'] = 0x306C
    self.table['C754'] = 0x306D
    self.table['C755'] = 0x306E
    self.table['C756'] = 0x306F
    self.table['C757'] = 0x3070
    self.table['C758'] = 0x3071
    self.table['C759'] = 0x3072
    self.table['C75A'] = 0x3073
    self.table['C75B'] = 0x3074
    self.table['C75C'] = 0x3075
    self.table['C75D'] = 0x3076
    self.table['C75E'] = 0x3077
    self.table['C75F'] = 0x3078
    self.table['C760'] = 0x3079
    self.table['C761'] = 0x307A
    self.table['C762'] = 0x307B
    self.table['C763'] = 0x307C
    self.table['C764'] = 0x307D
    self.table['C765'] = 0x307E
    self.table['C766'] = 0x307F
    self.table['C767'] = 0x3080
    self.table['C768'] = 0x3081
    self.table['C769'] = 0x3082
    self.table['C76A'] = 0x3083
    self.table['C76B'] = 0x3084
    self.table['C76C'] = 0x3085
    self.table['C76D'] = 0x3086
    self.table['C76E'] = 0x3087
    self.table['C76F'] = 0x3088
    self.table['C770'] = 0x3089
    self.table['C771'] = 0x308A
    self.table['C772'] = 0x308B
    self.table['C773'] = 0x308C
    self.table['C774'] = 0x308D
    self.table['C775'] = 0x308E
    self.table['C776'] = 0x308F
    self.table['C777'] = 0x3090
    self.table['C778'] = 0x3091
    self.table['C779'] = 0x3092
    self.table['C77A'] = 0x3093
    self.table['C77B'] = 0x30A1
    self.table['C77C'] = 0x30A2
    self.table['C77D'] = 0x30A3
    self.table['C77E'] = 0x30A4
    self.table['C7A1'] = 0x30A5
    self.table['C7A2'] = 0x30A6
    self.table['C7A3'] = 0x30A7
    self.table['C7A4'] = 0x30A8
    self.table['C7A5'] = 0x30A9
    self.table['C7A6'] = 0x30AA
    self.table['C7A7'] = 0x30AB
    self.table['C7A8'] = 0x30AC
    self.table['C7A9'] = 0x30AD
    self.table['C7AA'] = 0x30AE
    self.table['C7AB'] = 0x30AF
    self.table['C7AC'] = 0x30B0
    self.table['C7AD'] = 0x30B1
    self.table['C7AE'] = 0x30B2
    self.table['C7AF'] = 0x30B3
    self.table['C7B0'] = 0x30B4
    self.table['C7B1'] = 0x30B5
    self.table['C7B2'] = 0x30B6
    self.table['C7B3'] = 0x30B7
    self.table['C7B4'] = 0x30B8
    self.table['C7B5'] = 0x30B9
    self.table['C7B6'] = 0x30BA
    self.table['C7B7'] = 0x30BB
    self.table['C7B8'] = 0x30BC
    self.table['C7B9'] = 0x30BD
    self.table['C7BA'] = 0x30BE
    self.table['C7BB'] = 0x30BF
    self.table['C7BC'] = 0x30C0
    self.table['C7BD'] = 0x30C1
    self.table['C7BE'] = 0x30C2
    self.table['C7BF'] = 0x30C3
    self.table['C7C0'] = 0x30C4
    self.table['C7C1'] = 0x30C5
    self.table['C7C2'] = 0x30C6
    self.table['C7C3'] = 0x30C7
    self.table['C7C4'] = 0x30C8
    self.table['C7C5'] = 0x30C9
    self.table['C7C6'] = 0x30CA
    self.table['C7C7'] = 0x30CB
    self.table['C7C8'] = 0x30CC
    self.table['C7C9'] = 0x30CD
    self.table['C7CA'] = 0x30CE
    self.table['C7CB'] = 0x30CF
    self.table['C7CC'] = 0x30D0
    self.table['C7CD'] = 0x30D1
    self.table['C7CE'] = 0x30D2
    self.table['C7CF'] = 0x30D3
    self.table['C7D0'] = 0x30D4
    self.table['C7D1'] = 0x30D5
    self.table['C7D2'] = 0x30D6
    self.table['C7D3'] = 0x30D7
    self.table['C7D4'] = 0x30D8
    self.table['C7D5'] = 0x30D9
    self.table['C7D6'] = 0x30DA
    self.table['C7D7'] = 0x30DB
    self.table['C7D8'] = 0x30DC
    self.table['C7D9'] = 0x30DD
    self.table['C7DA'] = 0x30DE
    self.table['C7DB'] = 0x30DF
    self.table['C7DC'] = 0x30E0
    self.table['C7DD'] = 0x30E1
    self.table['C7DE'] = 0x30E2
    self.table['C7DF'] = 0x30E3
    self.table['C7E0'] = 0x30E4
    self.table['C7E1'] = 0x30E5
    self.table['C7E2'] = 0x30E6
    self.table['C7E3'] = 0x30E7
    self.table['C7E4'] = 0x30E8
    self.table['C7E5'] = 0x30E9
    self.table['C7E6'] = 0x30EA
    self.table['C7E7'] = 0x30EB
    self.table['C7E8'] = 0x30EC
    self.table['C7E9'] = 0x30ED
    self.table['C7EA'] = 0x30EE
    self.table['C7EB'] = 0x30EF
    self.table['C7EC'] = 0x30F0
    self.table['C7ED'] = 0x30F1
    self.table['C7EE'] = 0x30F2
    self.table['C7EF'] = 0x30F3
    self.table['C7F0'] = 0x30F4
    self.table['C7F1'] = 0x30F5
    self.table['C7F2'] = 0x30F6
    
    for x in self.table:
      s = '%04X' % self.table[x]
      self.table_u2b[s] = x
    


