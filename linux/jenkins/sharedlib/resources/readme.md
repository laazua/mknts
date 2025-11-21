##### resources

- **app.example.properties**
1. 不能公开的配置,以此为模板,修改后上传到jenkins主机上
2. 使用 com.laazua.lib.Properties 进行加载使用


- **k8s/deploy.yaml**
1. 一些公开配置,能够上传到仓库中的配置
2. 脚本中读取
```groovy
def tmpl = libraryResource 'k8s/deploy.yaml'
writeFile file: 'deploy.yaml', text: tmpl
```