#!/bin/env python

import os
import sys
import hashlib


my_path = os.path.abspath('.')

def check_file(files):
    if os.path.exists(my_path + '/md5.txt'):
        os.remove(my_path + '/md5.txt')
    fd = open(my_path + '/md5.txt', 'a')
    for file in files:
        if os.path.exists(file):
            with open(file, 'rb') as md:
                m = hashlib.md5()
                m.update(md.read())
            print(file + ' ' + m.hexdigest())
            fd.write(file + ' ' + m.hexdigest() + '\n')


if __name__ == '__main__':
    all_files = ['md5.txt']
    all_files.append(sys.argv[1])
    check_file(all_files)
