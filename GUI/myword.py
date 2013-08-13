#coding:utf-8

# 使用 from 模块 import 类名 : 此方式的使用方法 dic = QQDICT()
from model.QQDICT import QQDICT
# 使用 import 模块 : 此方式的使用方法 dic =  model.QQDICT.QQDICT()
# import model.QQDICT 
# 使用 import 模块 as 缩略名: 此方式的使用方法 dic =  qd.QQDICT()
# import model.QQDICT as qd

dic = qd.QQDICT()
word = dic.getMeaning("run")
print word.word
print word.pron
for means in word.meaning:
    print means

