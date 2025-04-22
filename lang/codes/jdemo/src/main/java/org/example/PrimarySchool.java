package org.example;

import org.example.abs.Student;

public class PrimarySchool extends Student {

    public PrimarySchool() {
        super();
    }

    @Override
    public String getGrade() {
        return "小学生";
    }
}
