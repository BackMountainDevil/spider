#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests


r = requests.get('https://cn.bing.com/')

print("r.status_code:" , r.status_code)     # 状态码
print('r.headers: ', r.headers)     # 请求头
print('r.encoding ', r.encoding)    # 编码
# print('r.text: ', r.text)     # 请求内容
print('Length of r.text: ', len(r.text))    # 请求内容长度， 我得到的是114233
print('r.text: ', r.text[1000 : 1200])    # 请求内容部分内容-字符串切片