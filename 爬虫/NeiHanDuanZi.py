#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Title=内涵社区段子爬取
Date=2018-1-29
'''

import requests
import re
import io
import time

#url= 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1517230734.0'
#html=requests.get(url)
timestamp=1517230734
header={'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh,zh-CN;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'csrftoken=ffb8d3b81b45c99fbebc69d47bccce03; tt_webid=6516453279488230919; uuid="w:d213ed978c3f4f41a37572e943246a04"; _ga=GA1.2.1182654738.1517230015; _gid=GA1.2.335155992.1517230015; _gat=1',
    'Host':'neihanshequ.com',
    'Pragma':'no-cache',
    'Referer':'http://neihanshequ.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-CSRFToken':'ffb8d3b81b45c99fbebc69d47bccce03',
    'X-Requested-With':'XMLHttpRequest'
}
while type(timestamp) == int or type(timestamp) == float:
    timestamp=str(timestamp)
    url= 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time='+timestamp
    html=requests.get(url,headers=header)
    timestamp=html.json()['data']['max_time']
    for n in range(1,len(html.json()['data']['data'])):
        context=html.json()['data']['data'][n]['group']['text']
        time.sleep(1)
        #print(len(html.json()['data']['data']))
        with io.open('duanzi.txt', 'a', encoding='utf-8' ) as dz:
            dz.write(context+'\n')
        print('成功写入')
