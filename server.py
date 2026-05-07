import http.server
import socketserver
import os

PORT = int(os.environ.get('PORT', 10000))

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)

with socketserver.TCPServer(("0.0.0.0", PORT), MyHandler) as httpd:
    print(f"Servidor corriendo en puerto {PORT}")
    httpd.serve_forever()