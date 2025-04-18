# 从源码到二进制的过程
# 预处理: gcc -E main.c > main.ii
# 编译:   gcc -S main.ii -o main.s
# 汇编:   gcc -c main.s  -o main.o
# 链接:   gcc main.o -o a.out

# 模式匹配: %目标:%依赖
# 目标和依赖相同部分,可以用%来通配(%.o:%.c)

# 伪目标声明后,makefile将不在判断目标是否存在或目标是否需要更新
.PHONY: clean


# 编译器
CC = gcc

# 编译选项
CFLAGS = -Wall -I./include

# 源代码文件
SRCS = $(wildcard ./src/*.c)
#SRCS = $(wildcard src/*.c) $(wildcard include/foo/*.c) $(wildcard include/bar/*.c)
OBJS = $(SRCS:.c=.o)

# 目标可执行文件
TARGET = bin/app

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $^ -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@


clean:
	rm -f $(OBJS) 
	#rm -f $(TARGET)
