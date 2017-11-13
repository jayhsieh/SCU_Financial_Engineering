

import pymongo
from pymongo  import MongoClient
import pprint
import operator
import psycopg2
import folium
import os
import json
import numpy as np
import pandas as pd
import sys 



print("請輸入id:",sys.argv[1])
id=sys.argv[1]




def Set():
    global client,db,collection,conn,cursor,m
    client = MongoClient('172.27.110.106', 27017)
    db = client['jackdb']
    collection=db['daily_report']
    conn = psycopg2.connect(host='172.27.110.104',port='5432', database='equity', user='quant', password='quant')
    cursor = conn.cursor()
    m = folium.Map(location=[23.8, 121.2], width='100%', height='100%', zoom_start=8)




def get_dict(icode,date):
    idict={}
    last_icode=""
    total_bs=0
    for aa in collection.find({"日期":date,"id":icode}):
        #pprint.pprint(aa)
        icode=aa['劵商分支']
        net_bs=int(aa['買進股數'])-int(aa['賣出股數'])
        if icode==last_icode or last_icode=="":
            total_bs+=net_bs
        else:
            idict[last_icode]=total_bs
            total_bs=net_bs
        last_icode=icode        
    return idict





def get_location(id):
    global date
    date=collection.distinct("日期",{"id":id})[-12:]
    ans=get_dict(id,date[-1])
    global sorted_idict_dsec,sorted_idict_asc
    sorted_idict_dsec = sorted(ans.items(), key=operator.itemgetter(1), reverse=True)[0:10]
    sorted_idict_asc = sorted(ans.items(), key=operator.itemgetter(1), reverse=False)[0:10]



def get_time_seris(id,location):
    #time_seris
    time_seris=np.zeros(len(date))
    for i in range(0,len(date),1):
        #print(i)
        days=date[i]
        totol_bs=0
        for aa in collection.find({"日期":days,"id":id,"劵商分支":location}):
            #aa['日期']=is_same_day
            net_bs=int(aa['買進股數'])-int(aa['賣出股數'])
            totol_bs+=net_bs
            #print(totol_bs)
        time_seris[i]=totol_bs
       # print(time_seris[i])
    
    return time_seris




# modify json
def modify_json(id,location,color1,rank):
    time_series=get_time_seris(id,location)
    f=open("D:\\專案-非爬蟲\\台灣經緯度\\vis.json", 'r',encoding='cp950')  
    jsonobj=json.load(f)
    jsonobj['axes'][1]["title"]=""
    n=len(jsonobj['data'][0]['values'])
    for i in range(0,n,1):
        jsonobj['data'][0]['values'][i]['val']=time_series[i]/1000
    conn_str="select 劵商分支,緯度,經度 from 劵商分支代碼 where 代碼='" + location + "'"
    a=pd.read_sql(conn_str,conn)
    jsonobj['axes'][0]["title"]=a.loc[0,'劵商分支']+color1.replace('red',' 買超排名 ').replace('green',' 賣超排名 ')+''+rank

#地圖
    folium.Marker(
        location=[a.loc[0,'緯度'],a.loc[0,'經度']],
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega((jsonobj), width=450, height=250)),icon=folium.Icon(color=color1, icon='info-sign')).add_to(m)



def main(id):
    Set()
    #id="8299"
    get_location(id)
    n=len(sorted_idict_dsec)
    for i in range(0,n,1):
        modify_json(id,sorted_idict_dsec[i][0],'red',str(i+1))
        modify_json(id,sorted_idict_asc[i][0],'green',str(i+1))
    m.save('D:\\專案-非爬蟲\\台灣經緯度\\'+date[-1].replace('/','')+'_'+id+'.html')



if len(sys.argv) < 2: #len小於2也就是不帶參數啦
    print("no argument")
    sys.exit()
elif len(sys.argv)==2:
    main(id)

