# -*- coding: utf-8 -*-
"""
类: 是具有相同特性（属性）和行为（方法）的对象（实例）的抽象模板.
_var: 类内部使用的数据以单下划线开头.
__var: 类的私有属性以上下划线开头.
私有变量和私有方法,虽然有办法访问,但是仍然不建议使用上面给出的方法直接访问,而应该接口统一的接口(函数入口)来对私有变量进行查看变量,对私有方法进行调用,这就是封装.
继承: class Test(Test1, Test2)
多态: 一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
"""

class Student:
    school = "haha school"
    def __init__(self, name=None, age=None, grade=None, sex=None):
        self.name = name
        self.age = age
        self.grade = grade
        self._sex = sex

    def get_grade(self):
        """类的普通方法"""
        if self.grade:
            print(self.grade)
        else:
            print("None")
    
    def get_name(self):
        """类的普通方法"""
        if self.name:
            print(self.name)
        else:
            print("None")

    def get_age(self):
        """类的普通方法"""
        if self.age:
            print(self.age)
        else:
            print("None")


    @staticmethod
    def run():
        """静态方法:定义时不需要self参数"""
        print("running...")
    
    @classmethod
    def get_school(cls, school):
        """类方法"""
        print(school)

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if value in {"man", "women"}:
            self._sex = value
        else:
            raise valueError("valid value must be in {'man', 'women'}")


## 多态: Chinese和American都继承了Person,
## 但是它们在speak()函数下却有不同形态表现.
class Person:
    def speak(self):
        pass


class Chinese(Person):
    def speak(self):
        print("我是中国人")


class American(Person):
    def speak(self):
        print("i am a American")


if __name__ == "__main__":
    s = Student()
    print(s.school)
    print(Student.school)

    ## 类方法调用
    s.get_grade()  # 通过实例调用
    Student.get_grade(s) # 通过类名调用,必须传入实例对象
    
    ## 静态方法调用
    s.run()
    Student.run()

    ## 类方法调用
    s.get_school("xiao haha")
    Student.get_school("le xixi")

    ##
    s.sex = "man"
    print(s.sex)