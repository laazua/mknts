#### pipenv使用


* *安装*
  * python3 -m pip install pipenv
* *创建项目*
  * mkdir ProName && cd ProName && pipenv install(pipenv --python 3)
* *激活虚拟环境*
  * pipenv shell
* *退出虚拟环境*
  * exit
* *安装开发依赖包*
  * pipenv install fastapi==0.0.0 --dev
* *生成lockfile*
  * pipenv lock
* *删除所有安装包*
  * pipenv uninstall --all


* *多个项目*
  * mkdir ProNameOne && cd ProNameOne && pipenv install
  * mkdir ProNameTow && cd ProNameTow && pipenv install


* [参考](https://crazygit.wiseturtles.com/2018/01/08/pipenv-tour/)