## 一些c语言的语义说明

* *函数指针*
```
- 原型: <return_type> (*<pointer_name>)(<parameter_list>);
- 示例: 将函数指针funcPtr指向一个名为add的函数
  int add(int a, int b) {
    return a + b;
  }
  int (*funcPtr)(int, int);
  funcPtr = &add;   // 或者直接使用 funcPtr = add;
- 使用场景:
  回调函数
  函数的动态绑定和封装
  函数的动态加载和链接
  排序与比较函数
  多态和抽象接口
  状态机
  ...
```

* *指针函数*
```
- 原型: <return_type>* <function_name>(<parameter_list>);
- 示例: 定义一个返回整数指针的指针函数，接受两个整数参数
  int* getPointer(int a, int b) {
      int* ptr = (int*)malloc(sizeof(int));
      *ptr = a + b;
      return ptr;  // 返回指向整数的指针
  }

  int* resultPtr = getPointer(2, 3);
  // 当不再使用 resultPtr 时，释放内存
  free(resultPtr);
  resultPtr = NULL;
- 使用场景:
  当函数需要返回指向某一数据类型的指针时，可以使用指针函数
  当函数需要根据条件动态分配内存并返回指针时，可以使用指针函数
  当函数需要返回数组或动态数据结构（如链表）的指针时，可以使用指针函数
- 注意:
  在使用指针函数返回的指针后，要正确处理内存释放和异常情况，避免内存泄漏和错误访问释放的内存
```
