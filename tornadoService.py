from datetime import date
import tornado.ioloop
import tornado.web

// use html2canvas to collect screenshot: https://html2canvas.hertzen.com/

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item1", "Item2", "Item3"]
        self.render("index.html", title="Hello World", items=items);

class APIHandler(tornado.web.RequestHandler):
    def get(self, id):
        response = { 'id': int(id),
                    'name': 'Data Nerd',
                    'date': date.today().isoformat() }
        self.write(response)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/([0-9]+)", APIHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
