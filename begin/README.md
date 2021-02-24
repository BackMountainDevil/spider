# 爬虫初步

[返回主目录](../README.md)

## 目录

## 最基本的爬虫 - Request
相关库传送门：  
- [Requests](https://github.com/psf/requests)  
>`python -m pip install requests `   
>Requests officially supports Python 2.7 & 3.5+.

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)  
>`pip install beautifulsoup4`  


代码案例：  
[基本爬虫](./base.py)   
[信息提取](./base_bs4.py)  
利用Requests模拟人点击网页发送GET请求的[基本爬虫](begin/base.py)，它可以获取Bing搜索首页的全部HTML代码，返回的HTML代码较长，需要提取其中的有用信息，通常借助BeautifulSoup进行提取-[信息提取](./base_bs4.py)。    
