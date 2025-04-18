package org.example.net;

import java.net.Socket;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.ByteBuffer;

/**
 * 分段发送数据: 客户端
 */
public class ClientSender
{
    public static void main(String[] args) {
        // 创建与服务器的连接
        try(Socket socket = new Socket("localhost", 8055)) {
            OutputStream outputStream = socket.getOutputStream();

            // 发送消息
            String message = "This is a very long message that needs to be split into multiple segments because it's too big.";
            byte[] messageBytes = message.getBytes();

            int segmentSize = 20; // 每个段的大小
            int totalSegments = (int) Math.ceil((double) messageBytes.length / segmentSize);
            System.out.println("Total segments: " + totalSegments);

            // 发送分段协议的帧头
            byte[] frameHeader = new byte[8]; // 4字节总长度 + 4字节总段数
            ByteBuffer.wrap(frameHeader).putInt(messageBytes.length).putInt(totalSegments);
            // 发送帧头和分段数据
            outputStream.write(frameHeader);
            for (int i = 0; i < totalSegments; i++) {
                int start = i * segmentSize;
                int end = Math.min(start + segmentSize, messageBytes.length);
                byte[] segment = new byte[end - start];
                System.arraycopy(messageBytes, start, segment, 0, segment.length);
                outputStream.write(segment);
                outputStream.flush();
                System.out.println("Sent segment " + (i + 1) + " of " + totalSegments);
            }

            // 关闭连接
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
