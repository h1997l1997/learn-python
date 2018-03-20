
#import os
import requests
#os.mkdir('Picture')
url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&pn=30&rn=30&gsm=1e&1517835556933='
html=requests.get(url)
html.encoding='utf-8'
pictuerurl=html.json()['data'][0]['hoverURL']
