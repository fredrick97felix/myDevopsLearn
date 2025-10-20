import http.server
import socketserver

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("A custom GET request was received.")
        # Call the parent class's do_GET method to serve the file
        super().do_GET()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT} with a custom handler")
    httpd.serve_forever()