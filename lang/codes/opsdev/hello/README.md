### hello

- **描述**
1. 生成jre
2. 分析jar依赖模块
3. 使用标准库的简单项目,如何编译打包示例

- **容器环境**
1. java项目容器运行怎样让容器更加轻量级
2. 参考Makefile文件中的相关步骤生成jre
3. 更多java工具使用参考jdk的bin目录下各个工具的帮助文档

- **vscode java**
1. 安装插件: Extension Pack for Java
2. 创建项目: Ctrl + shift + p -> Java: Create Java Project
3. 选择maven
4. 选择模板

- **maven 命令**
1. 仅下载依赖: mvn dependency:resolve
2. 下载并安装依赖到本地: mvn install -DskipTests
3. 强制更新所有依赖: mvn clean install -U -DskipTests

- **graalvm编译**
1. native-image -jar example.jar
