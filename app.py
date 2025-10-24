from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello World from Python Server!</h1>")

print("Server running on port 8080...")
HTTPServer(("0.0.0.0", 8080), HelloHandler).serve_forever()
