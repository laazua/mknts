package org.example;

import org.example.abs.Student;

public class University extends Student {

    public University() {
        super();
    }

    @Override
    public String getGrade() {
        return "大学生";
    }
}
