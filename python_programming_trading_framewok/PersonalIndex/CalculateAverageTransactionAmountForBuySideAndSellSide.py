'''
Created on 2018年4月30日

@author: Albert
'''
from RealTime.function import getMatch



#取得報價資訊，詳情請查看技巧51
with open('function.py', 'r') as f:
    exec(f.read())

#取得成交資訊
for i in getMatch():		
    MatchInfo=i.split(',')
    MatchTime=MatchInfo[0]
    MatchAmount=int(MatchInfo[3])
    MatchBCnt=int(MatchInfo[4])
    MatchSCnt=int(MatchInfo[5])

	#進行平均買賣口計算
    avgB=float(MatchAmount)/MatchBCnt
    avgS=float(MatchAmount)/MatchSCnt
    print( MatchTime,"avgB",avgB,"avgS",avgS)
