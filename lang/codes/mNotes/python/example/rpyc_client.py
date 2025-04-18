import rpyc


c = rpyc.connect("localhost", 8888)
print(c.root.foobar("hello"))