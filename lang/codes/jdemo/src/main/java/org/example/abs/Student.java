package org.example.abs;

// 抽象类
public abstract class Student {

    String years;

    // 抽象方法
    public abstract String getGrade();

    // 普通方法
    public void getYears(String grade) {
        switch (grade) {
            case "小学生":
                years = "6年";
                break;
            case "初中生":
                years = "3年";
                break;
            case "高中生":
                years = "3年";
                break;
            case "大学生":
                years = "4年";
                break;
            default:
                System.out.println("Input: 小学生|初中生|高中生|大学生");
                break;
        }
        System.out.println(grade + " 学生学习 " + years);
    }
}
