#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  导入模块
import re, time, urllib.request

# User-Agent
Header = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

def Get_Content(URL):
    try:
        Request = urllib.request.Request(URL, headers = Header)
        Response = urllib.request.urlopen(Request)
        Content = Response.read().decode('utf-8')
        Pattern_1 = re.compile('<div>(.*?)<img src="(.*?)"(.*?)</div>(.*?)</div>', re.S)
        Items = re.findall(Pattern_1, Content)
        for Item in Items:
            if Item[1] == '':
                print('此URL返回结果为空，跳过！')
                break
            else:
                print('签名:' + Item[3])
                print('图片:' + Item[1])
    except urllib.request.URLError as Error:
        if hasattr(Error, 'code'):
            print(Error.code)
        if hasattr(Error, 'reason'):
            print(Error.reason)

Count = 67565

for ID in range(1, (Count + 1)):
    URL = 'https://qianming001.vipappsina.com/i.php?id=' + str(ID)
    print('ID:' + str(ID) + ' ' + '链接:' + URL)
    Get_Content(URL)
    print('#' * 64)
