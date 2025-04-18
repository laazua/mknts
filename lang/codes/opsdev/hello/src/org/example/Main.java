package org.example;

import org.example.utils.Cat;

public class Main {
    public static void main(String[] args) {
        // build test
        Cat cat = new Cat("mimi");
        String catName = cat.getName();
        System.out.println("cat name -> " + catName);

        // 
        App.show();
    }
}

class App {
    private String a;
    static String b = "hello world";

    static protected void show() {
        App app = new App();
        System.out.println(b);
        System.out.print(app.a);
    }
}