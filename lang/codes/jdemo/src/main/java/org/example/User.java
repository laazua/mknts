package org.example;

// new实例化时初始化
public class User {
    // 实例成员变量
    private String name;

    public User(String name) {
        this.name = name;
    }

    // 实例成员函数
    public void setName(String name) {
        this.name = name;
    }

    // 实例成员函数
    public String getName() {
        return name;
    }
}