#HK
import pymysql
from pyquery import PyQuery as pq

hk_url = "https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/foreign-exchange-rates"
html_doc = pq(hk_url)

money_css = ".tableContent-light:nth-child(5) .lastTd"  
time_css = "#LbQuoteTime"

time = html_doc(time_css).text() 
money = html_doc(money_css).text()

db = pymysql.connect("localhost","jocelyn","123456","jocelyn",charset="utf8")
cursor = db.cursor()
sql = "INSERT INTO HKD VALUES ('HKD','"+money+"','"+time+"')"
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()