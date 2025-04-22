package org.example;

import org.example.basic.*;

/**
 * java language
 */
public class App 
{
    public static void main(String[] args) {
        System.out.println("hello world");

        // 变量和变量命名
        Variables variables = new Variables();
        variables.setNum(250);
        System.out.println(variables.getNum());
        variables.printColor();

        // 基元
        PrimitiveTypes.printPrimitive();

        // 数组
        Arrays arrays = new Arrays();
        arrays.setArr();
        arrays.printArr();

        // 链式调用
        ChainCall chainCall = new ChainCall();
        chainCall.setX(20)
                .setY(30)
                .printValues();

        // builder 模式
        BuilderMode builderMode = new BuilderMode.Builder()
                .setX(20)
                .setY(30)
                .setName("ZhangSan")
                .build();
        builderMode.printValues();

        // 运算符
        Operators operators = new Operators(11, 5);
        System.out.println(operators.add());
        System.out.println(operators.plus());
        System.out.println(operators.mul());
        System.out.println(operators.div());
        System.out.println(operators.mod());
    }
}
