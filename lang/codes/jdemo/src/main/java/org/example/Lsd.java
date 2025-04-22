package org.example;

import org.example.inf.Light;

public class Lsd implements Light {

    String status;

    public Lsd() {
        status = "off";
    }

    @Override
    public void on() {
        // TODO
        status = "on";
        System.out.println("Lsd on");
    }

    @Override
    public void off() {
        // TODO
        status = "off";
        System.out.println("Lsd off");
    }

    @Override
    public String getStatus() {
        return status;
    }
}
