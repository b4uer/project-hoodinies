import http.server
import socketserver
import socket
import os

PORT = 8000

server_name = socket.gethostbyname(socket.getfqdn())

# fill in the name of the folder in which the picture is located in the variable 'path'
path = 'Image-Server' # folder of the picture
web_dir = os.path.join(os.path.dirname(__file__), path)
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((server_name, PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

# Add text to see when something happens within the server
