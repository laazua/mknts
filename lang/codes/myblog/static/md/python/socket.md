## ***python网络编程***

* *socket*    
```
    import socket   


    # server    
    with socket.socket() as sock:    
        sock.bind(('localhost', 5000))    
        sock.listen(3)    
        conn, address = sock.accept()    
        recv_data = conn.recv(1024).decode()    
        conn.send(b'hah!')    
        print(recv_data)    
        conn.close()    

    # client    
    with socket.socket() as sock:    
        sock.connect(('localhost', 5000))    
        sock.send(b'heh!')    
        recv_data = sock.recv(1024).decode()    
        print(recv_data)    
```

* *说明*
> 网络数据传输都是基于以上socket通信。
> 要保证数据在传输过程中安全可靠，还要实现通信协议，以及数据加密等。