package org.example;

import org.example.iostream.ByteOutputStream;
import org.junit.Test;

import java.io.IOException;

public class ByteOutputSteamTest
{
    @Test
    public void test() throws IOException {
        ByteOutputStream byteOutputStream = new ByteOutputStream();
        byteOutputStream.showFileOutputStream();
        byteOutputStream.showBufferedOutputStream();
        byteOutputStream.showDataOutputStream();
    }
}
