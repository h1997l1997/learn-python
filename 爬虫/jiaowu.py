import requests


class NUAA:
    # 初始化函数

    def __init__(self):
        self.url = 'http://aao.nuaa.edu.cn/list_sub/333?sourceType=notice&page=%d&size=10&t=Sun%%20Jan%%2021%%202018%%2021:41:41%%20GMT+0800%%20(%%E4%%B8%%AD%%E5%%9B%%BD%%E6%%A0%%87%%E5%%87%%86%%E6%%97%%B6%%E9%%97%%B4)'

    def getData(self):
        self.html = requests.get(self.url % 1)
        #print(self.html.text)
        html_str=str(self.html.text)
        print(html_str)


nuaa = NUAA()
nuaa.getData()
