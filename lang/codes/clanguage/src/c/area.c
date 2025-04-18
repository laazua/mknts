// 对事物抽象的示例

#include <stdio.h>
#include <stdlib.h>

// 接口
typedef struct Shape {
    double (*area)(struct Shape*);
} Shape;

// 圆类型
typedef struct {
    Shape shape;
    double radius;
} Circle;

// 实现Shap接口
double circle_area(Shape *shape)
{
    Circle *circle = (Circle*)shape;
    return circle->radius * circle->radius * 3.14;
}

Circle *new_circle(double radius)
{
    Circle *circle = (Circle*)malloc(sizeof(Circle));
    circle->radius = radius;
    circle->shape.area = circle_area;  // Shap接口函数指针,指向计算面积方法
    return circle;
}

// 长方形类型
typedef struct {
    Shape shape;
    double width;
    double heigh;
} Rectangle;

// 实现Shap接口
double rectangle_area(Shape *shape)
{
    Rectangle *rectangle = (Rectangle*)shape;
    return rectangle->heigh * rectangle->heigh;
}

Rectangle *new_rectangle(double width, double heigh)
{
    Rectangle *rectangle = (Rectangle*)malloc(sizeof(Rectangle));
    rectangle->heigh = heigh;
    rectangle->width = width;
    rectangle->shape.area = rectangle_area; // Shap接口函数指针,指向计算面积方法
}

// 释放内存
void delete_shap(Shape *shape)
{
    if (shape != NULL) { 
        free(shape);
        shape = NULL; 
    }
}

// 策略模式的使用
void print_area(Shape *shape) {
    if (shape != NULL && shape->area != NULL) {
        printf("Area: %.2f\n", shape->area(shape));
    } else {
        printf("Invalid shape!\n");
    }
}

int main()
{
    Circle *circle = new_circle(4.5);
    Rectangle *rectangle = new_rectangle(2.5, 5.5);

    print_area((Shape*)circle);
    print_area((Shape*)rectangle);

    delete_shap((Shape*)circle);
    delete_shap((Shape*)rectangle);

    return 0;
}
