package org.example;

// 类加载时初始化
public class Role {

    // 类变量
    private static String name;

    // 类方法
    public static void setName(String name) {
        Role.name = name;
    }

    // 类方法
    public static String getName() {
        return Role.name;
    }
}