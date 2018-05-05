'''
Created on 2018年4月30日

@author: Albert
'''
from RealTime.function import getOrder



#取得報價資訊，詳情請查看技巧51
with open('function.py','r') as f:
	exec(f.read())

#定義指標變數
lastOrderBAmount=0
lastOrderSAmount=0

#取得委託資訊
for i in getOrder():		
	OrderInfo=i.split(',')
	OrderTime=OrderInfo[0]
	OrderBAmount=int(OrderInfo[2])
	OrderSAmount=int(OrderInfo[4])

	#紀錄上一筆總量資訊
	if lastOrderBAmount==0 and lastOrderSAmount==0:
		lastOrderBAmount=OrderBAmount
		lastOrderSAmount=OrderSAmount
		continue
	else:
		#進行計算差值	
		diffOrderBAmount=OrderBAmount-lastOrderBAmount
		diffOrderSAmount=OrderSAmount-lastOrderSAmount
		lastOrderBAmount=OrderBAmount
		lastOrderSAmount=OrderSAmount

	print( OrderTime,"diffOrderBAmount",diffOrderBAmount,"diffOrderSAmount",diffOrderSAmount)

