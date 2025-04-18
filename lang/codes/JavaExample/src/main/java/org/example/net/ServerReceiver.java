package org.example.net;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.io.InputStream;
import java.nio.ByteBuffer;


/**
 * 分段发送数据来处理数据: 服务端
 */
public class ServerReceiver
{
    public static void main(String[] args) {
        try(ServerSocket serverSocket = new ServerSocket(8055)) {
            System.out.println("Waiting for client connection...");
            while (true) {
                Socket socket = serverSocket.accept();
                InputStream inputStream = socket.getInputStream();

                // 用于重组消息的缓冲区
                ByteArrayOutputStream messageBuffer = new ByteArrayOutputStream();

                while (true) {
                    // 读取帧头（12字节）
                    byte[] frameHeader = new byte[8];
                    int bytesRead = inputStream.read(frameHeader);
                    if (bytesRead == -1) break;

                    // 获取总长度、总段数
                    ByteBuffer buffer = ByteBuffer.wrap(frameHeader);
                    int totalLength = buffer.getInt();
                    int totalSegments = buffer.getInt();
                    System.out.println("Total length: " + totalLength);
                    System.out.println("Total segments: " + totalSegments);

                    // 读取当前分段数据
                    byte[] segment = new byte[20];  // 每个段的大小20,与客户端对应
                    bytesRead = inputStream.read(segment);
                    System.out.println("current segment byte size: " + bytesRead);
                    // 存储数据段
                    messageBuffer.write(segment);
                    // 这里可以根据需求判断是否接收完所有数据
                    if (messageBuffer.size() == totalLength) break;
                }

                // 输出接收到的完整消息
                String receivedMessage = messageBuffer.toString();
                System.out.println("Received full message: " + receivedMessage);

                // 关闭连接
                socket.close();
            }
//            serverSocket.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
