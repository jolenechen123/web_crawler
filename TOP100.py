import pandas as pd
# %matplotlib inline
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
engine = create_engine("mysql+pymysql://root:usbw@localhost:3307/test?charset=utf8")
con = engine.connect()

url = "https://tw.money.yahoo.com/fund/ranklist"
df = pd.read_html(url)[1]
# df.head()
df_topStock = df.iloc[2:,3:13]
for x in range(7,13):
    df_topStock[x]= df_topStock[x].str.replace(r"\ue007  ","")
    df_topStock[x]= df_topStock[x].str.replace(r"\ue00a  ","-")
df_topStock['基金名稱']='nan'
df_topStock['更新日期']='nan'
df_topStock['淨值']='nan'
df_topStock['幣別']='nan'
df_topStock['1週']='nan'
df_topStock['1個月']='nan'
df_topStock['3個月']='nan'
df_topStock['1年']='nan'
df_topStock['3年']='nan'
df_topStock['5年']='nan'

df_topStock['基金名稱']=df_topStock[3]
df_topStock['更新日期']=df_topStock[4]
df_topStock['淨值']=df_topStock[5]
df_topStock['幣別']=df_topStock[6]
df_topStock['1週']=df_topStock[7]
df_topStock['1個月']=df_topStock[8]
df_topStock['3個月']=df_topStock[9]
df_topStock['1年']=df_topStock[10]
df_topStock['3年']=df_topStock[11]
df_topStock['5年']=df_topStock[12]

df_topStock = df_topStock.iloc[0:,10:]

df_topStock.to_sql(name='top100', con=con, if_exists='append', index=False)
