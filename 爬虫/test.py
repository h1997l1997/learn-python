#!/usr/bin/python
# -*- coding: utf-8 -*-


from tornado import web, ioloop, httpserver

#页面
#首页
class Main(web.RequestHandler):
    def get(self, *args, **kwargs):
        #self.write('wellcome')
        self.render('index.html')

#登录
class Login(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('login.html')
    def post(self,*args,**kwargs):
        username=self.get_argument('username')
        password=self.get_argument('password')
#设置
setting={
    #设置模板路径
    'template_path':'templates' #和子文件夹名一样
    #设置静态文件路径
    ?????????????????????????????????
}
# 路由 分机
application = web.Application([
    (r"/", Main),
    (r"/login",Login),
]**setting)

# socket 服务
if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
