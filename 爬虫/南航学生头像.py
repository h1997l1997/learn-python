import requests
import os

class YiCunZhao:
    def __init__(self):
        self.url = 'http://ded.nuaa.edu.cn/netean/GetPic.asp?pic=xh&xh='
        self.headers = {'Cookie': 'ASPSESSIONIDAQQCDRSS=BIFKIBJDIALBHJDKOMKICOHA',
                        'Referer': 'http://ded.nuaa.edu.cn/netean/com/jbqkcx.asp'}
        self.nuaaid = "123"

    def xuehao(self, x):
        for a in [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 510, 502, 503, 505, 506, 507, 508, 509, 510, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610]:
            a = str(a)
            for b in range(1, 40):
                self.nuaaid = x + str(a) + str(b).zfill(2)
                yesno = yicunzhao.get(self.nuaaid, x + a)

    def get(self, nuaa, filepath):
        url = self.url + nuaa
        pic = requests.get(url, headers=self.headers)
        lens = int(len(pic.content))
        if (nuaa[7:10] == '01' or nuaa[7:10] == '02' or nuaa[7:10] == '03' ) and (lens != 1141):
            isExists=os.path.exists(filepath)
            if not isExists:
                 os.mkdir(filepath)
            else:
                 pass
        else:
            pass
        if lens != 1141:
            yicunzhao.save(pic, nuaa, filepath)
            print("已获取证件照>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>100%%")

        else:
            print("学号不存在")
            pass

    def save(self, picture, nuaa1, path):
        f = open('%s/%s.jpg' % (path, nuaa1), 'wb')
        f.write(picture.content)
        f.close()
        print("正在保存学号%s的证件照>>>>>>>>>>>>>100%%" % nuaa1)


yicunzhao = YiCunZhao()
nuaaid = str(input("请输入入学年份"))
for xueyuan in [5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
    nuaaid1=str(xueyuan).zfill(2)+nuaaid
    os.mkdir(nuaaid1)
    os.chdir(nuaaid1)
    yicunzhao.xuehao(nuaaid1)
    os.chdir("..")
