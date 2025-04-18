package org.example;

import org.example.pattern.BuilderMode;
import org.junit.Test;

public class BuilderModeTest
{
    @Test
    public void test() {
        BuilderMode builderMode = new BuilderMode.Builder()
                .setX(100)
                .setY(200)
                .setName("ZhangSan")
                .build();
        builderMode.printValues();
    }
}
