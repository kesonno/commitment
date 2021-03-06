import os
import random
import tornado.httpserver
import tornado.ioloop
import tornado.web

names = ['Nick', 'Steve', 'Andy', 'Qi', 'Fanny', 'Sarah', 'Cord', 'Todd', 'Chris', 'Pasha', 'Gabe', 'Tony', 'Jason', 'Randal', 'Ali',  'Kim', 'Rainer']

def randline():
	text = 'commit_messages.txt'
	if not os.path.exists(text):
		return "Shit ..."
	f = file(text, 'rb')
	for i,j in enumerate(f):
		if random.randint(0,i) == i:
			line = j
	f.close()
	return line

def randname():
	for i,j in enumerate(names):
		if random.randint(0, i) == i:
			line = j
	return line

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		line = randline().replace("XNAMEX", randname())
		self.render("index.html", message = line)

settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = tornado.web.Application([
	(r"/", MainHandler),
], **settings)

if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(80)
	tornado.ioloop.IOLoop.instance().start()
