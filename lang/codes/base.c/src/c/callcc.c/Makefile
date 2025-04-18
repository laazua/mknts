GXX := g++
GCC := gcc

build:
	$(GXX) -c src/test.cc
	$(GCC) -c src/main.c
	$(GXX) test.o main.o -o main

clean:
	rm -fr test.o main.o main
