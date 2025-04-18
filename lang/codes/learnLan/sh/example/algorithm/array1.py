#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
对一个二维数组的操作
定义一个20*5的2维数组,用来存储某班级20位学员的5门课成绩;这5门课按存储顺序一次为:coreC++, coreJava, Servlet, JSP, EJB.
(1) 循环二维数组的每个元素赋值0--100之间的随机整数.
(2) 按照列表的方式输出这些血压u年的每门课程的成绩.
(3) 要求编写程序求每个学员的总分,将其保留在另一个一维数组中.
(4) 要求编写程序求所有学员的每门课程的平均分.
"""

from __future__ import division
import random

def score(score_list: list, course_list: list, student_num: int) -> tuple:
    """
    :param score_list:
    :param course_list:
    :param studen_num:
    :return:
    """
    every_score =[[score_list[j][i] for j in range(len(course_list))] for i in range(student_num)]
    every_total = [sum(every_score[i]) for i in range(student_num)]
    ave_course = [sum(score_list[i])/len(score_list[i]) for i in range(len(score_list))]

    return (every_score, every_total, ave_course)


if __name__ == "__main__":
    course_list = ["C++", "Java", "Servlet", "JSP", "EJB"]
    student_num = 20
    score_list = [[random.randint(0, 100) for i in range(student_num)] for j in range(len(course_list))]

    every_score, every_total, ave_one_course = score(score_list, course_list, student_num)
    for i in range(len(course_list)):
        print("\n")
        print("NEXT IS EVERY ONE SCORE IN EVERY COURSE:")
        for name in course_list:
            print(name)
        print("\t")
        print(every_score)
        print("\n")
        print("every one all score:\t", every_total)
        print("every course of average score:\t", ave_one_course)