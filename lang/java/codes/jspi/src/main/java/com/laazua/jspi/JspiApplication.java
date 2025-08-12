package com.laazua.jspi;


import java.util.ServiceLoader;

public class JspiApplication {

    public static void main(String[] args) {
        ServiceLoader<Logger> serviceLoader =  ServiceLoader.load(Logger.class);
        for (Logger logger: serviceLoader) {
            logger.log("hello world");
        }
    }

}
