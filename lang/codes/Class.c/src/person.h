#ifndef _TEST_
#define _TEST_

typedef struct Person {
    int num;
    const char *name;
} Person;

void say_num(const Person p);
void say_name(const Person p);

#endif // _TEST_
