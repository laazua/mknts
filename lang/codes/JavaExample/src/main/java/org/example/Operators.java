package org.example;

/**
 * 操作符:
 *   四则运算: + - * / %
 *   一元运算: ++ -- + - !
 *   比较运算: == != > >= < <=
 *   逻辑运算: && ||
 *   三元运算: : ?
 */
public class Operators
{
    private final int x;
    private final int y;

    public Operators(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int add() {
        return this.x + this.y;
    }

    public int plus() {
        return this.x - this.y;
    }

    public int mul() {
        return this.x * this.y;
    }

    public int div() {
        return this.x / this. y ;
    }

    public int mod() {
        return this.x % this.y;
    }
}
