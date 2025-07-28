### asyncio.streams

* **server**
```python
import asyncio
import json
import struct
import uuid
from typing import Tuple


class StreamServer:
    def __init__(
        self,
        head_len: int = 4,
        address: Tuple[str, int] = ("127.0.0.1", 8081),
        max_connections: int = 100,
        timeout: float = 10.0
    ) -> None:
        self._head_len = head_len
        self._address = address
        self._semaphore = asyncio.Semaphore(max_connections)
        self._timeout = timeout
        self._clients = set()

    async def handler(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        peername = writer.get_extra_info("peername")
        print(f"Client connected: {peername}")
        async with self._semaphore:
            self._clients.add(writer)
            try:
                while True:
                    try:
                        # 读取头部数据（长度）
                        head_buffer = await asyncio.wait_for(
                            reader.readexactly(self._head_len), timeout=self._timeout
                        )
                        body_len = struct.unpack(">I", head_buffer)[0]
                        print(f"[{peername}] Data length: {body_len} bytes")

                        # 读取消息体
                        body_buffer = await asyncio.wait_for(
                            reader.readexactly(body_len), timeout=self._timeout
                        )
                        body_str = body_buffer.decode("utf-8", errors="replace")
                        print(f"[{peername}] Received: {body_str}")

                        # 构造响应
                        message = {
                            "id": uuid.uuid4().hex,
                            "body": body_str
                        }
                        response = json.dumps(message).encode()
                        data = struct.pack(">I", len(response)) + response
                        writer.write(data)
                        await writer.drain()
                    except asyncio.TimeoutError:
                        print(f"[{peername}] Timeout, closing connection.")
                        break
                    except asyncio.IncompleteReadError:
                        print(f"[{peername}] Client disconnected.")
                        break
                    except Exception as e:
                        print(f"[{peername}] Error: {e}")
                        break
            finally:
                self._clients.discard(writer)
                writer.close()
                await writer.wait_closed()
                print(f"[{peername}] Connection closed.")

    async def start(self) -> None:
        server = await asyncio.start_server(self.handler, *self._address)
        addr = server.sockets[0].getsockname()
        print(f"Server running on {addr}")
        async with server:
            try:
                await server.serve_forever()
            except asyncio.CancelledError:
                print("Server shutdown requested.")
            finally:
                # 关闭所有活跃连接
                for writer in list(self._clients):
                    writer.close()
                    await writer.wait_closed()
                print("All client connections closed.")


if __name__ == "__main__":
    try:
        server = StreamServer()
        print("Starting TCP server...")
        asyncio.run(server.start())
    except KeyboardInterrupt:
        print("Server stopped by user.")

```

* **client**
```python
import asyncio
import struct
from typing import Tuple, Optional


class StreamClient:
    def __init__(
        self,
        head_len: int = 4,
        address: Tuple[str, int] = ('127.0.0.1', 8081),
        timeout: float = 10.0
    ):
        self._reader: Optional[asyncio.StreamReader] = None
        self._writer: Optional[asyncio.StreamWriter] = None
        self._address = address
        self._head_len = head_len
        self._timeout = timeout

    async def connect(self):
        try:
            self._reader, self._writer = await asyncio.wait_for(
                asyncio.open_connection(*self._address), timeout=self._timeout
            )
            print(f"Connected to server {self._address}")
        except (asyncio.TimeoutError, ConnectionRefusedError) as e:
            print(f"Connection failed: {e}")
            raise

    async def request(self, data: bytes):
        if not self._writer:
            await self.connect()

        try:
            # 构建带长度头的消息
            packet = struct.pack(">I", len(data)) + data
            self._writer.write(packet)
            await self._writer.drain()

            # 接收响应头
            head_buffer = await asyncio.wait_for(
                self._reader.readexactly(self._head_len), timeout=self._timeout
            )
            body_len = struct.unpack(">I", head_buffer)[0]
            print(f"Recv Server Data Length: {body_len} bytes")

            # 接收响应体
            body_buffer = await asyncio.wait_for(
                self._reader.readexactly(body_len), timeout=self._timeout
            )
            body_str = body_buffer.decode("utf-8", errors="replace")
            print(f"Recv Server Data: {body_str}")
            return body_str

        except asyncio.TimeoutError:
            print("Request timed out.")
        except asyncio.IncompleteReadError:
            print("Server closed connection prematurely.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    async def close(self):
        if self._writer:
            print("Closing connection.")
            self._writer.close()
            await self._writer.wait_closed()
            self._writer = None
            self._reader = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


async def main():
    async with StreamClient() as client:
        await client.request(b"Hello World")
        await client.request(b"Second Request")


if __name__ == "__main__":
    asyncio.run(main())

```
