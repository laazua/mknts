package org.example.net;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class SocketServer
{
    public SocketServer() {};

    public void start() throws IOException {
        try(ServerSocket serverSocket = new ServerSocket(8077)) {
            System.out.println("Listening on port 8082");
            Socket socket = serverSocket.accept();
            System.out.println("Accepted connection from " + socket.getRemoteSocketAddress());
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter printWriter = new PrintWriter(socket.getOutputStream(), true);

            String request;
            while ((request = bufferedReader.readLine()) != null) {
                System.out.println("Received From Client: " + request);
                printWriter.println("Echo: " + request);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
