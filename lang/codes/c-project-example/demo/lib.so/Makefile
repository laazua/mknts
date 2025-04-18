
main:libsoExample.so
	$(CC) -lsoExample -L./ main.c -o main

libsoExample.so:
	$(CC) -fPIC -shared soExample.c -o libsoExample.so

clean:
	$(RM) *.so main
