# 菁优网爬虫

## 说明

* interface 为第二版爬虫基于pyqt5 + selenium + PhantomJS 半自动方式

1.采用GUI界面方式半自动爬取，不限制账号，普通账号也可按次数爬取默认100次。此次数为请求次数，实际获取课题id为每页10*100页等于1000条数据

2.手动登陆，弹出浏览器页面可用qq方式登陆，后关闭窗口。获取cookie数据

3.爬虫方式使用selenium+PhantomJS无头浏览器方式静默爬取。因PhantomJS只有10M并满足现有功能，就没有使用谷歌火狐无头模式，即便谷歌火狐更好。后期可更换

4.目前已爬取真实课题ID为目标的半自动爬虫工具，后期待加入爬取详情页数据。详情页数据每次访问为一个真实请求，并且无账号也可访问。故为第二目标

## 操作方法
### 登陆与获取登陆账号信息
* 手动QQ登陆，登陆后自动跳转到菁优网主页，获取cookie信息
![login](/assets/login.gif)
### 章节爬取
* 章节爬取会自动将原来的已爬取数据进行更新，已爬取的题库数据不会丢失
![zhangjie](/assets/zhangjie.gif)
### 题库爬取
* 支持自动翻页，后期加上断点续爬功能
![tiku](/assets/tiku.gif)
### 详情页爬取
* 已完成，爬取详情页，和详情中的知识点。

## 开发环境
### 环境
安装依赖包环境
`pip install -r requirements.txt`

### 编译生成windows可执行程序
`pyinstaller main.spec`

### 启动
`python main.py`













