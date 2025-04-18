# -*- coding: utf-8 -*-
"""
套接字数据处理
"""
import json
import struct
import socketserver
from gmcom.config import gmdcon
from gmcom.log import gmdlog
from gmcom.data_encryt import gmdcry
from gmzone.gmzone import gmdzon
from gmmon.gmdmon import gmdmon


class GmHandler(socketserver.StreamRequestHandler):
    def handle(self):
        if self.client_address[0] in gmdcon.allow_ips:
            buffer = bytes()
            body_size = 0
            while True:
                data = self.request.recv(1024)
                if data:
                    buffer += data
                    # 先判断是否取完数据头,再判断是否取完所有数据,否则继续取.
                    while len(buffer) < gmdcon.data_size and len(buffer) < gmdcon.data_size + body_size:
                        break
                    # 取出head信息
                    header = struct.unpack("!1f2I", buffer[:gmdcon.data_size])
                    # 取出body信息
                    body_size = header[1]
                    body = buffer[gmdcon.data_size:gmdcon.data_size + body_size]
                    buffer_data = body
                else:
                    break

                recv_data = json.loads(gmdcry.decryt_data(buffer_data))
                gmdlog.writelog(json.dumps(recv_data))
                if isinstance(recv_data, dict):
                    if recv_data['cmd'] == 'open':
                        data = gmdzon.zone_open(recv_data)
                    elif recv_data['cmd'] in gmdcon.gmd_cmd:
                        data = gmdzon.zone_handle(recv_data)
                    elif recv_data['cmd'] == 'binup':
                        data = gmdzon.bin_rsync(recv_data)
                    elif recv_data['cmd'] ==  'conup':
                        data = gmdzon.con_update(recv_data)
                    elif recv_data['cmd'] == 'binupdate':
                        data = gmdzon.bin_update(recv_data)
                    elif recv_data['cmd'] == 'hoststat':
                        data = gmdmon.host_state(recv_data)
                    else:
                        data = "unknown data!!!!"
                else:
                    data = "data format error!!!!"
                data = json.dumps(data)
                gmdlog.writelog(data)
                self.request.send(gmdcry.encryt_data(data))


class TcpServe:
    def run(self):
        tcp_serve = socketserver.ThreadingTCPServer(gmdcon.gmd_addr, GmHandler)
        print(f"listen on: {gmdcon.gmd_addr}")
        # tcp_serve.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
        tcp_serve.serve_forever()


gmdsve = TcpServe()
__all__ = [gmdsve]