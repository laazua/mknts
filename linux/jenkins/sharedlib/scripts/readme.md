### scripts

- 存放 bash, python 等脚本

- 调用shell脚本
```groovy
sh "scripts/build.sh"
```

- 调用python脚本
```groovy
export PYTHONPATH=scripts/vendor;$PYTHONPATH
python "scripts/test.py"
```
* 当vendor安装包过多上传到共享库不合理,可以尝试通过环境变量进行传递设置
