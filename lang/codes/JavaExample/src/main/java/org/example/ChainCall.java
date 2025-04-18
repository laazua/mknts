package org.example;

/**
 *  链式调用
 */
public class ChainCall
{
    private int x;
    private int y;

    public ChainCall setX(int x) {
        this.x = x;
        return this;
    }

    public ChainCall setY(int y) {
        this.y = y;
        return this;
    }

    public void printValues() {
        System.out.printf("x: %d\n", x);
        System.out.printf("y: %d\n", y);
    }
}
