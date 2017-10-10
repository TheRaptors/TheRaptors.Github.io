#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  导入模块
import re, time, urllib.request

# User-Agent
Header = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

def Get_Index(URL, Page):
    Count = 1
    try:
        Request = urllib.request.Request(URL, headers = Header)
        Response = urllib.request.urlopen(Request)
        Content = Response.read().decode('utf-8')
        Pattern = re.compile('<div class="j-list-user">(.*?)class="u-user-name" target="_blank">(.*?)</a>(.*?)<span class="u-time  f-ib f-fr">(.*?)</span>(.*?)<a href="(.*?)">(.*?)</a>(.*?)(data-pic="(.*?)"|data-original="(.*?)"|data-mp4="(.*?)")', re.S)
        Items = re.findall(Pattern, Content)
        for Item in Items:
            print('第' + str(Page) + '页' + '第' + str(Count) + '个')
            print('发布：' + Item[1])
            print('时间：' + Item[3])
            print('标题：' + Item[6])
            print('链接：' + Item[8].replace('"', '').replace('data-original=', '').replace('data-mp4=', ''))
            Count += 1
    except urllib.request.URLError as Error:
        if hasattr(Error, 'code'):
            print(Error.code)
        if hasattr(Error, 'reason'):
            print(Error.reason)

def Get_Video(URL, Page):
    Count = 1
    try:
        Request = urllib.request.Request(URL, headers = Header)
        Response = urllib.request.urlopen(Request)
        Content = Response.read().decode('utf-8')
        Pattern = re.compile('<div class="j-list-user">(.*?)class="u-user-name" target="_blank">(.*?)</a>(.*?)<span class="u-time  f-ib f-fr">(.*?)</span>(.*?)<a href="(.*?)">(.*?)</a>(.*?)data-videoMlen="(.*?)"(.*?)data-mp4="(.*?)"', re.S)
        Items = re.findall(Pattern, Content)
        for Item in Items:
            print('第' + str(Page) + '页' + '第' + str(Count) + '个')
            print('发布：' + Item[1])
            print('时间：' + Item[3])
            print('标题：' + Item[6])
            print('时长：' + Item[8])
            print('链接：' + Item[10])
            Count += 1
    except urllib.request.URLError as Error:
        if hasattr(Error, 'code'):
            print(Error.code)
        if hasattr(Error, 'reason'):
            print(Error.reason)

def Get_Pic(URL, Page):
    Count = 1
    try:
        Request = urllib.request.Request(URL, headers = Header)
        Response = urllib.request.urlopen(Request)
        Content = Response.read().decode('utf-8')
        Pattern = re.compile('<div class="j-list-user">(.*?)class="u-user-name" target="_blank">(.*?)</a>(.*?)<span class="u-time  f-ib f-fr">(.*?)</span>(.*?)data-original="(.*?)"(.*?)title="(.*?)"', re.S)
        Items = re.findall(Pattern, Content)
        for Item in Items:
            print('第' + str(Page) + '页' + '第' + str(Count) + '个')
            print('发布：' + Item[1])
            print('时间：' + Item[3])
            print('标题：' + Item[7])
            print('链接：' + Item[5])
            Count += 1
    except urllib.request.URLError as Error:
        if hasattr(Error, 'code'):
            print(Error.code)
        if hasattr(Error, 'reason'):
            print(Error.reason)

def Get_Text(URL, Page):
    Count = 1
    try:
        Request = urllib.request.Request(URL, headers = Header)
        Response = urllib.request.urlopen(Request)
        Content = Response.read().decode('utf-8')
        Pattern = re.compile('<div class="j-list-user">(.*?)class="u-user-name" target="_blank">(.*?)</a>(.*?)<span class="u-time  f-ib f-fr">(.*?)</span>(.*?)<a href="(.*?)">(.*?)</a>', re.S)
        Items = re.findall(Pattern, Content)
        for Item in Items:
            print('第' + str(Page) + '页' + '第' + str(Count) + '个')
            print('发布：' + Item[1])
            print('时间：' + Item[3])
            print('内容：' + Item[6])
            Count += 1
    except urllib.request.URLError as Error:
        if hasattr(Error, 'code'):
            print(Error.code)
        if hasattr(Error, 'reason'):
            print(Error.reason)

def Get_Audio(URL, Page):
    Count = 1
    try:
        Request = urllib.request.Request(URL, headers = Header)
        Response = urllib.request.urlopen(Request)
        Content = Response.read().decode('utf-8')
        Pattern = re.compile('<div class="j-list-user">(.*?)class="u-user-name" target="_blank">(.*?)</a>(.*?)<span class="u-time  f-ib f-fr">(.*?)</span>(.*?)<div class="j-r-list-c-desc">(.*?)</div>(.*?)data-mp3="(.*?)"', re.S)
        Items = re.findall(Pattern, Content)
        for Item in Items:
            print('第' + str(Page) + '页' + '第' + str(Count) + '个')
            print('发布：' + Item[1])
            print('时间：' + Item[3])
            print('标题：' + Item[5])
            print('链接：' + Item[7])
            Count += 1
    except urllib.request.URLError as Error:
        if hasattr(Error, 'code'):
            print(Error.code)
        if hasattr(Error, 'reason'):
            print(Error.reason)

def Get_Hot(URL, Page):
    Count = 1
    try:
        Request = urllib.request.Request(URL, headers = Header)
        Response = urllib.request.urlopen(Request)
        Content = Response.read().decode('utf-8')
        Pattern = re.compile('<div class="j-list-user">(.*?)class="u-user-name" target="_blank">(.*?)</a>(.*?)<span class="u-time  f-ib f-fr">(.*?)</span>(.*?)<a href="(.*?)">(.*?)</a>(.*?)(data-original="(.*?)"|data-mp4="(.*?)")', re.S)
        Items = re.findall(Pattern, Content)
        for Item in Items:
            print('第' + str(Page) + '页' + '第' + str(Count) + '个')
            print('发布：' + Item[1])
            print('时间：' + Item[3])
            print('标题：' + Item[6])
            print('链接：' + Item[8].replace('"', '').replace('data-original=', '').replace('data-mp4=', ''))
            Count += 1
    except urllib.request.URLError as Error:
        if hasattr(Error, 'code'):
            print(Error.code)
        if hasattr(Error, 'reason'):
            print(Error.reason)

# 最大显示50页
Max_Page = 51

# 首页
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Index(URL = URL, Page = Page)

# 首页-穿越
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/old/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Index(URL = URL, Page = Page)

# 视频
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/video/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Video(URL = URL, Page = Page)

# 视频-穿越
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/old-video/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Video(URL = URL, Page = Page)

# 图片
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/pic/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Pic(URL = URL, Page = Page)

# 图片-穿越
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/old-pic/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Pic(URL = URL, Page = Page)

# 段子
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/text/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Text(URL = URL, Page = Page)

# 段子-穿越
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/old-text/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Text(URL = URL, Page = Page)

# 声音
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/audio/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Audio(URL = URL, Page = Page)

# 声音-穿越
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/old-audio/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Audio(URL = URL, Page = Page)
    
# 排行
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/hot/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Hot(URL = URL, Page = Page)

# 美女
for Page in range(1, Max_Page):
    URL = 'http://www.budejie.com/tag/117/'
    if Page == 1:
        URL = URL
    else:
        URL = URL + str(Page)
    Get_Hot(URL = URL, Page = Page)
