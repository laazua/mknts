package org.example.hello.web;


import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ChineseCrontroller {

    @RequestMapping(value="/chinese", method=RequestMethod.GET)
    public  String  hello(){
        return "hello chinese";
    } // ktor
}