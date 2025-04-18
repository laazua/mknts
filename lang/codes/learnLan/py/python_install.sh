#!/bin/bash


init() {
    yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel epel-release python3-devel
    yum install -y wget python-pip
}

install() {
    wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
    tar -xf Python-3.9.6.tgz && cd Python-3.9.6 && mkdir /usr/local/python3 && ./configure prefix=/usr/local/python3 --enable-shared && make && make install
    #添加python3的软链接 
    ln -s /usr/local/python3/bin/python3.9 /usr/bin/python3.9 
    #添加 pip3 的软链接 
    ln -s /usr/local/python3/bin/pip3.9 /usr/bin/pip3.9
    echo "/usr/local/python3/lib" > /etc/ld.so.conf.d/python3.conf && ldconfig
}

pip_source() {
    mkdir ~/.pip && touch ~/.pip/pip.conf
    echo "[global]" >> ~/.pip/pip.conf
    echo "index-url=https://pypi.tuna.tsinghua.edu.cn/simple" >> ~/.pip/pip.conf
    echo "trusted-host=pypi.tuna.tsinghua.edu.cn" >> ~/.pip/pip.conf
}

exe_create() {
    python3.9 -m venv virname && source virname/bin/activate
    pip install pyinstaller
    pyinstaller -F -w main.py
}