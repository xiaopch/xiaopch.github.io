#!/usr/bin/env python
# coding:utf-8

from bs4 import BeautifulSoup

import requests,re
from datetime import datetime
import pandas as pd
import os

import locale
locale.setlocale(locale.LC_CTYPE, 'Chinese')

text_list=[]

def get_billboard(url,filter_name,filter_attrs,frame_name='body',frame_attrs=''):
    root_url = os.path.split(url)[0]#.split('//')[-1]
    file_content = []

    print(root_url)
    # return

    response = requests.get(
        url=url,
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', },
    )
    # response.encoding = response.apparent_encoding
    ##print(ret.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    title=soup.title.text
##    ##print(soup.prettify())

    main_content = soup.find(name=frame_name, attrs=frame_attrs)
##    print(main_content)
    divs = main_content.find_all(filter_name,attrs=filter_attrs)
    print('总数:',len(divs))

    text_list.append('## '+title+'\n')
    for div in divs:
        line = '- '+div.text+'\n'
        print(line)
        text_list.append(line)

    return text_list

def getHotNews():
    global text_list
    text_list = []
    get_billboard("https://www.zhihu.com/billboard",'div',{"class":"HotList-itemTitle"})
    get_billboard("https://top.baidu.com/board?tab=realtime",'div',{"class":"c-single-text-ellipsis"})

    # get_weibo_top('https://s.weibo.com/top/summary','div',{"class":"data"})

    file_name = datetime.now().strftime('%m.%d_新闻.md')
    print(file_name)
    with open(file_name,'w',encoding='utf-8') as fh:
        fh.writelines(text_list)
getHotNews()

# import schedule
# import time
# # 循环执行模块 定时获取热搜内容
# schedule.every(3600).seconds.do(getHotNews)
# while True:
#   schedule.run_pending()
#   time.sleep(1)
# #




#
# get_billboard("http://top.baidu.com/buzz?b=2",'a',{"class":"list-title"})
# get_billboard("http://top.baidu.com/buzz?b=3",'a',{"class":"list-title"})
# get_billboard("http://top.baidu.com/buzz?b=4",'a',{"class":"list-title"})
# get_billboard("http://top.baidu.com/buzz?b=5",'a',{"class":"list-title"})
# get_billboard("http://top.baidu.com/buzz?b=7",'a',{"class":"list-title"})
# get_billboard("http://top.baidu.com/buzz?b=12",'a',{"class":"list-title"})
# get_billboard("http://top.baidu.com/buzz?b=42",'a',{"class":"list-title"})
