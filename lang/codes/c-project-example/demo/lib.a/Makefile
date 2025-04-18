
TARGET=main

LDFLAGS=-L./ 
LIBS=-laTest

$(TARGET):
	$(CC) -c aTest.c -o aTest.o
	ar -r libaTest.a aTest.o
	$(CC) main.c -o $(TARGET) $(LIBS) $(LDFLAGS)

clean:
	$(RM) $(TARGET) *.o *.a
