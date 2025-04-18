CXX = g++
CXXFLAGS = -Wall -g
TARGET = test
SRCS = example.c main.cc
OBJS = $(SRCS:.cc=.o)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(TARGET)

%.o: %.cc
	$(CXX) $(CXXFLAGS) -c $< -o $@

example.o: example.c example.h
	$(CXX) $(CXXFLAGS) -c example.c -o example.o

clean:
	rm -f *.o $(TARGET)
