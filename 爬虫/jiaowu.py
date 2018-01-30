


import requests
from bs4 import BeautifulSoup
import re

class NUAA:
    # 初始化函数

    def __init__(self):
        self.url = 'http://aao.nuaa.edu.cn/list_sub/333?sourceType=notice&page=%d&size=10&t=Sun%%20Jan%%2021%%202018%%2021:41:41%%20GMT+0800%%20(%%E4%%B8%%AD%%E5%%9B%%BD%%E6%%A0%%87%%E5%%87%%86%%E6%%97%%B6%%E9%%97%%B4)'

    def getData(self,x):
        self.html = requests.get(self.url % x)
        #print(self.html.text)
        soup=BeautifulSoup(self.html.text,'html.parser')
        #html_str=str(self.html.text)
        print(soup.prettify())
        print('----------')
        print(soup.get_text())
        html_text=str(soup.get_text())
        nuaa.clear(html_text)


    def clear(self,html_str):
        for n in range(0,10):
            n=str(n)
            html_str=html_str.replace(n,'')
        html_str=html_str.replace('首页','')
        html_str=html_str.replace('通知公告','')
        html_str=html_str.replace('教学服务','')
        html_str=html_str.replace('-','')
        html_str=html_str.replace(' ','')
        f=open('D:/1.txt','a')
        f.write(html_str)
        f.close()


nuaa = NUAA()
for x in range(1,18):
    nuaa.getData(x)
