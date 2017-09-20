#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 修改 Python 2.7.x 默认编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 导入模块
import re, time, urllib, urllib2

# User-Agent
Header = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

#
Basic_URL = 'http://dynamic.wallpaper.vip.xunlei.com/wallpaper_api/'
Parameter = {'req':'get_classify_image','offset':'0','classify_id':'2','sub_classify_id':'0','number':'100','resolution':'1920x1080','refer':'client_1.0.3.72'}
Classify_ID_List = {'热门':'1' ,'美女':'2' ,'明星':'3' ,'影视':'4' ,'动漫':'5' ,'创意':'6' ,'炫简':'7' ,'游戏':'8' ,'汽车':'9' ,'体育':'10','会员':'11','军事':'12','风景':'13','花卉':'15'}

for Classify_Type, Classify_ID in Classify_ID_List.items():
    Parameter['classify_id'] = Classify_ID
    Data = urllib.urlencode(Parameter)
    URL = Basic_URL + '?' + Data
    try:
        Request = urllib2.Request(URL, headers = Header)
        Response = urllib2.urlopen(Request)
        Content = Response.read().decode('utf-8')
        Pattern = re.compile('{"rtn":.*?,"total":"(.*?)"', re.S)
        Items = re.findall(Pattern, Content)
        for Item in Items:
            Total = int(Item.encode('utf-8'))
        Page = Total / 100
        for i in range(0, (Page + 1)):
            Parameter['offset'] = i * 100
            Data = urllib.urlencode(Parameter)
            URL = Basic_URL + '?' + Data
            Request = urllib2.Request(URL, headers=Header)
            Response = urllib2.urlopen(Request)
            Content = Response.read().decode('utf-8')
            Pattern = re.compile('{.*?,"name":"(.*?)","url":"(.*?)"', re.S)
            Items = re.findall(Pattern, Content)
            for Item in Items:
                print Classify_Type, Item[1].replace('\\', '')
    except urllib2.URLError as Error:
        if hasattr(Error, 'code'):
            print(Error.code)
        if hasattr(Error, 'reason'):
            print(Error.reason)