import datetime
import pandas as pd
# %matplotlib inline
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
engine = create_engine("mysql+pymysql://root:usbw@localhost:3307/test?charset=utf8")
# engine = create_engine("mysql+pymysql://jocelyn:123456@datapool.zapto.org:3306/jocelyn?charset=utf8")
con = engine.connect()

today = datetime.date.today()
url = "https://tw.stock.yahoo.com/s/list2.php?c=%B6%B3%BA%DD%AC%DB%C3%F6&rr=0.51292600%201536566161"
df = pd.read_html(url,encoding='big5hkscs')[6]
df[6]= df[6].str.replace(r"△","")
df[6]= df[6].str.replace(r"▽","-")
df_stock = df.iloc[1:,1:12]

df_stock['股票代號']='nan'
df_stock['股票名稱']='nan'
df_stock['日期']='nan'
df_stock['時間']='nan'
df_stock['成交']='nan'
df_stock['買進']='nan'
df_stock['賣出']='nan'
df_stock['漲跌']='nan'
df_stock['張數']='nan'
df_stock['昨收']='nan'
df_stock['開盤']='nan'
df_stock['最高']='nan'
df_stock['最低']='nan'

df_stock['股票代號']=df_stock[1].str.split(' ').str[0] 
df_stock['股票名稱']=df_stock[1].str.split(' ').str[1]
df_stock['日期']= today
df_stock['時間']= df_stock[2]
df_stock['成交']= df_stock[3]
df_stock['買進']= df_stock[4]
df_stock['賣出']= df_stock[5]
df_stock['漲跌']= df_stock[6]
df_stock['張數']= df_stock[7]
df_stock['昨收']= df_stock[8]
df_stock['開盤']= df_stock[9]
df_stock['最高']= df_stock[10]
df_stock['最低']= df_stock[11]
df_stock2 = df_stock.iloc[1:,11:]
df_stock2.head(10)

df_stock2.to_sql(name='cloud_stock77', con=con, if_exists='append', index=False)