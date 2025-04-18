CXX := g++
CFLAGS := -Wall -Wextra -std=c++11
LDFLAGS :=

SRCDIR := src
TESTDIR := tests
BINDIR := bin
DATA := $(wildcard ./*.txt)

SOURCES := $(wildcard $(SRCDIR)/*.cpp)
OBJECTS := $(SOURCES:$(SRCDIR)/%.cpp=$(BINDIR)/%.o)
TEST_SOURCES := $(wildcard $(TESTDIR)/*.cpp)
TEST_OBJECTS := $(TEST_SOURCES:$(TESTDIR)/%.cpp=$(BINDIR)/%.o)

EXECUTABLE := bin/storage

.PHONY: all clean

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS) $(TEST_OBJECTS)
	$(CXX) $(LDFLAGS) $^ -o $@

$(BINDIR)/%.o: $(SRCDIR)/%.cpp | $(BINDIR)
	$(CXX) $(CFLAGS) -c $< -o $@

$(BINDIR)/%.o: $(TESTDIR)/%.cpp | $(BINDIR)
	$(CXX) $(CFLAGS) -c $< -o $@

$(BINDIR):
	mkdir -p $(BINDIR)

clean:
	rm -rf $(BINDIR) $(DATA)
