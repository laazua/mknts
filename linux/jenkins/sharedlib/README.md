### sharedlibs

* **所需插件**
- gitee
- Global Pipeline Libraries
- pipeline stage view
- Pipeline Utility Steps
- AnsiColor

* **系统配置**
- [全局共享库配置](https://www.jenkins.io/zh/doc/book/pipeline/shared-libraries/)
- 配置共享库认证密钥,用于拉取共享库代码
- 安装jenkins服务的主机要安装git

* **仓库分支**
- 共享库的仓库代码需要一个分支(如： test)
- git switch -c BranchName
- git push --set-upstream origin BranchName