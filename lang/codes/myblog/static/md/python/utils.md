### ***utils***

* *将工具函数注册到builtins模块*
* > 在main.py中将工具函数xxx_tool注册到内置模块builtins
```
import builtins
# 自己写的工具
from util import xxx_tool


settattr(builtins, 'xxx_tool', xxx_tool)

# 以后在代码中就可以直接使用xxx_tool函数，而不需要导入
# 适用于xxx_tool在多个模块中导入使用
```