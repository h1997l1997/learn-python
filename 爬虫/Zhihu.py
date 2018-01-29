''''
Title=抓取知乎粉丝
Date=2018-01-24
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入模块
import requests
import time
import random  # 随机数


class GetZhiHu:
    # 构造函数 初始化函数
    def __init__(self):
        self.url = 'https://zhuanlan.zhihu.com/api/columns/sspaime/followers'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        self.f = open('D:\\2.txt', 'a')

    def getFenSi(self, data):
        self.html = requests.get(self.url, params=data, headers=self.header)
        for n in range(20):
            self.hash = self.html.json()[n]['name']
            self.f.write(self.hash + '\n' * 2)
        # print(self.html.json()[0]['hash'])
        # print(self.html.text)

    def fclose(self):
        self.f.close()


if __name__ == '__main__':
    #如果__name—__在本程序就等于__main__
    #程辉就运行成功，将if下面函数全部执行
    #如果被其他程序或者脚本调用，则不会执行if下面语句
    getzhihu = GetZhiHu()  # 实例化
    for x in range(0, 100, 1):
        data = {'limit': '20', 'offset': x}
        getzhihu.getFenSi(data)
    getzhihu.fclose()
