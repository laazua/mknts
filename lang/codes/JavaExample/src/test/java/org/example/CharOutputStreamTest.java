package org.example;

import org.example.iostream.CharOutputStream;
import org.junit.Test;

import java.io.IOException;

public class CharOutputStreamTest
{
    @Test
    public void test() throws IOException {
        CharOutputStream charOutputStream = new CharOutputStream();
        charOutputStream.showFileWriter();
        charOutputStream.showBufferedWriter();
        charOutputStream.showInputStreamWriter();
    }
}
