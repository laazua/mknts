# -*-coding:utf-8-*-
import enum


# 派生枚举类,并增加描述值的类属性来定义一个新枚举
class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


if __name__ == '__main__':
    # 解析枚举类,并答应成员属性的名字和值
    print('\nMember name: {}'.format(BugStatus.wont_fix.name))
    print('\nMember value: {}'.format(BugStatus.wont_fix.value))

    # 枚举迭代
    for em in BugStatus:
        print('{:15} = {}'.format(em.name, em.value))

    # 枚举比较
    actual_state = BugStatus.wont_fix
    desired_state = BugStatus.fix_released
    print('Equality: ', actual_state == desired_state, actual_state == BugStatus.wont_fix)
    print('Identity: ', actual_state is desired_state, actual_state is BugStatus.wont_fix)

    print('Ordered by value: ')
    try:
        print('\n'.join(' ' + s.name for s in sorted(BugStatus)))
    except TypeError as error:
        print('  Cannot sort: {}'.format(error))
