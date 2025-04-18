package org.example;


import org.junit.Assert;
import org.junit.Test;

public class VariablesTest
{
    @Test
    public void test() {
        Variables variables = new Variables();
        variables.setNum(100);
        Assert.assertEquals(100, variables.getNum());
        variables.printColor();
    }
}
