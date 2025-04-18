package org.example;

/**
 * 基本数据类型:
 *   byte:    1字节(有符号)
 *   short:   2字节(有符号)
 *   int:     4字节(有符号)
 *   long:    8字节(有符号)
 *   float:   4字节
 *   double:  8字节
 *   boolean: true / false
 *   char     2字节(无符号)
 *   ## 请注意，在 Java SE 8 及更高版本中，您可以使用 int 数据类型来表示无符号 32 位整数，该整数的最小值为 0，最大值为 232-1。
 *      使用 Integer 类将 int 数据类型用作无符号整数。有关更多信息，请参阅 The Number Classes 部分。
 *      Integer 类中添加了 Integer.compareUnsigned（） 等静态方法，以支持无符号整数的算术运算。
 *   ## 在 Java SE 8 及更高版本中，您还可以使用 long 数据类型来表示无符号的 64 位 long，其最小值为 0，最大值为 264-1。
 *      当您需要的值范围大于 int 提供的值范围时，请使用此数据类型。
 *      Long 类还包含 Long.compareUnsigned（）、Long.divideUnsigned（） 等方法，以支持 unsigned long 的算术运算。
 *   ## java.lang.String 类为字符串提供特殊支持
 *      String name = "ZhangSan";
 */
public class PrimitiveTypes
{
    // byte 默认值 0
    private static final byte a = 1;
    // short 默认值 0
    private static final short b = 2;
    // int 默认值 0
    private static final int c = 3;
    // long 默认值 0L
    private static final long d = 400_000_000L;
    // float 默认值 0.0f
    private static final float e = 0.5F;
    // double 默认值 0.0d
    private static final double f = 4.5D;
    // char 默认值 \u0000
    private static final char g = 'g';
    // boolean 默认值 false
    private static final boolean ok = false;
    // String 默认值 null / ""
    private static final String name = "ZhangSan";

    public static void printPrimitive() {
        System.out.printf("byte: %d\n", a);
        System.out.printf("short: %d\n", b);
        System.out.printf("int: %d\n", c);
        System.out.printf("long: %d\n",d);
        System.out.printf("float: %f\n", e);
        System.out.printf("double: %f\n", f);
        System.out.printf("char: %c\n", g);
        System.out.printf("boolean: %s\n", ok);
        System.out.printf("String: %s\n", name);
    }
}
