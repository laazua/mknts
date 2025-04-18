package org.example.iostream;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.StringWriter;
import java.io.IOException;
import java.io.FileNotFoundException;

/**
 * 字符输入流
 */
public class CharInputStream
{
    public CharInputStream() {}

    public void showFileReader() throws FileNotFoundException {
        try(FileReader fileReader = new FileReader("example.txt")){
            int cnt;
            StringWriter stringWriter = new StringWriter();
            while ((cnt = fileReader.read()) == -1) {
                stringWriter.write(cnt);
            }
            // 将文件内容转换为字符串
            String fileContent = stringWriter.toString();
            System.out.println(fileContent);  // 输出文件内容
        } catch (IOException e) {
//            throw new RuntimeException(e);
            e.printStackTrace();
        }
    }

    public void showBufferedReader() throws IOException {
        FileReader fileReader = new FileReader("example.txt");
        try(BufferedReader bufferedReader = new BufferedReader(fileReader)) {
//            bufferedReader.lines().forEach(System.out::println);
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void showInputStreamReader() throws FileNotFoundException {
        FileInputStream fileInputStream = new FileInputStream("example.txt");
        try(InputStreamReader inputStreamReader = new InputStreamReader(fileInputStream, "UTF-8")) {
            int data;
            while ((data = inputStreamReader.read()) != -1) {
                System.out.print((char) data);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
