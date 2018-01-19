#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


class Cfda:
    def __init__(self):
        self.url = 'http://125.35.6.84:81/xk/'
        self.f =open(r'cfda.txt')

    def getData(self, data):
        self.html = requests.post(self.url, data=data)
        print(self.html.json()['list'][n]['EPS_NAME'])
        data=self.html.json()['list'][n]['EPS_NAME']

    def writeData(self):
        self.f.write(self.data,'\n')

cfda = Cfda()
data = {'on': 'true',
        'page': 1,
        'pageSize': 15,
        'productName': '',
        'conditionType': 1,
        'applyname': '',
        'applysn': ''}
cfda.getData(data)
cfda.writeData()
