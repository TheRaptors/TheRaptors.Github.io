#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 修改 Python 2.7.x 默认编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 导入模块
import urllib, urllib2, re, time

# User-Agent
Header = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

# iOS 专辑
URL = 'http://fuli1024.com/weibofun/albums/album_list.php?apiver=20201&page=0&page_size=30&'
try:
    Request = urllib2.Request(URL, headers = Header)
    Response = urllib2.urlopen(Request)
    Content = Response.read().decode('utf-8')
    Pattern = re.compile('{"aid":(.*?),"aname":(.*?),.*?"adesc":(.*?),.*?"update_time":(.*?),', re.S)
    Items = re.findall(Pattern, Content)
    for Item in Items:
        Date = time.strftime('%Y-%m-%d %X', time.gmtime((int(Item[3].encode('utf-8').strip('"')))))
        print "专辑ID：", Item[0].strip('"'), "日期：", Date
        print "标题：", Item[1].strip('"')
        print "详情：", Item[2].strip('"')
        print('#' * 64)
except urllib2.URLError as Error:
    if hasattr(Error, 'code'):
        print(Error.code)
    if hasattr(Error, 'reason'):
        print(Error.reason)

# iOS 段子
URL = 'http://fuli1024.com/weibofun/weibo_list.php?apiver=20201&category=weibo_jokes&page=0&page_size=30&'
try:
    Request = urllib2.Request(URL, headers = Header)
    Response = urllib2.urlopen(Request)
    Content = Response.read().decode('utf-8')
    Pattern = re.compile('{"wid":(.*?),"update_time":(.*?),"wbody":(.*?),"comments":(.*?),.*?,"user_name":(.*?),', re.S)
    Items = re.findall(Pattern, Content)
    for Item in Items:
        Date = time.strftime('%Y-%m-%d %X', time.gmtime((int(Item[1].encode('utf-8').strip('"')))))
        if Item[4].encode('utf-8') != 'null':
            print "ID：", Item[0].strip('"'), "日期：", Date, "赞：", Item[3].strip('"'), "发布：", Item[4].strip('"')
        else:
            print "ID：", Item[0].strip('"'), "日期：", Date, "赞：", Item[3].strip('"'), "发布：", "官方"
        print Item[2].strip('"')
        print('#' * 64)
except urllib2.URLError as Error:
    if hasattr(Error, 'code'):
        print(Error.code)
    if hasattr(Error, 'reason'):
        print(Error.reason)

# iOS 美女
URL = 'http://fuli1024.com/weibofun/weibo_list.php?apiver=20201&category=weibo_girls&page=0&page_size=30&'
try:
    Request = urllib2.Request(URL, headers = Header)
    Response = urllib2.urlopen(Request)
    Content = Response.read().decode('utf-8')
    Pattern = re.compile('{"wid":(.*?),"update_time":(.*?),"wbody":(.*?),"comments":(.*?),.*?,"wpic_small":(.*?),"wpic_middle":(.*?),"wpic_large":(.*?),', re.S)
    Items = re.findall(Pattern, Content)
    for Item in Items:
        Date = time.strftime('%Y-%m-%d %X', time.gmtime((int(Item[1].encode('utf-8').strip('"')))))
        print "ID：", Item[0].strip('"'), "日期：", Date, "赞：", Item[3].strip('"')
        print Item[2].strip('"')
        # print "小图：", Item[4].strip('"')
        # print "中图：", Item[5].strip('"')
        print "大图：", Item[6].strip('"')
        print('#' * 64)
except urllib2.URLError as Error:
    if hasattr(Error, 'code'):
        print(Error.code)
    if hasattr(Error, 'reason'):
        print(Error.reason)

# iOS 视频
URL = 'http://fuli1024.com/weibofun/weibo_list.php?apiver=20201&category=weibo_videos&page=0&page_size=30&'
try:
    Request = urllib2.Request(URL, headers = Header)
    Response = urllib2.urlopen(Request)
    Content = Response.read().decode('utf-8')
    Pattern = re.compile('{"wid":(.*?),"update_time":(.*?),"wbody":(.*?),"comments":(.*?),.*?,"vsource_url":(.*?),.*?,"user_name":(.*?),', re.S)
    Items = re.findall(Pattern, Content)
    for Item in Items:
        Date = time.strftime('%Y-%m-%d %X', time.gmtime((int(Item[1].encode('utf-8').strip('"')))))
        if Item[5].encode('utf-8') != 'null':
            print "ID：", Item[0].strip('"'), "日期：", Date, "赞：", Item[3].strip('"'), "发布：", Item[5].strip('"')
        else:
            print "ID：", Item[0].strip('"'), "日期：", Date, "赞：", Item[3].strip('"'), "发布：", "官方"
        print Item[2].strip('"')
        print "视频地址：", Item[4].strip('"')
        print('#' * 64)
except urllib2.URLError as Error:
    if hasattr(Error, 'code'):
        print(Error.code)
    if hasattr(Error, 'reason'):
        print(Error.reason)

# iOS 趣图
URL = 'http://fuli1024.com/weibofun/weibo_list.php?apiver=20201&category=weibo_pics&page=0&page_size=30&'
try:
    Request = urllib2.Request(URL, headers = Header)
    Response = urllib2.urlopen(Request)
    Content = Response.read().decode('utf-8')
    Pattern = re.compile('{"wid":(.*?),"update_time":(.*?),"wbody":(.*?),"comments":(.*?),.*?,"wpic_small":(.*?),"wpic_middle":(.*?),"wpic_large":(.*?),.*?,"user_name":(.*?),', re.S)
    Items = re.findall(Pattern, Content)
    for Item in Items:
        Date = time.strftime('%Y-%m-%d %X', time.gmtime((int(Item[1].encode('utf-8').strip('"')))))
        if Item[7].encode('utf-8') != 'null':
            print "ID：", Item[0].strip('"'), "日期：", Date, "赞：", Item[3].strip('"'), "发布：", Item[7].strip('"')
        else:
            print "ID：", Item[0].strip('"'), "日期：", Date, "赞：", Item[3].strip('"'), "发布：", "官方"
        print Item[2].strip('"')
        # print "小图：", Item[4].strip('"')
        # print "中图：", Item[5].strip('"')
        print "大图：", Item[6].strip('"')
        print('#' * 64)
except urllib2.URLError as Error:
    if hasattr(Error, 'code'):
        print(Error.code)
    if hasattr(Error, 'reason'):
        print(Error.reason)