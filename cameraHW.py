from selenium import webdriver
from pyquery import PyQuery as pq
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="usbw",
port = 3307,
database="test"

)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE test8 (title VARCHAR(255), reply int, writer VARCHAR(255),writer_date date,response VARCHAR(255),response_date date, title_url VARCHAR(255))")




camera_url = "https://www.mobile01.com/forumtopic.php?c=20&p=1"
html_doc = pq(camera_url)

for i in range(1,5):

    title_css = "tr:nth-child({}) .topic_top".format(i)
    reply_css = "tr:nth-child({}) td.reply".format(i)
    writer_css = "tr:nth-child({}) .authur p+ p".format(i)
    writer_date_css ="tr:nth-child({}) .authur p:nth-child(1)".format(i)
    response_css = "tr:nth-child({}) .latestreply p+ p".format(i)
    response_date_css ="tr:nth-child({}) .latestreply p:nth-child(1)".format(i)


    title = html_doc(title_css).text()
    reply = html_doc(reply_css).text()
    writer = html_doc(writer_css).text()
    writer_date = html_doc(writer_date_css).text()
    response = html_doc(response_css).text()
    response_date = html_doc(response_date_css).text()
    title_url = "https://www.mobile01.com/{}".format(html_doc(title_css).attr("href"))

    sql = "INSERT INTO test8 values ('"+title+"', '"+reply+"', '"+writer+"', '"+writer_date+"', '"+response+"', '"+response_date+"', '"+title_url+"')"
    mycursor.execute(sql)
    mydb.commit()

print("down_part1")

for i in range(5,35):
    title_css = "tr:nth-child({}) .topic_gen".format(i)
    reply_css = "tr:nth-child({}) .reply".format(i)
    writer_css = "tr:nth-child({}) .authur p+ p".format(i)
    writer_date_css ="tr:nth-child({}) .authur p:nth-child(1)".format(i)
    response_css = "tr:nth-child({}) .latestreply p+ p".format(i)
    response_date_css ="tr:nth-child({}) .latestreply p:nth-child(1)".format(i)

    title2 = html_doc(title_css).text()
    reply2 = html_doc(reply_css).text()
    writer2 = html_doc(writer_css).text()
    writer_date2 = html_doc(writer_date_css).text()
    response2 = html_doc(response_css).text()
    response_date2 = html_doc(response_date_css).text()
    title_url2 = "https://www.mobile01.com/{}".format(html_doc(title_css).attr("href"))

    sql2 = "INSERT INTO test8 values ('"+title2+"', '"+reply2+"', '"+writer2+"', '"+writer_date2+"', '"+response2+"', '"+response_date2+"', '"+title_url2+"')"
    mycursor.execute(sql2)
    mydb.commit()

print("down_part2")


for j in range(2,21): 
    camera_url_2 = "https://www.mobile01.com/forumtopic.php?c=20&p={}".format(j)    
    html_doc = pq(camera_url_2)

    for i in range(1,31):
        title_css = "tr:nth-child({}) .topic_gen".format(i)
        reply_css = "tr:nth-child({}) .reply".format(i)
        writer_css = "tr:nth-child({}) .authur p+ p".format(i)
        writer_date_css ="tr:nth-child({}) .authur p:nth-child(1)".format(i)
        response_css = "tr:nth-child({}) .latestreply p+ p".format(i)
        response_date_css ="tr:nth-child({}) .latestreply p:nth-child(1)".format(i)

        title3 = html_doc(title_css).text()
        reply3 = html_doc(reply_css).text()
        writer3 = html_doc(writer_css).text()
        writer_date3 = html_doc(writer_date_css).text()
        response3 = html_doc(response_css).text()
        response_date3 = html_doc(response_date_css).text()
        title_url3 = "https://www.mobile01.com/{}".format(html_doc(title_css).attr("href"))

        sql3 = "INSERT INTO test8 values ('"+title3+"', '"+reply3+"', '"+writer3+"', '"+writer_date3+"', '"+response3+"', '"+response_date3+"', '"+title_url3+"')"
        mycursor.execute(sql3)
        mydb.commit()

print("down_part3")