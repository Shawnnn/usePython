#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
问题：10/16/2017 保存的图片gif无法打开,jpg是条纹的？ bs时候有误？编码问题？
解决：10/17/2017 编码问题：保存时候用了"w"，应该用"wb"
'''
import requests
import bs4
import thread

#爬虫抓取函数
def spider(page,url_list):
    path = "pics/" # this folder needs to be created in advance
    for url in url_list:
        response = requests.get("http:"+ url)
        pic_name = url.split("/")[-1]
        with open(path + pic_name, "wb" ) as f:
            f.write(response.content)
        print "saving picture {}...".format(pic_name)
    print "done with page {}".format(page)
    if page == max_page:
        print "done with web scraping!"

#设置边界：最小和最大页数
min_page = 1
max_page = 141
print "min_page is "+str(min_page)+";max_page is "+str(max_page)
min_page = input("请输入起始页：")
max_page = input("请输入终止页：")

# 顺序打开页面
for page in range(min_page, max_page+1):
    url = "http://jandan.net/pic/page-{}#comments".format(page)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    response = requests.get(url,headers=headers)

    #用beautiful soup 解析出所需的url
    bs_html = bs4.BeautifulSoup(response.text, "html.parser")
    pic_list = bs_html.find_all("a", "view_img_link" )
    url_list= [l.get("href") for l in pic_list]

    #使用多线程，以及调用爬虫函数
    thread.start_new_thread(spider, (page, url_list))

while 1:
    pass
