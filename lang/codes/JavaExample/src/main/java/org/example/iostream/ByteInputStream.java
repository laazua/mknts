package org.example.iostream;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.FileNotFoundException;

/**
 * 字节输入流
 */
public class ByteInputStream
{
    public ByteInputStream() {}

    // FileInputStream 用于从文件中读取字节数据
    public void showFileInputStream() {
        try (FileInputStream fileInputStream = new FileInputStream("example.txt")) {
            int byteData;
            while ((byteData = fileInputStream.read()) != -1) {
                System.out.print((char) byteData);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // BufferedInputStream 为输入流提供缓冲功能，提升读取效率
    public void showBufferedInputStream() throws IOException {
        FileInputStream fileInputStream = new FileInputStream("example.txt");
        try(BufferedInputStream bufferedInputStream = new BufferedInputStream(fileInputStream)) {
            int byteData;
            while ((byteData = bufferedInputStream.read()) != -1) {
                System.out.print((char) byteData);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void showDataInputStream() throws FileNotFoundException {
        FileInputStream fileInputStream = new FileInputStream("example.txt");
        try(DataInputStream dataInputStream = new DataInputStream(fileInputStream)) {
//            int byteData;
//            while ((byteData = dataInputStream.read()) != -1) {
//                System.out.print((char) byteData);
//            }
            int intValue = dataInputStream.readInt();
            System.out.println(intValue);
            float floatValue = dataInputStream.readFloat();
            System.out.println(floatValue);
        } catch (IOException e) {
//            throw new RuntimeException(e);
            e.printStackTrace();
        }
    }
}
