#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
[reference code]（http://git.oschina.net/crossin/crossincode/blob/master/weather/weather.py）

'''
import json
import urllib2
import requests
city_name = raw_input("search: ")
url = "http://wthrcdn.etouch.cn/weather_mini?city=%s" % city_name
try:
    req =  requests.get(url)
    # print req.encoding # None
    # print req.text
    # print type(req.text) # unicode

    # with open("cityWeather.txt","a+") as cw:
    #     cw.write(req.text.encode("utf8")+"\n")
    # print req.json()
    # print type(req.json()) # dict type
    result_dict = req.json() #get dict object
    data = result_dict.get("data")
    today = data.get("forecast")[0]
    # print data.get("city")
    # print type(data.get("city"))
    print u"城市：" + data.get("city")
    print "今天天气："
    print u"最高温度：%s\t最低温度：%s\t风力：%s\t天气类型：%s" % (today.get("high"), today.get("low"), today.get("fengli"), today.get("type"))
except:
    print "fail to check the weather!"