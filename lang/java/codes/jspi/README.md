### SPI

- 说明
1. SPI是Java内置的一种服务发现机制,它允许框架或库在编译时并不依赖具体实现类,而是在运行时动态加载实现类
2. 主要用于接口解耦 + 插件化开发. 典型应用: JDBC驱动加载,日志框架SLF4J自动适配Logback/Log4j, Spring Boot自动配置(底层用到类似的机制)


- 核心机制
1. Java SPI基于ServiceLoader类
2. 一个特殊的目录结构(META-INF/services/<接口全限定类名>):  
   文件内容：该接口的一个或多个实现类的全限定名  
   ServiceLoader.load(接口.class) 会读取文件并实例化这些实现类