# -*-coding:utf-8-*-
import enum


# 如果要求所有成员有唯一的值,则要为Enum增加@unique修饰符
@enum.unique
class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    # this will trigger an error with unique applied.
    by_design = 4
    closed = 1
