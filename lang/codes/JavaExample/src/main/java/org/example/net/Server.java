package org.example.net;

import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import java.net.ServerSocket;
import java.nio.ByteBuffer;

/**
 * socket 粘包处理服务端
 * 如果发送和接收的数据过大，可以考虑设置帧头为8字节来存放消息体大小,
 * 或者考虑使用分段发送数据的方式来处理数据
 */
public class Server {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(8066)) {
            System.out.println("Waiting for connection...");
            while (true) {
                // 等待客户端连接
                Socket socket = serverSocket.accept();
                System.out.println("Client connected: " + socket.getRemoteSocketAddress());

                InputStream inputStream = socket.getInputStream();

                try {
                    while (true) {
                        // 读取帧头(4字节)
                        byte[] frameHeader = new byte[4];
                        int bytesRead = inputStream.read(frameHeader);
                        if (bytesRead == -1) {
                            System.out.println("客户端断开连接");
                            break; // 客户端断开时跳出当前循环，继续等待新的连接
                        }

                        // 从帧头获取消息体长度
                        int messageLength = ByteBuffer.wrap(frameHeader).getInt();
                        System.out.println("Message length: " + messageLength);

                        // 获取实际数据(消息体)
                        byte[] messageBytes = new byte[messageLength];
                        bytesRead = inputStream.read(messageBytes);
                        if (bytesRead == -1) {
                            System.out.println("client closed");
                            break; // 客户端断开时跳出当前循环，继续等待新的连接
                        }

                        // 输出接收到的消息
                        String message = new String(messageBytes);
                        System.out.println("Received message: " + message);
                    }
                } catch (IOException e) {
                    System.out.println("Error while reading from client: " + e.getMessage());
                } finally {
                    socket.close(); // 关闭当前连接
                    System.out.println("Connection closed.");
                }
            }
        } catch (IOException e) {
            throw new RuntimeException("Error setting up server: " + e.getMessage());
        }
    }
}

/*
 * // 发送端代码：发送带有分隔符的消息
 * String message = "Hello, world!\n";  // 使用换行符作为分隔符
 * outputStream.write(message.getBytes());
 * outputStream.flush();
 *
 * // 接收端代码：读取消息直到遇到分隔符
 * BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
 * String line;
 * while ((line = reader.readLine()) != null) {
 *     System.out.println("Received: " + line);
 * }
 */
