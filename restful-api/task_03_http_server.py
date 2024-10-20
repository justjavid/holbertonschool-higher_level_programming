#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler as handler
import socketserver
import json

PORT = 8000

class BasicServer(handler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))
        elif self.path == "/info":
            self.send_response(200)
            self.end_headers()
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

with socketserver.TCPServer(("", PORT), BasicServer) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
