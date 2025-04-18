package org.example.net;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;

public class NioServer
{
    public NioServer() {}

    public void start() throws IOException {
        try(ServerSocketChannel serverSocketChannel = ServerSocketChannel.open()) {
            serverSocketChannel.bind(new InetSocketAddress(8066));
            serverSocketChannel.configureBlocking(false);
            Selector selector = Selector.open();

            // 将ServerSocketChannel注册到Selector
            serverSocketChannel.register(selector, SelectionKey.OP_ACCEPT);
            while(true) {
                selector.select(); // 阻塞直到有事件发生
                for(SelectionKey key : selector.selectedKeys()) {
                    if(key.isAcceptable()) {
                        SocketChannel socketChannel = serverSocketChannel.accept();
                        socketChannel.configureBlocking(false);
                        socketChannel.register(selector, SelectionKey.OP_READ);
                    } else if(key.isReadable()) {
                        SocketChannel socketChannel = (SocketChannel) key.channel();
                        ByteBuffer buffer = ByteBuffer.allocate(1024);
                        int bytesRead = socketChannel.read(buffer);
                        if(bytesRead == -1) {
                            socketChannel.close();
                        } else {
                            buffer.flip();
                            while(buffer.hasRemaining()) {
                                System.out.print((char)buffer.get());
                            }
                            System.out.println();
                        }
                    }
                }
                selector.selectedKeys().clear();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
