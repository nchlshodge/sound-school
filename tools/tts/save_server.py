# Receives the text list posted by the in-browser crawl and writes it to disk.
import http.server, sys
OUT=sys.argv[1]
class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        n=int(self.headers['Content-Length']); open(OUT,'wb').write(self.rfile.read(n))
        self.send_response(200); self.send_header('Access-Control-Allow-Origin','*'); self.end_headers(); self.wfile.write(b'saved')
http.server.HTTPServer(('127.0.0.1',8766),H).serve_forever()
