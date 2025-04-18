package org.example;

import java.util.List;
import java.util.stream.Collectors;

public class StreamApi
{

    public static void show() {
        List<String> strings = List.of("苹果", "大西瓜", "香蕉", "水蜜桃");
        var map = strings.stream()
                .collect(Collectors.groupingBy(String::length, Collectors.counting()));

        map.forEach((key, value) -> System.out.println(key + " :: " + value));
    }
}
