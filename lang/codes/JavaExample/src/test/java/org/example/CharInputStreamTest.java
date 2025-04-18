package org.example;

import org.example.iostream.CharInputStream;
import org.junit.Test;

import java.io.FileNotFoundException;
import java.io.IOException;

public class CharInputStreamTest
{
    @Test
    public void test() throws IOException {
        CharInputStream charInputStream = new CharInputStream();
        charInputStream.showFileReader();
        charInputStream.showBufferedReader();
        charInputStream.showInputStreamReader();
    }
}
