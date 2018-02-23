import requests
import os
class YiCunZhao:
    def __init__(self):
        self.url='http://ded.nuaa.edu.cn/netean/GetPic.asp?pic=xh&xh='
        self.headers={ 'Cookie':'ASPSESSIONIDAQQCDRSS=BIFKIBJDIALBHJDKOMKICOHA',
                       'Referer':'http://ded.nuaa.edu.cn/netean/com/jbqkcx.asp'}

    def get(self,nuaa):
        self.url=self.url+nuaa
        pic=requests.get(self.url,headers=self.headers)
        yicunzhao.save(pic,nuaa)
        print("已获取证件照")

    def save(self,picture,nuaa1):
        f=open('1/a.jpg','wb')
        f.write(picture.content)
        f.close()
        print("正在保存学号%s的证件照" % nuaa1)

yicunzhao=YiCunZhao()
nuaaid=str(input("请输入初始学号"))
yicunzhao.get(nuaaid)
