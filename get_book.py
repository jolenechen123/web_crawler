# 誠品書誠 動態網頁爬蟲 (http://www.eslite.com/newbook_list.aspx?cate=156&sub=221&list=231)
def get_book_info(url,page):
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

    discont_list = []
    name_list = []
    pub_list = []
    author_list = []
    date_list = []
    bind_list = []
    language_list = []
    price_list = []
    img_link_list = []
    book_url_list = []
    isbn_list = []
    store_list = []
    today_list = []

    chrome_driver_path = "C:\\Users\\ASUS\\Desktop\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
#     url = "http://www.eslite.com/newbook_list.aspx?cate=156&sub=221&list=231&page=2"
    for n in range(1,page):
        new_url = url + "&page={}".format(n)
        print(new_url)
        driver.get(new_url)

        for i in range(1,13):
            discont_xpath = "//div[@class='box_mid_billboard'][{}]/p[2]/span[@class='price_sale'][1]".format(i)
            discont = driver.find_element_by_xpath(discont_xpath)
            discont = discont.text
            discont_list.append(discont)
#             print(discont)

        nums = ["00","01","02","03","04","05","06","07","08","09","10","11"]
        for num in nums:
            #ctl01為例
            price_xpath = "//span[@id='ctl00_ContentPlaceHolder1_newbook_bookList_ctl{}_retailPrice']".format(num)
            price = driver.find_element_by_xpath(price_xpath)
            price = price.text
            price_list.append(price)
#             print(price)

            clickk_xpath = "//a[@id='ctl00_ContentPlaceHolder1_newbook_bookList_ctl{}_url2']".format(num)
            clickk = driver.find_element_by_xpath(clickk_xpath)
            clickk.click()

            book_url = driver.current_url
            book_url_list.append(book_url)
#             print(book_url)

            name_xpath = "//span[@id='ctl00_ContentPlaceHolder1_lblProductName']"
            name = driver.find_element_by_xpath(name_xpath)
            name = name.text
            name_list.append(name)
            print(name)

            author_xpath = "//h2[@class='PI_item']"
            author = driver.find_element_by_xpath(author_xpath)
            author = author.text
            author = author.replace("作者 ／ ","")
            author_list.append(author)
#             print(author)

            pub_xpath = "//h3[@class='PI_item'][1]"
            pub = driver.find_element_by_xpath(pub_xpath)
            pub = pub.text
            if "出版社 ／ " not in pub:
                pub = ""
            else:
                pub = pub.replace("出版社 ／ ","")
            pub_list.append(pub)
#             print(pub)

            date_xpath = "//h3[@class='PI_item'][2]"
            date = driver.find_element_by_xpath(date_xpath)
            date = date.text
            if "出版日期 ／ " not in date:
                date = ""
            else:
                date = date.replace("出版日期 ／ ","")
            date_list.append(date)
#             print(date)

            language_xpath = "//span[@id='ctl00_ContentPlaceHolder1_LiteralLanguage']"
            language = driver.find_element_by_xpath(language_xpath)
            language = language.text
            language_list.append(language)
#             print(language)

            bind_xpath = "//span[@id='ctl00_ContentPlaceHolder1_LiteralBind']"
            bind = driver.find_element_by_xpath(bind_xpath)
            bind = bind.text
            bind_list.append(bind)
#             print(bind)

            # img_xpath = "//img[@id='ctl00_ContentPlaceHolder1_mainphoto']/@src"
            # img = driver.find_element_by_xpath(img_xpath)
            img_css = "div div div div+ div div div a img"
            html_doc = pq(book_url)
            img = html_doc(img_css)
            img_link = img.attr("src")
            img_link_list.append(img_link)
#             print(img_link)

            isbn_xpath = "//div[@class='C_box'][5]/p[1]"
            isbn = driver.find_element_by_xpath(isbn_xpath)
            isbn = isbn.text
            isbn = isbn.replace("誠品26碼 ／","")
            isbn = isbn.replace("\nISBN 13 ／",",")
            isbn = isbn.replace("\nISBN 10 ／",",")
            isbn = isbn.replace("\nEAN ／",",")
            isbn_list.append(isbn)
#             print(isbn)

            store = "誠品"
            store_list.append(store)
#             print(store)

            today = datetime.date.today()
            today_list.append(today)
#             print(today)

            time.sleep(5)

            driver.back()

    driver.close()

    
    df = pd.DataFrame()
    df["書名"] = name_list
    df["作者"] = author_list
    df["折扣"] = discont_list
    df["出版社"] = pub_list
    df["出版日期"] = date_list
    df["裝訂"] = bind_list
    df["商品語言"] = language_list
    df["價格"] = price_list
    df["圖片"] = img_link_list
    df["商品連結"] = book_url_list
    df["抓取日期"] = today_list
    df["isbn"] = isbn_list
    df["書城"] = store_list
    df.to_sql(name='book_lan', con=con, if_exists='append', index=False)
    print("ok")
