#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
'''
@File    :  base_bs4.py
@Time    :  2021/02/24 15:42:38
@Author  :  Kearney
@Contact :  191615342@qq.com
@Desc    :  在base的基础上，使用bs4提取Bing搜索首页的标题
            <title>微软 Bing 搜索 - 国内版</title>
'''
import requests
from bs4 import BeautifulSoup


r = requests.get('https://cn.bing.com/')
soup = BeautifulSoup(r.text, features="html.parser")
print(soup.title)
