'''
Created on 2018年4月30日

@author: Albert
'''
from RealTime.function import getMatch, getLastUpDn5



#取得報價資訊，詳情請查看技巧51
with open('function.py','r') as f:
    exec(f.read())

#定義指標變數
OutDesk=0
InDesk=0

#取得成交資訊
for i in getMatch():		
	MatchInfo=i.split(',')
	MatchTime=MatchInfo[0]
	MatchPrcie=int(MatchInfo[1])
	MatchQty=int(MatchInfo[2])
	#取得上下五檔價資訊
	UpDn5Info=getLastUpDn5()
	Dn1Price=int(UpDn5Info[1])
	Up1Price=int(UpDn5Info[11])

	#進行內外盤判斷
	if MatchPrcie>=Up1Price:
		OutDesk+=MatchQty
	if MatchPrcie<=Dn1Price:
		InDesk+=MatchQty

	#內外盤比率計算
	OutInRatio=float(OutDesk)/(OutDesk+InDesk)

	print( MatchTime,"OutDesk Ratio",OutInRatio)

