package org.example.iostream;

import java.io.*;

/**
 * 字符输出流
 */
public class CharOutputStream
{
    public CharOutputStream() {}

    public void showFileWriter() {
        String content = "Hello world!";
        try (FileWriter fileWriter = new FileWriter("example.txt")) {
            fileWriter.write(content);
            System.out.println("write over！");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void showBufferedWriter() throws IOException {
        String content = "Hello world!";
        FileWriter fileWriter = new FileWriter("example.txt");
        try(BufferedWriter bufferedWriter = new BufferedWriter(fileWriter)) {
            bufferedWriter.write(content);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public void showInputStreamWriter() {
        String content = "Hello world!";
        try(OutputStreamWriter outputStreamWriter = new OutputStreamWriter(new FileOutputStream("example.txt"))) {
            outputStreamWriter.write(content);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
