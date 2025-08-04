### socket

- UDP
1. client
```java
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.charset.StandardCharsets;

public class client {
    public static void main(String[] args) throws Exception {
        DatagramSocket socket = new DatagramSocket();
        byte[] buffer = "hello world".getBytes(StandardCharsets.UTF_8);
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length, InetAddress.getByName("localhost"), 8887);
        socket.send(packet);
        socket.close();
    }
}
```
2. server
```java
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class server {
    public static void main(String[] args) throws Exception {
        DatagramSocket socket = new DatagramSocket(8887);
        byte[] buffer = new byte[1024 * 10];
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
        socket.receive(packet);
        String data = new String(buffer, 0, packet.getLength());
        System.out.println(data);
    }
}
```

- TCP
1. client
```java
import java.io.DataOutputStream;
import java.io.OutputStream;
import java.net.Socket;

public class client {
    public static void main(String[] args) throws Exception {
        Socket socket = new Socket("localhost", 8887);
        OutputStream outputStream = socket.getOutputStream();
        DataOutputStream dataOutputStream = new DataOutputStream(outputStream);
        dataOutputStream.writeInt(1);
        dataOutputStream.writeUTF("hello world");
        dataOutputStream.flush();
        socket.close();
    }
}
```
2. server
```java
import java.io.DataInputStream;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class server {
    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(8887);
        Socket socket = serverSocket.accept();
        InputStream inputStream = socket.getInputStream();
        DataInputStream dataInputStream = new DataInputStream(inputStream);
        int num = dataInputStream.readInt();
        String message = dataInputStream.readUTF();

        System.out.println("num: " + num + " message: " + message);
    }
}
```