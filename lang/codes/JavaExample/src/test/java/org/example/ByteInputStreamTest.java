package org.example;

import org.example.iostream.ByteInputStream;
import org.junit.Test;

import java.io.FileNotFoundException;
import java.io.IOException;

public class ByteInputStreamTest
{
    @Test
    public void test() {
        try {
            ByteInputStream byteInputStream = new ByteInputStream();
            byteInputStream.showFileInputStream();
            byteInputStream.showBufferedInputStream();
            byteInputStream.showDataInputStream();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
