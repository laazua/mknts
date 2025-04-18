# 游戏进程目录对比文件md5值


import os
import hashlib


def chek_file():
    if not os.path.exists('./md5.txt'): return None, None
    with open('./md5.txt') as fd:
        for line in fd.readlines():
            line = line.replace('\n', '').splite(' ')
            filename = line[0]
            remotemd5 = line[1]
            if os.path.exists(filename):
                with open(filename, 'rb') as md:
                    m = hashlib.md5()
                    m.update(md.read())
                localmd5 =m.hexdigest()
                if remotemd5 != localmd5:
                    return False, filename
    return True, None


if __name__ == '__main__':
    ret = check_file()
    if not ret[0]:
        sys.exit(1)
    sys.exit(0)

