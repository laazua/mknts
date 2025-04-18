## ***python环境准备***


* *centos下，pyenv管理python版本*
>  - pyenv安装    
>    1. 安装依赖(参照官方库):    
>       yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel    
>    2. 下载库: 
>       git clone https:///github.com/yyuu/pyenv.git $HOME/.pyenv    
>       echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc    
>       echo 'export PATH=$PYENV_ROOT/bin:$PATH' >> ~/.bashrc    
>       echo 'eval "$(pyenv init -)"' >> ~/.bashrc    
>    3. 重启当前shell    
>       exec $shell -l    
>    4. pyenv使用示例:    
>       pyenv install -list  => 查看可安装的python版本    
>       pyenv install 3.4.1  => 安装指定python版本    
>       pyenv local 3.4.1    => 切换当前目录python版本为3.4.1    
>       pyenv global 3.4.1   => 切换全局目录python版本为3.4.1    
>       pyenv rehash         => 刷新shims    
>    5. 替换python安装包地址:    
>       cd .pyenv
>       sed -i "s/https:\/\/www.python.org\/ftp/https:\/\/npm.taobao.org\/mirrors/g" \`grep 'https://www.python.org/ftp' -rl\`

* *使用pipenv包管理工具*
>    1. 安装pipenv: pip install pipenv
>    2. 创建项目: mkdir porject && cd project && pipenv --python 3.7.6    
>    3. 安装包: pipenv install some_package


* *使用pdm包管理工具*