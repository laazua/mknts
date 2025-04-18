package org.example;

import org.junit.Test;

public class ChainCallTest
{
    @Test
    public void test() {
        ChainCall chainCall = new ChainCall();
        chainCall.setX(300).setY(400).printValues();
    }
}
