__author__ = 'william'

import http.server
import socketserver

PORT = 8000


class Insult(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_head()
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(
            bytes("<body><p>Your mother was a hamster and your father smells of elderberries</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_HEAD(self):
        self.send_head()

    def send_head(self):
        self.send_response(202)
        self.send_header("Content-type", "text/html")
        self.end_headers()


httpd = socketserver.TCPServer(("", PORT), Insult)

print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
