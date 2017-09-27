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

Basic_URL = 'http://api.lovebizhi.com/windows_v3.php?client_id=1004&model_id=106&bizhi_width=1920&bizhi_height=1080'

# 推荐、热门下载、热门收藏
Type_List = {'推荐':'&a=home&p=', '热门下载':'&a=ranking&type=download&p=', '热门收藏':'&a=ranking&type=loved&p='}
for Type_Name, Type_Parameter in Type_List.items():
    Count = 1
    for Page in range(1, 21):
        URL = Basic_URL + Type_Parameter + str(Page)
        try:
            Request = urllib2.Request(URL, headers = Header)
            Response = urllib2.urlopen(Request)
            Content = Response.read().decode('utf-8')
            # Pattern = re.compile('{(.*?)"image":(.*?)"diy":"(.*?)"(.*?)"loved":"(.*?)"(.*?)"share":"(.*?)"(.*?)"down":"(.*?)"', re.S)
            Pattern = re.compile('{(.*?)"image":(.*?)"diy":"(.*?)"', re.S)
            Items = re.findall(Pattern, Content)
            for Item in Items:
                # print Type_Name + '第' + str(Count) + '张；' + '喜欢' + Item[4].encode('utf-8') + '；分享' + Item[6].encode('utf-8') + '；下载' + Item[8].encode('utf-8') + '；URL' + Item[2].replace('\\', '')
                print Type_Name + '第' + str(Count) + '张: ' + Item[2].replace('\\', '')
                Count += 1
        except urllib2.URLError as Error:
            if hasattr(Error, 'code'):
                print(Error.code)
            if hasattr(Error, 'reason'):
                print(Error.reason)

# 热门专题
Count = 1
for Page in range(1, 21):
    URL = Basic_URL + '&a=browse&id=special&p=' + str(Page)
    try:
        Request = urllib2.Request(URL, headers=Header)
        Response = urllib2.urlopen(Request)
        Content = Response.read().decode('utf-8')
        Pattern = re.compile('{(.*?)"name":"(.*?)"(.*?)"description":"(.*?)"(.*?)"detail":"(.*?)"', re.S)
        Items = re.findall(Pattern, Content)
        for Item in Items:
            print '专辑名称: ' + Item[1] + '\n' + '专辑说明: ' + Item[3] + '\n' + '专辑链接: ' + Item[5].replace('\\', '')
            for Page in range(1, 21):
                URL = Item[5].replace('\\', '') + '&p=' + str(Page)
                try:
                    Request = urllib2.Request(URL, headers=Header)
                    Response = urllib2.urlopen(Request)
                    Content = Response.read().decode('utf-8')
                    Pattern = re.compile('{(.*?)"image":(.*?)"diy":"(.*?)"', re.S)
                    Items_2 = re.findall(Pattern, Content)
                    for Item_2 in Items_2:
                        print '第' + str(Count) + '张: ' + Item_2[2].replace('\\', '')
                        Count += 1
                except urllib2.URLError as Error:
                    if hasattr(Error, 'code'):
                        print(Error.code)
                    if hasattr(Error, 'reason'):
                        print(Error.reason)
            print('#' * 32 + '分隔符' + '#' * 32)
    except urllib2.URLError as Error:
        if hasattr(Error, 'code'):
            print(Error.code)
        if hasattr(Error, 'reason'):
            print(Error.reason)

# 美图分类
URL = 'http://api.lovebizhi.com/windows_v3.php?client_id=1004&model_id=106&bizhi_width=1920&bizhi_height=1080&a=browse&id=category'
Count = 1
try:
    Request = urllib2.Request(URL, headers=Header)
    Response = urllib2.urlopen(Request)
    Content = Response.read().decode('utf-8')
    Pattern = re.compile('{(.*?)"name":"(.*?)"(.*?)"url":"(.*?)"', re.S)
    Items = re.findall(Pattern, Content)
    for Item in Items:
        print '分类名称: ' + Item[1] + '\n' + '分类链接: ' + Item[3].replace('\\', '')
        for Page in range(1, 21):
            URL = Item[3].replace('\\', '') + '&p=' + str(Page)
            try:
                Request = urllib2.Request(URL, headers=Header)
                Response = urllib2.urlopen(Request)
                Content = Response.read().decode('utf-8')
                Pattern = re.compile('{(.*?)"image":(.*?)"diy":"(.*?)"', re.S)
                Items_2 = re.findall(Pattern, Content)
                for Item_2 in Items_2:
                    print '第' + str(Count) + '张: ' + Item_2[2].replace('\\', '')
                    Count += 1
            except urllib2.URLError as Error:
                if hasattr(Error, 'code'):
                    print(Error.code)
                if hasattr(Error, 'reason'):
                    print(Error.reason)
        print('#' * 32 + '分隔符' + '#' * 32)
except urllib2.URLError as Error:
    if hasattr(Error, 'code'):
        print(Error.code)
    if hasattr(Error, 'reason'):
        print(Error.reason)

# 每日壁纸
URL = 'http://api.lovebizhi.com/windows_v3.php?client_id=1004&model_id=106&bizhi_width=1920&bizhi_height=1080&a=browse&id=everyday'
Count = 1
try:
    Request = urllib2.Request(URL, headers=Header)
    Response = urllib2.urlopen(Request)
    Content = Response.read().decode('utf-8')
    Pattern = re.compile('{(.*?)"date":"(.*?)"(.*?)"url":"(.*?)"', re.S)
    Items = re.findall(Pattern, Content)
    for Item in Items:
        print '日期: ' + Item[1] + '\n' + '链接: ' + Item[3].replace('\\', '')
        for Page in range(1, 21):
            URL = Item[3].replace('\\', '') + '&p=' + str(Page)
            try:
                Request = urllib2.Request(URL, headers=Header)
                Response = urllib2.urlopen(Request)
                Content = Response.read().decode('utf-8')
                Pattern = re.compile('{(.*?)"image":(.*?)"diy":"(.*?)"', re.S)
                Items_2 = re.findall(Pattern, Content)
                for Item_2 in Items_2:
                    print '第' + str(Count) + '张: ' + Item_2[2].replace('\\', '')
                    Count += 1
            except urllib2.URLError as Error:
                if hasattr(Error, 'code'):
                    print(Error.code)
                if hasattr(Error, 'reason'):
                    print(Error.reason)
        print('#' * 32 + '分隔符' + '#' * 32)
except urllib2.URLError as Error:
    if hasattr(Error, 'code'):
        print(Error.code)
    if hasattr(Error, 'reason'):
        print(Error.reason)
