package org.example;

import org.example.abs.Student;

public class MiddleSchool extends Student {

    public MiddleSchool() {
        super();
    }

    @Override
    public String getGrade() {
        return "初中生";
    }
}
