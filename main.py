import http.server
import socket
import select
import http.client
from urllib.parse import urlparse

class Proxy(http.server.BaseHTTPRequestHandler):
    whitelist = ["www.gvsu.edu", "www.nvidia.com", "www.michigan.gov"]

    def do_GET(self):
        parsed_url = urlparse(self.path)
        domain = parsed_url.netloc

        if domain in self.whitelist:
            conn = http.client.HTTPConnection(domain)
            conn.request("GET", parsed_url.path)
            res = conn.getresponse()
            self.send_response(res.status)
            for header, val in res.getheaders():
                self.send_header(header, val)
            self.end_headers()
            self.wfile.write(res.read())
            conn.close()
        else:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Access denied")

    def do_CONNECT(self):
        host, _, port = self.path.rpartition(':')
        if host in self.whitelist:
            self.connect_tunnel(host, port)
        else:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Access denied")

    def transparent_forward(self, parsed_url):
        try:
            conn = http.client.HTTPConnection(parsed_url.netloc)
            conn.request(self.command, parsed_url.path, self.headers)
            res = conn.getresponse()
            self.send_response(res.status)
            for header, val in res.getheaders():
                self.send_header(header, val)
            self.end_headers()
            self.wfile.write(res.read())
            conn.close()
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {str(e)}")

    def connect_tunnel(self, host, port):
        try:
            remote = socket.create_connection((host, int(port)))
            self.send_response(200)
            self.end_headers()
            
            conn = self.connection
            conn.settimeout(10)
            remote.settimeout(10)
            
            inputs = [conn, remote]
            while True:
                readable, _, exceptional = select.select(inputs, [], inputs)
                if exceptional:
                    break
                for s in readable:
                    data = s.recv(4096)
                    if not data:
                        break
                    if s is conn:
                        remote.sendall(data)
                    else:
                        conn.sendall(data)
        except Exception as e:
            self.send_error(502, f"Bad Gateway: {str(e)}")
        finally:
            remote.close()
            self.connection.close()

def run(server_class=http.server.HTTPServer, handler_class=Proxy, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        print("Starting proxy server on port", port)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down the server...")
        httpd.socket.close()

if __name__ == '__main__':
    run()
