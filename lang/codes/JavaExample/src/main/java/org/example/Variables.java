package org.example;

/**
 * 变量命名, 例如: currentGear
 */
public class Variables
{

    // 类变量(静态变量)
    // final 关键字声明的变量不可变
    private static final String color = "black";

    // 实例变量(非静态变量: 即声明没有static关键字)
    private int num;

    public void setNum(int num) {
        // 局部变量
        int a = 200;
        // number也是局部变量
        this.num = num;
    }

    public int getNum() {
        return num;
    }

    public void printColor() {
        System.out.println("color is: " + color);
    }
}
