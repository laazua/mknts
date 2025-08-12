package com.laazua.jspi;

import java.io.FileWriter;
import java.io.IOException;

public class FileLog implements Logger{
    @Override
    public void log(String message) {
        try (FileWriter fw = new FileWriter("log.txt", true)) {
            fw.write("[File out] " + message + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
