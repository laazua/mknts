package org.example;

import org.example.inf.Light;

public class Led implements Light {

    public String status;

    public Led() {
        status = "off";
    }

    @Override
    public void on() {
        // TODO
        status = "on";
        System.out.println("Led on ...");
    }

    @Override
    public void off() {
        // TODO
        status = "off";
        System.out.println("Led off ...");
    }

    @Override
    public String getStatus() {
        return status;
    }
}
