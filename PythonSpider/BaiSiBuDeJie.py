#!/usr/bin/env python
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
            print('链接：' + Item[8].replace('"', '').replace('data-original=', '').replace('data-mp4=', '').replace('data-pic=', ''))
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
Min_Page = 1
Max_Page = 51

# 基础域名
Basic_URL = 'http://www.budejie.com/'

# 扩展信息
List={'Type1': '首页', 'Domain1': '', 'Func1': Get_Index,
      'Type2': '首页-穿越', 'Domain2': 'old', 'Func2': Get_Index,
      'Type3': '视频', 'Domain3': 'video', 'Func3': Get_Video,
      'Type4': '视频-穿越', 'Domain4': 'old-video', 'Func4': Get_Video,
      'Type5': '图片', 'Domain5': 'pic', 'Func5': Get_Pic,
      'Type6': '图片-穿越', 'Domain6': 'old-pic', 'Func6': Get_Pic,
      'Type7': '段子', 'Domain7': 'text', 'Func7': Get_Text,
      'Type8': '段子-穿越', 'Domain8': 'old-text', 'Func8': Get_Text,
      'Type9': '声音', 'Domain9': 'audio', 'Func9': Get_Audio,
      'Type10': '声音-穿越', 'Domain10': 'old-audio', 'Func10': Get_Audio,
      'Type11': '排行', 'Domain11': 'hot', 'Func11': Get_Hot,
      'Type12': '美女', 'Domain12': 'tag/117', 'Func12': Get_Hot}

for Page in range(Min_Page, Max_Page):
    for i in range(1, 13):
        # print(List['Type' + str(i)])
        URL = Basic_URL + List['Domain' + str(i)]
        if Page == 1:
            URL = URL
        else:
            URL = URL + '/' + str(Page)
        List['Func' + str(i)](URL = URL, Page = Page)