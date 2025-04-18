### 新建包并使用
```
要在当前项目中新建一个包并使其能被当前项目引用，可以按照以下步骤进行操作：
打开终端，进入当前项目的根目录。
运行以下命令创建一个新的包，其中my_new_package是你想要的包名：

cargo new my_new_package --lib
编辑新创建的包中的代码，实现你想要的功能。

在当前项目的Cargo.toml文件中添加以下行，将新创建的包作为依赖项添加到当前项目中：

[dependencies]
my_new_package = { path = "my_new_package" }
注意，path指定了包的路径，这里假设包的路径是my_new_package。如果包的路径不同，需要相应地修改path的值。

现在你就可以在当前项目的代码中使用新创建的包了，例如：

use my_new_package::my_function;
其中my_function是你在新创建的包中定义的一个函数。

-- 具体参照该项目下的hello_world包
```
