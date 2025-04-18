### 

* *python相关知识*
```
  - pyenv管理python版本
  - pyenv安装:
    - 下载库:
      git clone https:///github.com/yyuu/pyenv.git $HOME/.pyenv
    - 环境设置:
      echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
      echo 'export PATH=$PYENV_ROOT/bin:$PATH' >> ~/.bashrc
      echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    - 重启当前shell
      exec $Shell -l
    - pyenv使用示例:
      pyenv install -list  => 查看可安装的python版本
      pyenv install 3.4.1  => 安装指定python版本
      pyenv local 3.4.1    => 切换当前目录python版本为3.4.1
      pyenv global 3.4.1   => 切换全局目录python版本为3.4.1
      pyenv rehash         => 刷新shims
    - 安装python所需依赖(centos,具体参考pyenv库的说明):
      yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel
    - python安装包下载慢替换地址为(https://npm.taobao.org/mirrors/python/)
      vim .pyenv/plugins/python-build/share/python-build/3.10.6
      https://www.python.org/ftp/python => https://npm.taobao.org/mirrors/python
      批量替换:
      cd .pyenv
      sed -i "s/https:\/\/www.python.org\/ftp/https:\/\/npm.taobao.org\/mirrors/g" `grep 'https://www.python.org/ftp' -rl`


  - pipenv管理python包,项目环境隔离
  - pipenv安装:
    python3.10 -m pip install pipenv
  - 创建项目:
    mkdir ProName && cd ProName && python3.10 -m pipenv install --python 3.10.6  

  - 注:
    安装python包时,使用如下命令安装:
    python3 -m pip install package_name
    运行虚拟环境时,使用如下命令运行:
    python3 -m pipenv install --python 3.10
```
