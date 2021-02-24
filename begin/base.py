#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
'''
@File    :    base.py
@Time    :    2021/02/24 15:30:14
@Author  :    Kearney
@Contact :    191615342@qq.com
@Desc    :    使用requests获取Bing搜索首页的全部HTML代码，有点长，被我注释掉了
'''
import requests


r = requests.get('https://cn.bing.com/')

print("r.status_code: ", r.status_code)     # 状态码
print('r.headers: ', r.headers)     # 请求头
print('r.encoding ', r.encoding)    # 编码
# print('r.text: ', r.text)     # 请求内容
print('Length of r.text: ', len(r.text))    # 请求内容长度， 我得到的是114233
print('r.text: ', r.text[1000: 1200])    # 请求内容部分内容-字符串切片

with open('bing.html', 'w') as file:    # 将爬取到的HTML代码保持到文件中
    file.write(r.text)
