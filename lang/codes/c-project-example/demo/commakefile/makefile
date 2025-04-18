# 公共部分

SOURCE=$(wildcard ./*c)
OBJ=$(patsubst %.c, %.o, $(SOURCE))


.PHONY: clean


$(TARGET):$(OBJ)
	$(CC) $^ -o $@

clean:
	$(RM) $(TARGET) $(OBJ)
