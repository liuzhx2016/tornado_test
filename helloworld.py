# -*- coding:utf-8 -*-
import os,sys,time
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

reload(sys)
sys.setdefaultencoding('gbk')  # @UndefinedVariable


class RootHandler(tornado.web.RequestHandler):
    def do_request(self):
        print "Get a request!"
        print self.request.arguments
        print self.request.files
        print self.request.path
        print self.request.headers
        body = self.request.arguments  #得到的就是一个字典，tornado内部转换了
        if (body.has_key("picname")):
            print body["picname"]  
            self.write(body["picname"][0])
        else:
            self.write("no picname param!")
    def post(self):
        self.do_request()        
    def get(self):
        self.do_request()
		
class ShowIndex(tornado.web.RequestHandler):
    def Runfun(self):
        print "show index!"
        self.render("index.html")
        #self.write("Hello, world")
    def post(self):
        self.Runfun()
    def get(self):
        self.Runfun()

class GetPic(tornado.web.RequestHandler):
    def initialize(self,database,nihao):
    	self.database = database
    	self.nihao = nihao
    def Runfun(self):
        print "show index!"
        print self.database
        print self.nihao
        #self.render("index.html")
        print self.request.arguments
        print self.request.files
        print self.request.path
        print self.request.headers
        
        print self.request.arguments.keys()

        print self.request.files['pic'][0]
        image_info = self.request.files['pic'][0]
        
        self.write("get over!")
    def post(self):
        self.Runfun()
    def get(self):
        self.Runfun()

class Coockie(tornado.web.RequestHandler):
	def Runfun(self):
		self.set_cookie("mycookie", "liuzhxisgood")
		if not self.get_cookie("mycookie"):
			self.set_cookie("mycookie", "liuzhxisgood")
			self.write("Your cookie was not set yet!")
		else:
			buf = self.get_cookie("mycookie")
			print buf
			self.write("Your cookie was set!")
	def post(self):
		self.Runfun()
	def get(self):
		self.Runfun()

class Test(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://localhost:9090/",
                   callback=self.on_response)

    def on_response(self, response):
		for i in range(20):
			time.sleep(1)
			print time.time() 
		self.finish("nihao")

#定义的tronado的应用类继承tornado.web.Application，重载初始化函数
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            #web服务器首页
            (r"/", RootHandler),
			(r"/index",ShowIndex),
			(r"/getpic",GetPic, {"database":"woshi liuzhx","nihao":"woshi zhe"} ),
			(r"/cookie",Coockie),
			(r"/test",Test)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "template"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            autoreload = True,
            cookie_secret="liuzhx"
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    tornado.httpserver.HTTPServer(Application()).listen(9090)
    print "Begin to listen!"
    tornado.ioloop.IOLoop.current().start()
