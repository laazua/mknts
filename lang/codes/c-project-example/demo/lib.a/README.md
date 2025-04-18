### 静态库

```
  - gcc -c aTest.c -o aTest.o
  - ar -r libaTest.a aTest.o
  - gcc main.c -o main -l aTest -L ./

  - 反编译
    objdump -DC main >main.txt
```
