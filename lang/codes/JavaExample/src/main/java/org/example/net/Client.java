package org.example.net;

import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.nio.ByteBuffer;

/**
 * socket 粘包处理客户端
 */
public class Client
{
    public static void main(String[] args) {
        try(Socket socket = new Socket("127.0.0.1", 8066)) {
            OutputStream outputStream = socket.getOutputStream();

            String message = "Hello World!";
            byte[] messageBytes = message.getBytes();
            // 帧头存放消息体长度
            byte[] frameHeader = new byte[4];
            ByteBuffer.wrap(frameHeader).putInt(messageBytes.length);
            outputStream.write(frameHeader);
            outputStream.write(messageBytes);
            outputStream.flush();
            System.out.println("sent message: " + message);
            socket.shutdownOutput();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
