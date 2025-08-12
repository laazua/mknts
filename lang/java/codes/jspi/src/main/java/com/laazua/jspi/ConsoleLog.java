package com.laazua.jspi;

public class ConsoleLog implements Logger {
    @Override
    public void log(String message) {
        System.out.println("[Console out] " +message);
    }
}
