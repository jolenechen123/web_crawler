# 國軍高雄總醫院藥品查詢系統 動態爬蟲 (https://806.mnd.gov.tw/ph/Med_Web/)
from selenium import webdriver
import pandas as pd
from pyquery import PyQuery as pq
import requests
import datetime
import time
import random
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
engine = create_engine("mysql+pymysql://root:usbw@localhost:3307/test?charset=utf8")
con = engine.connect()

name_e_list = []
name_c_list = []
effect_list = []
dep_list = []
note_list = []
img_url_list = []

chrome_driver_path = "C:\\Users\\ASUS\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n = [104,69,108,47,42,51,35,26,23,6,33,68,69,45,19,55,3,36,87,57,20,32,8,8,5,17]
for b,i in zip(a,n):
    url = "https://806.mnd.gov.tw/ph/Med_Web/index.php?action=search&ABC={}&hash=c3cf3ed90bcbc2431f609de4b0658c82".format(b)
    driver.get(url)

    for x in range(1,i+1):
        clickk_xpath = "//table[@class='table table-bordered table-hover main']/tbody/tr[{}]/td[1]".format(x)
        clickk = driver.find_element_by_xpath(clickk_xpath)
        clickk.click()



        name_e_xpath = "//p[@id='engName']"
        name_e = driver.find_element_by_xpath(name_e_xpath)
        name_e = name_e.text
        name_e_list.append(name_e)
    #             print(name)

        name_c_xpath = "//p[@id='chName']"
        name_c = driver.find_element_by_xpath(name_c_xpath)
        name_c = name_c.text
        name_c_list.append(name_c)
    #             print(name)

        effect_xpath = "//p[@id='sideEffect']"
        effect = driver.find_element_by_xpath(effect_xpath)
        effect = effect.text
        effect_list.append(effect)

        dep_xpath = "//p[@id='weiFu']"
        dep = driver.find_element_by_xpath(dep_xpath)
        dep = dep.text
        dep_list.append(dep)

        note_xpath = "//p[@id='note']"
        note = driver.find_element_by_xpath(note_xpath)
        note = note.text
        note_list.append(note)



        img_xpath = "//img[@id='medicine']"
        img = driver.find_element_by_xpath(img_xpath)
    #             img_css = "div div div div+ div div div a img"
    #             html_doc = pq(book_url)
    #             img = html_doc(img_css)
        img_link = img.attr("src")
        img_url = "https://806.mnd.gov.tw/ph/Med_Web/" + img_link
        img_url_list.append(img_url)
    #             print(img_link)

        driver.back()

    driver.close()

df = pd.DataFrame()
df["藥品英文名"] = name_e_list
df["藥品中文名"] = name_c_list
df["可能副作用"] = effect_list
df["衛福部核准適應症"] = dep_list
df["注意事項"] = notes_list
df["圖片"] = img_url_list
df.to_sql(name='medicine', con=con, if_exists='append', index=False)
print("ok")

