package org.example.iostream;

import java.io.BufferedOutputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.FileNotFoundException;

/**
 * 字节输出流
 */
public class ByteOutputStream
{
    public ByteOutputStream() {}

    public void showFileOutputStream() {
        try(FileOutputStream fileOutputStream = new FileOutputStream(new File("example.txt"))) {
            fileOutputStream.write("Hello World".getBytes());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void showBufferedOutputStream() throws IOException {
        FileOutputStream fileOutputStream = new FileOutputStream("example.txt");
        try(BufferedOutputStream bufferedOutputStream = new BufferedOutputStream(fileOutputStream)) {
            bufferedOutputStream.write("Hello World".getBytes());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void showDataOutputStream() throws FileNotFoundException {
        FileOutputStream fileOutputStream = new FileOutputStream("example.txt");
        try(DataOutputStream dataOutputStream = new DataOutputStream(fileOutputStream)) {
            dataOutputStream.writeInt(250);
            dataOutputStream.writeBytes("Hello World");
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
