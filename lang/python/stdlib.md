### 标准库

- **array**
```python
import array

# array.array(typecode, initializer)
inta = array.array('i', [1, 2, 3])
```
- **socket**
```python
import socket


# socket.socket(family, type, proto, fileno)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('localhost', 8080))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
```

- **socketserver**
```python
import socketserver


class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        """处理一次请求"""
        data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} connected")
        print(data)
        self.request.sendall(data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
```