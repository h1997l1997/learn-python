#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import webbrowser
import time
import os
from random import choice, random
import csv

if __name__ == '__main__':
    counter = 1
    while True:
        filename = "C://url.csv"
        url = []
        if filename != '':
            with open(filename) as csvfile:
                rows = csv.reader(csvfile)
                for row in rows:
                    url.append(row[0])

        else:
            print ("You may not set the options correctly,please try again")

        counter += 1
        webbrowser.open(choice(url),new=0,autoraise=True)
        print (webbrowser.get())
        time.sleep(20)

        if(counter==10):
            counter = 1
            os.system('taskkill /F /IM  Maxthon.exe')
