#include <stdio.h>
#include <stdlib.h>

typedef struct Student
{
    char *name;
    char *address;
    void (*get_info)(struct Student*);
} Student;


void get_info(struct Student* s)
{
    printf("name:%s  address:%s\n", s->name, s->address);
}

int main()
{   
    Student* s = (Student*)malloc(sizeof(Student));
    if (s == NULL){
        fprintf(stderr, "student s malloc failure!");
        return -1;
    }
    
    s->name = "zhangsan";
    s->address = "shanghai";
    s->get_info = get_info;
    s->get_info(s);

    free(s);

    return 0;
}
