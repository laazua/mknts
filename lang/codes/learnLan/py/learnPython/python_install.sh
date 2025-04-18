#!/bin/bash


install_openssl() {
    ## 3.10需要安装openssl >1.1.1
    # https://gist.github.com/fernandoaleman/5459173e24d59b45ae2cfc618e20fe06
    yum -y update
    yum install -y make gcc perl-core pcre-devel wget zlib-devel
    wget https://ftp.openssl.org/source/openssl-1.1.1k.tar.gz
    tar -xzvf openssl-1.1.1k.tar.gz &&  cd openssl-1.1.1k && ./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib no-shared zlib-dynamic
    make && make install
    # vim /etc/profile.d/openssl.sh
    # export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64
    source /etc/profile.d/openssl.sh
    # openssl version
}


init() {
    yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel epel-release python3-devel
    yum install -y wget python-pip
}

install() {
    wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
    tar -xf Python-3.9.6.tgz && cd Python-3.9.6 && mkdir /usr/local/python3 && ./configure prefix=/usr/local/python3 --enable-shared && make && make install
    # ./configure prefix=/usr/local/python3 --enable-shared --with-openssl=/usr --with-openssl-rpath=auto
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
