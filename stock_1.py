from pyquery import PyQuery as pq
from selenium import webdriver
import pandas as pd
import datetime

stock_url = "https://tw.stock.yahoo.com/s/list2.php?c=%B6%B3%BA%DD%AC%DB%C3%F6&rr=0.51292600%201536566161"
html_doc = pq(stock_url)
      
title_list = []
title_url_list = []

time_css = ".yui-text-left td:nth-child(3)"
transaction_css = "b"
buy_css = ".yui-text-left td:nth-child(5)"
sell_css = ".yui-text-left td:nth-child(6)"
up_down_css = ".yui-text-left table table font"
number_css = ".yui-text-left td:nth-child(8)"
Yesterday_css = ".yui-text-left td:nth-child(9)"
opening_css = ".yui-text-left td:nth-child(10)"
high_css = "td:nth-child(11)"
low_css = "td:nth-child(12)"


# title = [t.text for t in html_doc(title_css)]
today = datetime.date.today()
time = [ti.text for ti in html_doc(time_css)]
transaction = [tr.text for tr in html_doc(transaction_css)]
buy = [b.text for b in html_doc(buy_css)]
sell = [s.text for s in html_doc(sell_css)]
up_down = [ud.text for ud in html_doc(up_down_css)]
number = [nu.text for nu in html_doc(number_css)]
Yesterday = [yes.text for yes in html_doc(Yesterday_css)]
opening = [op.text for op in html_doc(opening_css)]
high = [hi.text for hi in html_doc(high_css)]
low = [lo.text for lo in html_doc(low_css)]


title_css_1 = ".yui-text-left table tr:nth-child(2) a"
title_1 = html_doc(title_css_1).text()
title_list.append(title_1)
title_url_1 ="https://tw.stock.yahoo.com{}".format(html_doc(title_css_1).attr("href"))
title_url_list.append(title_url_1)

title_css_2 = ".yui-text-left table tr:nth-child(3) a"
title_2 = html_doc(title_css_2).text()
title_list.append(title_2)
title_url_2 ="https://tw.stock.yahoo.com{}".format(html_doc(title_css_2).attr("href"))
title_url_list.append(title_url_2)

for i in range(4,65):
    title_css_3 = "tr:nth-child({}) a".format(i)
    title_3 = html_doc(title_css_3).text()
    title_list.append(title_3)
    title_url_3 ="https://tw.stock.yahoo.com{}".format(html_doc(title_css_3).attr("href"))
    title_url_list.append(title_url_3)

df = pd.DataFrame()
df["title"] = title_list
df["date"] = today
df["time"] = time
df["transaction"] = transaction
df["buy"] = buy
df["sell"] = sell
df["up_down"] = up_down
df["number"] = number
df["Yesterday"] = Yesterday
df["opening"] = opening
df["high"] = high
df["low"] = low
df["title_url"] = title_url_list
df.to_csv("stock.csv", index=False)
