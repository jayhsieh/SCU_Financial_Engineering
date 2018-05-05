'''
Created on 2018年4月30日

@author: Albert
'''
from RealTime.function import getOrder



#取得報價資訊，詳情請查看技巧51
with open('function.py','r') as f:
    exec(f.read())

#取得委託資訊
for i in getOrder():		
	OrderInfo=i.split(',')
	OrderTime=OrderInfo[0]
	OrderBCnt=int(OrderInfo[1])
	OrderBAmount=int(OrderInfo[2])
	OrderSCnt=int(OrderInfo[3])
	OrderSAmount=int(OrderInfo[4])

	#委託平均口數計算，並顯示
	print( OrderTime,"avgOrderB",float(OrderBAmount)/OrderBCnt,"avgOrderS",float(OrderSAmount)/OrderSCnt)

