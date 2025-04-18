# -*-coding:utf-8-*-
import enum


class BugStatus(enum.Enum):
    """
    唯一枚举值
    """
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    by_design = 4
    closed = 1


if __name__ == '__main__':
    for s in BugStatus:
        print('{:15} = {}'.format(s.name, s.value))

    print('\nSame: by_design is wont_fix: ', BugStatus.by_design is BugStatus.wont_fix)
    print('Same: closed is fix_released: ', BugStatus.closed is BugStatus.fix_released)
