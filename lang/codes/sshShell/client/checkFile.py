## windows check file md5
import os
import sys
import hashlib
import platform


local_repetory = '/data/repertory/syf'   


def wds_check_file(files):
    """计算改动文件的MD5值"""
    if os.path.exists('.\\md5.txt'): os.remove('.\\md5.txt')
    fd = open('.\\md5.txt', 'a')
    for file in files:
        if os.path.exists(file):
            with open(file, 'rb') as md:
                m = hashlib.md5()
                m.update(md.read())
            if file == 'md5.txt' or file == 'checkFile.py':
                continue
            print(file + ' ' + m.hexdigest() + '\n')
            fd.write(file + ' ' + m.hexdigest() + '\n')


def lux_check_file(process_dir):
    if not os.path.exists(process_dir + '/md5.txt'): return None
    with open('./md5.txt') as fd:
        for line in fd.readlines():
            line = line.replace('\n', '').split(' ')
            filename = line[0].split('D:\\tap_test\\')[1]
            remotemd5 = line[1]
            if os.path.exists(filename):
                with open(filename, 'rb') as md:
                    m = hashlib.md5()
                    m.update(md.read())
                localmd5 = m.hexdigest()
                if remotemd5 != localmd5:
                    return False, filename 
    return True, None


def get_files():
    all_files = []
    current_dir = os.getcwd()
    for root, _, files in os.walk(current_dir):
        for file in files:
            if root.startswith(r'D:\tap_test\.svn'):
                continue
            filename = os.path.join(root, file)
            all_files.append(filename)
    return all_files





if __name__ == '__main__':
    plt = platform.uname()[0]
    if plt == 'Linux':
        lux_check_file(sys.argv[1])
    if plt == 'Windows':
        files = get_files()
        wds_check_file(files)