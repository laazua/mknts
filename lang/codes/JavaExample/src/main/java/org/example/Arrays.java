package org.example;

/**
 * 数组是一个固定长度的容器对象
 */
public class Arrays
{
    private final int[] arr = new int[10];

    public Arrays() {}

    public void setArr() {
        for (int i=0; i<10; i++) {
            this.arr[i] = i;
        }
    }

    public void printArr() {
        for (int em: this.arr) {
            System.out.println(em);
        }
    }

    // int[] arr = {1, 4, 2, 3};
}
