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
上面的案例中的爬虫的缺点很明显，爬取了一大堆垃圾信息回来然后用bs4从垃圾中找到我们需要的信息。

### HTML

我们所看到的网页都是HTML代码在浏览器下的渲染输出结果，爬取网页就是在获取这些HTML代码。HTML代码中含有大量的标签（<>），每个标签都有属性（attribute）和文本（text），a标签是实现自动爬取的重要线索。

### bs4

 bs4主要作用是对HTML进行标签搜索，然后获取其对应的文本属性。  
bs4会将HTML转换为4种Python对象：Tag、NavigableString、BeautifulSoup、Comment.
bs4支持多种实例化对象：部分HTML代码片段、完整HTML代码、网页文件。
