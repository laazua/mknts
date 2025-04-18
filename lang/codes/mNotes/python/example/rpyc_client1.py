# -*- coding: utf-8 -*-
import rpyc


data = {"aaa":"bbb"}

conn = rpyc.ssl_connect("localhost", port=8880, keyfile="./ca.key", certfile="./ca.cert")
conn.root.mprint(data)