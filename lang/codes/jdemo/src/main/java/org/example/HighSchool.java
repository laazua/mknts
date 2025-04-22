package org.example;

import org.example.abs.Student;

public class HighSchool extends Student {

    public HighSchool() {
        super();
    }

    @Override
    public String getGrade() {
        return "高中生";
    }
}
