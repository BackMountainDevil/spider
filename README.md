# spider

#### 介绍

Python爬虫从零开始

## 爬虫初步

### 最基本的爬虫 - Request

一个比较好用的库：[Requests](https://github.com/psf/requests)  
模拟人点击网页发送GET请求的[基本爬虫](begin/base.py)，它可以获取bing首页的全部HTML代码，返回的HTML代码较长，需要提取其中的有用信息，通常借助[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)  



#### 使用说明

1.  克隆仓库  
```bash
git clone 
```
2.  安装虚拟环境  
需要使用pipenv将本项目与其它项目隔离，当然这并不是强制的，安装pipenv的办法也很简单 - `pip install pipenv`
```bash
pipenv install
```
3.  激活虚拟环境运行代码  
每次进入虚拟环境中都需要激活虚拟环境，然后进入对于的目录下运行相应代码
```bash
pipenv shell    # 激活环境
pipenv run python base.py   # 运行base.py
```
4. 删除虚拟环境（可选）
当不再需要使用项目的时候，删除项目文件的时候并不会自动删除虚拟环境，需要手动删除。
```bash
pipenv --rm
```


## 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
