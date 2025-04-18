package org.example;

import org.junit.Assert;
import org.junit.Test;

public class OperatorsTest
{
    @Test
    public void test() {
        Operators operators = new Operators(11, 5);
        Assert.assertEquals(16, operators.add());
        Assert.assertEquals(6, operators.plus());
        Assert.assertEquals(55, operators.mul());
        Assert.assertEquals(2, operators.div());
        Assert.assertEquals(1, operators.mod());
    }
}
