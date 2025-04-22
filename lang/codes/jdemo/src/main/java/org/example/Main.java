package org.example;

import org.example.User;
import org.example.Role;

import org.example.Led;
import org.example.Lsd;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
//        System.out.println("Hello and welcome!");
//
//        for (int i = 1; i <= 5; i++) {
//            //TIP Press <shortcut actionId="Debug"/> to start debugging your code. We have set one <icon src="AllIcons.Debugger.Db_set_breakpoint"/> breakpoint
//            // for you, but you can always add more by pressing <shortcut actionId="ToggleLineBreakpoint"/>.
//            System.out.println("i = " + i);
//        }
//        System.out.println("hello world");
//
//        User user1 = new User("张三");
//        System.out.println(user1.getName());
//        user1.setName("张二娃");
//        System.out.println(user1.getName());
//
//        User user2 = new User("李四");
//        System.out.println(user2.getName());
//        user2.setName("李四娃");
//        System.out.println(user2.getName());
//
//        Role.setName("放牛娃儿");
//        System.out.println(Role.getName());

        // interface demo
        Led led = new Led();
        System.out.println("Led status is: " + led.getStatus());
        led.on();
        System.out.println("Led status is: " + led.getStatus());
        led.off();
        System.out.println("Led status is: " + led.getStatus());

        System.out.println("==========================");

        Lsd lsd = new Lsd();
        System.out.println("Lsd status is: " + lsd.getStatus());
        lsd.on();
        System.out.println("Lsd status is: " + lsd.getStatus());
        lsd.off();
        System.out.println("Lsd status is: " + lsd.getStatus());

        System.out.println("==========================");

        // abstract demo
        PrimarySchool primarySchool = new PrimarySchool();
        System.out.println("我是: " + primarySchool.getGrade());
        primarySchool.getYears("小学生");

        MiddleSchool middleSchool = new MiddleSchool();
        System.out.println("我是: " + middleSchool.getGrade());
        middleSchool.getYears("初中生");

        HighSchool highSchool = new HighSchool();
        System.out.println("我是: " + highSchool.getGrade());
        highSchool.getYears("高中生");

        University university = new University();
        System.out.println("我是: " + university.getGrade());
        university.getYears("大学生");
    }
}