#載入相關套件
import time
import tailer

#取得當天日期
#Date=time.strftime("%Y%m%d")
Date='20170815'

#設定檔案位置
DataPath="C:\\Users\\jay\\Desktop\\Futures\\TickData\\Futures_"

#開啟這三個檔案  020 Match, 030 Commission, 080 UpDn5
MatchFile=open(DataPath + Date + '_I020.csv')
OrderFile=open(DataPath + Date + '_I030.csv')
UpDn5File=open(DataPath + Date + '_I080.csv')

#持續取得成交資訊
def getMatch():
	return tailer.follow(MatchFile,0)

#持續取得委託資訊
def getOrder():
	return tailer.follow(OrderFile,0)

#持續取得上下五檔價資訊
def getUpDn5():
	return tailer.follow(UpDn5File,0)

#取得最新一筆成交資訊
def getLastMatch():
	return tailer.tail(MatchFile,3)[-2].split(",")

#取得最新一筆委託資訊
def getLastOrder():
	return tailer.tail(OrderFile,3)[-2].split(",")

#取得最新一筆上下五檔價資訊
def getLastUpDn5():
	return tailer.tail(UpDn5File,3)[-2].split(",")